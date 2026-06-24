#!/usr/bin/env python3
"""Build index.html (at the repo root) from src/.

Pipeline (deterministic, no network):
  1. expand17.py — applies rounds 1–17 (… + Cārvāka/Māori/Andean + metaethics + mind-body), writes src/ideas.json
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
CHECK = "--check" in sys.argv  # compare a fresh in-memory build to index.html; mutates nothing

def run(script):
    if not CHECK:
        print(f"  → {script}")
    subprocess.run([sys.executable, script], cwd=SRC, check=True,
                   stdout=(subprocess.DEVNULL if CHECK else None))

def build_html():
    if not CHECK: print("1/3  Building ideas dataset…")
    run("expand17.py")
    if not CHECK: print("2/3  Attaching readings + validating…")
    run("merge.py")
    if not CHECK: print("3/3  Injecting data + vendored assets into template…")
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
    return html

out = ROOT / "index.html"

if CHECK:
    # Build-in-sync guard: regenerate the artifact from src/ in memory and compare
    # to the committed index.html. Catches the "edited the template but forgot to
    # rebuild" drift (notably from concurrent sessions sharing the working tree).
    #
    # The expand/merge pipeline rewrites src/ideas.json as a side effect, so
    # snapshot and restore it — `--check` must leave the tracked tree untouched
    # (it runs in CI and on shared working trees, where a stray write is a bug).
    ideas_path = SRC / "ideas.json"
    snapshot = ideas_path.read_bytes() if ideas_path.exists() else None
    try:
        fresh = build_html()
    finally:
        if snapshot is not None:
            ideas_path.write_bytes(snapshot)
        elif ideas_path.exists():
            ideas_path.unlink()
    current = out.read_text(encoding="utf-8") if out.exists() else ""
    if fresh != current:
        n = min(len(fresh), len(current))
        at = next((i for i in range(n) if fresh[i] != current[i]), n)
        print(f"✗ index.html is STALE — it is not a fresh build of src/.")
        print(f"  first divergence at byte {at:,} (fresh {len(fresh):,} B vs on-disk {len(current):,} B).")
        print("  Run `python3 build.py` and commit the rebuilt index.html.")
        sys.exit(1)
    print("✓ index.html is in sync with src/.")
    sys.exit(0)

html = build_html()
out.write_text(html, encoding="utf-8")
print(f"✓ Wrote {out.relative_to(ROOT)}  ({len(html):,} bytes)")
print("  Deploy index.html to any static host, or run `npm test` to smoke-test it.")
