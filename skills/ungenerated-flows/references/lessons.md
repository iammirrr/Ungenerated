# What we learned, and why

Lessons from building the flows of real apps with their owner (Comma, a script-writing app;
Flamely, a time tracker; CutRoom, a video editor). Each one transfers to any app. Where two lessons
disagreed, the newer one is here and the condition is said. Best first within each group.

## Nothing pretends

- **One rule over every flow: nothing pretends.** No stand-in store sheet, no offer the store
  can't grant, no "cancelled" that only changed the phone, no "subscribed" logged for a closed
  sheet. A person charged after "cancelling" is a refund, a one-star review and a rejection.
  (Comma, Nov 2026)
- **Nothing in onboarding promises what the build can't do on the phone.** "The Apple login is not
  working yet ... The continue with Google is not working. So, legitly, nothing is working."
  Hide what doesn't work. (Comma, Oct 2026)
- **A fake success is worse than an honest error.** A stub sign-in or a fake queued request makes
  the whole app untrustworthy: "80% of things are not working here, so what's the point of it."
  (Comma, Oct 2026)
- **A demo calls the real thing.** A "try it" step in onboarding runs the real model on their input,
  never hard-coded output: "it just literally put those lines, like hard-coded them." (Comma, Oct
  2026)
- **Log the result, not the tap.** Closing the store's sheet returns no plan, and it was logged as
  "subscribed". Record trial, active, closed or failed. (Comma, Nov 2026)
- **Promise a turnaround only once something works the queue every day.** The owner's own first
  request sat queued with nothing processing it while the app promised a time; change the copy only
  when the processor keeps the promise, have a person look at anything past about two-thirds of it,
  and let a missed promise apologise and give a request back. (Comma, Oct–Nov 2026)

## The board

- **Design on a live board, never static mockups.** Rows of small animated phones per part,
  playable as a flow: static screens were "ass", the live board "ten times better". (Flamely and
  Comma, Oct 2026)
- **Each part of the journey is its own section.** "There is no separate section for account,
  plan, paywall, setup; you basically combined those." (Comma, Oct 2026)
- **Variations are a switch on one card, picked by letter.** The owner chose "C for the main",
  "combine E and D". A cut screen is deleted from the board and the app the same round: "why the
  screen I cancelled are not deleted?" (Comma and Flamely, Oct 2026)
- **The board is the spec, and notes are the open list.** Every note reaches the native app in the
  same round and is cleared only when it's true on the phone: "I hope you applied the comment to
  actual application as well." (Comma, Oct 2026)
- **Keep the board lean and fast.** Screens only, one motion-off switch that lasts one visit, no
  speed sliders nobody uses: "the browser demo is too slow." (Comma and Flamely, Oct 2026)
- **No demo data.** Run the board on a real day one built from the onboarding's answers and live
  content: "the demo data is kind of ruining the quality of everything." (Comma, Oct 2026)
- **Mark what each screen needs from outside the app** (sign-in, payments, AI, a permission, an
  event): the owner loved it: "I really like this as a skill." (Comma, Oct 2026)
- **Work on the board the owner opens.** Not a published copy that goes stale: "that is where you
  need to update stuff." (Flamely, Oct 2026)
- **Split the board in two once the app grows: one page for the onboarding, one for the app.** One
  board buried the app under the onboarding; both pages load the same engine and screens, show
  different rows and number their cards separately, so numbers never clash. "create a serpaet board
  for the app and onboarding" (Comma, Oct 2026)
- **Once the app exists, the board mirrors it both ways.** Every screen and state the app shows is
  on it (the AI working, the leaving and offer flows, a journey that crosses sections in one row of
  its own), nothing else is, explored variations come off once one is built, and words and numbers
  come from the build; feedback had been landing on screens the phone no longer matched. The board
  stays the spec only for screens not built yet. "I want to see the things that are currently in the
  app" (Comma, Nov 2026)
- **A picked design gets its whole flow built, each screen as good as the first.** A strong first
  screen led into rough follow-on screens (the item opened, its detail, the next step), and the
  whole pick read as bad. "if I click, like, make a full flow" (Comma, Oct 2026)
- **Every item opens its own content.** Carry the item's id with the tap so each card opens its own
  page; a library where many tiles opened one sample screen looked fake and hid the real flow. "a
  lot of these are like pointing towards a single reel" (Comma, Oct 2026)
- **Judge a list or home layout under a realistic workload, behind a review switch.** Overload
  across stages was the home's real problem, and an empty list hides it; the options were compared
  on a dozen clearly labelled review items in every stage, from a separate store checked to leave
  the person's own writing untouched, while the board's normal view stays on real data. (Comma, Nov
  2026)

## Onboarding order and questions

- **Never open on sign-in.** Hook, questions, story, "make it yours", plan, account, paywall, then
  setup and the tour: "you do not want to show the login screen at first. That is the first rule."
  (Flamely, Oct 2026)
- **Every question screen asks something.** Facts and insights go in the story: "I don't know if
  this is an input screen." (Comma, Oct 2026)
- **Inputs are toys, and nothing locks.** Rulers, charts, swipe decks; Continue appears when
  they've answered, and a pick never moves on by itself. This replaced auto-advance on single
  picks (Comma, Oct 2026; Flamely asked for Continue on every question the same month). If a flow
  auto-advances anywhere, do it the same way everywhere.
- **A control owns every drag that starts on it.** The age ruler's drag moved the screen and the
  bug was reported 18 times. Never pick the gesture by direction; a finger's first points are
  noisy. Test with a diagonal drag. (Comma, Nov 2026)
- **Ask for the destination, not the current state.** "It needs to be how often you wanna post":
  that's what people came for. (Comma, Oct 2026)
- **A rejected question is replaced, not reworded.** "Just ask a different question. How many times
  do I have to tell you that?" (Flamely, Oct 2026)
- **Never label the person.** "There is no true creator category. Generalizing things that don't
  exist is what AI does." Talk about their time and their work. (Comma, Oct 2026)
- **Fewer questions up front.** Configuration (rhythm, hours, goals) moves into setup after the
  paywall: "put this in setup." (Comma, Oct 2026)
- **Onboarding never sends people out of the app to do a chore; it teaches a system feature by
  doing it once on the real path.** A screen that told them to copy a link and paste it back was
  removed; the share sheet and the widget gallery are shown step by step, then done for real:
  "make it actually functional." (Comma, Oct 2026)
- **Teach a system path as the current OS shows it, and notice when they come back.** A widget guide
  written from memory said to tap a + that iOS 18 removed, and no API adds a widget for the person:
  read the steps off a simulator with a UI test. A reminder follows them out only if notifications
  are already allowed, and on return the app checks that the widget is really there (WidgetKit's
  current configurations), then moves on or shows the steps again. (Comma, Oct 2026)
- **When a guide shows another app's or the system's screens, draw only what every phone has.** The
  share sheet differs from phone to phone, so draw it plainly, name only the control they tap and
  show both places the app can be (the end of the row, or under More); finding it took the owner a
  while on a real phone. (Comma, Oct 2026)
- **An answer scale reaches as far as the outcomes you show.** A results question that stopped well
  below what the app's own examples reach looked capped; the options went up to the millions. "when
  I show them they can reach millions, why do we stop here?" (Comma, Oct 2026)
- **Say each thing once in the onboarding, and when a step is cut, cut every mention of it.** A
  feature pitched in the story and again in the demo lost its second place; after the demo's lessons
  were removed, the account screen still listed one among what they had made. (Comma, Oct 2026)
- **Teach the by-hand path as clearly as the AI one.** The onboarding sold the AI and the templates
  and never showed that people can write every word themselves (a later setup step for it was cut
  for its small text, not its purpose). "another thing that we failed to market is the manual script
  writer" (Comma, Oct–Nov 2026)

## Opening, story and plan

- **The opening is the crux.** A short film that shows the dream outcome and plays itself, with no
  Continue until it ends. (Flamely, Oct 2026)
- **A tap hurries, never skips.** What's playing plays about twice as fast and Continue appears at
  once: "a tap means hurry up, not skip what I have not seen." (Comma, Oct 2026)
- **Before and after must be drastic and magical,** never a bar or rows of labels: "this is an ass
  screen ... there should be like some magical stuff." Exaggerate scale, never the facts.
  (Comma, Oct 2026)
- **The plan is earned from their answers.** Never show details they didn't give. (Flamely, Oct
  2026)
- **The screens after the opening are held to its standard:** one connected stage, real things,
  motion that tells the story. Plainer story and plan screens after a strong opening made the whole
  onboarding drop. "the aura of opening screen is just losing" (Comma, Oct 2026)
- **The story's honest part answers what they told you, against a real benchmark.** Someone already
  doing well hears that it's working and what to do next, never the warning meant for someone
  struggling; a comparison with others uses a published study or your own measured data, with the
  source beside the copy in the code rather than as small print under the chart. "what if they're
  getting good views?" (Comma, Oct–Nov 2026)
- **When a question moves later, the story's default never claims they said it.** Moving a question
  into setup left the story on a default value; the copy says what that amount comes to, never "you
  told us". (Comma, Oct 2026)

## Sign-in, consent and AI permission

- **Sign in before the paywall, and log the payment SDK into the account id.** A purchase made
  signed out stayed anonymous and the webhook answered "no user". (Comma, Nov 2026)
- **The success moment lands.** A tick, the character jumps once; a return says "Welcome back":
  "it's supposed to show a tick." (Comma, Nov 2026)
- **AI permission is the app's own sheet,** never a system alert: who writes, what is sent where,
  Allow or Keep writing by hand. "I want that pop-up to be nice." (Comma, Nov 2026)
- **Save a consent answer at the tap.** A delay lost it when the app closed. Present it from the
  root and from inside sheets, because a sheet can't show the root's sheet. (Comma, Nov 2026)
- **Ask each permission where it is first used,** unless the plan depends on it: a permissions
  screen for a camera nobody needs yet was removed. (Comma, Oct 2026)
- **One signal per success: when the character is on screen, it says it alone.** A bigger, happy
  character jumping says "you're in"; a tick beside it was one signal too many. This replaces the
  tick in "The success moment lands" wherever the character is there. "I don't need tick section
  here, simply because the corrector is happy" (Comma, Nov 2026)
- **The tap that asks for a permission still does its job.** After Allow, the recording (or whatever
  was tapped) starts by itself; a first tap that only brought up the system prompt read as a mic
  that didn't work. Guard start and stop so they can't overlap or finish after the person has left
  the screen. (Comma, Nov 2026)
- **Ask for exactly the permissions a capture uses, one after another, before it starts.** Camera,
  then microphone, then speech recognition only when a transcript is used, each input added once
  it's allowed: a microphone added unasked to a running camera put its prompt mid-take and could
  leave the audio silent, and a recorder that asks for speech recognition with the microphone fails
  for anyone who says no to transcripts. (Comma, Oct–Nov 2026)

## Paywall and the offer

- **Hard paywall.** "Currently if I cancel, it just let me in the app, which is pretty bad."
  Closing never lets anyone in; Restore is always there. (Comma, Nov 2026)
- **No free pass in test builds for real users.** The sandbox charges nothing; the free pass lives
  in Debug only. (Comma, Nov 2026, reversing Oct)
- **Prices from the store, in their currency; the trial only if the store says they can have it.**
  Otherwise everything says Subscribe. (Comma, Nov 2026)
- **The trial reminder only for a real trial,** the day before the store's own end date. Monthly
  subscribers were told their trial ended tomorrow. (Comma, Nov 2026)
- **One real offer after the paywall is closed.** "If they try to go back, we need to give them a
  massive discount ... we should not let them go." Real timer kept across reinstall, "free time"
  worked out from real prices, No thanks back to the paywall, never a fallback to full price. This
  replaced "no discount trick on close" (Flamely, Oct 2026). (Comma, Nov 2026)
- **The paywall is defined and never cheap.** One headline, the value, the trial timeline, every
  price, one button, no top bar: "it looks scammy now ... you make it look cheap." (Flamely and
  Comma, Oct 2026)
- **The paywall shows the product working and names everything they get.** Show what goes in and
  what comes out as a picture (a video, its beats, their script) instead of decorative side videos,
  and name every feature plainly with its own icon and room; when many concrete tools are the reason
  to pay, list them all (Comma's paywall has ten, in two columns) rather than three abstract lines.
  "show them a lot more features like what they're gonna get" (Comma, Oct–Nov 2026)
- **A reminder promised before notifications are allowed stays owed.** The paywall promised a
  reminder before the trial ends but scheduled it only if notifications were already on, and they
  were asked later in setup, so nobody got it; schedule it the moment permission is given. (Comma,
  Oct 2026)

## Cancel, deletion, feedback

- **Cancel goes all the way, with "Keep my plan" at every step.** What they made → why → one
  follow-up → one real offer → the store's own sheet → goodbye with dates: "MAKE THE FULL CANCEL
  FLOW A LOT MORE IN-DEPTH." (Comma, Nov 2026)
- **Cancel through the platform's sheet and read the result from the server.** A stand-in marked
  the phone "cancelled" while the store kept billing. (Comma, Nov 2026)
- **Offers must be grantable.** A plan switch, a lighter plan, a real promotional offer; never
  "half off" with nothing behind it. (Comma, Nov 2026)
- **The cancel flow's discount is the store's own promotional offer on the plan they're on**, at
  the same prices as the paywall's one-time offer (one set of numbers to check the margin on).
  Offer it for price, a pause and "something else"; where a better fix exists (formats → request
  content, too much → a lighter rhythm), offer that instead. Show it only when the store returns
  it, in the store's currency; taking it is the store's sheet, and the flow moves on only when the
  store says they stayed: "I WANT YOU TO GIVE THE DISCOUNTS ON CANCEL FLOW AS WELL". (Comma, Nov 2026)
- **Deleting the account is separate from cancelling.** Export first, hold to delete, and say the
  subscription isn't cancelled by it. Refuse signed out before clearing anything. (Comma, Oct and
  Nov 2026)
- **A public feedback board; cancel feedback private.** Votes and statuses in public, reasons in a
  private list the owner actually reads; analytics get the answer, never the words. (Comma, Nov
  2026)
- **Every step of the cancel flow has a direct way to the store's own cancel sheet; the questions
  are optional and the offer shows once.** A pre-submission audit read four or five screens with two
  required answers before Apple's sheet as an App Review 5.6 risk (manipulative practices). This
  replaces the gated order in "Cancel goes all the way": the steps stay, beside the way out, never
  in front of it. (Comma, Nov 2026)
- **The leaving flow is designed like the offer, not like settings.** Plain cards on paper for the cancel steps read as
  an afterthought next to a vivid one-time offer. Every step gets the offer's full-screen sky, big serif type and the
  mascot acting with intent, with a mood per step (calm for the plan, dusk for the questions, the offer's gold for the
  stay offer with its price leading, a warm sunset for goodbye, a quiet one for deletion, which never sells), while
  every rule above still holds: the store's sheet one tap away on every step, optional questions, terms under every
  buy button. "MAKE LEAVING FLOW MORE ATTRACTIVE ... MORE LIKE ONE TIME OFFER" (Comma, Nov 2026)
- **Prove account deletion on production, with a throwaway account, before every submission.** Code and a scheduled
  job that "should" delete prove nothing: Comma's had never once run on production. The check: a confirmed test
  user made with the admin API (never the owner's or the reviewer's), a real password session, a row saved under its
  own permissions, the exact endpoint the app calls, a call with no session that must be refused, then the account
  and every row gone (18-21 s) with the deletion record kept. List every table that holds a user id and doesn't
  cascade from the account. "MAKE 100% SURE ACCOUNT DELTEION AND ALL THE STUFF IS WROKING" (Comma, Nov 2026)

## The app's own screens and AI writing

- **Creating never starts on a blank page.** "If we click on write script, it should never start
  from like a blank page, that is what we are eliminating." Gather their material first, then ask
  how to write it. (Comma, Nov 2026)
- **Context given once is never asked again, and the AI never writes blind.** "I already gave it a
  context and when I was borrowing the shape it was again asking me." (Comma, Nov 2026)
- **Dictation never loses words.** A pause wiped a whole brain dump in a shipped build. (Comma, Nov
  2026)
- **Drafts come back whole, and every version is kept.** "If we wasted credits on that, yes it would
  be better to keep it." (Comma, Nov 2026)
- **Moving between stages never re-runs the AI.** Re-running is an explicit button that says it
  uses a credit. (Comma, Nov 2026)
- **Show AI limits exactly, from the server's own numbers.** "IN SETTINGS ALSO WE NEED AI
  TRANSPARENCY A LOT. SHOW EXACTLY WHAT IS LEFT." (Comma, Nov 2026)
- **Don't give an early stage its own tab.** "The ideas should not have its own screen because I
  have to go to the ideas and then I have to put into the scripts." An unwritten idea is a draft.
  (Comma, Nov 2026)
- **Creation lives where the work lives,** not behind a global plus: "we can remove the plus icon
  cuz it adds no value." (Comma, Nov 2026)
- **Never mix unfinished drafts with ready work.** Status groups in one compact list, finished work
  in its own archive. (Comma, Nov 2026)
- **Get the manual basics working before AI on top.** Select, move, resize, delete: "I can't even do
  basic editing myself, let alone the editing from Claude." (CutRoom, Nov 2026)
- **Every AI button opens a prompt with what and where filled in.** "How does it even know where?
  I can't even prompt it there." (CutRoom, Nov 2026)
- **Delete is always visible, with Undo.** "I CAN'T DELETE DRAFTS." (Comma, Nov 2026)
- **Screens after onboarding are for using, not watching.** Make the core actions really work:
  "I can't even add the entry in my calendar." (Flamely, Oct 2026)
- **Typing never hides the tab bar, and every keyboard has an obvious way out that keeps the
  words.** A focus flag hid the whole tab bar the moment a field took focus, even with no keyboard
  up, and the idea composer's keyboard couldn't be closed; tab-bar visibility follows navigation
  depth (shown at a tab's root), the composer sits clear of the tabs, and switching tabs dismisses
  the keyboard and keeps the unsent words. "the keyboard is not closing on the ideas" (Comma, Nov
  2026)
- **A document editor may hide its navigation bar while typing, with one labelled Done right above
  the keyboard.** The first focus mode hid the bar with no obvious way back; Done clears every focus
  at once (a line and a heading can each hold it), works from a hardware keyboard, brings the bar
  back and shows no save popup, because words save as they're typed. "THE DONE PLACMENT IS SOO
  FREAKING WERIRID" (Comma, Nov 2026)
- **A writing screen is the page itself, edge to edge.** A rounded card floating on a patterned
  ground was rejected; the page fills the screen even when the text is short, its margin runs to the
  bottom, and the pattern stays off every writing screen (editor, free writer, AI draft). "MAKE THE
  SCRIPT WRITING SCNREE FULL PAPPER PLEASE" (Comma, Nov 2026)
- **A page's actions are small, labelled and on one line.** AI actions say what they do in words
  ("Refine with AI") beside the text, also while editing, because bare icons went unnoticed; a big
  "ready" checklist row became a small reversible toggle at the top, which never moves filmed or
  posted work back to writing. "THE WRIITNG OR REFEIREN WITH AI SHOULD BE OBVIOUS" (Comma, Nov 2026)
- **Never lock the editor while AI rewrites it.** Apply the result only to text unchanged since the
  request was sent, never to the line being typed, and let Undo bring the old text back without
  losing newer words. Locking manual writing during a refine was proposed and rejected, because the
  revision-checked merge already keeps newer words; a test types during a deliberately slowed refine
  to prove it. (Comma, Nov 2026)
- **When AI adapts a reference, the person can show the reference's line beside each new line,**
  part by part and even after a line is filled, with their own idea and context at the top. The
  match couldn't be judged until the original could be shown beat by beat. "clearly match line beat
  by beat" (Comma, Nov 2026)
- **Point at what to edit with a drawn hand, and let an empty new line clean itself up.** A "tap
  anywhere to change" caption wasn't enough; a drawn hand points at the line, tutorial style. A new
  empty line shows what to type and removes itself when left empty, a beat after focus leaves, so
  the tap that moved focus to the tool beside it still lands. "is there any way we can just use a
  hand icon" (Comma, Oct–Nov 2026)
- **A count on a button is a notification circle that appears only when there is something.** Posted
  showed a "0" in a different style from Drafts' red badge; both became real buttons in one style,
  the count shown only when it isn't zero. "posted are showing like zero" (Comma, Nov 2026)
- **Coming back to a list finds it as it was left, and a new item opens the group it lands in.** The
  open group, the search text and the filter survive Back (a rewrite lost the open group until it
  was restored), and capture opens the new item's group so it's seen arriving, not filed out of
  sight. (Comma, Nov 2026)
- **Finding ideas starts from a topic; a personal story is optional, never the gate.** Six fixed
  life-story prompts couldn't fit different lives, and someone without a story got nothing;
  topic-first angles (four shown, more on request, each opening to a short brief, kept once) work
  for anyone. "I need ideas from the niches that I worked in" (Comma, Nov 2026)
- **Capturing an idea asks for nothing but the thought.** No required title, category, format or
  date; organising comes later, in categories the person names when they want to. "add the
  categories if I want to, manually" (Comma, Nov 2026)
- **When the app can't do a step itself, hand over a list they can copy.** The app runs no live
  research, so after the AI's questions a specific research checklist can be ticked as already done
  and copied in one tap as a brief for their own assistant; the rest travels with the draft. "I want
  this list to be copyable" (Comma, Nov 2026)
- **Using an item never duplicates it;** it stays one and shows how many times it was used. Building
  from one idea once split it into several copies. "you use this idea one time, so probably show a
  number" (Comma, Oct 2026)
- **A step that needs another tab's content opens it as a sheet over the flow.** Borrowing from the
  library while working on an idea jumped to the Library tab and lost the place. "library should be
  open like directly here because we are following the flow" (Comma, Nov 2026)
- **A count opens what it counts.** An idea that said it had made four scripts didn't show them; it
  now lists each one, tappable. (Comma, Nov 2026)
- **Media at the top of a detail page introduces it; the title and tabs still show on the first
  screen.** A tall video header filled the first screen and hid the page, so it went square across
  the page. "TOP REEL CAN BE LITTLE SMMALER IN MY EYES" (Comma, Nov 2026)
- **A setting that changes an onboarding answer reuses that onboarding screen,** in an app frame,
  without the tab bar; settings had grown their own forms for the same answers. "the screens that we
  are confirming on the onboarding" (Comma, Nov 2026)
- **A share extension says what happened and gets every share to the account.** Sent at once when
  signed in, otherwise the moment the app opens, and a failure says why; a share that silently never
  reached the server read as a feature that didn't work. "I think Instagram sharing stuff is not
  working properly at the moment" (Comma, Oct 2026)

- **Work lists are one bar of tabs that opens on what needs doing now.** A home that split work into a chip for drafts
  and a two-tab bar for the rest read as two systems. One bar of three tabs (the ready-to-do stage first and where it
  opens, then drafts, then done), each with its count (the drafts count red like a notification), and the main create
  button in the centre of an empty tab's page, never pinned under the bar. "make it a 3 tab think ... tabs starts with
  to film and write script button must be incenter" (Comma, Nov 2026)
- **A picker for a person's own collections is a drop-down from the start.** Chips for series, folders or tags work for
  three and break at thirty; a field-like drop-down (None, each one with its count, New…) holds any number. "WE MIGHT
  HAVE ALOT OF SERIS OF CONTENTS" (Comma, Nov 2026)
- **One way in for one job.** An older screen that started a script from a library item, beside the newer "write
  script" flow, confused even the owner ("WTF IS THIS ?"). Every entry opens the same flow with its context filled in
  (the chosen item shown at the top, its option first at the decision step), so there is one flow to learn and fix.
  (Comma, Nov 2026)
- **Settings keep only what a person needs.** Rows that repeat another screen (restore purchases when the subscription
  page and the paywall have it), pages about concepts the product dropped, and anything for a feature this release
  doesn't have read as junk. The setting for an onboarding answer reuses the onboarding's own screen, without the tab
  bar. "REMOVE USELESS STUFF FROM SETTING" (Comma, Nov 2026)
## Porting to native

- **Port UI and motion first, one section at a time; wire services last.** "For all the
  technicality ... we will leave that out for the last." (Flamely, Oct 2026)
- **A debug test bar to jump, replay and loop, never in a build anyone uses.** "In simulator I was
  able to jump between the different screens, that is the most turning point"; later "remove any
  sort of these settings bars." (Flamely and Comma, Oct–Nov 2026)
- **Controls identical to the board's, measured, not eyeballed.** "Button isn't identical." Copy
  the computed style. (Flamely, Oct 2026)
- **Every animation approved on the board reaches the app.** "I'm still not able to see the
  animations that we made on the browser in the app." (Comma, Nov 2026)
- **Native chrome for navigation.** The platform's own tab bar, sheets and alerts: "I wanna keep
  iOS native navigation, the liquid glass one." (Flamely and Comma, Oct–Nov 2026)
- **Support is a help window, not a policy page.** Questions down the left, the open answer on the
  right (a one-line answer as its title, then the detail, then one reassuring note); on a phone the
  same questions open in place. Write each as a `<details>` so it works without script and links by
  id (`/support/#cancel`), and put "email us" and "ask for a feature or report a bug" above it. The
  support page and the public feedback board share one header with two tabs. "I have a feedback
  board ... really nice-looking support sections ... make it for this one as well." (Comma, Nov 2026)
- **A board that was built is not a board that works.** Ship the backend with the page, then post,
  approve, vote and unvote from the real page, and delete the test rows; an undeployed board on a
  live site just says "Could not connect". (Comma, Nov 2026)
- **In SwiftUI, a context menu on a whole row takes the long press from any drag inside it.** Give
  each hold its own target: a row-wide menu swallowed the reorder gesture in the first native check,
  so the menu moved to the heading, and once holding the item meant "move", delete became a drop
  zone at the bottom with Undo. (Comma, Nov 2026)
- **An in-app drag carries a private type only the app accepts.** Otherwise text dragged in from
  another app can reorder the document, and the app's own drag payload can be dropped into a text
  field. (Comma, Nov 2026)
- **A collapsible group's open state belongs to the screen that owns the list, not to the row.**
  State kept in the row dies with it when its last item is deleted, so Undo brought the item back
  into a closed group; owned by the parent, delete then Undo leaves it open. (Comma, Nov 2026)
- **Fast taps never land on two screens.** Ignore a move asked by a screen that is no longer
  showing, let the screen fading out take no taps, and drop a second move within about 280 ms unless
  it is one intended double step; without this, a quick double tap moved two screens at once.
  (Comma, Oct 2026)
- **A second tap on a row while it opens never opens it twice.** Every push goes through one function
  that refuses the route already on top, so a fast double tap can't stack the same screen on itself.
  Inside a choreographed screen, the tap that moves on plays the rest out fast before the next screen
  starts (see ungenerated-motion, gestures). (Comma, Nov 2026)
- **Port the font weight the browser drew, not the number in the CSS.** The browser snaps a weight
  to the cuts it loaded: 650 rendered as Bold and 900 fell to ExtraBold because only 400–800 were
  loaded, so the app uses those same static cuts. (Comma, Oct 2026)
- **Keep a video's poster under the player until its first frame is drawn, and drive its rate from
  the scene clock.** The poster covers the empty layer while the clip loads, and a rate of 0 when
  the scene pauses lets the test bar's pause and slow motion hold the video too. (Comma, Oct 2026)
- **Decoration never takes a tap or sits over a control.** A section's glow reached over the search
  field above it and swallowed its taps, the paywall's hero covered its close button, and a flying
  character had to be kept clear of "No thanks"; turn hit-testing off for anything that only
  decorates, and tap every control in the played flow after placing decoration. (Comma, Nov 2026)
- **Use the platform's real glass on floating controls only, one control at a time.** Content keeps
  the app's own surfaces, older OS versions get a material fallback and Reduce Transparency a solid
  surface; interactive glass on the tab container let a tab tap reach the content underneath, so
  each control keeps its own glass and hit region. "include the actual liquid glass integration into
  the app" (Comma, Nov 2026)

- **The opening's problem includes the AI shortcut.** If the app helps people write, the pain isn't only the blank page:
  many already ask a chatbot and get the lines everyone says. Show both on the same page, one after the other, so the
  ones who already use AI see why it fails. "call a chat GPT, make me a script and it will write a really shit script."
  (Comma, Nov 2026)
- **Waiting on AI is never a still screen.** Even a fast model takes seconds; in the onboarding show the app's own
  working state (the light, the character, short honest status lines), and hand off without a blink when the answer
  lands. "It is like looking like a very weird pause, a big pause." (Comma, Nov 2026)
- **A topic question is one thing at a time.** Not a wall of tag pills plus sub-tags plus a free-text box: pick the
  topic, then the screen becomes only its parts (or a strip you swipe with the pick shown large). "These tabs don't look
  good ... it's too much going on in this screen." (Comma, Nov 2026)
- **A one-time offer is a moment.** It lands with confetti and particles, the character arrives and stays put (a loop
  drifting across the sky reads as weird), and the price billed is the largest number on it ("free" only for a real
  trial, never for a discount). "I was expecting some confetti ... crazy particles. Our character looks so weird, it's
  like floating." (Comma, Nov 2026)

- **Setup before the account, the paywall last.** Let people set the app up (share, reminders, widget, voice) before
  asking for an account, keep everything on the phone and sync it at sign-in, then end the onboarding on the paywall.
  "Shift the whole setup stuff on top of ... account ... we probably ask them paywall at the end." (Comma, Nov 2026)
- **"I already have an account" is a paywall door.** Signing in from the opening must check the subscription and land a
  non-paying account on the paywall, or a hard paywall has a free way in for anyone who ever made an account. (Comma, Nov 2026)
- **How-to steps show one actual phone, the same way every time.** Sharing, the widget, reminders and connecting each play
  on the same device frame, with a finger, a tap and Done; no step list or small notes around it. "I like the phone stuff,
  honestly. Tap done and all that nicer stuff." (Comma, Nov 2026)
- **No bold accent subtitle under a heading.** If a line is truly needed it is quiet ink, regular weight; usually it goes.
  "Why is this orange stuff?" (Comma, Nov 2026)
- **An optional "teach it your voice" step says what happens and why at a glance**: one plain question, tap to talk,
  transcribed on the phone, Skip. "Want drafts that sound like you" alone left the owner confused. (Comma, Nov 2026)
- **A "use it inside your AI" setup step is honest about the tap.** Claude and ChatGPT can't add a connector from a link
  yet: copy the address, open the connector settings, say where to paste; show the step only to accounts that can really
  connect. (Comma, Nov 2026)
- **"One tap to connect your AI" has to really add it.** A screen that copies an address and opens settings reads as
  broken ("I see nothing"). Use whatever really pre-fills the target app's add-connector box (check what exists today;
  for Claude a `customize/connectors?modal=add-custom-connector&connectorName=…&connectorUrl=…` link opens it filled in,
  undocumented), let the app icons themselves be the buttons, and say only the one step left there ("tap Add, then
  Connect"). Then check it where the person looks: install it on their machine before saying it works. (Comma, Nov 2026)
- **Ask for a permission before the sheet closes, never after.** One tap that closed a sheet and opened a page on another
  tab left that page to ask for the AI permission mid-transition; the permission sheet couldn't show, read as a no, and
  the page said "I couldn't write it just now" to a new user who had done nothing wrong. Ask inside the sheet first (the
  way every other AI step in it does), treat a run cancelled by navigation as no failure, and test the path through the
  sheet on a fresh install, not only the page on its own. (Comma, Nov 2026)

## Voice and recording

- **Talking is tap to start and tap to keep, never hold to talk, and a pause never ends it.**
  Holding a button while thinking aloud was awkward, and a step that moved on when the voice stopped
  felt rushed. When they stop, wait for the recogniser's last words (up to a second behind; cap the
  wait near 1.5 s): judging at the instant the finger lifted, the first build said "Didn't catch
  that" to someone who had just spoken. "it should be click, and I can just speak at the bar"
  (Comma, Oct–Nov 2026)
- **Speech recognition uses the phone's own language variant, never a hard-coded one.** Pick the
  device's English (UK, India and so on) or US English, on the device when that variant can run
  there and over the network otherwise; fixed to on-device US English, every mic worked in the
  simulator and fell back to typing on a phone set to another English. "microphone is generally not
  working at all" (Comma, Oct 2026)
- **When voice can't work, say which thing is in the way and offer typing.** Name it (microphone
  off, speech recognition off, the system's Dictation off under Settings › General › Keyboard, no
  recogniser for the language, no sound for three seconds) with Settings one tap away and typing
  always there, and stop retrying once the recogniser ends three times in a row at once. Every mic
  screen in the first phone build failed quietly. (Comma, Oct 2026)
- **A voice-following prompter moves on heard words, never on a timer, and never waits on a missed
  word.** The next script word moves it on; it jumps ahead only on stronger evidence (a long word,
  or the next heard word agreeing), far only when several words in a row agree, and never back by
  itself; numbers match spelled out ("8" and "eight"), contractions count as one word and common
  homophones match. The first one waited on a missed word until it was said again. "it's supposed to
  follow by words, not like automatically do them" (Comma, Oct 2026)
- **Keep the screen awake while someone reads or records from it, and only then.** The prompter
  dimmed and locked mid-take until the idle timer was switched off for as long as it is up. "the
  screen keep dimming off" (Comma, Oct 2026)
- **A recording is saved exactly as filmed.** The app's own words (script, captions, transcript)
  help while filming and are never burned in or laid over the playback. "That transcription is only
  for us." (Comma, Oct 2026)

## Learning and practice

- **A learning tab makes people do the skill, not study facts about it.** The first course taught
  how videos are built and nobody said a word; it became speaking practice (a one-minute topic
  roulette, a story from three words, explain it simply), where every lesson has them speak.
  "actually helping them to speak out speak better, articulate better" (Comma, Oct–Nov 2026)
- **A learning path is only as good as the practice inside each step.** The path was rebuilt while
  its lessons stayed the same, and a prompt plus a timer wasn't enough either; each step needs
  several attempts with one named change per retry, and a dozen sessions that teach beat a long road
  of empty nodes. "It is just simply not giving enough practices" (Comma, Nov 2026)
- **Practice stays practice.** Every speaking exercise can be filmed with the app's real camera and
  saved only when asked; a practice take never becomes a draft, and carrying its text into real work
  is an explicit action. "there's always a film button" (Comma, Oct–Nov 2026)
- **Practice feedback claims only what the app really measured.** The one-minute timer pauses when
  the app goes to the background and says so; there is no score and no claim about what was heard; a
  refused microphone is never shown as a failed skill; and a filler-word count waits until the
  phone's transcription is known to keep "um" and "uh". (Comma, Nov 2026)
- **Gamification stays calm.** Points only for real milestones (a take, a post, a lesson, a practice
  round), none for writing, catching ideas or opening a page, and writing keeps the streak quietly;
  a league, if there is one, lives on a profile-type screen off the main pages and never shows
  made-up people as real, which a pre-submission audit flagged as an App Review risk. "it's giving
  me XPs for writing" (Comma, Oct–Nov 2026)
- **Every day of a learning road is the practice itself, on the screen the store shows.** Quiz screens (multiple
  choice, put-in-order, pick one) felt like homework next to the store screenshot of a person practising out loud.
  Each day is one exercise on that same screen (the day's skill in one line, a topic, a timer, start), and finishing
  it is the lesson; free practice stays one tap away and must fit the width (a chip cut off at the edge reads as a
  bug). "NOT THESE MUTLIPLE QUESTION SHIT" (Comma, Nov 2026)
- **Rewards are for milestones people are proud of.** Daily quests for small things (spot three, finish one, film
  one) cheapen every reward. Achievements are real milestones in tiers (10, 25, 50, 100 scripts; 10, 25, 50 videos
  filmed and posted; 30- and 100-day streaks), shown as a moment (the paywall's sky, the mascot presenting the
  nearest one with its progress), and a stamp not earned yet is a "?" with no name, so there is something left to
  discover. "PLEASE DONT GIVE AWARD ON SIMPLE THINGS ... MINI VERSION OF PAYWALL" (Comma, Nov 2026)

## Connecting the app to an AI assistant

- **The connection looks like the app at every step, or it reads as a scam.** A working, standards-correct connector
  still felt fake to its owner: a developer's free subdomain in the address bar, a bare sign-in page with the brand as
  plain text, the auth server's random address on the identity provider's page, and a consent page written as a
  security warning ("the app chose this name itself", "this address is a program on this device") for assistants the
  app knows. Serve it from the app's own domain, in the app's look, name the assistant with its real icon (recognise
  the known ones by their verified return address), and keep the warnings for unknown apps only. "ITS TREMENDOUSLY
  WEIRD AND SCAMMY" (Comma, Nov 2026)
- **In the app, the person picks their assistant by name, then taps Connect.** Icons alone were unclear; two named
  choices (Claude, ChatGPT) under a phone that shows the app working inside the picked one, and one button that says
  which ("Connect Claude"). "SELECT THE CLAUDE AND CHATGPT NOT THEIR ICON ITS VERY UNCLEAR" (Comma, Nov 2026)
- **List the connector in the assistants' own directories before promising "one tap".** A listing gives the trusted
  front door (the app's name, icon and a Connect button inside the assistant); the directories review the sign-in
  pages, want a setup page, a privacy page, support and an icon, and need a reviewer login. Sign in with Apple can't
  be shared with a reviewer, so a second provider (Google, with a dedicated reviewer account on a comped plan) is part
  of the listing work. (Comma, Nov 2026)

- **Built feedback leaves the board at once.** As soon as a note is built, delete it from the board's notes, side by side
  with the work; re-read the notes first and delete only the ones actually built (a new note can arrive while you work),
  keeping a backup. "Please implemented feedback should be removed from the notes ... always clear feedback on board side
  by side as soon as possible." (Pip, Nov 2026)
- **No "whole part" cards on the board.** A card that plays a section's screens in a row duplicates Play the flow and
  slows the board. "Remove the screen where it shows full flow, that is not needed." (Pip, Nov 2026)
- **The board is still by default.** Dozens of moving phones make it slow: every card is a picture of its screen, a
  Still/Moving switch plays them all, and each card has its own play button that shows that one screen big and moving.
  The switch is the board's, never the app's Reduce Motion, or the phone build goes still too. "Make the screen still
  with no motion cuz it makes things slow ... on each screen there should be an option to see that specific screen fully
  in motion." (Pip, Nov 2026)
- **A screen that teaches never moves on by itself.** The opening film and the story stop at the end of each beat with
  Continue; a tap at a pause goes on, a tap while it plays runs it at twice the speed to the next stop, never skipping.
  A scene that starts at a pause starts past it. "Take nice pauses on screens where we are educating, don't auto move,
  take Comma's philosophy: tap to 2x the screen speed." (Pip, Nov 2026)
- **No mascot inside the questions; the mascot is the progress bar.** He crawls along the top as the questions go, so
  the answers have the whole screen. (Pip, Nov 2026)
- **Ask only what changes the plan, the way the person would say it.** A question the story can assume goes ("remove
  this"); a this-or-that duel becomes one grid of categories ("only take categories, we don't need this selection");
  languages are many, not one ("people can speak multiple languages"); ask about their experience, not a label
  ("while looking a word up, do you get distracted?"). After changing the options, check Continue is still on screen.
  (Pip, Nov 2026)
- **Answer cards wear the app's colours.** Time-of-day bands in generic sky colours "don't match my app's branding":
  tint them from the accent and the gold, deepening to night. (Pip, Nov 2026)
- **No consent screen and no camera ask up front.** Analytics are on with a switch in Settings (the owner's call), and
  the camera is asked for when the reader first points it at a page. Hard paywall; one exit offer (two weeks free) with a
  real timer. (Pip, Nov 2026)
- **A "you forget it" beat shows what was found before it fades.** The search finds the meaning under the word; then
  word and meaning fade away together as the weeks go. "Show the meaning at least, and both word and meaning kinda fade
  away." (Pip, Nov 2026)
- **End the opening on the promise, in the product's own medium.** Not a fill-in card with a dashed box: the kept word
  flies out of its book into the blank in a line of a book page and a highlighter marks it there, as the first scene
  marked it. "Any creative direction we can take here?" (Pip, Nov 2026)
