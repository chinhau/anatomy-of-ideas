# -*- coding: utf-8 -*-
"""Round-ten expansion: The Secret of the Golden Flower (太乙金華宗旨).

A Daoist inner-alchemy (neidan) classic — the Eastern mirror of round nine's
Western Magnum Opus, and bridged to it by the very same figure: Richard
Wilhelm's 1929 translation carried C. G. Jung's commentary. Joins the existing
Chinese badge / East lane.

Imports `expand9` (rounds 1-9, already rebuilt) and extends, then rebuilds.
"""
import concepts
import expand    # round one
import expand2   # round two
import expand3   # round three
import expand4   # round four
import expand5   # round five
import expand6   # round six
import expand7   # round seven
import expand8   # round eight
import expand9   # round nine

# ---- the concept: (id, qid, trad, era, gloss, thinkers) ----
NEW_C10 = [
 ("Circulation of the Light","trans","chn",1668,"Turn the light of awareness back upon its source and let it circulate; the spirit, no longer spent outward, coagulates into an immortal self — the golden flower.",["Lü Dongbin tradition"]),
]
concepts.C.extend(NEW_C10)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R10 = [
 ("Circulation of the Light","The Dao","builds"),
 ("Circulation of the Light","The Magnum Opus","echoes"),
 ("Circulation of the Light","Sitting in Forgetting","echoes"),
 ("Circulation of the Light","Wu Wei","echoes"),
 ("Circulation of the Light","Yoga: Stilling the Mind","echoes"),
]
concepts.R.extend(NEW_R10)

concepts.main()
