# What we learned, and why

Lessons from building and launching Comma (iOS, Supabase backend), Flamely (Mac/Windows/iOS), Pip (iOS) and CutRoom (a Mac desktop app with an AI agent inside), Oct–Nov 2026. Each one came from a real leak, a near miss, or a rule the owner had to repeat. The apps appear only as examples.

## Keys and secrets

**1. A key pasted into chat is a leaked key: store it in an ignored file, never echo, log or commit it, and tell the owner it must be rotated.** Why: owners paste live keys mid-chat; it happened in several projects. Comma, Oct–Nov 2026; Flamely, Oct–Nov 2026; CutRoom, Oct 2026.

**2. Secrets live in ignored local env files and CI secrets, never in the repo, the docs or the logs.** The most powerful keys (database service role) live only in CI secrets. Why: the standing rule became "Service role key ... GitHub Actions secrets ONLY, never local". Comma, Oct–Nov 2026.

**3. One key per environment.** Test keys in Debug, live keys in production, and the build fails if they cross. Why: a Release build with a payments test key alerts and then crashes; a test key that grants access in production is a free pass for everyone. Flamely, Oct 2026.

**4. Never ship a build that carries the owner's own login, keys or session.** Every person who installs it signs in as themselves. Why: "my friend will download this same version, can you tell what if he is also logged into my claude". CutRoom, Oct 2026.

**5. Before a repo goes public, remove keys and personal media from the files and from git history, then add a pre-commit hook that blocks them coming back.** Why: "remove any of the claude api key and stuff, I will put this opensource, plus also remove my pictures and videos". CutRoom, Oct 2026.

**6. A private product repo never becomes public. A public showcase uses images, never the product's code.** Why: "YOU CAN [use] COMMA EXAMPLES IN THE PUBLIC REPO BUT NEVER THE CODE OF ITS GRAPHICS ONLY IMAGES". Comma, Nov 2026.

**7. Uploads and automation sign with a scoped store API key, not a person's account password.** It can be revoked alone and never needs a human session. Comma, Nov 2026.

## Access control

**8. Before opening sign-ups, check every table's row-level policies.** "Full access using true" for any signed-in user, or RLS off on a table, lets anyone with the public key read or wipe it. Why: an audit found internal pipeline tables open to every signed-in account and a backup table with RLS off. Comma, Oct 2026.

**9. Fix open tables with restrictive admin-only policies that AND with the existing ones**, so the owner's own tools keep working while users are locked out. Comma, Oct 2026.

**10. Enforce every limit on the server: money ceilings, minimum input, rate limits, paid gates.** The client shows the limit; the server is the lock. Why: "a per-person money ceiling enforced on the server". Comma, Nov 2026.

**11. Server-to-server brokers sign their requests (HMAC) and refuse unsigned calls.** Comma, Nov 2026.

**12. A new external integration (an MCP connector, a partner API) ships with admission closed** until sign-in, ownership and each gate are verified on a real device. Comma, Nov 2026.

**13. A destructive account action refuses when signed out, before clearing anything locally.** Otherwise it wipes the person's work with no server record. Comma, Nov 2026.

## Production and other projects

**14. Never pause, restore, delete or change a production database, a sibling app or a release workflow without the owner's yes in this conversation.** Migrations are additive and have a rollback. Why: an agent paused the wrong production project: "why you paused flamely prod ... for fuck sake"; "I WOULDNT CHANGE DB AT ALL … YOU CAN TEST IT BUT DONT CHANGE THINGS". Comma, Oct 2026; Flamely, Oct–Nov 2026.

**15. Keep each app's accounts, keys, buckets and projects separate.** A shared org or key means one leak opens both. Why: "THIS IS NEW APP KEEP THIS SEPARATE FROM comma and flamely please". Pip, Oct 2026; Comma, Oct 2026.

**16. Don't switch on an optional production transport just because its server side is deployed.** Each needs its own authenticated release-build check on a device. Why: a signed-in launch crash came from a probe to an endpoint that wasn't deployed. Comma, Nov 2026.

## Agents and AI

**17. An AI agent with web access may read only files inside its own project folders.** A page it reads can tell it to read a secret and send it out. Why: an audit found file reads unrestricted while web fetch was on; "one poisoned web page can send private files out during a normal run". Fixed with path checks. CutRoom, Nov 2026.

**18. Never let the AI provider key reach the client.** Every model call goes through your server, which checks the user, the limit and the input. Comma, Oct–Nov 2026.

## The device

**19. Hide sensitive content when the app goes to the background**, so the app-switcher snapshot iOS writes to disk doesn't hold it. Why: a review found an open private card would land in the snapshot. Pip, Nov 2026.

**20. A test build never fills a real account with sample data**; samples stay on the device and never sync. Why: a build put sample content into the owner's real account. Comma, Oct 2026.

**21. Never test on the owner's real projects or leave test items in their space.** Use private copies and clean up. Why: a "Script test" project appeared in the owner's library; "delete your tests videos". CutRoom, Oct 2026.

## How to run it

**22. Security is a standing pre-launch layer: API leaks, data leaks, hack vulnerabilities**, every time, not once. Why: "SECONDARY LAYER AND AUDIT CHECKER API LEAKS DATA LEAK HACK VULNERABILITIES". Flamely, Nov 2026.

**23. Do the checks yourself when a connector or key on the machine allows it**; send back only the steps that need the owner's hands (a dashboard behind their login, rotating a key, Touch ID), with exact click-by-click steps. Why: "if there is any connector connected to you that you can use for this, probably you don't really need my permission". Comma, Oct 2026.

**24. Start from the app profile, report everything, wait for approval, then fix.** Why: "all skill should start from apps ... COVER EVERYTHING AUDIT AND TELL USER AND AFTER APPROVAL THESE SKILL FIX THESE". Flamely, Nov 2026.

**25. List what is deployed, not just what is in the repo.** Flamely's database project still ran four functions that weren't in the repository (`admin_wipe_paddle`, `admin_seed_paddle_catalog`, …). They turned out to be retired stubs that only answer 410 "gone", but a deployed function nobody owns is where a hole hides: read each one, and delete them before launch. Flamely, Nov 2026.

**26. When the deploy is an upload of a bundled file, read the deployed copy back and probe it.** After uploading a payment webhook through the database connector, Flamely compared the stored source with the bundle and sent an unsigned request (it must answer 401) before trusting it. Flamely, Nov 2026.

**27. A connector that refuses destructive SQL is a guard, not an obstacle.** The database connector declined deleting user accounts; the owner did it in the dashboard. Never work around it with another route. Flamely, Nov 2026.

## Assistant connectors

**28. An assistant connector gets its own narrow grant, never the person's app session.** Supabase's built-in OAuth server, in beta at the time, offered only identity scopes and its tokens reach whatever the person's session can (a consent screen doesn't narrow that), so the connector issues its own audience-bound grant with the app's permissions, checks it on every call, and lets its refresh tokens expire before the grant behind them. Comma, Nov 2026.

**29. Give an assistant the least power first, and enforce it on the server.** The first grant only saved new items and read their receipts; reading the person's work is a separate, optional permission at consent, and a write to existing work adds a version beside the person's words, never editing or deleting them. A tool's read-only or destructive annotation is a hint to the client, not authorization. Comma, Nov 2026.

**30. What a connecting client says about itself is an unverified label: show it as such and never let it authorize anything.** Any client can register under a famous assistant's name and a model can report any provider it likes, so the consent screen and the owner's list label names unverified, treat the return address as plain data, and open or copy saved links only on an explicit tap, never fetching them. Comma, Nov 2026.

**31. Split server authority by job: each automated caller gets its own key and a short literal list of the database functions it may call, never the service key.** The connector holds one signing key per broker (one only issues grants, the other only saves and reads receipts) while the service key stays inside the database platform, so a leaked save key can't grant access; an unattended content pipeline gets the same kind of narrow door, because the service key on its machine could do anything in the database. Comma, Oct–Nov 2026.

**32. A server request that carries a privileged key goes only to a pinned origin and refuses every redirect.** `fetch` follows redirects by default and a custom key header can travel with them, so the brokers send with redirects off, treat any 3xx as unavailable, cap the response size and time out. Comma, Nov 2026.

**33. Check the grant and write in one transaction, under the row lock disconnect takes, then prove it by disconnecting.** A permission check followed by a separate write lets a save from a just-disconnected assistant slip through, so the save locks the grant row, re-checks status, owner and scope (on the token and on the stored grant) and writes the item and its receipt together. The last check runs in the real assistant: connect, save, see it on the phone, disconnect, save again and see it refused; a health response or a fixture account is not that check. Comma, Nov 2026.

**34. Treat everything a connector sends an assistant as published.** The guide, the server instructions and every tool result are readable by the person in their own chat, so none of it may hold a secret, another person's data or a prompt you couldn't show. Comma, Nov 2026.

**35. Every assistant write carries a stable key: the same key returns the first answer, the same key with different content is a conflict.** A retry after an ambiguous timeout then can't save twice and the assistant checks the receipt instead of saving again; a model can still invent a new key after losing context, so this narrows duplicates without promising exactly once. Comma, Nov 2026.

**36. Cap open OAuth client registration, and let clients already connected keep working at the cap.** Dynamic registration is an unauthenticated write anyone can repeat; the connector admits at most 1,000 lasting clients, while refresh and tool calls for existing ones carry on. Comma, Nov 2026.

## Web sign-in

**37. Sign in with Apple on the web signs with a client secret that lasts at most six months: record its end date and a one-command renewal where the team will see them.** It is a token your server signs from a key, not a lasting password; when it lapses, web sign-in stops with no change on your side, and so does anything that signs in through it, like an assistant connector. Comma, Nov 2026.

**38. When one auth project serves the app and the web, group Apple's Services ID under the app's App ID, list it first in the provider's client IDs, and keep the app's ID and callbacks after it.** The first ID drives the web flow (with the bundle ID first, the phone signs in while Apple rejects the web) and dropping the app's ID breaks the phone; the grouping is what makes both resolve to the same person, so never link the two by matching email strings, which can differ or be reused. Comma, Nov 2026.

**39. Use a sign-in callback only after checking it belongs to this browser's pending sign-in.** A callback that arrived after sign-out brought the session back to life, until the ownership check moved before the callback is consumed. Comma, Nov 2026.

**40. Split a Cookie header on semicolons only.** A parser that also split on commas let a crafted cookie value create a second, trusted cookie pair; a regression test reproduced it before the fix. Comma, Nov 2026.

**41. Rate-limit IPv6 by its /64, treat IPv4-mapped addresses as IPv4, and keep sign-in limits separate and stricter.** One device can rotate through endless addresses inside its own /64, so a limit keyed on the full address is no limit. Comma, Nov 2026.

## The database

**42. Revoke a new Postgres function from PUBLIC, not only from the app's roles.** Every function gets EXECUTE for PUBLIC by default and the anonymous and signed-in roles inherit it, so a function revoked from both stayed callable by anyone until the security advisor flagged it; revoke from public, anon and authenticated, then grant what it needs. Comma, Oct 2026.

**43. Keep tables the client must never read in a schema the data API doesn't expose, reached only through narrow server functions.** The entitlement mirror, request queue, limits and switches, webhook receipts, push outbox, deletion jobs, waitlist and feedback board all live there, so a missing or wrong row policy can't leak what the API can't see; prove it with an anonymous request the API refuses because the schema isn't exposed, and never use a definer function to get around a policy that fails. Comma, Oct–Nov 2026.

**44. Keep internal tools and users' data apart: production gets its own project before the first real user, and the two meet only through narrow server functions.** The first schema shared a development project with an internal content pipeline; production started as a fresh project with only the app's schema, written so the move was a copy, not a rewrite, and one function publishes finished items into the app's read-only copy while another hands requests to the pipeline's inbox, so either side can be rebuilt without touching the other. Comma, Oct 2026.

**45. An anonymous session is a signed-in token, so every costly endpoint and policy checks it isn't anonymous.** Supabase gives anonymous users the authenticated role with an is_anonymous claim, and the first AI function would have let every fresh install reach the model once anonymous sign-ins were on; refuse them in code (a 403 asking to sign in) and in policies with a restrictive check on the claim beside a permissive policy, never on metadata the user can edit. Comma, Oct 2026.

**46. On a table every signed-in account can read, each new column is public too: check it before adding.** Read access was granted table-wide (anonymous accounts included), so new credit columns rode on it with no new grant; it was safe only because those handles and links were already public. Comma, Oct 2026.

**47. Rules that must hold whatever client writes go in the table as constraints.** A private cancel-flow entry can only be new or handled and can never be voted on, so no admin drag, bug or later screen can move it onto the public board, and each JSON column a client writes is size-capped (a script's beats at 200 KB) so a modified client can't fill the database through its own rows. Comma, Oct–Nov 2026.

**48. Credits and points are a ledger only the server writes, unique per (reason, reference).** They come only from a verified signed callback (an ad network's reward) or a server trigger, never granted client-side as a fallback, so a retried callback can't pay twice, a farmed action can't earn twice and a jailbroken phone can't print credits; cap them per day too. Comma, Oct 2026.

## Public endpoints

**49. A secret-guarded endpoint and every spending limit fail closed when the secret or limit isn't set.** The billing webhook, the scheduled push sender and backup, and the feedback admin door answer 503 until their secret exists (an admin key under 24 characters counts as unset), and the shared AI budget refuses every call while no daily limit is set, so a missed setup step blocks instead of opening the door. Comma, Oct–Nov 2026.

**50. An endpoint that accepts both anonymous and signed-in callers refuses a user token that doesn't verify; it never quietly treats the caller as anonymous.** An expired token gets 401 so the app refreshes and resends, instead of the post being filed without its account. Comma, Nov 2026.

**51. Every write path gets its own server switch that stops new writes without a code change and keeps saved data readable.** Posting, voting and the waitlist can each be paused the moment a spam wave starts while the rest keeps working, and the assistant connector opened one account at a time, the owner's first, before testers and then everyone. Comma, Nov 2026.

**52. Set the hashing salt once and never change it.** Anonymous votes and rate limits are keyed to salted hashes of device ids and network addresses (one network adds at most three votes to a post, counted under a row lock), so rotating the salt like a secret silently resets every limit and lets everyone vote again. Comma, Nov 2026.

## Hosting and backups

**53. On a database plan with no backups, run your own nightly backup before real users arrive.** The free plan keeps none and pauses idle projects, so a nightly job writes one gzipped snapshot of every personal table, plus the auth users and their sign-in identities so a restore keeps people's ids, to a private bucket that a lifecycle rule empties after 30 days; content that can be republished is left out, and real traffic keeps the project awake. Comma, Oct 2026.

**54. Never host app media in a web root shared with another site's backend.** The first media host shared its document root with the website's backend: one wrong .htaccess took the whole subdomain down and SFTP uploads kept dropping, so media moved to object storage behind a CDN. Comma, Oct 2026.

**55. Audit what your host serves publicly, not just what the app uses.** The full original audio of 83 reels and their music stems sat public on the content host although the app never used them: the highest copyright risk in the system, open to anyone who guessed the URL pattern. Comma, Oct 2026.

**56. On GitHub Free a private repo gets no deployment approvals and no environment secrets.** Required reviewers and wait timers on private repos need Enterprise, and environment secrets in private repos need a paid plan, so a deploy gate has to live elsewhere or be paid for. Comma, Oct 2026.
