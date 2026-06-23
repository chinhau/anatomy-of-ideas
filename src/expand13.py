# -*- coding: utf-8 -*-
"""Round-thirteen expansion: new traditions on the honesty bar.

The canon audit flagged three genuinely-absent traditions that own sharp, named
ideas with real, dated texts: the Sikh tradition (an entire world religion missing),
the Sāṃkhya darśana (the classical Indian realist dualism — the audit's "Sāṃkhya &
Nyāya", minus Nyāya, whose epistemology the existing Pramāṇa concept already carries),
and Muhammad Iqbal's modern Islamic philosophy of selfhood. Khudi doubles as a
counter-pole to the atlas's contemplative tilt: it argues for strengthening the self,
not dissolving it.

One new badge (skh, Sikh — joins the East lane). Imports expand12 and rebuilds.
"""
import concepts
import expand, expand2, expand3, expand4, expand5, expand6
import expand7, expand8, expand9, expand10, expand11, expand12

concepts.TRAD.update({"skh": "Sikh"})

# ---- the new concepts: (id, qid, trad, era, gloss, thinkers) ----
NEW_C13 = [
 ("Ik Onkar (The One Reality)","abs","skh",1499,"There is one formless, timeless reality whose name is truth; it pervades all and is reached by remembering it — not by ritual, priest, or caste.",["Guru Nanak"]),
 ("Sewa (Selfless Service)","live","skh",1500,"Service to others, offered with no thought of reward, is worship made real — and the great leveller that dissolves caste and rank.",["Guru Nanak"]),
 ("Sāṃkhya (Spirit and Nature)","real","ind",350,"Reality is two: puruṣa, pure witnessing consciousness, and prakṛti, ever-active nature; liberation is learning to tell them apart.",["Īśvarakṛṣṇa"]),
 ("Khudi (The Self Affirmed)","self","isl",1915,"The self is not to be dissolved but strengthened; the ego, tempered and made vital, becomes God's free co-worker — not a drop lost in the sea.",["Muhammad Iqbal"]),
]
concepts.C.extend(NEW_C13)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R13 = [
 ("Ik Onkar (The One Reality)","Tawhid (Divine Unity)","echoes"),
 ("Ik Onkar (The One Reality)","Brahman","echoes"),
 ("Ik Onkar (The One Reality)","Bhakti","echoes"),
 ("Sewa (Selfless Service)","Agape","echoes"),
 ("Sewa (Selfless Service)","Ubuntu","echoes"),
 ("Sewa (Selfless Service)","Mohist Universal Love","echoes"),
 ("Sāṃkhya (Spirit and Nature)","Brahman","rejects"),
 ("Sāṃkhya (Spirit and Nature)","Substance Dualism","echoes"),
 ("Yoga: Stilling the Mind","Sāṃkhya (Spirit and Nature)","builds"),
 ("Khudi (The Self Affirmed)","Mystical Union (Fana)","rejects"),
 ("Khudi (The Self Affirmed)","Anattā (No-Self)","rejects"),
 ("Khudi (The Self Affirmed)","Self-Actualization","echoes"),
]
concepts.R.extend(NEW_R13)

concepts.main()
