# Field study: the screens around the exit

Screens studied on Appllama (14 October 2026), from apps in its library of top-grossing iOS
apps. Most iOS apps hand the cancel itself to Apple's sheet, so in-app exit work lives in the
screens around it. Summarised in our own words; no screens are reproduced. R numbers are entries in
`ungenerated-audit-app-review/references/rejections.md`, rows are that folder's `checklist.md`.

| What it is | Seen in | The lesson |
|---|---|---|
| A loss-framed confirm when someone dismisses a one-time offer ("Are you sure to give up the discount?", Discard offer / Stay) | Blessed (daily verse) | Seen, not copied: with vendors reporting Apple stricter on offers in 2026, closing an offer closes it, with no confirm and never a second offer ([cancel-flow.md](cancel-flow.md), checklist row 90). |
| "Before you go… one-time special offer", a third off, priced per week, "No commitment, cancel anytime", a mascot holding a gift | WeightBuddy (calorie tracker) | The no-commitment line lowers the stakes; the per-week figure must sit smaller than the billed price (rejections.md R26). Right for win-back, and on a paywall only after a cancelled purchase sheet, never when the paywall is closed (R46, [one-time-offer.md](one-time-offer.md)); wrong for a cancel flow's goodbye. |
| Subscription info as a card: status, type, renewal date, then "If you want to cancel your subscription, learn how here" | Mondly (languages) | Show the facts before the action; link to the how-to rather than hiding it. |
| A help article: how to cancel on iOS in five steps, "If you don't see that button, you're already canceled", "Apple handles all subscription payments, not us", "Did this answer your question?" | Invoice Maker | Exact steps and who bills answer the angriest support tickets before they're written. |
| A delete-account modal: deleting removes the data but does NOT stop the recurring subscription; stop it with Manage Subscription first | Regrid (property), Photoleap, Motionleap | On the App Store, delete is not cancel. Say it first, link to the plan, then delete. |
| Delete account with a grace period: data deleted, reactivate within 10 days; cancel the subscription separately | OurPact (parental control) | A grace period turns a regretted delete into a non-event. |

## What none of them did

- None paired the delete sheet with the person's own numbers or an export; a data export before
  deletion is both a kindness and, in the EU, an obligation.
- None offered a break; on iOS the honest break is renewal off, data kept and a reminder on the
  day they pick.
