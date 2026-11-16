# Real rejections, and what fixed them

What developers were rejected for in 2024–2026, in Apple's words as they pasted them in public, and the fix when one was reported. Before a run, read the entries behind a checklist row to see how App Review applies it. After a rejection, search this file for the guideline number or the first words of Apple's message.

Collected 16 Nov 2026 from the Apple Developer Forums, the RevenueCat Community, Hacker News, Daring Fireball, GitHub, dev.to, vendor blogs (RevenueCat, Superwall, Adapty) and Apple's own pages. Guideline quotes were checked against developer.apple.com/app-store/review/guidelines ("Last Updated" 16 Oct 2026). Reddit isn't quoted: it blocks automated readers, and nothing here is Reddit second-hand. App Review changes without notice (the toggle-paywall wave came with "no announcement, no updated documentation, no grace period"), so re-check an entry before leaning on it.

Each entry:

- **Apple said**: the rejection as the developer pasted it, trimmed with "…", with its source and month. *(developer's words)* marks a paraphrase where Apple's text wasn't posted.
- **Cause** and **Fix**: what was changed and whether it passed; "none reported" when nobody said.
- **Common**: independent reports found in this search, and Apple's own numbers where they exist.
- **Row**: the `checklist.md` row it tests (numbers as of 16 Nov 2026, 94 rows, with the row's short name so it survives renumbering), or **not in checklist** (collected at the end).

Forum threads are `developer.apple.com/forums/thread/<number>`; the forums show month and year only. App Review's forum reply "We believe we have resolved this issue" is boilerplate, not a fix.

## The numbers

- 2025: 9,100,620 submissions reviewed, 2,093,244 rejected (about one in four). By section: Performance 1,354,418, Legal 495,673, Design 415,532, Business 283,820, Safety 151,159 (one submission can fail several). 387,087 were approved after a rejection. https://www.apple.com/legal/app-store/transparency/2025/
- 2025, by cause: "over 443,000 submissions for privacy violations", "over 371,000 submissions that copied other apps, were found to be spam, or otherwise misled users", "over 22,000 submissions for containing hidden or undocumented features". Apple Newsroom, May 2026: https://www.apple.com/newsroom/2026/05/the-app-store-stopped-over-2-point-2-billion-usd-in-fraudulent-transactions-in-2025/
- "On average, over 40% of unresolved issues are related to guideline 2.1: App Completeness." App Review is "typically reviewing at least 50% of submissions in less than 24 hours and 90% in less than 48 hours". https://developer.apple.com/distribute/app-review/

## 1. Safety (1.x)

### R1. A social app missing the UGC precautions (1.2)
**Apple said:** "Require that users agree to terms (EULA) and these terms must make it clear that there is no tolerance for objectionable content or abusive users", "A method for filtering objectionable content", "A mechanism for users to flag objectionable content", "A mechanism for users to block abusive users", "The developer must act on objectionable content reports within 24 hours by removing the content and ejecting the user who provided the offending content". After those were built, the next review added "Age rating must reflect 18+", "A mechanism for users to immediately remove posts from the feed", contact information inside the app, and: "Note that providing a demo video showing the app in use is not sufficient to continue the review." https://developer.apple.com/forums/thread/807358 (Nov 2025)
**Cause:** the reviewer couldn't find each precaution, and new items appeared on the second pass. The developer's backend showed that review lasted about five minutes.
**Fix:** every item built and described in the notes, with a backend admin login; outcome not reported.
**Common:** 1 detailed 2025 report; the template is old (e.g. thread 679400). Since 16 Oct 2026, 1.2 adds: "It is your responsibility to remove content that violates this guideline, your terms of service, or your community standards."
**Row:** 79 (UGC precautions), 62 (age rating).

### R2. AI output with no filter at a low age rating (1.2)
**Apple said:** "Your app includes AI-generated content but does not appear to include content filtering at this time. Since your app may produce content not appropriate for all audiences, it would be appropriate to revise your app's age rating to 17+ in App Store Connect or implement content filtering." https://developer.apple.com/forums/thread/742007 (Nov 2023)
**Fix:** Apple's two options: a higher age rating, or filtering "so that all generated content is appropriate for your app's current age rating". Outcome not reported.
**Common:** 1 verbatim. 1.2 now names "AI content creation apps", and Apple's 16 Oct 2026 change makes moderation cover imagery "generated using AI tools" (https://developer.apple.com/news?id=vvzx6cul).
**Row:** 80 (AI content counts as UGC), 62 (age rating).

### R3. A support URL that isn't a support page (1.5)
**Apple said:** "The Support URL provided in App Store Connect … does not direct to a website with information users can use to ask questions and request support." https://developer.apple.com/forums/thread/840182 (Jul 2026)
**Cause:** the URL was a blog post with a comment box at the bottom.
**Fix:** the developer says the rejection "has been overturned" (he doesn't remember whether by appeal). A reply from someone with 20+ apps lists what passes: "A dedicated URL (e.g. yoursite.com/support) used only for the app", "The app name at the top", "A visible contact method without scrolling: a support email address or a contact form (social links alone don't count)", "No login, no "coming soon", and it loads on mobile".
**Common:** 1 verbatim 2026 report; an Oct 2026 survey of posted rejections lists the related 1.5 wording "does not properly navigate to the intended destination" (https://blakecrosley.com/blog/app-review-what-reviewers-look-for-2026).
**Row:** 63 (support URL).

## 2. Performance (2.x)

### R4. The reviewer couldn't get in (2.1(a))
**Apple said:** "App Review was unable to successfully access all or part of the app." (TestFlight Beta App Review, after a demo account "with sample content in all four sections", the credentials in Beta App Review Information and testing notes) https://developer.apple.com/forums/thread/845934 (Sep 2026). Another app's test login failed because the phone field had the country code pre-filled and the reviewer typed it again *(developer's words)*, https://developer.apple.com/forums/thread/786863 (Jun 2025).
**Cause:** a login that works for the team fails for a stranger: pre-filled fields, email verification, one-time codes, region or rate limits, a backend asleep.
**Fix:** none reported in either. 2.1(a): "include demo account info (and turn on your back-end service!)". The suggestion in 845934: test the exact credentials from a clean install outside your own network, and ask App Review which screen failed.
**Common:** 2 here, and 3 more where the reviewer got in but couldn't reach the purchase (R5, R6).
**Row:** 3 (backend live, demo account works), 83 (demo account in the notes).

### R5. The reviewer's sandbox account is already subscribed (2.1)
**Apple said:** "App remained on the same page after we tapped Continue" (https://community.revenuecat.com/general-questions-7/ios-app-store-rejection-reviewers-unable-to-pass-paywall-6486, Jun 2025). In Mar 2026, a repeated request for a user with an expired subscription *(developer's words)*: https://community.revenuecat.com/tips-discussion-56/app-store-review-loop-sandbox-subscription-transfers-to-every-new-demo-user-reviewer-can-never-see-paywall-7526
**Cause:** a sandbox subscription belongs to the reviewer's sandbox Apple Account, not to your app's demo user, so every new demo user inherits it and the paywall never appears (or the store answers "You're currently subscribed to this").
**Fix:** explain it in the reply and ask the reviewer to cancel that sandbox subscription, or to test with "a brand new Apple sandbox tester account"; making more demo users doesn't help. Approved the next day (Mar 2026). RevenueCat staff: a TestFlight video of the flow "has helped".
**Common:** 2.
**Row:** 84 (demo account with an expired subscription), partly: an expired demo user doesn't help when the reviewer's own sandbox account is subscribed, so the notes must say how to reach the paywall.

### R6. The purchase is buried behind use (2.1, then 2.2)
**Apple said:** first that the reviewer couldn't locate the purchase *(developer's words)*; then a visible "IAP Test" shortcut was rejected under 2.2 as a "Beta feature"; then: "While we appreciate you provide an instruction... we require a quicker way to access in-app purchases without spending significant time to play games." https://developer.apple.com/forums/thread/812208 (Jan 2026)
**Fix:** after a phone call with App Review, a hidden tap sequence on the title screen that jumps to the purchase screen, described in the notes with a video offered. "my app … has been officially approved" the same month.
**Common:** 1 detailed report; 2.1(b) wants purchases "visible to the reviewer".
**Row:** not in checklist (every purchase reachable in under a minute from the notes, with no visible test button).

### R7. An iPhone-only app fails on iPad (2.1(a))
**Apple said:** "users expect apps they download to function on all the devices where they are available. Since your app may be downloaded onto iPad devices, it is important that it also function as expected for iPad users." (iPad Air 5th generation, iPadOS 18.4.1, after the developer had removed iPad from the device families) https://developer.apple.com/forums/thread/781735 (Apr 2025). "“Create PIN” button was not responsive Review device: iPad Air 11-inch (M3) OS version: iPadOS 26.2.1" https://developer.apple.com/forums/thread/815079 (Feb 2026). "Bug description: The app did not load its content." on iPad Air (5th generation), iPadOS 18.3.1: https://developer.apple.com/forums/thread/775846 (Mar 2025).
**Cause:** compatibility mode: controls off screen or under the keyboard, embedded web content failing.
**Fix:** Apple DTS: "iPads support running iPhone apps in compatibility mode, so all apps should "work" when run on an iPad. Note that this does NOT mean that their interface expands or otherwise "supports" the full iPad experience" (https://developer.apple.com/forums/thread/727753, Jan 2026). Run the build on an iPad simulator and fix what breaks; dropping iPad support doesn't stop it. The web-content case passed after every resource was loaded over HTTPS (a later reply on 775846).
**Common:** 4 reports in 2025–26 (also https://developer.apple.com/forums/thread/813147, Jan 2026), plus R29. Next: a developer summarising Apple's Oct 2026 guidance says that from April 2027 "If App Review finds that an app's UI is broken on iPhone Duo and can't be operated … the app may be rejected under Guideline 2.1(a), in the same way iPhone-only apps have been rejected for issues found on iPad" (https://developer.apple.com/forums/thread/851106; re-verify).
**Row:** 1 (no crash on iPhone and iPad), 94 (every screen works on iPad).

### R8. Purchases not submitted with the version (2.1(b))
**Apple said:** "We are unable to complete the review of your app because one or more of your in-app purchase products have not been submitted for review." Then: "as we were able to find in-app purchase items in the binary, we noticed that they have not been submitted for review." https://developer.apple.com/forums/thread/749359 (Mar 2024)
**Cause:** the first subscriptions weren't added to the version's submission, or one sat in "Missing Metadata".
**Fix:** "Just remove the build and you will see a button to submit in-app purchases" (reply), then check each subscription's state. RevenueCat staff (Dec 2025): "Apple requires that the first subscriptions you put in your app are sent together with your app for review", and "the products must be in the "Ready to Submit" or "Approved" state in order for the reviewers to make purchases." That developer's sandbox purchase went through once the app and the subscriptions went in together: https://community.revenuecat.com/general-questions-7/multiple-ios-app-store-rejection-due-to-revenue-cat-purchase-failure-there-was-a-problem-with-the-apple-store-7175
**Common:** 2 verbatim; the Oct 2026 survey (R3) lists it among the recurring 2.1 texts.
**Row:** 4 (purchases complete and submitted together).

### R9. Products load in TestFlight, not for the reviewer (2.1(b))
**Apple said:** "the in-app purchases do not load successfully." (iPad Air 11-inch (M3), iPadOS 26.6; both products Ready to Submit and attached; agreements, bank and tax active) https://developer.apple.com/forums/thread/844471 (Sep 2026). An empty product list *(developer's words)*: https://developer.apple.com/forums/thread/829142 (Jun 2026).
**Cause:** varies. On 844471 an Apple App Store Commerce Engineer replied: "I have had few reports around this time frame and I believe its linked to an outage which was resolved." On 829142 the subscription wasn't really attached.
**Fix:** 829142: "We have created a completely new subscription, mirroring settings from the existing one. Then we used it in the app, and it worked! Product list has been fetched." Suggested on 844471: fetch products at launch, retry, show a retry button, and log what StoreKit returns on the reviewer's session.
**Common:** 2 read in full, and about ten more 2025–26 threads with the same symptom in the title (e.g. https://developer.apple.com/forums/thread/827016, "Subscriptions fail to load in Review but work perfectly in TestFlight").
**Row:** 4, 32 (Paid Apps Agreement active); the retry is **not in checklist**.

### R10. "Information Needed" about the business model (2.1)
**Apple said:** the standard questions, as collected in 2019: "Does your app access any paid content or services?", "What are the paid content or services, and what are the costs?", "Do individual customers pay for the content or services?", "Where do they pay, and what's the payment method?", "How do users obtain an account?" (https://allenpike.com/2019/information-needed). Still sent in 2026, including for a paywall that was in the code but switched off *(developer's words: Apple wants "details about the business model")*: https://developer.apple.com/forums/thread/820156 (Mar 2026).
**Fix:** answer every question plainly; Allen Pike's clients who answered vaguely went into a slow secondary review. None reported on 820156.
**Common:** 2.
**Row:** 85 (the notes describe the business model), 9 (dormant features).

### R11. Unfinished or test features (2.2)
**Apple said:** "our app includes incomplete features that users are required to use, such as login service." "If your app is not ready for public distribution or is intended to demonstrate an app concept, use TestFlight." https://developer.apple.com/forums/thread/705524 (May 2022). In Jan 2026 an "IAP Test" button was a "Beta feature" (R6).
**Fix:** finish the feature or take it out; test shortcuts never in the Release build.
**Common:** 2.
**Row:** 2 (no placeholder or dead features), 5 (no test UI in Release), 88 (no "coming soon").

### R12. iPad screenshots made from iPhone ones (2.3.3)
**Apple said:** "Your iPad Pro (2nd Gen) and 13-inch iPad screenshots show an iPhone device frame scale. Upload new screenshots that accurately reflect the app in use on iPad." "Some or all of the provided screenshots do not sufficiently show the app in use." "iPhone screenshots should be taken on iPhone, not on iPad." https://developer.apple.com/forums/thread/765166 (Oct 2024)
**Fix:** capture each size on that device or its simulator; no outcome posted. In Feb 2026 another developer wrote that "it keeps getting rejected for not providing ipad screenshots" (thread 781735).
**Common:** 2.
**Row:** 58 (screenshots true to the build, at the required sizes).

### R13. Other platforms in the app or the listing (2.3.10)
**Apple said:** "The app or metadata includes information about third-party platforms that may not be relevant for App Store users, who are focused on experiences offered by the app itself." "Remove instances of this information from the app and its metadata, including the app description, promotional text, What's New info, previews, and screenshots. Revise the app's home page to remove Google Play references." https://developer.apple.com/forums/thread/748862 (Mar 2024)
**Cause:** "It seems that you mention Android or Windows in the app description, screenshots etc." (reply).
**Fix:** remove other platforms' names, badges and device frames from the listing and from the app's own screens. If App Review misread a real integration: "Reply to App Review in App Store Connect with additional information if the app's functionality and how it interacts with third-party platforms has been misunderstood."
**Common:** 2 (also 2.3.10 with 3.1.1 over links to a GitHub page, https://developer.apple.com/forums/thread/786489, Jun 2025).
**Row:** 58.

### R14. An app preview with frames or hands (2.3.4)
**Apple said:** "Includes device images and/or device frames." "Displays real hands." After the frame became an outline: "Includes framing around the video screen capture of the app." "Shows footage other than the app in use." https://developer.apple.com/forums/thread/797679 (Aug 2025). The same "framing around the video screen capture" on https://developer.apple.com/forums/thread/815379 (Feb 2026).
**Fix:** a full-bleed screen recording; 2.3.4 allows "narration and video or textual overlays". App Review's forum reply only offered an appeal.
**Common:** 2 in 2025–26.
**Row:** 61 (preview captured from the app).

### R15. "Free" in screenshots and previews counts as a price (2.3.2, 2.3.7)
**Apple said:** the developer marked unpaid content "free" in preview videos, and on a call App Review said "free" counts as a price *(developer's words)*. Outcome: "I was not able to find any terminology that Apple would accept, so I have removed all the annotations from the videos. They have accepted this". https://developer.apple.com/forums/thread/742443 (Nov–Dec 2023)
**Common:** 1. 2.3.7: screenshots and previews "should not include prices"; 2.3.14 (Oct 2026): creative assets carry no "specific or discounted pricing information".
**Row:** 59, 60 cover creative assets and the description; **not in checklist** for screenshots and previews.

### R16. The same image for several promoted purchases (2.3.2)
**Apple said:** "You submitted duplicate or identical promotional images for different promoted in-app purchase products" (RevenueCat Community, Nov 2025, link in R8).
**Fix:** removed the promotional images; promoting purchases on the store is optional.
**Common:** 1.
**Row:** not in checklist.

### R17. Age rating (2.3.6)
**Apple said:** "Age rating must reflect 18+" for a social app (R1); "17+ … or implement content filtering" for an AI app (R2). New from 16 Nov 2026: "Starting November 16, 2026, App Store Connect will include new content descriptors", declaring "Shared Location" and "Dating and Relationships: Features that enable dating or relationship connections between real people and/or a virtual companion that engages a user in sexual or romantic content." "Apps that include Dating and Relationships receive a minimum age rating of 18+." "All apps must have these declarations completed by January 12, 2027." https://developer.apple.com/news/?id=yxkh08us (2 Nov 2026)
**Common:** 2 rejections; the questionnaire is now required on every submission.
**Row:** 62 (age rating), partly: the two new descriptors aren't in it yet.

### R18. Background audio the reviewer can't find (2.5.4)
**Apple said:** three rejections for a reader app that speaks documents aloud; the latest said the audio "does not play in the background as intended", the earlier ones that the reviewer couldn't locate the audio feature *(developer's words)*. https://developer.apple.com/forums/thread/826849 (May 2026)
**Cause:** the reviewer didn't find the play button, or didn't start playback before locking the screen.
**Fix:** a fitness-app developer in the same thread, after two 2.5.4 rejections, believes a screen recording attached to the reply, showing audio continuing during a workout, got theirs through. If the app has no persistent audio, remove `audio` from `UIBackgroundModes`.
**Common:** 2 apps in 2026.
**Row:** 8 (background modes used for their purpose).

### R19. Apps that run code made after review (2.5.2)
**Apple said:** a builder app's co-founder "was told that his app violated Guideline 2.5.2", and the app was removed on 26 Mar 2026. Apple told The Information "certain vibe coding features breach long-standing App Store rules"; "An Apple spokesperson said the policy is not targeted specifically at vibe coding apps." https://mjtsai.com/blog/2026/03/20/updates-to-vibe-coding-apps-rejected-from-the-app-store/
**Cause:** apps that generate and run new apps inside themselves change their features after review. Apps merely written with AI tools aren't the target.
**Common:** 3 named apps (Replit, Vibecode, Anything), Mar 2026.
**Row:** not in checklist (only for apps that download or run code).

### R20. Features the reviewer couldn't see (2.5.19, 5.6)
**Apple said:** "We've identified a pattern of unusual behavior with the app that is commonly associated with fraudulent activity. Specifically, the app contains features that appear to have been intentionally hidden during the review process." Three times, same words: https://developer.apple.com/forums/thread/848576 (Sep 2026). The same for screens that unlock only after a purchase or a holding period, with two review accounts provided: https://developer.apple.com/forums/thread/841506 (Aug 2026).
**Cause (developer's guesses):** an "Upgrade to Pro" link to a web checkout not shown in the demo video, then hidden on iOS by a platform flag; an "Admin" link visible to everyone that worked only for admins; gated screens the reviewer couldn't reach.
**Fix suggested (reply, unconfirmed):** "give review an admin demo account and describe the admin screens in the Review Notes", "give a demo login for each role", and say what was removed and why; if the same boilerplate returns, appeal rather than reply again. No approval reported.
**Common:** 2 threads, 3+ developers; Apple: "over 22,000" such rejections in 2025. 2.5.19 (16 Oct 2026): "Don't include any hidden, dormant, or undocumented features in your app; your app's functionality should be clear to end users and App Review."
**Row:** 9 (no hidden or switched features), 91 (remote paywalls); a login for every role isn't in either.

## 3. Business (3.x)

### R21. Tips through a web link (3.1.1)
**Apple said:** "the recent changes to guidelines 3.1.1, 3.1.1(a), 3.1.3 and 3.1.3(a) have not changed the scenarios where In-App Purchase is required." "it would be appropriate to revise the app to use in-app purchase to process "tips" for developers and digital content creators." https://developer.apple.com/forums/thread/844046 (Aug 2026)
**Fix:** none reported (appeal pending).
**Common:** 1.
**Row:** 14 (digital goods through in-app purchase), 15 (outside purchase links only where allowed).

### R22. A business sign-up read as an outside purchase (3.1.1)
**Apple said:** "The app includes an account registration feature for businesses and organizations, which is considered access to external mechanisms for purchases or subscriptions to be used in the app." "Remove the account registration features for business and organizations." https://developer.apple.com/forums/thread/817400 (Mar 2026)
**Cause:** the reviewer assumed business accounts are paid for outside the app; the developer says nothing is sold outside.
**Fix:** none reported. A developer with 15 years of rejections: "Write review notes under the App Review Information box to avoid unnecessary rejection." (He also warns against appealing; see Myths.)
**Common:** 1; reviewer misreadings recur (a 3.1.1 rejection where the reviewer took the system's StoreKit sign-in sheet for a custom password field: https://developer.apple.com/forums/thread/827361).
**Row:** 14, 85 (the notes describe the business model).

### R23. No Restore button (3.1.1)
**Apple said:** "We found that your app offers in-app purchases that can be restored but does not include a "Restore Purchases" feature" (https://community.revenuecat.com/sdks-51/we-get-rejected-from-apple-store-review-about-restore-purchases-693, Oct 2021). A subscription-only app was rejected for the same (https://developer.apple.com/forums/thread/730977, Jun 2023).
**Fix:** a visible Restore button on the paywall that calls restore.
**Common:** 2, both older; few 2024–26 reports, likely because paywall SDKs ship the button.
**Row:** 25 (Restore visible).

### R24. Terms of Use and Privacy links missing (3.1.2)
**Apple said:** "The submission did not include all the required information for apps offering auto-renewable subscriptions." "The following information needs to be included within the app: A functional link to the Terms of Use (EULA) A functional link to the Privacy Policy" "The following information needs to be included in App Store metadata: A functional link to the Terms of Use (EULA) A functional link to the Privacy Policy" https://developer.apple.com/forums/thread/813493 (Jan 2026; the app linked Apple's standard EULA inside the app)
**Cause:** the Terms link lived only in the app.
**Fix:** "You'll need to add the link in the App description as well." (reply). Others had the links on the paywall, in settings, in the description and in the privacy field, and stayed rejected until App Review cleared it on its side (https://developer.apple.com/forums/thread/809635, Dec 2025). A RevenueCat staffer on a third case: check the link isn't broken and its touch target isn't too small next to the purchase button (https://community.revenuecat.com/tips-discussion-56/app-rejection-due-3-1-2-business-payment-subscriptions-5405, Nov 2024).
**Common:** 3 in 2024–26; the Oct 2026 survey (R3) quotes the older form "We were unable to find the following required item(s) in your app's metadata: – A functional link to the Terms of Use (EULA)".
**Row:** 24 (Terms and Privacy links in the app and the metadata).

### R25. The trial is louder than the price (3.1.2)
**Apple said:** "Your auto-renewable subscription promotes the free trial or introductory period for your subscription more clearly" "and conspicuously than the billed amount." (https://community.revenuecat.com/general-questions-7/rejected-due-to-guideline-3-1-2-business-payments-subscriptions-4775, Jul 2024). For a "Try for Free" main button: "The auto-renewable subscription promotes the free trial, introductory pricing, or introductory period for the subscription more clearly and conspicuously than the billed amount." (https://developer.apple.com/forums/thread/841626, Aug 2026)
**Fix:** "I changed it to "Continue" and got accepted." (three days after posting). A second developer, rejected for a paywall copied from Apple's own example: "So my app was just approved with no changes to the paywall", after pointing the reviewer to that example. RevenueCat's suggested line: "{{ sub_offer_duration }} free trial. After the trial ends, the subscription will renew for {{ price_per_period }}".
**Common:** 3.
**Row:** 20 (billed amount most prominent), 21 (trial length and the price after it).

### R26. The per-month figure is bigger than the billed price (3.1.2)
**Apple said:** "the billed amount is the most clear and conspicuous pricing element in the layout"; other pricing "must be displayed in a subordinate position and size to the total billed amount", naming "calculated pricing information" (a yearly plan with a 3-day trial and a per-month figure). https://community.revenuecat.com/general-questions-7/guideline-3-1-2-business-payments-subscriptions-6793 (Aug 2025)
**Fix:** none reported. The rule: the amount charged per period is the biggest price on screen; "$x/month" and "save y%" are smaller and below it.
**Common:** 1 verbatim; the same rule as R25.
**Row:** 20.

### R27. A free-trial toggle (3.1.2)
**Apple said:** "The purchase screen includes a toggle to add or remove a free trial from the subscription purchase." "This design is confusing and may prevent users from understanding" "that they are committing to an auto-renewing subscription that will begin charging them after the free trial period." "Remove the toggle for adding or removing a free trial from the subscription purchase screen." "Users should be presented with a clear subscription offer that explicitly states whether a free trial is included." https://www.revenuecat.com/blog/growth/r-i-p-toggle-paywall-we-hardly-knew-ye/ (9 Feb 2026)
**Cause:** one switch that quietly changed the product (often a weekly plan with a trial against a yearly plan without).
**Fix that passed:** Flo replaced its "Enable free trial" toggle with a fixed 14-day free-trial plan option on multi-plan paywalls (RevenueCat's 23 Apr 2026 update). Appeals didn't work, and apps already approved with toggles couldn't ship updates until they removed them (https://adapty.io/blog/your-toggle-paywall-is-about-to-get-rejected/, 11 Feb 2026).
**Common:** "In mid-January 2026, Apple started mass-rejecting apps with toggle paywalls." (Adapty). Superwall, after an off-the-record conversation with Apple: "Free trial toggles on paywalls are not allowed. Full stop." (https://superwall.com/blog/external-checkout-a-b-testing-and-trial-toggles-confirmed-apples-rules-for-ios, 3 Jun 2026)
**Row:** 20 and 21 are close; **not in checklist** as "no trial toggle".

### R28. Not enough "ongoing value" for a renewing subscription (3.1.2(a))
**Apple said:** "Auto-renewing subscriptions are only appropriate for services that provide dynamic, ongoing value" "to the user over an extended period of time." Three times (25 Jun, 8 Jul and 10 Jul 2025). https://community.revenuecat.com/general-questions-7/app-review-rejection-guideline-3-1-2-ongoing-value-6617
**Cause:** the reviewer didn't see what keeps arriving; arguing that cloud backup is ongoing value didn't move them.
**Fix:** switched to non-renewing subscriptions and passed.
**Common:** 1.
**Row:** 26 (ongoing value, seven days, all devices).

## 4. Design (4.x)

### R29. An iPad layout that uses part of the screen (4.0)
**Apple said:** "Parts of the app's user interface were still crowded, laid out, or displayed in a way that made it difficult to use the app when reviewed on iPad Air (5th generation) running iPadOS 26.0." "Specifically, when viewed on iPad, your app uses only a portion of the screen." https://developer.apple.com/forums/thread/800657 (Sep 2025)
**Fix:** none reported (App Review pointed to an appeal). Either lay it out for iPad, or drop iPad from the device families and pass R7 in compatibility mode.
**Common:** 1 in 2025.
**Row:** 74 (iPad layouts when iPad is supported).

### R30. Asking for a name or email after Sign in with Apple (4.0)
**Apple said (thread title):** "Your app requires users to provide their name and/or email address after using Sign in with Apple. This information is already provided by the Authentication Services framework." https://developer.apple.com/forums/thread/730223 (May 2023)
**Fix:** none posted. Take the name and email from the credential (Apple sends them only on the first authorization, so keep them then); make any extra field optional.
**Common:** 1 verified.
**Row:** 42 (asks only for what it needs), partly; the Sign in with Apple case isn't named.

### R31. A web wrapper (4.2)
**Apple said:** "Your app provides a limited user experience as it is not sufficiently different from a mobile browsing experience." "Including iOS features such as push notifications, Core Location, and sharing do not provide a robust enough experience to be appropriate for the App Store." (https://developer.apple.com/forums/thread/121924, Aug 2019). The same reasoning for a Capacitor app with native location, geocoding, the share sheet and Maps links: "not sufficiently differentiated from web browsing and that features such as Core Location or sharing alone are not robust enough" *(developer's words)*, https://developer.apple.com/forums/thread/812889 (Jan 2026).
**Fix suggested (Oct 2026 reply, unconfirmed):** build the core flow natively (the booking form, saved addresses, past trips) and hand off to the web only for payment; describe the features in plain words in the notes, not framework names.
**Common:** 3, plus a 4.2.2 rejection of a 650-book reading app (https://developer.apple.com/forums/thread/770026, Dec 2024).
**Row:** 72 (more than a website).

### R32. An invite-only app (4.2)
**Apple said:** "the usefulness of the app is limited because it seems to be intended for a small, or niche, set of users." "Specifically, the app is intended for invited friends only." (quoted on Hacker News, https://news.ycombinator.com/item?id=47916438, 2026)
**Fix:** in the same thread, another developer's niche app (a school's bell schedule) was approved only as unlisted distribution.
**Common:** 1.
**Row:** not in checklist.

### R33. Spam: "similar binary, metadata, and/or concept" (4.3(a))
**Apple said:** App Review on the forums: "Typically, these apps share a similar binary, metadata, and overall concept as apps already on the App Store, with only minor differences." (https://developer.apple.com/forums/thread/794830, Jul 2025, one flashcard app per language; https://developer.apple.com/forums/thread/788684, Jun 2025, where versions 1.0 and 1.1 passed and earned, then 1.2 and 2.1 were rejected.)
**Cause:** one app split across bundle IDs (4.3(a): "Don't create multiple Bundle IDs of the same app"), or an app that reads like many others (that wording is really 4.3(b)'s).
**Fix:** for variants, one app with the variations as in-app purchases. For originals, from developers who cleared it: "make sure the bundle id and CFBundleName are your own brand, not a placeholder like com.example", "delete template demo screens and starter assets that are still in the bundle", "name one verifiable feature that no other app in the category has and where to tap to see it — "our app is unique" gets ignored, a specific tap path gets read" (https://developer.apple.com/forums/thread/847036, Sep 2026). "Don't resubmit the same build with only a general explanation." (https://developer.apple.com/forums/thread/842971, Aug 2026). The Meet with App Review session on 788684 "was vague".
**Common:** 4 read in full, more than 15 other threads from late 2024 to 2026 with 4.3 in the title, and an Ask HN (https://news.ycombinator.com/item?id=48515589). Apple: "over 371,000" copy, spam or misleading rejections in 2025.
**Row:** 73 (not a copy), 93 (the app's own design, not generated).

### R34. A portfolio rejected in one night (4.3(a))
**Apple said:** "Guideline 4.3(a) - Design - Spam" on twelve updates on 22 Aug 2026, naming no app, screenshot or code. https://thechosenvictor.com/blog/twelve-apps-rejected-guideline-4-3a-spam
**Cause (the developer's measurements):** none of 1,030 Swift files was shared between apps, but the release notes under review were "46.3% mean, 90.9% max" similar, with "eight of twelve opening on the identical sentence", and "All twelve of mine went up inside ninety minutes from one API key" (his reply on thread 842971). Two screenshots showed things the apps don't contain.
**Fix:** rewrote every release note to that app's own changes, replaced the screenshots, and sent one reply on one app asking which apps Apple meant. Outcome not reported; the apps were later retired.
**Common:** 1 (twelve apps).
**Row:** not in checklist (release notes specific to each app; no batch of look-alike submissions).

### R35. A saturated category (4.3(b))
**Apple said:** an astrology app with a "Tarot card of the day" was rejected, and the App Review Board upheld it. John Gruber retracted his complaint about it: the app was "entirely dedicated to astrology, not astronomy". https://daringfireball.net/2026/08/retraction_app_store_rejection_of_the_week (8 Aug 2026). 4.3(b) lists "fortune telling" among the categories where Apple "will not accept new submissions unless they offer a meaningfully different or improved experience".
**Fix:** none; the developer moved to the web.
**Common:** 1, high-profile. 4.3(b) was rewritten in June 2026 to open "Don't submit apps that are indistinguishable from what's already widely available" (https://macrumors.com/2026/06/09/app-store-guidelines-low-quality-apps/).
**Row:** 73, 93.

### R36. A third-party login without an equivalent (4.8)
**Apple said:** "The app uses a third-party login service, but does not appear to offer an equivalent login option with the following features:" "The login option limits data collection to the user's name and email address." "The login option allows users to keep their email address private as part of setting up their account." "The login option does not collect interactions with the app for advertising purposes without consent." "If the app already includes a login option that meets the above requirements, reply to App Review in App Store Connect, identify which login option meets the requirements, and explain why it meets the requirements." https://developer.apple.com/forums/thread/750911 (Apr 2024, replies to May 2026)
**Cause:** Google sign-in added to an approved app; in May 2026 a guest mode plus a Microsoft login that asks for no email still failed.
**Fix:** Sign in with Apple (the replies' inference; no approval posted), or a reply naming the option that meets all three.
**Common:** 8 developers in that thread over two years; 5 more 4.8 threads in search results.
**Row:** 40 (an equivalent login).

## 5. Legal (5.x)

### R37. No account deletion (5.1.1(v))
**Apple said:** "The app supports account creation but does not include an option to initiate account deletion." "Only offering to temporarily deactivate or disable an account is insufficient." "If users need to visit a website to finish deleting their account, include a link directly to the website page where they can complete the process." "only apps in highly-regulated industries may require users to use customer service resources, such as making a phone call or sending an email, to complete account deletion." "If the app already supports account deletion, reply to App Review in App Store Connect and identify where to locate this feature." https://developer.apple.com/forums/thread/765160 (Oct 2024)
**Fix:** a delete in the app that deletes, or a direct link to the page that finishes it. Sign in with Apple or Google counts as creating an account.
**Common:** 1 verbatim; 3 more threads in search results.
**Row:** 37 (deletion inside the app).

### R38. Sign-in required for parts that aren't account-based (5.1.1(v))
**Apple said:** "Apps cannot require user registration prior to allowing access to app content and features that are not associated specifically to the user." The App Review Board: "Users should be allowed to access none account-based features before registration and login." "Once the user decides to use account-based features, the app may present the registration or login feature at that time." https://developer.apple.com/forums/thread/724336 (Feb 2023)
**Fix:** a guest mode for the parts that aren't account-based (the developer's plan; no outcome posted).
**Common:** 1 verbatim, older; the rule's text is unchanged.
**Row:** 31 (sign-in before purchase), 42 (no sign-in without account-based features).

### R39. Sign-up fields the app doesn't need (5.1.1)
**Apple said:** "Required fields not relevant to core functionality: City, State, and Birthdate" (BuddyBoss's summary of the rejection, updated 10 Jan 2026: https://buddyboss.com/docs/app-store-guideline-5-1-1-legal-privacy-data-collection-and-storage/)
**Fix:** remove them, or make them optional and labelled "(optional)", then reply in App Store Connect; the form was server-side, so no new build.
**Common:** 1.
**Row:** 42.

### R40. A vague purpose string (5.1.1(ii))
**Apple said:** "One or more purpose strings in the app do not sufficiently explain the use of protected resources. Purpose strings must clearly and completely describe the app's use of data and, in most cases, provide an example of how the data will be used." The rejected string: "In order to take a picture or video, this app requires permission to access the camera". https://developer.apple.com/forums/thread/790111 (Jun 2025; another developer there had "changed it twice")
**Fix:** none posted. Name the feature and give an example of what happens with the data.
**Common:** 2.
**Row:** 46 (purpose strings).

### R41. Tracking without ATT, or a tracking label you can't remove (5.1.2)
**Apple said:** "We noticed your app accesses web content you own where you collect cookies. However, you do not use App Tracking Transparency to request the user's permission before collecting data used to track." "Collecting cookies is a form of tracking." https://developer.apple.com/forums/thread/688582 (Aug 2021; the template since iOS 14.5). In 2026 an update that had stopped tracking was rejected under 5.1.2(i) for weeks, because App Store Connect wouldn't drop "Device ID used for tracking" while an older live version had `NSUserTrackingUsageDescription` *(developer's words)*; Apple DTS asked whether the binary still contains that key, or an SDK links AdSupport or AppTrackingTransparency. https://developer.apple.com/forums/thread/840650 (Aug 2026)
**Fix:** either ask with ATT before tracking, or remove tracking everywhere (SDKs, web views, the usage string) and update the labels; only the Account Holder or an Admin can.
**Common:** 2; Apple: "over 443,000" privacy rejections in 2025.
**Row:** 49 (labels match the code), 50 (ATT only if the app tracks).

### R42. Data sent to a third-party AI (5.1.1(i), 5.1.2(i))
**Apple said:** "The app appears to share the user's personal data with a third-party AI service but the app does not clearly explain what data is sent, identify who the data is sent to, and ask the user's permission before sharing the data." "Apps may only use, transmit, or share personal data after they meet all of the following requirements:" "Disclose what data will be sent", "Specify who the data is sent to", "Obtain the user's permission before sending data", "Identify in the privacy policy what data the app collects, how it collects that data, all uses of that data, and confirm any third party the app shares data with provides the same or equal protection". https://developer.apple.com/forums/thread/815109 (Feb 2026; the same text on 816140 and 815842). After 8 submissions: "We were not presented with the consent prompt on launch or anywhere else in the app." https://developer.apple.com/forums/thread/820209 (Mar 2026)
**Cause:** a privacy-policy line or a sign-up checkbox wasn't enough; the reviewer has to meet a clear ask that names the provider before anything leaves the device. On 820209 a "seen once" flag let the gate be skipped.
**Fix that passed (https://developer.apple.com/forums/thread/815842, Feb 2026):** rewrote the privacy policy, listing the AI processors; added a paragraph to the App Store description naming the provider and saying it doesn't train on the data; added a consent screen in onboarding with a "Continue with AI" button; said the same in the release notes. "Our version was just approved!" Another app passed "thanks to detailed feedback from the review team" (https://developer.apple.com/forums/thread/815100). 820209 removed the skip flag so the gate shows on every launch until the person agrees or declines.
**Common:** the biggest 2026 cluster: about ten developers on 815842 alone, plus 815109, 815100, 816140, 820209 and a children's app (815715), Feb–Mar 2026, after 5.1.2(i) gained "including with third-party AI" (Nov 2025). Some were updates that hadn't touched the AI: "This is the third rejection for a version that only changes the storefront images."
**Row:** 51 (third-party AI disclosed, permission first).

### R43. A required-reason API not declared (ITMS-91053)
**Apple said:** "ITMS-91053: Missing API declaration" "references one or more APIs that require reasons, including the following API categories:" "NSPrivacyAccessedAPICategoryUserDefaults" "you must include a NSPrivacyAccessedAPITypes array in your app's privacy manifest to provide approved reasons for these APIs used by your app's code." (the email pasted on https://github.com/OneSignal/OneSignal-iOS-SDK/issues/1397, May 2024)
**Fix:** the SDK added privacy manifests in its 5.2.0 release; "Its fixed." For your own code, declare the reason in the app's manifest.
**Common:** 8+ SDK issue trackers and forum threads in search results; enforced since 1 May 2024.
**Row:** 48 (privacy manifests).

### R44. An SDK without a privacy manifest (ITMS-91061)
**Apple said:** "ITMS-91061: Missing privacy manifest- Your app includes "<path/to/SDK>", which includes <SDK>, an SDK that was identified in the documentation as a privacy-impacting third-party SDK. Starting February 12, 2025, if a new app includes a privacy-impacting SDK, or an app update adds a new privacy-impacting SDK, the SDK must include a privacy manifest file." (Apple DTS, https://developer.apple.com/forums/thread/774960, Feb 2025)
**Fix (DTS):** "contact the SDK's provider for an updated version that includes a valid privacy manifest", and "make sure the file only describes the privacy practices of your app. Do not add the privacy practices of the SDK to your app's privacy manifest."
**Common:** 8 forum threads in search results, naming Firebase, GoogleDataTransport, Alamofire and Unity.
**Row:** 48.

### R45. A privacy policy page that stopped loading (5.1.1(i))
**Apple said:** not posted. "App #7 got rejected because I linked to a Notion page that had gone private." "The fix took two minutes. The delay cost me four days." https://dev.to/devkoan/your-ios-app-needs-a-privacy-policy-heres-how-to-get-one-in-60-seconds-hhg
**Fix:** host the policy as a plain public page you control.
**Common:** 1.
**Row:** 92 (plain static legal pages), 6 (every link works).

## 5.6 Developer Code of Conduct: the paywall flow

The 2026 surge: "manipulate customers" and "hidden features" rejections arrive without specifics, and several developers report reviews that lasted minutes.

### R46. An offer when the paywall is closed (5.6)
**Apple said:** "Guideline 5.6 - Developer Code of Conduct. The app attempts to manipulate customers into making unwanted in-app purchases. Specifically, the app shows a one time offer for subscription when the user closes the initial subscription page launched upon opening the app." https://developer.apple.com/forums/thread/768912 (Nov 2024)
**Setup:** "a soft paywall at the end of onboarding, and if the user closes that paywall we pop a second paywall with a one-time offer with an introductory offer (2 months for $1, "Once you close your one-time offer, it's gone!")". The same flow had passed in "the last few versions".
**Fix:** none posted (App Review said it would contact the developer).
**Since:** Adapty (Feb 2026) reports apps with a second offer on dismissal being rejected; RevenueCat (Feb 2026): "Apple is also getting stricter on instant paywall abandonment offers". Superwall's account of Apple's position (Jun 2026): "Showing any offer after a cancelled transaction is allowed — any price, any product, any type of deal." "What's not allowed is looping the user." Superwall's FAQ: "If your "one-time offer" keeps reappearing to the same user, Apple may flag this as deceptive marketing." (https://superwall.com/docs/support/faq/app-store-compliance-paywall-events)
**What separates them:** an offer after someone cancels the store's purchase sheet (they tried to buy) has no rejection on record in this search; an offer fired by closing the paywall has one.
**Common:** 1 verbatim, 2 vendor warnings.
**Row:** 90 (an offer after a declined purchase), which treats both triggers alike; the evidence doesn't.

### R47. A paywall with no way out (5.6)
**Apple said:** "We noticed your app attempts to manipulate customers into making unwanted in-app purchases." "The next submission of this app may require a longer review time." https://developer.apple.com/forums/thread/725056 (Feb 2023). The developer: "There is no exit button, the content is only available if purchased or subscribed."
**Advice in the thread (community):** if the app can't work without a subscription, "you should explain to the review team why your app requires to have such a business model". No outcome posted.
**Common:** 1 verbatim, older. An unofficial Sep 2026 forum list of 5.6 triggers names exit-discount offers and back-to-back paywalls in onboarding (https://developer.apple.com/forums/thread/848158).
**Row:** 29 (the paywall can be closed, or the hard paywall is clear).

### R48. A trial on screen, a plan without one selected (5.6)
**Apple said:** "Guideline 5.6 - Developer Code of Conduct" "The app attempts to manipulate customers into making unwanted In-App Purchases.", with a screenshot of the paywall attached. https://developer.apple.com/forums/thread/818023 (Mar 2026)
**Cause (accepted answer, not Apple):** "the Monthly plan is selected by default and doesn't appear to include a trial. Because the screen heavily promotes a free trial, having a prominent "Continue" button while a non-trial plan is selected can give the false impression that tapping it starts a trial." Also no list of what the subscription unlocks, and no renewal terms.
**Fix suggested:** no plan selected until the person picks one ("the "Subscribe" button remains disabled until a choice is explicitly made"), a list of what's unlocked, and the renewal terms. Outcome not posted.
**Common:** 1.
**Row:** 21 and 29 are close; **not in checklist**: the trial wording follows the selected plan.

### R49. Review suspended for quality (5.6)
**Apple said:** "Guideline 5.6 - Developer Code of Conduct - Review Suspended", "required quality standard", "not eligible for resubmission", "ensure every screen, interaction, and piece of content has been thoughtfully designed" (fragments pasted by several developers: https://developer.apple.com/forums/thread/835626, Jun 2026)
**Fix:** none reported. App Review pointed to the App Review Board; another reply advised submitting a newly designed app; one warned that resubmitting under a new app ID can read as spam.
**Common:** 3+ developers in one thread, Jun–Jul 2026.
**Row:** 93 (the app's own design, not generated).

### R50. A rating ask in onboarding (5.6.3, 5.6.1)
**Apple said:** RevenueCat (18 Jun 2026) reports Apple rejecting onboarding review prompts under 5.6.3: "Manipulating any element of the App Store customer experience such as charts, search, reviews, or referrals to your app erodes customer trust and is not permitted." Its advice: "Stop asking users to review your app during the onboarding flow." https://www.revenuecat.com/blog/engineering/dont-prompt-ratings-during-onboarding/
**Rule:** 5.6.1: "Use the provided API to prompt users to review your app … and we will disallow custom review prompts."
**Common:** 1 vendor report; also on the Sep 2026 forum list of 5.6 triggers (848158). No pasted rejection found.
**Row:** 81 (ratings through the system API), 87 (none in onboarding).

### R51. Retention messages in Apple's cancel flow (new, Nov 2026)
**Apple said (App Store Connect Help):** "Header and body text can't reference promotional offers, discounts, or specific prices, such as "$9.99," "50% off," or "one month free." Because all subscribers see this text, including those who aren't eligible for an associated offer, App Review rejects retention messages that contain pricing or offer mentions." "Avoid claims that coerce subscribers or guarantee unverifiable outcomes." https://developer.apple.com/help/app-store-connect/manage-subscriptions/configure-retention-messages (live since 4 Nov 2026: https://developer.apple.com/news?id=fk9ps3gv)
**What it means:** Apple now gives every subscription app a save message, and an offer, on its own cancellation screen. No 2024–26 rejection was found for an in-app cancel flow; the risk to a gauntlet stays 5.6's "manipulative practices".
**Common:** new; a rule, no reports yet.
**Row:** 89 (cancelling without a gauntlet), partly: the message-text rules aren't in it.

## What gets apps approved fast

1. **Plan for the slow week.** Apple's figure is "at least 50% of submissions in less than 24 hours and 90% in less than 48 hours". In Feb 2026 developers reported 10 to 30 days in Waiting for Review; one waited 15 days for review and had feedback minutes after it started (https://developer.apple.com/forums/thread/815537, https://developer.apple.com/forums/thread/815989). Submit a week before any date that's been announced.
2. **Notes a stranger can follow.** 2.3.1(a): new features "must be described with specificity in the Notes for Review section of App Store Connect (generic descriptions will be rejected)". Give a tap path to every paid and sensitive feature (R6), a login for every role and subscription state (R5, R20), plain words rather than framework names (R31), and the business model (R10). Write them from `review-notes.md`.
3. **A short recording as well as the account, never instead of it.** Apple: "If features require an environment that is hard to replicate or require specific hardware, be prepared to provide a demo video or the hardware." A TestFlight video "has helped" (R5); a recording got background audio through (R18). But "providing a demo video showing the app in use is not sufficient to continue the review" when the app needs a login (R1).
4. **Purchases ready before the upload.** Every product Ready to Submit and in the same submission (R8), the agreements active, the paywall fetching with a retry (R9), a purchase reachable in seconds (R6), and a line on the reviewer's own sandbox account (R5).
5. **Reply in App Store Connect first: specific, and once.** "You can correspond with App Review to resolve the issues before resubmitting the build." Ask which screen, or which app (R34: one reply on one app, not twelve). Pointing the reviewer to Apple's own paywall example got one app approved unchanged (R25); explaining the sandbox got one approved the next day (R5). The forums aren't a channel: "there are no review engineers actively monitoring the posts" (Apple DTS on thread 812208).
6. **Ask for a call.** "you can use the Reply to App Review message window to request a call with an Apple representative"; "include your time zone"; "Calls are typically completed within three to five business days." (https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review/). A call got R6 approved. App Review lists the options itself: "Reply to the message from App Review in App Store Connect and request clarification." "Request a call with an Apple representative to discuss the outcome of the review." "Submit an appeal to the App Review Board if you believe your app follows the App Review Guidelines." (thread 815079)
7. **Meet with App Review before a risky submission, not after a spam rejection.** "In each 30-minute video appointment, you can ask for advice on what to expect during review, how your app can best align with guidelines, reasons for common rejections". After a 4.3 it "was vague" (R33); another developer learned the kind of match but not the app (R34's thread).
8. **Appeal once, with specifics, through the form.** "Provide specific reasons why you believe your app complies with the App Review Guidelines." "Submit only one appeal per submission that didn't pass review." "Respond to any requests for additional information before submitting an appeal." And: "Don't use the Reply to App Review field to appeal a rejection or removal or to request an expedited review." Results: overturned (R3), upheld (R35), toggle appeals failed (R27).
9. **Expedite only for a broken release or a dated event.** For "fixing a critical bug in your app or releasing your app to coincide with an event you're directly associated with"; for a bug, "include the steps to reproduce the bug on the current version of your app"; "Please respect your fellow developers by seeking expedited review only when you truly need it." In Feb 2026 an expedite requested on a call was still waiting "24 hours after" (thread 815989).
10. **Ship an update's fix now and settle the guideline next time.** "If a bug-fix update is rejected but introduces no legal or safety concerns, you can choose to resolve the issues in your next submission", when the message opens "Bug Fix Submissions: The issues we've identified below are eligible to be resolved on your next update." "Do not resubmit the app at this time, as it will trigger a new review." "Issues that were deferred on a previous submission aren't eligible to be deferred again on the next submission." https://developer.apple.com/help/app-review/after-submitting-for-review/bug-fix-submissions
11. **A metadata problem needs no new build.** "Metadata Rejected: App Review didn't accept your metadata. Read the message from App Review, edit the metadata to resolve the issue, and reply to the message from App Review." https://developer.apple.com/help/app-store-connect/reference/app-and-submission-statuses
12. **Hold a risky feature for a later version.** A Mac dictation app was rejected under 2.4.5 for its Accessibility permission; "The clipboard-only version of WhisperPad needs no AX permission and that's what got through." (https://news.ycombinator.com/item?id=48369088). Since 2.5.19 the held feature arrives in its own reviewed version, described in that version's notes, never switched on from a server.
13. **Don't dodge.** New bundle IDs didn't clear a 4.3(a) (847036, in R33); resubmitting a suspended app under a new app ID can read as spam (R49); cancelling and resubmitting after eight days of waiting didn't jump the queue (815537).

## Myths

- **"Hard paywalls get rejected."** The guidelines don't require a free tier; 3.1.2(c) asks you to "clearly describe what the user will get for the price". What did get rejected: a paywall with no exit button where nothing worked without paying (R47, 2023), and an offer fired by closing the paywall (R46). Say in the listing and the notes what's paid, keep Restore and the terms on the paywall, and don't fire a second offer on close.
- **"Any link to my website breaks 3.1.1."** For the United States storefront, Apple's entitlements "are not required for developers to include buttons, external links, or other calls to action". Elsewhere the ban is on links "that direct customers to purchasing mechanisms other than in-app purchase"; support and privacy links are required. One binary ships to every storefront, so a US-only purchase link has to check the storefront. Superwall: "A web checkout link can be used in addition to — but not as a replacement for — in-app purchase in the United States."
- **"Remote paywalls get rejected."** Superwall: "Remote paywall updates and A/B testing are 100% allowed and encouraged." and "A paywall pushed via a remote update is held to the same standard as one submitted in a binary." The one remote-paywall rejection found was a paywall that didn't load offline (https://community.revenuecat.com/general-questions-7/remote-paywall-and-app-store-rrejection-5535, Dec 2024). The real risk since 2.5.19 is a variant the reviewer never saw.
- **"Apple's standard EULA isn't enough."** Every 2024–26 Terms rejection found was about where the link sits (R24), not which terms.
- **"It failed on IPv6, so IPv6 is the bug."** Apple DTS: "This does not mean that the failure was specifically caused by that network." "if your app crashes during App Review then that's clearly a bug in your app; your app shouldn't crash regardless of the state of the network." (https://developer.apple.com/forums/thread/49979). No 2024–26 rejection caused by IPv6 was found; test it anyway (row 11), it's cheap.
- **"Apple rejects apps written with AI."** "the policy is not targeted specifically at vibe coding apps" (R19). The rejections hit apps that run new code after review (2.5.2), look-alikes (4.3) and low quality (R49), whoever wrote the code.
- **"Weekly subscriptions aren't allowed."** 3.1.2(a): "the subscription period must last at least seven days". A week is the minimum, not banned.
- **"iPhone-only apps aren't reviewed on iPad."** They are, in compatibility mode (R7).
- **"A demo video can replace a demo account."** Not when the app needs a login (R1); 2.1(a) allows a built-in demo mode only "with prior approval by Apple".
- **"Appealing gets your account terminated."** A veteran's warning: "Do NOT file an appeal because they do make mistakes. If they do, you will be done for good." (thread 817400). Apple: "If you disagree with the outcome of your review, please submit an appeal. This may help get your app on the store." No termination for a good-faith appeal was found.
- **"Cancel and resubmit to get reviewed sooner."** One developer cancelled after eight days, resubmitted and waited again (thread 815537); nothing shows it helps.
- **"Urgency words are banned."** Superwall's FAQ: "Apple does not explicitly ban urgency-style messaging on paywalls." "These are permitted, but with one key rule: the offer must be genuine." The rejection on record (R46) was about when the offer appeared, not its words.

## Not in the checklist yet

For the next pass of `checklist.md` (numbers as of 16 Nov 2026):

1. Every purchase is reachable within a minute from the notes, with no visible test shortcut (R6).
2. No free-trial toggle (R27), and the trial wording follows the selected plan: no plan without a trial preselected under trial copy (R48). Rows 20, 21 and 29 are close.
3. No prices, "free" included, in screenshots and previews (2.3.7) (R15), and each promoted in-app purchase has its own image (R16).
4. The two age-rating descriptors added 16 Nov 2026: Shared Location, and Dating and Relationships (a romantic or sexual virtual companion counts; 18+); every app by 12 Jan 2027 (R17). Row 62.
5. Retention-message text: no prices or offers, no coercive or unverifiable claims (R51). Row 89.
6. 4.3 hygiene: the bundle ID and CFBundleName are the app's own, no template leftovers, release notes specific to each app, no batch of look-alike submissions, no resubmitting under a new bundle ID (R33, R34, R49).
7. An invite-only or single-organisation app goes out as unlisted (R32).
8. The paywall fetches products with a retry and has an offline state; it never sits empty (R9).
9. Apps that download or run code after review (2.5.2) (R19).
10. Refinements to existing rows: row 84, the reviewer's own sandbox Apple Account may already be subscribed (R5); row 9, a login for every role and no link that works only for admins (R20); row 42, never ask again for the name or email Sign in with Apple gave (R30); row 51, the AI consent shows on every fresh install until answered, and the provider is also named in the description (R42); row 90, the only verbatim rejection is for an offer fired by closing the paywall, not by cancelling the purchase sheet (R46).
