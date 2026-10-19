# MentorMind Home page, set B: notes

Rendered from the app's real `web/onboard.html` (commit 2f36e0f) in Chromium, 440x956 @3x (PNGs 1320x2868), iPhone user agent, locale en-US, timezone UTC. Firebase modules and every `/api/*` call were mocked; no model, Firestore, Paystack or Anthropic call. App code unchanged; nothing committed or pushed.

## Files and scrollY (CSS px; page height 1654, viewport 956, max scrollY 698)
| File | scrollY | Slider counter |
|---|---|---|
| home-scroll-01.png | 0 | 20 of 50 |
| home-scroll-02.png | 450 | 20 of 50 |
| home-scroll-03.png | 698 | 20 of 50 |
| slider-pos-20.png | 0 | 20 of 50 |
| slider-pos-21.png | 0 | 21 of 50 |
| slider-pos-27.png | 0 | 27 of 50 |
| slider-pos-29.png | 0 | 29 of 50 |
| slider-pos-34.png | 0 | 34 of 50 |
| slider-pos-39.png | 0 | 39 of 50 |

Scroll series: steps of 450 CSS px, then the final step to the very bottom (698). Consecutive shots overlap by 506/956 = 53% (450 to 450) and 708/956 = 74% (450 to 698). In the scroll series the slider is paused on position 20. The hamburger button is fixed on screen, so it appears over content as the page scrolls.

## Slider positions (paused with the app's own pause button; the pause icon shows as a play triangle)
Passages and era lines are the real ones from `slider-passages.json` (`all_entries`, by position). Era lines are uppercased by CSS.
- slider-pos-20.png: counter `20 of 50`; era `THE UNITED STATES, 1885, WRITING HIS MEMOIRS AS HE WAS DYING`; "One of mine is that in positions of great responsibility every one should do his duty to the best of his ability where assigned by competent authority, without application or the use of influence to change his position."; attribution `— Ulysses S. Grant`
- slider-pos-21.png: counter `21 of 50`; era `A STOIC SCHOOL AT NICOPOLIS, AROUND 108 AD`; "But where there is death or exile or pain or infamy, there we attempt to run away, there we are struck with terror."; attribution `— Epictetus`
- slider-pos-27.png: counter `27 of 50`; era `CONCORD, MASSACHUSETTS, 1845 TO 1854`; "Philanthropy is almost the only virtue which is sufficiently appreciated by mankind."; attribution `— Henry David Thoreau`
- slider-pos-29.png: counter `29 of 50`; era `ANCIENT CHINA, BY TRADITION THE 6TH CENTURY BC`; "When wealth and honours lead to arrogancy, this brings its evil on itself."; attribution `— Lao Tzu`
- slider-pos-34.png: counter `34 of 50`; era `TUSKEGEE, ALABAMA, 1901`; "I believe that one always does himself and his audience an injustice when he speaks merely for the sake of speaking."; attribution `— Booker T. Washington`
- slider-pos-39.png: counter `39 of 50`; era `NEW ENGLAND, MID-1800S`; "Life is a festival only to the wise."; attribution `— Ralph Waldo Emerson`

## Exact visible text
Headline: `You've walked with 2 mentors, and you're 3 weeks into your current run.`

Stat card:
```
THIS WEEK
3 weeks
with Epictetus
```
Stat card:
```
COMMITMENTS
1 of 5
kept, 3 still pending
```
Commitments panel label: `YOUR COMMITMENTS, IN ORDER`

Commitment rows (oldest first):
1.
```
1
Write down one small thing to finish each morning.
Benjamin Franklin · Sep 28, 2026
Kept
```
2.
```
2
Rehearse the opening two minutes aloud, twice.
Epictetus · Oct 5, 2026
Not kept
```
3.
```
3
Send one question to a colleague I admire.
Epictetus · Oct 8, 2026
Not yet reviewed
```
4.
```
4
Finish one task fully before opening the next.
Epictetus · Oct 12, 2026
Not yet reviewed
```
5.
```
◆
Take a ten-minute walk before the meeting.
Epictetus · Oct 15, 2026
Not yet reviewed
```
A word from your mentor card (as rendered):
```
A WORD FROM YOUR MENTOR
“But a tranquil and happy life contains nothing so sure as continuity and freedom from obstacle.”
— Epictetus
```
Raw text nodes: label `A word from your mentor` (uppercased by CSS to A WORD FROM YOUR MENTOR), passage `“But a tranquil and happy life contains nothing so sure as continuity and freedom from obstacle.”` (the code adds the curly quotes), attribution `— Epictetus`.

## Things to know
- **Kept commitment in the list:** the real server's `home-dashboard` leaves kept commitments OUT of `commitment_timeline` (it only returns ones not yet kept). This mock includes the kept one, as you asked, so the list shows 5 rows; a real account with this history would show 4 rows plus the '1 of 5' card.
- **Card wording** ('1 of 5' / 'kept, 3 still pending') and the status labels ('Kept', 'Not kept', 'Not yet reviewed') are the app's own strings, produced by the app code from the mocked counts (kept 1, not kept 1, total 5, pending 3).
- **Word card passage:** exactly as you gave it. It is a real Epictetus passage: `data/epictetus.json`, chunk index 174, as returned by the app's own passage filter (see `mentor-card-candidates.json`).
- **Mocked state:** user Alex, the 2 mentors (Epictetus, Benjamin Franklin), 3-week streak, the 5 commitments and dates are supplied by me from your spec; the 'In your own words' card is hidden.
- The slider's 8 s auto-advance was disabled in the test harness as a safeguard; the pause button was also pressed for real.
