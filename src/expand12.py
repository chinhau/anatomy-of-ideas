# -*- coding: utf-8 -*-
"""Round-twelve expansion: the core backfill.

A multi-agent critique pass found the atlas had drifted — eleven rounds of adding
world-traditions and contemplative practice had masked glaring holes in the
bread-and-butter analytic, epistemological, and political canon, and had left the
'free', 'mean', and 'peace' questions thin and inward-tilted. This round backfills
thirteen load-bearing ideas a philosophy-literate visitor would be shocked to find
absent: the Gettier problem, the problem of induction, the problem of evil, Berlin's
two liberties, Mill's harm principle, Nozick, Singer, Weber's iron cage, Du Bois's
double consciousness, Quine, the Turing test, Jackson's knowledge argument, and
liberation theology (suffering as injustice-to-be-fought, not only borne).

No new badges — all reuse existing tradition codes. Imports expand11 and rebuilds.
"""
import concepts
import expand, expand2, expand3, expand4, expand5, expand6
import expand7, expand8, expand9, expand10, expand11

# ---- the backfill: (id, qid, trad, era, gloss, thinkers) ----
NEW_C12 = [
 ("The Gettier Problem","know","ana",1963,"Justified true belief can still fail to be knowledge: you can be right for the wrong reasons, by luck.",["Edmund Gettier"]),
 ("The Problem of Induction","know","enl",1748,"No number of past observations logically guarantees the future; the sunrise we expect rests on habit, not proof.",["David Hume","Nelson Goodman"]),
 ("The Problem of Evil","abs","enl",1779,"If God is all-good and all-powerful, why is there suffering? The oldest argument against a benevolent Absolute.",["Epicurus","David Hume","J. L. Mackie"]),
 ("Two Concepts of Liberty","free","ana",1958,"Freedom-from (no one coercing me) versus freedom-to (mastering myself) — and the warning that 'positive' liberty can license tyranny.",["Isaiah Berlin"]),
 ("The Harm Principle","just","c19",1859,"The only ground for coercing anyone against their will is to prevent harm to others; over himself, the individual is sovereign.",["John Stuart Mill"]),
 ("The Entitlement Theory","just","ana",1974,"Justice is in how holdings arose — just acquisition and transfer — not in any end-pattern; the minimal state is the most that's justified.",["Robert Nozick"]),
 ("Animal Liberation","live","ana",1975,"To weigh a being's suffering less because it is not human is speciesism — the same error as racism or sexism.",["Peter Singer"]),
 ("The Iron Cage","mean","soc",1905,"Rational capitalism, once a calling, hardens into a cage of bureaucratic order that disenchants the world and outlasts its faith.",["Max Weber"]),
 ("Double Consciousness","self","soc",1903,"To be Black in white America is to see yourself always through others' eyes — a twoness, two warring selves in one body.",["W. E. B. Du Bois"]),
 ("Two Dogmas of Empiricism","know","ana",1951,"There is no clean line between truths-by-meaning and truths-by-fact; belief faces experience as a whole web, revisable anywhere.",["W. V. O. Quine"]),
 ("The Turing Test","mind","sci",1950,"Stop asking whether machines 'think'; if a machine's conversation is indistinguishable from a human's, that is enough.",["Alan Turing"]),
 ("The Knowledge Argument","mind","ana",1982,"Mary knows every physical fact about color yet learns something new on first seeing red — so not all facts are physical.",["Frank Jackson"]),
 ("Liberation Theology","peace","chr",1971,"Suffering is not only borne inwardly but structural injustice to be fought; God takes a preferential option for the poor.",["Gustavo Gutiérrez"]),
]
concepts.C.extend(NEW_C12)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R12 = [
 ("The Gettier Problem","Skepticism","echoes"),
 ("The Gettier Problem","Pramāṇa","echoes"),
 ("The Problem of Induction","Empiricism","rejects"),
 ("Falsifiability","The Problem of Induction","builds"),
 ("The Problem of Induction","Skepticism","echoes"),
 ("The Problem of Evil","The Five Ways","rejects"),
 ("The Problem of Evil","The Ontological Argument","rejects"),
 ("The Death of God","The Problem of Evil","echoes"),
 ("Two Concepts of Liberty","Natural Rights","builds"),
 ("Two Concepts of Liberty","The General Will","rejects"),
 ("Two Concepts of Liberty","The Harm Principle","builds"),
 ("The Harm Principle","Utilitarianism","builds"),
 ("The Harm Principle","Natural Rights","echoes"),
 ("The Entitlement Theory","Justice as Fairness","rejects"),
 ("The Entitlement Theory","Natural Rights","builds"),
 ("Animal Liberation","Utilitarianism","builds"),
 ("Animal Liberation","Ahimsa","echoes"),
 ("The Iron Cage","Historical Materialism","rejects"),
 ("The Iron Cage","The Death of God","echoes"),
 ("Capitalist Realism","The Iron Cage","builds"),
 ("Double Consciousness","The Mirror Stage","echoes"),
 ("Double Consciousness","Existential Self","echoes"),
 ("Two Dogmas of Empiricism","Empiricism","rejects"),
 ("Two Dogmas of Empiricism","Verification Principle","rejects"),
 ("Two Dogmas of Empiricism","Paradigm Shifts","echoes"),
 ("The Chinese Room","The Turing Test","rejects"),
 ("The Turing Test","Functionalism","echoes"),
 ("The Turing Test","Behaviorist Mind","echoes"),
 ("The Knowledge Argument","Materialism","rejects"),
 ("The Knowledge Argument","What It Is Like","builds"),
 ("The Knowledge Argument","The Hard Problem","echoes"),
 ("Liberation Theology","Historical Materialism","builds"),
 ("Liberation Theology","Agape","builds"),
 ("Liberation Theology","Satyagraha","echoes"),
 ("Liberation Theology","Denial of the Will","rejects"),
]
concepts.R.extend(NEW_R12)

concepts.main()
