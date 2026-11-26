# What we learned, and why

Lessons from reviewing real apps with their owner (Comma, a script-writing app; Flamely, a time
tracker; Pip; CutRoom, a video editor). Each one transfers to any app. Best first within each group.

## Proving it works

- **Nothing reaches the owner until it works on a real phone.** Sign-in, AI calls, every button:
  "80% of things are not working"; "it's sloppy itself, nothing is really fixed." (Comma, Oct 2026)
- **"Written, compiles, never seen running" is not done.** Run a clean install, the real launch
  path, every control tapped: "This app's supposed to be production ready, but it's clearly not."
  (Flamely and Pip, Nov 2026)
- **A bug reported twice gets a real-input stress test,** not another look. The age ruler was
  "fixed" and reported again 18 times; a diagonal drag reproduced it. (Comma, Nov 2026)
- **A check counts only if it really exercised the thing.** It must fail on any failure line it
  prints and show its target was reached. One printed FAILED lines and still said "Everything
  held"; another passed because nothing was left to test. (CutRoom, Oct–Nov 2026)
- **Check order for any flow: tap tests, then the events, then the money, then screenshots.**
  Each catches what the one before can't. (Comma, Nov 2026)
- **Confirm events in the analytics tool itself, not in the code.** "PLEASE END TO END CONFIRM THE
  ANALYTICS POSTHOG EVENT." A closed sheet had been logged as "subscribed". (Comma, Nov 2026)
- **Fast double taps must never skip a step, delete twice or flip a rating.** "If I tap quickly,
  it's overlapping with the previous screen"; one star tap removed another. (Comma, Oct 2026)
- **Losing user text is a showstopper.** A pause in dictation wiped a brain dump in a shipped
  build. (Comma, Nov 2026)
- **Test the installed build the way a user would,** not the dev server: "that's how users test."
  The dev server was smooth while the installed app stuttered. (CutRoom, Oct 2026)
- **Test with Reduce Motion on and on the oldest phone in use.** The owner's phone froze the
  character under Reduce Motion and lacked the on-device model. (Comma, Oct 2026)
- **Check every number on screen against its source, then add a guard.** "You wrote wrong prices
  in the second video ... never make these mistakes again." (CutRoom, Oct 2026)
- **Prove it from a clean state.** Wipe the test data, run it end to end, show the owner: "so I can
  clearly see that it is working." (CutRoom and Comma, Oct–Nov 2026)
- **Prove a crash fix on the device that crashed, installed over the crashing build with its
  account and data, not on a clean install.** The launch crash hit only signed-in people, so debug
  fixtures and a fresh install never showed it; the fix went over the bad build with the data
  backed up, and the same account and every item were checked before upload. (Comma, Nov 2026)
- **When testing on the owner's phone, back up its data first, then read its data, the AI log and
  the crash reports yourself.** He does the tapping and you report what happened, instead of
  asking him to describe it: "let me do the testing, and then we get the report" (Comma, Nov 2026)
- **When a bug comes back after fixes, record what the person sees frame by frame and check every
  element on screen, not only the control you assume.** The ruler behind 19 reports was fixed
  twice in its drag gesture; the real fault was the number above it, whose spring bump restarted
  on every step until it ballooned and vanished: "THE NUMBER GETT BIGGER AND VANSISHES" (Comma,
  Nov 2026)
- **Test voice features with recordings fed in as the microphone, and assert where they stop.**
  Follow each recording with silence (a recogniser gives its last word only after a pause), add a
  missed word and a long pause, run it on every recogniser the app uses, and check the spoken word
  stays on the reading line. Never open the live microphone on the simulator: it timed out Apple's
  audio service and aborted the app mid-test, so there it reports no input. (Comma, Oct–Nov 2026)
- **Tap tests never spend money.** UI tests run AI steps on a fixture that checks interaction and
  consent, test simulators don't reach the real AI service unless asked to, and checks that call
  the paid model are opt-in. (Comma, Oct–Nov 2026)
- **Test deleting the last item as its own case.** A page emptied of its last section offered an
  Add that didn't start a new page, and the switch to the empty state must not drop a composer's
  unsent words; only tests that delete the last one and add again caught them. (Comma, Nov 2026)
- **Give the server a test-push path and prove the whole chain on a real phone before relying on
  push.** A signed-in person can queue one test push to their own phones, one a minute, which
  exercises the key, the token's environment, the outbox and the sender at once; the first one
  reached Apple the day the key landed. (Comma, Nov 2026)
- **An assistant integration works only when the whole loop passes on the real clients,
  disconnect included.** Save from the assistant, get the durable receipt, find the same item on
  the phone after refresh and restart, disconnect, then prove the next save is refused; local
  tests and a deployed server are not that proof, and Connect isn't offered before it. (Comma,
  Nov 2026)
- **Open every screen on its own when checking for errors, not only the page that holds them.** A
  board that loads clean can still hold a screen that throws when it builds; after a shared helper
  or style changes, sweep every screen under every style, and capture a screen that branches on
  earlier answers once per branch. (Comma, Oct 2026)
- **Sweep every playable screen for dead controls before showing it.** Every control opens a
  screen, goes back or acts, and a hand-off to the system (mail, the browser, the store) answers
  with a message; a script that taps them all reports the count every round, and it must be zero:
  "every screens kind of work out" (Comma, Oct 2026)

## Builds

- **Before handing over a build, confirm it is the newest and carries every change.** "WRONG
  BUILD"; "DID YOU CHECK IN ALL THE CODEX CHANGES AS WELL?" Check the version, the build number
  and other agents' work. (Flamely, Comma and CutRoom, Oct–Nov 2026)
- **Test in the simulator before any build, and open it for the owner.** "NEXT TIME OPEN SIMULATOR
  SO I CAN DO IT." (Comma, Nov 2026)
- **One simulator, tests one after another.** "PLEASE ONLY USE 1 simulator." Parallel runs filled
  the disk and made checks flaky. (Comma and CutRoom, Nov 2026)
- **Make a tester build only when the owner asks for one; until then each round ends in the
  simulator, and you say when his phone is behind.** He handed builds to the agent, then took them
  back while the screens were still changing; the latest word wins, and it replaces "builds are
  your call": "we do not want to make build right now" (Comma, Oct–Nov 2026)
- **Before a build goes to the owner's phone, check the backend end to end and report what works,
  what doesn't and what only he can do.** Sign-in, data and its access rules, functions, sync,
  content delivery, payments, queues, push and analytics each get a line; a build on a
  half-working backend wastes his test: "give me full stuat report on the backend as well before
  you do so" (Comma, Oct 2026)
- **Run the checks on the exact frozen commit you upload, in one clean run, and call the build
  ready only when Apple says it is available to test.** One upload came from a commit carrying a
  later round that the full tap suite never ran on; an accepted upload can still be processing or
  fail, so the notes keep "uploaded" and "available" as separate lines with their times. (Comma,
  Oct–Nov 2026)
- **Ship the riskiest feature to testers alone first, as a bare test tool.** The voice-following
  prompter went out early on its own (paste any text, record a real take, save it to Photos), so
  it met a real phone and a real voice before the rest was ready: "That is all I need ... put the
  test flight right now" (Comma, Oct 2026)

## The slop gate

- **The default AI look is slop.** Indigo and violet, the trendy serif-plus-grotesk pairing,
  generic gradients, sparkles, persona labels, invented stats, corny promises, faded full-screen
  cards, cards that are only big text: "ALL OF THAT SCREAM AI SLOP TO ME." (Comma and CutRoom,
  Oct–Nov 2026)
- **Hunt the small tells he named:** rounded chips inside text, little nuggets on cards, tabs
  nobody needs, icons added to headers, "Typed just now" stamps, a date header on a screen that
  isn't a calendar, small text, shadows behind icons: "these rounded stuff and within the text,
  like little stuff ... the tabs and the little nuggets." (Comma, Oct–Nov 2026)
- **Never the sparkle icon for AI.** "You do not want to show this weird AI symbol"; "I hate the
  icon of the stars." (Comma, Oct–Nov 2026)
- **No small text.** "No one is gonna read that, so you have to be very clear with the headings."
  (Flamely, Oct 2026)
- **No boxed or double-outlined cards.** "I do not like the boxed look ... I like independent
  look." (Flamely, Oct 2026)
- **No step counters.** "Why do we have step one of four? Why are you showing that?" (Flamely, Oct
  2026)
- **Real brand icons only.** The App Store drawn as a phone emoji, Google Docs as a drawn tile:
  "it's not an icon." (Comma, Oct–Nov 2026)
- **Never add text for the sake of text.** An empty moment, with the reason written down, is a
  valid result: "IT ADDS ASS TEXT ON MY VIDEOS." (CutRoom, Nov 2026)
- **Unslop everything, not only what was named.** Repeats, captions that say nothing, decorative
  icons: "all these little things kind of matter a lot." (Comma, Oct 2026)
- **Turn each repeated tell into a lint rule** so it can't come back. A project's taste notes grew
  about sixty regex checks this way. (Comma, Oct 2026)
- **Measure alignment and gaps; don't eyeball them.** "ALIGNMENT ISSUES"; "there's no right and
  left gap." Anything called fixed must survive a close look. (Comma and Flamely, Oct 2026)
- **Measure jitter frame by frame** on every screen with springs. "SCREEN KINDA JITTERY."
  (Comma, Oct 2026)
- **Capture motion in real time.** Headless virtual time freezes animations mid-way and makes
  working screens look broken. (Comma, Oct 2026)
- **Make quiet elements dark enough to see.** Slider tracks were "nearly invisible" on the phone.
  (Flamely, Oct 2026)
- **Point every taste lint at the whole product, the app's source and copy included, not only the
  prototype.** The sparkle banned on the board came back in the app on AI writing, credits and the
  permission sheet, and an old turnaround promise survived in three app strings after the board
  had changed. (Comma, Oct–Nov 2026)
- **Review every new screen against the kit's shared parts before it ships.** An independent read
  of one new settings screen found private copies of colours and font weights, a second
  destructive red, a plain ground missing the pages' pattern and its own press motion without the
  shared Reduce Motion handling; each fix is the shared part, checked light, dark and at large
  text. (Comma, Nov 2026)
- **The Continue button is the word alone,** with no arrow chip or circular arrow inside it. It was
  among the first tells removed and is linted since: "continue button should not have the circular
  arrow" (Comma, Oct 2026)
- **Check that every glyph really draws: emoji on hardware, icon names against the set.** An icon
  name missing from the set drew nothing, silently. When only the simulator shows emoji as boxes,
  reproduce it outside the app before touching anyone's text; here it was the simulator, left for
  a device check. (Comma, Nov 2026)
- **Measure whether text overflows by the words, not the box.** A label that doesn't wrap can run
  into its neighbour while its box looks fine: four of a paywall's ten perk labels passed their
  margin at 13 pt. (Comma, Nov 2026)
- **Capture screenshots one at a time.** Several headless browsers loading one local preview
  server at once came back blank or "can't be reached", which looks like broken screens. (Comma,
  Oct 2026)
- **Check a looping animation at exact moments:** pause every animation at the same time and take
  one shot per moment. Real-time shots land wherever the clock happens to be; three timed runs
  never caught a character's clapper shut. (Comma, Oct 2026)
- **Prove motion with pixels, not a look:** two screenshots a beat apart and the difference over
  the moving part. A character that read its clock inside its own drawing stood still across the
  app for days, and one screenshot shows a pose either way; the same difference with no input
  ranks a flow's stillest screens, so motion goes where it is missing. (Comma, Oct 2026)
- **Judge timing from logged timestamps and looks from a recording; never timing from a
  recording.** Recording the simulator slows it, and a scene clock capped per frame slows with it,
  so a recorded film looks slower than it runs; log each screen's start against wall time and
  compare it with the design's milliseconds. (Comma, Oct 2026)

## Showing the owner

- **A round isn't delivered until the owner sees it.** Serve with no caching, version every asset
  link, open a fresh URL and check the served files carry the change: "WTS YOU DID I DIDNT SEE ANY
  CHANGE?" (Comma, Oct 2026)
- **Never ask the owner to pick what he can't see.** Open each option, link each one, side by side:
  "the paywall, I want you to show me, like I can't see." (Comma, Oct 2026)
- **Clear the owner's own test data before a review round.** "I've written a lot of scripts, and I
  do not want them to reflect here." (Comma, Oct–Nov 2026)
- **Short status: where we are, what's next, what's his and what's yours.** "CUT THE CRAP AND TELL
  ME WHERE WE ARE AT." (Comma, Nov 2026)
- **Never go dark on long jobs.** "You're saying you didn't build anything for the past 9 hours?"
  (CutRoom and Comma, Nov 2026)
- **Before acting on the owner's verdict, check which build and which data it came from.** He
  judged AI scripts by output from before the fix ("the scripts arent good it needs 1:1"), and was
  once asked to pick a screen that wasn't on his phone yet. (Comma, Oct 2026)

## Running rounds

- **Log every point of feedback first, then change things.** Number each note; the log is the open
  list: "I'm telling you this again and again." (Comma, Oct 2026)
- **Converge: keep what was picked, change only what was flagged.** "Refine the first design
  instead of changing everything." (Comma, Oct 2026)
- **Apply feedback exactly where it was aimed.** Over-applying a correction across the whole app
  made things worse. (Flamely, Oct 2026)
- **When the owner can't put it into words, show two or three working variants.** (Comma, Oct–Nov
  2026)
- **When the owner says you've misunderstood, stop and restate it in their words.** "YOU NOT
  GETTING ME." (CutRoom, Nov 2026)
- **Every round improves the skill.** Turn every lesson and every bug into a rule the next session
  reads: "SYSTEMIZE IT SO WE DON'T HAVE TO DO IT AGAIN." (Comma, CutRoom and Flamely, Oct–Nov 2026)
- **When a whole set is rejected without a reason, ask what's off, or show two or three directions
  for one screen, before rebuilding the set.** Thirty-five styled onboarding screens were rejected
  in one line ("looks ass tbh"); the reasons, no motion and wretched layouts, came only when
  asked. (Comma, Oct 2026)
- **When a picked screen gets new data or a refactor, capture it beside its last approved version
  before showing it.** Serve the approved commit beside the current one and capture the same
  screen on both: moving a library to live data silently swapped its picked tiles for another
  card (squashed tiles, one word per line, the New tag gone): "I LIKED THAT 1 reel format better"
  (Comma, Oct 2026)
- **A script that starts a browser takes it down with it.** Screenshot runs were stopped by a timer that killed the script
  and left its headless browser alive, each one still drawing a moving board. With several helpers taking pictures, 36 of
  them piled up, the load average passed 190, helpers stalled and an hour was lost while the owner waited. The script
  kills its browser on exit, on every stop signal and at its own time limit; a helper ends with the count of headless
  browsers at zero; and when a machine slows, the process list is read before anything is blamed. (Pip, 27 Nov 2026)
- **Resume a stalled helper, don't restart it.** A helper that stops mid-task keeps its context when it is messaged again;
  a fresh one repeats an hour of reading. Tell it what happened, to check what was left half-done, and to carry on. (Pip,
  27 Nov 2026)

## Accessibility

- **Assert touch-target sizes in UI tests, native controls included.** A system toolbar button
  measured 36 pt on every run and had to move into the content to get a real 44 pt target; a
  status pill keeps its 36 pt look inside a 44 pt hit area. (Comma, Nov 2026)
- **Give every gesture-only action an accessibility action.** Hold-to-move and drop-to-delete
  can't be done with VoiceOver, so each movable item offers Move up, Move down and Delete as
  accessibility actions. (Comma, Nov 2026)

- **Look at the first frame of every scene card.** A card cut from a longer film opened on the pause that ends the scene
  before it: last scene's title and a Continue button. (Pip, Nov 2026)
- **A removed screen takes its code with it.** Delete its helpers, its styles and its references in the order and the
  flow, then load every screen on its own and confirm no errors; a half-shelved screen left the whole file unparseable.
  (Pip, Nov 2026)
- **Measure the board, not a feeling.** Long tasks while it loads and for three seconds after: still cards cost a burst
  at load and nothing after; moving cards kept a quarter of the main thread busy. (Pip, Nov 2026)
