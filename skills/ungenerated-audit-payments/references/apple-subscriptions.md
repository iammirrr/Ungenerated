# Apple subscriptions: what Apple's documents say

How auto-renewable subscriptions work on the App Store, what the store does on its own, and the rules the purchase screens and the server must follow, in Apple's exact words (short quotes) with the page and the date read. **Every page was read on 16 Nov 2026**; Apple's Developer Program License Agreement was version LYL262, dated October 29, 2026. Re-read before relying on a number. The App Review side of the same rules (what the screens must show, review notes) is in `ungenerated-audit-app-review/references/apple-docs.md` §2–3 and that skill's checklist §2.

Short names used below:
- **Subs page**: developer.apple.com/app-store/subscriptions/
- **Schedule 2**: developer.apple.com/support/terms/apple-developer-program-license-agreement/ (Schedule 2)
- **HIG IAP**: developer.apple.com/design/human-interface-guidelines/in-app-purchase
- **ASC Help**: developer.apple.com/help/app-store-connect/manage-subscriptions/ (page named in each line)
- **Notifications**: developer.apple.com/documentation/appstoreservernotifications/notificationtype

## 1. What the screens must disclose

| Element | Apple's words | Source (read 16 Nov 2026) |
|---|---|---|
| Title | "Title of auto-renewing subscription, which may be the same as the in-app product name" | Schedule 2 §3.8(b) |
| Length | "Length of subscription" | Schedule 2 §3.8(b) |
| Price | "Price of subscription, and price per unit if appropriate" | Schedule 2 §3.8(b) |
| Links in the app | "Links to Your Privacy Policy and Terms of Use must be accessible within Your Licensed Application." | Schedule 2 §3.8(b) |
| Links in the metadata | "your app and App Store metadata must include links to your Terms of Use and Privacy Policy." | Subs page |
| What they get | "Subscription name and duration, and the content or services provided during the subscription period" | Subs page |
| Renewal price | "Full renewal price, shown clearly and prominently, and localized in available currencies" | Subs page |
| Restore | "A way for current subscribers to sign in or restore purchases" | Subs page |
| Biggest number | "the amount that will be billed must be the most prominent pricing element in the layout" | Subs page |
| Free trial | "clearly indicate how long the free trial lasts and the price billed once the free trial is over" | Subs page |
| Trial converts | "make sure people know that when the free trial is over, a payment will be automatically initiated for the next subscription period." | HIG IAP |
| Intro price | "list the introductory price, the duration of the offer, and the standard price the customer pays after the offer ends." | HIG IAP |
| Every purchase | "Display the total billing price for each in-app purchase you offer, regardless of type." | HIG IAP |
| The law | "You must do so in compliance with all legal and regulatory requirements." | Schedule 2 §3.10 |

- Schedule 2 §3.8(b) in this version lists only title, length, price and the links. The longer list older templates paste (charged at confirmation, renews unless turned off 24 hours before, managed in account settings, unused trial forfeited) is not in it. Auto-renewal wording by the button still comes from the HIG line above and from auto-renewal laws (owned by `ungenerated-audit-privacy`).
- Schedule 2 §3.8(c): "You must fulfill the offer during the entire subscription period, as marketed, including any Billing Grace Period You authorize"; otherwise Apple may refund "the full amount, or any portion thereof".
- HIG IAP: "Use the default confirmation sheet. ... Don’t modify or replicate this sheet." "Display your store only when people can make payments." "Encourage a new subscription only when someone isn’t already a subscriber."
- Fetch before showing: "Fetch product information using StoreKit APIs before presenting In-App Purchases in your app's UI to ensure the displayed details match your configuration in App Store Connect." (developer.apple.com/help/app-review/before-submitting-for-review/configure-in-app-purchases, read 16 Nov 2026)

## 2. Products, groups, prices, proceeds

- Durations: "Possible durations are 1 week, 1 month, 2 months, 3 months, 6 months, and 1 year." "You can have up to 100 subscriptions per group. Users can subscribe to one subscription product per group at a time." (ASC Help, offer-auto-renewable-subscriptions, read 16 Nov 2026). Schedule 2 §3.8(a): "weekly, monthly, bi-monthly, tri-monthly, semi-annual or annual". G 3.1.2(a): at least seven days.
- One group: "creating a single group is the best practice for most apps as it prevents people from accidentally purchasing multiple subscriptions." Levels: "Arrange your subscriptions in order from the one that offers the most (level 1) to the one that offers the least." (Subs page, read 16 Nov 2026)
- Changing plans (Subs page, read 16 Nov 2026): upgrade: "They’re immediately upgraded and receive a refund of the prorated amount of their original subscription." Downgrade: "The subscription continues until the next renewal date, then is renewed at the lower level and price." Crossgrade: same duration "begins immediately"; different durations take effect "at the next renewal date". Notifications: `DID_CHANGE_RENEWAL_PREF` with `UPGRADE` or `DOWNGRADE`.
- New payment option: "monthly subscriptions with a 12-month commitment" (Subs page, read 16 Nov 2026); Billing Grace Period "doesn't apply" to them and offer limits apply per configuration (ASC Help).
- Multiseat: "Multiseat purchasing is enabled by default in App Store Connect, unless you’ve previously adjusted this setting." Only apps without StoreKit 2, or subscriptions with Family Sharing on, start opted out (ASC Help, manage-purchase-options-for-auto-renewable-subscriptions, read 16 Nov 2026). Apple, 16 Sep 2026: "Starting today, multiseat purchases are enabled by default for subscriptions in App Store Connect"; "Volume Purchasing launches on October 22, 2026, and Group Purchases will launch this winter" (developer.apple.com/news/?id=likeohx4, read 16 Nov 2026). Schedule 2 §3.8(c) now covers refunds of Group Purchases. If it stays on, members arrive by `SUBSCRIBED` and leave by `REVOKE`, seat refunds by `REFUND` with subtype `SEATS` (Notifications). Decide before the first release.
- Also new for iOS 27, by request: "Bundles and Suites", several subscriptions or apps sold as one In-App Purchase, "available later this year in iOS 27" (same post).
- Family Sharing: shares "with up to five family members"; "You can enable Family Sharing for your subscription in App Store Connect. Please note that this can’t be undone." Read `ownershipType` to tell the purchaser from family members (Subs page, read 16 Nov 2026). Leaving the family or a refund sends `REVOKE` (Notifications).
- Prices (Subs page, read 16 Nov 2026): "800 price points ... with an additional 100 higher price points available upon request"; "you can schedule one future price change at a time, per territory". Decreases: "existing subscriptions will automatically renew at the lower price. You don’t have the option to preserve the higher price for existing subscribers." Increases: "Some price increases require subscribers to opt in"; "If they don’t agree, their subscription expires at the end of their current billing cycle"; "You can keep an unlimited number of active subscribers at their existing price". Schedule 2 §3.9: without consent "the auto-renewal feature will be disabled". `PRICE_INCREASE` notifies `PENDING` or `ACCEPTED`; `EXPIRED` with `PRICE_INCREASE` when declined.
- Proceeds (Subs page, read 16 Nov 2026): "During a subscriber’s first year of service, you receive 70% of the subscription price at each billing cycle, minus applicable taxes. After a subscriber accumulates one year of paid service, your net revenue increases to 85%". Small Business Program members "receive 85% ... regardless". "Free trials and renewal extensions are excluded from days of paid service." "If the subscription is renewed within 60 days, the days of paid service resume from the recovery date."
- Server notifications URL: an optional App Information field, "Only visible for apps that offer In-App Purchases" (developer.apple.com/help/app-store-connect/reference/app-information/required-localizable-and-editable-properties, read 16 Nov 2026). "Use the App Store Server API and enable App Store Server Notifications to get real-time changes to the status of your subscriptions." (Subs page)

## 3. Offers

Kinds (Subs page, read 16 Nov 2026): "You can create introductory offers, offer codes, promotional offers, and win-back offers." Discount types: "Free trial", "Pay as you go", "Pay up front". "At the end of the offer period, the subscription auto-renews at the standard price unless a subscriber cancels it."

### Introductory offers
ASC Help, set-up-introductory-offers-for-auto-renewable-subscriptions (read 16 Nov 2026):
- "An introductory offer is a limited-time discounted price or free trial for the initial period of a subscription." It "automatically appears on your app’s product page on the App Store for eligible users."
- Eligibility: "each person is only eligible to redeem one introductory offer per subscription group." "New and returning customers are only eligible to use one introductory offer per subscription group. For example, if a customer uses a free trial and then upgrades to a subscription product in the same group that also has a free trial, they aren't eligible for the second offer."
- "When displaying offers in your app, use receipt validation to ensure that you’re only showing offers to people who can redeem them."
- Free trial lengths: "3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year." Pay as you go: in multiples of the subscription period up to 12 months (weekly: "1 to 12 Weeks"). Pay up front: "1, 2, 3, or 6 Months. 1 Year."
- "You can have one current and one future introductory offer per storefront." Overlapping dates: "the latest action overwrites existing introductory offers." "Once you create an introductory offer, you won’t be able to edit it."
- StoreKit: `isEligibleForIntroOffer` is true "if the customer is eligible for an introductory offer on this auto-renewable subscription, or any auto-renewable subscription in the same subscription group"; it "may be `true` even if you haven’t set up an introductory offer in App Store Connect" (developer.apple.com/documentation/storekit/product/subscriptioninfo/iseligibleforintrooffer, read 16 Nov 2026). So check both eligibility and `subscription.introductoryOffer != nil` before trial copy. Server-decided eligibility: `introductoryOfferEligibility(compactJWS:)`.

### Promotional offers
ASC Help, set-up-promotional-offers-for-auto-renewable-subscriptions (read 16 Nov 2026):
- For "existing and previously subscribed customers"; "Customers can accept the offer even if they've already accepted an introductory offer."
- "You can have up to 10 active offers per subscription." "Promotional offers apply to all storefronts where your subscription is available — you can't limit an offer to specific countries or regions." "Once you create a promotional offer, only the price can be edited."
- Signed: "To get started, generate keys for In-App Purchases" (the In-App Purchase key; StoreKit takes a `Product.SubscriptionOffer.Signature`). Your app decides who sees them: "You decide the business logic for promotional offers" (Subs page).

### Win-back offers
ASC Help, set-up-win-back-offers, and developer.apple.com/documentation/storekit/supporting-win-back-offers-in-your-app (read 16 Nov 2026):
- "Your subscription needs to be approved by App Review before you can create a win-back offer." Not available for a first submission.
- Per product: "Win-back offers are configured per subscription product, not per subscription group. Customers are only eligible for win-back offers for their most recently lapsed subscription product within each group".
- Limits: "a maximum of 350 win-back offers per subscription"; "a maximum of 5 win-back offers per storefront, per subscription at a time"; "The earliest you can schedule your offer to go live is one day after today, and the event must run for a minimum of 3 days."
- Eligibility: Minimum Paid Duration "any value between 1 and 24 months, or 3, 4, and 5 years"; Time Since Last Subscribed "a minimum value of 1 month and a maximum value of 24 months" (both required); Wait Between Offers "between 2 and 24 months" (optional). Overlaps: "Apple automatically selects and displays one offer".
- Shown without code: "Win-back offers are automatically displayed to eligible customers in their Manage Subscription page on iOS 14.3, iPadOS 14.3, and macOS 14 or later, and within your app on the win-back offer sheet on iOS 18, iPadOS 18, and macOS 15 or later." StoreKit "displays a win-back offer sheet when it receives a winBackOffer message".
- Streamlined Purchasing is on by default: the redemption completes outside the app and arrives in `Transaction.updates`, so iterate it "as soon as your app launches". Turning it off needs an approved binary using `PurchaseIntent` ("your lastest approved app binary must use the PurchaseIntent API").
- Direct link `https://apps.apple.com/win-back/<win-back offer Apple ID>`: check `eligibleWinBackOfferIds` from Get All Subscription Statuses first; "Send the direct link to eligible customers only." Server side, "An offerType of `4` indicates a win-back offer."
- Promotion on the App Store needs an approved subscription image; "You may not upload an image that is the same as your app icon, or any of your app screenshots"; a promoted win-back offer "will replace any In-App Purchase promotions in the same storefront."

### Offer codes
ASC Help, set-up-subscription-offer-codes; Subs page; HIG IAP (read 16 Nov 2026):
- Two kinds: "one-time-use codes (18-digit unique codes), or custom codes (such as SPRINGPROMO)". "You can create codes for a maximum of 1 million redemptions per app, per quarter." One-time codes "Expire after a maximum of six months from the date they’re created"; custom codes need no expiry but can have a limit. "Customers are limited to redeeming one code per offer."
- Eligibility you choose: "New subscribers", "Existing subscribers" (including billing retry or grace "as long as auto-renew remains enabled"), "Expired subscribers". "Existing subscribers can only redeem codes that are an upgrade from or at the same level as their current subscription."
- With an intro offer: "Yes" redeems the intro first then the code's offer; "No" redeems the code, then the standard price, keeping intro eligibility. A no-auto-renew option exists: "Checking the box will prevent auto-renewal ... you’ll only be able to choose Free offers".
- Redemption: a URL, the App Store (custom codes can't be typed in account settings), or in the app with `offerCodeRedemption(isPresented:onCompletion:)` / `presentOfferCodeRedeemSheet`. "In order for offer codes to be redeemed, your app must be available on the App Store." Custom codes: "only alphanumeric ASCII characters".
- Schedule 2 §3.13: "You shall not sell the Offer Codes or accept any form of payment"; every instrument that hands codes out carries "(i) The code expiration date or while supplies last; (ii) The Territory in which the codes can be redeemed; (iii) Apple Account is required, subject to prior acceptance of license and usage terms; (iv) Codes are not for resale, and have no cash value; (v) Full terms apply; see https://www.apple.com/legal/internet-services/itunes/ww; and (vi) Offer and content are provided by You."

### South Korea: a second consent after a trial or discount
"additional consent must be obtained for your trial or offer after the initial transaction"; it "must be obtained from customers within 30 days from the payment or conversion date" for "Free to paid trials" and "Discounted subscription offers to standard-price subscriptions". "The App Store will help to get consent by informing the affected subscribers with an email, push notification, and in-app price consent sheet" (developer.apple.com/news/?id=bo1b122z, since 14 Feb 2025, read 16 Nov 2026). So the app must not suppress the in-app price consent message (`Message.Reason.priceIncreaseConsent`) for good. The post doesn't say what happens when someone doesn't agree; read the renewal state from the server, never assume.

### Apple's own save step at cancellation
- Available since 4 Nov 2026: "Retention messages appear in the cancellation flow and can include text, images, or a special offer"; App Store Connect sets "subscriber eligibility and the wait time between offers" (developer.apple.com/news/?id=fk9ps3gv, read 16 Nov 2026).
- App Store Connect retention messages: "When a subscriber initiates a cancellation, a retention message can highlight key features, announce upcoming content, or present a promotional offer"; "You can create up to 10 retention messages per app"; "A subscription can have only one retention message assigned to it at a time"; body text: "do not reference specific offers or prices"; "Ensure your message includes localizations for all storefronts" (ASC Help, configure-retention-messages, read 16 Nov 2026).
- Retention Messaging API (pre-release, request access): Apple calls your server "when an active subscriber views a subscription details page with a Cancel button"; the message shows "after they tap Cancel Subscription"; "Don’t upload content that is misleading or inaccurate"; production needs a passed performance test; visible on "iOS 15.1 or later" (developer.apple.com/documentation/retentionmessaging, read 16 Nov 2026).
- Renewal date extensions for outages: "twice per calendar year, each up to 90 days in the future"; extended days don't count toward the 85% year (Subs page).

## 4. Managing, cancelling, refunds

- In-app management: `AppStore.showManageSubscriptions(in:)` (or `in:subscriptionGroupID:`) and SwiftUI `manageSubscriptionsSheet(isPresented:)` show "the customer’s currently active subscription for your app and the options to view, upgrade, downgrade, or cancel their subscription". Mac apps need Mac Catalyst or macOS 27.3; for iPhone apps on a Mac, "if isiOSAppOnMac is `true,` avoid showing the user interface for this feature." (developer.apple.com/documentation/storekit/appstore/showmanagesubscriptions(in:), read 16 Nov 2026). Web fallback: https://apps.apple.com/account/subscriptions/.
- Around it: "you might show a promotional offer", "provide an offer to help win them back", "present a survey", but "always make it easy for people to access the system-provided management UI where they can cancel if they wish." (Subs page). HIG IAP: "Always make it easy for customers to cancel an auto-renewable subscription."
- What a cancel looks like on the server: `DID_CHANGE_RENEWAL_STATUS` / `AUTO_RENEW_DISABLED`, access continues to the end of the period, then `EXPIRED` / `VOLUNTARY`. Re-enabling: `AUTO_RENEW_ENABLED` ("Customer subscribes again after canceling a subscription, which reenables auto-renew") (Notifications).
- Refunds in the app: `Transaction.beginRefundRequest(in:)` / `refundRequestSheet(for:isPresented:onDismiss:)`; "The App Store takes up to 48 hours to either approve or deny a refund." Not for multiseat subscriptions (developer.apple.com/documentation/storekit/transaction/beginrefundrequest(in:), read 16 Nov 2026). The system then turns auto-renew off: "The system turned off auto-renew because the customer initiated a refund through your app using the refund request API." Web fallback: https://support.apple.com/118223.
- Refund outcomes (Notifications): `REFUND` with `revocationDate` and `revocationReason`; `REFUND_DECLINED`; `REFUND_REVERSED`: "If your app revoked content or services as a result of the related refund, it needs to reinstate them." `CONSUMPTION_REQUEST`: a refund request "for a consumable In-App Purchase or auto-renewable subscription"; answer with consumption data only "If the customer provided consent".
- HIG IAP on refund help: "Make it easy for people to request a refund"; "Avoid characterizing or providing guidance on Apple’s refund policies."
- Schedule 2 §6.3: Apple may refund within "ninety (90) days of the date of download" or the subscription period if shorter, and you reimburse Apple.
- Account deletion with a running subscription: "notify them that billing will continue through Apple and ask them to cancel"; scheduled deletion only with an immediate option (developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion, read 16 Nov 2026).

## 5. Failed payments: grace period and billing retry

- Retry: "When a subscription renewal fails, Apple attempts to recover it for 60 days." (Subs page). `DID_FAIL_TO_RENEW`: "If the `subtype` is `GRACE_PERIOD`, continue to provide service through the grace period. If the `subtype` is empty, the subscription isn’t in a grace period and you can stop providing the subscription service." Then `GRACE_PERIOD_EXPIRED`, `DID_RENEW` / `BILLING_RECOVERY` on recovery, or `EXPIRED` / `BILLING_RETRY` (Notifications).
- Billing Grace Period (ASC Help, enable-billing-grace-period-for-auto-renewable-subscriptions, read 16 Nov 2026): set per app, "Configurability isn’t available for individual subscription products"; "select a period of 3, 16, or 28 days"; "If your app offers weekly subscriptions, even if you select a 16 or 28 day grace period, the actual grace period will only be 6 days"; it "doesn't apply for monthly subscriptions with a 12 month commitment"; turn it on in sandbox first. Scope: "all renewals (existing paid renewals and free offers transitioning to paid renewals) or only to existing paid renewals" (Subs page). Apple's overview page still says "either 6 or 16 days, depending on the subscription duration"; the dedicated page above is the current one.
- The store asks for the card itself: "Starting in iOS 16.4 and iPadOS 16.4, if a subscription doesn’t successfully renew, a system-provided sheet appears in your app upon launch"; you can "delay or suppress this sheet in StoreKit using messages" (`Message.Reason.billingIssue`).
- Schedule 2 §3.8(c): you must deliver "including any Billing Grace Period You authorize".
- Status in one call: "The Get All Subscription Statuses endpoint lets you determine in one simple check whether a subscription is active, expired, in billing retry, or in grace period." (Subs page)

## 6. Server notifications (version 2)

From Notifications (read 16 Nov 2026); each type in Apple's words, shortened:

| Type | Meaning |
|---|---|
| `SUBSCRIBED` | "the customer subscribed"; `INITIAL_BUY` or `RESUBSCRIBE` (also Family Sharing and group members) |
| `DID_RENEW` | renewed; `BILLING_RECOVERY` after a failure |
| `DID_CHANGE_RENEWAL_STATUS` | `AUTO_RENEW_ENABLED` / `AUTO_RENEW_DISABLED` (also after an in-app refund request) |
| `DID_CHANGE_RENEWAL_PREF` | `UPGRADE`, `DOWNGRADE`, empty (downgrade undone), `INCREASE_QUANTITY` / `DECREASE_QUANTITY` (seats) |
| `DID_FAIL_TO_RENEW` | billing retry; `GRACE_PERIOD` subtype keeps service |
| `GRACE_PERIOD_EXPIRED` | "you can turn off access" |
| `EXPIRED` | `VOLUNTARY`, `BILLING_RETRY`, `PRICE_INCREASE`, `PRODUCT_NOT_FOR_SALE` |
| `OFFER_REDEEMED` | an active subscriber redeemed an offer; `UPGRADE` / `DOWNGRADE` |
| `PRICE_INCREASE` | `PENDING` / `ACCEPTED` |
| `REFUND`, `REFUND_DECLINED`, `REFUND_REVERSED` | refund granted, declined, reversed after a dispute |
| `REVOKE` | access through Family Sharing or a group "is no longer available" |
| `CONSUMPTION_REQUEST` | Apple asks for consumption data on a refund request |
| `RENEWAL_EXTENDED`, `RENEWAL_EXTENSION` | renewal date extensions |
| `RESCIND_CONSENT` | "the parent or guardian has withdrawn consent for a child’s app usage" |
| `UNCLAIM_SEATS` | seats unclaimed (developer-hosted invitations) |
| `ONE_TIME_CHARGE` | non-subscription purchases and their offer codes |
| `TEST` | sent only when you call Request a Test Notification |
| `EXTERNAL_PURCHASE_TOKEN`, `METADATA_UPDATE`, `MIGRATION`, `PRICE_CHANGE` | external purchase and Advanced Commerce API only |

## 7. Testing

From developer.apple.com/documentation/storekit/testing-at-all-stages-of-development-with-xcode-and-the-sandbox, …/testing-in-app-purchases-with-sandbox, …/testing-an-auto-renewable-subscription and TN3186 (all read 16 Nov 2026):

- Three environments: StoreKit Testing in Xcode (no App Store Connect setup; transactions "signed by Xcode"; forced errors), the sandbox (real App Store Connect data, App Store-signed transactions, server notifications), TestFlight ("uses the sandbox"). "None of the test environments charge users when they test buying a product. The App Store doesn’t send emails for purchases or refunds made in the test environments."
- Renewals: "In the sandbox environment, subscription renewals happen at an accelerated rate, and auto-renewable subscriptions renew up to 12 times after the initial purchase." The rate is set per Sandbox Apple Account in App Store Connect.
- Resetting: clearing a sandbox account's purchase history makes it "eligible for introductory offers" again; the storefront can only be changed in App Store Connect; interrupted purchases, Family Sharing, win-back sheet display and age assurance scenarios are sandbox settings.
- TestFlight: "Apps that you download from TestFlight always run in the sandbox environment." To use sandbox controls there, sign out of Media & Purchases; "Consider using a dedicated testing device".
- Products not loading: bundle ID mismatch, In-App Purchase capability off, wildcard App ID, invalid signing, inactive membership, no Paid Apps Agreement in effect, incomplete banking or tax; App Store Connect edits "can take up to 1 hour" to reach the sandbox (TN3186).
- App Review uses the same sandbox: "App Review evaluates your In-App Purchases in the same sandbox environment you use for testing", and "Paid In-App Purchases won't function in review until this agreement is active." (developer.apple.com/help/app-review/before-submitting-for-review/configure-in-app-purchases, read 16 Nov 2026)

## 8. The first submission, payments side

1. Paid Apps Agreement, bank and tax all Active (App Store Connect › Business).
2. Each subscription: Display Name, Description, price in every storefront, **App Review Screenshot**; the group's display name; levels ranked.
3. The app version, the subscription group and every subscription in one draft submission: "The first ... auto-renewable subscription ... must be submitted with a new app version." (developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-purchase, read 16 Nov 2026)
4. No win-back offers yet (they need an approved subscription); introductory and promotional offers can go with it; promotional offers need the In-App Purchase key in the billing service.
5. Billing Grace Period length, Family Sharing (one-way) and multiseat decided in App Store Connect.
6. The server notification URL set (production and sandbox) and the server verifying signed payloads.
7. A demo account with an expired subscription for App Review: "provide a demo account with an expired subscription to enable review of the entire purchase flow." (developer.apple.com/help/app-review/before-submitting-for-review/complete-review, read 16 Nov 2026)
