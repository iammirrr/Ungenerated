# One-time offer

One honest discount for someone who tried to buy and stepped back: they picked a plan, the store's
purchase sheet came up, and they cancelled it. It replaces "Countdown timers" only in this one
place: the timer is real and the offer is real, or there is no offer.

Proof for the rules below: § is `ungenerated-audit-app-review/references/apple-docs.md`, R is an
entry in that folder's `rejections.md`, a row is its `checklist.md` (offers: rows 22, 27, 28, 90).

## Rules

- **Not in a first submission.** The safest version 1.0 ships without it (not in the build, not
  behind a switch); add it in an update whose review notes say what it is and how the reviewer
  meets it. Apple has rejected a one-time offer under 5.6 ("The app attempts to manipulate
  customers into making unwanted in-app purchases. Specifically, the app shows a one time offer for
  subscription when the user closes the initial subscription page launched upon opening the app.",
  R46), and vendors report Apple getting stricter on these in 2026. A held feature arrives in its
  own reviewed version, never switched on from a server (2.5.19; rejections.md, "What gets apps
  approved fast" 12; rows 9, 91).
- **Only after a cancelled purchase sheet.** The person tapped a plan and closed the store's own
  sheet without buying. No rejection is on record for this trigger, and Superwall's account of
  Apple's position is that "Showing any offer after a cancelled transaction is allowed" while
  "What's not allowed is looping the user" (R46). Never when the paywall is closed (the trigger
  R46 was rejected for), never at launch, never on the first view of the paywall, never in the
  cancel flow (it has its own offer, [cancel-flow.md](cancel-flow.md)), never to lapsed
  subscribers (Apple shows them its own win-back sheet; row 90).
- **Once, closable, never looping.** It shows the first time the sheet is cancelled. "No thanks",
  the close button or the timer running out ends it for good: it never pops up again by itself, no
  "Are you sure?" on closing, and no paywall reopens itself. "If your "one-time offer" keeps
  reappearing to the same user, Apple may flag this as deceptive marketing." (Superwall, R46)
- **Only if the account can get it.** Check eligibility with the store (StoreKit
  `isEligibleForIntroOffer`, or the payment SDK's eligibility check) and that the offer exists:
  `isEligibleForIntroOffer` "may be `true` even if you haven't set up an introductory offer"
  (row 27). If either fails, there is no offer: cancelling the sheet leaves them on the paywall.
- **Real products.** The offer is an introductory price on its own products in the same
  subscription group (or a store promotional offer), set up in the store and in the payment SDK as
  a separate offering. Something the store actually grants (row 28).
- **Never fall back to the full-price product.** If the offer product or package is missing, hide
  the offer. A fallback would charge full price under an offer's headline.
- **A real timer.** One hour (or whatever you pick), started the first time it's shown and kept in
  the Keychain, so reopening or reinstalling doesn't reset it. When it ends, the offer is gone. In
  test builds keep it in ordinary storage so a tester can reinstall and see it again
  (`ungenerated-audit-payments` › lessons 50).
- **The billed price leads.** The biggest number is what the store charges: the first period's
  price and its length, then the regular price after it ("$79.99 for your first year, then $99.99 a
  year"). HIG: "list the introductory price, the duration of the offer, and the standard price the
  customer pays after the offer ends"; "the amount that will be billed must be the most prominent
  pricing element" (§2; rows 20, 22).
- **"Free" only for a real free trial.** A discount is a price, not free time: a "2 months free"
  headline in huge type over a small grey price was flagged before submission as promoting a false
  price (2.3.1(a), 3.1.2(a); `ungenerated-audit-app-review` › lessons 35).
- **A saving, if shown, is worked out from the store's prices** in the person's currency, rounded
  down, and sits smaller than the price: "Save 20%" or "$20 off your first year" from (full price
  for the period − offer price). It is then true in every currency. Convert through `doubleValue`,
  never `NSDecimalNumber.intValue` (`ungenerated-audit-payments` › lessons 42).
- **Discount the first period only.** Renewals return to full price. Work out the margin after the
  store's cut and the worst-case cost of the person's usage.
- **"No thanks" goes back to the paywall,** never into the app (the paywall is hard).
- **It's a purchase screen:** the plan's name and length, the billed price first, auto-renewal,
  Terms and Privacy links as real tap targets ([paywall.md](paywall.md); rows 17–24).
- **The look:** "One-time offer", the countdown, at most two deals, one button ("Claim my offer"),
  and "No thanks" as a real, easy tap. It lands as a moment: confetti or particles once as it
  arrives, the app's character arriving and staying put (flows lessons, "A one-time offer is a
  moment"). That confetti is the owner's pick, a named exception to "no confetti for things that
  are not achievements" (`ungenerated-review` › no-slop, references/no-slop.md). No guilt.

## Where it lives

Over the paywall, after the store's purchase sheet is cancelled; closing it returns to the
paywall. Nowhere else.

## Events

- `exit_offer_started` (the timer starts, at the first show)
- `exit_offer_shown`
- `exit_offer_claim_tapped` {plan}
- `purchase_result` {plan, result: trial | active | closed | failed} (the same event as the paywall)
- `exit_offer_declined`
- `exit_offer_expired`

## Mistakes and traps

- An offer purchase that falls back to the regular product charges full price. Hide the offer.
- A saving written for US dollars is false in other currencies. Compute it.
- A "2 months free" headline over the real price read as a false price. Lead with what's billed.
- A timer kept in ordinary storage resets on reinstall, so the "one hour" is a lie.
- "No thanks" letting people into the app turns a hard paywall into a soft one.
- The trigger moved twice. "No discount trick on close" (Flamely, Oct 2026), then one real offer
  after close (Comma, Nov 2026), then, once Apple's rejection of the close trigger was found (R46),
  only after a cancelled purchase sheet, once, and not in a first submission (Nov 2026).
