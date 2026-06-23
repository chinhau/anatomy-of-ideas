# -*- coding: utf-8 -*-
"""Round-nine expansion: the Hermetic & Esoteric tier (+ a Norse companion).

The Western esoteric current — Hermeticism, Gnosticism, alchemy, perennialism
— shaped centuries of thought and art, and is studied seriously today
(Hanegraaff, Jonas, Jung). It enters on the same bar as everything else: real,
dated sources and identifiable authors. Because these are fringe or actively
disputed truth-claims, the four esoteric concepts are tagged **Contested** —
presented as historically influential ideas about reality, not as consensus or
endorsement. Norse Ragnarök rides along as myth (its own badge), like the other
literary-mythic entries, and is *not* tagged contested.

Both badges fall in the West lane. Imports `expand8` (rounds 1-8, already
rebuilt) and extends, then rebuilds.
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

concepts.TRAD.update({
    "her": "Hermetic & Esoteric",
    "nrs": "Norse",
})

# ---- the tier: (id, qid, trad, era, gloss, thinkers) ----
NEW_C9 = [
 ("As Above, So Below","real","her",200,"The cosmos mirrors itself at every scale; the human being is a small world bound by hidden correspondence to the great one.",["Hermes Trismegistus (corpus)"]),
 ("Gnosis (The Divine Spark)","trans","her",150,"A spark of the divine lies trapped in matter; we are asleep in a flawed world, and salvation comes not by faith but by awakening secret knowledge.",["Valentinus"]),
 ("The Magnum Opus","trans","her",300,"Turning base metal to gold is a mask for the real work: the slow transmutation of the soul through dissolution and rebirth — solve et coagula.",["Zosimos of Panopolis"]),
 ("The Perennial Philosophy","abs","her",1540,"Beneath every religion's surface lies one and the same mystical truth; the traditions are many dialects of a single perennial wisdom.",["Agostino Steuco","Aldous Huxley"]),
 ("Ragnarök (Twilight of the Gods)","mean","nrs",1220,"Even the gods are mortal; the world ends in fire and a green world rises after — meaning is the courage to meet a doom that fate has already fixed.",["Snorri Sturluson"]),
]
concepts.C.extend(NEW_C9)

# Note: these esoteric concepts are NOT flagged "Contested". The badge is scoped
# to claims that present in the register of established empirical science but lack
# consensus (the consciousness/reality theories). Doctrinal and metaphysical
# claims — esoteric AND religious alike — are disclosed by their tradition badge,
# not by this tag, so the tag fires consistently across traditions.

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R9 = [
 ("As Above, So Below","Monadology","echoes"),
 ("As Above, So Below","The One","builds"),
 ("As Above, So Below","Ma'at (Cosmic Order)","echoes"),
 ("Gnosis (The Divine Spark)","Allegory of the Cave","echoes"),
 ("Gnosis (The Divine Spark)","Ātman = Brahman","echoes"),
 ("Gnosis (The Divine Spark)","Original Sin","rejects"),
 ("The Magnum Opus","Self-Cultivation","echoes"),
 ("The Magnum Opus","Sudden Enlightenment, Gradual Cultivation","echoes"),
 ("The Magnum Opus","As Above, So Below","builds"),
 ("The Perennial Philosophy","Hwajaeng (Reconciling Disputes)","echoes"),
 ("The Perennial Philosophy","Mystical Union (Fana)","echoes"),
 ("The Perennial Philosophy","Brahman","echoes"),
 ("Ragnarök (Twilight of the Gods)","Amor Fati","echoes"),
 ("Ragnarök (Twilight of the Gods)","The Heroic Code","echoes"),
 ("Ragnarök (Twilight of the Gods)","Being-toward-Death","echoes"),
]
concepts.R.extend(NEW_R9)

concepts.main()
