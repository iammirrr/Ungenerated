<!-- Part of ungenerated-flows. Was the `consent-and-permissions` skill. -->
> **When:** Ask for consent and system permissions honestly and in context - the terms accepted in one plain line under the sign-in button, usage analytics with a switch that withdraws consent in one tap, an unmistakable "does and never does" promise checked against the privacy policy, and each system permission asked where it is used, with at most one screen before the system alert whose only button opens it. Covers what iOS and Android actually allow. Use for privacy, terms, consent, analytics opt-out, notifications, Screen Time, location, camera or tracking prompts.

# Consent and permissions

Proof for the rules below: § is `ungenerated-audit-app-review/references/apple-docs.md`, R is an
entry in that folder's `rejections.md`, a row is its `checklist.md`.

## The terms: one line under the sign-in button

- **One plain line under the sign-in buttons:** "By continuing, you agree to the Terms of Use and
  Privacy Policy.", both linked, each a real tap target, at a size people read. Signing in is the
  yes; nothing else asks. It puts acceptance before money changes hands, and the paywall links
  both documents again (Schedule 2 §3.8(b); row 24).
- **No tick boxes and no disabled Continue.** The core processing runs on the contract, so
  accepting the terms is an acknowledgement, not a permission. The line replaced two unticked boxes
  ("I accept the Terms of Use", "I've read the Privacy Policy") that held Continue until both were
  ticked (Comma, Nov 2026).
- **The documents are plain pages** that load without script, a login or a cookie wall, at
  addresses that stay up (row 92; R45).

## Usage analytics: consent, and a switch to withdraw it

- **Apple's rule.** "Apps that collect user or usage data must secure user consent for the
  collection, even if such data is considered to be anonymous at the time of or immediately
  following collection. Paid functionality must not be dependent on or require a user to grant
  access to this data. Apps must also provide the customer with an easily accessible and
  understandable way to withdraw consent." (G 5.1.1(ii), §5; row 53)
- **The pattern.** The privacy policy says what analytics collects; the sign-in line accepts it;
  and the app has a switch: Settings › Usage analytics, with one plain line on what it sends and
  never sends ("What you tap and use in the app, never your words, so we can fix and improve it.").
  Off stops the analytics SDK at once and at every launch before any event (the SDK's own opt-out,
  read from the saved choice); on again starts a fresh anonymous id, then identifies the account.
- **Nothing paid depends on it.** The switch changes what is sent, never what works.
- **What is sent before the line is collection too.** Onboarding events from before sign-in are
  covered only if the person has agreed by then: hold them on the phone until the line is
  accepted, or put the same line under the opening's first button. How App Review tests this isn't
  documented (row 53), so treat it as Apple's words, not a known rejection.
- **Where the law asks for opt-in** (analytics beyond what's strictly needed in the EU and UK,
  marketing email), the switch starts off and the person turns it on. Optional choices stay
  separate and are never bundled with the terms (`ungenerated-audit-privacy` › lessons 12).

## The promise: what the app does and never does

Shown once, after the paywall or beside the sign-in line, as reassurance about what they chose. It
asks for nothing; the terms were accepted at sign-in.

It must be **unmistakable**:

- **Two big cards:** a green tick with "The app does", a red cross with "The app never". Green
  means does, red means never, and the colours mean nothing else on the screen.
- **Three short bold lines each, one line of detail under each.** Someone who reads only the bold
  still understands. One line of detail, never two: shorten until it fits.
- **The app does**: concrete things ("Tracks your work time" / "On this phone, and on your computer").
- **The app never does**: ("Records what you type" / "No keystrokes, screenshots or audio").
- **No "may", no "might", no legal words.** The legal text is one tap away.
- **Check every line against the privacy policy, for every platform the account touches.** Easy
  traps: "never sees your screen" when a companion app records window titles; "nothing leaves your
  device" when crash reports are on by default or text goes to an AI provider. One broken promise
  costs more than none.

## Permissions

- **Ask where it is first used.** Never at launch. Ask where the reason is visible; when a
  permission isn't needed to build the plan (a camera for filming, the microphone), ask at the
  moment of use (Comma, Oct 2026). Often no screen is needed at all: the system alert with a
  specific purpose string, at that moment.
- **At most one screen before a system alert, with one button.** One line of why and a single
  "Continue" (or "Next") that opens the system alert. No "Not now", "Skip", "Maybe later" or close.
  HIG: "Include only one button and make it clear that it opens the system alert"; "don't provide
  a way for people to leave the screen or window without viewing the system alert — like offering
  an option to close or cancel." (§5; row 47; a "Not now" screen is among the common rejections in
  checklist §9.)
- **Whatever they answer, the flow goes on.** A denial is respected: the feature says "Not allowed"
  with a way to Settings where it is used, and everything else works. Apple: "Where possible,
  provide alternative solutions for users who don't grant consent" (5.1.1(iv)); nothing may depend
  on allowing push, location or tracking, and nothing rewards it (5.1.2(i); row 54).
- **One permission at a time, never a rows-of-toggles screen.** A toggle can't grant access by
  itself, and a screen of rows with a way on past them lets people leave without seeing the
  alerts, which the HIG rules out. This replaced the permissions-rows screen.
- **Ask what the next screen needs first.** On iOS, Screen Time access (Family Controls) must be
  granted before the app can show the app picker.
- **Purpose strings say what the feature does with it,** with an example, in one sentence,
  localized. "In order to take a picture or video, this app requires permission to access the
  camera" was rejected as vague (R40; row 46).
- **AI consent is its own sheet,** at the first AI moment ([ai-permission.md](ai-permission.md)).
- **Personal permissions go before the price** (with the rest of "make it yours"); the top
  screen-time apps all do it, and the plan can then use what was allowed.
- **Tracking:** the App Tracking Transparency prompt only if the app really tracks. Before it, no
  incentive, no screen that looks like a request, no picture of the alert and no annotations on
  the screen behind it, all named as rejection causes (HIG, §5; row 50).
- Show the real system sheet text on the board; don't redesign Apple's or Google's dialogs.

## Platform facts worth knowing

- iOS notifications: one system prompt per install; after a denial only Settings can change it.
- iOS Screen Time shields are drawn by the system; apps set the icon, title, subtitle and two
  buttons, not the layout.
- Android 13+: notifications need a runtime permission.

## Anti-patterns

- Tick boxes for the terms that hold Continue; the one line under the sign-in button replaces them.
- Pre-ticked boxes for optional choices (marketing email).
- "Allow everything" buttons.
- "Not now", "Skip" or a close on a screen before a system alert.
- A fake permission dialog styled like the system's that leads to the real one.
- Analytics with no way to turn it off in the app.

## Events

- Accepting the terms is `signin_result` ([sign-in.md](sign-in.md)); the line sits under its buttons.
- `permission_result` {permission, result: allowed | denied}

Once the analytics switch is off, nothing is sent, including that it was turned off.
