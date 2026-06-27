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

## Verification policy (amended 2026-06-27)

- **Byte-match is the anti-fabrication test, not a print-fidelity guarantee.** A PD
  passage must be byte-verified **present** in `source_url` after normalising
  *encoding* (HTML entities, curly quotes, dashes, whitespace, case). It proves the
  text exists in a real PD source; it does not, by itself, prove the text matches
  the author's print.
- **A byte-mismatch is a triage signal, not an auto-reject.** Classify it: (1)
  encoding → fix the normaliser; (2) transcription/OCR defect in the source →
  **correct toward the cited print edition** and log "transcription-verified,
  print-corrected: \<what changed\>"; (3) genuine fabrication/misquote → **reject**.
  Only (3) is a real failure. The print-correction path is the PD analogue of the
  in-copyright edition+locator record (see Ivan Ilyich below).
- **Rival-fit (authoring).** A thesis-passage on an unsettled question needs a rival
  that *denies its exact proposition*, not one that merely shares the topic; else it
  is adjacency → keep searching or both stay none.

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

### The Readiness Potential — Libet vs Schurger (a live-rivals pair on free will)
The first **contested-concept** pair (concept `contested=True`, question status
`live-rivals`), so plural-or-none **requires** two rivals or none. Both are
in-copyright journal prose shipped as bounded-B fair-use (single sentences,
attributed, no affiliate link). Scope note: contested *scientific* concepts are the
feature's weakest fit (Phase 0: passages win where the prose IS the datum), so only
the two that touch an existential ache — free will here, the self below — were
shipped; IIT, Global Workspace, Analytic Idealism and The Case Against Reality stay
**none** by design.
- **Passage 1 (thesis — the threat):** "It is concluded that cerebral initiation of
  a spontaneous, freely voluntary act can begin unconsciously…" *Benjamin Libet,*
  *Time of Conscious Intention to Act…* (*Brain* 106, **1983**, pp. 623–642).
  Byte-verified against the PubMed abstract (<https://pubmed.ncbi.nlm.nih.gov/6640273/>).
- **Passage 2 (rebuttal):** "The reason we do not experience the urge to move…is
  simply because, at that time, the neural decision to move (crossing the decision
  threshold) has not yet been made." *Aaron Schurger,* accumulator model (*PNAS* 109,
  **2012**, E2904–E2913). Byte-verified against the open-access PNAS/PMC full text
  (<https://pmc.ncbi.nlm.nih.gov/articles/PMC3479453/>).
- **Rights:** both **in-copyright-fair-use**; Schurger's book pointer is the free PMC
  full text, Libet's is none (paywalled journal).

### The Ego Tunnel — Metzinger vs Zahavi (a live-rivals pair on the self)
The second contested pair (question status `live-rivals`). Both in-copyright prose,
verbatim-verified against full texts.
- **Passage 1 (thesis):** "The Ego is a transparent mental image: You — the physical
  person as a whole — look right through it. You do not see it. But you see with it."
  *Thomas Metzinger,* *The Ego Tunnel* (Basic Books, **2009**), Introduction.
  Byte-verified against the full text; edition pointer is the WorldCat record
  (<https://search.worldcat.org/isbn/9780465020690>).
- **Passage 2 (rebuttal):** "Rather, experiences are necessarily like something for a
  subject, they necessarily involve a point of view – they come with perspectival
  ownership." *Dan Zahavi,* "We and I," *The Philosopher*. Byte-verified against the
  live essay (<https://www.thephilosopher1923.org/post/we-and-i>), which is also the
  free book pointer. (The line Zahavi quotes about "the utter elimination of
  experience" is **Joseph Margolis'**, not Zahavi's — verified and not attributed to
  Zahavi.)
- **Rights:** both **in-copyright-fair-use**.

### Plan-A heat-pilot (added 2026-06-27)

Seven passages across five questions, non-Western-led, arranged so **no question
debuts Western-only** (`mind` and `abs` each open with a non-Western voice). All
selected by **heat** (does the line out-pull its gloss), not by provenance
convenience. Independently byte-verified (fresh re-fetch, HTML-aware normaliser).

#### The Dao — Laozi (solo recognition, `real`)
- **Passage:** "The Tao that can be trodden is not the enduring and unchanging Tao.
  The name that can be named is not the enduring and unchanging name." (26 words)
- **Edition:** James Legge, 1891 (= Sacred Books of the East v39). **PD.** ch. 1.
- **Source / verification:** Project Gutenberg #216
  (<https://www.gutenberg.org/cache/epub/216/pg216.txt>); byte-verified 2026-06-27.
- **Book pointer:** <https://www.gutenberg.org/ebooks/216>.

#### The Butterfly Dream — Zhuangzi (solo recognition, `mind`)
- **Passage:** "Formerly, I, Kwang Kâu, dreamt that I was a butterfly… or it was now
  a butterfly dreaming that it was Kâu." (65 words)
- **Edition:** James Legge, 1891, *The Writings of Kwang-dze* (Sacred Books of the
  East v39), Bk II. **PD.**
- **Verification:** **transcription-verified, print-corrected.** Full span
  byte-verified present in the Legge SBE v39 transcription; the single period after
  "enjoying itself" was restored to Legge's 1891 print (the digital transcription
  drops it, fusing two sentences). No clean PD *scan* byte-matches the proper name
  "Kwang Kâu" (archive.org SBE-v39 OCR garbles it), so edition + locator are
  recorded per the verification policy above. Verified 2026-06-27.
- **Source / book pointer:** <https://www.sacred-texts.com/tao/sbe39/sbe39123.htm>
  / <https://www.sacred-texts.com/tao/sbe39/index.htm>.

#### Nirvana — The Dhammapada (solo recognition, `peace`)
- **Passage:** "From love comes grief, from love comes fear; he who is free from
  love knows neither grief nor fear." (19 words)
- **Edition:** F. Max Müller, 1881 (= Sacred Books of the East v10), ch. XVI, v. 215.
  **PD.**
- **Source / verification:** Project Gutenberg #2017
  (<https://www.gutenberg.org/cache/epub/2017/pg2017.txt>); byte-verified 2026-06-27.
- **Book pointer:** <https://www.gutenberg.org/ebooks/2017>.

#### Mystical Union (Fana) — Rumi (solo recognition, `trans`)
- **Passage:** "Hearken to the reed-flute, how it discourses… I burst my breast,
  striving to give vent to sighs, And to express the pangs of my yearning for my
  home." (56 words, the Song of the Reed)
- **Edition:** E. H. Whinfield, 1898, *Masnavi i Ma'navi*, Book I proem. **PD.**
- **Source / verification:** archive.org item `masnaviimanavi`
  (<https://archive.org/download/masnaviimanavi/Masnavi_i_Ma_navi_djvu.txt>);
  byte-verified 2026-06-27.
- **Book pointer:** <https://archive.org/details/masnaviimanavi>.

#### Tawhid (Divine Unity) — The Qur'an (rival pair on `abs`, with The Problem of Evil)
A **partial rival pair** on an open question: Tawhid **affirms** a single,
incomparable Absolute; The Problem of Evil **presses** the theodicy difficulty.
Epicurus attacks the deity's *attributes*, not the Absolute's bare existence — a
tighter counter (naturalist denial / śūnyatā on the divine) is **backlog**; the pair
ships because two voices keep the open question plural rather than a verdict.
- **Passage:** "SAY: He is God alone: God the eternal! He begetteth not, and He is
  not begotten; And there is none like unto Him." (23 words)
- **Edition:** J. M. Rodwell, 1861, *The Koran*, Surah al-Ikhlas (112:1–4). **PD.**
- **Source / verification:** Project Gutenberg #2800
  (<https://www.gutenberg.org/cache/epub/2800/pg2800.txt>); byte-verified 2026-06-27.
- **Book pointer:** <https://www.gutenberg.org/ebooks/2800>. Sacred text — transmit,
  not "answers your ache."

#### Stream of Consciousness — William James (non-rival second voice on `mind`)
- **Passage:** "Consciousness, then, does not appear to itself chopped up in bits…
  A 'river' or a 'stream' are the metaphors by which it is most naturally described."
  (51 words)
- **Edition:** William James, 1890, *The Principles of Psychology*, Vol. I, ch. IX.
  **PD.**
- **Source / verification:** Project Gutenberg #57628
  (<https://www.gutenberg.org/cache/epub/57628/pg57628.txt>); byte-verified 2026-06-27.
- **Book pointer:** <https://www.gutenberg.org/ebooks/57628>.

#### The Problem of Evil — David Hume (rival to Tawhid on `abs`)
- **Passage:** "EPICURUS's old questions are yet unanswered. Is he willing to
  prevent evil, but not able?… Is he both able and willing? whence then is evil?"
  (39 words)
- **Edition:** David Hume, 1779, *Dialogues Concerning Natural Religion*, Part X
  (Philo restating Epicurus). **PD.**
- **Source / verification:** Project Gutenberg #4583
  (<https://www.gutenberg.org/cache/epub/4583/pg4583.txt>); byte-verified 2026-06-27.
- **Book pointer:** <https://www.gutenberg.org/ebooks/4583>.

## Deferred (authored-but-not-shipped)

_(none)_
