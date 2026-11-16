# What we learned, and why

Lessons from Comma (iOS, with a speech-following teleprompter), CutRoom (a Mac video editor), Flamely and Pip, Oct–Nov 2026. The apps appear only as examples.

## Feel comes first

**1. Playback, scrubbing and dragging must feel as smooth as the best-known app in the category; usability comes before features.** Why: "why the playback is not smooth as butter as compared to CapCut and DaVinci"; "LITERALLY THE PLAYBACK AND USABILITIES COMES FIRST". CutRoom, Oct–Nov 2026.

**2. Real-time features (speech following, prompters, live transcription) must never stall or go deaf.** Why: "its not responsive and it get stuck and stop working"; "It is not smooth, it is not following my words". Comma, Oct 2026.

**3. Dropping or picking media must show up within milliseconds; never freeze the UI while a file loads.** Why: "If I have to drag one photo in the editor, that's taking like... forever... it's freezing". CutRoom, Nov 2026.

**4. A list still scrolls when the gesture starts on one of its items, and long lists are lazy.** Why: "I'm not also not able to scroll when I am in the script". Comma, Nov 2026.

## Measure

**5. Measure with numbers before and after (updates per second, slowest seek, memory), on a quiet machine and under load.** Comma, Oct 2026; CutRoom, Oct–Nov 2026.

**6. Look for causes outside the app too.** One "choppy" report came from the system's audio service being overloaded: the player followed the audio clock, and the fix was to follow the device's own clock. CutRoom, Oct 2026.

**7. Find slow frames and long tasks with a per-frame sampler before calling motion smooth.** Comma, Oct 2026.

**8. Don't measure while the machine is overloaded.** Parallel agents and builds pushed load sky-high, made checks time out and filled the disk; run measurements alone. CutRoom, Nov 2026; Comma, Nov 2026.

## Make it cheaper

**9. Preview from lightweight copies, export from the originals.** With a 1080p play copy, scrubbing went from about 11 to 80 updates a second and memory halved. Why: "when we're showing the video, it doesn't need to show 4K video". CutRoom, Nov 2026.

**10. Where smoothness matters, use the platform's native media layer, not a web view.** Why: "why mac one is super smooth and nice while tauri one sucks". CutRoom, Oct 2026.

**11. A preview that leaves the screen stops completely (timers, animations, video) and rebuilds when it comes back.** Why: the design board got slower the further you scrolled. Comma, Oct 2026.

**12. Animate backgrounds and camera moves with transforms on the compositor**, so they cost nothing per frame. Comma, Oct 2026.

**13. In a grid of small looping illustrations, let every tile play, phases offset, and keep each loop small and in place.** Animating only the picked ones made the still tiles read as broken in a real build, so that rule was reversed. Why: "keep these animaton but play the animation". Comma, Oct 2026.

**14. A SwiftUI `Canvas` that reads the clock inside its drawing never redraws; drive it from a `TimelineView` or a changing input**, and stop that timeline when nothing moves. Comma, Oct 2026.

**15. Keep the design board fast; strip anything not under review.** Why: "the browser demo is too slow". Comma, Oct 2026.

**16. Attached context must not make every AI call slower and dearer:** summarise once, reuse the brief. Comma, Nov 2026.

## Device and battery

**17. Handle heat and idle: lower the work rate when the phone is hot, let the screen sleep when nothing happens, stop the camera when unused.** Why: a review found a hot phone kept the screen on forever with a dead camera preview. Pip, Nov 2026.

**18. Check what Reduce Motion and the owner's real phone do.** An older phone without the newest on-device features and with Reduce Motion on froze an animation that worked in the simulator. Comma, Oct 2026.

## The machine

**19. Keep only the latest build; clean old simulators, derived data and builds as you go, and say what takes the space.** Why: "only keep latest build please"; "TELL ME WHAT IS TAKING TOO MUCH SPACE". Flamely, Oct–Nov 2026; Pip, Oct 2026.

**20. One simulator, tests one after another.** Why: "PLEASE ONLY USE 1 simulator". Comma, Nov 2026.

## Disk and build caches

**21. When a build, link, install or signing step fails, check free disk before debugging the code, and free only what a build can recreate.** "No space left" and errno 28 surfaced as test failures, a link error and a signing failure, and each frozen release copy left about 4 GB of build data behind; archives, test results and logs stay, because an archive's dSYMs decoded a launch crash. Comma, Nov 2026.

**22. Point every build folder at one shared package checkout, and resume a build with the same compiler flags.** Each fresh build folder downloaded every Swift package again (about 3.7 GB) and ran the disk out mid-build, and a cold build with the analytics, crash and payments SDKs passed a tool's ten-minute call limit under load; `-clonedSourcePackagesDirPath` reuses the checkouts, and changed flags throw the incremental build away. Comma, Nov 2026.

## Serving shared content

**23. Publish what is the same for everyone as a static file on a CDN, rebuilt at each publish, not as a sync between databases or a query per person.** The library moved from a database-to-database sync job to one published file that the app and the assistant connector both read, so new items appear without an app update and cost no database reads; the database keeps only what is personal. Comma, Oct–Nov 2026.

**24. Make every image once, at its size, when you publish, under a key that never changes.** Frames at 360 px wide and quality 45 average 12.6 KB (about 0.28 MB a video) with nothing to resize on request, and a redone frame gets a new versioned key instead of overwriting, so phones and the CDN can cache every file for a year as immutable. Comma, Oct 2026.

**25. Serve shared media from object storage with free egress behind a CDN, on your own domain; never from a shared web host, the bucket's development URL or the source platform's links.** A library visit plays about ten short clips (about 5 MB), so 1,000 daily users would pull up to about 150 GB a month from one shared server; Cloudflare's r2.dev address is rate-limited and meant for testing, a custom domain needs its DNS on Cloudflare, and platform links such as avatars expire, so copy the media in. Comma, Oct 2026.

## Long text

**26. A row's preview renders a bounded prefix of a long text, never the whole field.** A very long field laid out in full inside a compact row spilled over the controls beside it; the full words stay stored and open in the editor. Comma, Nov 2026.
