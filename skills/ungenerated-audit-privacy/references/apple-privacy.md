# Apple privacy: manifests, required reasons, labels, tracking, AI

What Apple's own pages require for privacy on the App Store, in Apple's exact words (short quotes), with the page and the date read. **Every page was read on 16 Nov 2026**; re-read before relying on a list, they change. The App Review checklist rows that use this are in `ungenerated-audit-app-review/references/checklist.md` §4; the guideline quotes in context are in that skill's `apple-docs.md` §5–7.

Short names used below:
- **Manifests**: developer.apple.com/documentation/bundleresources/privacy-manifest-files and its child pages
- **Reasons**: developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api and …/app-privacy-configuration/nsprivacyaccessedapitypes/nsprivacyaccessedapitype
- **Labels**: developer.apple.com/app-store/app-privacy-details/
- **Tracking**: developer.apple.com/app-store/user-privacy-and-data-use/
- **SDK list**: developer.apple.com/support/third-party-SDK-requirements/
- **G 5.1.1** etc.: developer.apple.com/app-store/review/guidelines/#5.1.1 ("Last Updated: October 16, 2026")

## 1. Privacy manifests

- The file: "Apps and third-party SDKs — distributed as XCFrameworks, Swift packages, or Xcode projects — can contain a privacy manifest file, named `PrivacyInfo.xcprivacy`." It records "The types of data collected" (all platforms) and "The required reasons APIs your app or third-party SDK uses" (iOS, iPadOS, tvOS, visionOS, watchOS). (Manifests, read 16 Nov 2026)
- Top-level keys (Manifests):
  - `NSPrivacyTracking`: "whether your app or third-party SDK uses data for tracking as defined under the App Tracking Transparency framework."
  - `NSPrivacyTrackingDomains`: domains "that engage in tracking. If the user has not granted tracking permission through the App Tracking Transparency framework, network requests to these domains fail and your app receives an error."
  - `NSPrivacyCollectedDataTypes`: one dictionary per data type with `NSPrivacyCollectedDataType`, `NSPrivacyCollectedDataTypeLinked`, `NSPrivacyCollectedDataTypeTracking`, `NSPrivacyCollectedDataTypePurposes`. "Xcode won’t generate a privacy report correctly if you define your own collected data types ... Use values listed in the documentation for the keys."
  - `NSPrivacyAccessedAPITypes`: one dictionary per required-reason category with `NSPrivacyAccessedAPIType` and `NSPrivacyAccessedAPITypeReasons` (§2).
- Where it goes: iOS apps "place the privacy manifest at the root of your app’s bundle"; iOS frameworks "at the root of your framework’s bundle"; macOS in `Contents/Resources/` (or `Versions/A/Resources/` for frameworks). Swift packages must declare it: "Xcode doesn’t recognize privacy manifest files as resources by default", so `.process("PrivacyInfo.xcprivacy")`. Static libraries can't carry one: build "a new static framework target". (developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk, read 16 Nov 2026)
- Who declares what: "If you use the API in your app’s code, then you need to report the API in your app’s privacy manifest file. If you use the API in your third-party SDK’s code, then you need to report the API in your third-party SDK’s privacy manifest file." "For each executable or dynamic library in an app that uses a required reason API, the bundle that includes the executable or dynamic library needs to include a privacy manifest file". For data: "Your app’s privacy manifest file doesn’t need to cover data collected by third-party SDKs that your app links to." (Reasons; developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests, read 16 Nov 2026)
- When an SDK needs one: always if it's on the SDK list (§3); "Otherwise, include a privacy manifest file in your third-party SDK if it uses a required reasons API, collects data about the person using apps that include the third-party SDK, enables the app to collect data about people using the app, or contacts tracking domains." (Manifests)
- Upload gates: "Starting May 1, 2024, apps that don’t describe their use of required reason API in their privacy manifest file aren’t accepted by App Store Connect." "App Store Connect rejects app submissions that include invalid privacy manifest files"; the email names "the name and path of the invalid files". "Starting February 12, 2025, apps you submit for review in App Store Connect must contain a valid privacy manifest file for a certain number of commonly used third-party SDKs." (Reasons; adding-a-privacy-manifest…, read 16 Nov 2026)
- An SDK with a broken manifest you can't get fixed: delete or fix it in the archive and submit from Xcode; "Removing or modifying the invalid privacy manifest breaks the archived app’s signature. Xcode will re-sign your app when you distribute your archive from the Archives organizer." Debugging: TN3181 (developer.apple.com/documentation/technotes/tn3181-debugging-invalid-privacy-manifest).
- The report: Product › Archive, Control-click the archive, "Generate Privacy Report"; "Refer to this report when you provide your app’s privacy details in App Store Connect." (describing-data-use-in-privacy-manifests, read 16 Nov 2026)

## 2. Required-reason APIs, every category and code

From Reasons (read 16 Nov 2026). "Regardless of whether a user gives your app permission to track, fingerprinting is not allowed." "You may use these APIs and the data derived from their use for the declared reasons only. These declared reasons must be consistent with your app’s functionality as presented to users, and you may not use the APIs or derived data for tracking." New reasons: developer.apple.com/contact/request/privacy-manifest-reason/.

**`NSPrivacyAccessedAPICategoryFileTimestamp`**: `creationDate`, `modificationDate`, `fileModificationDate`, `contentModificationDateKey`, `creationDateKey`, `getattrlist`, `getattrlistbulk`, `fgetattrlist`, `stat`, `fstat`, `fstatat`, `lstat`, `getattrlistat`.
- `DDA9.1`: "display file timestamps to the person using the device. Information accessed for this reason, or any derived information, may not be sent off-device."
- `C617.1`: "access the timestamps, size, or other metadata of files inside the app container, app group container, or the app’s CloudKit container."
- `3B52.1`: "access the timestamps, size, or other metadata of files or directories that the user specifically granted access to, such as using a document picker view controller."
- `0A2A.1`: an SDK's wrapper, used "when the app calls your wrapper function"; "may only be declared by third-party SDKs"; not for SDKs "created primarily to wrap required reason API(s)".

**`NSPrivacyAccessedAPICategorySystemBootTime`**: `systemUptime`, `mach_absolute_time()`.
- `35F9.1`: "measure the amount of time that has elapsed between events that occurred within the app or to perform calculations to enable timers." Not sent off-device, except "information about the amount of time that has elapsed between events that occurred within the app".
- `8FFB.1`: "calculate absolute timestamps for events that occurred within your app"; those timestamps may leave the device, the boot time may not.
- `3D61.1`: "include system boot time information in an optional bug report that the person using the device chooses to submit", "prominently displayed to the person as part of the report."

**`NSPrivacyAccessedAPICategoryDiskSpace`**: `volumeAvailableCapacityKey`, `volumeAvailableCapacityForImportantUsageKey`, `volumeAvailableCapacityForOpportunisticUsageKey`, `volumeTotalCapacityKey`, `systemFreeSize`, `systemSize`, `statfs`, `statvfs`, `fstatfs`, `fstatvfs`, `getattrlist`, `fgetattrlist`, `getattrlistat`.
- `85F4.1`: "display disk space information to the person using the device"; not sent off-device (a local-network exception with explicit permission, never "over the Internet").
- `E174.1`: "check whether there is sufficient disk space to write files, or to check whether the disk space is low so that the app can delete files when the disk space is low. The app must behave differently based on disk space in a way that is observable to users." Not sent off-device, except to skip a download.
- `7D9E.1`: disk space "in an optional bug report that the person using the device chooses to submit".
- `B728.1`: health research apps only, "to detect and inform research participants about low disk space".

**`NSPrivacyAccessedAPICategoryActiveKeyboards`**: `activeInputModes`.
- `3EC4.1`: "your app is a custom keyboard app"; "Providing a systemwide custom keyboard to the user must be the primary functionality of the app."
- `54BD.1`: "present the correct customized user interface to the person using the device. The app must have text fields for entering or editing text and must behave differently based on active keyboards in a way that is observable to users."

**`NSPrivacyAccessedAPICategoryUserDefaults`**: `UserDefaults`.
- `CA92.1`: "read and write information that is only accessible to the app itself. This reason does not permit reading information that was written by other apps or the system".
- `1C8F.1`: "only accessible to the apps, app extensions, and App Clips that are members of the same App Group as the app itself."
- `C56D.1`: an SDK's wrapper around user defaults, SDKs only.
- `AC6B.1`: "read the `com.apple.configuration.managed` key to retrieve the managed app configuration set by MDM, or to set the `com.apple.feedback.managed` key".

Typical app: `UserDefaults` → `CA92.1` (add `1C8F.1` when a widget or extension shares an App Group suite); file dates in its own container → `C617.1`; elapsed-time measurements → `35F9.1`; checking free space before saving → `E174.1`.

## 3. SDKs that need their own manifest and signature

From the SDK list (read 16 Nov 2026): "You must include the privacy manifest for any SDK listed below when you submit new apps in App Store Connect that include those SDKs, or when you submit an app update that adds one of the listed SDKs as part of the update. Signatures are also required in these cases where the listed SDKs are used as binary dependencies. Any version of a listed SDK, as well as any SDKs that repackage those on the list, are included in the requirement." Signatures: "When you adopt a new version of a third-party SDK in your app, Xcode will validate that it was signed by the same developer".

The 86 names: Abseil, AFNetworking, Alamofire, AppAuth, BoringSSL / openssl_grpc, Capacitor, Charts, connectivity_plus, Cordova, device_info_plus, DKImagePickerController, DKPhotoGallery, FBAEMKit, FBLPromises, FBSDKCoreKit, FBSDKCoreKit_Basics, FBSDKLoginKit, FBSDKShareKit, file_picker, FirebaseABTesting, FirebaseAuth, FirebaseCore, FirebaseCoreDiagnostics, FirebaseCoreExtension, FirebaseCoreInternal, FirebaseCrashlytics, FirebaseDynamicLinks, FirebaseFirestore, FirebaseInstallations, FirebaseMessaging, FirebaseRemoteConfig, Flutter, flutter_inappwebview, flutter_local_notifications, fluttertoast, FMDB, geolocator_apple, GoogleDataTransport, GoogleSignIn, GoogleToolboxForMac, GoogleUtilities, grpcpp, GTMAppAuth, GTMSessionFetcher, hermes, image_picker_ios, IQKeyboardManager, IQKeyboardManagerSwift, Kingfisher, leveldb, Lottie, MBProgressHUD, nanopb, OneSignal, OneSignalCore, OneSignalExtension, OneSignalOutcomes, OpenSSL, OrderedSet, package_info, package_info_plus, path_provider, path_provider_ios, Promises, Protobuf, Reachability, RealmSwift, RxCocoa, RxRelay, RxSwift, SDWebImage, share_plus, shared_preferences_ios, SnapKit, sqflite, Starscream, SVProgressHUD, SwiftyGif, SwiftyJSON, Toast, UnityFramework, url_launcher, url_launcher_ios, video_player_avfoundation, wakelock, webview_flutter_wkwebview.

Check: list the app's packages (`Package.resolved`, `Podfile.lock`, `pubspec.lock`, `package.json`) against the list, then find each one's `PrivacyInfo.xcprivacy` inside the built app. An SDK not on the list still needs one if it uses a required-reason API, collects data or tracks (§1): "you are responsible for all the code the SDK includes in your app". Analytics, crash, payments and AI SDKs that aren't on the list are no exception to that.

## 4. App privacy labels

From Labels (read 16 Nov 2026), unless marked.

**What counts.** "“Collect” refers to transmitting data off the device in a way that allows you and/or your third-party partners to access it for a period longer than what is necessary to service the transmitted request in real time." "“Third-party partners” refers to analytics tools, advertising networks, third-party SDKs, or other external vendors whose code you’ve added to your app." "even if you collect the data for reasons other than analytics or advertising, it still needs to be declared." "Data that is processed only on device is not “collected”". Data sent and "immediately discarded after servicing the request" need not be disclosed.

**Data types**, label name and manifest constant (`NSPrivacyCollectedDataType…`):

| Category | Type: Apple's definition | Constant suffix |
|---|---|---|
| Contact Info | Name: "Such as first or last name" | `Name` |
| | Email Address: "Including but not limited to a hashed email address" | `EmailAddress` |
| | Phone Number: "Including but not limited to a hashed phone number" | `PhoneNumber` |
| | Physical Address: "Such as home address, physical address, or mailing address" | `PhysicalAddress` |
| | Other User Contact Info: "Any other information that can be used to contact the user outside the app" | `OtherUserContactInfo` |
| Health & Fitness | Health: "Health and medical data" (HealthKit, Clinical Health Records, research, "any other user provided health or medical data") | `Health` |
| | Fitness: "Fitness and exercise data, including but not limited to the Motion and Fitness API" | `Fitness` |
| Financial Info | Payment Info: card or bank details; not collected when "the payment information is entered outside your app, and you as the developer never have access" | `PaymentInfo` |
| | Credit Info: "Such as credit score" | `CreditInfo` |
| | Other Financial Info: "Such as salary, income, assets, debts" | `OtherFinancialInfo` |
| Location | Precise Location: "the same or greater resolution as a latitude and longitude with three or more decimal places" | `PreciseLocation` |
| | Coarse Location: lower resolution, "such as Approximate Location Services" | `CoarseLocation` |
| Sensitive Info | "racial or ethnic data, sexual orientation, pregnancy or childbirth information, disability, religious or philosophical beliefs, trade union membership, political opinion, genetic information, or biometric data" | `SensitiveInfo` |
| Contacts | "a list of contacts in the user’s phone, address book, or social graph" | `Contacts` |
| User Content | Emails or Text Messages: "subject line, sender, recipients, and contents" | `EmailsOrTextMessages` |
| | Photos or Videos: "The user’s photos or videos" | `PhotosorVideos` |
| | Audio Data: "The user’s voice or sound recordings" | `AudioData` |
| | Gameplay Content | `GameplayContent` |
| | Customer Support: "Data generated by the user during a customer support request" | `CustomerSupport` |
| | Other User Content: "Any other user-generated content" | `OtherUserContent` |
| Browsing History | "content the user has viewed that is not part of the app, such as websites" | `BrowsingHistory` |
| Search History | "Information about searches performed in the app" | `SearchHistory` |
| Identifiers | User ID: "screen name, handle, account ID, assigned user ID, customer number" | `UserID` |
| | Device ID: "the device’s advertising identifier, or other device-level ID" | `DeviceID` |
| Purchases | Purchase History: "An account’s or individual’s purchases or purchase tendencies" | `PurchaseHistory` |
| Usage Data | Product Interaction: "app launches, taps, clicks, scrolling information ... or other information about how the user interacts with the app" | `ProductInteraction` |
| | Advertising Data: "information about the advertisements the user has seen" | `AdvertisingData` |
| | Other Usage Data: "Any other data about user activity in the app" | `OtherUsageData` |
| Diagnostics | Crash Data: "Such as crash logs" | `CrashData` |
| | Performance Data: "Such as launch time, hang rate, or energy use" | `PerformanceData` |
| | Other Diagnostic Data | `OtherDiagnosticData` |
| Surroundings | Environment Scanning | `EnvironmentScanning` |
| Body | Hands, Head | `Hands`, `Head` |
| Other Data | "Any other data types not mentioned" | `OtherDataTypes` |

**Purposes** (`NSPrivacyCollectedDataTypePurpose…`): Third-Party Advertising (`ThirdPartyAdvertising`), Developer’s Advertising or Marketing (`DeveloperAdvertising`), Analytics: "Using data to evaluate user behavior, including to understand the effectiveness of existing product features, plan new features, or measure audience size or characteristics" (`Analytics`), Product Personalization: "Customizing what the user sees" (`ProductPersonalization`), App Functionality: "Such as to authenticate the user, enable features, prevent fraud, implement security measures, ensure server up-time, minimize app crashes, improve scalability and performance, or perform customer support" (`AppFunctionality`), Other Purposes (`Other`).

**Linked.** "Data collected from an app is often linked to the user’s identity, unless specific privacy protections are put in place before collection to de-identify or anonymize it". Not linked also needs: "You must not attempt to link the data back to the user’s identity" and "You must not tie the data to other datasets". "“Personal Information” and “Personal Data”, as defined under relevant privacy laws, are considered linked to the user." Analytics identified by account ID is linked.

**Optional disclosure** needs all of: not used for tracking; not used for third-party advertising, your advertising or marketing, or other purposes; "Collection of the data occurs only in infrequent cases that are not part of your app’s primary functionality, and which are optional for the user"; provided in the app's interface, clearly, with "the user’s name or account name ... prominently displayed in the submission form" and chosen "each time". "data collected on an ongoing basis after an initial request for permission must be disclosed." Separate optional sets exist for product improvement programs (explicit two-option opt-in, changeable in settings, not linked, not for personalization), regulated financial services and IRB-approved health research.

**Cases Apple settles** (Labels): web views: "Data collected via web traffic must be declared, unless you are enabling the user to navigate the open web." IP addresses: declare by use, "such as precise location, coarse location, device ID, or diagnostics." In-app messages between users: "Declare emails or text messages". Free text and voice: "Mark "Other User Content" to represent generic free form text fields and "Audio Data" for voice recordings"; if you ask for a specific type (a name, photos), declare it. Different data for free or paid users, children, regions: "Please disclose all data collected from your app". Apple frameworks: "You are not responsible for disclosing data collected by Apple." Precise location coarsened before storing: declare Coarse Location.

**Links.** "Privacy Policy (Required): The URL to your publicly accessible privacy policy." "Privacy Choices (Optional)": where people manage or delete their data.

**Keeping it true.** "You’re responsible for keeping your responses accurate and up to date. ... you do not need to submit an app update in order to change your answers." Publishing confirms the answers "comply with the App Review Guidelines and applicable law" (developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy, read 16 Nov 2026).

## 5. Tracking and App Tracking Transparency

From Tracking and Labels (read 16 Nov 2026).

- Definition: "“Tracking” refers to linking data collected from your app about a particular end-user or device, such as a user ID, device ID, or profile, with Third-Party Data for targeted advertising or advertising measurement purposes, or sharing data collected from your app about a particular end-user or device with a data broker." "“Third-Party Data” refers to any data about a particular end-user or device collected from apps, websites, or offline properties not owned by you."
- It includes SDKs: "Placing a third-party SDK in your app that combines user data from your app with user data from other developers’ apps to target advertising or measure advertising efficiency, even if you don’t use the SDK for these purposes." Single sign-on providers too: "If the user will be subject to tracking as a result of SSO functionality included in your app, you must use the App Tracking Transparency prompt". Deep-linking tools that "create a shared identity of the user between applications from different companies for ad targeting" need it. Web views used for app functionality count.
- Not tracking: linking "solely on the end-user’s device"; data brokers used "solely for fraud detection or prevention or security purposes"; consumer reporting agencies for credit.
- The prompt: "you need to receive the user’s permission through the App Tracking Transparency (ATT) framework in order to track them or access their device’s advertising identifier"; without permission "the device’s advertising identifier value will be all zeros". The vendor ID: "The identifier for vendor (IDFV) may be used for analytics across apps from the same content provider. In this case, the use of the App Tracking Transparency framework is not required."
- No gating or rewards: "Can I gate functionality on agreeing to allow tracking, or incentivize users to agree ... ? No, per the App Review Guidelines: 5.1.2(i)." No other identifier instead: a hashed email or phone used to track still needs ATT permission.
- Fingerprinting: "you may not derive data from a device for the purpose of uniquely identifying it." Apps referencing SDKs that do "may be rejected from the App Store."
- Custom screens before the prompt (HIG Privacy, developer.apple.com/design/human-interface-guidelines/privacy, read 16 Nov 2026): rejected designs include "offering incentives, displaying a screen or window that looks like a request, displaying an image of the alert, and annotating the screen behind the alert"; a legal consent screen before or after ATT "to comply with local privacy laws is allowed".
- EU from iOS 27.2: an alternative ATT prompt with an "Additional Information" button; "only the alternative version of the system prompt is available for apps distributed in Germany, France, Italy, Poland, and Romania"; EU users can be asked again "one year after the user’s previous choice". Consent management screens are allowed, but "your app must always respect the user’s response to the App Tracking Transparency prompt, even if their response to other prompts conflicts."
- Manifest side: `NSPrivacyTracking` true needs `NSPrivacyTrackingDomains`, and those domains fail without permission (§1).

## 6. Consent, permissions and data use in the guidelines

From developer.apple.com/app-store/review/guidelines/ (read 16 Nov 2026):

- G 5.1.1(i), the policy must "Identify what data, if any, the app/service collects, how it collects that data, and all uses of that data", confirm third parties give "the same or equal protection", and "Explain its data retention/deletion policies and describe how a user can revoke consent and/or request deletion of the user’s data." Linked in App Store Connect "and within the app in an easily accessible manner."
- G 5.1.1(ii): "Apps that collect user or usage data must secure user consent for the collection, even if such data is considered to be anonymous at the time of or immediately following collection. Paid functionality must not be dependent on or require a user to grant access to this data." A way "to withdraw consent" must be easy. GDPR legitimate interest is allowed only with "all terms of that law."
- Purpose strings (developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings, read 16 Nov 2026): name "the specific feature or outcome"; "Write a separate purpose string for every protected resource"; "one brief, complete sentence in active voice and sentence case, ending with a period"; localized; an SDK's API references are yours to justify or remove.
- G 5.1.1(iii): "only collect and use data that is required to accomplish the relevant task"; prefer "the out-of-process picker or a share sheet". G 5.1.1(iv): "not attempt to manipulate, trick, or force people to consent"; offer alternatives when people decline.
- G 5.1.2(i): permission before using, transmitting or sharing personal data; "including with third-party AI"; ATT for tracking; no requirement to enable "push notifications, location services, tracking" to use the app or get rewards.
- G 5.1.2(ii)–(vi): no repurposing "without further consent"; no profiles built "surreptitiously"; no contact databases from Contacts or Photos, and no "information about which other apps are installed"; no marketing use of HealthKit, ClassKit, face or depth data.
- G 2.5.14: "explicit user consent" and "a clear visual and/or audible indication when recording".
- G 5.1.4: children's data under COPPA, GDPR and similar; apps "intended primarily for kids should not include third-party analytics or third-party advertising".

## 7. Third-party AI

- The rule: "You must clearly disclose where personal data will be shared with third parties, including with third-party AI, and obtain explicit permission before doing so." (G 5.1.2(i), read 16 Nov 2026)
- The policy must cover it: the AI provider is a third party that must give "the same or equal protection" (G 5.1.1(i)).
- AI content counts as user-generated content: "This includes social media, user-generated content platforms, and AI content creation apps", with filtering, reporting, blocking and published contact (G 1.2). Since 16 Oct 2026 that explicitly includes "nonconsensual intimate imagery — including imagery generated using AI tools" (developer.apple.com/news/?id=vvzx6cul, read 16 Nov 2026).
- AI companions and the age rating: the "Dating and Relationships" descriptor (from 16 Nov 2026) covers "a virtual companion that engages a user in sexual or romantic content", and such apps "receive a minimum age rating of 18+" (developer.apple.com/news/?id=yxkh08us, read 16 Nov 2026).
- App Review wants it named: list "External services and platforms ... (for example, data providers, authentication services, payment processors, or AI services)" in the review notes (developer.apple.com/help/app-review/before-submitting-for-review/complete-review, read 16 Nov 2026).
- Labels, a reading of Apple's definition (not Apple's words): text or voice sent to an AI provider is "collected" when you or the provider can access it "for a period longer than what is necessary to service the transmitted request in real time" (stored drafts, logs, a provider's retention for abuse checks). Declare it as Other User Content (and Audio Data for voice), App Functionality, and linked when it's tied to the account. Data sent and discarded at once is not collected.

## 8. Age assurance and children

From developer.apple.com/support/age-assurance/ and Apple developer news of February 24 and June 3, 2026 (read 16 Nov 2026):
- "developers are responsible for their own age restrictions. In certain regions, where legally required, Apple uses age assurance methods to confirm an Apple Account holder’s age and shares age categories with you through the Declared Age Range API. In those regions, you must check the age of the people using your app."
- Regions and dates: Texas SB 2420 for new Apple Accounts "starting June 4, 2026" (consent for "downloads, Apple In-App Purchases, and significant changes"); Utah "as of May 6, 2026"; Louisiana "as of July 1, 2026"; from February 24, 2026 Apple blocks 18+ downloads in Australia, Brazil and Singapore "unless they have been confirmed to be adults".
- Tools: Declared Age Range API (entitlement `com.apple.developer.declared-age-range`), PermissionKit's significant-change flow, "New age rating property type in StoreKit", and `RESCIND_CONSENT`: "When a parent or guardian revokes consent for their child to access an app, Apple will prevent the app from launching."
- "If my app is rated 18+, do I still need to implement the Declared Age Range API? Yes. In regions where legally required". "Are changes to my app’s terms or privacy policy considered significant app updates? It depends." Full support needs "the iOS 26.2 and iPadOS 26.2 SDKs, or later". App Review: "No, there are no changes to the App Review process."
- Testing: sandbox scenarios for age ranges, significant changes and consent revocation, "Starting in iOS 26.2 and iPadOS 26.2" (developer.apple.com/documentation/storekit/testing-age-assurance-in-sandbox, read 16 Nov 2026).
- A terms page with a minimum age above Apple's computed rating forces an override: "you must override to a rating that adheres to the requirements" (developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating, read 16 Nov 2026).

## 9. Deletion, from the privacy side

Account deletion rules are in `ungenerated-audit-app-review/references/apple-docs.md` §4. The privacy points: "Deleting an account removes the account from the developer's records, along with any data associated with the account that the developer isn't legally required to maintain"; "If you're legally required to retain some user information, let people know what information will and won't be retained"; deletion offered under CCPA or GDPR in some countries isn't enough: "Everyone should be able to delete their accounts, regardless of where they're located." (developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion, read 16 Nov 2026)
