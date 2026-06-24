# Resonant passages — provenance ledger

The per-passage verification record required by **ADR 0006** (amended to "bounded
B"). Every passage shipped in `src/passages_mean.py` must have a row here pinning
its edition, translator, year, locator, rights tier, and verification. Reject any
passage whose provenance cannot all be pinned.

This is risk analysis, not legal advice.

## Bounded-B bounds (what may ship)

- **Prose only**, ≤ ~100 words, historically attributed, full provenance recorded.
- **Hard-excluded** (stay paraphrase-or-PD): song lyrics, **in-copyright** full
  poems / **haiku** (a 3-line work quoted whole = the whole work — factor 3),
  **litigious estates**, and **current commercial translations** still actively
  marketed. *The full-poem/haiku exclusion is a copyright rule:* its factor-3
  rationale only bites on in-copyright works, so a genuinely **PD** haiku (in a PD
  translation) may ship whole — there is no market to harm and no exclusive right to
  infringe. (Amended 2026-06-23 to ship Bashō.)
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
- **Plural-or-none, refined to recognition-vs-verdict** (ADR 0006, 2026-06-24).
  On an unsettled (`open` / `live-rivals` / `dissolved`) concept, a passage that
  *argues a contested thesis* needs **≥2 rival passages or none**; a passage that
  states **no** contested thesis — a phenomenological observation / recognition —
  may stand alone. The authoring test: *would a reasonable rival passage contradict
  this one?* Yes → pair or cut; only-deepens → solo is honest. (The machine half
  enforces just `contested ⇒ ≥2 or none`; "argues a thesis" is not mechanizable.)
  Worked example: Homer's Sarpedon argues glory redeems a short life → paired with
  Achilles' rejection. Tolstoy's Caius syllogism claims nothing about life's worth
  → stands alone.

## Ledger

### The Heroic Code — Homer (a TRUE 2-rival pair on an `open` question)
This concept ships **two rival passages** — the code affirmed, then rejected —
because a single one argued a verdict on an open question (see the recognition-vs-
verdict rule above). Both Samuel Butler prose, **1898**, **PD**, from Project
Gutenberg #2199 (<https://www.gutenberg.org/ebooks/2199>; plain text
<https://www.gutenberg.org/cache/epub/2199/pg2199.txt>).
- **Passage 1 (affirms):** "My good friend, if, when we were once out of this
  fight… either win glory for ourselves, or yield it to another." *Locator:* Book
  XII, Sarpedon to Glaucus. 66 words. Byte-matched 2026-06-23.
- **Passage 2 (rejects):** "My life is more to me than all the wealth of Ilius…
  but when his life has once left him it can neither be bought nor harried back
  again." *Locator:* Book IX, Achilles to the embassy. 80 words. Byte-matched
  2026-06-24 against the Gutenberg #2199 plain text (and confirmed against the live
  gutenberg.org cache that "and a man buy both tripods" is Butler's archaic
  phrasing, not an OCR artifact).
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

### Yūgen — Matsuo Bashō (a SOLO PD haiku — pure recognition, no thesis)
Ships **whole** because it is genuinely **PD**: the full-poem/haiku exclusion is a
copyright rule whose factor-3 "quoting the entire work" rationale evaporates once
there is no copyright to infringe (bound relaxed 2026-06-23). Stands **alone** under
the recognition-vs-verdict rule — a haiku states no contested thesis, so no rival is
owed; Yūgen is also non-contested, so the machine rule (`contested ⇒ ≥2 or none`) is
satisfied.
- **Passage:** "On a withered branch / A crow is sitting / This autumn eve."
- **Translator / edition:** W. G. Aston, *A History of Japanese Literature*, **1899**,
  p.295. **PD.**
- **Source:** archive.org `historyjapanese00asto`
  (<https://archive.org/details/historyjapanese00asto>).
- **Verification:** byte-matched 2026-06-23 against **two** independent PD Aston
  scans (`historyjapanese00asto` and `AHistoryOfJapaneseLiterature`); both confirm
  the three lines verbatim, OCR noise only at the decorative quotation marks. The
  rendering chosen over the frog haiku — the crow on the withered branch carries the
  yūgen jolt the academic prose alternative lacked.
- **Book pointer:** archive.org scan (free full text — a genuine "go read it"
  pointer, not a sales link).

## Deferred (authored-but-not-shipped)

_(none)_
