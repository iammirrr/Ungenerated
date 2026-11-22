# Banners: Apple's creative assets and the rest

Claude makes the banners (they're layout, type and the real app, which Claude can build and render exactly). The icons
inside them come from `ungenerated-icons`. The owner: "BANNER SHOULD BE MADE BY CLAUDE ICON SHOULD BE WRITTEN DRAFTS TO
CODEX"; "BANNER IS LOOK NEW APPSTORE STUFF".

Check the current [creative asset specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications/), [Apple's preview templates](https://developer.apple.com/app-store/asset-best-practices/), and [App Store Connect instructions](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-your-app-store-assets/#manage-creative-assets).

## What Apple's creative assets are

- Header and Search Results are optional creative assets on **iOS and iPadOS 27 and later**. Each slot holds one
  asset and appears under **App Store Connect › app version › Product Page Information**.
- Upload to each slot directly or use **Browse Assets** to choose from Asset Library. Asset Library also supports
  standalone review. Custom Product Pages can have their own creative assets.

## The sizes

| App Store Connect slot | Final image | Art safe area (x, y from top left) |
|---|---|---|
| **Header** | 3840 × 1646 PNG | 1646 × 661 at (1097, 493) |
| **Search Results** | 3840 × 2560 PNG (1920 × 1280 minimum; JPEG also accepted) | 2168 × 1030 at (836, 765) on the 3840 × 2560 canvas |
| **Universal asset** | 5244 × 2950 PNG shared by both slots | 1402 × 962 at (1921, 660) |
| **In-app event card** | 1920 × 1080 up to 3840 × 2160 | See Apple's event template |
| **In-app event details** | 1080 × 1920 up to 2160 × 3840 | See Apple's event template |

Dedicated Header and Search Results videos can run 5–30 s at 30 or 60 fps. Header starts muted and can be unmuted;
Search Results stays muted. Event videos run 15–30 s.

- **The header** is for a first-time visitor: what the app is, in one picture.
- **The search result** states the app's purpose at a glance and shows the real interface. Without it, the app's
  events, preview and screenshots show there instead, so it competes with your own first screenshots.

## Apple's rules

- No alpha channel.
- The focal point centred inside the template's safe area (download Apple's templates and check against them).
- One short phrase that adds to the picture, or none. Not a paragraph, not the app name repeated.
- No prices, discounts, URLs or ©.
- No other platforms' logos, and no Apple awards.
- Content suitable for 4+.
- Localised per language, like the screenshots.
- Videos: work with the sound off, loop seamlessly, have a strong poster frame, and no fast cuts.

## How to build them

1. **Same system as the screenshots.** The screenshots' headline type, pill and grounds, and the app's real screens
   or real UI pieces (`references/screenshots.md`). A banner that looks like a different brand from the screenshots
   breaks the page.
2. **One idea per banner.** Usually the app's core moment, big, in the centre: the feature the first screenshot sells.
   No props, no stickers, no collage.
3. **HTML on the board, rendered to exact pixels.** One page per banner at half size, captured at 2x with the board's
   capture tool (`ungenerated-flows` template, `tools/capture.mjs`):

   ```
   W=1920 H=823  DSF=2 node tools/capture.mjs "http://localhost:4173/banners/header.html" out/header 1500   # 3840 × 1646
   W=1920 H=1280 DSF=2 node tools/capture.mjs "http://localhost:4173/banners/search.html" out/search 1500   # 3840 × 2560
   W=2622 H=1475 DSF=2 node tools/capture.mjs "http://localhost:4173/banners/universal.html" out/universal 1500   # 5244 × 2950
   ```

   Then remove the alpha channel: a browser's PNG often carries one even when every pixel is opaque.

   ```
   python3 -c "import sys; from PIL import Image; [Image.open(p).convert('RGB').save(p) for p in sys.argv[1:]]" out/*.png
   ```

4. **The header and search videos are cut from the trailer's scenes** (`references/trailer.md`): the same Remotion
   project, a new composition at 21:9 or 3:2, one movement made to loop (its last frame is its first). No new
   footage, no fast cuts. Check the loop point frame by frame, and pick the poster frame on purpose.
5. **Check the final exports.** Open both encoded PNGs and preview the art-safe-area crops using the coordinates
   above. Confirm the headline and main subject survive each crop and are readable at storefront size. Verify
   dimensions and RGB encoding with no alpha channel.
6. **Deliver both files.** Follow the repo's existing asset paths, or use `store/creative-assets/<locale>/header.png`
   and `store/creative-assets/<locale>/search-results.png`. For each requested locale, give the path to each PNG and
   name its matching slot. For a full listing, track Header and Search Results as separate deliverables alongside
   screenshots and the app preview.
7. **Check the listing in App Store Connect.** Under the app version's Product Page Information, use **Header** and
   **Search Results** to place the corresponding images for that locale. Use **Preview** to inspect iPhone and iPad
   crops and orientations and save the assignments when uploading is in scope.

## Every language, in one run

A listing isn't finished with the header and search picture in one language: every localization the screenshots
ship in gets both. The owner, seeing only English filled: "I WANT YOU TO AT LEAST COMPLETE THE LISTING FOR ALL".

- **Reuse the screenshots' translated headlines.** Take each banner's phrase from the screenshot headlines that are
  already translated (the same keys, the same boxed word), so every language exists the moment the banner does. The
  app's own UI inside the phone stays in the languages the app actually ships.
- **A long translation wraps, it doesn't shrink.** Fit each line on one line first; if that leaves the type under
  about 80% of the English size, let it wrap onto a third line at full size and shrink only until it fits the room.
  Never break a word, never let the boxed word split, and keep right-to-left languages right-to-left.
- **Check the safe-area crop of every language on one sheet** before uploading: crop each PNG to the safe area and
  tile them; that is what an iPhone shows.

## Uploading through the App Store Connect API

The Asset Library and its placements are in the public API, so every language goes up in one run instead of a
drag-and-drop per language:

1. `POST /v1/appAssetLibraryImages` with `category: "CREATIVE_ASSETS"`, `fileName`, `fileSize` and the relationship
   `assetLibrary` (its id is the app's id). PUT the bytes to each returned `uploadOperations` entry, then
   `PATCH` the image with `uploaded: true`. Unlike screenshots it takes no `sourceFileChecksum` (the API refuses it).
2. `POST /v1/appAssetLibraryPlacements` with `placementType` `PRODUCT_PAGE_HEADER_ASSET` or
   `APP_STORE_SEARCH_RESULTS_ASSET` and two relationships: `appStoreVersionLocalization` and `image`. Placing can
   fail while Apple is still processing the picture: retry for a minute.
3. **A slot holds one.** List the localization's placements (`GET /v1/appStoreVersionLocalizations/{id}/placements`,
   with `include=image` to see each one's image) and `DELETE /v1/appAssetLibraryPlacements/{id}` the old one first.
4. **One image can sit in several localizations**: upload the English picture once and place it in every English
   localization.
5. **Then clean the library:** delete every `CREATIVE_ASSETS` image no slot uses, and any image still
   `AWAITING_UPLOAD` from a failed run, so nothing stray waits for review.
6. **Verify with a read, never by running the uploader again.** Count each localization's placements with a GET: a
   second run "to count" re-uploads and replaces every slot, and if it stops halfway a language is left empty.

## The rest of the artwork a launch needs

| Asset | Size | Notes |
|---|---|---|
| Website hero | the site's own | the header banner's picture, recomposed for the page |
| Open Graph image | 1200 × 630 | what a shared link shows; one phrase, the real app, the icon |
| Google Play feature graphic | 1024 × 500 | only when there's an Android app; no device frames required |

Thumbnails and header art: the brand's own background, uncluttered, the subject and logo big, and checked in both
square and vertical crops if it'll be reused in social.
