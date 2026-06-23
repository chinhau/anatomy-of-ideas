# -*- coding: utf-8 -*-
"""Round-fourteen expansion: a home for the philosophy of language.

The tab-redesign critique flagged the deepest structural gap in the atlas: no
question owned LANGUAGE/meaning, so "What can I know?" read pre-1900. The
linguistic turn made questions about knowledge into questions about meaning, so
philosophy of language earns its home under `know`. Five analytic landmarks
(Frege, Russell, Kripke, Austin, Grice) plus one Continental anchor (Saussure)
so the room is not purely Anglo.

One new badge (str, Structuralism). Imports expand13 and rebuilds.
"""
import concepts
import expand, expand2, expand3, expand4, expand5, expand6
import expand7, expand8, expand9, expand10, expand11, expand12, expand13

concepts.TRAD.update({"str": "Structuralism"})

# ---- the new concepts: (id, qid, trad, era, gloss, thinkers) ----
NEW_C14 = [
 ("Sense and Reference","know","ana",1892,"A name carries both a reference — what it picks out — and a sense, the way it is presented; 'morning star' and 'evening star' name one planet under two senses.",["Gottlob Frege"]),
 ("On Denoting","know","ana",1905,"'The present King of France' is a disguised quantifier, not a name; descriptions melt into logical form, so a sentence can name nothing and come out false rather than nonsense.",["Bertrand Russell"]),
 ("Naming and Necessity","know","ana",1980,"Names are rigid designators, fixed by a causal chain of use rather than a description — so some truths are necessary yet known only after looking.",["Saul Kripke"]),
 ("How to Do Things with Words","know","ana",1962,"To say something is often to do something — 'I promise', 'I name this ship'; much of language performs acts rather than describing facts.",["J. L. Austin"]),
 ("Speaker Meaning","know","ana",1975,"What a speaker means outruns what the words say; talk runs on shared maxims, so we convey more by implying than by stating.",["Paul Grice"]),
 ("Arbitrariness of the Sign","know","str",1916,"The bond between word and concept is arbitrary; each sign takes its value only from its difference from the others in the system.",["Ferdinand de Saussure"]),
]
concepts.C.extend(NEW_C14)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R14 = [
 ("On Denoting","Sense and Reference","rejects"),
 ("Naming and Necessity","On Denoting","rejects"),
 ("How to Do Things with Words","Language Games","echoes"),
 ("Speaker Meaning","How to Do Things with Words","builds"),
 ("Arbitrariness of the Sign","Language Games","echoes"),
]
concepts.R.extend(NEW_R14)

concepts.main()
