# -*- coding: utf-8 -*-
"""Round-nineteen expansion: an Islamic golden-age (falsafa) backfill.

The `isl` lane was 9 concepts deep but only ONE was falsafa (Avicenna's Flying
Man); the rest was Sufi/mystical + kalām. The rationalist-philosophical pole was
absent and al-Ghazālī appeared only as a tag. A 2026-06-24 source-research pass +
2-agent critique (citations / red-team-balance) added the falsafa thread as a
debate, not a list:

  • Occasionalism (isl, al-Ghazālī 1095, `know`) — what looks like cause-and-
    effect is God's habit; 'necessary connection' is expectation, not a power in
    things. Glossed so his target is metaphysical NECESSITY (for divine
    omnipotence/miracle), NOT a ban on inquiry — he is not "the man who killed
    Islamic science." Anticipates Hume: The Problem of Induction `echoes` it.
  • Harmony of Religion and Philosophy (isl, Averroes/Ibn Rushd c.1180, `know`) —
    truth does not contradict truth, so demonstration and revelation can't really
    clash; the point-by-point reply (Tahāfut al-Tahāfut) `rejects` Occasionalism.
    ONE truth reached two ways — the Latin "double-truth Averroism" is a reception
    artifact he denied, kept out of the gloss.
  • The Virtuous City (isl, al-Fārābī c.940, `just`) — Plato's philosopher-king in
    a prophetic key (intellect touching the Active Intellect), NOT theocracy.
  • The Necessary Being (isl, Avicenna c.1027, `real`) — the essence/existence
    distinction + contingency proof. Avicenna had only the Flying Man; this is the
    metaphysics al-Ghazālī attacks and Aquinas inherits (The Five Ways `builds` on it).

RETAG (NOT a new concept): the existing **Faith Beyond Reason** node conflated two
distinct al-Ghazālī theses — fideism AND occasionalism ("even cause and effect rest
on God's will"). Its gloss is stripped to pure fideism here so it doesn't duplicate
the new Occasionalism entry; its existing links are unchanged.

Dropped after critique: Ibn Khaldūn / ʿAṣabiyya — a tonal orphan (philosophy of
history) that lands in the already-saturated `just` lane and doesn't engage the
al-Ghazālī↔Averroes spine; held for a future philosophy-of-history round. No new
badges (isl already exists).
"""
import concepts
import expand, expand2, expand3, expand4, expand5, expand6
import expand7, expand8, expand9, expand10, expand11, expand12
import expand13, expand14, expand15, expand16, expand17, expand18

# ---- retag: strip occasionalism out of Faith Beyond Reason (pure fideism now) ----
for _i, _c in enumerate(concepts.C):
    if _c[0] == "Faith Beyond Reason":
        concepts.C[_i] = (_c[0], _c[1], _c[2], _c[3],
            "Reason cannot reach the deepest truths; certainty comes not from proof but from the heart's direct taste of the divine.",
            _c[5])
        break

# ---- the new concepts: (id, qid, trad, era, gloss, thinkers) ----
NEW_C19 = [
 ("Occasionalism","know","isl",1095,"What looks like cause and effect is only God's habit: fire does not burn the cotton — God creates the burning when they touch, and could withhold it. 'Necessary connection' is our expectation, not a power in things; only God truly acts. (His quarrel with the philosophers was over divine freedom and miracle, not a ban on inquiry.)",["Al-Ghazali"]),
 ("Harmony of Religion and Philosophy","know","isl",1180,"Truth does not contradict truth, so demonstrated philosophy and revelation cannot really clash; where scripture's plain sense collides with a proof, the trained reader must take it as allegory — and the Law itself commands this. One truth reached two ways, for two kinds of mind, never two truths.",["Averroes (Ibn Rushd)"]),
 ("The Virtuous City","just","isl",940,"The excellent city mirrors the order of the cosmos: its ruler is a philosopher-prophet whose intellect touches the Active Intellect and whose imagination can cast demonstrated truth into images the many can live by. Plato's philosopher-king, recast where prophecy and reason deliver one wisdom.",["al-Fārābī"]),
 ("The Necessary Being","real","isl",1027,"In everything around us, what a thing is (its essence) is one question and that it is (its existence) another — existence is something added to essence. Follow the chain of such contingent beings and you reach one whose essence simply is to exist: the Necessary Being, owing its being to nothing outside itself.",["Avicenna (Ibn Sina)"]),
]
concepts.C.extend(NEW_C19)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R19 = [
 ("Harmony of Religion and Philosophy","Occasionalism","rejects"),
 ("Harmony of Religion and Philosophy","Faith Beyond Reason","rejects"),
 ("Harmony of Religion and Philosophy","The Five Ways","echoes"),
 ("Occasionalism","The Necessary Being","rejects"),
 ("Occasionalism","Tawhid (Divine Unity)","builds"),
 ("The Problem of Induction","Occasionalism","echoes"),
 ("The Necessary Being","The Unmoved Mover","builds"),
 ("The Five Ways","The Necessary Being","builds"),
 ("The Virtuous City","Philosopher-Kings","builds"),
 ("The Virtuous City","Government by Virtue","echoes"),
]
concepts.R.extend(NEW_R19)

concepts.main()
