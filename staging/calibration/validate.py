# -*- coding: utf-8 -*-
"""Standalone validator for a single staged passage candidate.

Ports the per-passage predicates from tests/smoke.mjs (lines ~277-291) plus an
INDEPENDENT byte-match (the agent's self-report is NOT trusted): the candidate
text must appear, after light normalisation, in the locally cached source bytes.

Usage:
    python3 staging/calibration/validate.py            # validate all candidates
Reads:  staging/calibration/candidates/*.json
Caches: staging/calibration/_cache/<sha>.txt  (fetched source bodies)
Writes: staging/calibration/decision_log.json + prints a summary table.
"""
import json, re, glob, os, hashlib, urllib.request, sys, html

ROOT = os.path.dirname(__file__)
CAND = os.path.join(ROOT, "candidates")
CACHE = os.path.join(ROOT, "_cache")
os.makedirs(CACHE, exist_ok=True)

RIGHTS = {"PD", "in-copyright-fair-use"}
VERDICT = re.compile(r"\b(prove[sn]?|proven|encapsulat|the answer|solved|refute[sd]?)\b", re.I)
CRIT = re.compile(r"\b(Loeb|Oxford Classical Text|Teubner|OCT)\b", re.I)
REQ = ["text", "author", "work", "edition_year", "locator", "source", "rights"]


def norm(s):
    # Unescape HTML entities first: HTML-served PD sources serve e.g. "k&acirc;u",
    # which otherwise throws a FALSE byte-mismatch (encoding noise, not fabrication).
    s = html.unescape(s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\u2012", "-")
    s = s.replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def fetch(url):
    h = hashlib.sha1(url.encode()).hexdigest()[:16]
    p = os.path.join(CACHE, h + ".txt")
    if os.path.exists(p):
        return open(p, encoding="utf-8", errors="replace").read()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 calibration-bytematch"})
    body = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
    open(p, "w", encoding="utf-8").write(body)
    return body


def check(c):
    reasons = []
    for f in REQ:
        if not (isinstance(c.get(f), str) and c[f].strip()):
            reasons.append(f"missing:{f}")
    if c.get("rights") not in RIGHTS:
        reasons.append("bad-rights")
    if c.get("rights") == "PD" and not (c.get("source_url") or "").strip():
        reasons.append("PD-without-source_url")
    wc = len((c.get("text") or "").split())
    if wc > 100:
        reasons.append(f"over-100-words:{wc}")
    if CRIT.search(" ".join([c.get("work", ""), c.get("source", ""), c.get("translator", "")])):
        reasons.append("critical-edition")
    if not c.get("settled") and VERDICT.search(c.get("text", "")):
        reasons.append("verdict-word-on-unsettled")
    # INDEPENDENT byte-match
    bm = None
    if c.get("rights") == "PD" and (c.get("source_url") or "").strip():
        try:
            body = fetch(c["source_url"])
            bm = norm(c["text"]) in norm(body)
            if not bm:
                reasons.append("BYTE-MISMATCH")
        except Exception as e:
            bm = None
            reasons.append(f"fetch-failed:{type(e).__name__}")
    return {"id": c.get("id"), "word_count": wc, "byte_match": bm,
            "agent_byte_match": c.get("byte_match"), "verdict": "accept" if not reasons else "reject",
            "reasons": reasons, "source_url": c.get("source_url"), "locator": c.get("locator")}


def main():
    files = sorted(glob.glob(os.path.join(CAND, "*.json")))
    log = []
    for fp in files:
        cand = json.load(open(fp, encoding="utf-8"))
        for c in (cand if isinstance(cand, list) else [cand]):
            log.append(check(c))
    json.dump(log, open(os.path.join(ROOT, "decision_log.json"), "w"), ensure_ascii=False, indent=2)
    acc = sum(1 for r in log if r["verdict"] == "accept")
    print(f"candidates={len(log)} accept={acc} reject={len(log)-acc}")
    for r in log:
        flag = ""
        if r["agent_byte_match"] is True and r["byte_match"] is False:
            flag = "  <-- AGENT CLAIMED MATCH, INDEPENDENT CHECK FAILED"
        print(f"  [{r['verdict']:6}] {r['id']:32} bm={str(r['byte_match']):5} wc={r['word_count']:3} {','.join(r['reasons'])}{flag}")


if __name__ == "__main__":
    main()
