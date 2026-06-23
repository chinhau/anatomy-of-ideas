# -*- coding: utf-8 -*-
"""The ideas themselves: concepts, the great questions they answer,
and the links between ideas.
Color is carried by QUESTION (the new organizing principle), not tradition."""

import json

# ---- the eight perennial questions (the spine) ----
# qid, label, hue, one-line framing
QUESTIONS = [
    ("real",  "What is real?",            "#C99A33", "Metaphysics — the nature of being itself."),
    ("know",  "What can I know?",         "#46C4D4", "Epistemology — knowledge, its sources and limits."),
    ("self",  "What is the self?",        "#E2719E", "Mind & identity — what, if anything, the 'I' is."),
    ("live",  "How should I live?",       "#A9C23F", "Ethics — the good life and right action."),
    ("just",  "What is a just society?",  "#EA6A45", "Politics — power, justice, the legitimate order."),
    ("free",  "Is the will free?",        "#9070D8", "Freedom & determinism — whether we author our acts."),
    ("peace", "Why do we suffer?",        "#2E9E8F", "Liberation — the root of suffering and the way to peace."),
    ("abs",   "Is there an Absolute?",    "#7C8BD6", "The divine, the ground of being, ultimate reality."),
]

# ---- where human thought actually is on each question (the epistemic spine) ----
# Per the 5-state taxonomy in docs/MISSION.md, reviewed by a 4-agent panel
# (epistemics / even-handedness / working-scientist / red-team) on 2026-06-23.
# Each question carries a PRIMARY state + an optional RESIDUE state (the part the
# primary call leaves live), a confidence flag, and a move-based rationale that
# names no single thinker as having "settled" it. This is one map, from one
# vantage — see the honesty notes in docs/MISSION.md.
#   states: handed-off | hardened | live-rivals | open | dissolved
#   conf:   clear | contested
# qid -> (status, residue|None, conf, why)
STATUS = {
 "real":  ("handed-off",  "live-rivals", "contested",
           "Physics and cosmology now constrain what can be real; the realism-vs-anti-realism question stays live."),
 "know":  ("hardened",    "open",        "contested",
           "Formal limits genuinely closed sub-questions and naive foundationalism was abandoned — but justification debates stay live."),
 "mind":  ("handed-off",  "open",        "contested",
           "Science took over large parts of the mechanics; much of higher cognition, and the hard problem, survive the handoff."),
 "self":  ("live-rivals", "dissolved",   "contested",
           "A deflationary turn reframes the substantial self as a useful fiction; substance-self traditions hold the question wide open."),
 "live":  ("live-rivals", None,          "clear",
           "Virtue, duty, and consequence are mature, articulate, non-converging camps."),
 "just":  ("live-rivals", None,          "clear",
           "Liberal, libertarian, communitarian, and capability views are a stable, informed disagreement."),
 "free":  ("live-rivals", "open",        "contested",
           "Compatibilist, libertarian, and hard-determinist camps persist; the underlying metaphysics resists resolution in principle."),
 "peace": ("handed-off",  "live-rivals", "contested",
           "The mechanisms of suffering were handed to medicine and psychology; read as the problem of evil, the question stays live."),
 "mean":  ("open",        None,          "contested",
           "An evaluative, first-person residue that empirical work cannot absorb."),
 "trans": ("live-rivals", "open",        "contested",
           "Clinical methods of change are tested but contested; the contemplative ends of transformation stay open."),
 "abs":   ("open",        None,          "clear",
           "Resists resolution in principle; the map takes no side."),
}

# tradition badge codes (for a small label only) reuse the atlas inks loosely
TRAD = {
    "grk":"Ancient Greek","hel":"Hellenistic","med":"Medieval","mod":"Early Modern",
    "enl":"Enlightenment","c19":"19th C.","phe":"Phenomenology","ana":"Analytic",
    "con":"Continental","pra":"Pragmatism","psy":"Psychology","ind":"Indian",
    "bud":"Buddhist","chn":"Chinese","jpn":"Japanese",
}

# ---- the concepts ----
# id, qid, trad, era (year; BCE negative), gloss, thinkers
C = [
 # ---------- REALITY ----------
 ("Theory of Forms","real","grk",-380,"True reality is eternal, perfect Forms; the visible world is their shadow.",["Plato"]),
 ("Hylomorphism","real","grk",-350,"Every substance is matter shaped by form; reality is here, not in a Form-heaven.",["Aristotle"]),
 ("Atomism","real","grk",-420,"Everything is atoms moving in the void; no purpose, only matter and space.",["Democritus","Epicurus"]),
 ("Being is One","real","grk",-475,"Change is illusion; what truly is, is single, eternal and unchanging.",["Parmenides"]),
 ("Everything Flows","real","grk",-500,"All is becoming; you cannot step in the same river twice.",["Heraclitus"]),
 ("Materialism","real","enl",1750,"Only physical matter exists; mind and spirit are matter in motion.",["d'Holbach","La Mettrie"]),
 ("Idealism","real","mod",1710,"To be is to be perceived; reality is fundamentally mental, not material.",["Berkeley"]),
 ("Absolute Idealism","real","enl",1807,"Reality is Spirit (Geist) coming to know itself through history.",["Hegel"]),
 ("One Substance","real","mod",1677,"God and Nature are one infinite substance; everything is a mode of it.",["Spinoza"]),
 ("Process Reality","real","ana",1929,"The basic units of reality are events and becomings, not static things.",["Whitehead"]),
 ("Śūnyatā (Emptiness)","real","bud",200,"Nothing has inherent, independent existence; all is empty of fixed essence.",["Nagarjuna"]),
 ("Dependent Origination","real","bud",-450,"Nothing stands alone; each thing arises in dependence on conditions.",["The Buddha"]),
 ("Brahman","real","ind",-700,"A single non-dual absolute underlies all; the many-world is appearance (maya).",["Upanishads","Shankara"]),
 ("The Dao","real","chn",-400,"An ineffable source and pattern flows through all things; name it and you miss it.",["Laozi"]),
 ("Yin–Yang / Qi","real","chn",-300,"Reality is the dynamic interplay of complementary polarities and vital energy.",["Zhou cosmology"]),
 ("Monadology","real","enl",1714,"Reality is composed of countless windowless minds (monads) in pre-set harmony.",["Leibniz"]),

 # ---------- KNOWLEDGE ----------
 ("Allegory of the Cave","know","grk",-380,"We mistake shadows for reality; knowledge is the painful turn toward the light.",["Plato"]),
 ("Rationalism","know","mod",1640,"Reason, not the senses, is the road to certain knowledge.",["Descartes","Leibniz"]),
 ("Empiricism","know","mod",1690,"All knowledge begins in sense experience; the mind starts blank.",["Locke","Hume"]),
 ("The Cogito","know","mod",1637,"I can doubt everything but the doubting; 'I think, therefore I am.'",["Descartes"]),
 ("Tabula Rasa","know","mod",1689,"The mind at birth is a blank slate written on by experience.",["Locke"]),
 ("Skepticism","know","hel",-300,"Suspend judgment; certainty is unreachable, and peace lies in not grasping it.",["Pyrrho","Sextus"]),
 ("Transcendental Idealism","know","enl",1781,"We never know things-in-themselves, only a world shaped by the mind's categories.",["Kant"]),
 ("Falsifiability","know","ana",1934,"A claim is scientific only if some possible observation could refute it.",["Popper"]),
 ("Paradigm Shifts","know","ana",1962,"Science changes by revolutions, not steady accumulation; frameworks are incommensurable.",["Kuhn"]),
 ("Verification Principle","know","ana",1936,"A statement is meaningful only if it can be verified by experience or is logical.",["Logical Positivists"]),
 ("Two Truths","know","bud",200,"There is conventional everyday truth and ultimate truth; both are needed.",["Nagarjuna"]),
 ("Pramāṇa","know","ind",200,"Knowledge has valid sources: perception, inference, comparison, testimony.",["Nyaya school"]),
 ("Anekāntavāda","know","ind",-500,"Truth is many-sided; every claim is partial, true from some standpoint.",["Mahavira"]),

 # ---------- SELF ----------
 ("The Immortal Soul","mind","grk",-380,"The self is a deathless soul, temporarily housed in the body.",["Plato"]),
 ("Substance Dualism","mind","mod",1641,"Mind and body are two different substances; the thinking self is non-physical.",["Descartes"]),
 ("Ātman = Brahman","self","ind",-700,"Your deepest Self is identical with the absolute; 'thou art that.'",["Upanishads"]),
 ("Anattā (No-Self)","self","bud",-450,"There is no permanent self — only a changing bundle of processes.",["The Buddha"]),
 ("Bundle Theory","self","mod",1739,"The self is just a bundle of perceptions in flux; no enduring 'I' is found.",["Hume"]),
 ("The Unconscious","self","psy",1900,"Most of the mind is hidden; we are driven by forces we don't see.",["Freud"]),
 ("Collective Unconscious","self","psy",1916,"Beneath the personal psyche lies a shared layer of universal archetypes.",["Jung"]),
 ("Behaviorist Mind","mind","psy",1913,"Drop the inner self; study only observable behavior and conditioning.",["Watson","Skinner"]),
 ("Functionalism","mind","ana",1967,"Mind is what mind does; mental states are functional roles, not stuff.",["Putnam"]),
 ("Existential Self","self","phe",1943,"Existence precedes essence; there is no fixed self — we make ourselves by choosing.",["Sartre"]),
 ("Being-in-the-World","self","phe",1927,"The self isn't a thing inside us but our embodied, involved being-among-things.",["Heidegger","Merleau-Ponty"]),
 ("The Mirror Stage","self","con",1949,"The 'I' is formed from outside — an image and the gaze of the Other.",["Lacan"]),
 ("Relational Self","self","chn",-500,"A person is constituted by their roles and relationships, not isolated within.",["Confucius"]),
 ("Self-Actualization","self","psy",1954,"The self is a project; health is becoming all that one can be.",["Maslow","Rogers"]),

 # ---------- ETHICS ----------
 ("Eudaimonia","live","grk",-340,"The good life is flourishing through the exercise of virtue and reason.",["Aristotle"]),
 ("The Golden Mean","live","grk",-340,"Virtue lies between extremes — courage between cowardice and recklessness.",["Aristotle"]),
 ("Stoic Virtue","live","hel",-300,"Live according to reason and nature; only virtue is truly good.",["Zeno","Epictetus"]),
 ("Epicurean Pleasure","live","hel",-300,"The good is pleasure rightly understood — tranquility and absence of pain.",["Epicurus"]),
 ("Categorical Imperative","live","enl",1785,"Act only on a rule you could will everyone to follow; treat people as ends.",["Kant"]),
 ("Utilitarianism","live","c19",1789,"The right act produces the greatest happiness for the greatest number.",["Bentham","Mill"]),
 ("Ren & Li","live","chn",-500,"Cultivate humaneness (ren) through ritual propriety (li) and right relationships.",["Confucius"]),
 ("Wu Wei","live","chn",-400,"Act without forcing; align with the natural flow rather than strive against it.",["Laozi","Zhuangzi"]),
 ("Ahimsa","live","ind",-500,"Non-violence toward all living things, in deed, word and thought.",["Mahavira","Gandhi"]),
 ("Master & Slave Morality","live","c19",1887,"Inherited morality is a slave's revolt; revalue values and create your own.",["Nietzsche"]),
 ("Authenticity","live","phe",1943,"To live well is to own your freedom and refuse 'bad faith' — fleeing it.",["Sartre","Kierkegaard"]),
 ("Care Ethics","live","con",1982,"Morality grows from relationship and care, not abstract rules.",["Gilligan","Noddings"]),

 # ---------- SOCIETY ----------
 ("Philosopher-Kings","just","grk",-380,"The just city is ruled by those who know the good; each part in its place.",["Plato"]),
 ("Social Contract","just","mod",1651,"Legitimate authority rests on an agreement among the governed.",["Hobbes","Locke","Rousseau"]),
 ("Leviathan","just","mod",1651,"Without a strong sovereign, life is a war of all against all.",["Hobbes"]),
 ("Natural Rights","just","mod",1689,"All have rights to life, liberty and property that the state must protect.",["Locke"]),
 ("The General Will","just","enl",1762,"Legitimacy flows from the people's collective will toward the common good.",["Rousseau"]),
 ("Historical Materialism","just","c19",1848,"History is driven by class struggle over the means of production.",["Marx","Engels"]),
 ("Justice as Fairness","just","ana",1971,"Choose principles of justice from behind a 'veil of ignorance' about your place.",["Rawls"]),
 ("Power/Knowledge","just","con",1975,"Power and knowledge produce each other; discipline shapes the modern subject.",["Foucault"]),
 ("Legalism","just","chn",-250,"Order comes from strict, impartial law and clear rewards and punishments.",["Han Feizi"]),
 ("Government by Virtue","just","chn",-500,"Rulers should lead by moral example; the people follow virtue, not force.",["Confucius","Mencius"]),
 ("Mohist Universal Love","just","chn",-430,"Impartial concern for all yields the greatest social benefit.",["Mozi"]),
 ("Satyagraha","just","ind",1920,"Nonviolent resistance — truth-force — as a means of political change.",["Gandhi"]),

 # ---------- FREE WILL ----------
 ("Hard Determinism","free","enl",1770,"Every event is caused; free will is an illusion we cannot escape.",["d'Holbach"]),
 ("Libertarian Free Will","free","mod",1641,"We have genuine, undetermined freedom to choose otherwise.",["Descartes","Reid"]),
 ("Compatibilism","free","mod",1748,"Freedom is acting on your own desires — fully compatible with causation.",["Hume","Dennett"]),
 ("Amor Fati","free","hel",100,"Some things are up to us, some are not; love your fate and align your will.",["Epictetus","Nietzsche"]),
 ("Karma","free","ind",-700,"Acts bear fruit; you are bound by deeds yet morally responsible for them.",["Vedic thought"]),
 ("Pre-established Harmony","free","enl",1714,"Minds and bodies don't interact; God synchronized them in advance.",["Leibniz"]),
 ("Condemned to be Free","free","phe",1943,"We are 'condemned to be free' — radically responsible, with no excuses.",["Sartre"]),
 ("Eternal Recurrence","free","c19",1882,"Live as if you must relive each moment forever; will it, and be free.",["Nietzsche"]),
 ("Illusion of the Doer","free","ind",800,"The sense of being an independent agent is itself part of the illusion (maya).",["Shankara"]),

 # ---------- SUFFERING / LIBERATION ----------
 ("Four Noble Truths","peace","bud",-450,"Life involves suffering; its cause is craving; it can cease; a path leads out.",["The Buddha"]),
 ("Nirvana","peace","bud",-450,"The blowing-out of craving; liberation from the cycle of suffering.",["The Buddha"]),
 ("The Eightfold Path","peace","bud",-450,"A practical path — right view, intention, speech, action, and more — out of suffering.",["The Buddha"]),
 ("Non-Attachment","peace","bud",-450,"Suffering loosens its grip when we stop clinging to what changes.",["Buddhist & Yogic"]),
 ("Samsara & Moksha","peace","ind",-700,"Bound to a cycle of rebirth, the soul seeks moksha — release into the absolute.",["Vedanta"]),
 ("Stoic Apatheia","peace","hel",100,"Peace is freedom from destructive passions; master judgment, accept what is.",["Epictetus","Aurelius"]),
 ("Ataraxia","peace","hel",-300,"Tranquility — an unshakable calm — is the highest human good.",["Epicurus","Pyrrho"]),
 ("Denial of the Will","peace","c19",1818,"Life is suffering driven by blind Will; release comes from denying that will.",["Schopenhauer"]),
 ("The Absurd","peace","phe",1942,"Life has no given meaning; we find peace by revolting and living fully anyway.",["Camus"]),
 ("Logotherapy","peace","psy",1946,"We endure almost any 'how' if we have a 'why'; meaning is the antidote to despair.",["Frankl"]),
 ("Flow","peace","psy",1990,"Deepest well-being arrives in absorbed, skillful action for its own sake.",["Csikszentmihalyi"]),

 # ---------- THE ABSOLUTE ----------
 ("The Unmoved Mover","abs","grk",-350,"The chain of motion needs a first cause that moves all without itself moving.",["Aristotle"]),
 ("The One","abs","hel",250,"All reality emanates from a single ineffable source, 'the One,' and longs to return.",["Plotinus"]),
 ("The Ontological Argument","abs","med",1078,"God is that than which none greater can be conceived — so God must exist.",["Anselm"]),
 ("The Five Ways","abs","med",1265,"Five rational paths — from motion, cause, contingency — argue to God.",["Aquinas"]),
 ("Pantheism","abs","mod",1677,"God is not beyond the world; God is the world, 'Deus sive Natura.'",["Spinoza"]),
 ("Pascal's Wager","abs","mod",1670,"Reason can't settle God's existence, so weigh the bet — belief is the safer wager.",["Pascal"]),
 ("Via Negativa","abs","med",500,"The absolute is beyond words; we can say only what God is not.",["Pseudo-Dionysius"]),
 ("The Death of God","abs","c19",1882,"'God is dead' — the absolute foundation of values has collapsed; now what?",["Nietzsche"]),
 ("Non-Theistic Absolute","abs","bud",200,"Ultimate reality (emptiness) is no creator-God but the absence of fixed ground.",["Madhyamaka"]),
]

# ---- links between ideas: (a, b, type) ----
# builds  : a develops / extends b   (directed a -> b)
# rejects : a opposes / overturns b  (directed a -> b)
# echoes  : a and b strikingly converge across traditions (undirected)
R = [
 # reality debates
 ("Everything Flows","Being is One","rejects"),
 ("Process Reality","Everything Flows","builds"),
 ("Hylomorphism","Theory of Forms","rejects"),
 ("Materialism","Atomism","builds"),
 ("Materialism","Idealism","rejects"),
 ("Idealism","Materialism","rejects"),
 ("Absolute Idealism","Idealism","builds"),
 ("One Substance","Substance Dualism","rejects"),
 ("Pantheism","One Substance","builds"),
 ("Śūnyatā (Emptiness)","Dependent Origination","builds"),
 ("Śūnyatā (Emptiness)","Brahman","rejects"),
 ("Dependent Origination","Being is One","rejects"),
 ("The Dao","Brahman","echoes"),
 ("Process Reality","Everything Flows","echoes"),
 ("Process Reality","Dependent Origination","echoes"),
 ("Yin–Yang / Qi","Everything Flows","echoes"),
 # knowledge debates
 ("Empiricism","Rationalism","rejects"),
 ("Rationalism","Empiricism","rejects"),
 ("The Cogito","Rationalism","builds"),
 ("Tabula Rasa","Empiricism","builds"),
 ("Tabula Rasa","Theory of Forms","rejects"),
 ("Transcendental Idealism","Rationalism","builds"),
 ("Transcendental Idealism","Empiricism","builds"),
 ("Transcendental Idealism","Skepticism","rejects"),
 ("Skepticism","Rationalism","rejects"),
 ("Falsifiability","Verification Principle","rejects"),
 ("Paradigm Shifts","Falsifiability","rejects"),
 ("Verification Principle","Empiricism","builds"),
 ("Two Truths","Śūnyatā (Emptiness)","builds"),
 ("Anekāntavāda","Skepticism","echoes"),
 ("Pramāṇa","Empiricism","echoes"),
 ("Allegory of the Cave","Theory of Forms","builds"),
 # self debates
 ("Substance Dualism","The Immortal Soul","builds"),
 ("Anattā (No-Self)","Ātman = Brahman","rejects"),
 ("Bundle Theory","Substance Dualism","rejects"),
 ("Bundle Theory","Anattā (No-Self)","echoes"),
 ("Behaviorist Mind","The Unconscious","rejects"),
 ("Behaviorist Mind","Substance Dualism","rejects"),
 ("Functionalism","Behaviorist Mind","builds"),
 ("Collective Unconscious","The Unconscious","builds"),
 ("Existential Self","Substance Dualism","rejects"),
 ("Existential Self","Theory of Forms","rejects"),
 ("Being-in-the-World","Substance Dualism","rejects"),
 ("Being-in-the-World","Existential Self","echoes"),
 ("Relational Self","Substance Dualism","rejects"),
 ("Self-Actualization","The Unconscious","builds"),
 ("The Mirror Stage","The Unconscious","builds"),
 ("Anattā (No-Self)","The Immortal Soul","rejects"),
 # ethics debates
 ("The Golden Mean","Eudaimonia","builds"),
 ("Categorical Imperative","Utilitarianism","rejects"),
 ("Utilitarianism","Categorical Imperative","rejects"),
 ("Utilitarianism","Epicurean Pleasure","builds"),
 ("Stoic Virtue","Eudaimonia","builds"),
 ("Master & Slave Morality","Categorical Imperative","rejects"),
 ("Master & Slave Morality","Stoic Virtue","rejects"),
 ("Authenticity","Master & Slave Morality","builds"),
 ("Care Ethics","Categorical Imperative","rejects"),
 ("The Golden Mean","Ren & Li","echoes"),
 ("Wu Wei","Stoic Virtue","echoes"),
 ("Ren & Li","Government by Virtue","builds"),
 ("Ahimsa","Satyagraha","builds"),
 # society debates
 ("Leviathan","Social Contract","builds"),
 ("Natural Rights","Social Contract","builds"),
 ("The General Will","Social Contract","builds"),
 ("Natural Rights","Leviathan","rejects"),
 ("Historical Materialism","Absolute Idealism","rejects"),
 ("Historical Materialism","Natural Rights","rejects"),
 ("Justice as Fairness","Utilitarianism","rejects"),
 ("Justice as Fairness","Social Contract","builds"),
 ("Power/Knowledge","Justice as Fairness","rejects"),
 ("Legalism","Government by Virtue","rejects"),
 ("Mohist Universal Love","Ren & Li","rejects"),
 ("Mohist Universal Love","Utilitarianism","echoes"),
 ("Government by Virtue","Philosopher-Kings","echoes"),
 ("Satyagraha","Ahimsa","builds"),
 # free will debates
 ("Compatibilism","Hard Determinism","builds"),
 ("Compatibilism","Libertarian Free Will","builds"),
 ("Hard Determinism","Libertarian Free Will","rejects"),
 ("Libertarian Free Will","Hard Determinism","rejects"),
 ("Condemned to be Free","Hard Determinism","rejects"),
 ("Eternal Recurrence","Amor Fati","builds"),
 ("Amor Fati","Hard Determinism","echoes"),
 ("Illusion of the Doer","Hard Determinism","echoes"),
 ("Karma","Libertarian Free Will","echoes"),
 ("Pre-established Harmony","Hard Determinism","echoes"),
 # suffering / liberation
 ("Nirvana","Four Noble Truths","builds"),
 ("The Eightfold Path","Four Noble Truths","builds"),
 ("Non-Attachment","Four Noble Truths","builds"),
 ("Samsara & Moksha","Karma","builds"),
 ("Stoic Apatheia","Non-Attachment","echoes"),
 ("Ataraxia","Non-Attachment","echoes"),
 ("Ataraxia","Stoic Apatheia","echoes"),
 ("Denial of the Will","Non-Attachment","echoes"),
 ("Denial of the Will","Samsara & Moksha","echoes"),
 ("Denial of the Will","Brahman","builds"),
 ("The Absurd","The Death of God","builds"),
 ("Logotherapy","The Absurd","builds"),
 ("Flow","Self-Actualization","builds"),
 ("Flow","Wu Wei","echoes"),
 # the absolute
 ("The Five Ways","The Unmoved Mover","builds"),
 ("The Five Ways","The Ontological Argument","rejects"),
 ("Pantheism","The Unmoved Mover","rejects"),
 ("The One","The Unmoved Mover","builds"),
 ("Via Negativa","The One","builds"),
 ("Via Negativa","Non-Theistic Absolute","echoes"),
 ("The Death of God","The Five Ways","rejects"),
 ("Non-Theistic Absolute","Śūnyatā (Emptiness)","builds"),
 ("Non-Theistic Absolute","Brahman","rejects"),
 ("Brahman","The One","echoes"),
 ("Pascal's Wager","The Five Ways","rejects"),
 # cross-question bridges (idea ↔ idea across problems)
 ("Denial of the Will","Idealism","builds"),
 ("Historical Materialism","Materialism","builds"),
 ("The Death of God","Master & Slave Morality","echoes"),
 ("Self-Actualization","Eudaimonia","echoes"),
 ("Being-in-the-World","Process Reality","echoes"),
 ("Monadology","Idealism","builds"),
 ("Pre-established Harmony","Monadology","builds"),
 ("Monadology","One Substance","rejects"),
]

# ===================== build & validate =====================
# "Contested" is scoped to claims presented in the register of established empirical
# science that nonetheless lack consensus. It is deliberately NOT applied to doctrinal
# or metaphysical truth-claims (religious or esoteric) — those are disclosed by their
# tradition badge instead, so the tag fires the same way across every tradition.
CONTESTED = {"Integrated Information","The Ego Tunnel","Analytic Idealism","The Case Against Reality","The Readiness Potential","Global Workspace"}

# "Practice" marks a concept carried by a real exercise you *perform* — a discipline,
# not only a thesis you assert. The criterion is the tradition's practice, not the
# gloss's grammar: it fires even where a concept is phrased doctrinally (the Stoic
# entries name Hadot's askēsis — the dichotomy of control, the view from above), so
# the West's practice-philosophy is not flattened into mere doctrine. The sole
# principled exclusion is a path that rejects method by definition (Choiceless
# Awareness). This restores the method/doctrine distinction the atlas otherwise loses.
PRACTICE = {
    "Hesychasm (The Jesus Prayer)","The Spiritual Exercises","Dzogchen (The Great Perfection)",
    "The Four Foundations of Mindfulness","Dhikr (Remembrance)","The Eightfold Path",
    "Mindfulness (MBSR)","Yoga: Stilling the Mind","Self-Cultivation","Sitting in Forgetting",
    "Ren & Li","Sudden Enlightenment, Gradual Cultivation","Stoic Virtue","Stoic Apatheia",
    "Amor Fati","Wu Wei","The Examined Life","Attention & Unselfing","Engaged Buddhism",
    "Non-Attachment",
}

def main():
    qids = {q[0] for q in QUESTIONS}
    qhue = {q[0]: q[2] for q in QUESTIONS}
    concepts = []
    seen = set()
    for cid, qid, trad, era, gloss, thinkers in C:
        if cid in seen:
            raise SystemExit(f"DUPLICATE concept id: {cid}")
        seen.add(cid)
        if qid not in qids:
            raise SystemExit(f"BAD question id {qid} on {cid}")
        concepts.append({
            "id": cid, "q": qid, "trad": trad, "tradLabel": TRAD.get(trad, trad),
            "era": era, "gloss": gloss, "thinkers": thinkers, "color": qhue[qid],
            "contested": cid in CONTESTED,
            "practice": cid in PRACTICE,
        })

    ids = {c["id"] for c in concepts}

    # validate links
    miss = set()
    links = []
    for a, b, t in R:
        if a not in ids: miss.add(a)
        if b not in ids: miss.add(b)
        links.append({"source": a, "target": b, "type": t})
    if miss:
        raise SystemExit("MISSING concept ids in links: " + ", ".join(sorted(miss)))

    # degree
    deg = {c["id"]: 0 for c in concepts}
    for l in links:
        deg[l["source"]] += 1
        deg[l["target"]] += 1
    for c in concepts:
        c["deg"] = deg[c["id"]]

    out = {
        "questions": [{"id": q[0], "label": q[1], "hue": q[2], "framing": q[3],
                       "status": STATUS[q[0]][0], "statusResidue": STATUS[q[0]][1],
                       "statusConf": STATUS[q[0]][2], "statusWhy": STATUS[q[0]][3]} for q in QUESTIONS],
        "concepts": concepts,
        "links": links,
    }
    with open("ideas.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)

    import collections
    by_t = collections.Counter(l["type"] for l in links)
    by_q = collections.Counter(c["q"] for c in concepts)
    print(f"Concepts: {len(concepts)}  Links: {len(links)}")
    print("Link types:", dict(by_t))
    print("Per question:", dict(by_q))
    iso = [c["id"] for c in concepts if deg[c["id"]] == 0]
    print("Isolates:", iso if iso else "none")

if __name__ == "__main__":
    main()
