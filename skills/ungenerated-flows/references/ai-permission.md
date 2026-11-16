# AI permission

Before any of the person's words leave the phone for an AI provider, ask once, on the app's own
sheet. It is a promise about their writing, so it gets the same care as the paywall.

Apple's rule: "You must clearly disclose where personal data will be shared with third parties,
including with third-party AI, and obtain explicit permission before doing so." (G 5.1.2(i),
`ungenerated-audit-app-review/references/apple-docs.md` §5; checklist row 51.) In 2026 it was the
biggest cluster of rejections: "the app does not clearly explain what data is sent, identify who
the data is sent to, and ask the user's permission before sharing the data", and a privacy-policy
line or a sign-up checkbox wasn't enough (rejections.md R42).

## Rules

- **It names the provider before any text leaves the device.** What is sent, to whom (the
  company and the model), for what, and what stays on the phone, at the moment of asking; never
  only in the privacy policy (R42).
- **The app's own sheet, never a system alert.** An alert can't show who does the work or what is
  sent, and it looks like an error. The sheet holds:
  - the app's mark (its character, if it has one) in front of the provider's real icon, never a
    sparkle;
  - one heading: "*App* writes with *Provider*";
  - one line on what it's for;
  - what is sent and where, in plain words, every line true and in the privacy policy ("Your words
    go to Anthropic to write. They aren't used for training. Audio and video stay on this phone.");
  - two buttons: **Allow *Provider*** and **Keep writing by hand**.
- **Swiping it away means no.** Treat it exactly like "Keep writing by hand".
- **Save the answer at the tap.** Write it before the sheet's exit animation starts, on the phone
  and on the server (answer, time, the version of the words). A delay lost the answer when the app
  closed.
- **Show it from wherever AI starts.** A sheet can't present the root's sheet, so present it from
  the app's root and from inside every sheet that has an AI action.
- **No means the app still works.** Every manual path keeps working. An AI action tapped later
  shows the sheet again; nothing nags in between.
- **Never a condition of finishing onboarding.** An AI step in the onboarding (a "try it" demo)
  offers "Write it myself" beside "Try again" when the answer is no, or the network or the
  provider is out of reach, and the onboarding goes on either way. Apple: apps must not "manipulate,
  trick, or force people to consent to unnecessary data access", and "Where possible, provide
  alternative solutions for users who don't grant consent" (G 5.1.1(iv), §5).
- **Until they answer, it shows.** Put the first AI moment where a reviewer meets it (the
  onboarding's try-it step), and never let a "seen once" flag skip it. After eight submissions one
  app was told "We were not presented with the consent prompt on launch or anywhere else in the
  app."; its flag had let the gate be skipped (R42).
- **Revocable in Settings,** in the same words ([ai-transparency.md](ai-transparency.md)).
  Revoking stops all sending at once.
- **The server checks too.** An AI request without a recorded yes is refused (fail closed), so a
  bug in the app can't send words.
- **Ask at the first AI moment,** not at launch and not on a permissions screen.
- **Say it everywhere else too.** What passed after the 2026 rejections: the privacy policy lists
  the AI provider as a processor, the App Store description names it and says it doesn't train on
  the data (when that is true), a consent screen in the onboarding, and the same in the release
  notes (R42). The review notes list it among the external services, as Apple asks (apple-docs
  §11).

## Where it lives

- The first AI action anywhere (in onboarding, the first real AI demo).
- Settings › AI: the switch, what is sent to whom.

## Events

- `ai_permission_shown` {where}
- `ai_permission_answer` {answer: allow | by_hand | dismissed, where}
- `ai_permission_revoked`

## Mistakes

- The answer was saved after a delay and lost when the app closed. Save at the tap.
- Shown only from the root, it never appeared inside the writing sheet, where it was needed.
- A system-style prompt felt cheap. The owner: "I want that pop-up to be nice ... we use Claude for
  every writing, so it is high quality."
- The onboarding's try-it step had no way on when the AI was refused or out of reach. Now it
  offers "Write it myself" and "Try again", and the onboarding continues (Comma, Nov 2026).
