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

Bounded-B bounds enforced here and in tests/smoke.mjs: <= ~100 words, attributed,
full provenance; NO lyrics / litigious estates / current commercial translations.
The full-poem / haiku exclusion applies to IN-COPYRIGHT works only: a 3-line poem
quoted whole is the factor-3 worst case, but that copyright rationale evaporates
for a genuinely PD haiku, which may ship whole. See docs/PASSAGES.md for the
provenance ledger.
"""

PASSAGES = {

# Homer / The Heroic Code — a TRUE pair on an OPEN question: Sarpedon affirms the
# code (mortal men charge precisely because death is unavoidable — win glory or
# yield it), then Achilles rejects it to the embassy (a life outweighs all the
# treasure of Troy; cattle can be raided back, a life cannot). Two rival passages,
# not one verdict. Both Butler 1898 PD, byte-matched to Project Gutenberg #2199.
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
  {
    "text": "My life is more to me than all the wealth of Ilius while it was yet "
            "at peace before the Achaeans went there, or than all the treasure "
            "that lies on the stone floor of Apollo\u2019s temple beneath the "
            "cliffs of Pytho. Cattle and sheep are to be had for harrying, and a "
            "man buy both tripods and horses if he wants them, but when his life "
            "has once left him it can neither be bought nor harried back again.",
    "author": "Homer",
    "work": "The Iliad",
    "translator": "Samuel Butler",
    "edition_year": "1898",
    "locator": "Book IX — Achilles to the embassy",
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

# Bashō / Yūgen — the crow on the withered branch: the eternal flashing in an
# ordinary autumn instant. A whole PD haiku (Aston's 1899 prose-history rendering,
# public domain) — the full-poem exclusion is a copyright rule whose factor-3
# rationale does not apply here. States no thesis; pure recognition, so it stands
# alone honestly. Byte-matched to two independent PD Aston scans.
"Yūgen": [
  {
    "text": "On a withered branch\nA crow is sitting\nThis autumn eve.",
    "author": "Matsuo Bashō",
    "work": "(hokku)",
    "translator": "W. G. Aston",
    "edition_year": "1899",
    "locator": "A History of Japanese Literature, p.295",
    "source": "Aston, A History of Japanese Literature (1899)",
    "source_url": "https://archive.org/details/historyjapanese00asto",
    "rights": "PD",
    "book_url": "https://archive.org/details/historyjapanese00asto",
  },
],

# Free will / The Readiness Potential — a live-rivals pair on an OPEN question.
# Libet reads the early brain signal as the act being initiated BEFORE we are aware
# of deciding (the famous threat to free will); Schurger's accumulator model rebuts
# it — the readiness potential is spontaneous noise crossing a threshold, so at that
# moment there is no decision yet to "precede" awareness. Two contending readings of
# the same data, not one verdict. Both in-copyright-fair-use prose (journal
# sentences), verbatim-verified against PubMed (Libet) and the open PNAS text
# (Schurger). Contested ⇒ the pair is required, never a lone passage.
"The Readiness Potential": [
  {
    "text": "It is concluded that cerebral initiation of a spontaneous, freely "
            "voluntary act can begin unconsciously, that is, before there is any "
            "(at least recallable) subjective awareness that a 'decision' to act "
            "has already been initiated cerebrally.",
    "author": "Benjamin Libet",
    "work": "Time of Conscious Intention to Act in Relation to Onset of Cerebral "
            "Activity (Readiness-Potential)",
    "translator": "",
    "edition_year": "1983",
    "locator": "Brain 106, pp. 623\u2013642 (conclusion)",
    "source": "Libet, Gleason, Wright & Pearl, Brain 106 (1983)",
    "source_url": "https://pubmed.ncbi.nlm.nih.gov/6640273/",
    "rights": "in-copyright-fair-use",
    "book_url": "",
  },
  {
    "text": "The reason we do not experience the urge to move as having happened "
            "earlier than about 200 ms before movement onset is simply because, at "
            "that time, the neural decision to move (crossing the decision "
            "threshold) has not yet been made.",
    "author": "Aaron Schurger",
    "work": "An accumulator model for spontaneous neural activity prior to "
            "self-initiated movement",
    "translator": "",
    "edition_year": "2012",
    "locator": "PNAS 109, pp. E2904\u2013E2913",
    "source": "Schurger, Sitt & Dehaene, PNAS 109 (2012)",
    "source_url": "https://www.pnas.org/doi/10.1073/pnas.1210467109",
    "rights": "in-copyright-fair-use",
    "book_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3479453/",
  },
],

# The self / The Ego Tunnel — a live-rivals pair on an OPEN question. Metzinger:
# the self is a transparent model the organism looks THROUGH and mistakes for
# reality (nobody ever had a self). Zahavi rebuts it — experience is always FOR a
# subject, comes with a first-personal point of view, so a minimal experiential
# self is built into consciousness, not an illusion. Both in-copyright-fair-use
# prose, verbatim-verified against full texts. Contested ⇒ the pair is required.
"The Ego Tunnel": [
  {
    "text": "The Ego is a transparent mental image: You \u2014 the physical person "
            "as a whole \u2014 look right through it. You do not see it. But you "
            "see with it.",
    "author": "Thomas Metzinger",
    "work": "The Ego Tunnel: The Science of the Mind and the Myth of the Self",
    "translator": "",
    "edition_year": "2009",
    "locator": "Introduction",
    "source": "Thomas Metzinger, The Ego Tunnel (Basic Books, 2009)",
    "source_url": "https://search.worldcat.org/isbn/9780465020690",
    "rights": "in-copyright-fair-use",
    "book_url": "",
  },
  {
    "text": "Rather, experiences are necessarily like something for a subject, they "
            "necessarily involve a point of view \u2013 they come with perspectival "
            "ownership.",
    "author": "Dan Zahavi",
    "work": "We and I",
    "translator": "",
    "edition_year": "2023",
    "locator": "The Philosopher (essay)",
    "source": "Dan Zahavi, 'We and I', The Philosopher",
    "source_url": "https://www.thephilosopher1923.org/post/we-and-i",
    "rights": "in-copyright-fair-use",
    "book_url": "https://www.thephilosopher1923.org/post/we-and-i",
  },
],

}

if __name__ == "__main__":
    n = sum(len(v) for v in PASSAGES.values())
    print(f"passages: concepts={len(PASSAGES)} passages(total)={n}")
