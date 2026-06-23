# -*- coding: utf-8 -*-
"""Round-eleven expansion: the practice-text gap.

The atlas leaned toward treatise-philosophy — argued theses — and under-counted
the contemplative traditions whose unit is a *method*, not a proposition. This
round adds five great practice texts whose teaching IS the discipline they
prescribe: hesychast prayer of the heart, the Ignatian Exercises, Dzogchen,
Buddhist mindfulness, and Sufi dhikr. Each names a real author/tradition and a
real, dated text. No new badges or lanes — they join Christian / Buddhist /
Islamic.

Imports `expand10` (rounds 1-10, already rebuilt) and extends, then rebuilds.
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
import expand10  # round ten

# ---- the practice texts: (id, qid, trad, era, gloss, thinkers) ----
NEW_C11 = [
 ("Hesychasm (The Jesus Prayer)","trans","chr",1338,"Still the mind, draw it down into the heart, and pray the Name without ceasing until the uncreated light dawns within.",["Gregory Palamas"]),
 ("The Spiritual Exercises","self","chr",1548,"A graded month of imaginative meditation and daily self-examination, training the soul to discern the spirits and choose freely for the good.",["Ignatius of Loyola"]),
 ("Dzogchen (The Great Perfection)","mind","bud",1350,"Awareness is already pure and perfect; nothing need be added or removed — simply recognize the naked, self-knowing ground and rest there.",["Longchenpa"]),
 ("The Four Foundations of Mindfulness","know","bud",-250,"Watch the body, feelings, mind, and phenomena arise and pass; in bare, sustained attention, see directly how all things are impermanent and not-self.",["The Buddha"]),
 ("Dhikr (Remembrance)","trans","isl",1300,"Repeat the divine Name with breath and heart until rememberer, remembered, and remembrance become one and the heart is polished to a mirror.",["Ibn ʿAṭāʾ Allāh al-Iskandarī"]),
]
concepts.C.extend(NEW_C11)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R11 = [
 ("Hesychasm (The Jesus Prayer)","Mystical Union (Fana)","echoes"),
 ("Hesychasm (The Jesus Prayer)","Circulation of the Light","echoes"),
 ("Hesychasm (The Jesus Prayer)","Grace","echoes"),
 ("The Spiritual Exercises","Self-Cultivation","echoes"),
 ("The Spiritual Exercises","The Magnum Opus","echoes"),
 ("The Spiritual Exercises","Grace","builds"),
 ("Dzogchen (The Great Perfection)","Sudden Awakening","echoes"),
 ("Dzogchen (The Great Perfection)","Choiceless Awareness","echoes"),
 ("Dzogchen (The Great Perfection)","Śūnyatā (Emptiness)","builds"),
 ("The Four Foundations of Mindfulness","The Eightfold Path","builds"),
 ("The Four Foundations of Mindfulness","Anattā (No-Self)","echoes"),
 ("The Four Foundations of Mindfulness","Non-Attachment","echoes"),
 ("Dhikr (Remembrance)","Mystical Union (Fana)","builds"),
 ("Dhikr (Remembrance)","Hesychasm (The Jesus Prayer)","echoes"),
 ("Dhikr (Remembrance)","Tawhid (Divine Unity)","echoes"),
]
concepts.R.extend(NEW_R11)

concepts.main()
