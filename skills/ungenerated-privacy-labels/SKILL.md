---
name: ungenerated-privacy-labels
description: Fill in Apple's App Privacy labels (the "privacy nutrition labels") in App Store Connect for any iOS or Mac app, right the first time. Builds the answer sheet from the privacy manifests the app and every SDK actually ship (Sentry, PostHog, RevenueCat, Firebase and the rest) plus the code, makes the app's PrivacyInfo.xcprivacy match, then fills it in through computer use or Claude in Chrome, or walks the owner screen by screen with exactly what to tick. Use for "App Privacy", "privacy labels", "nutrition labels", "do you collect data from this app", "what do I tick", "data types", "linked to the user", "used for tracking", or when the owner pastes one of App Store Connect's privacy screens. Part of ungenerated.
---

# App Privacy labels: one answer sheet, filled in once

Apple has no App Store Connect API key route for App Privacy, so the answers are clicked in: about 3 screens per data type, 30+ screens for a normal app. The work is getting the sheet right before the first click. Apple's definitions, in Apple's words, are in `ungenerated-audit-privacy` › `references/apple-privacy.md` §4; this skill is the doing. `references/lessons.md` has why each step exists.

## 1. Build the answer sheet from evidence, never from memory

1. **Every manifest, merged.** Build or resolve packages once (`xcodebuild -resolvePackageDependencies`), then
   `python3 scripts/labels.py <repo> --name <XcodeProjectName>`. It reads the app's own `PrivacyInfo.xcprivacy` files and every SDK's (Swift packages in DerivedData, Pods, vendored frameworks), skips SDK test apps, and prints one row per data type. A row marked **MISSING** is a type an SDK declares that the app doesn't: declare it unless the code proves the SDK can't send it (crash reporters declare Other Diagnostic Data, analytics SDKs Other Usage Data, and hand-written lists miss both).
2. **The code, for what no manifest says.** Sign-in (Sign in with Apple gives Name and Email Address), anything the person writes that syncs or is kept (Other User Content), text sent to an AI provider that keeps it for any time (Other User Content), the account id (User ID), an install id (Device ID: any device-level id, not only the advertising one), web views, and IP turned into location by an analytics project (PostHog GeoIP, GA) = Coarse Location unless that setting is off.
3. **Linked: Yes** whenever the app ties the SDK to the account (Sentry `setUser`, PostHog `identify`, RevenueCat `logIn`, Firebase `setUserID`), even where the SDK's own manifest says No.
4. **Tracking: Yes** only with ads, data brokers, or joining with other companies' data. No advertising id and no tracking prompt means No for every type.
5. **The release build only.** A feature compiled out of the release build (a debug leaderboard, a test bar) collects nothing. When the owner asks "does X count?", check whether X ships before answering.
6. **Write the sheet** into the project's docs, one table: data type · purposes · linked · tracking · what it is in this app. Make the app's `PrivacyInfo.xcprivacy` carry the same rows and re-run `labels.py` until nothing is MISSING. The privacy policy names the same things.

The usual stack, for a start (confirm each against the steps above):

| What the app uses | Data types | Purposes |
|---|---|---|
| Sign in with Apple / Google | Name, Email Address | App Functionality |
| An account | User ID | App Functionality (+ Analytics when analytics is identified with it) |
| An install id (rate limits, analytics before sign-in) | Device ID | App Functionality (+ Analytics) |
| Writing, notes, uploads that sync; text sent to an AI provider | Other User Content | App Functionality |
| RevenueCat / StoreKit status on a server | Purchase History | App Functionality |
| PostHog, Amplitude, Mixpanel, Firebase Analytics | Product Interaction, Other Usage Data | Analytics |
| Sentry, Crashlytics, Bugsnag | Crash Data, Performance Data, Other Diagnostic Data | App Functionality |

Never ticked without ads or marketing email: Third-Party Advertising, Developer's Advertising or Marketing, Product Personalization (unless recommendations use the data), Other Purposes.

## 2. Fill it in

Pick the first that's available:

1. **Computer use or Claude in Chrome.** Load that tool's skill first. Open App Store Connect › the app › **App Privacy**. The owner signs in themselves; never type their password or a 2FA code. Click the sheet in, check every purpose screen against it (§3), then stop on the product-page preview and show the owner. Press **Publish** only on their yes: for a live app it changes the store page at once.
2. **fastlane**, if it's installed and the owner accepts an Apple ID session (not the API key): `upload_app_privacy_details_to_app_store` takes the same sheet as JSON. Confirm the action exists first (`fastlane action upload_app_privacy_details_to_app_store`).
3. **The owner clicks**, with the card in §4.

## 3. The screens, in Apple's order

1. **Privacy Policy URL** (required); **User Privacy Choices URL** (optional, leave empty unless there's a page for it).
2. **"Do you or your third-party partners collect data from this app?"** Yes, whenever any SDK sends anything off the phone.
3. **The data types list**: one long checklist by category, under Apple's "Optional Disclosure" text. Ignore that text unless a type is collected only in a rare, optional form that shows the person's name and is chosen each time (an optional feedback form). "Purchases" stands alone in the list; its later screen calls it "purchase history".
4. **For each ticked type, in list order:** "Indicate how *type* collected from this app is being used" (purposes) → linked to the user's identity? → used for tracking?
5. **Product page preview** → **Publish** (top right).

**The check:** every purpose screen names its type. A screen for a type that isn't on the sheet is either a wrong tick in step 3 or a row the sheet missed; run `labels.py` before telling the owner to untick it. Purpose screens counted = rows on the sheet.

## 4. Talking to the owner

- They want the ticks, not the reasons. The first answer is the whole sheet as one table, one row per screen: **Screen · Tick · Linked · Tracking**. No prose per type.
- When they paste a screen, answer that screen only: its ticks and the two answers.
- When they ask about one item ("does the leaderboard count?"), answer yes or no with the one-line reason, then the full table again.
- Answers can change later without an app update: edit and Publish again. A new SDK or a new kind of data means a new row on the sheet, in the manifest and in the policy, together.
