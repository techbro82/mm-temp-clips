"""
investor_stats.py  -  READ ONLY aggregate usage statistics.

Lives outside the repo on purpose. Run it from the repo directory on Render's
Shell tab (where the live Firebase credential already exists):

    cd /opt/render/project/src        # or wherever `ls` shows memory.py
    python /tmp/investor_stats.py
    python /tmp/investor_stats.py --cost-log render_logs.txt     # token averages from saved logs

It only READS: db.collection("users").stream(), db.collection("consents").stream()
and firebase_admin.auth.list_users(). It never writes, never calls Anthropic, and
prints counts, averages and dates only - never an email, name, user id or message text.
Set EXCLUDE_EMAILS="a@x.com,b@y.com" to leave the founder's own accounts out.
"""
import os
import re
import statistics
import sys
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, os.getcwd())

FIREBASE_UID = re.compile(r"^[A-Za-z0-9]{28}$")
TEST_PREFIXES = ("smoketest", "test", "demo", "tmp", "fake")


def _dt(s):
    if not s:
        return None
    try:
        d = datetime.fromisoformat(s)
    except (ValueError, TypeError):
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def _day(d):
    return d.astimezone(timezone.utc).date()


def _sessions(user, key):
    for th in (user.get(key) or {}).values():
        for s in (th.get("sessions") or []):
            yield s


def classify_test(uid, excluded_uids):
    """Return the rule name that makes this id a test/non-customer account, else None."""
    if uid in excluded_uids:
        return "founder email (matched in Firebase Auth)"
    low = uid.lower()
    if low.startswith(TEST_PREFIXES):
        return "id starts with a test prefix"
    if not FIREBASE_UID.match(uid):
        return "id is not Firebase-UID shaped (seed/dev id)"
    return None


def pct(n, d):
    return f"{(100.0 * n / d):.0f}%" if d else "n/a"


def compute(users, consent_ids, auth_rows, exclude_emails):
    """users: {uid: record}; consent_ids: set of uid; auth_rows: list of (uid, email, created_dt) or None."""
    exclude_emails = {e.strip().lower() for e in exclude_emails if e.strip()}
    excluded_uids = set()
    if auth_rows:
        for uid, email, _ in auth_rows:
            if email and email.lower() in exclude_emails:
                excluded_uids.add(uid)
    rule_counts = Counter()
    all_ids = set(users) | set(consent_ids) | {r[0] for r in (auth_rows or [])}
    test_ids = set()
    for uid in all_ids:
        rule = classify_test(uid, excluded_uids)
        if rule:
            rule_counts[rule] += 1
            test_ids.add(uid)

    real_users = {u: r for u, r in users.items() if u not in test_ids}
    real_consents = {u for u in consent_ids if u not in test_ids}
    real_auth = [r for r in (auth_rows or []) if r[0] not in test_ids]

    out = {"excluded_total": len(test_ids), "excluded_by_rule": dict(rule_counts)}
    out["auth_accounts"] = len(real_auth) if auth_rows is not None else None
    out["consented_accounts"] = len(real_consents)
    out["accounts_created"] = len(real_auth) if auth_rows is not None else len(real_consents | set(real_users))
    out["onboarded"] = len(real_users)

    per_user_days, solo_counts, room_counts = {}, [], []
    all_dates, kept, notkept, pending, room_commit = [], 0, 0, 0, 0
    solo_total = room_total = 0
    commit_solo = commit_room = 0
    for uid, u in real_users.items():
        days = set()
        n_solo = n_room = 0
        for s in _sessions(u, "threads"):
            d = _dt(s.get("date"))
            if d:
                days.add(_day(d)); all_dates.append(_day(d))
            n_solo += 1
            if (s.get("commitment") or "").strip():
                commit_solo += 1
                v = s.get("commitment_kept")
                kept += v is True; notkept += v is False; pending += v is None
        for s in _sessions(u, "council_threads"):
            d = _dt(s.get("date"))
            if d:
                days.add(_day(d)); all_dates.append(_day(d))
            n_room += 1
            if (s.get("commitment") or "").strip():
                commit_room += 1
                v = s.get("commitment_kept")
                kept += v is True; notkept += v is False; pending += v is None
        per_user_days[uid] = len(days)
        solo_total += n_solo; room_total += n_room
        if n_solo:
            solo_counts.append(n_solo)
        if n_room:
            room_counts.append(n_room)

    out["accounts_with_a_session"] = sum(1 for v in per_user_days.values() if v >= 1)
    for k in (2, 3, 7):
        out[f"active_{k}plus_days"] = sum(1 for v in per_user_days.values() if v >= k)
    out["solo_sessions"] = solo_total
    out["solo_avg_per_account"] = round(statistics.mean(solo_counts), 2) if solo_counts else None
    out["solo_median_per_account"] = statistics.median(solo_counts) if solo_counts else None
    out["room_sittings"] = room_total
    out["accounts_with_a_room"] = len(room_counts)
    out["commitments_total"] = commit_solo + commit_room
    out["commitments_solo"] = commit_solo
    out["commitments_room"] = commit_room
    out["kept"], out["not_kept"], out["pending"] = kept, notkept, pending
    out["session_date_min"] = str(min(all_dates)) if all_dates else None
    out["session_date_max"] = str(max(all_dates)) if all_dates else None
    created = [_dt(u.get("created_at")) for u in real_users.values()]
    created = [c for c in created if c]
    out["onboarded_date_min"] = str(_day(min(created))) if created else None
    out["onboarded_date_max"] = str(_day(max(created))) if created else None
    if auth_rows is not None and real_auth:
        out["signup_date_min"] = str(_day(min(r[2] for r in real_auth if r[2])))
        out["signup_date_max"] = str(_day(max(r[2] for r in real_auth if r[2])))
    return out


def cost_from_log(path):
    pat = re.compile(r"\[cost\] mode=(\w+) type=(\w+) input_tokens=(\d+) output_tokens=(\d+)")
    agg = {}
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            m = pat.search(line)
            if not m:
                continue
            _, typ, i, o = m.groups()
            a = agg.setdefault(typ, [0, 0, 0])
            a[0] += 1; a[1] += int(i); a[2] += int(o)
    return agg


def print_cost(agg):
    replies = ("solo_reply", "room_seat_reply", "room_closing_reply")
    print("\nToken usage from [cost] log lines (counts only):")
    tot = [0, 0, 0]
    for typ in sorted(agg):
        n, i, o = agg[typ]
        print(f"  {typ:24s} calls={n:6d}  avg_input={i/n:9.1f}  avg_output={o/n:8.1f}")
        if typ in replies:
            tot = [tot[0] + n, tot[1] + i, tot[2] + o]
    if tot[0]:
        print(f"  {'ALL mentor replies':24s} calls={tot[0]:6d}  avg_input={tot[1]/tot[0]:9.1f}  avg_output={tot[2]/tot[0]:8.1f}")


def main():
    if "--cost-log" in sys.argv:
        print_cost(cost_from_log(sys.argv[sys.argv.index("--cost-log") + 1]))
        return
    import memory
    db = memory._init_firestore()
    if db is None:
        print("No Firestore connection - run this on Render's Shell tab, where FIREBASE_CREDENTIALS exists.")
        sys.exit(1)
    users = {}
    for doc in db.collection("users").stream():
        users[doc.id] = memory._migrate(doc.to_dict() or {})
    consent_ids = {doc.id for doc in db.collection("consents").stream()}
    auth_rows = None
    try:
        from firebase_admin import auth
        rows = []
        for u in auth.list_users().iterate_all():
            ts = u.user_metadata.creation_timestamp
            rows.append((u.uid, u.email, datetime.fromtimestamp(ts / 1000, tz=timezone.utc) if ts else None))
        auth_rows = rows
    except Exception as e:
        print(f"(Firebase Auth listing unavailable: {type(e).__name__}; accounts_created falls back to consents + users)")
    r = compute(users, consent_ids, auth_rows, os.environ.get("EXCLUDE_EMAILS", "").split(","))
    try:
        import session
        model, mt = session.MODEL, session.MAX_TOKENS
    except Exception:
        model = mt = "unknown (could not import session.py)"
    n = r["accounts_with_a_session"]
    print("MentorMind aggregate usage  (UTC dates; no personal data)")
    print("=" * 60)
    print(f"Excluded test/founder accounts: {r['excluded_total']}  by rule: {r['excluded_by_rule']}")
    print(f"Accounts created (Firebase Auth):   {r['auth_accounts']}")
    print(f"Accounts that consented (signed in):{r['consented_accounts']}")
    print(f"Accounts created (used below):      {r['accounts_created']}")
    print(f"Completed onboarding (users docs):  {r['onboarded']}")
    print(f"Accounts with >=1 session:          {n}")
    for k in (2, 3, 7):
        c = r[f'active_{k}plus_days']
        print(f"Active on >= {k} distinct days:       {c}  ({pct(c, n)} of accounts with a session, {pct(c, r['onboarded'])} of onboarded)")
    print(f"Solo sessions total:                {r['solo_sessions']}  avg/account={r['solo_avg_per_account']}  median={r['solo_median_per_account']}  (accounts with >=1 solo session only)")
    print(f"Round Table sittings:               {r['room_sittings']}  across {r['accounts_with_a_room']} accounts")
    print(f"Commitments created: {r['commitments_total']} (solo {r['commitments_solo']}, room {r['commitments_room']})  kept={r['kept']}  not_kept={r['not_kept']}  pending={r['pending']}")
    print(f"Session dates:   {r['session_date_min']} to {r['session_date_max']}")
    print(f"Onboarded dates: {r['onboarded_date_min']} to {r['onboarded_date_max']}")
    if "signup_date_min" in r:
        print(f"Sign-up dates:   {r['signup_date_min']} to {r['signup_date_max']}")
    print(f"Model: {model}   solo reply max_tokens: {mt}")
    print("Token usage is NOT stored in Firestore. Re-run with --cost-log <saved Render log file> for averages.")


if __name__ == "__main__":
    main()
