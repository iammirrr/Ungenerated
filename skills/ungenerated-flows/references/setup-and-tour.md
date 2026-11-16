<!-- Part of ungenerated-flows. Was the `setup-and-tour` skill. -->
> **When:** Design the first-run setup and tour - personal setup (how their day goes, permissions, sharing, reminders, the widget) before the account and the paywall, which comes last, and work admin after it; start straight at the first useful entity (clients, projects, a goal), let people add several or skip, then a short tour of coach marks on the real app screens. Use for "set up your account", "add your first X", workspace setup, product tours or coach marks.

# Setup and tour

## The order: personal setup before the account, the paywall last, work admin after it

The top-earning screen-time apps (studied 2026) all run the *personal* setup before the paywall and
none run work admin there. Split setup in two:

1. **Make it yours, before the account:** how their day goes, the permissions, the things that
   pull them away, and the light setup that makes the app theirs (sharing into it, reminders, the
   widget, their voice), all kept on the phone. The account that saves it closes this part and
   syncs it at sign-in ([account-signup.md](account-signup.md)). They build something of their
   own, the plan can use it, and leaving now costs more. Give these screens the same progress bar
   and answer rows as the questions, so it reads as one journey. (Reminders and the widget moved
   here from after the paywall: flows lessons, "Setup before the account, the paywall last".)
2. Then the plan, and the onboarding ends on the paywall.
3. **After the paywall** (paid, or past a soft paywall): work admin, the workspace first (its
   name, and who it is for: just me or my team, the team option marked Soon if teams aren't live,
   pre-picked from the team-size question), then the entities (clients, projects), then the
   tour. Show the workspace live as the app's switcher will. By now it feels like unpacking, not a
   hurdle. A long hands-on setup after paying doesn't hurt; work admin before the price does.

## Setup

1. **No "Let's set up" screen.** Start at the first real question: "Let's get you started. Who do
   you work with?"
2. **Add one, add more, or skip.** A name is enough; details are optional behind a disclosure.
   Each added item appears as a row with its own colour and its key detail.
3. **One entity per screen**, in dependency order (clients before projects).
4. A live preview of where the entity will appear in the app (a calendar block in its colour).
5. The terms were accepted at sign-in, in one line under the button; nothing in setup asks for
   them again. A "does and never does" promise, if the app has one, comes first after the paywall
   and asks for nothing ([consent-and-permissions.md](consent-and-permissions.md)).

- **No step counters.** "Step 2 of 4" adds reading and makes setup feel like paperwork. The
  progress is the screens getting shorter.
- **A project fits on one screen.** Its name, its colour, who it is for, and billing as two
  lines: Billable on or off, then hourly or fixed with the amount and the currency (the client's
  rate already in). Don't send billing to a screen of its own; the amount belongs with the project.
- **Setup is a taste of the app.** Each step is set on the app's real surfaces, drawn at their
  real size and without a device frame: the notifications as they will arrive for the reminders,
  the widgets as they sit on the Home Screen. People learn the app while they set it up, and the
  tour that follows has less to explain. A phone drawn inside the phone reads as a demo.
- **Ask how they work, not which technique.** Use the questions' answer rows, each with the day
  it describes drawn underneath as a thin calendar strip (work, breaks, meetings); the tap answers
  and moves on. The pick sets the numbers,
  said in plain words underneath ("90-minute blocks and 20-minute breaks"). No method names, and
  pre-pick from anything they already answered.
- **The widget ask:** in the personal setup, the widgets at real size on a home-screen ground, the
  three steps to add one, Done and Later. iOS can't add a widget for the person, so never pretend
  to. (No system alert follows, so Later is fine here.)
- **Containerless.** Don't wrap setup content in cards. Switches are plain rows; real surfaces
  (a notification, a widget) stand on the ground by themselves, drawn as the platform draws them.
- **The project screen is the form, cleanly:** name, colour, client, then billing as one control
  (Not billed · Hourly · Fixed price) and one large amount line with the currency. A fake
  "tracking now" preview on top only adds noise.
- **Reminders as rows that own their notification.** Each row is the switch, with the notification
  it sends right under it; switching off folds the notification away. The step's only button is
  Continue, which brings the system's notifications alert if it hasn't been asked: no "Not now" on
  a screen before a system alert (HIG; checklist row 47 in `ungenerated-audit-app-review`).
  Whatever they answer, setup goes on, and the reminders are scheduled the moment notifications
  are allowed ([consent-and-permissions.md](consent-and-permissions.md)).
- **The widget ask is the platform's own widget gallery, without the card:** the app's icon, the
  widget's name and one line, the widget at real size on the ground; the sizes slide past with page dots, each
  coming alive. The how-to is three small steps in one row.
- **In-app menus, never the browser's dropdown.** A native select draws outside the phone on a
  design board and looks broken; build the platform menu anchored to its field.

## Tour

- Its own part of the flow, after setup, on the **real app screens**, not illustrations.
- One coach mark at a time: the screen dims except a window around the target; a card says what
  it is in one line; Next, and a quiet Skip.
- **The window's radius = the target's radius + the padding around it.** Mismatched corners are
  the most visible flaw of a tour.
- Three or four marks at most. End with the one action that starts real use.
- **Teach the real mechanisms, in the order they happen:** the main control, the question the app
  will ask while they work, where the answer lands, the report. Let each step hand over to the next
  (the answer typed in step two is the title on the calendar in step three). Never tour a feature
  the product doesn't have.

## Anti-patterns

- A checklist screen that lists the setup steps before doing them.
- Tours over screenshots.
- Ten coach marks.
- Work admin (clients, rates, projects) before the price.
- A technique list ("Pomodoro, 52/17…") where a picture of their day would do.

## Events

- `setup_step_done` {step, added: count | skipped}
- `widget_guide_shown`, `widget_guide_done`
- `tour_step` {n}, `tour_skipped`, `tour_completed`
