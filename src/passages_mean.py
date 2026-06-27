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
  text         verbatim passage; for rights == "PD" it is byte-verified PRESENT
               in source_url (the anti-fabrication test). May be print-corrected
               toward the cited edition where the only digital source carries a
               transcription/OCR defect, with the change logged in docs/PASSAGES.md.
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

# === Plan-A heat-pilot (added 2026-06-27) — 7 passages / 5 questions, non-Western-
# led, arranged so NO question debuts Western-only (mind & abs each open with a
# non-Western voice). All independently byte-verified; see docs/PASSAGES.md. ===

# real (handed-off) — Laozi via Legge: the apophatic opening; the deepest thing
# slips every instrument. Pure recognition, stands alone.
"The Dao": [
  {
    "text": "The Tao that can be trodden is not the enduring and unchanging Tao. "
            "The name that can be named is not the enduring and unchanging name.",
    "author": "Laozi",
    "work": "Tao Te Ching",
    "translator": "James Legge",
    "edition_year": "1891",
    "locator": "ch. 1",
    "source": "Project Gutenberg #216 (Legge; = Sacred Books of the East v39)",
    "source_url": "https://www.gutenberg.org/cache/epub/216/pg216.txt",
    "rights": "PD",
    "book_url": "https://www.gutenberg.org/ebooks/216",
  },
],

# mind (handed-off) — Zhuangzi's vertigo: which is the dream? Pure recognition,
# pairs (non-rival) with James below. PRINT-CORRECTED: the period after "itself"
# is restored to Legge's 1891 print (the sacred-texts transcription drops it); the
# full span is otherwise byte-verified present. See docs/PASSAGES.md.
"The Butterfly Dream": [
  {
    "text": "Formerly, I, Kwang K\u00e2u, dreamt that I was a butterfly, a butterfly "
            "flying about, feeling that it was enjoying itself. I did not know that "
            "it was K\u00e2u. Suddenly I awoke, and was myself again, the veritable "
            "K\u00e2u. I did not know whether it had formerly been K\u00e2u dreaming "
            "that he was a butterfly, or it was now a butterfly dreaming that it was "
            "K\u00e2u.",
    "author": "Zhuangzi",
    "work": "The Writings of Kwang-dze",
    "translator": "James Legge",
    "edition_year": "1891",
    "locator": "Bk II (The Adjustment of Controversies)",
    "source": "Legge, Sacred Books of the East v39 (transcription, print-corrected)",
    "source_url": "https://www.sacred-texts.com/tao/sbe39/sbe39123.htm",
    "rights": "PD",
    "book_url": "https://www.sacred-texts.com/tao/sbe39/index.htm",
  },
],

# peace (handed-off) — the Dhammapada's bald equation: love is the root of grief
# and fear. Recognition; non-contested, stands alone.
"Nirvana": [
  {
    "text": "From love comes grief, from love comes fear; he who is free from love "
            "knows neither grief nor fear.",
    "author": "The Dhammapada",
    "work": "The Dhammapada (Pali Canon)",
    "translator": "F. Max M\u00fcller",
    "edition_year": "1881",
    "locator": "ch. XVI, v. 215",
    "source": "Project Gutenberg #2017 (M\u00fcller; = Sacred Books of the East v10)",
    "source_url": "https://www.gutenberg.org/cache/epub/2017/pg2017.txt",
    "rights": "PD",
    "book_url": "https://www.gutenberg.org/ebooks/2017",
  },
],

# trans (live-rivals) — Rumi's reed torn from the bed, wailing to return: pure
# ache, no contested thesis about HOW we transform. Non-contested concept, so the
# machine rule clears and solo is honest under recognition-vs-verdict.
"Mystical Union (Fana)": [
  {
    "text": "Hearken to the reed-flute, how it discourses When complaining of the "
            "pains of separation - \" Ever since they tore me from my osier bed, "
            "My plaintive notes have moved men and women to tears. I burst my "
            "breast, striving to give vent to sighs, And to express the pangs of "
            "my yearning for my home.",
    "author": "Jalal al-Din Rumi",
    "work": "The Masnavi",
    "translator": "E. H. Whinfield",
    "edition_year": "1898",
    "locator": "Book I, proem (the Song of the Reed)",
    "source": "archive.org 'Masnavi i Ma'navi' (Whinfield, item masnaviimanavi)",
    "source_url": "https://archive.org/download/masnaviimanavi/Masnavi_i_Ma_navi_djvu.txt",
    "rights": "PD",
    "book_url": "https://archive.org/details/masnaviimanavi",
  },
],

# abs (open) — a TRUE rival pair: Tawhid AFFIRMS a single, incomparable Absolute;
# The Problem of Evil below PRESSES the theodicy difficulty with such a deity. Two
# voices keep the open question plural, never a verdict. (Partial rival — Epicurus
# attacks the attributes, not bare existence; a tighter counter is backlog.)
"Tawhid (Divine Unity)": [
  {
    "text": "SAY: He is God alone: God the eternal! He begetteth not, and He is not "
            "begotten; And there is none like unto Him.",
    "author": "The Qur'an",
    "work": "Surah al-Ikhlas (112), 'The Unity'",
    "translator": "J. M. Rodwell",
    "edition_year": "1861",
    "locator": "112:1\u20134",
    "source": "Project Gutenberg #2800 (Rodwell, The Koran)",
    "source_url": "https://www.gutenberg.org/cache/epub/2800/pg2800.txt",
    "rights": "PD",
    "book_url": "https://www.gutenberg.org/ebooks/2800",
  },
],

# mind — second voice (Western): James, "it is nothing jointed; it flows." A
# non-rival recognition beside Zhuangzi, so `mind` never debuts Western-only.
"Stream of Consciousness": [
  {
    "text": "Consciousness, then, does not appear to itself chopped up in bits. Such "
            "words as 'chain' or 'train' do not describe it fitly as it presents "
            "itself in the first instance. It is nothing jointed; it flows. A "
            "'river' or a 'stream' are the metaphors by which it is most naturally "
            "described.",
    "author": "William James",
    "work": "The Principles of Psychology",
    "translator": "",
    "edition_year": "1890",
    "locator": "Vol. I, ch. IX ('The Stream of Thought')",
    "source": "Project Gutenberg #57628 (Volume 1 of 2)",
    "source_url": "https://www.gutenberg.org/cache/epub/57628/pg57628.txt",
    "rights": "PD",
    "book_url": "https://www.gutenberg.org/ebooks/57628",
  },
],

# abs — second voice (Western), the RIVAL to Tawhid: Hume puts Epicurus's
# unanswered trilemma. Pairs with Tawhid so the open question stays plural.
"The Problem of Evil": [
  {
    "text": "EPICURUS's old questions are yet unanswered. Is he willing to prevent "
            "evil, but not able? then is he impotent. Is he able, but not willing? "
            "then is he malevolent. Is he both able and willing? whence then is "
            "evil?",
    "author": "David Hume",
    "work": "Dialogues Concerning Natural Religion",
    "translator": "",
    "edition_year": "1779",
    "locator": "Part X (Philo, restating Epicurus)",
    "source": "Project Gutenberg #4583",
    "source_url": "https://www.gutenberg.org/cache/epub/4583/pg4583.txt",
    "rights": "PD",
    "book_url": "https://www.gutenberg.org/ebooks/4583",
  },
],

}

if __name__ == "__main__":
    n = sum(len(v) for v in PASSAGES.values())
    print(f"passages: concepts={len(PASSAGES)} passages(total)={n}")
