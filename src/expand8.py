# -*- coding: utf-8 -*-
"""Round-eight expansion: other civilizations (the clean tier).

Fills the largest remaining civilizational gaps with concepts that each clear
the bar — a real, dated source and an identifiable author or tradition:
Zoroastrian Persia, Nahua (Aztec) Mesoamerica, Mesopotamia (via the lit lane),
Ancient Egypt, and a second Jewish entry. Nahua thought joins the Indigenous
lane; the ancient Near-Eastern and Mediterranean entries join the West lane.

Imports `expand7` (rounds 1-7, already rebuilt) and extends, then rebuilds.
"""
import concepts
import expand    # round one
import expand2   # round two
import expand3   # round three
import expand4   # round four
import expand5   # round five
import expand6   # round six
import expand7   # round seven

concepts.TRAD.update({
    "zor": "Zoroastrian",
    "nah": "Nahua (Aztec)",
    "egy": "Ancient Egyptian",
})

# ---- the clean tier: (id, qid, trad, era, gloss, thinkers) ----
NEW_C8 = [
 ("Cosmic Dualism","live","zor",-1000,"The cosmos is a battlefield of truth against the lie, light against dark; each soul must choose a side, and the choice matters.",["Zarathustra"]),
 ("Flower and Song","know","nah",1450,"On a fleeting, slippery earth, truth cannot be grasped directly — only flower-and-song, poetry and art, can speak it.",["Nezahualcoyotl"]),
 ("The Search for Immortality","mean","lit",-1200,"A king storms the world for deathlessness, loses it, and learns the only immortality is the work and the city he leaves behind.",["Epic of Gilgamesh"]),
 ("Ma'at (Cosmic Order)","just","egy",-2375,"Truth, justice, and cosmic order are one principle; the king upholds ma'at against chaos, and each heart is weighed by it.",["Ptahhotep"]),
 ("Radical Amazement","know","jew",1955,"Knowledge begins not in doubt but in wonder; awe before the sheer existence of things is the root of insight and the religious life.",["Abraham Joshua Heschel"]),
]
concepts.C.extend(NEW_C8)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R8 = [
 ("Cosmic Dualism","Yin–Yang / Qi","rejects"),
 ("Cosmic Dualism","Marriage of Heaven and Hell","echoes"),
 ("Cosmic Dualism","Original Sin","echoes"),
 ("Flower and Song","Mono no Aware","echoes"),
 ("Flower and Song","Negative Capability","echoes"),
 ("Flower and Song","Yūgen","echoes"),
 ("The Search for Immortality","The Heroic Code","echoes"),
 ("The Search for Immortality","Being-toward-Death","echoes"),
 ("The Search for Immortality","Carpe Diem","echoes"),
 ("Ma'at (Cosmic Order)","The Dao","echoes"),
 ("Ma'at (Cosmic Order)","Government by Virtue","echoes"),
 ("Ma'at (Cosmic Order)","Antigone's Law","echoes"),
 ("Radical Amazement","The Cogito","rejects"),
 ("Radical Amazement","Negative Capability","echoes"),
 ("Radical Amazement","Mono no Aware","echoes"),
]
concepts.R.extend(NEW_R8)

concepts.main()
