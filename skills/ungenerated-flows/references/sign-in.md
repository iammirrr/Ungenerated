# Sign in

The door for new and returning people. Where the account screen sits and how it looks is in
[account-signup.md](account-signup.md); this page is what the door must do.

Proof for the rules below: § is `ungenerated-audit-app-review/references/apple-docs.md`, R is an
entry in that folder's `rejections.md`, a row is its `checklist.md`.

## Rules

- **Late, and before the paywall.** Never the first screen. The personal setup comes first and
  stays on the phone, the account saves it and syncs it at sign-in, then the plan, then the paywall
  last. A purchase made before sign-in belongs to a phone, not a person.
- **The terms in one line under the buttons:** "By continuing, you agree to the Terms of Use and
  Privacy Policy.", both linked, real tap targets. Signing in is the yes; no tick boxes
  ([consent-and-permissions.md](consent-and-permissions.md)). Usage analytics gets its own switch
  in Settings, so the consent can be withdrawn in one tap (G 5.1.1(ii), §5; row 53).
- **Log the payment SDK into the account id** the moment sign-in succeeds (RevenueCat
  `Purchases.logIn(accountId)`, or StoreKit's `appAccountToken`). A purchase made signed out stays
  on an anonymous id, and the server's webhook can't match it to anyone.
- **Apple first.** Sign in with Apple, or another login with the same three features, is required
  once any other social login is offered (App Review 4.8; R36; row 40). Its button is no smaller
  than the others and needs no scrolling (HIG; row 43). Google is wanted by most audiences. Email,
  if at all, is a one-time code, never a password.
- **Only the doors that work.** A provider that doesn't work in this build is hidden until it does
  (Google stays hidden until its OAuth client exists and the backend accepts it). A button that
  fails is worse than no button.
- **The success moment lands, with one signal.** If the app's character is on screen, its happy
  jump says "you're in" alone; otherwise a tick closes. One success haptic, then move on. Not a
  toast, not a silent jump to the next screen, never a tick beside the character (flows lessons,
  "One signal per success").
- **Returning people hear "Welcome back,"** and their data comes back. Signing in from the opening
  skips the questions they already answered, then checks the subscription: a paying account goes
  to the app, any other lands on the paywall. Without that check, "I already have an account" is a
  free way past a hard paywall for anyone who ever made one (flows lessons, "I already have an
  account is a paywall door").
- **Apple sends the name and email only on the first sign-in.** Save them then, and never ask for
  them again; any extra field is optional. Asking for a name or email after Sign in with Apple was
  rejected (R30; 5.1.1(x): optional "for the user"; row 42).
- **"Hide My Email" gives a relay address.** Register your sending domain with Apple's relay or
  your emails won't arrive, and accept both relay domains: privaterelay.appleid.com and, for new
  addresses after Apple's change announced in Aug 2026, private.icloud.com (§4; row 43).
- **A cancelled sheet is not an error.** If they close Apple's or Google's sheet, stay on the
  screen quietly. A real failure gets one line and a retry.
- **Signing out** logs the payment SDK out too and clears this account's local data. It deletes
  nothing on the server ([account-deletion.md](account-deletion.md) does that).

## Where it lives

- Onboarding: the account screen after the personal setup, before the plan and the paywall.
- The opening: a small "I already have an account" that opens the same door, then the
  subscription check.
- Settings › Account: who is signed in, Sign out, Delete account. On a hard paywall, Sign out and
  Delete account are reachable from the paywall too, for an account that hasn't paid
  ([paywall.md](paywall.md); 5.1.1(v); row 37).

## Events

- `signin_shown` {where}
- `signin_started` {provider}
- `signin_result` {provider, result: new | returning | cancelled | failed}
- `signed_up` once, for a new account
- `signed_out`

Identify the person with the account id at `signin_result`, so the anonymous onboarding events
merge into them. Never identify by name or email.

## Mistakes

- A purchase made signed out stayed on an anonymous id and the webhook answered "no user". Sign in
  before the paywall, then log the payment SDK in.
- The success went by with no moment. The owner: "it's supposed to show a tick." Later, with the
  character on screen, the tick was one signal too many: the character alone says it.
- Provider buttons that didn't work yet were on screen: "legitly, nothing is working." Hide them.
- Identifying by email put personal data into analytics.
- The first version of this page sent returning people straight to the app, which let a
  non-paying account past a hard paywall.
- Two tick boxes held Continue until both were ticked; one line under the button replaced them.
