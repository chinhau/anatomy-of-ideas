# -*- coding: utf-8 -*-
"""Round-five expansion: the clean tier of African & Indigenous philosophy.

These traditions answer the eleven questions in their own right — Ubuntu on
the self, Àṣẹ on the force in things, perspectivism on mind across species,
the sacred-land thinkers on transcendence. They enter on the strictest bar:
each concept names a *living or modern, named author* and a *real, dated
text*, never anonymous "essential reading" that would force colonial
ethnography to stand in as authority.

Each people keeps its own badge — "African Philosophy", "Native American",
"Aboriginal Australian" — rather than one flattened "Indigenous" bucket;
they share only a timeline lane, the way Indian/Buddhist/Chinese/Japanese
already share the East lane.

Imports `expand4` (rounds 1-4, already rebuilt) and extends, then rebuilds.
"""
import concepts
import expand    # round one
import expand2   # round two
import expand3   # round three
import expand4   # round four

concepts.TRAD.update({
    "afr": "African Philosophy",
    "nam": "Native American",
    "abo": "Aboriginal Australian",
})

# ---- the clean tier: (id, qid, trad, era, gloss, thinkers) ----
NEW_C5 = [
 ("Ubuntu","self","afr",1999,"A person is a person through other persons; the self is woven from community, not prior to it.",["Mogobe Ramose"]),
 ("Àṣẹ (Vital Force)","real","afr",1976,"A vital force runs through word and world — the power that makes things happen, alive in speech, breath, and being.",["Wándé Abímbólá"]),
 ("Amerindian Perspectivism","real","nam",1998,"All beings see themselves as persons; what differs across the living world is not culture but the body through which it is seen.",["Eduardo Viveiros de Castro"]),
 ("The Sacred Land","abs","nam",1973,"The holy is bound to place, not time; revelation rises from particular land, not from a line of history.",["Vine Deloria Jr."]),
 ("The Land Is Law","just","abo",1999,"The land is the law and the ground of identity; to be a person is to hold a custodial relationship with country.",["Mary Graham"]),
]
concepts.C.extend(NEW_C5)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R5 = [
 ("Ubuntu","Relational Self","echoes"),
 ("Ubuntu","Care Ethics","echoes"),
 ("Ubuntu","Existential Self","rejects"),
 ("Àṣẹ (Vital Force)","Yin–Yang / Qi","echoes"),
 ("Àṣẹ (Vital Force)","The Dao","echoes"),
 ("Amerindian Perspectivism","Dependent Origination","echoes"),
 ("Amerindian Perspectivism","Brahman","echoes"),
 ("The Sacred Land","Mono no Aware","echoes"),
 ("The Sacred Land","The Dao","echoes"),
 ("The Land Is Law","Ubuntu","echoes"),
 ("The Land Is Law","The Sacred Land","echoes"),
 ("The Land Is Law","Social Contract","rejects"),
 ("The Land Is Law","Things Fall Apart","echoes"),
]
concepts.R.extend(NEW_R5)

concepts.main()
