# -*- coding: utf-8 -*-
"""Round-seventeen expansion: the mind-body problem.

The `mind` lane was rich in *anti*-physicalist arguments (The Hard Problem,
What It Is Like, The Knowledge Argument, The Chinese Room) but largely missing
the physicalist positions those arguments target — the same one-sided imbalance
Round 16 fixed for ethics. A 2026-06-24 source-research pass + a 2-agent critique
(citations / red-team-balance) gave physicalism its voice and added the
cross-tradition counter-pole it was missing:

  • Mind-Brain Identity Theory (ana, Place 1956 / Smart 1959) — the positive
    type-physicalist thesis the anti-physicalist cluster all rebut yet which was
    absent. The reading note carries the multiple-realizability objection (so the
    tile isn't presented as unproblematic) — MR itself is NOT a separate tile, as
    the existing Functionalism is already Putnam's (1967) conclusion from it.
  • Anomalous Monism (ana, Davidson 1970) — token physicalism with no
    psychophysical laws; the type-vs-token bridge as its own tile.
  • Eliminative Materialism (ana, P. Churchland 1981) — folk psychology as a
    false empirical theory (glossed as that, NOT as "there are no minds").
  • Yogācāra / Mind-Only (bud, Vasubandhu c. 350) — the non-Western IDEALIST
    counter-pole. Cārvāka (added R15) is *also* materialist, so it reinforces the
    physicalist pole rather than balancing it; Yogācāra is the genuine rival (an
    Asian idealism ~1300 yrs before Berkeley), glossed as "experience is
    consciousness-structured," NOT "the world is illusion."

Dropped after critique: Multiple Realizability (duplicates Functionalism's
Putnam-1967 source — folded into the Identity→Functionalism link + note); The
Extended Mind (distinct from Embodied Mind but not a physicalist position —
deferred to a future 4E mini-round); Supervenience (a relation, not a position).

No new badges (Analytic + Buddhist already exist). Imports expand16 and rebuilds.
"""
import concepts
import expand, expand2, expand3, expand4, expand5, expand6
import expand7, expand8, expand9, expand10, expand11, expand12
import expand13, expand14, expand15, expand16

# ---- the new concepts: (id, qid, trad, era, gloss, thinkers) ----
NEW_C17 = [
 ("Mind-Brain Identity Theory","mind","ana",1959,"The mind just is the brain: each mental state is identical to a brain state, the way lightning turned out to be electrical discharge — no extra mental stuff, no soul, feeling pain simply is a certain neural firing. (The standard reply: one mind-kind could run on many different physical systems, so perhaps only each particular state, not each type, is physical.)",["J.J.C. Smart","U.T. Place","Herbert Feigl"]),
 ("Anomalous Monism","mind","ana",1970,"Every mental event is some physical event — yet no strict laws link the mental to the physical. Mind is neither a separate substance nor reducible to neuroscience: the very same events, caught in two vocabularies that never lock together into law.",["Donald Davidson"]),
 ("Eliminative Materialism","mind","ana",1981,"'Belief,' 'desire,' 'pain' belong to folk psychology — a primitive theory of mind that, like phlogiston or the four humours, a mature neuroscience may show to be simply false. The bet is that these everyday categories will be replaced, not tidily reduced.",["Paul M. Churchland","Patricia S. Churchland"]),
 ("Yogācāra (Mind-Only)","mind","bud",350,"All we ever meet is consciousness and its images; the seeming split between an inner grasper and an outer grasped world is itself constructed by mind. Not that nothing exists — but that experience is 'mind-only' (vijñapti-mātra), structured through and through by consciousness.",["Vasubandhu"]),
]
concepts.C.extend(NEW_C17)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R17 = [
 ("Mind-Brain Identity Theory","Substance Dualism","rejects"),
 ("Mind-Brain Identity Theory","Bhūtacaitanyavāda (Mind from Matter)","echoes"),
 ("Functionalism","Mind-Brain Identity Theory","rejects"),
 ("The Knowledge Argument","Mind-Brain Identity Theory","rejects"),
 ("Anomalous Monism","Mind-Brain Identity Theory","builds"),
 ("Anomalous Monism","Eliminative Materialism","rejects"),
 ("Eliminative Materialism","Mind-Brain Identity Theory","builds"),
 ("Eliminative Materialism","The Intentional Stance","rejects"),
 ("Yogācāra (Mind-Only)","Mind-Brain Identity Theory","rejects"),
 ("Yogācāra (Mind-Only)","Bhūtacaitanyavāda (Mind from Matter)","rejects"),
 ("Yogācāra (Mind-Only)","Idealism","echoes"),
 ("Yogācāra (Mind-Only)","Śūnyatā (Emptiness)","echoes"),
]
concepts.R.extend(NEW_R17)

concepts.main()
