<!-- Part of ungenerated-flows. Was the `paywall` skill. -->
> **When:** Design an honest, high-converting paywall - one value beat before the price, everything they get named, the amount billed as the biggest price on screen, the subscription terms by the button, a trial timeline with real dates only for a plan that has a trial, prices from the store or an honest "didn't load", money that rolls, a bright calm ground, and no dark patterns. Use for subscription screens, pricing, trials, upgrade prompts or "the paywall looks scammy".

# Paywall

Proof for the rules below: § is `ungenerated-audit-app-review/references/apple-docs.md`, R is an
entry in that folder's `rejections.md`, a row is its `checklist.md` (the purchase screen: rows
16–25).

## Before the price (1–3 beats, no top bar)

- One screen of value in their terms: their week before and with the app, from their answers.
- If something is really free without paying (a companion app), say so before the price. Behind a
  hard paywall nothing is, so nothing there is called free: a "Free" perk on a hard paywall was
  flagged before submission (`ungenerated-audit-app-review` › lessons 35).
- A small commitment (hold the hero to commit) can lead into the paywall.

## The paywall

1. **Every plan's billed amount is visible before any tap, and it is the biggest pricing text.**
   Apple: "the amount that will be billed must be the most prominent pricing element in the
   layout"; a per-month or per-week figure and any "save x%" sit smaller and below it, "in a
   subordinate position and size" (§2; R26; row 20). Work every saving out from the store's real
   prices, rounded down, never typed in.
2. **Everything they get, named.** Show the product working (what goes in, what comes out) and
   name every paid feature plainly, each with its own icon and room; when many concrete tools are
   the reason to pay, list them all (two columns hold ten) rather than three abstract lines. Give
   the limits the server enforces ("50 exports a month"). 3.1.2(c): "clearly describe what the
   user will get for the price. How many issues per month? How much cloud storage?"; a paywall
   rejected under 5.6 also lacked a list of what it unlocks (R48; row 16; flows lessons, "The
   paywall shows the product working").
3. **The trial timeline**: today, the reminder day, the first charge day with its price, all real
   dates. Only when the selected plan has a trial and this account can still have it; otherwise
   there is no timeline (rows 21, 27).
4. **Money rolls** on slot-machine reels when a plan changes; time never does.
5. **A bright, calm ground**: one colour field or a soft gradient, fine grain at most.
6. **One button whose words follow the selected plan.** "Continue" or "Subscribe" works for every
   plan. Trial words go on it only when the picked plan has a trial for this account, and never
   louder than the billed price beside it: "Try for Free" as the main button was rejected under
   3.1.2 and passed as "Continue" (R25); a screen selling a free trial while a plan without one
   was pre-selected was rejected under 5.6, by the accepted answer's reading (R48).
7. **The terms by the button, on every purchase screen.** The plan's name and length, the billed
   price, that it renews automatically until cancelled and how to cancel, and for a trial its length
   and the price after it ("3 days free, then $99.99 a year. Renews automatically; cancel anytime in
   Settings."), with Terms of Use and Privacy Policy as real links with real tap targets (Schedule 2
   §3.8(b); §2; R24; rows 17–24). Then Restore purchases, visible (R23; row 25).

## Prices that load, or say they didn't

- **Prices come from the store, in their currency** (StoreKit `displayPrice`, or the payment SDK's
  localised string), fetched at launch and again on the paywall with a retry. Apple: "Fetch product
  information using StoreKit APIs before presenting In-App Purchases in your app's UI" (§2; row 19).
- **No hard-coded price, not even as a fallback.** When the store returns nothing, the paywall says
  so in one line ("Prices didn't load. Check your connection.") with Try again, and nothing on it
  pretends: no typed-in price, no plan cards without prices, no button that does nothing. Reviewers
  have seen products fail to load in review while TestFlight worked (R9). Log the store's error,
  untruncated (`ungenerated-audit-payments` › lessons 32).
- **Buying is the store's own sheet.** The button calls the store's purchase; its confirmation sheet
  is never imitated, redrawn or covered ("Use the default confirmation sheet. ... Don't modify or
  replicate this sheet.", HIG, §2; row 33). A stand-in "App Store" sheet shown when products didn't
  load was found in one release build before submission.

## The way out

- Say how to cancel on the paywall, in its small print ("Cancel anytime in Settings"), and make
  it true: the platform's cancel sheet is one tap from the subscription screen ([cancel-flow.md](cancel-flow.md)).
- On a trial, the reminder on the timeline is a promise. Send it.
- **A hard paywall still has a visible close.** It never lets anyone into the paid app and never
  fires an offer (an offer shown when the paywall was closed was rejected under 5.6, R46); it goes
  back a step, or to a plain locked screen with Subscribe and Restore.
- **Sign out and Delete account are reachable from a hard paywall.** Someone who made an account
  and won't pay must be able to delete it without paying (5.1.1(v): deletion "easy to find", §4;
  row 37; [account-deletion.md](account-deletion.md)).
- **Explain a hard paywall to App Review.** The review notes say the app needs a subscription,
  what's paid, why, and where Restore is; the listing says what's paid (2.3.2). A paywall with "no
  exit button" was rejected, and the advice was to "explain to the review team why your app
  requires to have such a business model" (R47; R10; row 85). The guidelines don't require a free
  tier (rejections.md, Myths).

## Never

- Laurels, invented reviews, "#1 app" claims you cannot prove.
- Fake countdowns and "only today" prices that are always there. The one real timer is the
  one-time offer's ([one-time-offer.md](one-time-offer.md)).
- Pre-selected expensive plans hidden below the fold.
- Per-week prices that hide an annual charge, or any breakdown or saving bigger than the billed
  price (R26).
- A free-trial toggle. Apple: "Remove the toggle for adding or removing a free trial from the
  subscription purchase screen." (R27). If both are needed, the trial is its own plan option with
  its own terms.
- Trial words while a plan without a trial is selected (R48), or for an account that can't have
  the trial (row 27).
- "Free" for anything but a real free trial; a discount is a price (lessons 35 in
  `ungenerated-audit-app-review`).
- A hard-coded price, a stand-in store sheet, or anything that looks like Apple's purchase sheet.
- An offer fired by closing the paywall (R46), or a second paywall straight after the first (on an
  unofficial list of 5.6 triggers, R47).
- A close button that is hard to find.

## Lessons from shipping (Comma, Nov 2026)

- **Hard paywall.** Closing never lets anyone in. Restore is always on screen. The one-time offer
  comes only after a cancelled purchase sheet ([one-time-offer.md](one-time-offer.md)); it first
  opened from the close button, the trigger Apple has rejected (R46).
- **No free pass outside Debug.** Not in TestFlight, not in production. The store's sandbox charges
  nothing, so testers buy for real. A free pass for tap tests lives in Debug builds only.
- **Prices from the store, in their currency,** and the board, the app and the store agree. The
  first builds kept a hard-coded price as a fallback; it goes, for the honest "didn't load" above.
- **The trial only if the account can still have it, and only on a plan that has one.** Otherwise
  the copy, the button and the steps say Subscribe, and the trial timeline is skipped.
- **A short trial comes with limited AI,** so it can't be farmed (Comma: three days, a handful of
  AI scripts).
- **Every purchase screen** (paywall, offer, plan picker, the subscription screen's "Subscribe
  again" and "Change plan", the cancel flow's offers) links Terms and Privacy and states the price,
  the length and that it renews automatically (3.1.2). The pre-submission audit found buy buttons
  outside the paywall with none of it.
- **Sign in first** and log the payment SDK into the account id ([sign-in.md](sign-in.md)).
- **Log the result, not the tap.** Closing the store's sheet returns no plan; it was logged as
  "subscribed" until it was caught.
- **The trial reminder only for a real trial,** the day before the store's own end date. Monthly
  subscribers were told "your free trial ends tomorrow".

## Events

- `paywall_shown` {where}
- `paywall_plan_picked` {plan}
- `paywall_prices_failed` {code}
- `purchase_started` {plan, trial}
- `purchase_result` {plan, result: trial | active | closed | failed}
- `trial_started` / `subscribed`, only when the plan really started
- `restore_result` {found, where}
- `paywall_closed`

Set the plan and status on the person. One dashboard holds the paywall and cancel funnels.
