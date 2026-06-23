# -*- coding: utf-8 -*-
"""Round-three additions, addressing the panel's two data defects:
  • the missing counter-pole — the serious case FOR engagement, relation and care
  • the 2.2% women problem
These are defect-fixes, not open-ended growth; after this the dataset freezes."""
import concepts
import expand    # round one
import expand2   # round two

concepts.TRAD.update({"fem":"Feminist & Care Ethics", "eth":"Ethics"})

NEW_C3 = [
 ("The Face of the Other","self","phe",1961,"Ethics begins in the face of the Other — an infinite claim that comes before the self.",["Emmanuel Levinas"]),
 ("I and Thou","self","phe",1923,"Two ways of meeting the world: the detached I–It, or the whole-hearted I–Thou.",["Martin Buber"]),
 ("Attention & Unselfing","live","eth",1970,"Goodness as the patient, loving attention that unselfs us before the real.",["Iris Murdoch","Simone Weil"]),
 ("The Capabilities Approach","just","eth",2000,"Justice measured by what people are actually able to do and to be.",["Martha Nussbaum","Amartya Sen"]),
 ("Modern Virtue Ethics","live","ana",1958,"The twentieth-century revival of character over rules and consequences.",["G.E.M. Anscombe","Philippa Foot","Alasdair MacIntyre"]),
 ("Engaged Buddhism","just","bud",1965,"Compassion turned outward — meditation in the service of the suffering world.",["Thich Nhat Hanh","B.R. Ambedkar"]),
]
concepts.C.extend(NEW_C3)

NEW_R3 = [
 ("The Face of the Other","Existential Self","builds"),
 ("The Face of the Other","I and Thou","echoes"),
 ("The Face of the Other","Being-toward-Death","rejects"),
 ("The Face of the Other","Cynic Self-Sufficiency","rejects"),
 ("I and Thou","The Presentation of Self","rejects"),
 ("I and Thou","To Have or To Be","echoes"),
 ("I and Thou","Brahman","echoes"),
  ("Care Ethics","Justice as Fairness","rejects"),
 ("Care Ethics","Ren & Li","echoes"),
 ("Care Ethics","Existential Self","builds"),
 ("Attention & Unselfing","Anattā (No-Self)","echoes"),
 ("Attention & Unselfing","Society of the Spectacle","rejects"),
 ("Attention & Unselfing","Wu Wei","echoes"),
 ("Attention & Unselfing","The Extinction of Experience","echoes"),
 ("The Capabilities Approach","Justice as Fairness","builds"),
 ("The Capabilities Approach","Utilitarianism","rejects"),
 ("The Capabilities Approach","Eudaimonia","builds"),
 ("Modern Virtue Ethics","The Golden Mean","builds"),
 ("Modern Virtue Ethics","Eudaimonia","builds"),
 ("Modern Virtue Ethics","Categorical Imperative","rejects"),
 ("Modern Virtue Ethics","Utilitarianism","rejects"),
 ("Engaged Buddhism","Four Noble Truths","builds"),
 ("Engaged Buddhism","Non-Attachment","rejects"),
 ("Engaged Buddhism","The Human Condition","echoes"),
]
concepts.R.extend(NEW_R3)

concepts.main()
