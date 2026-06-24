# -*- coding: utf-8 -*-
"""Resonant passages (ADR 0006, amended to "bounded B").

One verbatim paragraph per concept where the prose *is* the datum — rendered
first in the drawer, above the gloss, to hand the reader the words that answer
the ache they already carry, then point them to the book.

This is a SMALL, GATED pilot, not a 293-row second forever-job. A concept gets a
passage only where one genuinely out-pulls its one-line note (Phase 0 blind test,
ADR 0006). Render only where a passage exists — never an empty slot.

Schema — keyed by concept id → list of passage dicts (a list so the
plural-or-none rule for contested concepts can be honoured later):
  text         verbatim passage (byte-matched to source_url when rights == "PD")
  author       original author
  work         the work it is drawn from
  translator   translator / editor (or "" for an original-language author)
  edition_year year of the cited edition/translation
  locator      where in the work (book/chapter/section)
  source       human-readable provenance
  source_url   scan URL — REQUIRED for rights == "PD"; edition pointer otherwise
  rights       "PD" | "in-copyright-fair-use"
  book_url     optional quiet, NON-affiliate pointer to read the whole thing

Bounded-B bounds enforced here and in tests/smoke.mjs: prose only, <= ~100 words,
attributed, full provenance; NO lyrics / full poems / haiku / litigious estates /
current commercial translations. See docs/PASSAGES.md for the provenance ledger.
"""

PASSAGES = {

# Homer / The Heroic Code — Sarpedon to Glaucus on why mortal men still charge.
# Butler's 1898 prose is public domain; byte-matched to Project Gutenberg #2199.
"The Heroic Code": [
  {
    "text": "My good friend, if, when we were once out of this fight, we could "
            "escape old age and death thenceforward and forever, I should neither "
            "press forward myself nor bid you do so, but death in ten thousand "
            "shapes hangs ever over our heads, and no man can elude him; therefore "
            "let us go forward and either win glory for ourselves, or yield it to "
            "another.",
    "author": "Homer",
    "work": "The Iliad",
    "translator": "Samuel Butler",
    "edition_year": "1898",
    "locator": "Book XII — Sarpedon to Glaucus",
    "source": "Project Gutenberg #2199 (Butler prose translation)",
    "source_url": "https://www.gutenberg.org/cache/epub/2199/pg2199.txt",
    "rights": "PD",
    "book_url": "https://www.gutenberg.org/ebooks/2199",
  },
],

# Tolstoy / Ivan Ilyich's Mirror — the Caius syllogism: death in the abstract is
# correct; death of *this* irreplaceable self is unthinkable. Maude translation is
# in-copyright; quoted as bounded-B fair-use prose (~68 words), no affiliate link.
"Ivan Ilyich's Mirror": [
  {
    "text": "The syllogism he had learnt from Kiesewetter's Logic — 'Caius is a "
            "man, men are mortal, therefore Caius is mortal' — had always seemed "
            "to him correct as applied to Caius, but certainly not as applied to "
            "himself. That Caius — man in the abstract — was mortal, was perfectly "
            "correct; but he was not Caius, not an abstract man, but a creature "
            "quite, quite separate from all others.",
    "author": "Leo Tolstoy",
    "work": "The Death of Ivan Ilyich",
    "translator": "Louise and Aylmer Maude",
    "edition_year": "1935",
    "locator": "ch. VI",
    "source": "Trans. Louise & Aylmer Maude (World's Classics)",
    "source_url": "https://www.worldcat.org/title/death-of-ivan-ilyich/oclc/2588832",
    "rights": "in-copyright-fair-use",
    "book_url": "",
  },
],

}

if __name__ == "__main__":
    n = sum(len(v) for v in PASSAGES.values())
    print(f"passages: concepts={len(PASSAGES)} passages(total)={n}")
