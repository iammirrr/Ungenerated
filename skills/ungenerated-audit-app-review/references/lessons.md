# What we learned, and why

Lessons from preparing Comma (iOS), Flamely (Mac/Windows/iOS), Pip (iOS) and CutRoom (Mac) for the stores, Oct–Nov 2026. The apps appear only as examples.

## Nothing promises what the build can't do

**1. Nothing in the app or the listing promises what the build can't do on the phone** (sign-in, AI, share extension, widget, voice, rating). Why: "legitly, nothing is working to begin with". Comma, Oct 2026.

**2. No stand-in store sheets and no offers the store can't grant.** A pretend step is a refund, a one-star review and a rejection. Comma, Nov 2026.

**3. Screenshots are true to the app.** Why: "Apple wants you to show real screenshots". Comma, Nov 2026.

**4. Don't claim a platform until it has been built and run on it.** Why: "SO YOU TELLING ME ITS STILL NOT CROSS PLATFORM". CutRoom, Nov 2026.

## Purchases

**5. Every paywall shows Restore, the auto-renewal terms, and Terms and Privacy links.** It is guideline 3.1.2 and the auto-renewal laws. Flamely, Oct 2026; Comma, Nov 2026.

**6. Every subscription product needs its review screenshot and is "Ready to Submit" before the version is sent.** Comma, Nov 2026.

**7. Sign in before the paywall only when the purchase is tied to the account for a reason** (sync, the web); then say so in the review notes. Comma, Nov 2026.

## Accounts and sign-in

**8. Where another social sign-in is offered, offer Sign in with Apple too, placed above it.** Flamely, Oct 2026; Comma, Oct 2026.

**9. In-app account deletion, separate from cancelling, saying the subscription isn't cancelled.** Comma, Nov 2026.

## Before submitting

**10. Privacy and terms URLs are live and linked on the paywall and in the listing.** Why: the listing's privacy URL was empty and both pages returned 404 the day before submission. Comma, Nov 2026.

**11. Store builds carry no debug tools, test menus or fixture data; scan the archive before upload.** Why: a Release configuration shipped the test bar and fixtures; "remove any sort of these settings bars". Pip, Nov 2026; Comma, Nov 2026.

**12. Check the signed archive's entitlements (Sign in with Apple, push, app groups) for the app and every extension before upload.** Why: "BRO YOU LITERALLY SEND THIS BUILD WITHOUT ALL THIS"; a build went out unsigned, with no Sign in with Apple and no push. Comma, Oct 2026.

**13. A distributed app runs on a clean machine without the developer's folders, tools or login; test a fresh install.** Why: "IT SHOULDN'T BE DEPENDING ON SOME FOLDER ... SHARED ACROSS THE DIFFERENT USER WHO INSTALLED MY APPS". CutRoom, Nov 2026.

**14. Optional backend features stay off in the release build until verified on a real device.** One unverified probe crashed launch for signed-in people. Comma, Nov 2026.

## Ratings

**15. No rating screen of your own: ask only through the store's own review prompt, after a real win, never in onboarding.** Guideline 5.6.1 disallows custom review prompts, and one that sends 1–3 stars to private feedback and 4–5 to the store is review gating. Why: "it's not taking me to the App Store". Comma, Oct–Nov 2026.

**16. The system rating sheet never shows in TestFlight; the test build says so instead of looking broken.** Comma, Oct 2026.

## Brand and wording

**17. Use the store's real brand icon or badge wherever you refer to it**, never an emoji or a lookalike. Comma, Nov 2026.

**18. Cite the exact guideline before warning about a rejection.** Why: "why are you saying that will be rejected from the App Store? Tell me the one reason." Flamely, Oct 2026.

## AI and data

**19. Ask before personal data goes to a third-party AI, in the app's own sheet, and say what goes where.** It is guideline 5.1.2(i) as well as trust. Comma, Nov 2026.

**20. Show no tracking prompt the app doesn't need.** Why: "MAKE SURE IT DOESN'T ASK ANY WEIRD POPUP TRACKING". Comma, Nov 2026.

## From developers who ship

**21. Checklists from people who get approved go into the audit as rows, each checked against Apple's own text before it's trusted.** A rating screen in onboarding, "soon" labels, a cancel gauntlet, remote paywalls, legal pages that aren't plain pages, a copied or generated look, an untested iPad. Why: "he tells like tons of lists that ... the app store won't approve ... you probably want to be like monitoring that". Comma, Nov 2026.

**22. A custom "how's it going" stars screen is a custom review prompt even when 4–5 stars lead to Apple's sheet.** 5.6.1 says Apple will "disallow custom review prompts"; ask only with the system API, after a real success, never in onboarding. Comma, Nov 2026.

**23. A test-only compile flag must never be on in the Release configuration.** TestFlight and the App Store get the same binary, so a flag on in Release ships test wording, removes rate limits on prompts and mislabels analytics; check test builds at runtime (sandbox receipt) instead. Comma, Nov 2026.

**24. The marketing version is part of the release plan.** A store version 1.0 can only take builds whose version string is 1.0; months of 0.1.0 TestFlight builds can't be attached. Set it before the build you mean to submit. Comma, Nov 2026.

## Release builds

**25. Never reuse a build number, and count an interrupted upload as having used its number.** An upload stopped midway may or may not have registered with App Store Connect, so the next build skipped that number rather than risk a refused or confusing upload. Comma, Nov 2026.

**26. With no registered device, archive unsigned, sign every bundle ad hoc with its own entitlements, then let the App Store export sign for distribution.** A signed archive failed ("Your team has no devices from which to generate a provisioning profile") and the terminal couldn't use the signing key; ten test builds archived with signing off reached testers with no Sign in with Apple and no push, because the export keeps only the entitlements the binaries carry. Keep a map of every bundle to its entitlements file that stops the run on any bundle it doesn't know, so a new extension can't ship without its capabilities. Comma, Oct 2026.

**27. Create the app's record in App Store Connect before the first upload.** Without it the upload fails with "Error Downloading App Information", which never says the record is missing. Comma, Oct 2026.

## App Store Connect

**28. Settle every permanent identifier before the app's record exists: the bundle id, the product ids and the billing service's entitlement ids.** The bundle id can't change once a build is uploaded and product ids can never be reused; after the app's rename its billing entitlement still carries the old name. An id with no brand in it survives a later rename. Comma, Oct–Nov 2026.

**29. Check the developer account's legal name early; it is the seller name on the store.** When the portal's Edit can't change it, Apple Developer Support has to, with ID documents, and that waits on Apple. Comma, Nov 2026.

**30. Fill the App Store Connect record early; it is half the submission.** With the build nearly ready, version 1.0 still had no build, copyright, description, keywords, URLs, category, age rating, screenshots, review details, price or territories, and the API can't read the privacy labels, so they are checked by hand. Comma, Nov 2026.

**31. Create the support mailbox and send it a test before its address goes into the app, the listing and the review notes.** The address was already in every draft while the mailbox didn't exist yet. Comma, Nov 2026.

**32. Leave China mainland out of a generative-AI app's availability unless you hold the permit there.** Generative AI needs a permit in China mainland, and an ICP filing, so the listing went to every other territory. Comma, Nov 2026.

## Releasing

**33. Submit the first version for manual release, and flip the launch-day server switches before pressing Release.** Approval can land on any day, and automatic release would have put the app live while a beta switch still made everyone Pro; phased release paces only automatic updates for people who already have the app, so it doesn't protect a 1.0. Comma, Nov 2026.

**34. When the website moves, keep every address a shipped build links to answering, and build the legal pages with relative links.** Builds on phones link the old privacy, terms and support paths from the paywall; when the site moved to its own subdomain the old path kept serving the same folder, so every earlier build's links still work, where a dead privacy or terms link on a paywall is a rejection. Why: "later we will shift it to its own website". Comma, Nov 2026.

## Prices and the word "free"

**35. On every purchase screen the price charged leads, and "free" appears only for a real free trial.** The pre-submission audit found a one-time offer headlined "2 months free" in huge type over a small grey price, a "Free" perk on a hard paywall, and a listing saying "free to try" when only the yearly plan had a trial (2.3.1(a), 3.1.2(a)); state a saving if you like, never larger than the price. Comma, Nov 2026.

## Pushes and ads

**36. A "new this week" push is marketing: its own switch, off until the person turns it on, and never time-sensitive.** Guideline 4.5.4 needs opt-in for marketing pushes; a digest of new library items feels like service to the builder but reads as promotion to Apple, and time-sensitive is for things happening within the hour. Comma, Oct 2026.

**37. Ads are review and privacy work, not an SDK drop-in.** They need a way to report an ad (2.5.18), the Advertising answer in the age rating, the ad networks' attribution IDs in Info.plist and app-ads.txt on the website; personalised ads add the tracking prompt with no reward for allowing it (5.1.2(i)), "Data Used to Track You" labels, tracking domains in the privacy manifest and a certified consent form in the EEA and UK. Asked for rewarded ads, the owner kept them out of the first version as the simpler review. Comma, Oct 2026.

## Assistant connectors

**38. Listing a connector in an assistant's directory is its own review: every tool titled and hinted read-only or destructive, and the documentation, privacy and support pages live before submitting.** One-click install exists only through each company's directory (no link adds a custom connector by URL), so a deployed server is not yet a public connector. Why: "something public so people can connect one click". Comma, Nov 2026.

