# Passage drafter brief

The standing brief for any agent (or session) tasked with proposing resonant
passages. Embodies the validated "autonomy on the grind, human gate on the truth
claim" shape (ADR 0006; calibration n=20, 0 fabrications). Nothing here merges to
canon — drafts land in `staging/` and pass a human gate.

## Hard rules (never break)

1. **Scope of automation = PD only, English-original, non-contested concepts.**
   Translated works, scripture, and contested concepts are HUMAN-ONLY tier (locator
   / edition / rival choice is not mechanizable). The Plan-A non-Western passages
   were hand-made, not looped.
2. **Drafter ⊥ verifier.** The drafter must NOT write the verifier's cache or
   inputs (`_cache/`, validator). An agent once pre-seeded the cache and nearly
   defeated the "independent" check. Draft text + cite a `source_url`; let an
   isolated pass re-fetch and byte-match.
3. **No unsupervised loop, no per-concept target count.** Most concepts ship ZERO
   passages by design. There is no "done" to loop toward. Fill a queue on demand;
   do not run continuously.
4. **Output to `staging/` only.** Never touch `src/passages_mean.py`,
   `src/ideas.json`, or `docs/PASSAGES.md`.

## Selection: HEAT, not provenance

A passage earns its slot only if it **out-pulls the one-line gloss** in a blind read
(ADR 0006 Phase-0 test). Byte-match is hygiene, never value. Ask:
- Does the line make a stranger *flinch* before they can argue with it?
- Does it produce a felt recognition / vertigo a summary can't?
If it is merely correct-and-pretty but not stronger than a good gloss → **cut it.**

## Composition

- **Never debut a question Western-only.** A question's first passage must include a
  non-Western voice (sequencing-as-pedagogy). Automation can only produce
  English-original PD, so non-Western voices are hand-made.

## Recognition-vs-verdict & rival-fit (unsettled questions)

On an `open` / `live-rivals` / `dissolved` question:
- A passage that states **no contested thesis** (a phenomenological recognition) may
  stand alone.
- A passage that **argues a contested thesis** needs ≥2 genuine rivals or none.
- **Rival-fit test:** rival B must *deny or directly undercut A's exact
  proposition*, not merely share the topic. State A in one sentence; if B is only
  *adjacent*, it is not a pair → keep searching or both stay none.
  (Worked example: Tawhid affirms a transcendent Absolute; Epicurus attacks its
  *attributes*, not its bare existence — a PARTIAL rival, shipped to keep the
  question plural, with a tighter counter left as backlog.)

## Verification = anti-fabrication (not print-fidelity)

- Byte-match the drafted text against `source_url` after normalising **encoding**
  (HTML entities, curly quotes, dashes, whitespace, case). This proves the text
  exists in a real PD source — it is the fabrication filter.
- A mismatch is a **triage** signal: (1) encoding → fix the normaliser; (2) source
  transcription/OCR defect → correct toward the cited print + log it; (3) genuine
  fabrication/misquote → **reject**. Only (3) is a real failure; the system should
  fail SAFE (decline rather than match garbage).
- Record full provenance (author · work · translator/edition · year · locator ·
  source · rights). ≤ ~100 words. No Loeb/OCT/Teubner critical editions. No
  affiliate links.
