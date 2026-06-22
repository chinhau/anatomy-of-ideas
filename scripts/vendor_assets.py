#!/usr/bin/env python3
"""One-time vendoring of third-party assets so the built page makes ZERO
external network calls (privacy / GDPR: no Google-Fonts IP leak; supply chain:
no single-CDN dependency on D3).

Outputs (committed, become the source of truth — build.py inlines them):
  src/vendor/d3.min.js     — D3 v7.8.5, fetched from cdnjs
  src/vendor/fonts.css     — @font-face rules with woff2 embedded as base64 data: URIs

Only the `latin` and `latin-ext` subsets are kept (latin-ext carries the
diacritics in terms like Śūnyatā / Ātman / Anattā). Cyrillic / Greek / Vietnamese
subsets are dropped to keep the payload small.

Re-run only to refresh the pinned assets. NOT part of the normal build (the build
is offline and deterministic).
"""
import base64, pathlib, re, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
VENDOR = ROOT / "src" / "vendor"; VENDOR.mkdir(parents=True, exist_ok=True)

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
D3_URL = "https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"
FONTS_URL = ("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:"
             "ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@300;400;500;600"
             "&display=swap")
KEEP_SUBSETS = {"latin", "latin-ext"}


def fetch(url, ua=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA} if ua else {})
    with urllib.request.urlopen(req) as r:
        return r.read()


def vendor_d3():
    data = fetch(D3_URL)
    (VENDOR / "d3.min.js").write_bytes(data)
    print(f"  d3.min.js          {len(data):>9,} bytes")


def vendor_fonts():
    css = fetch(FONTS_URL, ua=True).decode("utf-8")
    # blocks look like:  /* latin */\n@font-face {\n ... }\n
    blocks = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
    out, kept, total = [], 0, 0
    for subset, block in blocks:
        if subset not in KEEP_SUBSETS:
            continue
        m = re.search(r"url\((https://[^)]+\.woff2)\)", block)
        if not m:
            continue
        woff2 = fetch(m.group(1))
        total += len(woff2)
        b64 = base64.b64encode(woff2).decode("ascii")
        data_uri = f"url(data:font/woff2;base64,{b64}) format('woff2')"
        block = re.sub(r"url\(https://[^)]+\.woff2\)\s*format\('woff2'\)",
                       data_uri, block)
        out.append(f"/* {subset} */\n{block}")
        kept += 1
    (VENDOR / "fonts.css").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"  fonts.css          {kept} faces, {total:,} bytes of woff2 inlined")


if __name__ == "__main__":
    print("Vendoring third-party assets (one-time)…")
    vendor_d3()
    vendor_fonts()
    print("✓ Wrote src/vendor/d3.min.js + src/vendor/fonts.css")
