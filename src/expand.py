# -*- coding: utf-8 -*-
"""Augments the base concept dataset with the gaps surfaced by the doc audit:
new questions (mind / meaning / transformation), consciousness studies,
Islamic & mystical thought, cognitive science, systems, James, Wittgenstein,
Daoist consciousness, yoga, the CBT/mindfulness lineage, Darwin, Machiavelli."""

import concepts

# ---- new tradition badges ----
concepts.TRAD.update({
    "isl":"Islamic Golden Age", "cog":"Cognitive Science",
    "sci":"Science", "sys":"Systems & Cybernetics", "csn":"Consciousness Studies",
})

# ---- reorder questions and insert the three new ones ----
NEWQ = {
    "mind":  ("mind","How does the mind work?","#4F9DE0","Mind & consciousness — perception, cognition, awareness."),
    "mean":  ("mean","What makes life worth living?","#E0913D","Meaning — purpose, value, what matters."),
    "trans": ("trans","How do we transform?","#C75DBA","Transformation — how minds change, heal, and awaken."),
}
order = ["real","know","mind","self","live","just","free","peace","mean","trans","abs"]
base = {q[0]: q for q in concepts.QUESTIONS}
base.update(NEWQ)
concepts.QUESTIONS[:] = [base[k] for k in order]

# ---- reassign two existing concepts to the meaning question ----
concepts.C[:] = [t if t[0] not in ("Logotherapy","Flow") else (t[0],"mean",*t[2:])
                 for t in concepts.C]

# ---- new concepts: (id, q, trad, era, gloss, thinkers) ----
NEW_C = [
 # ---- MIND / CONSCIOUSNESS ----
 ("Stream of Consciousness","mind","psy",1890,"Consciousness is not a chain of links but a continuous, flowing river.",["William James"]),
 ("The Hard Problem","mind","csn",1995,"Why is there any felt experience at all? Why isn't it all dark inside?",["David Chalmers"]),
 ("What It Is Like","mind","csn",1974,"A state is conscious if there is something it is like to be in it.",["Thomas Nagel"]),
 ("Panpsychism","mind","csn",1929,"Mind goes all the way down; experience is a basic feature of matter.",["Whitehead","Chalmers"]),
 ("Integrated Information","mind","csn",2004,"Tononi's theory: consciousness is integrated information — the more a system unifies, the more, it proposes, it feels.",["Tononi","Koch"]),
 ("The Intentional Stance","mind","cog",1987,"Predict a mind by treating it as a rational agent with beliefs and desires.",["Daniel Dennett"]),
 ("Strange Loop","mind","cog",1979,"The 'I' is a self-referential loop the brain spins up to model itself.",["Douglas Hofstadter"]),
 ("The Embodied Mind","mind","csn",1991,"Cognition is enacted by a living body coping with its world, not computed in the skull.",["Varela","Thompson"]),
 ("Universal Grammar","mind","cog",1965,"We are born with a deep grammar; language unfolds, it isn't merely learned.",["Noam Chomsky"]),
 ("Dual-Process Mind","mind","cog",2011,"Two systems think for us — one fast and intuitive, one slow and deliberate.",["Daniel Kahneman"]),
 ("Neutral Monism","mind","ana",1921,"Mind and matter are two arrangements of one neutral, more basic stuff.",["Russell","James"]),
 ("Developmental Stages","mind","cog",1936,"The child's mind builds reality through distinct stages of growth.",["Jean Piaget"]),
 ("Cybernetics & Feedback","mind","sys",1948,"Minds and machines alike steer by loops of feedback and correction.",["Norbert Wiener"]),
 ("The Butterfly Dream","mind","chn",-300,"Am I a man who dreamt he was a butterfly, or a butterfly dreaming he is a man?",["Zhuangzi"]),
 # ---- MEANING ----
 ("Meaning Is Created","mean","phe",1946,"No meaning is handed down; we forge it through our choices and projects.",["Sartre","Camus"]),
 ("Inherent Purpose (Telos)","mean","grk",-340,"Each thing has a telos, an end it is for; the good life fulfils ours.",["Aristotle"]),
 ("Ikigai","mean","jpn",1960,"A 'reason for being' — the daily sense that life is worth waking for.",["Japanese tradition"]),
 ("Positive Psychology","mean","psy",1998,"Study not only illness but flourishing — engagement, relationship, meaning.",["Martin Seligman"]),
 ("The Examined Life","mean","grk",-399,"'The unexamined life is not worth living' — meaning through self-scrutiny.",["Socrates"]),
 # ---- TRANSFORMATION ----
 ("Cognitive Behavioral Therapy","trans","psy",1960,"Change the thought and you change the feeling; rework distorted beliefs.",["Aaron Beck","Albert Ellis"]),
 ("Mindfulness (MBSR)","trans","psy",1979,"Non-judgmental present-moment awareness, carried from Buddhism into medicine.",["Jon Kabat-Zinn"]),
 ("Acceptance & Commitment","trans","psy",1986,"Stop struggling with inner experience; accept it and act on your values.",["Steven Hayes"]),
 ("Individuation","trans","psy",1921,"Becoming whole by integrating the shadow and the unconscious into the self.",["Carl Jung"]),
 ("Yoga: Stilling the Mind","trans","ind",200,"Yoga is the stilling of the mind's fluctuations, freeing pure awareness.",["Patañjali"]),
 ("Sudden Awakening","trans","bud",700,"Enlightenment is not earned by degrees but breaks open all at once.",["Huineng","Linji"]),
 ("Self-Cultivation","trans","chn",1500,"The mind already knows the good; growth is polishing that knowing into action.",["Wang Yangming"]),
 ("Integral Theory","trans","csn",1995,"Map human growth across stages, states and perspectives all at once.",["Ken Wilber"]),
 ("Mystical Union (Fana)","trans","isl",1250,"The self dissolves; lover and Beloved become one.",["Rumi","Ibn Arabi"]),
 # ---- ISLAMIC & MYSTICAL, plus other gaps ----
 ("Unity of Being","abs","isl",1230,"All that exists is one divine reality; creation is God's self-disclosure.",["Ibn Arabi"]),
 ("The Flying Man","self","isl",1020,"Floating, senseless, you would still know you exist — the self is no mere body.",["Avicenna"]),
 ("Faith Beyond Reason","know","isl",1095,"Reason cannot reach the deepest truths; even cause and effect rest on God's will.",["Al-Ghazali"]),
 ("Language Games","know","ana",1953,"Words mean by their use in forms of life, not by mirroring the world.",["Ludwig Wittgenstein"]),
 ("Pragmatism","know","pra",1907,"True ideas are the ones that work — that pay their way in experience.",["William James","Dewey"]),
 ("Evolution by Natural Selection","real","sci",1859,"Design without a designer: life's complexity from variation and selection.",["Charles Darwin"]),
 ("Political Realism","just","mod",1532,"Politics runs on power, not piety; the prince must master fortune and force.",["Machiavelli"]),
 ("Qualified Non-Dualism","abs","ind",1100,"World and souls are real parts of God — one, yet not featureless.",["Ramanuja"]),
]
concepts.C.extend(NEW_C)

# ---- new links ----
L = lambda a,b,t: (a,b,t)
NEW_R = [
 # mind cluster
 ("The Hard Problem","What It Is Like","builds"),
 ("The Hard Problem","Materialism","rejects"),
 ("The Hard Problem","Functionalism","rejects"),
 ("Panpsychism","Process Reality","builds"),
 ("Panpsychism","Materialism","rejects"),
 ("Panpsychism","Neutral Monism","echoes"),
 ("Integrated Information","The Hard Problem","builds"),
 ("The Intentional Stance","Functionalism","builds"),
 ("The Intentional Stance","The Hard Problem","rejects"),
 ("Strange Loop","Functionalism","builds"),
 ("Strange Loop","Anattā (No-Self)","echoes"),
 ("Strange Loop","Bundle Theory","echoes"),
 ("The Embodied Mind","Being-in-the-World","builds"),
 ("The Embodied Mind","Substance Dualism","rejects"),
 ("The Embodied Mind","Dependent Origination","echoes"),
 ("Universal Grammar","Tabula Rasa","rejects"),
 ("Universal Grammar","Behaviorist Mind","rejects"),
 ("Developmental Stages","Universal Grammar","rejects"),
 ("Dual-Process Mind","The Unconscious","echoes"),
 ("Neutral Monism","One Substance","builds"),
 ("Neutral Monism","Substance Dualism","rejects"),
 ("Cybernetics & Feedback","Functionalism","builds"),
 ("Cybernetics & Feedback","Process Reality","echoes"),
 ("Stream of Consciousness","Empiricism","builds"),
 ("Stream of Consciousness","Everything Flows","echoes"),
 ("Stream of Consciousness","Pragmatism","builds"),
 ("The Butterfly Dream","The Dao","builds"),
 ("The Butterfly Dream","The Cogito","echoes"),
 ("The Butterfly Dream","Skepticism","echoes"),
 # meaning cluster
 ("Meaning Is Created","The Absurd","builds"),
 ("Meaning Is Created","Existential Self","builds"),
 ("Meaning Is Created","Inherent Purpose (Telos)","rejects"),
 ("Inherent Purpose (Telos)","Eudaimonia","builds"),
 ("Inherent Purpose (Telos)","The Unmoved Mover","echoes"),
 ("Ikigai","Eudaimonia","echoes"),
 ("Ikigai","Flow","echoes"),
 ("Positive Psychology","Self-Actualization","builds"),
 ("Positive Psychology","Flow","builds"),
 ("Positive Psychology","Eudaimonia","echoes"),
 ("Stoic Virtue","The Examined Life","builds"),
 ("The Examined Life","Allegory of the Cave","echoes"),
 ("Logotherapy","Meaning Is Created","echoes"),
 # transformation cluster
 ("Cognitive Behavioral Therapy","Stoic Virtue","builds"),
 ("Cognitive Behavioral Therapy","The Unconscious","rejects"),
 ("Cognitive Behavioral Therapy","Stoic Apatheia","builds"),
 ("Mindfulness (MBSR)","Non-Attachment","builds"),
 ("Mindfulness (MBSR)","The Eightfold Path","builds"),
 ("Mindfulness (MBSR)","Stoic Apatheia","echoes"),
 ("Acceptance & Commitment","Mindfulness (MBSR)","builds"),
 ("Acceptance & Commitment","Non-Attachment","builds"),
 ("Individuation","Collective Unconscious","builds"),
 ("Individuation","Self-Actualization","echoes"),
 ("Individuation","Samsara & Moksha","echoes"),
 ("Yoga: Stilling the Mind","Samsara & Moksha","builds"),
 ("Yoga: Stilling the Mind","Non-Attachment","builds"),
 ("Yoga: Stilling the Mind","Mindfulness (MBSR)","echoes"),
 ("Sudden Awakening","Nirvana","builds"),
 ("Sudden Awakening","Wu Wei","echoes"),
 ("Self-Cultivation","Ren & Li","builds"),
 ("Self-Cultivation","Relational Self","builds"),
 ("Integral Theory","Self-Actualization","builds"),
 ("Integral Theory","Developmental Stages","builds"),
 ("Integral Theory","Absolute Idealism","echoes"),
 ("Mystical Union (Fana)","Unity of Being","builds"),
 ("Mystical Union (Fana)","Brahman","echoes"),
 ("Mystical Union (Fana)","Nirvana","echoes"),
 # islamic / mystical / other
 ("Unity of Being","The One","builds"),
 ("Unity of Being","Brahman","echoes"),
 ("Unity of Being","Pantheism","echoes"),
 ("The Flying Man","Substance Dualism","echoes"),
 ("The Flying Man","The Cogito","echoes"),
 ("Faith Beyond Reason","Rationalism","rejects"),
 ("Faith Beyond Reason","The Unmoved Mover","rejects"),
 ("Faith Beyond Reason","Pascal's Wager","echoes"),
 ("Language Games","Verification Principle","rejects"),
 ("Language Games","Theory of Forms","rejects"),
 ("Language Games","Pragmatism","echoes"),
 ("Pragmatism","Empiricism","builds"),
 ("Pragmatism","Rationalism","rejects"),
 ("Pragmatism","Falsifiability","echoes"),
 ("Evolution by Natural Selection","Materialism","builds"),
 ("Evolution by Natural Selection","Inherent Purpose (Telos)","rejects"),
 ("Evolution by Natural Selection","Process Reality","echoes"),
 ("Political Realism","Philosopher-Kings","rejects"),
 ("Political Realism","Government by Virtue","rejects"),
 ("Political Realism","Leviathan","builds"),
 ("Qualified Non-Dualism","Brahman","builds"),
 ("Qualified Non-Dualism","Ātman = Brahman","rejects"),
]
concepts.R.extend(NEW_R)

# ---- new dialectical arguments ----
NEW_ARG = [
 {"title":"What Is Consciousness?","note":"The defining puzzle of modern mind science.",
  "steps":[("Materialism","thesis"),("The Hard Problem","antithesis"),
           ("Panpsychism","response"),("The Embodied Mind","synthesis")]},
 {"title":"Where Does Meaning Come From?","note":"Given, or made by us?",
  "steps":[("Inherent Purpose (Telos)","thesis"),("The Death of God","antithesis"),
           ("Meaning Is Created","response"),("Logotherapy","synthesis")]},
 {"title":"How Do We Change?","note":"Three routes to transforming a mind.",
  "steps":[("Behaviorist Mind","thesis"),("Cognitive Behavioral Therapy","antithesis"),
           ("Mindfulness (MBSR)","synthesis")]},
 {"title":"Innate or Learned?","note":"Where does the mind's structure come from?",
  "steps":[("Tabula Rasa","thesis"),("Universal Grammar","antithesis"),
           ("Developmental Stages","synthesis")]},
]
concepts.ARG.extend(NEW_ARG)

# ---- build & validate (reuses concepts.main on the mutated globals) ----
concepts.main()
