#!/usr/bin/env python3
"""Build index.html (at the repo root) from src/.

Pipeline (deterministic, no network):
  1. expand11.py — applies rounds 1–11 (… + the Golden Flower + the practice texts), writes src/ideas.json
  2. merge.py    — attaches ranked thinkers + readings, validates full coverage
  3. inject      — splices src/ideas.json + src/atlas_graph.json + the vendored D3/fonts
                   into src/template.html (escaping </ so embedded blobs can't close their
                   <script>/<style> tags) -> index.html at the repo root.

The root index.html IS the deployable (GitHub Pages serves the repo root). The
constellation data (src/atlas_graph.json) is a maintained data file. The one-time
migrations that grew it from 376 to 425 stars live in migrations/ and are idempotent;
you do NOT need to run them for a normal build.
"""
import subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SRC  = ROOT / "src"

def run(script):
    print(f"  → {script}")
    subprocess.run([sys.executable, script], cwd=SRC, check=True)

print("1/3  Building ideas dataset…")
run("expand11.py")
print("2/3  Attaching readings + validating…")
run("merge.py")

print("3/3  Injecting data + vendored assets into template…")
ideas = (SRC / "ideas.json").read_text(encoding="utf-8").replace("</", "<\\/")
atlas = (SRC / "atlas_graph.json").read_text(encoding="utf-8").replace("</", "<\\/")
i18n  = (SRC / "i18n.json").read_text(encoding="utf-8").replace("</", "<\\/")
d3js  = (SRC / "vendor" / "d3.min.js").read_text(encoding="utf-8").replace("</script", "<\\/script")
fonts = (SRC / "vendor" / "fonts.css").read_text(encoding="utf-8")
assert "</style" not in fonts.lower(), "fonts.css must not contain a closing style tag"
html  = (SRC / "template.html").read_text(encoding="utf-8")
html  = html.replace("__IDEAS_JSON__", ideas).replace("__ATLAS_JSON__", atlas).replace("__I18N_JSON__", i18n)
html  = html.replace("__FONTS_CSS__", fonts).replace("__D3_JS__", d3js)
assert not any(p in html for p in ("__IDEAS_JSON__", "__ATLAS_JSON__", "__I18N_JSON__", "__FONTS_CSS__", "__D3_JS__")), "placeholder not replaced"
out = ROOT / "index.html"
out.write_text(html, encoding="utf-8")
print(f"✓ Wrote {out.relative_to(ROOT)}  ({len(html):,} bytes)")
print("  Deploy index.html to any static host, or run `npm test` to smoke-test it.")
