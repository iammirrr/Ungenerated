# What we learned, and why

Lessons from launching Comma (iOS, AI writing), Flamely (Mac/Windows/iOS), Pip (iOS) and CutRoom (Mac), Oct–Nov 2026. The apps appear only as examples; each rule holds for any app.

## Deleting the account

**1. Deleting the account is separate from cancelling, and says plainly that it does not cancel the store subscription.** Link to the platform's subscription settings next to it. Why: people assume deletion stops billing; it doesn't, and the store keeps charging. Comma, Nov 2026.

**2. Deletion refuses when signed out, before clearing anything.** Otherwise it wipes the person's work on the phone with no server record and no deletion actually done. Comma, Nov 2026.

**3. Offer export first, then hold to delete, and publish web deletion steps.** Apple requires in-app deletion; Google Play requires in-app and web. Comma, Nov 2026.

## AI and consent

**4. Ask before any of the person's text leaves the device for a third-party model.** The app's own sheet says what is sent, to whom, and what stays on the phone (for example "not used for training; audio and video stay on the phone"). Comma, Nov 2026.

**5. Save the consent answer at the tap.** Why: a delayed save lost the answer when the app closed, and the person was asked again (or worse, treated as yes). Comma, Nov 2026.

**6. Swiping the consent sheet away means no.** Only a tap on Allow is a yes. Comma, Nov 2026.

**7. Consent is revocable in settings, and revoking keeps the app usable by hand.** Why: AI is a help, not a gate; a person who says no still writes. Comma, Nov 2026.

**8. Show people what the AI did and what was sent where, in settings.** Why: "AI TRANSPARENCY A LOT, SHOW EXACTLY WHAT IS LEFT". Comma, Nov 2026.

**9. Use the platform's on-device speech recognition where it can; never route a person's voice through your servers without need.** Why: "this microphone is supposed to be local using local iOS stuff". Comma, Oct 2026.

## Analytics and crash reports

**10. Analytics get the answers, never the person's own words.** A cancel reason goes to analytics as the picked category plus a "wrote a note" flag; the note itself goes to a private store. Why: "PostHog gets the answers, never their words". Comma, Nov 2026.

**11. Identify analytics users by account id only, never name or email.** Comma, Nov 2026.

**12. Keep analytics and crash reports off until the person says yes**, where the law or the promise requires it. Why: "take consent we need it". Pip, Oct 2026.

**13. Show no tracking prompt the app doesn't need.** If nothing tracks across apps, there is no App Tracking Transparency prompt. Why: "MAKE SURE IT DOESN'T ASK ANY WEIRD POPUP TRACKING". Comma, Nov 2026.

**14. Filter test builds out of the data, and keep analytics anonymous where it can be.** Flamely, Oct 2026.

**15. Read an analytics or crash vendor's pricing and data terms before wiring it in.** Why: "I'm really scared like PostHog will charge me a lot simply because they're asking me for my bank account ... we should read this through". Comma, Oct 2026.

## Collect less

**16. Store the minimum the feature needs.** Keep the book's cover, not the photo of the person's shelf. Why: "we only save their covers ... never the picture of them ... until its necessary". Pip, Oct 2026.

**17. A test build never fills a real account with sample data.** Samples stay on the device and never sync. Why: a build put sample content into the owner's real account. Comma, Oct 2026.

**18. In a personal tool, every network call is one the user triggered, and each is logged.** CutRoom's standing rule: "no accounts, no telemetry; network calls logged". CutRoom, Oct 2026.

**19. The owner's personal media stays local:** out of git, previews only on localhost, never published. Before publishing anything built from logs, strip ids, hosts, timestamps and paths. CutRoom, Oct–Nov 2026.

## Disclosures

**20. Privacy and terms pages are live and linked before launch**, from the store listing and from every purchase screen. Why: the listing's privacy URL was empty and both pages returned 404 a day before submission. Comma, Nov 2026.

**21. When data practice changes, update every disclosure in the same change:** the privacy policy, the web pages, the store labels, the cookie notice. Why: "UPDATE THE WEB PAGES ... AND ANY OTHER DISCLOSURE WHERE NEEDED". Flamely, Nov 2026.

**22. Check the launch traps nobody tests**: an age gate (COPPA), self-hosted fonts (GDPR), session replay with consent and masking (CIPA), unsubscribe link and postal address (CAN-SPAM), renewal terms by the button, a DMCA agent for uploads. Why: "the hidden 53k mistake are usually the things nobody thought to test ... FOR ALL THESE LEGAL SHIT EVEN THINGS I MISSED". Flamely, Nov 2026.

**23. Cancel feedback stays private even when the feedback board is public.** Comma, Nov 2026.

**24. A new data point changes the policy first, then the code.** Collecting countries from the IP meant replacing Flamely's "without your IP address or your location" line with the exact new wording, in the app's policy and the website's together, a new version and date, and the existing re-consent screen once; the owner approves the wording before anything ships. Flamely, Nov 2026.

**25. The app's tracking switch can promise less than the vendor collects.** Check the vendor's own enrichment (GeoIP on ingestion, IP storage, session replay defaults) in its project settings and in stored events, not just the SDK call in the code. Flamely, Nov 2026.

**26. A public feedback board is user content.** Posts are shown publicly once approved, so it needs the takedown contact and, in the US, a registered DMCA agent like any upload feature. Flamely, Nov 2026.

**27. Before launch, read every sentence of the policy and terms against what ships now.** A site round can quietly make a line false: a form that now asks for a name, a demo that no longer asks for the microphone, a connection to the person's own AI assistant (say who handles what they share there: the assistant's maker, under their own agreement), an introductory offer the terms never mention. Fix them in the same round. Comma, Nov 2026.

## Sign in with Apple's own duties

**28. Sign in with Apple leaves two jobs your auth service may not do: revoking Apple's token when the account is deleted, and acting on Apple's account notifications.** Supabase Auth keeps no Apple refresh token and ignores Apple's server-to-server notices (forwarding turned off, consent revoked, Apple account deleted), so you need your own function that exchanges the authorization code at sign-in and calls Apple's revoke endpoint at deletion, plus an endpoint for the notices; flagged in the first plan, the revoke was still recorded as not built at the pre-submission audit. Comma, Oct–Nov 2026.

**29. Email to people who hid their address with Apple needs your sending domain registered with Apple's relay and signed (SPF and DKIM), and every address check must accept both relay domains.** The domain's mail records allowed only the web host, so the welcome email would have gone to spam, and to relay addresses it would never have arrived; relay addresses end in privaterelay.appleid.com and, since Apple's change in 2026, also private.icloud.com. Comma, Oct–Nov 2026.

## Deletion, sign-out and retention

**30. Deleting an account is one job with a recorded step for every place the person's data lives, inside the database and out.** Personal tables cascade from the user, shared things they made keep the content and lose their id, and the job's own row (no foreign key, the id only) outlives the deletion as proof; Comma's first job did the database half and left the billing customer, the analytics person, the email contact and Apple's token for later. Comma, Oct–Nov 2026.

**31. Every outside connection to the person's data (an AI assistant, an OAuth grant) is listed in settings with what it may do and a Disconnect, and account deletion revokes them first.** Comma revokes assistant grants in the same transaction that queues the deletion, and every connector tool refuses an account with a deletion pending, so nothing writes into data being erased; disconnecting stops future access and keeps what was already saved. Comma, Nov 2026.

**32. A push token belongs to whoever is signed in on that phone now: sign-out removes it, and registering it moves it from any other account.** Without both, a shared or handed-down phone keeps getting the previous person's notifications. Comma, Oct 2026.

**33. A retention period needs the job that enforces it.** Comma's data plan gave every table a period and a reason (AI usage 13 months for cost and abuse history, billing events 25 months for the refund window, the push outbox 30 days, deletion records two years with the id only), but no scheduled job prunes any of them, so each period, and any policy line built on one, is only a promise. Comma, Nov 2026.

## Forms and public pages

**34. A waitlist answers the same whether the address is new or already on it.** Otherwise the form tells anyone whether a given person signed up; keep each address once, lower-cased, and rate-limit by a salted hash of the network address, never the address itself. Comma, Nov 2026.

**35. Keep the owner's personal details (a home city, a "made by" line) off the app's public pages unless a law requires them.** The website's footer named the owner's home city; it came off every page the round the owner saw it, and the privacy policy and terms name the operator and the governing country without it. Comma, Nov 2026.

## Other people's work in the product

**36. Show other creators' work only as small frames and short excerpts beside your own analysis, each with a linked handle and a link to the original, never their video or audio.** Small frames used to teach are the lowest risk (transformative; the EU quotation exception also needs the source and the author's name), a full transcript is riskier, and hosted music is a near-complete copy: the old pipeline's music fallback on a public URL was the biggest copyright risk in the system. Why: "it's supposed to also show the creators profile". Comma, Oct 2026.

**37. Before launch, give creators one takedown path that removes their items everywhere and keeps them out, and don't count on the DMCA safe harbour for a library you curate.** The safe harbour covers material stored at a user's direction, not what you choose and publish, so register a DMCA agent, remove a taken-down item from the library and from every save (never the person's own writing built on it) and block the creator from future publishing and requests; Comma's terms gave a takedown email, but the blocklist that makes a takedown stick was still a proposal. Comma, Oct–Nov 2026.
