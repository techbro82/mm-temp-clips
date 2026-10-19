# MentorMind, day 12 screens: notes

Source: `web/onboard.html`, `server.py`, `mentors.py`, `retriever.py`, `data/*.json` of techbro82/mentormind (read-only clone, app code untouched).
Rendered in Chromium at 440x956 @3x (PNG 1320x2868), iPhone user agent. Firebase modules and every `/api/*` call were mocked locally; no model, Firestore, payment or production call was made. Google Fonts were loaded from Google.

## How the slider text was produced
- Home page markup: `#wqSection` in `web/onboard.html`. Cards are built by `renderWisdomCarousel(quotes)` from `GET /api/mentor-wisdom`.
- That endpoint returns `_wisdom_sample_today()`, i.e. `_build_wisdom_sample(pool, day)` over `_build_mentor_wisdom()` (`server.py`). I ran those functions unmodified (sliced out of `server.py`, executed outside the app) against `data/*.json` with day = 2026-10-19. Pool: 825 passages; sample: 50 slides from 22 different mentors. No API calls.
- Each card shows: the mentor's `era` line (stored lowercase, uppercased by CSS), the passage, and `— {mentor_display}`. All 50 entries are in `slider-passages.json` (`all_entries`; `one_per_mentor` lists 22).
- The page opens on the middle slide (index 25 of 50, `Math.floor(len/2)`) and auto-advances every 8 s. For the screenshots I used the real ‹ and › buttons to reach slide 20 (Grant) and then 21, 22, 23. The auto-advance timer was disabled by the harness only so a shot could not land mid-slide; the app code is untouched.
- The slide order is day-hashed, so it is the real order for 2026-10-19 and changes daily. Passages are verbatim; slide 23 (Marcus Aurelius) contains the real Greek word εὔμοιρος.

## How the 'A word from your mentor' card was produced
- Code: `home_dashboard()` in `server.py` (the `passage = None ...` block), rendered by `renderNewHome()` into `#hnPassageCard`.
- It needs no model: BM25 (`retriever.Retriever`) over the mentor's corpus using the person's narrative (situation + goal + struggle), 'voice' chunks first, each filtered by `_trim_passage`, the first 3 clean ones kept, one picked by a day hash (`sha256(day + mentor_key)`). I ran that same logic for a sample Alex whose mentor is Epictetus.
- Sample narrative used as the query (my input, not app data): situation "I have to give my first presentation at work next week.", goal "To speak calmly and clearly.", struggle "I dread how it will land.". A different narrative can pick a different passage.
- Result today: heading "A word from your mentor" (source_kind `voice`; "From Epictetus's own story" is used only for `life` chunks), passage:
  > For the future, relying on these opinions, walk about upright, free; not trusting to the size of your body, as an athlete, for a man ought not to be invincible in the way that an ass is.
  attribution "— Epictetus".
- Source: `data/epictetus.json`, chunk index 23 (id `epic-0-0023`, kind `voice`, source "Discourses, trans. George Long", 472 words); the passage is a verbatim sentence from that chunk (checked: it appears in the chunk text unchanged). Full detail in `mentor-card-passage.json`.

## Visible text of each screen

### 01-home-top.png
Fixed top of page, same on all Home shots: hamburger menu button (top left), logo `MentorMind`, then the headline `You've walked with 1 mentor, and you're 2 weeks into your current run.`, then the label `WISDOM, FROM EVERY MENTOR`.
- Era line: `THE UNITED STATES, 1885, WRITING HIS MEMOIRS AS HE WAS DYING`
- Passage: One of mine is that in positions of great responsibility every one should do his duty to the best of his ability where assigned by competent authority, without application or the use of influence to change his position.
- Attribution: `— Ulysses S. Grant`
- Counter: `20 of 50`
- Controls: ‹ , pause (two bars), ›
- Below the slider: stat cards `THIS WEEK / 2 weeks / with Epictetus` and `COMMITMENTS / 0 of 1 / kept, 1 still pending`; `YOUR COMMITMENTS, IN ORDER` begins.

### 02-home-slider-2.png
Fixed top of page, same on all Home shots: hamburger menu button (top left), logo `MentorMind`, then the headline `You've walked with 1 mentor, and you're 2 weeks into your current run.`, then the label `WISDOM, FROM EVERY MENTOR`.
- Era line: `A STOIC SCHOOL AT NICOPOLIS, AROUND 108 AD`
- Passage: But where there is death or exile or pain or infamy, there we attempt to run away, there we are struck with terror.
- Attribution: `— Epictetus`
- Counter: `21 of 50`
- Controls: ‹ , pause (two bars), ›
- Below the slider: stat cards `THIS WEEK / 2 weeks / with Epictetus` and `COMMITMENTS / 0 of 1 / kept, 1 still pending`; `YOUR COMMITMENTS, IN ORDER` begins.

### 03-home-slider-3.png
Fixed top of page, same on all Home shots: hamburger menu button (top left), logo `MentorMind`, then the headline `You've walked with 1 mentor, and you're 2 weeks into your current run.`, then the label `WISDOM, FROM EVERY MENTOR`.
- Era line: `THE UNITED STATES, EARLY 1900S`
- Passage: Very often the man with the moral courage to speak in the open against labor when it is wrong is the only man anxious to do effective work for labor when labor is right.
- Attribution: `— Theodore Roosevelt`
- Counter: `22 of 50`
- Controls: ‹ , pause (two bars), ›
- Below the slider: stat cards `THIS WEEK / 2 weeks / with Epictetus` and `COMMITMENTS / 0 of 1 / kept, 1 still pending`; `YOUR COMMITMENTS, IN ORDER` begins.

### 04-home-slider-4.png
Fixed top of page, same on all Home shots: hamburger menu button (top left), logo `MentorMind`, then the headline `You've walked with 1 mentor, and you're 2 weeks into your current run.`, then the label `WISDOM, FROM EVERY MENTOR`.
- Era line: `THE ROMAN FRONTIER, AROUND 175 AD, ON CAMPAIGN`
- Passage: Let death surprise me when it will, and where it will, I may be εὔμοιρος, or a happy man, nevertheless.
- Attribution: `— Marcus Aurelius`
- Counter: `23 of 50`
- Controls: ‹ , pause (two bars), ›
- Below the slider: stat cards `THIS WEEK / 2 weeks / with Epictetus` and `COMMITMENTS / 0 of 1 / kept, 1 still pending`; `YOUR COMMITMENTS, IN ORDER` begins.

### 05-home-bottom.png (scrolled to the bottom)
Slider is scrolled partly off the top (shows slide "23 of 50", Marcus Aurelius). Visible below it:
- `THIS WEEK` / `2 weeks` / `with Epictetus`
- `COMMITMENTS` / `0 of 1` / `kept, 1 still pending`
- `YOUR COMMITMENTS, IN ORDER` / `Rehearse the opening two minutes aloud, twice.` / `Epictetus · Oct 11, 2026` / `Not yet reviewed`
- `A WORD FROM YOUR MENTOR` / “For the future, relying on these opinions, walk about upright, free; not trusting to the size of your body, as an athlete, for a man ought not to be invincible in the way that an ass is.” / `— Epictetus`  (the label is written "A word from your mentor" in the HTML and uppercased by CSS; curly quotes added by the code)

### 06-chat-grant.png
Logo, `Sign out` button (top right), heading `Ulysses S. Grant`, then the italic notice `MentorMind's mentors are AI, inspired by the writings of real people. They are not the real people, and not therapy or professional advice.`, input placeholder `Say something...` with a microphone icon, button `Send`, buttons `← Back` and `End session`. No messages.

## Computed styles (hex)

### Slider (Home, `#wqSection`)
| Element | Font family | Size | Weight | Text colour | Background | Border | Radius | Padding | Spacing / notes |
|---|---|---|---|---|---|---|---|---|---|
| Section `.wq-section` | Inter, system-ui, sans-serif | 16px | 300 | #ECE3D2 | gradient #0A0D15 to #0E111A to #0B0E17 | none | 20px | 16px 0px 10px 0px | margin 4px / 16px |
| Label `.wq-label` | Inter, system-ui, sans-serif | 10.88px | 500 | #CAA25E | transparent | none | 0px | 0px 0px 0px 0px | letter-spacing 2.5px, uppercase, centred; margin 0 / 8px |
| Slide card `.wq-card.centered` | Inter, system-ui, sans-serif | 16px | 300 | #ECE3D2 | gradient #1B2132 to #141A27 | #8A7444 1px | 16px | 14px 18px 14px 18px | 330x215.7 on this slide; non-centred cards are blurred 5px, scale .84, opacity .35; centred card shadow rgba(0, 0, 0, 0.9) 0px 30px 70px -30px, rgba(216, 166, 87, 0.4) 0px 0px 50.0192px -13.9945px |
| Opening quote mark `.wq-mark` | Cormorant Garamond, serif | 54.4px | 700 | #D8A657 | transparent | none | 0px | 0px 0px 0px 0px | decorative, opacity .14, absolute top -8px left 12px |
| Era / attribution line above passage `.wq-era` | Inter, system-ui, sans-serif | 10.24px | 300 | #CAA25E | transparent | none | 0px | 0px 0px 0px 0px | letter-spacing 2px, uppercase, margin-bottom 4px |
| Passage `.wq-text` | Cormorant Garamond, serif | 16px | 500 italic | #ECE3D2 | transparent | none | 0px | 0px 0px 0px 0px | line-height 22.72px |
| Attribution `.wq-attr` ("— Name") | Cormorant Garamond, serif | 16px | 600 | #F0C479 | transparent | none | 0px | 0px 0px 0px 0px | margin-top 8px |
| Counter `.wq-counter` ("20 of 50") | Inter, system-ui, sans-serif | 12.48px | 300 | #948E7D | transparent | none | 0px | 0px 0px 0px 0px | letter-spacing 0.5px, centred, min-width 64px |
| Arrow buttons `.wq-nav-btn` ‹ › | Arial | 16px | 400 | #CAA25E | #141A27 | #8A7444 1px | 50% | 1px 6px 1px 6px | 30x30 circle, glyphs U+2039 and U+203A, centred, gap 14px; font is the browser's default button font (Arial) |
| Pause button `#wqPause` | Arial | 16px | 400 | #CAA25E | #141A27 | #8A7444 1px | 50% | 1px 6px 1px 6px | 30x30 circle, two-bar SVG 12x12 filled currentColor (rects x2 w3 and x7 w3, height 10), play icon when paused |

Hover on a ‹ / › / pause button (CSS `.wq-nav-btn:hover`): border #D8A657, text #F0C479, background #1B2132. The screenshots were taken with no hover.

### 'A word from your mentor' card (`#hnPassageCard`)
| Element | Font family | Size | Weight | Text colour | Background | Border | Radius | Padding | Spacing / notes |
|---|---|---|---|---|---|---|---|---|---|
| Card `.hn-quote-card` | Inter, system-ui, sans-serif | 16px | 300 | #ECE3D2 | gradient #1B2132 to #141A27 | #2A3245 1px | 14px | 16px 18px 16px 18px | full width on phone (flex 1 1 100%); margin-top 16px on the row |
| Label `.hn-card-label` | Inter, system-ui, sans-serif | 11.2px | 300 | #CAA25E | transparent | none | 0px | 0px 0px 0px 0px | letter-spacing .4px, uppercase |
| Passage `.hn-quote-text` | Cormorant Garamond, serif | 16.32px | 300 italic | #ECE3D2 | transparent | none | 0px | 0px 0px 0px 0px | line-height 1.55; curly quotes added in JS |
| Attribution `.hn-quote-attr` | Inter, system-ui, sans-serif | 11.52px | 300 | #948E7D | transparent | none | 0px | 0px 0px 0px 0px | margin-top 8px |

### Home headline
| Element | Font family | Size | Weight | Text colour | Background | Border | Radius | Padding | Spacing / notes |
|---|---|---|---|---|---|---|---|---|---|
| `.hn-page-headline` | Cormorant Garamond, serif | 29.6px | 500 | #ECE3D2 | transparent | none | 0px | 0px 0px 0px 0px | bold parts (mentor count, weeks) #CAA25E weight 600 |

### Chat screen (`06-chat-grant.png`)
| Element | Font family | Size | Weight | Text colour | Background | Border | Radius | Padding | Spacing / notes |
|---|---|---|---|---|---|---|---|---|---|
| Mentor heading `h1` | Cormorant Garamond, serif | 25.6px | 500 | #ECE3D2 | transparent | none | 0px | 0px 0px 0px 0px | margin 17.152px / 17.152px |
| AI notice `.ai-notice` | Inter, system-ui, sans-serif | 12.16px | 300 italic | #948E7D | transparent | none | 0px | 0px 0px 0px 0px | italic, centred |
| Input `#msg` | Inter, sans-serif | 16px | 300 | #ECE3D2 | #141A27 | #2A3245 1px | 10px | 13px 42px 13px 15px | margin 0px / 0px |
| Send `.act` | Inter, sans-serif | 16px | 500 | #1A1206 | gradient #D8A657 to #8A7444 | none | 11px | 13px 24px 13px 24px | margin 22px / 0px |
| Back `.choice.inline` | Inter, sans-serif | 16px | 400 | #ECE3D2 | gradient #1B2132 to #141A27 | #2A3245 1px | 11px | 14px 16px 14px 16px | margin 0px / 0px |
| End session `.choice.inline` | Inter, sans-serif | 16px | 400 | #ECE3D2 | gradient #1B2132 to #141A27 | #2A3245 1px | 11px | 14px 16px 14px 16px | margin 0px / 0px |

Page background for all shots: #0E111A (`--ink`) with drifting blue/gold ambient glows and gold particles; page text #ECE3D2; body font Inter 16px / 300.

## Things that depend on state I supplied or that the app decides at run time
- **Fake user 'Alex'** and the dashboard numbers on Home (1 mentor, 2-week streak, 1 commitment 'Rehearse the opening two minutes aloud, twice.' dated Oct 11, 2026, not yet reviewed) are mocked; the real values come from the user's record.
- **Slide order and which mentor opens**: day-hashed; the app opens on the middle slide. Grant is slide 20 today.
- **The 'A word' passage** depends on the person's own narrative text and the day; a different person or day can give a different Epictetus passage, or a 'From … own story' heading if a mentor has only memoir chunks.
- **'In your own words' card** (below the mentor card) is hidden because the mock has no past user words.
- **Chat screen**: the italic AI notice shows because Grant is not in the person's 'spoken with' list; it is absent for a mentor they've already sat with. The chat is empty because `/api/session/start` was mocked.
- Home shows a hamburger (mobile nav) instead of 'Sign out' because the sidebar layout is active on that screen.
