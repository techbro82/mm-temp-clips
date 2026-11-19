# MentorMind landing page: current state inventory

Source: `origin/master` at `f677703` (19 Nov 2026). `landing.html` in this folder is that exact committed file (LF line endings, 65,787 bytes).
The live page at https://mentormindhq.com/ matches it, except that the server adds cache-busting `?v=hash` to the image and favicon URLs.
Screenshots were taken from the live page in headless Chrome on 19 Nov 2026, after every animation had finished.
Nothing was submitted or changed: no form was sent, the app was not opened.

## How the page is built
- One file. 1 `<style>` block and 7 inline `<script>` blocks. No CSS or JS file is loaded from the repo.
- Loaded from outside: Google Fonts only (`fonts.googleapis.com` stylesheet, `fonts.gstatic.com` font files). Everything else comes from mentormindhq.com.
- No analytics, ads or tracking scripts.
- Fixed behind everything: 3 blurred glows (`.ambient`) and a particle canvas (`#pageParticles`).
- Page height: about 7,560 px at 1440 wide, about 9,500 px at 390 wide.
- Page order: nav, hero, demo, how it works (with carousel), memory, support/donation, FAQ, footer.

## Sections, in page order

| # | Section | What it is for | Layout |
|---|---|---|---|
| 1 | **Nav + hero** (`.hero`, 100vh) | First impression, one action | Nav is absolute at the top: logo + wordmark left, two buttons right (Sign in outlined, Sign up gold). Headline, one italic line and one button sit in a left column (left 8%, max 28 characters wide) over a full-bleed looping video. On a phone the text is centred, at 44% down. |
| 2 | **Demo** ("A conversation, unhurried") | Shows what a reply feels like | Centred single column. Small caps label, centred serif title, then one glass card (max 860 px): mentor name and era, the "You" message in italics, a typed-out Marcus Aurelius reply (97 words, a hand-written script, not a live reply), a fake input box with mic and a Send button (neither works), and the caption "A glimpse. The real conversation begins when you enter." |
| 3 | **How it works** (`#how-it-works`) | Three steps, then the mentors | Centred label and title; three numbered items in a row (I, II, III); then a full-width carousel of 12 mentor cards (text left over a portrait right), prev, pause and next buttons, and the line "One from each part of life. Many more wait within." |
| 4 | **Memory** ("What sets it apart") | The one differentiator | One centred glass frame (max 820 px) with corner brackets and a gold hairline, a 2-sentence statement, and a small italic line "Return, and they ask what became of your last resolve." |
| 5 | **Support / donation** (`#support`) | Takes one-time gifts | Narrow centred column (max 640 px). In order: gold flame icon, title, intro paragraph; "What a gift actually does" (2 star-bullet items); a 34-word statement ("Somewhere, right now, someone needs...") followed by two real quote cards (Epictetus, Douglass); "Choose what feels right" with 3 equal tier cards; a "your own amount" box; email field and Give button; "Plainly" with a link to /about. Two hidden result states (thank-you, failed). |
| 6 | **FAQ** | Answers doubts | Centred label and title, then 7 accordion rows (max 760 px). |
| 7 | **Footer** | Links and the AI notice | Brand block (logo, tagline, 4 round social icons, @mentormindhq) plus 3 link columns (Explore, Company, Legal); a bottom row with copyright and a tagline; a centred AI notice. Stacks to one column on a phone. |

Section padding is 90 to 170 px top and bottom. Sections 2, 3, 4 and 6 all use the same pattern: a small gold label above a centred serif heading.

## Visual effects and animations

| Effect | Where | Details |
|---|---|---|
| Looping video | Hero background | `hero-desktop-v2.mp4` (1920x1080, 10 s, 3.77 MB) or `hero-phone-v2.mp4` (540x960, 10 s, 866 KB). Autoplay, muted, loop. The phone file is chosen when the window is 700 px wide or less, or the browser has data saver on. Posters: `hero-desktop-poster-v3.jpg`, `hero-phone-poster-v3.jpg`. |
| Darkening veils | Over the hero video | `.veil-left`: a left-to-right gradient, 96% to 0% navy over 72% of the width. `.veil-vign`: a soft vignette. At 820 px or less the left veil becomes a top-to-bottom gradient. |
| Drifting glows | Fixed, whole page | 3 blurred circles (blur 60px, opacity .5): blue 640x520 top right (22 s drift), dark blue 520x460 bottom left (26 s), gold 360x360 centre (9 s pulse). |
| Gold particles | Fixed canvas, whole page | About 1 dot per 9,000 px of screen (about 144 on desktop, about 36 on a phone), drifting up, redrawn about 30 times a second, paused when the tab is hidden. |
| Hero text fade-up | Hero | Headline lines at 0.5 s and 0.85 s, subline at 1.2 s, button at 1.5 s; each rises 16 px over 1.2 s. |
| Scroll reveals | 10 elements | Fade up 26 px over 1 s when 18% visible (demo label, title and card; pillars label, title and row; the four support blocks). Runs once. |
| Typed demo reply | Demo card | Word by word, 95 ms a word, each word blurs in. Starts when 50% of the card is visible. **It replays: 7 seconds after it finishes it starts again, as long as the card is on screen.** |
| Word-by-word reveal | Memory statement (140 ms a word, 24 words) and the "Somewhere, right now" line (90 ms a word, 34 words) | Each word fades in from a 4 px blur. Memory also draws its gold rule to 120 px and fades in a 640 px radial glow. |
| Corner brackets and hairline | Memory frame | Two 46 px bracket corners and a 1 px gold gradient rule. |
| Glass blur | Nav buttons (4px), demo card (6px), memory frame (6px) | `backdrop-filter`. |
| Carousel | Section 3 | 12 slides, 560x320 px on desktop and 340x280 px on a phone, 30 px gap. The centred slide is sharp; the others are blurred 6px, scaled to 82% and faded to 45%. Moves every 4.2 s, wraps around, has prev, pause and next buttons (46 px round). **It starts on slide 7 (Carnegie), not slide 1.** Order: Marcus Aurelius, Augustine, Epictetus, Douglass, Franklin, Grant, Carnegie, Darwin, Emerson, Thoreau, Addams, Cicero. |
| Flames and embers | Support section | A 3-layer flickering SVG flame (loops of 2.6, 2.1 and 1.7 s) on the intro (7 rising ember dots) and on each tier card (4 each). Flame size grows with the tier ($2 small, $25 large). |
| Tier cards | Support section | Hover: lifts 4 px with a gold glow. Selected: gold border, the flame scales to 120% with a bright glow. Selection is client-side only; nothing is sent until Give. |
| Gold gradient buttons | Sign up, hero, Give | Top-to-bottom gold gradient, lifts and glows on hover. |
| Accordion | FAQ | Plus icon turns into a minus, answer slides open over 0.5 s, one open at a time. |
| Logo | Nav and footer | Two stacked images (book, flame). The flame sways about 1.4 degrees every 3.6 s and a soft glow pulses behind it. This is the only motion that respects `prefers-reduced-motion`. |

The star bullets in the support list are a text symbol (a four-point star). The social icons and flames are inline SVG.

## Colours (hex)
- Page background `#0e111a`; raised card `#1b2132` to `#141a27`; borders `#2a3245`
- Gold `#d8a657` (main), `#caa25e` (soft), `#8a7444` (dim), `#f0c479` (bright, flames and quote names)
- Parchment text `#ece3d2`; dim text `#a9a290`; faint text `#948e7d`
- Button text `#1a1206`; error text `#d98a7a`
- Glows: blue `rgba(63,90,140,.5)`, dark blue `rgba(40,52,80,.55)`, gold `rgba(216,166,87,.10)`

## Fonts and sizes (measured on the live page; desktop / phone)
Headings use Cormorant Garamond (400 to 600, plus italics). Body uses Inter (300 to 500). Body text is 300 weight in parchment-dim.

| Element | Font | Desktop | Phone | Colour |
|---|---|---|---|---|
| Hero headline | Cormorant | 64 px, 500 | 40 px | #ece3d2 (2nd line gold italic) |
| Hero subline | Cormorant italic | 21.6 px | 16.8 px | #a9a290 |
| Section titles | Cormorant | 54 px, 500 | 35 px | #ece3d2 |
| Small caps labels | Inter | 16.8 px, 500, 3 px spacing | same | #d8a657 |
| Memory statement | Cormorant | 48 px | 32 px | #ece3d2 (one phrase gold italic) |
| Support title | Cormorant | 40 px | 30 px | #ece3d2 |
| FAQ title / question | Cormorant | 48 px / 21.6 px | 32 px / 21.6 px | #ece3d2 |
| Demo reply | Inter | 20.5 px, 300 | same | #ece3d2 |
| Carousel name / blurb | Cormorant 600 / Inter | 30 px / 14.7 px | same | #ece3d2 / #a9a290 |
| Body paragraphs | Inter | 15.7 to 16.3 px, 300 | same | #a9a290 |
| Quote card text / era | Cormorant italic / Inter | 14.7 px / **9.9 px** | same | #ece3d2 / #caa25e |
| Tier amount | Cormorant | 30 px | same | #caa25e |
| Footer links / labels | Inter | 15.2 px / 12.5 px | same | #a9a290 / #caa25e |
| AI notice | Inter | 12.5 px | same | #948e7d |

## Images and video (all from the repo's `web/` folder)
- Video: `hero-desktop-v2.mp4`, `hero-phone-v2.mp4`
- Posters: `hero-desktop-poster-v3.jpg` (1920x1080), `hero-phone-poster-v3.jpg` (540x960)
- Logo: `brand/logo-book-sm.webp` and `brand/logo-flame-sm.webp` (nav and footer, layered); `logo-mark.png` (favicon only)
- 12 mentor portraits, each 1240x692, 80 to 92 KB: `mentors/mortality.jpeg` (Marcus Aurelius), `faith.jpeg` (Augustine), `adversity.jpeg` (Epictetus), `freedom.jpeg` (Douglass), `craft.jpeg` (Franklin), `leadership.jpeg` (Grant), `wealth.jpeg` (Carnegie), `science.jpeg` (Darwin), `thinking.jpeg` (Emerson), `nature.jpeg` (Thoreau), `service.jpeg` (Addams), `friendship.jpeg` (Cicero). All 12 are the same composition: a marble bust in a glowing gold arch on navy. None is lazy-loaded.
- No other images. Flames, social icons, speaker and mic icons are inline SVG.
- Cold load on desktop, measured: 25 requests, about 5.1 MB (video 3.77 MB, images 1.17 MB, fonts 0.12 MB). I did not measure a cold phone load; expect roughly 2 MB (866 KB video plus about 1 MB of portraits).

## What the pre-launch lock changes (live right now: lock is ON)
- On load the page asks `/api/prelaunch/info`. Live answer: `locked: true`, form `https://tally.so/r/kbbEYo`.
- When locked, one thing changes: the hero button text goes from "Get started" to **"Join the founding list"**, and clicking it opens the form in a new tab instead of going to /app. The selector is `.hero .cta .btn-gold` and the code lives in the last inline script.
- Nothing else on the page changes. Sign in and Sign up in the nav, and the footer Sign in, still go to /app. While locked, the server refuses new accounts and sends them to `/closed` ("We open soon.").
- If the request fails, or the form address is not https, the button stays "Get started".
- **The founding list form is a plain external Tally link** (opened in a new tab). It is not embedded and it is not our own form.
- Donations are not affected by the lock.

## Other things the page does that cost something
- `/api/public/mentor-quote/epictetus` and `/douglass` are fetched on load for the two quote cards. If either fails, its card is simply not shown.
- `/api/public/donate/init` runs on Give; `/api/public/donate/verify` runs when someone returns from Paystack. The thank-you and failed states appear only after that return, so the `-FORCED` screenshots show them made visible by hand. No payment was started.

## Things that do not work well, or look broken, on a phone
Measured at 390 wide; there is no horizontal scroll and no console error.
1. **Demo card is cramped.** It keeps its desktop padding (44 px sides), so the reply sits in a column about 230 px wide and runs to over 20 lines at 20 px. The section is 2,009 px tall, 2.4 screens. The fake input ("Speak plainly...") wraps to two lines next to the Send button.
2. **Stray space in the memory statement:** "compound into a relationship , the way..." The comma is its own animated word with a space before it. Shows at both widths; on a phone the statement also breaks over about 10 lines.
3. **Tiny text:** quote-card era label 9.9 px, the demo "You" label 10.9 px, the era under the mentor name 11.8 px, form label and footer labels 12.5 px.
4. **Small tap targets:** Sign in and Sign up are 34 px tall (74 and 79 px wide); footer link rows are 25 px tall; "Read more about why this exists" is 19 px tall.
5. **Carousel text over the portrait:** on a phone the text panel covers 72% of the card and the last words of each blurb run under the bust. The carousel also advances by itself every 4.2 s and starts on slide 7.
6. **The demo and the carousel never stop on their own.** The demo restarts every ~17 s while visible. Only the logo respects reduced motion.
7. **Weight and work:** the glows, the particle canvas, 3 blurred glass panels and endless flame loops all run together. I did not measure frame rate on a real phone, so this is a risk, not a finding.
8. **Landscape and tablets (561 to 820 px):** not captured.

Not tested: a real phone or Safari; the checkout; tap behaviour.

## Screenshots in this folder
Naming: `desktop-NN-section.png` and `phone-NN-section.png`, in page order. Sections taller than the screen have letters (a, b, c...) in scroll order, with a 60 px overlap.
- `01` nav + hero. Desktop has two: `01` at the video's first frame and `01b` mid-video (5.5 s, where the golden burst peaks). Phone has one, at the first frame.
- `02` demo, `03` how it works + carousel (held on slide 1), `04` memory, `05` support/donation, `06` FAQ, `07` footer.
- `05x` donation with the $10 tier selected. `06x` FAQ with the first answer open.
- `05y ... -FORCED` the thank-you and failed states, made visible by hand.
- `desktop-full.png` (1440 x 7740) and `phone-full.png` (589 x 15500; scaled to 75.6% because a 2x capture would pass Chrome's size limit).
- `_capture-report.json` holds the raw measurements (section positions, computed styles, console output, request lists). Its phone network totals are not a cold load (the browser cache was warm), so use the figures in this file.
