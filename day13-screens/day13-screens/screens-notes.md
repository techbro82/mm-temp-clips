# MentorMind day 13 screens: notes

Rendered from the app's real `web/onboard.html` (commit 2f36e0f) in Chromium, 440x956 @3x (PNGs 1320x2868), iPhone user agent. Firebase modules and every `/api/*` call were mocked; no model, Firestore, Paystack or Anthropic call. App code unchanged; nothing committed or pushed. Mock user: Alex, alex@example.com, sign-in method 'Email and password'. Screens 1 and 2 use a signed-out mock (the sign-up gate only shows when signed out); screens 3 to 5 use the signed-in mock.

Text below is the rendered `innerText`, line by line. CSS uppercases nothing on these screens except where noted.

## 01-signup-consent.png (sign-up mode of #authGate, checkbox NOT ticked)
```
MentorMind
The counsel of the ages, kept for you.
Sign in
Sign up
show
Create account
I confirm I am 18 or over and agree to the Terms of Service and Privacy Policy.
or
Continue with Google
```
- 'Sign up' tab is selected; the primary button reads 'Create account' and is disabled (dimmed) until the box is ticked; the consent line is fully visible (y 573 to 610 of 956). 'Terms of Service' and 'Privacy Policy' are links (/terms?ref=signup, /privacy?ref=signup). Placeholders (not in the text above): 'Email', 'Password'. The 'Forgot password?' button is hidden in sign-up mode.

## 02-signup-consent-ticked.png (same screen, box ticked)
```
MentorMind
The counsel of the ages, kept for you.
Sign in
Sign up
show
Create account
I confirm I am 18 or over and agree to the Terms of Service and Privacy Policy.
or
Continue with Google
```
- Identical text. The checkbox is ticked (gold) and 'Create account' is enabled (full colour).

## 03-settings-privacy.png (Settings, Privacy tab; page scrollY 0)
```
Settings
Profile
Account
Privacy
Billing
Download your conversations
A plain-text file of your conversations, readable summaries and, where kept, the full back-and-forth, including your Round Table sittings. Choose a mentor, a Round Table room and/or a date range, or leave them open for everything. Choosing a mentor also includes the Round Table sittings they were seated in.
Everything (all mentors and rooms)
Epictetus
Benjamin Franklin
Download
```
- Elements, in order: the select (default option 'Everything (all mentors and rooms)'; its option group 'Mentors' lists Epictetus and Benjamin Franklin), two date fields (empty, show mm/dd/yyyy), and the 'Download' button. All fully on screen (the Download button ends at y 696 of 956). The top-left menu button is the app's fixed mobile nav.

## 04-settings-account.png (Settings, Account tab; page scrollY 42)
```
Settings
Profile
Account
Privacy
Billing
Display name
Save
Email
alex@example.com
Sign-in method
Email and password
Change password
Change
Delete account
Delete
```
- Field values: Display name input holds 'Alex'. The Delete account row (label plus red 'Delete' button) is fully visible, ending at y 936 of 956. Nothing was clicked here.

## 05-delete-confirm.png (after clicking the red 'Delete' button; page scrollY 156)
```
Settings
Profile
Account
Privacy
Billing
Display name
Save
Email
alex@example.com
Sign-in method
Email and password
Change password
Change
This permanently deletes your account and every conversation, with no way back. Type your email to confirm. A 24-hour grace period follows, and you can cancel any time before it ends.
Delete my account
Cancel
```
- The confirmation block (fully visible, y 691 to 936):
```
This permanently deletes your account and every conversation, with no way back. Type your email to confirm. A 24-hour grace period follows, and you can cancel any time before it ends.
Delete my account
Cancel
```
- Input placeholder: 'Type your email to confirm' (empty). 'Delete my account' is disabled (dimmed) because the email has not been typed. The deletion was NOT confirmed and no delete request was sent (no /delete-request call was made; the mock log shows none).

## Notes
- The strings come straight from the app's markup; nothing was rewritten. Source lines in web/onboard.html: consent line at ~922 (sign-up gate), Download block ~1458, delete-account block ~1426-1437.
- In shots 4 and 5 the page is scrolled so the whole delete section is in view; the menu button is fixed and may overlap the top-most nav item or heading slightly in shot 5.
- The email the user must type for the real button to enable is the account email (alex@example.com here); it was not typed.
