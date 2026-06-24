# Resonant passages — provenance ledger

The per-passage verification record required by **ADR 0006** (amended to "bounded
B"). Every passage shipped in `src/passages_mean.py` must have a row here pinning
its edition, translator, year, locator, rights tier, and verification. Reject any
passage whose provenance cannot all be pinned.

This is risk analysis, not legal advice.

## Bounded-B bounds (what may ship)

- **Prose only**, ≤ ~100 words, historically attributed, full provenance recorded.
- **Hard-excluded** (stay paraphrase-or-PD): song lyrics, full poems / **haiku**
  (a 3-line work quoted whole = the whole work), **litigious estates**, and
  **current commercial translations** still actively marketed.
- **No affiliate links** beside quoted text; the book pointer is a quiet,
  non-monetised link.
- **Takedown / opt-out:** rights-holders may request removal of any in-copyright
  passage; honour promptly. (Wire a contact route into the site before any
  in-copyright passage is publicised.)

## Authoring discipline (checked at curation, NOT by the smoke test)

- **No reader-directed second person.** The passage must not flatter the reader
  ("at times *you* feel…", Barnum). *Quoted intra-narrative dialogue is exempt* —
  Homer's Sarpedon says "nor bid *you* do so" to Glaucus, which is the author's
  verbatim text, not us addressing the reader. This is why the smoke test does
  **not** ban second person mechanically (it would false-positive on dialogue).
- **Anti-Barnum:** cut any passage that would comfort just anyone or makes no
  falsifiable claim. Specificity over comfort.
- **Recognition, not resolution:** never frame a passage as "the answer." Plural-
  or-none on contested concepts (enforced in code).

## Ledger

### The Heroic Code — Homer
- **Passage:** "My good friend, if, when we were once out of this fight… either win
  glory for ourselves, or yield it to another." (Sarpedon to Glaucus.)
- **Translator / edition:** Samuel Butler, prose translation, **1898**.
- **Locator:** *The Iliad*, Book XII.
- **Rights:** **PD** (US public domain; pre-1930 author *and* pre-1930 translation).
- **Source / scan:** Project Gutenberg #2199 — <https://www.gutenberg.org/ebooks/2199>;
  plain text <https://www.gutenberg.org/cache/epub/2199/pg2199.txt>.
- **Verification:** byte-matched against the Gutenberg #2199 plain text (the run of
  lines beginning "My good friend, if, when we were once out of this fight").
  66 words. Verified 2026-06-23.
- **Book pointer:** Gutenberg ebook page (free full text — a genuine "go read it"
  pointer, not a sales link).

### Ivan Ilyich's Mirror — Leo Tolstoy
- **Passage:** the Caius syllogism — "The syllogism he had learnt from Kiesewetter's
  Logic… but a creature quite, quite separate from all others."
- **Translator / edition:** Louise and Aylmer Maude, **1935** (World's Classics).
- **Locator:** *The Death of Ivan Ilyich*, ch. VI.
- **Rights:** **in-copyright-fair-use** (bounded B). ~69 words of prose excerpted
  from a full-length work, attributed, with no affiliate link. A clean **PD**
  alternative exists (N. H. Dole, 1899, archive.org `in.ernet.dli.2015.93640`) but
  its OCR is too garbled to byte-match; if a clean PD scan is later sourced, switch
  the rights tier to PD and byte-match it.
- **Source / edition pointer:** WorldCat record for the Maude edition —
  <https://www.worldcat.org/title/death-of-ivan-ilyich/oclc/2588832>.
- **Verification:** transcribed from the canonical Maude translation; locator and
  translator pinned. Verified 2026-06-23. (No byte-match against a public scan,
  because the cited edition is in copyright — recorded edition + locator instead.)
- **Book pointer:** none (no affiliate link beside in-copyright text); the work
  title in the colophon is the pointer.

## Deferred (authored-but-not-shipped)

### Yūgen — Matsuo Bashō — DEFERRED
The Phase-0 winner was the **frog haiku**, which falls in the **hard-excluded
"full poems / haiku" bucket** (a 3-line work quoted whole). A PD prose alternative
exists — W. G. Aston, *A History of Japanese Literature* (1899, archive.org
`historyjapanese00asto`), on the "suggestiveness" of Bashō's haikai — but it is
academic and faintly dismissive ("absurd to put forward any serious claim"), so it
does **not** carry the jolt that won Phase 0. Held back until either (a) the
haiku-exclusion bound is deliberately relaxed for genuinely **PD** haiku (whose
factor-3 copyright rationale does not apply), or (b) a stronger PD prose passage on
yūgen is found. Recorded so the gap is a decision, not an oversight.
