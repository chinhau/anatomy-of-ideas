# -*- coding: utf-8 -*-
"""Round-two expansion driven by the book-briefing audit:
  • The Performance Trap (the critique-of-modern-life cluster the map lacked)
  • The Withdrawal lineage (the positive content of 'graceful refusal')
  • Death-facing (Ch7's frontier)
  • The latest voices, 20th–21st century through 2024
Imports `expand` (which has already applied round one) and extends further."""

import concepts
import expand  # applies round-one additions and rebuilds once

concepts.TRAD.update({
    "crt":"Critical Theory", "soc":"Sociology", "amr":"American Transcendentalism",
})

NEW_C2 = [
 # ---- THE PERFORMANCE TRAP ----
 ("Society of the Spectacle","just","crt",1967,"Modern life is mediated by images; we watch representations where we once lived.",["Guy Debord"]),
 ("The Burnout Society","just","crt",2010,"No longer disciplined from outside, we exploit ourselves — and call it freedom.",["Byung-Chul Han"]),
 ("The Presentation of Self","self","soc",1956,"Everyday life is theatre; the self is a performance staged for an audience.",["Erving Goffman"]),
 ("Simulacra & Hyperreality","real","crt",1981,"Copies without originals; the map has replaced the territory.",["Jean Baudrillard"]),
 ("One-Dimensional Man","just","crt",1964,"Consumer society manufactures false needs and quietly absorbs all dissent.",["Herbert Marcuse"]),
 ("Capitalist Realism","just","crt",2009,"It is easier to imagine the end of the world than the end of capitalism.",["Mark Fisher"]),
 ("Bullshit Jobs","just","soc",2018,"Whole careers feel pointless — work as moral and social performance.",["David Graeber"]),
 ("The Human Condition","just","phe",1958,"Labour, work and action — and the modern eclipse of public life by mere making.",["Hannah Arendt"]),
 # ---- THE WITHDRAWAL LINEAGE ----
 ("Cynic Self-Sufficiency","live","hel",-350,"Strip wants to the bone, owe society nothing, be free as a dog in the sun.",["Diogenes"]),
 ("Live Unnoticed","live","hel",-300,"'Lathe biōsas' — live unnoticed; step out of the race for status.",["Epicurus"]),
 ("Self-Reliance","live","amr",1841,"Trust the self over the crowd; withdraw to nature to hear your own voice.",["Ralph Waldo Emerson"]),
 ("Sitting in Forgetting","trans","chn",-300,"Zuowang — 'sit and forget' body and mind until you merge with the Way.",["Zhuangzi"]),
 ("To Have or To Be","mean","psy",1976,"Two modes of living: grasping at having, or simply being.",["Erich Fromm"]),
 # ---- DEATH-FACING ----
 ("Being-toward-Death","peace","phe",1927,"Facing one's own death calls a life back from the crowd into authenticity.",["Martin Heidegger"]),
 ("The Denial of Death","peace","psy",1973,"Civilization is a vast defense mechanism against the terror of mortality.",["Ernest Becker"]),
 ("The Art of Dying","trans","bud",1350,"Death as a passage to be met with awareness — the bardo between lives.",["Karma Lingpa","Padmasambhava (attrib.)"]),
 # ---- THE LATEST VOICES (20th–21st c. → 2024) ----
 ("The Chinese Room","mind","ana",1980,"Running a program is not understanding; syntax never adds up to meaning.",["John Searle"]),
 ("The Ego Tunnel","self","csn",2009,"Metzinger argues no one ever had a self — only a transparent model the brain mistakes for one.",["Thomas Metzinger"]),
 ("Controlled Hallucination","mind","cog",2021,"Perception is the brain's best guess — a hallucination reined in by the senses.",["Anil Seth","Andy Clark"]),
 ("Global Workspace","mind","cog",1988,"Consciousness is information broadcast to the whole brain from a central stage.",["Bernard Baars","Stanislas Dehaene"]),
 ("Identity Is Not What Matters","self","ana",1984,"What matters is psychological continuity, not a deep further fact of 'me'.",["Derek Parfit"]),
 ("Analytic Idealism","real","csn",2019,"On Kastrup's idealism, reality is fundamentally mental; matter is how mind looks from outside.",["Bernardo Kastrup"]),
 ("The Case Against Reality","know","cog",2019,"Hoffman's interface theory: evolution tuned perception for fitness, not truth, so spacetime may be just our interface.",["Donald Hoffman"]),
 ("The Divided Brain","mind","cog",2009,"The hemispheres offer two ways of attending to the world — and ours is unbalanced.",["Iain McGilchrist"]),
 ("Shared Fictions","just","soc",2011,"Money, nations and rights are stories — fictions that let strangers cooperate.",["Yuval Noah Harari"]),
 ("Gender Performativity","self","crt",1990,"Gender is not what you are but what you repeatedly do — an act with no actor behind it.",["Judith Butler"]),
 ("Choiceless Awareness","trans","ind",1954,"Freedom is observing without the observer — no method, no path, no guru.",["Jiddu Krishnamurti"]),
 ("The Readiness Potential","free","cog",1983,"The brain stirs before we feel we 'decided' — though whether that dooms free will is disputed, as Schurger reads it as mere noise accumulating.",["Benjamin Libet"]),
 ("The Extinction of Experience","self","soc",2024,"Screen-life thins out embodied, face-to-face experience and the self it grew.",["Christine Rosen"]),
]
concepts.C.extend(NEW_C2)

NEW_R2 = [
 # performance trap
 ("The Burnout Society","Power/Knowledge","builds"),
 ("The Burnout Society","One-Dimensional Man","echoes"),
 ("Society of the Spectacle","Historical Materialism","builds"),
 ("Society of the Spectacle","Allegory of the Cave","echoes"),
 ("Society of the Spectacle","Simulacra & Hyperreality","echoes"),
 ("The Presentation of Self","Society of the Spectacle","echoes"),
 ("Simulacra & Hyperreality","Society of the Spectacle","builds"),
 ("Simulacra & Hyperreality","Allegory of the Cave","echoes"),
 ("Simulacra & Hyperreality","Idealism","echoes"),
 ("One-Dimensional Man","Historical Materialism","builds"),
 ("One-Dimensional Man","Power/Knowledge","echoes"),
 ("Capitalist Realism","One-Dimensional Man","builds"),
 ("Capitalist Realism","The Burnout Society","echoes"),
 ("Bullshit Jobs","Capitalist Realism","echoes"),
 ("Bullshit Jobs","Historical Materialism","builds"),
 ("The Human Condition","Historical Materialism","rejects"),
 ("The Human Condition","Bullshit Jobs","echoes"),
 ("The Human Condition","Philosopher-Kings","echoes"),
 ("Gender Performativity","Power/Knowledge","builds"),
 ("Gender Performativity","Existential Self","builds"),
 ("Gender Performativity","The Presentation of Self","echoes"),
 # withdrawal
 ("Stoic Virtue","Cynic Self-Sufficiency","builds"),
 ("Cynic Self-Sufficiency","Wu Wei","echoes"),
 ("Cynic Self-Sufficiency","Political Realism","rejects"),
 ("Live Unnoticed","Epicurean Pleasure","builds"),
 ("Live Unnoticed","Ataraxia","builds"),
 ("Live Unnoticed","Cynic Self-Sufficiency","echoes"),
 ("Self-Reliance","Cynic Self-Sufficiency","echoes"),
 ("Self-Reliance","Brahman","echoes"),
 ("Self-Reliance","Authenticity","echoes"),
 ("Sitting in Forgetting","The Dao","builds"),
 ("Sitting in Forgetting","Wu Wei","builds"),
 ("Sitting in Forgetting","Anattā (No-Self)","echoes"),
 ("Sitting in Forgetting","Yoga: Stilling the Mind","echoes"),
 ("To Have or To Be","Non-Attachment","builds"),
 ("To Have or To Be","The Burnout Society","echoes"),
 ("To Have or To Be","The Unconscious","builds"),
 # death
 ("Being-toward-Death","Being-in-the-World","builds"),
 ("Being-toward-Death","Authenticity","builds"),
 ("Being-toward-Death","Stoic Virtue","echoes"),
 ("The Denial of Death","Being-toward-Death","builds"),
 ("The Denial of Death","The Unconscious","builds"),
 ("The Denial of Death","The Absurd","echoes"),
 ("The Art of Dying","Samsara & Moksha","builds"),
 ("The Art of Dying","Nirvana","builds"),
 ("The Art of Dying","Being-toward-Death","echoes"),
 # latest / consciousness
 ("The Chinese Room","Functionalism","rejects"),
 ("The Chinese Room","The Intentional Stance","rejects"),
 ("The Chinese Room","The Hard Problem","echoes"),
 ("The Ego Tunnel","Strange Loop","builds"),
 ("The Ego Tunnel","Anattā (No-Self)","echoes"),
 ("The Ego Tunnel","Bundle Theory","echoes"),
 ("Controlled Hallucination","The Embodied Mind","builds"),
 ("Controlled Hallucination","Transcendental Idealism","builds"),
 ("Controlled Hallucination","Idealism","echoes"),
 ("Controlled Hallucination","Global Workspace","echoes"),
 ("Global Workspace","Integrated Information","echoes"),
 ("Global Workspace","The Hard Problem","rejects"),
 ("Identity Is Not What Matters","Bundle Theory","builds"),
 ("Identity Is Not What Matters","Anattā (No-Self)","echoes"),
 ("Analytic Idealism","Idealism","builds"),
 ("Analytic Idealism","Panpsychism","builds"),
 ("Analytic Idealism","Materialism","rejects"),
 ("Analytic Idealism","Brahman","echoes"),
 ("The Case Against Reality","Transcendental Idealism","builds"),
 ("The Case Against Reality","Evolution by Natural Selection","builds"),
 ("The Case Against Reality","Controlled Hallucination","echoes"),
 ("The Divided Brain","Dual-Process Mind","builds"),
 ("The Divided Brain","Yin–Yang / Qi","echoes"),
 ("Shared Fictions","Social Contract","builds"),
 ("Shared Fictions","Society of the Spectacle","echoes"),
 ("Shared Fictions","Language Games","echoes"),
 ("Choiceless Awareness","Anattā (No-Self)","echoes"),
 ("Choiceless Awareness","Yoga: Stilling the Mind","rejects"),
 ("Choiceless Awareness","Sudden Awakening","echoes"),
 ("The Readiness Potential","Libertarian Free Will","rejects"),
 ("The Readiness Potential","Hard Determinism","builds"),
 ("The Readiness Potential","Illusion of the Doer","echoes"),
 ("The Extinction of Experience","The Embodied Mind","builds"),
 ("The Extinction of Experience","Society of the Spectacle","echoes"),
 ("The Extinction of Experience","The Burnout Society","echoes"),
]
concepts.R.extend(NEW_R2)

concepts.main()
