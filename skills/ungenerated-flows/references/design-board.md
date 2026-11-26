<!-- Part of ungenerated-flows. Was the `design-board` skill. -->
> **When:** Scaffold and run a live design board for a mobile app - every screen a working phone in rows, the kit in its own view, research in its own view, transitions side by side, Pick and Note on every card, and Play the flow full screen. Ships a ready template (engine, parts, transitions, local server, screenshot tools). Use when starting to design screens, when someone wants to "see all the screens", review a flow, or prototype motion before building natively.

# Design board

The board is where an app is designed and reviewed before it is built. Every screen is a live
390 × 844 phone that plays its motion; the reviewer picks variations and leaves notes on the
screens themselves; "Play the flow" walks the whole journey full screen.

## The levels (never make more than the level needs)

A board has four levels, and each thing lives at exactly one. Going up a level for something that
belongs lower is how a board bloats into "10 different screens of the same thing" that the owner
can no longer read.

| Level | Is | Holds |
|---|---|---|
| Tab at the top | A part of the work | The whole app (journey order, in the app today and not yet, per place), Later (features set aside), Kit, Language, Character |
| Row | A place or a flow | Its screens in the order a person meets them |
| Card | One screen | One live phone |
| Tabs on top of the card | That screen's versions, states, use cases and edge cases | Default, empty, offline, error, returning, the other designs to pick from |

- **A variation is a tab, never a card.** Connection drops, an empty state, a returning reader, a
  second design: tabs on the one card (`tabOf`, or a shared Pick `group`). The owner, Pip, 26 Nov
  2026: "if you are creating variations, you do not want to create more screens. Instead, you want
  to put at the top of the tabs so I can see within the screen. So it's not very bloated ... so I
  can exactly tell you: okay, this one is not needed, this one is needed".
- **An idea is one card.** A feature not in the app yet is one card; its screens and states are its
  tabs.
- **Set-aside features get the Later tab,** never rows mixed into the app's own places.
- **Nothing settings-like gets a place of its own** (cancel, delete, notifications, feedback): they
  are rows under Settings, because that is where the person finds them.

## Start one

1. Copy `template/` from this skill (`ungenerated-flows/template/`) into the project, for example `design/board/`.
2. Fill in `board.config.js`: the app's name, one section per part of the flow (in order), the
   kit sections (`view: 'kit'`), and research cards as you gather them (`ungenerated-foundation` › app-research (references/app-research.md)).
3. Replace `css/tokens.css` with the app's kit (`ungenerated-foundation` › design-kit (references/design-kit.md)).
4. Write screens in `js/screens/<section>.js` with `F.def({...})`, one file per section, and add
   each file to `index.html` before `js/board.js`.
5. Run `node tools/serve.mjs` and open the printed address. On a phone on the same Wi-Fi, open the
   second address to review with real fingers. Picks and Notes save to `review/store.json`.

## A screen

```js
F.def({
  id: 'q-goal', section: 'questions', name: 'What are you here for?',
  flow: true,            // part of Play the flow
  enter: 'step',         // how it is entered: cut, dissolve, step, layer, carry, cover
  progress: 0.3,         // the question bar
  group: 'goal-style',   // variations share a group: tabs on one card; the reviewer Picks one
  // tabOf: 'q-goal',     // a state or edge case of another screen: a tab on that screen's card
  // tab: 'Empty',        // the tab's label, 1–3 words (else the part of the name after " · ")
  intent: 'One sentence: what this screen is for.',
  build(ctx) {
    const { body } = F.frame(ctx);
    body.append(F.qTop(ctx, { progress: 0.3 }), F.qHead(ctx, 'What are you *here for?*'));
    // ctx.at, ctx.loop, ctx.on, ctx.haptic, ctx.next, ctx.answers, ctx.mode ('board' | 'flow' | 'demo')
  },
});
```

- A **whole-part card** leads each row: `F.def({ id: 'seq-questions', section: 'questions', seq: true })`.
  It plays the section's screens in order with their real transitions and is outlined on the board.
- In `ctx.mode !== 'flow'` a screen may demo itself (a finger taps the answer); in the flow it waits
  for the person.
- `#only-<id>` shows one screen at real size; `#play` and `#play-<id>` open the flow.
- **Motion style.** `style: 'calm'` on a screen (or on `window.BOARD` for the whole app) makes the
  engine's helpers move in that personality and picks the screen-to-screen move: `fade`, `push`,
  `step`, `carry`, `iris` or `grow` (`ungenerated-motion` › motion-styles (references/motion-styles.md)). The Kit view's Motion styles row shows the
  same four parts (a heading, a button, a toggle, a value) in all seven, so the reviewer can pick
  by feel.

## The board's layout (keep it)

- Views in the order of the work: **Research · Kit · Screens · Transitions**.
- Each card: a small tool bar (number, Replay, Note, Pick, ⓘ), its tabs when it has versions or
  states (one line, a dot on a tab with a note, a mark on the picked one), the phone, one line with
  its name. The description and the note sit behind ⓘ, over the phone. Nothing else around the card.
- The first card of a row is the whole part, outlined, the same size as the rest.
- Variations, states and edge cases are tabs on one card (the levels, above), never extra cards or rows.
- Every card's intent says where the screen is reached from: "where do I come from to this screen?"
  is the first question the owner asks of a feature.
- Theme switch (Auto, Light, Dark) and Play the flow in the top bar. Nothing else up there.

## Publish it

The board the reviewer uses is the one served from the project (`tools/serve.mjs`), on their
computer and on their phone over the same Wi-Fi. Make every change there. Publish a copy (a
private web page, a Claude artifact, any static host behind a login) only when they ask for one,
for someone off the network. A copy goes stale the moment the board changes, so never treat it
as the board or update it instead. Picks and Notes saved on a copy stay in that copy's store.

## Rules

- No native code for a screen until it is approved here.
- Use only motion that the native platform can reproduce (transform, opacity, blur, clip).
- One screen file per section; shared parts go in `js/parts.js`, never copied between screens.
