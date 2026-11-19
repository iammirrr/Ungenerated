# Launch dashboards, click by click

Every web dashboard step a subscription app needs before submitting, written so a **computer-use agent** (Claude
computer use, ChatGPT agent, Codex with a browser) can do it while the owner only signs in. App Privacy has its own skill:
`ungenerated-privacy-labels`.

Placeholders: `<APP_ID>` (App Store Connect's numeric Apple ID for the app), `<BUNDLE_ID>`, `<SERVICES_ID>` (the web
Sign in with Apple identifier), `<DOMAIN>`, `<SENDER_EMAIL>`, `<SUPABASE_REF>`, `<RC_PROJECT>`/`<RC_APP>` (RevenueCat ids
from its dashboard address). Never put real values in this file.

## Rules for the agent
- The owner signs in; the agent never types a password and never asks for one.
- **Never paste a key, token or secret into a web page, a chat with another service, or a file that gets committed.**
  Keys the dashboards create go straight to the owner's local secret store (`.env`, never committed) or to the person
  running the release, by hand.
- Stop and screenshot when a page doesn't match these steps; dashboards change.
- After each step, prove it from the API where one exists (commands below), not from the page alone. A page opened
  before an automatic change can show stale empty boxes.

## 1. App Store Server Notifications → RevenueCat
1. RevenueCat › project › Apps › the App Store app (`https://app.revenuecat.com/projects/<RC_PROJECT>/apps/<RC_APP>`) ›
   **Apple Server to Server notification settings**.
2. Press **Apply in App Store Connect** (needs RevenueCat's App Store Connect API key set). It fills both production and
   sandbox. Leave the forwarding URL empty if your server already gets RevenueCat's own webhook. Keep "Track new purchases
   from server-to-server notifications" ticked.
3. No button? Copy the notification URL shown there; App Store Connect › the app › App Information › App Store Server
   Notifications › Production Server URL › Set Up URL › paste › Save; the same for Sandbox (Version 2).
4. Prove it: `GET /v1/apps/<APP_ID>?fields[apps]=subscriptionStatusUrl,subscriptionStatusUrlVersion,subscriptionStatusUrlForSandbox`
   must show RevenueCat's URL and `V2` for both.

## 2. App Encryption Documentation
Nothing to upload when the app only uses Apple's own encryption (HTTPS, Keychain): set `ITSAppUsesNonExemptEncryption`
to `NO` in Info.plist and the question stops. Prove it: `GET /v1/builds/<BUILD>?fields[builds]=usesNonExemptEncryption`
→ `false`. Upload documentation only for your own or non-standard encryption.

## 3. App-Specific Shared Secret
Not needed when purchases are validated with an In-App Purchase key (StoreKit 2, RevenueCat's App Store Connect setup).
Only if a provider asks for it: App Information › App-Specific Shared Secret › Manage › Generate, and paste it into
that provider directly.

## 4. Sign in with Apple: private relay email
So people who chose "Hide My Email" receive your mail.
1. `https://developer.apple.com/account/resources/services/list` › **Sign in with Apple for Email Communication** ›
   Configure.
2. Email Sources › **+** › Domains and Subdomains: `<DOMAIN>` › Register. **+** › Email Addresses: `<SENDER_EMAIL>` ›
   Register.
3. Both rows must show a green **SPF** check. A failure means the domain's SPF record doesn't include the server that
   sends the mail (for example `include:_spf.<mail host>`); fix the DNS record, then re-check.
4. Every additional sending service (a newsletter tool) needs its own SPF include or DKIM before its mail reaches relay
   addresses.

## 5. Sign in with Apple: account notices from Apple
So the server hears when someone revokes the app or deletes their Apple account.
1. Certificates, Identifiers & Profiles › Identifiers › `<BUNDLE_ID>` › Sign In with Apple › Configure ›
   **Server-to-Server Notification Endpoint**: your endpoint (for example
   `https://<SUPABASE_REF>.supabase.co/functions/v1/apple-notices`) › Save. Repeat on `<SERVICES_ID>` if the web uses it.
2. The endpoint must verify Apple's signed token against `https://appleid.apple.com/auth/keys` and act on
   `consent-revoked` and `account-delete`.

## 6. App Store Connect: age rating and China
App Information › Age Rating › Edit. Answer every question, including the newer ones (shared location, dating). If the
app is not sold in China mainland, the two China questions (AI-generated content services, security assessment) are
**No**. Selling AI features in China needs an ICP filing, a CAC generative-AI registration and a China-approved model;
plan it as its own project.

## 7. App Review contact
Set it by API instead of the page: `POST /v1/appStoreReviewDetails` (or `PATCH` the existing one) with
`contactFirstName`, `contactLastName`, `contactPhone`, `contactEmail`, `demoAccountRequired`, linked to the version.

## 8. Google sign-in for a Supabase app
1. `https://console.cloud.google.com/projectcreate` › a project named after the app.
2. `https://console.cloud.google.com/auth/branding`: app name, support email, home page, privacy and terms URLs;
   Audience: External.
3. `https://console.cloud.google.com/auth/clients` › Create client › **Web application** › Authorised redirect URI
   exactly `https://<SUPABASE_REF>.supabase.co/auth/v1/callback` › Create.
4. The Client ID and Client secret go to the release owner by hand, then into Supabase › Authentication › Providers ›
   Google. Add Google to the privacy page in the same change. Apple's guideline 4.8 is already met when Sign in with
   Apple is offered beside it.

## 9. Keys the release needs
- **Sentry:** a personal token at `https://<ORG>.sentry.io/settings/account/api/auth-tokens/` with Project Read,
  Release Admin (symbol upload), Issue & Event Read (reports) and Event Admin (deleting a person's events). **Sentry shows
  a token once**: save it in the password manager at creation; nobody can read it from the page later.
- **PostHog:** a personal API key at `https://us.posthog.com/settings/user-api-keys` (or the EU host), read for reports,
  plus Person write if deletions must remove the person. One key covers every project in the account.
- **Anthropic:** a key created inside a workspace needs nothing else; a personal (user) key needs an
  `anthropic-workspace-id` header on every call. Test any new key with one tiny real call before it replaces the old one.

## Prompt to hand to a computer-use agent
> You are doing one dashboard step for the release of `<APP NAME>`. The owner is signed in. Follow
> `dashboards.md` section `<N>` exactly. Never type a password, never paste a key into a page, never press Submit or
> Release. If anything on screen differs from the steps, stop and take a screenshot. When done, take a screenshot that
> shows the result.
