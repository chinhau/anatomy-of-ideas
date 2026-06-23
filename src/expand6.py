# -*- coding: utf-8 -*-
"""Round-six expansion: the clean tier of Korean thought.

Korea is its own current within East Asian philosophy, not a footnote to
China — the Four-Seven Debate is one of the most sustained arguments in the
history of moral psychology, and Wŏnhyo and Jinul are major Buddhist
philosophers in their own right. As with round five, every concept names a
real author and a real, dated text. Korean trads join the existing **East**
timeline lane (alongside Indian/Buddhist/Chinese/Japanese).

Imports `expand5` (rounds 1-5, already rebuilt) and extends, then rebuilds.
"""
import concepts
import expand    # round one
import expand2   # round two
import expand3   # round three
import expand4   # round four
import expand5   # round five

concepts.TRAD.update({"kor": "Korean"})

# ---- the clean tier: (id, qid, trad, era, gloss, thinkers) ----
NEW_C6 = [
 ("The Four-Seven Debate","mind","kor",1568,"Do the moral feelings spring from principle and the raw passions from matter? Korea's central argument on the sources of the heart.",["Yi Hwang (Toegye)"]),
 ("Principle Rides on Force","real","kor",1575,"Principle never moves on its own; it rides on the material force that alone acts — the two forever inseparable.",["Yi I (Yulgok)"]),
 ("Hwajaeng (Reconciling Disputes)","know","kor",671,"Each school grasps a corner of the truth; wisdom harmonizes their quarrels back into one mind.",["Wŏnhyo"]),
 ("Sudden Enlightenment, Gradual Cultivation","trans","kor",1205,"Awakening breaks open in an instant, but old habits wear away only slowly; insight and practice complete each other.",["Jinul"]),
 ("In Is Heaven (Innaecheon)","just","kor",1860,"Every person bears Heaven within; to serve another human being is to serve the divine — and all are equal in it.",["Choe Je-u"]),
]
concepts.C.extend(NEW_C6)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R6 = [
 ("The Four-Seven Debate","Ren & Li","builds"),
 ("The Four-Seven Debate","Self-Cultivation","echoes"),
 ("Principle Rides on Force","The Four-Seven Debate","rejects"),
 ("Principle Rides on Force","Yin–Yang / Qi","echoes"),
 ("Principle Rides on Force","The Dao","echoes"),
 ("Hwajaeng (Reconciling Disputes)","Anekāntavāda","echoes"),
 ("Hwajaeng (Reconciling Disputes)","Two Truths","builds"),
 ("Hwajaeng (Reconciling Disputes)","Śūnyatā (Emptiness)","echoes"),
 ("Sudden Enlightenment, Gradual Cultivation","Sudden Awakening","builds"),
 ("Sudden Enlightenment, Gradual Cultivation","Self-Cultivation","echoes"),
 ("Sudden Enlightenment, Gradual Cultivation","The Eightfold Path","echoes"),
 ("In Is Heaven (Innaecheon)","Mohist Universal Love","echoes"),
 ("In Is Heaven (Innaecheon)","Ātman = Brahman","echoes"),
 ("In Is Heaven (Innaecheon)","Engaged Buddhism","echoes"),
]
concepts.R.extend(NEW_R6)

concepts.main()
