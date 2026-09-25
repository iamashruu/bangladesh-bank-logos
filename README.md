<div align="center">

# Bangladesh Bank Logos

**Vector logos for 63 banks operating in Bangladesh — collected, de-duplicated, and graded by quality.**

Every logo is shown at 40&nbsp;px next to the auto-traced and raster versions it replaces, so you can
see what you are getting before you ship it.

`50/52` directory banks have a true vector &nbsp;·&nbsp; `40/63` have a crisp
vector icon &nbsp;·&nbsp; `88/90` files are genuine vector art &nbsp;·&nbsp; `0` embedded rasters

**[→ Browse the gallery](https://iamashruu.github.io/bangladesh-bank-logos/)**

</div>

---

## Why this exists

Logo sets for Bangladeshi banks are easy to find and almost all bad. The three failure modes, in
increasing order of how well they hide:

1. **Raster scrapes.** A PNG or JPG lifted off the bank's website at whatever size it happened to be —
   anywhere from 30×32 to 2588×2588, often with a baked-in white box.
2. **Auto-traced favicons.** An SVG produced by running a bitmap tracer over a `favicon.ico`. It is a
   vector file, so it passes every "is this an SVG?" check, but the source was 16 or 32 pixels wide.
   The result is blobby at every size and the lettering is mush.
3. **SVGs with embedded rasters.** A `<svg>` wrapper around a base64 PNG. Scales exactly as badly as
   the PNG inside it.

This repo started as an audit of a remittance app's bank directory, where all three were in play at
once. Of a 124-file SVG pack already in production, **112 were tracer output** — 8 traced from a
48×48 source, 7 from a **16×16**, 3 from 32×32. Switching from the PNGs to "proper SVGs" would have
changed nothing visible.

So: the `original/` directory here holds only art that was drawn as vector, and the traced and raster
tiers are kept alongside it for comparison rather than thrown away.

## At a glance

| | |
| --- | --- |
| Banks covered | **52** in the main directory, **11** additional (foreign / central / cooperative) |
| True vector originals | **88** of 90 files |
| Banks with a crisp vector icon | **39** of 63 |
| SVGs containing embedded rasters | **0** |
| Auto-traced comparison set | 124 files (`icon/`, `full/`) |
| Raster comparison set | 29 files (`current-live/`) |
| Format | SVG throughout; comparison rasters are JPG / PNG / WebP |

## Quick start

The gallery is live at **[iamashruu.github.io/bangladesh-bank-logos](https://iamashruu.github.io/bangladesh-bank-logos/)** — nothing to install.

To work with the files locally:

```bash
git clone https://github.com/iamashruu/bangladesh-bank-logos.git
cd bangladesh-bank-logos
open index.html          # macOS — or just drag it into a browser
```

`index.html` is a browsable gallery of every bank. Search by name or short code, then **Copy SVG**,
**Copy data URI**, or **Download**.

Each card shows **every version held for that bank** as a row of thumbnails, so you can pick rather
than take what you are given. The one marked **★** is the best available — the highest-quality vector
we have. Click a thumbnail to swap the card's preview and retarget its copy and download buttons.

**62 of the 63 banks carry both an icon and a with-text version**, so you can take the square mark for
a 40&nbsp;px slot and the wordmark for a header. The *Show* filter narrows the whole grid to one or the
other. A caveat on the labels: they are derived from each file's aspect ratio, which is a reliable
guide to the **lockup shape** but not a promise about lettering — several square marks are circular
seals with the bank's name set inside them.

Logos always sit on a **white** tile by default, because that is what they were drawn for. Use the
backdrop toggle to check one against dark or a transparency grid before you ship it, and the theme
toggle for the page chrome itself. Press <kbd>/</kbd> to jump to search.

It is a single static page with no build step and no network calls, so it works opened straight from
disk and unchanged on GitHub Pages.

To use a logo in an application, take the file from `original/`:

```
original/dutch-bangla-bank-plc-1.svg
original/brac-bank-plc-1.svg
```

Banks with more than one original are numbered in best-match order — `-1` is the recommended pick.
The alternates are usually a Bengali-script lockup, an icon-only mark, or an older wordmark.

`manifest.json` carries the whole mapping if you want to generate a picker, a stylesheet, or a seed
script from it.

### Rendering at small sizes

These are wordmarks as often as they are icons, so aspect ratios vary widely. Use `object-fit:
contain` inside a square box rather than `cover`, which crops the overflow and lops the bottom off a
tall mark:

```css
.bank-logo { width: 40px; height: 40px; object-fit: contain; }
```

## Repository layout

| Path | Contents | Use it? |
| --- | --- | --- |
| `original/` | 75 genuine vector logos, `<bank-slug>-<n>.svg` | **Yes — this is the point of the repo** |
| `icon/` | 62 square marks from the auto-traced pack | Comparison only |
| `full/` | 62 wordmarks from the auto-traced pack | Comparison only |
| `current-live/` | 29 raster scrapes found in production | Comparison only |
| `unidentified/` | 2 real logos nobody has attributed yet | Help wanted |
| `index.html` | Browsable gallery — search, preview, copy, download | **Open it first** |
| `logos-data.js` | SVG source text the gallery's copy buttons read | Generated; no need to edit |
| `manifest.json` | Machine-readable bank → file mapping | For tooling |

## Coverage

**39 of 63 banks have a crisp vector icon.** 15 of those existed nowhere as a separate
file: they were **extracted from the bank's own vector wordmark**, by measuring where the symbol ends
and the lettering begins and cropping the SVG's `viewBox` to that box. That yields the real vector
artwork rather than a re-trace, so it stays sharp at any size. Every one was checked by eye before
being accepted — two more were produced and rejected, one that cropped empty and one that dragged a
rule out of the lockup with it.

A `◻︎` in the tables below means the form exists but only as a trace, and will look soft at 40&nbsp;px.

<details>
<summary><b>52 banks in the main directory</b> — 50 with a true vector original</summary>

| Bank | Short code | Vector | Files |
| --- | --- | :---: | --- |
| AB Bank PLC | `ABBL` | ✅ | `ab-bank-plc-1.svg` |
| Agrani Bank PLC | `AGRANI` | ✅ | `agrani-bank-plc-1.svg`, `agrani-bank-plc-2.svg`, `agrani-bank-plc-3.svg` |
| Al-Arafah Islami Bank PLC | `AIBL` | ✅ | `al-arafah-islami-bank-plc-1.svg` |
| Bangladesh Commerce Bank Limited | `BCBL` | ✅ | `bangladesh-commerce-bank-limited-1.svg` |
| Bangladesh Krishi Bank | `KRISHI` | ✅ | `bangladesh-krishi-bank-1.svg` |
| Bank Al-Falah Limited | `ALFALAH` | ✅ | `bank-al-falah-limited-1.svg` |
| Bank Asia PLC. | `BANKASIA` | ✅ | `bank-asia-plc-1.svg`, `bank-asia-plc-2.svg`, `bank-asia-plc-3.svg` |
| BASIC Bank Limited | `BASIC` | ✅ | `basic-bank-limited-1.svg` |
| Bengal Commercial Bank PLC. | `BGCB` | ✅ | `bengal-commercial-bank-plc-1.svg` |
| BRAC Bank PLC | `BRAC` | ✅ | `brac-bank-plc-1.svg` |
| Citizens Bank PLC | `CITIZENS` | ✅ | `citizens-bank-plc-1.svg` |
| City Bank PLC | `CITYBANK` | ✅ | `city-bank-plc-1.svg` |
| Community Bank Bangladesh PLC. | `COMMUNITY` | ✅ | `community-bank-bangladesh-plc-1.svg` |
| Dhaka Bank PLC | `DHAKA` | ✅ | `dhaka-bank-plc-1.svg` |
| Dutch-Bangla Bank PLC | `DBBL` | ✅ | `dutch-bangla-bank-plc-1.svg` |
| Eastern Bank PLC | `EBL` | ✅ | `eastern-bank-plc-1.svg`, `eastern-bank-plc-2.svg` |
| Export Import Bank of Bangladesh PLC | `EXIM` | ✅ | `export-import-bank-of-bangladesh-plc-1.svg` |
| First Security Islami Bank PLC | `FSIBL` | ✅ | `first-security-islami-bank-plc-1.svg` |
| Global Islami Bank PLC | `GIBL` | ✅ | `global-islami-bank-plc-1.svg` |
| ICB Islamic Bank Ltd. | `ICBI` | ✅ | `icb-islamic-bank-ltd-1.svg` |
| IFIC Bank PLC | `IFIC` | ✅ | `ific-bank-plc-1.svg` |
| Islami Bank Bangladesh PLC | `IBBL` | ✅ | `islami-bank-bangladesh-plc-1.svg` |
| Jamuna Bank PLC | `JAMUNA` | ✅ | `jamuna-bank-plc-1.svg` |
| Janata Bank PLC | `JANATA` | ✅ | `janata-bank-plc-1.svg` |
| Meghna Bank PLC | `MEGHNA` | ✅ | `meghna-bank-plc-1.svg`, `meghna-bank-plc-2.svg` |
| Mercantile Bank PLC | `MERCANTILE` | ✅ | `mercantile-bank-plc-1.svg` |
| Midland Bank Limited | `MIDLAND` | ✅ | `midland-bank-limited-1.svg` |
| Modhumoti Bank PLC | `MODHUMOTI` | ✅ | `modhumoti-bank-plc-1.svg`, `modhumoti-bank-plc-2.svg` |
| Mutual Trust Bank PLC | `MTB` | ✅ | `mutual-trust-bank-plc-1.svg` |
| National Bank Limited | `NBL` | ✅ | `national-bank-limited-1.svg`, `national-bank-limited-2.svg`, `national-bank-limited-3.svg` |
| National Credit & Commerce Bank PLC | `NCC` | ✅ | `national-credit-commerce-bank-plc-1.svg` |
| NRB Bank PLC | `NRBBANK` | ✅ | `nrb-bank-plc-1.svg` |
| NRBC Bank PLC | `NRBC` | ✅ | `nrbc-bank-plc-1.svg` |
| One Bank PLC | `ONEBANK` | ✅ | `one-bank-plc-1.svg`, `one-bank-plc-2.svg` |
| Padma Bank PLC | `PADMA` | ✅ | `padma-bank-plc-1.svg` |
| Prime Bank PLC | `PRIME` | ✅ | `prime-bank-plc-1.svg` |
| Probashi Kollyan Bank | `—` | ❌ | — |
| Pubali Bank PLC | `PUBALI` | ✅ | `pubali-bank-plc-1.svg`, `pubali-bank-plc-2.svg` |
| Rajshahi Krishi Unnayan Bank | `RAKUB` | ✅ | `rajshahi-krishi-unnayan-bank-1.svg` |
| Rupali Bank PLC | `RUPALI` | ✅ | `rupali-bank-plc-1.svg` |
| SBAC Bank PLC | `SBAC` | ✅ | `sbac-bank-plc-1.svg` |
| Shahjalal Islami Bank PLC | `SJIBL` | ✅ | `shahjalal-islami-bank-plc-1.svg` |
| Shimanto Bank PLC | `SHIMANTO` | ✅ | `shimanto-bank-plc-1.svg` |
| Social Islami Bank PLC | `SIBL` | ✅ | `social-islami-bank-plc-1.svg`, `social-islami-bank-plc-2.svg` |
| Sonali Bank PLC | `SONALI` | ✅ | `sonali-bank-plc-1.svg` |
| Southeast Bank PLC | `SOUTHEAST` | ✅ | `southeast-bank-plc-1.svg` |
| Standard Bank PLC | `STANDARD` | ❌ | — |
| Standard Chartered Bank | `SCB` | ✅ | `standard-chartered-bank-1.svg` |
| The Premier Bank PLC | `PREMIER` | ✅ | `the-premier-bank-plc-1.svg` |
| Trust Bank PLC | `TRUST` | ✅ | `trust-bank-plc-1.svg` |
| Union Bank PLC | `UNION` | ✅ | `union-bank-plc-1.svg` |
| United Commercial Bank PLC | `UCB` | ❌ | — |

</details>

<details>
<summary><b>11 additional banks</b> — foreign, central and cooperative</summary>

| Bank | Short code | Vector | Files |
| --- | --- | :---: | --- |
| Bangladesh Bank — BANGLADESH BANK | `BANGLADESH_BANK` | ✅ | `bangladesh-bank-bangladesh-bank-1.svg` |
| BDBL — BANGLADESH DEVELOPMENT BANK LTD. | `BDBL` | ✅ | `bdbl-bangladesh-development-bank-ltd-1.svg` |
| BSBL — BANGLADESH SAMABAYA BANK LTD. | `BSBL` | ✅ | `bsbl-bangladesh-samabaya-bank-ltd-1.svg` |
| Citibank — CITI BANK N A | `CITI` | ✅ | `citibank-citi-bank-n-a-1.svg` |
| ComBank — COMMERCIAL BANK OF CYLON | `COMBANK` | ✅ | `combank-commercial-bank-of-cylon-1.svg` |
| HBL — HABIB BANK LTD. | `HBL` | ✅ | `hbl-habib-bank-ltd-1.svg`, `hbl-habib-bank-ltd-2.svg`, `hbl-habib-bank-ltd-3.svg` |
| HSBC — HONGKONG & SHANGHAI BANKING CORP. | `HSBC` | ✅ | `hsbc-hongkong-shanghai-banking-corp-1.svg` |
| NBP — NATIONAL BANK OF PAKISTAN | `NBP` | ✅ | `nbp-national-bank-of-pakistan-1.svg` |
| SBI — STATE BANK OF INDIA | `SBI` | ✅ | `sbi-state-bank-of-india-1.svg`, `sbi-state-bank-of-india-2.svg` |
| Uttara Bank — UTTARA BANK LTD. | `UTTARA` | ✅ | `uttara-bank-uttara-bank-ltd-1.svg` |
| Woori Bank — WOORI BANK | `WOORI` | ✅ | `woori-bank-woori-bank-1.svg` |

</details>

## ⚠️ Provenance and licensing — read before publishing

**Bank logos are registered trademarks. This repository does not and cannot license them.** The files
are collected for identification and interoperability — so an application can show a customer which
bank they are sending money to. That is a narrow use, and it is not a grant of any right to you.

The artwork here came from at least three kinds of source, with incompatible terms:

| Source | Files (approx.) | Terms |
| --- | --- | --- |
| Wikimedia Commons | ~37 | Per-file. Many Bangladeshi bank logos there are tagged `PD-textlogo`; others are explicitly **non-free**. Must be checked individually. |
| seeklogo.com | ~18 | Their terms permit personal use and **restrict redistribution**. These are the most likely to need removing. |
| Bank websites / brand kits | ~20 | All rights reserved unless a published brand guide says otherwise. |

**Consequence:** this collection **cannot** ship under a blanket permissive licence. Before making it
public, a maintainer should:

- [ ] Record the exact source URL and licence for every file in `original/` (`manifest.json` currently
      stores only the source filename)
- [ ] Remove or replace the seeklogo-derived files
- [ ] Keep Commons files only where the file page carries a licence that permits redistribution
- [ ] Split licensing explicitly — e.g. the metadata, contact sheet and tooling under MIT or CC0, the
      artwork under a "trademarks of their respective owners" notice
- [ ] Add a contact route for takedown requests

There is deliberately no `LICENSE` file in this repository yet. Adding one before that audit is done
would be asserting a right nobody here holds.

## Known gaps — help wanted

**Two banks have no vector original:**

| Bank | Status |
| --- | --- |
| United Commercial Bank PLC | Auto-traced mark only. Not on Wikimedia Commons. |
| Probashi Kollyan Bank | **Nothing at all** — no vector, no traced mark, no raster, and no row in the source directory. |

**Nothing blurry is published.** A trace is only as good as the bitmap it came from: tracing a
3000&nbsp;px source gives clean curves, tracing a 16&times;16 favicon gives mush at every size. The build
reads each file's trace source — tracers record it as the SVG's own `width`/`height` — and **drops any
trace whose source was under 120&nbsp;px on its shortest edge**. That removed 18 files, including the
BASIC Bank wordmark traced from 314&times;57 and ten icons traced from favicons of 16&times;16 to 48&times;48.

21 traces remain, all from sources of 120&nbsp;px or more, and they are still marked `lower quality`
in the gallery. The threshold lives in `tools/build-data.py` as `MIN_TRACE_EDGE`.

The cost is that **18 banks now show only one of the two forms** rather than a soft stand-in for the
other — 14 have no icon, 4 no wordmark. Supplying real vector art for those is the most useful thing
anyone can contribute; see **Known gaps**.

### A wrong logo, found and fixed

`sibLogo.svg` was filed under **Social Islami Bank (SIBL)** and ranked as its recommended mark. It is
not SIBL's logo — it reads **"Standard Islami Bank PLC."**, which is **Standard Bank PLC** under its
renamed Islamic-banking identity. The filename matcher had taken it because `sib` is a prefix of
`sibl`. It is now filed under Standard Bank PLC, which closes that bank's gap, and SIBL shows its own
red-fan mark instead. Worth knowing if you pulled from an earlier copy of this set.

**Two files in `unidentified/` are real logos nobody has matched to a bank:**

- `jpl-logo-1.svg` — a purple (`#3a2e8d`) 894×150 wordmark
- `295285302_…-ezgif.com-jpg-to-svg-converter.svg` — a 3.7 MB tracer artefact off a Facebook image;
  almost certainly not worth keeping even once identified

**Two files in `original/` are tracer output**, kept because no drawn-vector source has turned up for
them yet — `rupali-bank-plc-1.svg` and `shahjalal-islami-bank-plc-1.svg`. They are far better than the
favicon traces described above (their sources were 3068×450 and 3600×900, not 16×16), but they are
still traces: the curves are polygonal up close. Both are flagged `traced ⚠` in the contact sheet, and
both are the highest-value replacements anyone could contribute.

**23 of the originals have no `viewBox`**, carrying only `width`/`height`. They render correctly
through `<img>`, which is how the contact sheet and most applications use them, but an inline `<svg>`
sized with CSS will show a clipped corner instead of scaling. The fix is mechanical — copy the
intrinsic size into a `viewBox="0 0 W H"` — and has not been applied yet:

```bash
for f in original/*.svg; do grep -qi viewBox "$f" || echo "$f"; done
```

## Contributing

Replacements are more valuable than additions. A better file for a bank that already has one is a
straight win.

**Where to look, in order of preference:**

1. The bank's own press kit, brand guidelines page, or investor-relations download
2. The SVG served by the bank's website (check the page source before assuming there is only a PNG)
3. Wikimedia Commons, if the file page carries a redistributable licence

**Every submission must pass these:**

- [ ] **Drawn as vector, not traced.** Tracer output announces itself in the file header:
      ```bash
      grep -li 'VTracer\|ezgif\|potrace' original/*.svg
      # two known hits today (see Known gaps); your file must not add a third
      ```
- [ ] **No embedded rasters:**
      ```bash
      grep -l 'data:image' original/*.svg                   # must return nothing
      ```
- [ ] **Legible at 40 px.** Open `index.html` and look at it next to the others. If the lettering
      closes up, it is a wordmark being asked to do an icon's job — submit the icon lockup instead.
- [ ] **Valid XML**, and carries a `viewBox` so it scales when inlined:
      ```bash
      python3 -c "import xml.etree.ElementTree as E,sys;[E.parse(f) for f in sys.argv[1:]]" original/*.svg
      grep -qi viewBox your-new-file.svg || echo 'add viewBox="0 0 W H"'
      ```
- [ ] **Named** `<bank-slug>-<n>.svg`, matching the slug already in `manifest.json`
- [ ] **Sourced** — state the URL you took it from and the licence on that page, in the PR description

**After adding or replacing a file**, add it to `manifest.json` and regenerate `logos-data.js`, which
is what the gallery's copy buttons read:

```bash
python3 tools/build-data.py
```

A manifest entry may pin `"form": "icon"` or `"form": "wordmark"`. Without one the form is inferred
from the artwork's aspect ratio, which is right for most files and wrong for a **stacked lockup** —
square, yet carrying the bank's name. Community Bank and Al-Arafah are both pinned for this reason.

**If you have the logo as EPS or AI**, it converts to real vector rather than a trace:

```bash
gs -dNOPAUSE -dBATCH -dSAFER -sDEVICE=pdfwrite -dEPSCrop -sOutputFile=logo.pdf logo.eps
pdftocairo -svg logo.pdf logo.svg        # an .ai file is already a PDF; skip the first step
```

Check the result before committing it: stock vector packs often wrap the mark in a coloured
background plate spanning the whole artboard, which has to be removed so the logo is transparent,
and the `viewBox` re-cropped to the artwork once it is gone.

**Also welcome:** identifying the two files in `unidentified/`, and any part of the licensing audit
above.

## Acknowledgements

Logos remain the property and trademarks of their respective banks. Comparison files were retained
only to document the quality problem this collection exists to fix.
