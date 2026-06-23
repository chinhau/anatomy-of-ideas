# -*- coding: utf-8 -*-
"""Round-seven expansion: scripture-born concepts (the Abrahamic theological core).

The atlas is idea-centric, so a scripture is never a node — it is a *source*.
This round names the distinctive *ideas* the Abrahamic scriptures contributed,
which until now appeared only as readings or were absent: Christian, Jewish,
and Islamic doctrines, each with scripture as the Primary reading and named
theologians (Augustine, Maimonides, al-Ash'ari) as the thinkers. These fold
into the existing West lane.

Imports `expand6` (rounds 1-6, already rebuilt) and extends, then rebuilds.
"""
import concepts
import expand    # round one
import expand2   # round two
import expand3   # round three
import expand4   # round four
import expand5   # round five
import expand6   # round six

concepts.TRAD.update({"chr": "Christian", "jew": "Jewish"})

# ---- scripture-born concepts: (id, qid, trad, era, gloss, thinkers) ----
NEW_C7 = [
 ("Agape","live","chr",55,"Love as self-giving gift, not desire for the lovable — patient, unearned, poured out even on the enemy.",["Paul of Tarsus","Augustine of Hippo"]),
 ("Grace","free","chr",427,"Salvation is an unearned gift, not a wage; no ladder of works reaches it — only the gift descends.",["Augustine of Hippo"]),
 ("Original Sin","self","chr",412,"Human nature is born already fractured; the will is divided against itself and cannot heal itself alone.",["Augustine of Hippo"]),
 ("Logos (The Word)","abs","chr",95,"In the beginning was the Word — the divine reason through which all things are made and hold together.",["John the Evangelist","Philo of Alexandria"]),
 ("Covenant","just","jew",-600,"A binding pact between God and a people: chosen and obligated at once, sealed by law.",["Hebrew Bible"]),
 ("Imago Dei","self","jew",-550,"Every human is made in the image of God, and so bears an inviolable worth no station can erase.",["Hebrew Bible","Maimonides"]),
 ("Tikkun Olam","just","jew",1573,"Creation shattered and the divine sparks scattered; our task is to gather them — to repair a broken world.",["Isaac Luria"]),
 ("Tawhid (Divine Unity)","abs","isl",650,"God is absolutely one — no partner, no division, no likeness; all multiplicity hangs from a single source.",["The Quran","al-Ash'ari"]),
 ("Fitra","self","isl",650,"Every soul is born with an innate disposition toward truth and the divine, before culture overlays it.",["The Quran"]),
]
concepts.C.extend(NEW_C7)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R7 = [
 ("Agape","Mohist Universal Love","echoes"),
 ("Agape","Care Ethics","echoes"),
 ("Grace","Original Sin","builds"),
 ("Grace","Karma","rejects"),
 ("Original Sin","Tabula Rasa","rejects"),
 ("Original Sin","The Underground Man","echoes"),
 ("Logos (The Word)","The Dao","echoes"),
 ("Logos (The Word)","The One","builds"),
 ("Logos (The Word)","The Five Ways","echoes"),
 ("Covenant","Social Contract","echoes"),
 ("Covenant","Tikkun Olam","builds"),
 ("Imago Dei","In Is Heaven (Innaecheon)","echoes"),
 ("Imago Dei","Ātman = Brahman","echoes"),
 ("Tikkun Olam","Engaged Buddhism","echoes"),
 ("Tikkun Olam","Mohist Universal Love","echoes"),
 ("Unity of Being","Tawhid (Divine Unity)","builds"),
 ("Tawhid (Divine Unity)","Pantheism","rejects"),
 ("Tawhid (Divine Unity)","The Five Ways","echoes"),
 ("Mystical Union (Fana)","Tawhid (Divine Unity)","echoes"),
 ("Fitra","Tabula Rasa","rejects"),
 ("Fitra","Imago Dei","echoes"),
]
concepts.R.extend(NEW_R7)

concepts.main()
