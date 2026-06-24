# -*- coding: utf-8 -*-
"""Round-sixteen expansion: the metaethics backfill.

The atlas was rich in *normative* ethics (how to act — Eudaimonia, the Categorical
Imperative, Utilitarianism, Care Ethics…) but silent on *metaethics*: the status
of moral claims themselves. A 2026-06-23 source-research pass + a 3-agent critique
(citations / red-team / balance) shaped a 7-concept round and, crucially, re-cut
its question-mapping along the atlas's own grain:

  • the *grounding/derivation* hinges live under `live` (ethics):
      Euthyphro Dilemma (grk), the Is–Ought Gap (enl), Moral Error Theory (ana),
      and the kalām Euthyphro — Ḥusn & Qubḥ (isl), added so the dilemma is not
      left a Greek island.
  • the *semantics/epistemology of moral terms* go under `know`, beside the
      existing philosophy-of-language + Indian-epistemology cluster:
      the Open-Question Argument (ana), Emotivism (ana), and Mīmāṃsā's
      dharma-from-the-Word (ind, sibling to the existing Pramāṇa).

No new badges (all five traditions already exist). Per the Option-A contested
policy, none are flagged: a tradition badge is the disclosure for a philosophical
position. Framing honesty notes from the critique are baked into the glosses —
Error Theory drops the "useful fiction" gloss (that is later fictionalism, not
Mackie); Emotivism is dated to Ayer 1936 and keeps Blackburn's quasi-realism in
the reading note, not the headline (the term "expressivism" post-dates 1936);
Mīmāṃsā hooks on the *self-validating, authorless* Veda, not bare śabda, to stay
distinct from Pramāṇa. Imports expand15 and rebuilds.
"""
import concepts
import expand, expand2, expand3, expand4, expand5, expand6
import expand7, expand8, expand9, expand10, expand11, expand12
import expand13, expand14, expand15

# ---- the new concepts: (id, qid, trad, era, gloss, thinkers) ----
NEW_C16 = [
 ("The Euthyphro Dilemma","live","grk",-380,"Socrates' trap: is an act good because the gods command it, or do they command it because it is already good? Either morality is an arbitrary divine whim, or its standard stands above the gods — and needs no god to ground it.",["Plato","Socrates"]),
 ("The Is–Ought Gap","live","enl",1739,"Hume's guillotine: from premises about what *is* the case, no conclusion about what *ought* to be can validly follow. Fact and value are split by a gap that no argument from nature alone can cross.",["David Hume"]),
 ("Moral Error Theory","live","ana",1977,"Our moral talk reaches for objective values woven into the world — duties that would bind us whatever we felt. There are no such queer facts, so every positive moral claim is, strictly, false.",["J.L. Mackie"]),
 ("The Open-Question Argument","know","ana",1903,"Whatever natural fact you equate with goodness — pleasure, survival, what we desire — it stays sensible to ask 'but is that good?' So 'good' names a simple, non-natural property, and defining it by nature is a fallacy.",["G.E. Moore","W.D. Ross"]),
 ("Emotivism","know","ana",1936,"Moral words state no facts; they vent and stir feeling. 'Stealing is wrong' adds nothing factual to 'stealing' — it means roughly 'Boo, stealing!' and tries to move you to feel the same.",["A.J. Ayer","C.L. Stevenson"]),
 ("Mīmāṃsā: Dharma from the Word","know","ind",-200,"Duty (dharma) is a future-facing 'ought' no perception or inference can reach; it is known only through the Veda's injunctions — an authorless, self-validating Word that needs no God or author to vouch for it.",["Jaimini","Kumārila Bhaṭṭa"]),
 ("Ḥusn & Qubḥ: Reason vs. Command","live","isl",950,"Are good and evil (ḥusn wa qubḥ) qualities reason can discover for itself, as the Muʿtazila held — or is a thing good only because God commands it, as the Ashʿarīs replied? Islam's own Euthyphro.",["ʿAbd al-Jabbār","al-Ashʿarī"]),
]
concepts.C.extend(NEW_C16)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R16 = [
 ("The Euthyphro Dilemma","Theory of Forms","echoes"),
 ("The Euthyphro Dilemma","Ḥusn & Qubḥ: Reason vs. Command","echoes"),
 ("The Is–Ought Gap","The Open-Question Argument","echoes"),
 ("The Is–Ought Gap","The Problem of Induction","echoes"),
 ("Moral Error Theory","The Open-Question Argument","rejects"),
 ("Moral Error Theory","Emotivism","echoes"),
 ("The Open-Question Argument","Utilitarianism","rejects"),
 ("Emotivism","Verification Principle","builds"),
 ("Mīmāṃsā: Dharma from the Word","Pramāṇa","echoes"),
 ("Mīmāṃsā: Dharma from the Word","Faith Beyond Reason","echoes"),
 ("Ḥusn & Qubḥ: Reason vs. Command","Categorical Imperative","echoes"),
]
concepts.R.extend(NEW_R16)

concepts.main()
