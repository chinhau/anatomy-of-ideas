# -*- coding: utf-8 -*-
"""Round-fifteen expansion: three traditions cleared off the honesty bar.

The canon audit kept Andean, Māori, and Cārvāka thought excluded only because
their canon is oral/anonymous — the atlas requires a named author + dated text.
A 2026-06-23 source review (then a 3-agent critique) found each can now be
anchored to citable scholarship, so they enter as a trimmed, balance-correcting
set (4 this-worldly to 1 cosmological, against the atlas's old quietist tilt):

  • Cārvāka materialism (mind) — the atlas's only classical-Indian materialist.
    NOT flagged contested: classical materialism (cf. the un-flagged Materialism
    and Atomism) is disclosed by its badge, not the science-overreach flag.
  • Māori tikanga (live) + mauri/woven universe (real) — insider-authored.
  • Andean ayni (just) + yanantin (real) — reciprocity and complementary dualism.

Dropped after critique: buen vivir (its own theorist calls it non-indigenous, a
2008 policy coinage), the Worlded Self and ayllu (a 5th/6th relational-self
restatement of ground Ubuntu/Perspectivism/Relational-Self already hold), and Te
Whare Tapa Whā (a 1980s health-policy model, the weakest distinct move).

Three new badges (crv, mao, and). Imports expand14 and rebuilds.
"""
import concepts
import expand, expand2, expand3, expand4, expand5, expand6
import expand7, expand8, expand9, expand10, expand11, expand12, expand13, expand14

concepts.TRAD.update({"crv": "Cārvāka", "mao": "Māori", "and": "Andean"})

# ---- the new concepts: (id, qid, trad, era, gloss, thinkers) ----
# Oral/anonymous traditions are dated to the codifying text (cf. Ubuntu 1999),
# with the reading note disclosing the modern codification; Cārvāka is a genuinely
# ancient idea reconstructed from later hostile sources, so it keeps its old era.
NEW_C15 = [
 ("Bhūtacaitanyavāda (Mind from Matter)","mind","crv",-600,"Consciousness is no soul but a quality that arises when the four elements combine — as the power to intoxicate arises when ferments are mixed — and ends when the body does.",["Bṛhaspati (attrib.)","Purandara"]),
 ("Tikanga (Right Conduct)","live","mao",2003,"Right action is tikanga — correct practice rooted in values like mana, tapu and manaakitanga; ethics is keeping relationships in balance, not obeying an abstract rule.",["Hirini Moko Mead"]),
 ("Mauri (The Woven Universe)","real","mao",2003,"Reality is one woven fabric, each thing carrying mauri, a binding life-force; cosmos and person are continuous, not split into mind and matter or subject and object.",["Māori Marsden"]),
 ("Ayni (Reciprocity)","just","and",1988,"To live well is to keep ayni — the binding reciprocity by which people, community and the living world give and return in balance; obligation, not contract, holds the world together.",["Josef Estermann","Catherine Allen"]),
 ("Yanantin (Complementary Dualism)","real","and",1986,"Opposites — male and female, day and night — are not rivals to be resolved but yanantin: paired halves that complete each other; reality runs on balanced, productive tension.",["Tristan Platt","Hillary Webb"]),
]
concepts.C.extend(NEW_C15)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R15 = [
 ("Bhūtacaitanyavāda (Mind from Matter)","The Immortal Soul","rejects"),
 ("Bhūtacaitanyavāda (Mind from Matter)","Materialism","echoes"),
 ("Bhūtacaitanyavāda (Mind from Matter)","Karma","rejects"),
 ("Tikanga (Right Conduct)","Ren & Li","echoes"),
 ("Tikanga (Right Conduct)","Ubuntu","echoes"),
 ("Mauri (The Woven Universe)","Yin–Yang / Qi","echoes"),
 ("Mauri (The Woven Universe)","The Dao","echoes"),
 ("Ayni (Reciprocity)","Social Contract","rejects"),
 ("Ayni (Reciprocity)","Ubuntu","echoes"),
 ("Yanantin (Complementary Dualism)","Yin–Yang / Qi","echoes"),
 ("Yanantin (Complementary Dualism)","Mauri (The Woven Universe)","echoes"),
]
concepts.R.extend(NEW_R15)

concepts.main()
