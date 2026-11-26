# What we learned, and why

The motion rules in this skill came from real rounds with one owner. Each lesson: the rule, the reason
(his words where he said it), and where it came from. Comma (a script-writing app), Flamely (a focus
tracker, phone and desktop) and CutRoom (a video editor) are the apps; their exact looks and characters
are examples only.

## What moves at all

- **App screens don't animate in; only achievements, popups and moments of change move.** "If it's not
  an achievement or it's not a pop-up, I do not want it to be animated ... this is an app and I want to
  experience it that way." The onboarding, by contrast, should visibly move. (Comma, Oct 2026)
- **Every animated element adds meaning; never one to fill space.** "Make sure it's clearly adding
  value." (CutRoom, Oct 2026)
- **Make every effect slightly less than your first instinct.** "Make the shake of the icons slightly
  less"; attention belongs on the words, not the effects. (Comma, Oct 2026)
- **One idea per move.** Landing proof and structure in the same motion cost coherence. (Comma, Oct 2026)
- **If text entrances are wanted, one soft blur-in from one shared helper, the same everywhere, and it
  never shifts layout.** "All the text across the app should have that nice animation, the blurred
  one." The first helper's side padding shipped every centred title 8 pt off centre. Ordinary app
  screens still don't move in as a whole. (Comma, Oct–Nov 2026)
- **A heading that holds a live part (a counting number, nested pieces) rises as one block; only plain
  headings split into lines.** A line-by-line entrance rebuilds the heading's text, which would
  replace a number the screen is still counting. (Comma, Oct 2026)

## Continuity

- **One hero travels and each scene grows out of the last.** His favourite moment was a phone turning
  into a laptop: "it's seamless. I love it"; "it needs to be seamless, it doesn't need to be a
  transition". (Flamely, Oct 2026)
- **Camera moves are one continuous animation, with no stop between a zoom and a follow and never an
  empty frame between beats.** "It's not smooth, the zoom in on the first frame." (Comma, Oct 2026)
- **Nothing is cut off by the frame by accident.** "It zooms to the point that the Mac cuts out." A
  half-phone crop on purpose was liked. (Flamely, Oct 2026)
- **Let colour carry the story.** A scene that starts grey and gains colour when the hero comes alive
  was loved. (Flamely, Oct 2026)
- **After recording, the camera view settles into the player in one move, no cut.** (Comma, Oct 2026)
- **Keep the frame still and move only the content.** "What reads as polished is a frame that never
  moves"; the owner approved that direction from research into his desktop app. (Flamely, Oct 2026)
- **After a transition, nothing from the last screen stays hanging on top.** A leftover emblem
  floating over the next screen was the first thing the owner flagged. "on top, we do not want this
  freaking thing going on" (Comma, Oct 2026)
- **Never crossfade between grounds of very different tone; cut under a whip or a push.** In a film,
  blending near-black into cream passed through a muddy grey and near-black into orange through brown,
  so every tone change became a clean cut hidden under a move. (Comma, Nov 2026)

## Feel

- **The jelly press: quick in, springy out.** In to about 0.93 and 1.5 pt down in 80 ms, out on a loose
  spring (SwiftUI `.spring(response: 0.42, dampingFraction: 0.4)`). "Buttons are flat" became "I really
  like the feel of the buttons now"; "iOS defaults don't feel good, a little bubble makes it ours".
  (Comma, Oct 2026)
- **Press and selection are fluid, never rigid, clicky or "chittery"; an icon never swaps while
  pressed.** "The feel of clicking everything matters to me." (Flamely, Oct 2026)
- **Bubbly, never childish.** "Bubbly is a modern, catchy, good feel; childish is too much of it."
  (Comma, Oct 2026)
- **Things glide in; they never pop, jerk or twitch.** "The popping out of the stuff in the plan
  doesn't look good, it's just jerking out." (Flamely, Oct 2026)
- **Haptics fire on the peak and by meaning.** A selection tick on a step, success on completion, never
  on everything. (Comma, Flamely, Oct 2026)

## Nothing buzzes

- **No element bounces back and forth or gets bumped repeatedly; when several things land on one
  target, it settles once. Measure frame by frame.** "Screen kinda jittery"; "certain jerks and
  jittering". (Comma, Oct–Nov 2026)
- **Zero layout jitter: nothing resizes or re-flows while something animates or is dragged; test at the
  smallest size.** "It still jitters at a small size"; header text jittered while a slider moved.
  (Flamely, Oct 2026)
- **Offset the phases of looping illustrations so a grid never pulses in unison, and in a picker let
  every tile play, picked or not;** picking adds the ring and the check. This replaces "animate only
  the picked ones": still tiles read as broken in a real build. "keep these animaton but play the
  animation" (Comma, Oct 2026)
- **Anything that animates on a tap survives taps faster than its animation.** "If I click every week
  and move promptly, it breaks; it shows grey stuff." Set targets declaratively; one cancellable
  animation per element. (Comma, Oct 2026)
- **A shadow never moves on its own.** Tilting gift cards whose shadows shimmered: "shadows are jitter here from the cards
  ... do deep audit and fix that". A blurred shadow redrawn every frame (box-shadow or filter: drop-shadow on something
  that transforms, or animated itself) flickers. The object and its shadow are two layers; the shadow is still and
  pre-blurred and moves only by transform and opacity; nothing that turns in 3D carries one. Prove it with pictures taken
  along the motion. (Pip, 27 Nov 2026)

## State changes

- **Nothing flat flips; a change of state is a swap.** A drawn character or badge flipping shows it is
  a cut-out: "remove the flipping of the 2D graphic completely". (Comma, Oct 2026)
- **No slide-and-blur swap on changing numbers or labels;** while a control moves they crossfade in
  place. "I generally do not like the text swapping animations." (Comma, Oct 2026)
- **Animate numbers by their meaning: money rolls like a slot machine, time flows.** "For the money I
  wanted a slot machine ... that looks lovely." (Flamely, Oct 2026)
- **When a limited resource is spent, show it moving:** a spark flies from the action to the counter,
  which rolls down, plus a short toast. He picked that from three options side by side. (Comma, Nov 2026)
- **The AI working has one signature:** a thin light running exactly on the edge of the card it is
  reading, the original visible first, then the new words written in. No glow, no spinner, no dark
  trail, no second card behind; every card it reads gets the effect. "I like it, I want that in the
  app." (Comma, Nov 2026)
- **Cap the AI's writing animation: one line at a time at a readable pace (about 2.3 s a line), faster
  when many lines change, under about 8 s in all.** It stays a signature, never a wait on top of the
  model's own time. (Comma, Nov 2026)
- **A gradient that fades out ends on its own colour at zero opacity, never on clear.** Clear is
  transparent black, so the AI light's trail faded through a dark band in the app until each stop
  ended on its own colour at opacity 0. "I don't like the black trail that it has" (Comma, Nov 2026)

## Gestures

- **A control owns every drag that starts on it; the page never moves with it.** "I've reported this
  bug eighteen times now." Never pick the gesture by direction: a real finger's first points are noisy.
  (Comma, Oct–Nov 2026)
- **A flick glides straight onto a step, capped, without overshooting and coming back.** "When I slide
  really fast, the 56 kind of shoops in and then moves out." (Comma, Oct–Nov 2026)
- **Drags follow the finger 1:1 and values change smoothly.** "The daily goal and the time is not
  smoothly changing at all." (Flamely, Oct 2026)
- **Reorder by holding the item: it lifts, the others flow around it; no grip handles.** "When I click,
  it just smoothly comes out and I can move it around"; "I do not like the three dots or three bars".
  (Comma, Nov 2026)
- **A tap hurries an animation and never skips it.** "It should bring the animation to the end, but not
  skip it"; Continue appears at once, a second tap moves on. (Comma, Oct 2026)
- **The tap that moves on plays the rest of the screen out first, fast; it never cancels its pending
  beats.** The opening's second tap jumped to the next screen mid-hurry and dropped the old screen's
  later beats, the ones that hide its card, its page and an app icon, so they stayed on under the
  next screen: "IF I TAP TAP TAP TAP CRAZIY ... everything OVERLAPPSS AND EVERYTHING LOOKS SO ASS".
  Now the rest plays in about 0.24 s in its order (no haptics while it races), then the next screen
  starts; taps meanwhile are ignored; a debug assert checks each screen starts with the last one's
  layers gone, and a tap-storm test runs it. (Comma, Nov 2026)
- **Build hold-to-lift as a short long press (about 0.3 s, 8 pt of slack) sequenced before the drag
  and attached to the whole item as a simultaneous gesture.** Then a swipe still scrolls and only a
  hold lifts; switch it off on the line being typed, heard or rewritten, where a hold already means
  something else. (Comma, Nov 2026)
- **Keep a hold or a lift in gesture state, which resets when the system takes the touch away.** A
  cancelled touch (an alert, a call) never runs the end handler, so a hold kept in a flag set on
  change and cleared on end was left running; read the press through the gesture's own state
  (`@GestureState` in SwiftUI) and time the hold on the clock. (Comma, Oct–Nov 2026)
- **Save a reorder only after the lifted item has settled, with animation off; while it is up, the
  list scrolls only at its edges and only the way the finger is going.** Saved while things still
  move, the list jumps on drop, one of the things the owner ruled out. (Comma, Nov 2026)
- **A drop target's hit area is its visible shape and the edge below it, and never overlaps the band
  that auto-scrolls the list.** A padded delete zone swallowed drops meant for the last rows and
  covered the edge-scroll band; a debug-only position log caught it before it shipped.
  (Comma, Nov 2026)
- **A scroll-based picker takes its value only from the finger.** When layout or code scrolls it (on
  appear, after a resize) it returns to its value: `scrollTo` ignored a padded edge margin, the extra
  scroll on appear moved a time ruler, and the ruler saved that as its value. Build edge margins as
  views, not padding. (Comma, Oct 2026)

## Pacing

- **The opening plays itself, with at most one meaningful tap and one final call to action.** After
  every beat was made to need a tap: "That sequence is supposed to play itself." (Flamely, Oct 2026)
- **Keep the opening short (about 20 s), but hold each hard idea long enough to read.** "30 seconds is
  too much"; "this section is so quick I can't comprehend it"; "add about one second to each of these
  frames". (Flamely, Comma, Oct 2026)
- **Explainers are motion that plays through;** Continue comes when the idea has played. (Comma, Oct 2026)
- **No progress or story bars on hook and story screens.** "Remove this." (Flamely, Oct 2026)
- **On a paywall, the motion happens on the way in;** once landed it is nearly still, apart from a
  subtle living background. (Flamely, Oct 2026)
- **Motion graphics over video cut in and out sharply; only the motion inside them is smooth.** "Fade-in
  effects suck ... sharp jumps, and motion within them should be smooth." This is for overlays on video,
  not for app UI. (CutRoom, Oct 2026)
- **Proof belongs on the item from its first frame, not at the end of a sequence.** Likes and hearts
  that arrived on a reel only at the end read as an afterthought. "the first frame is supposed to show
  the heart, like sign, not the end frame" (Comma, Oct 2026)

## The character

- **One character on a screen; it visits and is never parked or circled.** "We do not want a lot of
  characters here and there"; "I don't really like the circle around this character". (Comma, Oct 2026)
- **It is always alive and has no glow.** "The character isn't animating in the app"; "I hate the glowy
  character". (Comma, Oct–Nov 2026)
- **It reacts to real moments, not to every tap.** A tick and a jump on sign-in; "if the mascot moves on
  every tap it kills its sacred moments". (Comma, Oct–Nov 2026)
- **Big enough to read, with moods and roaming eyes; no soft blush.** He asked for about 45% bigger
  across the board. (Comma, Oct 2026)
- **The identity mark is used whole, with nothing glowing behind it.** (Flamely, Oct 2026)
- **A character walking a short distance slows down so it still takes steps.** At its normal pace
  (about 340 pt a second) a 60 pt walk is one step and reads as a slide, so the pace comes from the
  distance. (Comma, Oct 2026)

## Reduce Motion and shipping

- **Reduce Motion removes big jumps only; small in-place loops still play, and nothing freezes
  half-way.** The owner's own phone had it on, and the character froze in a build. (Comma, Oct 2026;
  Flamely, Oct 2026)
- **Every animation approved on the board ships in the app; check them side by side.** "I'm still not
  able to see the animations that we made on the browser in the app." (Comma, Oct–Nov 2026)
- **For ambient motion natively, drive one timeline at a modest rate** and animate values, not state on
  every frame; it kept a 120 Hz phone cool. (Flamely, Oct 2026)
- **Hand the hero from one section to the next.** When one section takes a single item apart and the next shows the
  collection, open the collection on that same item alone, then let the rest arrive around it ring by ring as you scroll
  (pinned, the count climbing), ending at a generous size. An endless auto-scrolling loop of tiles reads as filler.
  "Every reel has a shape ... should be really nicely translating to that library that grows ... it's just moving like
  vertically ... an endless loop." (Comma, Nov 2026)
- **A mascot acts out the screen's job: entrance, job, exit.** It drops in and lands with its own sound move (a slate's
  clack), says one line, tries each option for size (a hop onto each, a wink), waits between them; on the pick it leaps
  into the chosen app's icon, which pops and keeps a small badge of it. One leap, not a jump-then-dive: two arcs back to
  back read as a double bounce on a frame-by-frame jitter check. "Make more of his animation, be creative." (Comma, Nov 2026)
- **Swapping the footer's buttons must not move the page.** Later and Continue share one grid cell (or a fixed-height
  slot); hiding one and showing the other with `hidden` changes the footer's height and shifts everything above it.
  (Comma, Nov 2026)
- **When porting, pose before position: scale, rotate and blur first, then offset or position.**
  SwiftUI scales and rotates about the layout frame, which an earlier offset doesn't move, so the
  first native AI pencil turned about its middle instead of its tip and wrote half its size away from
  the words; a frame-by-frame recording beside the board found it. "THE ANIATMATON YOU DIDNT ADDED
  PROERPELY at all" (Comma, Oct–Nov 2026)
- **When a value gets a second move, schedule it at its own time; never start it now with a delay.**
  On the web two animations on one property stack, so a delayed one waits its turn; a native engine
  that keeps one track per value replaces the running move at once, so a press with a delayed lift
  would lose the press. (Comma, Oct 2026)

- **Check the character at its widest pose.** A crawl stretched the rig past its SVG box and cut it off; let the art
  overflow its box (`overflow: visible`) and capture every pose, not only the idle one. "Crawl animation has this bug ...
  character can be bigger." On a hero moment the character is bigger than feels safe. (Pip, Nov 2026)
- **No shadow under the character.** The owner's art carries its own shading; a blob shadow under it reads as a sticker.
  (Pip, Nov 2026)
- **Time passing on a calendar: pages flip back over the binding.** Torn pages falling, swaying and turning in 3D "look
  weird"; each page flips up and back behind the band, quicker as it goes, shading a little as it turns, and the day
  under it is already the next. Reduce Motion: the day just changes. (Pip, Nov 2026)
- **Forgetting is a fade piece by piece.** The word's letters and its meaning's words go last first, each blurring and
  drifting up a few points, the meaning a little ahead of the word; the word comes back the other way when it's caught.
  (Pip, Nov 2026)
- **A teaching film runs on a clock you can stop.** Make the film a pure function of its time, so pauses, a 2× hurry,
  a scene card that starts mid-film and the native port all share one timeline. Stop a millisecond before the next scene,
  or the pause shows the next scene's title. (Pip, Nov 2026)

- **A tile that flips through frames never paints an empty box over a picture.** When frames are stacked and cross-faded,
  a frame still downloading must be transparent, not a placeholder colour, so the frame underneath stays visible; only
  the bottom frame gets a placeholder. Otherwise a tile that has shown its picture goes blank every time the next frame
  isn't there yet, and the whole shelf looks broken and sluggish. (Comma, Nov 2026)
- **Fetch pictures at launch, decode them when shown.** Download every thumbnail and avatar into the disk cache while the
  user is still in the onboarding (a few at a time, newest first), but don't decode them: decoding hundreds fills memory,
  iOS empties the in-memory cache, and tiles reload. Give the in-memory cache a cost ceiling so it drops the oldest
  pictures first. "Load the thumbnails at the start so they don't look empty when we reach there" (Comma, Nov 2026)
- **While AI works, everything else steps back.** The glow on the writing is the only thing moving; the other choices
  fade back until it's done. "Others options should fade here ... it needs to show that, okay, it's writing" (Comma,
  Nov 2026)
