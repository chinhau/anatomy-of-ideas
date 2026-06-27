# -*- coding: utf-8 -*-
"""PROPOSAL ONLY — merge-ready entries for the "Plan A" heat-pilot.

NOT wired into the build. These 7 dicts are formatted to drop straight into the
PASSAGES dict in src/passages_mean.py once you sign off. Composition: 5
non-Western (hand-made, human-tier) + 2 Western, arranged so NO question debuts
Western-only (mind & abs each open with a non-Western voice first).

All 7 independently byte-matched (fresh fetch, HTML-aware) and <=100 words.
One editorial change: The Butterfly Dream period after "itself" is RESTORED to
Legge's 1891 print (the sacred-texts transcription drops it; Ivan Ilyich
precedent — record edition+locator when no clean public scan matches the exact
form).
"""

PROPOSAL = {

# real (handed-off) — DEBUT, non-Western. Laozi via Legge: the apophatic opening
# that says the deepest thing slips every instrument. Pure recognition, solo.
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

# mind (handed-off) — DEBUT, non-Western first. Zhuangzi's vertigo: which is the
# dream? States no contested thesis; pure recognition. Pairs (non-rival) with
# James below — two recognitions of a mind that will not hold still.
# Period after "enjoying itself" restored to Legge's print (see module docstring).
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

# peace (handed-off) — DEBUT, non-Western. The Dhammapada's bald equation: love is
# the root of grief and fear. Recognition, no rival owed; non-contested, solo.
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

# trans (live-rivals) — DEBUT, non-Western. Rumi's reed torn from the bed, wailing
# to return: pure ache, no contested thesis about HOW we transform. Solo is honest
# under recognition-vs-verdict (concept is non-contested, so machine rule clears).
"Mystical Union (Fana)": [
  {
    "text": "Hearken to the reed-flute, how it discourses When complaining of the "
            "pains of separation - Saying, \"Ever since I was parted from the "
            "reed-bed, My lament hath caused man and woman to moan. I want a bosom "
            "torn by severance, That I may unfold to such a one the pain of "
            "love-desire.\"",
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

# abs (open) — DEBUT, non-Western first. A TRUE rival pair on an open question:
# Tawhid AFFIRMS a transcendent, incomparable Absolute; Hume/Epicurus below PRESSES
# the ancient difficulty with such a deity. Two voices, not one verdict — plural,
# so the open question is never presented as settled.
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

# mind — second voice (Western). James: consciousness "is nothing jointed; it
# flows." Non-rival recognition beside Zhuangzi.
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

# abs — second voice (Western), the RIVAL to Tawhid. Hume puts Epicurus's
# unanswered trilemma: able? willing? whence then is evil? Pairs with Tawhid above
# so the open question stays plural.
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
    n = sum(len(v) for v in PROPOSAL.values())
    print(f"proposal: concepts={len(PROPOSAL)} passages(total)={n}")
