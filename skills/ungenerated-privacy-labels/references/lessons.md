# What we learned, and why

From filling in App Privacy for Comma (iOS, AI writing, Sentry, PostHog, RevenueCat), Nov 2026. The app appears only as an example; each rule holds for any app.

**1. Build the sheet from every SDK's own privacy manifest, not from a hand-written list.** Why: the hand-written list had nine types; Sentry's manifest also declares Other Diagnostic Data and PostHog's Other Usage Data. The owner ticked Other Diagnostic Data by accident and was told to untick it, when it was right. `scripts/labels.py` merges them all. Comma, Nov 2026.

**2. An SDK's "not linked" becomes linked once the app identifies it with the account.** Why: Sentry, PostHog and RevenueCat each ship `Linked: false`, but the app calls `setUser`/`identify`/`logIn` with the account id after sign-in, so Apple's own rule ("Analytics identified by account ID is linked") makes every one of them Yes. Comma, Nov 2026.

**3. Give the owner one table, one row per screen they'll see: Screen · Tick · Linked · Tracking.** Why: an answer grouped by category with the purposes in a sentence below had to be asked for three more times ("BRO ITS FOR ALL ... GIVE ME WHAT TO TICK FOR EACH"). The screens come one data type at a time, so the answer must too. Comma, Nov 2026.

**4. Answer the screen they pasted, not the whole topic.** Why: each paste is the screen in front of them; they need the ticks for it, the two yes/no answers, and nothing else. Comma, Nov 2026.

**5. Labels describe the release build.** Why: the owner asked whether a leaderboard counted as Name; the league existed only in debug builds (cut from release before review) and never sent a name. Check what ships before answering "does X count". Comma, Nov 2026.

**6. Plan for clicks: there's no API key route.** Why: everything else in the listing was set through the App Store Connect API; App Privacy wasn't, and the owner had to click 30+ screens. Use computer use or Claude in Chrome when available, and keep the owner's sign-in and the final Publish theirs. Comma, Nov 2026.

**7. Keep three things identical: the labels, the app's `PrivacyInfo.xcprivacy`, and the privacy policy.** Why: when a type was added to the labels, the manifest still lacked it; reviewers and the Xcode privacy report compare them. Change all three in the same round. Comma, Nov 2026.

**8. Turn off what you don't want to declare before you declare.** Why: the analytics project was storing IP-derived city and coordinates (GeoIP on), which would have meant Coarse Location; switching GeoIP off and discarding IPs kept the label honest and shorter. Comma, Nov 2026.
