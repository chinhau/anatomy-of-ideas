# -*- coding: utf-8 -*-
"""Round-eighteen expansion: an East-Asian / Confucian backfill.

The atlas tagged Mencius, Xunzi, Zhu Xi and Wang Yangming on shared concepts
but flattened their signature *debates* into one entry each — the "hidden gap"
the 2026-06-23 concept-gap audit named. A 2026-06-24 source-research pass +
2-agent critique (citations / red-team-balance) sharpened the two flattened
nodes and added the missing poles:

  • Human Nature Is Good (chn, Mencius c.-300) + Human Nature Is Bad (chn, Xunzi
    c.-250) — the founding Confucian debate on xing, a clean two-pole pair on the
    `self` axis. Glossed so Mencius is innate *sprouts* needing cultivation (not
    finished virtue) and Xunzi's xing-è is *crooked / unwrought* reshaped by ritual
    (NOT theological evil).
  • Investigation of Things (chn, Zhu Xi c.1175) — gewu, the Cheng-Zhu
    epistemology (`know`): moral knowledge won by investigating the principle (li)
    in things, gradually, from the outside in. The explicit rival to —
  • the existing **Self-Cultivation** node, whose gloss is gloss-for-gloss Wang
    Yangming's liangzhi / unity-of-knowing-acting. Round 18 RETAGS it to Wang
    alone (Zhu Xi dropped in readings_extra.py) so the headline Neo-Confucian split
    reads as a rivalry, not a smear. gewu `rejects` Self-Cultivation across the
    know↔trans axes (cross-question edges are already normal here, cf. Four-Seven).
  • Being-Time (jpn, Dōgen 1240) — Uji, a metaphysics of time (`real`): each
    existent IS time, each moment total. Gives `jpn` its first formal philosopher
    (it had only Ikigai); echoes the Western process-metaphysics ally Process
    Reality and its Buddhist root Dependent Origination.

These also ROOT the previously-orphaned Korean Four-Seven Debate, which descends
from Mencius's four sprouts + Zhu Xi's li/qi but whose sources weren't in the graph.

Dropped after critique: Nishida Kitarō (Pure Experience / Absolute Nothingness) —
a near-isolate with no in-round rival that would deepen the consciousness/
"nothingness" cluster right after R17's Yogācāra; held for a dedicated
modern-non-Western round. No new badges (chn + jpn already exist).
"""
import concepts
import expand, expand2, expand3, expand4, expand5, expand6
import expand7, expand8, expand9, expand10, expand11, expand12
import expand13, expand14, expand15, expand16, expand17

# ---- the new concepts: (id, qid, trad, era, gloss, thinkers) ----
NEW_C18 = [
 ("Human Nature Is Good","self","chn",-300,"We are born with four moral 'sprouts' (duan): the pang of compassion, the sense of shame, the impulse to defer, the feel for right and wrong. Goodness is these sprouts grown to maturity — human nature tends to the good as water tends downhill, and cruelty is a stunting, not our origin.",["Mencius"]),
 ("Human Nature Is Bad","self","chn",-250,"Left to itself, human nature is crooked (è) — spontaneously grasping, partial, prone to strife. What we call virtue is a deliberate human craft (wei), straightened into us by ritual, teachers and the sages, the way a warped board is steamed flat. Not innate evil — raw material that needs working.",["Xunzi"]),
 ("Investigation of Things","know","chn",1175,"Moral understanding is won from the outside in: investigate the principle (li) inherent in each thing and affair, one after another, until one day it breaks through into comprehensive insight. Knowledge precedes and guides right action — the gradual, studious road to sagehood.",["Zhu Xi"]),
 ("Being-Time","real","jpn",1240,"Time is not a road things travel down; each existent is time and each time is an existent. The pine is time, the moment is the whole of being. Time does not flow past us — it is what we are, total and complete in every now.",["Dōgen"]),
]
concepts.C.extend(NEW_C18)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R18 = [
 ("Human Nature Is Bad","Human Nature Is Good","rejects"),
 ("Human Nature Is Good","Relational Self","builds"),
 ("Human Nature Is Good","Ren & Li","builds"),
 ("Human Nature Is Bad","Ren & Li","builds"),
 ("Human Nature Is Bad","Legalism","echoes"),
 ("Investigation of Things","Self-Cultivation","rejects"),
 ("Self-Cultivation","Human Nature Is Good","builds"),
 ("Investigation of Things","Human Nature Is Good","builds"),
 ("Investigation of Things","Yin–Yang / Qi","echoes"),
 ("The Four-Seven Debate","Human Nature Is Good","builds"),
 ("The Four-Seven Debate","Investigation of Things","builds"),
 ("Principle Rides on Force","Investigation of Things","rejects"),
 ("Being-Time","Process Reality","echoes"),
 ("Being-Time","Dependent Origination","echoes"),
]
concepts.R.extend(NEW_R18)

concepts.main()
