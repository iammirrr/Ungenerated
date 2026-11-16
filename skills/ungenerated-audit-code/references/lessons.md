# What we learned, and why

Lessons from the code of Comma (SwiftUI app and a web design board), Flamely (Mac/Windows desktop plus an iOS client), Pip (iOS) and CutRoom (Tauri/Rust and native Mac), Oct–Nov 2026. Each came from a bug that shipped or a mess the owner had to point out. The apps appear only as examples.

## Dead and duplicated

**1. Screens cut from the design are deleted from the code, not left as dead routes.** Why: "why the screen I cancelled are not deleted?"; he asked for an audit of "dead screens". Comma, Oct–Nov 2026.

**2. One source for content shared by two surfaces** (a design board and the app, two clients): one course file, one character builder, one text helper, so a change lands in both. Why: the board and the app drifted every time content was copied. Comma, Oct–Nov 2026.

**3. Build the system that does the job; don't hand-edit one case to make it look right.** Why: "ARE YOU SYSTEMIZING IT RIGHT, NOT HARD CODING AND EDITING IT?" CutRoom, Oct–Nov 2026.

**4. Lay down the base that features plug into (one registry, each type only configuring it)** instead of a pile of one-off mock-ups. Why: "this is the architecture that we are following rather than just randomly making some mock-ups". CutRoom, Oct–Nov 2026.

## Risky logic

**5. Talking into a box only ever adds.** A pause, a recogniser restart or a second mic tap never replaces what was there. Why: "WHEN I TAKE PAUSE BRAIN DUMPING IT REMOVES ALL OF THE PREVIOUS TEXT" (shipped data loss). Comma, Nov 2026.

**6. Each item keeps its own state; an answer never carries into the next question.** Why: "it kinda copied the same answer to the second one automatically". Comma, Nov 2026.

**7. One source of truth and one undo history per document.** Two stores with two undo stacks drift; a stray undo wiped files and approved work was silently lost. CutRoom, Oct–Nov 2026.

**8. The approve path carries everything the draft made; test that an approved item survives the next save and redraw.** Why: approved custom graphics disappeared the next time anything was drawn. CutRoom, Nov 2026.

**9. When several processes write the same files, use a lock or a revision check.** Otherwise one silently overwrites the other. CutRoom, Nov 2026.

**10. When two clients share logic, prove parity by running the original's real code on awkward inputs** (midnight, daylight saving, overlaps, rounding) and comparing in tests. Why: "IT HAS 100% SAME LOGIC AS THE DESKTOP APP"; a fixture generator found 7 mismatches in 2,684 cases. Flamely, Oct 2026.

**11. A new client never changes what existing clients compute.** Write new data where old clients don't read it until they're ready. Why: "MAKE SURE THIS ISNT HURTING OUR DESKTOP APP A SINGLE BIT". Flamely, Oct 2026.

**12. Across devices a person has one state** (active anywhere means active; one schedule; settings sync). Why: "WHY LIKE 15 MIN TIMER ASK ON WINDOWS AND MAC SEPARATELY THAT DOESNT MAKE SENSE?" Flamely, Oct–Nov 2026.

**13. Clip anything time-based to its day.** Why: "the work is leaking out of even of the 2 a.m. ... Probably one of the biggest bugs". Flamely, Nov 2026.

**14. A destructive account action refuses when signed out, before clearing anything locally.** Comma, Nov 2026.

## Platform traps (examples of "check the compiler and framework, not just your logic")

**15. Swift 6.2 with Approachable Concurrency could pass garbage to stored `async @Sendable` closures; marking them `@concurrent` fixed a shipped launch crash.** Comma, Nov 2026.

**16. A SwiftUI `Canvas` that reads the clock inside its drawing never redraws;** drive it from a `TimelineView` or a changing input. The character stood still across the app for days. Comma, Oct 2026.

**17. Shared visual helpers must not add layout as a side effect.** A blur helper's side padding pushed every centred text 8 pt right in a shipped build. Comma, Nov 2026.

**18. When you fork an engine, prefix new class names per screen;** reused names inherit the engine's rules (an inherited margin knocked a calendar out of line). Comma, Oct 2026.

**19. A flow's order is its registration order;** keep each screen in its part's file and print the order after moving anything. Comma, Oct 2026.

**20. When porting to another platform, use that platform's native equal for each piece, never a cheaper downgrade, and leave the working platform untouched.** Why: "never replace to cheap stuff". CutRoom, Oct 2026.

## Tests

**21. Keep UI tests current with the UI; fix flaky waits; a failing test may be a real bug.** Bringing 15 failing tests up to date found a real one (an item's fields lost their ids inside an editor). Comma, Nov 2026.

**22. Tap tests prove every flow**, and the check order is tap tests, then analytics events, then the database and payments, then screenshots. Comma, Nov 2026.

**23. For bugs that are hard to reproduce, build a flight recorder into test builds** that logs exactly what happened. Why: "make the test app slightly more intuitive and better so you are able to kinda like understand the problem". Flamely, Oct 2026.

**24. Fix at the root and explain the cause with a before and after.** Why: "you need to recode it and like why it's happening to begin with". Flamely, Oct 2026.

## Releases

**25. Check the signed archive's entitlements for the app and every extension before each upload.** Why: "BRO YOU LITERALLY SEND THIS BUILD WITHOUT ALL THIS"; a build shipped with no Sign in with Apple and no push. Comma, Oct 2026.

**26. Freeze each release on its own branch, after every parallel agent's changes are merged.** Why: "DID YOU CHECK IN ALL THE CODEX CHANGES AS WELL?" Comma, Nov 2026.

**27. Optional backend features stay off in production until verified on a real device.** One unverified probe crashed launch. Comma, Nov 2026.

**28. Store builds carry no debug tools, test menus or fixture data;** scan the archive before upload. Pip, Nov 2026.

**29. A distributed app never depends on the developer's folders or tools;** test a fresh install. CutRoom, Nov 2026.

## Working on the code

**30. One simulator, tests run one after another.** Why: "PLEASE ONLY USE 1 simulator"; parallel builds ran the disk out. Comma, Nov 2026.

**31. Don't let several agents edit one tree at once without lanes; keep to two or three.** Why: a tree stopped compiling because lanes were mid-edit. Pip, Nov 2026; Flamely, Oct 2026.

**32. Code from a delegated model is reviewed and tested before it's applied;** a thinking-only answer is not delivered code. Comma, Nov 2026.

**33. An "insert or ignore" that later code depends on must only be ignorable because the row already exists.** Flamely's desktop created a new account's profile with `INSERT OR IGNORE`; the table had `UNIQUE(email)`, and an older profile on the computer held the email (the account had been deleted and made again), so nothing was inserted and the next statement failed its foreign key. The app showed only "Could not activate local data for this account" on Windows, and it worked on the Mac, which never had the old profile. Same code, different leftover data: check what's on the failing machine. Flamely B-220, Nov 2026.

**34. A catch-all error message hides the cause; keep the real reason where you can read it.** The sign-in failure above was diagnosed from the code, because the app logged the cause only in test builds. Flamely, Nov 2026.

**35. A test for a fix must fail without the fix; check it once.** The first test for the bug above passed without the fix, because reading a missing row returned "null" just like the expected empty email. Flamely, Nov 2026.

## Sync

**36. Page through the server by key until an empty page, never until a short one.** The data API caps rows per response below what the client asks for, so a short page doesn't mean the end; review caught this before the full pull shipped. Comma, Nov 2026.

**37. An update or delete that matches no rows fails loudly.** Old clients writing through a changed schema silently changed zero rows and still reported success; the new path raises an error for them instead. Comma, Nov 2026.

**38. Take compare-and-swap revisions from one database sequence, not a per-row counter.** A row deleted and recreated would restart its counter and accept a stale client's old revision; a sequence never repeats, and its gaps are expected. Comma, Nov 2026.

**39. Two items are the same only when their id says so; never merge because the text matches.** The old sync auto-merged ideas with identical bodies, which collapses different ideas that share a headline; dedupe by id or retry key and accept an occasional visible duplicate. Comma, Nov 2026.

**40. Merge a sync conflict part by part using stable ids, and show both versions only where both devices changed the same part.** Each save writes "where version = the one I read"; zero rows changed means fetch, merge each part by its id and save again, so nothing is lost silently, no version silently wins, and the person reviews only real clashes. Comma, Oct–Nov 2026.

**41. Clear a sync conflict automatically only when the server can prove which write was yours.** A review suggested auto-clearing conflicts that looked clean; without a receipt for each attempt that could overwrite another device's later revert, so both versions are shown and the person chooses. Comma, Nov 2026.

**42. A sync never loses words: save each pending write before sending it, keep the local copy as the truth until the server confirms, and let an empty or failed fetch delete nothing.** A legacy test-data cleanup could delete ideas before pulling them, and the old push swallowed errors so one failed upload silently stopped the rest; with the attempt on disk first, an app killed mid-save still has it on the next launch. Comma, Oct–Nov 2026.

**43. Bind every queued write and every cache to the account that made it.** After a sign-out or an account switch a pending save never uploads under the next account and a late fetch never fills the next person's cache; a capture made while signed out waits until the person chooses where it goes, and a corrupt cached copy never erases what they wrote. Comma, Nov 2026.

**44. Keep and use the refresh token.** An app that stored only the access token signed up again on the first 401 after it expired, so each phone would have become a new anonymous user every hour and run into the auth provider's per-IP limit on anonymous sign-ins. Comma, Oct 2026.

**45. When an app and its extension share one session, sign out only on a definite rejection, after re-reading the shared keychain.** Refresh tokens rotate, so whichever process refreshes first leaves the other holding a dead copy; a rejected refresh first adopts a newer session for the same person from the keychain, and a network error or rate limit never signs anyone out. Comma, Nov 2026.

**46. Never hold a lock or a serial storage queue across a network call.** Two sign-in operations stalled behind one slow upstream identity call until the waits moved outside the critical sections. Comma, Nov 2026.

## Changing and deleting items

**47. After a delete, nothing may bring the item back.** An open editor, an autosave, a late callback or a launch step that adopts old records into a new type must refuse a removed item: deleting now closes only that item's routes, free writing can't recreate a draft just deleted, and deleting a draft made from an old idea archives the idea, or the next launch would adopt it again. Comma, Nov 2026.

**48. A parent's status derived from its children lets unfinished work win.** A review caught ideas with one finished and one unfinished script filed as done; an idea stays in progress while any child is unfinished, counts as used only when all are filmed or posted, and returns to new when its last child is deleted. Comma, Nov 2026.

**49. When you change what an object is, re-check everything keyed to it.** Folding ideas into drafts let a new, empty draft earn the first-story stamp on creation; the stamp now needs written words. Comma, Nov 2026.

## Data formats

**50. Feed client decoders the real database's output, not hand-written fixtures.** A contract test decoding JSON straight from Postgres caught a date parser that accepted only UTC while the database sent numeric offsets; the same test keeps 64-bit revision numbers exact. Comma, Nov 2026.

**51. Postgres timestamps carry microseconds: never pass them through a millisecond type.** A JavaScript driver turned a sync cursor into a JS Date, so .162821 became .162 and every row looked new on every run (it also encoded JSON a second time); pass such values as text and cast them in SQL. On the phone, Apple's ISO 8601 formatter parsed the six-digit fractions only once they were trimmed. Comma, Oct 2026.

**52. Count text limits the same way on every side, in Unicode code points, with a byte limit too.** Swift counts grapheme clusters, JavaScript UTF-16 units and Postgres code points, so one limit enforced three ways disagrees on emoji and combining marks; count code points explicitly everywhere, add a total byte cap, return the field and its limit instead of truncating, and test emoji, combining marks and a non-Latin script. Comma, Nov 2026.

## Old builds and the server

**53. Deploy the server first and keep it working for every installed build.** New tasks, migrations and widened constraints go live before the build that calls them (a source type the app saves would have been refused by a check constraint it had outgrown), and old builds keep their fields filled and their known-bad requests repaired on the server: when a response split one list into two the server kept filling the old one, and builds that sent only part of a reference had the whole one loaded server-side. Comma, Oct–Nov 2026.

**54. Before a server rule refuses old builds' writes, move every device on that account to a build that understands it, and snapshot the account's rows first.** An old binary can't show an error it doesn't know and its sync swallowed failures, so turning on revision-checked sync would have silently dropped every older build's saves; the first account moved only after the compatible build was verified on the owner's phone. Comma, Nov 2026.

## The database

**55. Never run the database CLI's push, or its suggested repair, on a project whose migration history holds entries your repo doesn't.** One project's history held another tool's 40 migrations and different version numbers for three of the app's own files, and repair rewrites that history; name each file by the version the database recorded and apply migrations one at a time. Comma, Oct 2026.

**56. The repo's migrations must rebuild production: save every change the day it's applied, as a new file exactly as applied, and prove the set builds an empty database.** One migration applied straight to the database reached the repo two days later, and the development files leaned on tables only development had, so production started from one clean baseline; only one repo ever changes a schema, and changes awaiting the owner's yes wait in a separate proposals folder. Comma, Oct 2026.

**57. Before replacing a live database function, diff your file against what production runs.** The repo's copy can be stale (production even had a column no migration in the repo created), so read the live definition, change only what you mean to, and record any drift in a migration. Comma, Nov 2026.

**58. When a database function's arguments change, drop the old overload, or give the new version a new name while old callers drain.** Two overloads make an RPC call ambiguous; an old signature was dropped once nothing called it, while the AI budget's functions took new names so old server instances kept working until they were gone. Comma, Oct–Nov 2026.

**59. Prove database behaviour on the real database: whole flows inside a transaction you roll back, locking on several real connections.** Requests end to end and the paid-plan check for a cancelled account ran on the real schema in rolled-back transactions and left nothing behind; races ran on a real Postgres of production's version with competing connections, because an in-process Postgres has one backend and passes them by construction. Comma, Oct–Nov 2026.

**60. After publishing, read the content as the app's own role.** A weekly collection was created without its published timestamp while the policy shows only published rows, so it would never have appeared and nothing would have errored. Comma, Oct 2026.

**61. Every state a job can enter needs a way out, including "won't do" and "failed" with a reason the person sees.** Requests accepted from a short link with no id yet were never sent on, and nothing could mark a request unusable or failed, so they would have waited forever while the app promised an answer. Comma, Oct 2026.

**62. A re-publish updates the existing row and keeps the fields it doesn't own.** Publishing an item again would have wiped like counts that existed only in the app's table; republish over the same id so every save and link keeps working, and keep the current value of each field another source fills unless the new one is present. Comma, Oct–Nov 2026.

**63. When the app keeps its own copy of an internal pipeline's content, that copy stands alone.** Copy every field the app shows instead of joining into the pipeline's tables, which production doesn't have, and take an item down with a status and a blocklist, never by deleting the pipeline's rows: they cascade on delete but the app's copy has no foreign key to them, so the item would stay live with nothing behind it. Comma, Oct 2026.

## Push notifications

**64. Store each push token's APNs environment and send to the matching host.** Debug builds register sandbox tokens while TestFlight and App Store builds register production ones; on BadDeviceToken try the other environment once and correct the record, and delete a token that fails in both. Comma, Oct–Nov 2026.

**65. Sending straight to APNs from a serverless function works, but cache the provider token per fixed window with the same issued-at in every instance.** One unauthenticated request answered 403 MissingProviderToken, which proved the runtime reaches Apple over HTTP/2 with no relay; Apple wants the token renewed no more often than every 20 minutes and at least every 60, and cold starts each minting their own count as renewals (TooManyProviderTokenUpdates), so the issued-at comes from a 50-minute window. Comma, Oct 2026.

**66. Classify every push answer: drop the device on a dead token, stop the run on a configuration error, retry only network and server errors.** A 403 or a wrong topic means every push will fail the same way, so the run aborts and puts its rows back unspent, and until the push key exists the sender touches nothing so every row waits. Comma, Oct 2026.

## Sharing into the app

**67. Declare a share extension's activation with Apple's version-2 dictionary and strict matching, and prove it through the real share sheet.** The version-1 dictionary, then a custom predicate, hid the app whenever a link came beside a video, even in the full app list, so nothing reached the server; the strict rule (web URL and text) lists it and still excludes video-only and picture-only shares, each case checked through the system sheet. Why: "I think Instagram sharing stuff is not working properly". Comma, Oct–Nov 2026.

**68. A share extension puts what it's handed into a shared inbox before any network call.** The app sends what's left at launch, on every return to the front and after sign-in, and only the server's explicit refusal removes an item, so no link is lost to a missing account or a dead network; when anything outside the app can add data (an assistant saving while the app sleeps), pull on every return to the front too. Comma, Oct–Nov 2026.

**69. Parse shared links from the shapes share sheets really send, and key them on the post's id, never the raw URL.** Instagram adds a per-share tracking parameter, so one post arrives as many URLs, and its /share/ links carry a token that looks like a post id but isn't: the parser took it for the id, missed the library and the dedupe and queued a job for a post that doesn't exist. Strip the query, take the id only from known paths, resolve short links on the server, and test every real shape (35 were checked). Comma, Oct 2026.

## Device and framework traps

**70. A shared device resource is released only by the code that claimed it.** Speech recognition deactivated an audio session the camera or a file player had borrowed and froze the app; the session is now reference-counted, and a practice timer holds the keep-awake setting only while running, restores the previous value on exit and never overrides the camera's claim. Comma, Oct–Nov 2026.

**71. When the camera records while speech recognition listens, hold one audio session for the whole take.** Releasing it between recognition stretches switched off the camera's microphone too, so listening stopped mid-take. Why: "my mid transcribing, it stopped picking up words". Comma, Oct 2026.

**72. Apple's older live speech recognizer stops about every minute: restart it in a pause before the limit, never for a UI action, and use SpeechAnalyzer where it exists.** A follower that gave up after a few quick ends stopped following after a pause, and restarting to re-read a line lost the words said meanwhile; the iOS 26 analyzer needs no restarts. Why: "I take a pause and it never kind of resumes". Comma, Oct 2026.

**73. Leaving a screen cancels everything it started.** Speech results land late, so closing dictation stops it and drops any result that arrives afterwards (a test feeds one after leaving); a review of a practice camera found startup and the count-in still running after exit and interrupted takes left behind, so exit now cancels both and finishes or discards the recording. Comma, Nov 2026.

**74. In SwiftUI a Button wrapped around a view that has its own tap gesture never fires; give the view the action instead.** The character's own tap handling swallowed the Button's tap, so its action is now passed in as a parameter. Comma, Oct 2026.

**75. On iOS 26 a GeometryReader preference doesn't update while a ScrollView scrolls; read the scroll view's own geometry.** A ruler's tape moved but its number didn't; it was found only by dragging it for real in a UI test. Comma, Oct 2026.

**76. Swift's attached macros take one variable per declaration.** A multi-variable `@ObservationIgnored var a, b, c` broke the shared build; split it into one declaration per variable. Comma, Nov 2026.

## Tests, releases and agents

**77. Compile the tests with the app target's exact compiler settings.** A transport's checks passed in two language modes and with optimisation while the app crashed at launch, because the app was built with an upcoming concurrency feature on; a one-file reproduction with the app's flags exposed the compiler bug. Comma, Nov 2026.

**78. UI tests assert what a person can actually do, and never race the clock.** Controls behind a system sheet still "exist" in the accessibility tree, so assert hittable and enabled, and a query for a hidden menu's absence stole focus from the editor under test; a four-second Undo toast expired while the runner collected a snapshot under load, so a test fixture now holds it and the product's timing stays as it is. Comma, Nov 2026.

**79. A release copy made from git lacks the git-ignored runtime config: copy it in privately and check the build has it.** Builds frozen from clean checkouts had no env file, so their crash-symbol upload was skipped. Comma, Nov 2026.

**80. Give a delegated model a narrow job.** A broad job spent its whole output allowance on thinking and returned no code, while two narrower jobs on the same work came back complete. Comma, Nov 2026.

**81. When other sessions share the repo and the machine, stage by exact path, give each helper its own build folder, and validate from one frozen copy of all sources.** Adding everything sweeps another session's half-finished work into your commit; a helper told to use "your scratch dir" built into the main session's folder and both builds failed with "database is locked"; a candidate copied without the new file its two editors shared couldn't compile. Comma, Oct–Nov 2026.
