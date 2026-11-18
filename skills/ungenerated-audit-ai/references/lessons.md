# What we learned, and why

Lessons from building AI into Comma (an iOS app that helps people write short video scripts), CutRoom (a Mac video editor with an AI agent inside), Flamely and Pip, Oct–Nov 2026. Comma used the smallest Claude model for every job; that is an example of "the cheapest model that does it well", not a rule about a model.

## Cost and limits

**1. Cap what one person can cost, with a hard money ceiling on the server.** Why: "WE CAN'T LET 1 USER COST US [that much] a month ... where we using AI". Comma, Nov 2026.

**2. Cost-test every AI job on light, typical and heavy inputs before trusting a number.** Why: "those 50 cents are just 1 or 2 days testing so basically we need better testing"; "make test users like a fitness creator with his story ... I want to know how much it costs ... and the quality". Comma, Nov 2026.

**3. A cost measured on another model is not evidence.** An early high estimate came from a bigger model than the one that shipped. Comma, Nov 2026.

**4. Use the cheapest model that does the job well, and invest in prompts and guidance rather than a bigger model.** Why: "please use haiku only ever no opus at all" (Comma); "SONNET WITH GOOD BACKUP PROMPTS AND SKILL IS ALL WE NEED" (CutRoom). Comma, Nov 2026; CutRoom, Nov 2026.

**5. Don't add costly tools (live web search) the price can't carry.** Hand the person a brief they can take to their own assistant instead. Why: "we do not want to do web search ... we are not charging people enough for that"; "We are not an LLM tool". Comma, Nov 2026.

**6. Plan for abuse before launch: count credits per person and decide limits.** Why: "how much they abuse AI that is on them and we have to understand the token credits". Flamely, Oct 2026.

**7. A trial gets a smaller AI allowance.** Why: "no free week only 2 days free with very limited ai". Comma, Nov 2026.

**8. Cut cost with caching, a short stored summary per person, and attachments converted to text once.** Why: "caching the context of the users and making summary points"; "it should convert it into MD file". Comma, Nov 2026.

**9. When the output is the same for everyone, generate it once at build time** on the cheapest good model instead of calling it live. Pip, Oct 2026.

**10. Where the person's own assistant can do the heavy work (through MCP), let it, and just store the result.** Why: "that could potentially also save us a token". Comma, Nov 2026.

## Limits people can see

**11. Make limits visible before and after use:** a count by the action, a toast when one is used, a used-up screen, an offline message, and exempt the owner's account. Why: "it's supposed to be very clear that there is a limit ... per week"; "MAKE SURE TOASTS AND ERRORS FOR NO INTERNET AND EXHAUSTED SCREEN"; "clear my limit ... I'm the owner". Comma, Nov 2026.

**12. The usage screen reads the server's own gate, so it can't disagree with what's enforced; show fair use as a share, never in dollars.** Why: "SHOW EXACTLY WHAT IS LEFT". Comma, Nov 2026.

**13. Limit-stopped requests are listed in the history too.** Otherwise a refusal looks like a lost request. Comma, Nov 2026.

## Never on junk, never twice

**14. No AI call on too little input: a minimum of real words in the app, and the server refuses too.** Why: "if I just pick H or gibberish, it's still calling the AI, which is obviously wasting credits". Comma, Nov 2026.

**15. Navigation and resuming never re-run AI; re-running is a button that says it uses credit.** Why: "it starts loading again"; "there should be a button like reprocess the idea". Comma, Nov 2026.

**16. Keep every version the person paid for.** Why: "IF WE WASTED CREDITS ON THAT YES IT WOULD BE BETTER TO KEEP IT". Comma, Nov 2026.

**17. No AI button on an empty document;** offer it once there are words. Why: "it doesn't even know what topic that I want to write in". Comma, Nov 2026.

## Consent

**18. Consent before any text leaves the device, in the app's own sheet that says what goes where.** Swiping it away is no; the answer is saved at the tap (a delayed save lost it when the app closed); revoking keeps the app usable by hand. Comma, Nov 2026.

**19. On iOS, a sheet inside a sheet can't show the root's sheet;** present the consent sheet from both places, or the AI action silently does nothing. Comma, Nov 2026.

## Quality

**20. Bad output is usually bad input: send the whole source, not a slice.** Why: bad scripts came from sending 6 of 16 parts and a prompt that kept the reference's subject, not from the model. Comma, Oct 2026.

**21. Never write blind: every call gets the full context, and context given once is never asked for again.** Why: "it doesn't take context it doesn't take anything"; "I already gave it a context and when I was borrowing the shape it was again asking me". Comma, Nov 2026.

**22. When the input is thin, ask a few plain, non-technical questions that expand the idea**, never re-asking what was said. Why: "I know I didn't give it enough context, so it just started to hallucinate"; "It should let me expand on the ideas instead". Comma, Oct–Nov 2026.

**23. The person's new context outranks old drafts in the prompt.** Why: "If I give it a context, then it's supposed to follow that". Comma, Nov 2026.

**24. Adapting a template transfers the concept and keeps the structure, and swaps the subject completely.** Why: "how does this even relate to software engineering? We have to convert that into something similar"; "the scripts aren't good it needs 1:1". Comma, Oct 2026.

**25. Let the person set how closely to follow a reference** (a closeness control), never one fixed level. Comma, Nov 2026.

**26. Measure fidelity with an eval that counts (line-for-line structure), not by eye.** Comma, Oct 2026.

**27. Output comes back whole; a partial result is fixed at the source, never shown as done.** Why: "neither the AI give the full script". Comma, Nov 2026.

**28. Several takes must be different kinds, chosen first.** Why: "three different drafts, like story, opinion ... Not three drafts in the same". Comma, Nov 2026.

**29. Show one result once;** never a first answer that gets replaced. Why: "it was showing me different research, and then after that, it kind of changes that". Comma, Nov 2026.

**30. AI never invents a fact.** Every claim needs a source the person gave; with none, it says nothing. CutRoom, Nov 2026.

**31. Suggested ideas are specific and researchable, not generic.** Why: "it's gonna talk about the science of lifting weight in a very specific topic". Comma, Nov 2026.

## The person stays in charge

**32. AI proposes; the person approves.** Changes are shown, previewed and approved, all at once or one by one; anything removed can be brought back. Why: "it's cutting automatically. It's not even asking me"; "I STILL CAN'T BRING BACK WHAT YOU CUT". CutRoom, Oct 2026.

**33. When a run produces nothing, say so in one sentence with the reason and one next step.** A vague "try again" loop is a launch blocker. Why: "it said it doesn't work. Try again. I tried again. It doesn't work". Comma, Nov 2026; CutRoom, Nov 2026.

**34. Ask at most one question, then act on the best guess and name it.** CutRoom, Oct–Nov 2026.

## Surfaces and setup

**35. A demo before sign-in calls the real model; never hard-code its output.** Why: "you need to ask the real Haiku model ... it just literally put those lines like hard-coded them". Comma, Oct 2026.

**36. Don't rely on an on-device model for a demo; many phones lack it.** Use a server model capped per device. Comma, Oct 2026.

**37. Design boards and test tools call the same prompts and model as the app.** Why: "I WANNA ACTUAL USABLE APP SO I CAN GIVE YOU GOOD FEEDBACK". Comma, Oct 2026.

**38. Keep every prompt in one file.** Review and parity across surfaces get easy. Comma, Oct 2026.

**39. Ship the AI's guidance (rules, examples) inside the app, not in the developer's folder.** Why: "IT SHOULDN'T BE DEPENDING ON SOME FOLDER, CUTROOM APP IS DISTRIBUTIVE APP". CutRoom, Nov 2026.

**40. An agent with web access reads only inside its own folders.** A fetched page can tell it to send a secret out. CutRoom, Nov 2026.

**41. When a conversation restarts, carry a summary of what was decided into the new one.** CutRoom, Nov 2026.
- **Admin AI work runs on the owner's own Claude, not the app's API key.** Content work only the owner does (breaking
  down media for a library, processing a queue) can be a skill in the owner's Claude Code: scripts do the mechanical
  half (download, frames, transcript, upload, checks), the owner's subscription does the thinking, and the app's API
  budget stays for users. Publish only through a script that checks the result first. (Comma, Nov 2026)

## Ceilings that hold

**42. When the usage gate can't be read, refuse the AI call.** The first AI function counted usage through a database schema the API didn't expose, so every count failed quietly, read as zero and capped nobody; it now answers "unavailable" whenever the gate, the budget reservation or the model's price can't be read. Comma, Oct–Nov 2026.

**43. Reserve each call's worst-case cost before sending, with the SDK's automatic retries and any model fallback off, and never release a reservation early.** SDKs retry by default, so one timeout can become a second billable call nobody reserved, and a request that timed out may still be billed, so an interrupted call keeps its reservation; usage rows carry the reservation id so nothing counts twice. Comma, Nov 2026.

**44. Size each job's effort and output cap from measured runs, and check that no answer hit the cap.** At low effort a whole script came back in about 300 tokens of thin lines, so the job runs at medium; its cap is twice the most any script has used, which halved the worst a call can cost, and the cost run confirmed no answer was cut off. Comma, Oct–Nov 2026.

**45. Keep the AI kill switch, the model id, every limit and every exemption in server config, and test the limits from an ordinary account.** The model moved to the smallest one with a config edit and no app release, and the code's default matches the config; but the owner's account is exempt and a beta flag lifted everyone's allowance, so the owner's own testing never met the trial's or the free plan's limits. Comma, Nov 2026.

**46. Every route to free AI must cost an abuser something: no email or anonymous sign-up, fixed jobs only, and a pre-sign-in demo that takes nothing but an id and the person's short input.** The first AI function let anonymous sessions through, so each phone could have become many accounts with fresh allowances; the demo reads its source from the server's own copy, never from the request, and is capped per install, per network (a keyed hash of the IP) and in total, so neither endpoint works as a free general-purpose model. Comma, Oct 2026.

**47. When you add an AI task, add it to the usage log's allowed kinds in the same change.** Two new tasks were logged under an old task's name because the log's check didn't allow them yet, so their cost per task couldn't be told apart. Comma, Nov 2026.

**48. Measure the client's real request timeout against a deliberately slow server before sizing AI jobs.** A build's configured 12-second limit turned out to be 60 seconds in practice, the only reason a 25-second script survived; a number in config is a guess until it is measured. Comma, Oct 2026.

**49. Before an expensive AI job, run the cheap checks that can make it unnecessary.** An item already processed answers at once, ten people asking for the same item make one job, and a cheap qualification check (the video's views against its creator's recent median) runs before the breakdown, with a refusal that doesn't use the person's allowance. Why: "if that is not even an outlier, then why would you even do that?" Comma, Oct–Nov 2026.

**50. Don't plan to cut AI cost by moving real jobs to the phone's own model.** Apple's on-device model had 4,096 tokens for input and output together and wasn't on older phones (the owner's included), while the smallest cloud model wrote a script for about a third of a cent. Why: "should be also opt for a local model". Comma, Oct 2026.

## Prompts that keep the person's subject

**51. Borrow a template's mechanics, never what it was selling, and keep a reference with a sponsor plug in the eval set.** A "comment a word and I'll send the link" ending, a numbered count or a callback stays, with the person's own word or a blank like [WORD]; the source's sponsor, product and link kept leaking into unrelated scripts until the prompt forbade them, and five paid live runs on a reference ending in a product plug then showed no source brand in the spoken lines. Comma, Nov 2026.

**52. Label generated structure from a small fixed set of familiar roles, and let the person rename them.** Labels the model invented per script came back vague and repeated; six fixed roles (Hook, Context, Problem, Turn, Payoff, Call to action), written exactly and shareable by two parts, read the same on every surface. Why: "there are two proof, there are demo, free part". Comma, Nov 2026.

**53. On thin input the model stays on the person's exact subject and writes a visible blank for any fact they didn't give.** It drifted to a nearby topic that was easier to fit (a game featuring slime became a recipe for real slime) and added mechanics, timings and results nobody gave, and asking it to match a source's length tempted it to pad lines with invented facts; a short blank like [how many] or [the result] keeps the line true and shows what to fill in. Comma, Nov 2026.

## Media in, published content out

**54. Separate the voice from the music before transcribing, and distrust a transcript of a video nobody speaks in.** Song lyrics landed in the library as spoken lines, and a "Please subscribe" phrase appeared on a video with no voice at all; transcribe the vocal stem only, and leave the lines empty when nobody talks. Comma, Nov 2026.

**55. Show a vision model every frame, as labelled contact sheets, never a hand-picked few.** Frames taken every half second and set in grids, each tile stamped with its time, fit a minute of video's 60–150 frames into a few images, so cuts, reveals and text changes aren't missed and image tokens stay low. Why: "NOT 18 ... ALMOST ALL ... I WANT CLIPPING FRAME WHERE NEED". Comma, Nov 2026.

**56. AI output that goes live to everyone passes coded checks, is retried once with the failures quoted, and then waits for a person until it has earned automatic publishing.** A scan found 46 of 79 live library items broken (parts with no job, talking videos with no lines, song lyrics stored as speech); the gate checks transcript coverage (99% of the words, in order, in whole sentences), lengths and required fields, and the owner reads every item the first week, then one in ten plus everything flagged. Why: "FULL COMPLETE SENTENCES, 100% coverage". Comma, Nov 2026.

## Assistant connectors

**57. Serve an assistant connector's working rules from the server, as MCP instructions and a guide tool, not only from a plugin's skills.** A phone gets the connector without the plugin, so rules kept only in the plugin left it with tools and no guidance; once the server sent the same uses as instructions and a guide tool returned the app's own writing rules from the prompt file the app uses, the phone behaved like the desktop. Comma, Nov 2026.

**58. An assistant writing into the app saves only when the person asks, keeps their decisions apart from its own suggestions, and reports a save only on the tool's receipt.** Brainstorming is not a save request; a request the tools can't do (schedule, edit a script) is offered plainly as what they can do, "saved" is never claimed as "on your phone" before the phone refreshes, and when the tools are missing it says so and keeps the content in the chat, never falling back to direct database access that would skip the plan check, the limits and the idempotency. Comma, Nov 2026.

**59. Test a new provider key with one real call before it replaces the old one in production.** An Anthropic key the owner sent started `sk-ant-usr-`: a user key with no workspace, refused on every call with "must include the anthropic-workspace-id header". A workspace key (`sk-ant-api03-`) needs no extra header. Checked with a free models call and one tiny message before touching the server's secret, the outage didn't get worse. Comma, Nov 2026.
