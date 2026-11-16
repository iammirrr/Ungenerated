<!-- Part of ungenerated-flows. Was the `cancel-flow` skill. -->
> **When:** Design the cancel flow (exit flow) for a subscription app - the platform's own cancel sheet one tap from the subscription screen and from every step, so leaving is never blocked; one optional exit question with four or five specific answers and no "Other"; one offer matched to the answer, shown once and never in the way (a fair price, a pause or break, a cheaper plan, more trial time, or no offer at all); the person's own numbers; a personal goodbye and an easy way back; and Apple's own retention message, if used, within its text rules. Use when designing cancellation, "manage subscription", retention or win-back screens, or when churn is the problem.

# Cancel flow

A cancel flow has three jobs: keep the people an honest offer can keep, learn why the others
leave, and part well with everyone. A flow that traps people saves a few this month and loses
the trust that would have brought them back. A good one changes the mind of roughly one in five
to one in three people who start it.

**Leaving never blocks the platform's subscription sheet.** Its steps stand beside the way out,
never in front of it. Apple: "Always make it easy for customers to cancel an auto-renewable
subscription. If the manage subscription action is deep within an app — or hard to recognize —
subscribers can feel they're being discouraged or prevented from canceling" (HIG); around the
sheet you may show an offer or a survey, but "always make it easy for people to access the
system-provided management UI where they can cancel if they wish" (subscriptions page). Guideline
5.6 rules out "manipulative practices", and a pre-submission audit read four or five screens with
two required answers in front of Apple's sheet as that risk.

Proof for the rules below: § is `ungenerated-audit-app-review/references/apple-docs.md`, R is an
entry in that folder's `rejections.md`, a row is its `checklist.md` (cancelling: row 89; Apple's
sheet: row 30; offers: row 28).

## Why it works

- **People arrive defensive.** Someone who had to hunt for Cancel comes in angry and refuses
  everything. Someone who found it where they expected comes in calm and actually reads the offer.
  That's why easy cancelling saves more people, not fewer.
- **Leaving is a decision about one reason.** Ask for that reason and answer it: a price problem
  gets a price, a time problem gets a pause, a product problem gets a person. A generic "50% off"
  answers a question nobody asked, and it costs you the most.
- **The answers teach you.** A specific list ("My team uses another tracker") tells you something
  you can act on. "Other" and long surveys tell you nothing, and every extra question loses people
  who were about to stay.
- **Their own numbers feel like theirs.** "412 hours since March" is something they made; an
  average is marketing. People value what they made, so say what they keep, not only what they lose.
- **Cheap offers wear out.** An offer shown every time becomes the price. People who stay at a
  price that fits (a smaller plan, yearly billing) stay longest; deep discounts hold people only
  until they run out.
- **The goodbye is the first screen of coming back.** A clear, warm, exact goodbye is what people
  remember when they need the product again.

## The screens

At most two screens stand between the subscription screen and the platform's sheet (the question,
the offer), both skippable, each with a button that opens the sheet at once.

1. **The subscription screen, where they expect it.** Settings → the plan. What it did for them
   (their numbers), the plan, its price, the next charge date and who bills it, and what stays if
   they leave ("Your data stays."). A cheaper way to pay sits above the ways out (yearly billing,
   a smaller plan). Two ways out, both plain and visible: **Manage in App Store** (the platform's
   name for it) opens the platform's sheet directly, one tap; **Cancel subscription** starts the
   short in-app exit below.
2. **One question, optional.** Four or five answers, one pick, written in the product's words. No
   "Other". The answer's one follow-up and an optional note appear in place under the pick, on the
   same screen. "Skip" and "Cancel in the App Store" both open the platform's sheet; no answer is
   required to leave.
3. **One offer, matched to the answer** (table below), only where the store can grant it, shown
   once. Its own screen, with "Cancel in the App Store" as a full button that opens the sheet at
   once, not a grey link and not one more step. Declining never leads to a second offer.
4. **The platform's own sheet.** On iOS, `manageSubscriptionsSheet` does the cancelling; on
   Android, the Play subscription centre; on the web, the checkout provider's cancel page. Show
   the real thing on the board; never fake it in the app. Apple's own retention message may appear
   inside it (below).
5. **The goodbye**, once the server says renewal is off: their name, a thank-you, the exact day
   access ends, "You won't be charged again", what they keep, export, and one tap to undo.
6. **Coming back.** The same plan screen after it ends: what happened, every price, one tap to
   restart, their data waiting.
7. **On a trial** (its own card): more trial time if the platform allows it; otherwise the truth
   ("Cancel now and keep the rest of your trial") beside a reminder before the first charge.
   Many trial cancels happen in the first minutes, from people who don't trust themselves to
   remember.

## How each screen should look and feel

These come from a flow that was built, reviewed screen by screen and approved; the feel matters as
much as the logic.

- **Big things.** Large icons on the answers, large numbers for their value ("412 h"), one idea
  per screen. Small grey rows read as a form; a form reads as a trap.
- **The subscription screen shows what it did for them** before any button: their hours, their
  best week, the streak, in the product's own visuals (its ring, its mascot, its chart), not a
  feature list. This is "Look what you built": it lives here and on the goodbye, never as a step
  of its own in front of the sheet.
- **Offers stand on the paywall's own ground and type**, so staying looks like the product they
  bought. The button that keeps the plan is made like the plan (the brand's gradient or texture,
  its icon); "Cancel in the App Store" is a plain full-width outline button under it that opens the
  sheet, never a link.
- **Every offer is a purchase screen:** the billed price is its biggest number, then its length and
  the price after it ("$8.99 a month for 2 months, then $11.99 a month"), auto-renewal, Terms and
  Privacy links (rows 17–24). "Free" only for a real free period.
- **One question as big icon rows**, one tap answers it. "Another tool" shows the real icons of
  the tools people actually move to, so the answer is recognised, not read.
- **A break is a picker plus a timeline:** one, two or three months as big cards with the return
  date under each; under that, three steps (today, the day it pauses, the day you're back) with
  short links between the icons, never a line through them.
- **The yearly answer keeps the year:** a discounted next year with the new price and date, and a
  reminder a week before; no refund talk.
- **Budget gets the whole menu at once** on one screen (a free month, a few months at half price,
  a discounted year), every billed price visible, the best value picked, the button naming what the
  picked one charges. Never a second offer after a no.
- **The goodbye finishes like the product**, with their numbers ("You tracked 412 hours with us")
  and the exact last day; coming back is one tap from the same plan screen.
- **Every step keeps "Cancel in the App Store" at the bottom**, the same place and the same
  weight, so nobody has to look for it, and it always opens the sheet itself.

## Match the offer to the answer

| They say | Offer | Watch for |
|---|---|---|
| It doesn't fit my budget right now | Either ask what would feel fair (three price ranges) and match it, or show the whole menu once: a free month, a few months at a discount, a discounted year, every price visible, the best value picked | Never one offer after another. Up to about 40% keeps value best; deeper cuts and free months save more people this month and fewer a year on, so measure the cohort. Once a year |
| I'm taking a break | A pause with a cap (three months at most) and the resume date on screen | Where the store can't pause (App Store), the honest version: renewal off, data kept, a reminder on the day they pick, nothing charges by itself |
| It's missing something | No discount. A line of feedback, "Tell me when it ships", or a person to talk to | Name wishes, never promise unshipped features |
| We moved to another tool | No offer. Let them take their data (export now or later) | Pretending an offer will help is slop |
| I got what I came for | Applause: their numbers, a thank-you, the way to the sheet as the main button, "Tell us what helped" | These people write your best stories |

Write the answers so they neither insult the product nor sound final: "doesn't fit my budget
right now", not "too expensive"; "I'm taking a break", not "I don't use it anymore". Name the
reasons only your customers have; specific answers make people stop and think.

## Apple's own save step: retention messages

Since 4 Nov 2026 Apple can show your message, and an offer, inside its own cancellation flow,
"after they tap Cancel Subscription on a subscription details page" (§3; R51).

- **Set up in App Store Connect** (Subscriptions › Retention Messaging): up to 10 retention
  messages per app, one assigned to a subscription at a time, text and images, optionally a
  promotional offer, with "subscriber eligibility and the wait time between offers"; localise it
  for every storefront. A server-driven version (the Retention Messaging API) is pre-release, by
  request, iOS 15.1 or later (`ungenerated-audit-payments` › apple-subscriptions.md §3).
- **Its words never mention the offer or a price.** "Header and body text can't reference
  promotional offers, discounts, or specific prices, such as "$9.99," "50% off," or "one month
  free."" Every subscriber sees the text, including those who can't get the offer, so "App Review
  rejects retention messages that contain pricing or offer mentions." Say what they keep or what is
  really coming ("Your 40 scripts stay here if you come back."); the attached offer shows its own
  terms.
- **No pressure and no promises you can't check.** "Avoid claims that coerce subscribers or
  guarantee unverifiable outcomes." No "you'll lose everything", no "you'll double your views".
- **One offer per exit.** Pick where the save offer lives, the app's own step or Apple's message,
  not both for the same person: two offers in one exit is the second offer after a no that this
  page rules out. Apple's message can carry the offer while the app's flow keeps only the question.

## The screens around the flow

A real exit has more doors than the cancel button. Design these too (each is small):

- **Plan status, plainly.** Status, plan, renewal date and who bills it, before any action.
- **"How do I cancel?" help.** The platform's exact steps (on iOS: Settings → your name →
  Subscriptions → the app → Cancel Subscription), who handles payments ("Apple bills this, not
  us"), "If you don't see Cancel, you've already cancelled", and "Did this help?".
- **Delete account is not cancel.** On the App Store the platform bills, so deleting an account
  does not stop the subscription. The delete sheet says so first and offers "Manage subscription"
  before "Delete". Give deletion a short grace period ("Undo within 10 days") and say what is
  erased and from where ([account-deletion.md](account-deletion.md)).
- **Closing an offer closes it.** No "Are you sure?" confirm and never a second offer: an offer
  "is shown once, closes" (row 90), and a dismissal that asks again is the start of a loop. A stray
  tap costs one offer; a confirm costs trust and invites a 5.6 read.
- **Reminders that prevent angry cancels:** a week before a yearly renewal and before a trial's
  first charge, with the date and the price; they cost a few saves and earn the trust that brings
  people back.
- **Failed payments are not a cancel.** Show a quiet banner with the platform's update-payment
  sheet and its billing grace period; never route it into the cancel flow.
- **Win-back is for the long gone,** weeks after the end: their data waiting, the price per week
  or per month, "No commitment, cancel anytime". Not on the goodbye. On iOS 18 and later Apple
  shows its own win-back sheet to eligible lapsed subscribers; don't stack a second offer on it
  (row 90).
- **Restore purchases** answers in place: "Your plan is back" or "Nothing to restore on this
  Apple ID", never a dead end.

## Rules

1. **Resistance comes from value, never from obstacles.** Make staying look like the product:
   their own numbers big on the subscription screen, the offers on the paywall's own ground, the
   button that keeps the plan made like the plan. The way to the platform's sheet stays a proper
   button at the bottom of every step, never a grey link and never missing.
2. **The platform's sheet is one tap away, from the subscription screen and from every step.**
   "Manage in App Store" opens it directly; inside the flow, "Cancel in the App Store" opens it at
   once. It does not lower saves; it raises trust. Several US states require cancelling online to
   be as easy as signing up. (HIG and subscriptions page, §2; row 89.)
3. **One question, and it is optional.** Skipping opens the sheet. Every extra question costs
   saves, and a required answer before the sheet is a gauntlet (5.6; row 89).
4. **No "Other".** It becomes a second cancel button, and its answers are made up.
5. **One offer per person, matched to the reason, shown once, never in the way.** At most once a
   year; nobody with an active discount gets another; no stacking pauses; declining it opens the
   sheet. An offer every time turns Cancel into a coupon machine.
6. **Yearly plans are different.** No refund is needed: cancelling stops the renewal and every
   paid day stays. Offer a discounted next year, and remind them a week before it ends.
7. **Their own numbers, never an average.** "412 hours since March", not "users save 5 hours".
   If they saved nothing, don't show the counter.
8. **Say what stays** as clearly as what stops. If the data or the free tier stays, that is the
   strongest honest line you have.
9. **No second discount after they leave.** The one matched offer in the exit (the app's or Apple's
   retention message) is the only discount. Don't chase people who cancelled last week with
   another one; a win-back offer is for people long gone. Otherwise you teach everyone to cancel.

## Never

- Cancel hidden in a menu, behind support, a chat, a phone call or "email us".
- A required answer, a screen that can only be left forward, or a loop between the subscription
  screen and the platform's sheet; more than the question and the offer in front of it.
- Confirmshaming ("No, I don't want to save money"), crying mascots, guilt, "You'll lose
  everything" when they won't.
- Countdown timers, spin-the-wheel discounts, "this offer disappears forever".
- Multi-select reasons, long surveys, a required text field.
- A retention message that names a price, a discount or a free period, or promises an outcome.
- Pauses that resume and charge without warning.
- A goodbye that only says "You will lose access at the end of your billing period."

## Measure

- **Save rate:** about 20–36% for teams that work on the flow. Above 50%, the offers are too
  generous and the product looks cheaper than it is.
- **Saved people still paying later:** 40–70% is healthy; far above that, you're giving away too
  much.
- **Lifetime value by offer:** of the people who took each offer, how many still pay a year on.
- **Direct exits:** how many open the sheet from the subscription screen or skip the question.
  Many is fine; it means the way out is easy to find.
- **Voluntary vs involuntary churn:** failed payments need retries and reminders, not this flow.
- **Read the answers every week.** About three in ten leave feedback you can use.

## On the board

One row: the subscription screen (with Manage in App Store), the question, one card per answer's
offer, the platform sheet (with a retention message, if one is set up), the goodbye, coming back,
the trial case. A second, smaller row for the screens around the flow: plan status, the help
article, delete account, the renewal and trial reminders, the failed payment banner, win-back and
restore. A whole-part card plays one path end to end, and a second plays the direct way out.
The board's demo finger acts inside a screen; only the whole-part card moves between screens.

See `cancel-flow-benchmarks.md` for the numbers and where they come from, and
`cancel-flow-field-study.md` for what real apps do around the exit.

## Lessons from shipping (Comma, Nov 2026)

The newest version of this flow, built end to end, then revised after a pre-submission audit. The
rules above already carry it.

- **The steps, beside the way out:** what they made and what stops on which date (the
  subscription screen) → the main reason → one follow-up on that reason, with an optional note →
  one real offer, only where the store can grant one → the platform's own cancel sheet → a goodbye
  with what happens when, export and a way back. The audit read the first build (four or five
  screens, two required answers before Apple's sheet) as a 5.6 risk; now every step has a direct
  way to the sheet, the questions are optional and the offer shows once.
- **"Keep my plan" in plain sight at every step,** beside the way to the sheet.
- **Cancel through the platform's sheet and read the result from the server** (the billing
  service says it won't renew: cancelled, still paid until the date). A stand-in that marked the
  phone "cancelled" while the store kept billing shipped until it was caught.
- **Offers must be grantable:** the real switch to yearly, a lighter plan, a real promotional or
  win-back offer. Never "half off" or "a month free" with nothing in the store behind it. On iOS a
  discount for someone already subscribed is a promotional offer on the plan they're on, shown only
  when the store returns it (`ungenerated-audit-payments` › lessons 33).
- **Every buy button in the exit is a purchase screen.** The audit found "Subscribe again",
  "Change plan" and the offers with no price per period, renewal or Terms and Privacy (3.1.2).
- **"Subscribe again" while cancelled** opens the platform's sheet to turn renewal back on. It is
  not a new purchase.
- **The reason, the answer and the note go to the private feedback list**
  ([feedback-board.md](feedback-board.md)). Analytics get the answer and whether they wrote a
  note, never the words.
- **Deleting the account is its own flow** ([account-deletion.md](account-deletion.md)).

## Events

- `subscription_opened`
- `cancel_tapped`, `cancel_started`
- `cancel_reason` {reason}
- `cancel_followup` {answer, wrote_note}
- `cancel_offer_shown` / `cancel_offer_taken` / `cancel_offer_declined` {offer}
- `cancel_store_opened` {from: subscription | question | offer}
- `cancel_completed` (when the server reports renewal off, not when the sheet closes)
- `cancel_kept` {step}
- `resubscribe_tapped`
