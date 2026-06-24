# -*- coding: utf-8 -*-
"""Thinkers + readings for expand18.py (the East-Asian / Confucian backfill).

Citations verified in a 2026-06-24 research pass. The classical Chinese and
medieval Japanese sources are compiled/recorded texts, so each leads with the
standard scholarly Translation (Van Norden, Hutton, Gardner, Tanahashi) plus a
Study. Dates are the canonical composition of the source, not the translation."""

EXTRA18 = {
"Human Nature Is Good": (["Mencius"],[
  ("Mencius (comp. disciples)","Mengzi (trans. Bryan W. Van Norden, with traditional commentaries)","c.-300","Translation","The four-sprouts argument (2A6, 6A); the now-standard scholarly English."),
  ("Mencius","Mencius (trans. D.C. Lau, Penguin Classics)","c.-300","Translation","The older standard rendering of the Mengzi."),
  ("Kwong-loi Shun","Mencius and Early Chinese Thought","1997","Study","The leading philosophical reconstruction of the xing-shan (good-nature) thesis."),
]),
"Human Nature Is Bad": (["Xunzi"],[
  ("Xunzi","Xunzi: The Complete Text (trans. Eric L. Hutton)","c.-250","Translation","Includes the chapter 'Human Nature Is Bad' (性惡); now the scholarly default."),
  ("Xunzi","Xunzi: A Translation and Study of the Complete Works (trans. John Knoblock)","c.-250","Translation","The fuller three-volume apparatus and commentary."),
  ("Paul R. Goldin","Rituals of the Way: The Philosophy of Xunzi","1999","Study","On virtue as deliberate artifice (wei) and the reshaping power of ritual (li)."),
]),
"Investigation of Things": (["Zhu Xi"],[
  ("Zhu Xi","Learning to Be a Sage (trans. Daniel K. Gardner)","1175","Translation","Selections from the Zhuzi yulei on gewu — investigating the principle (li) in things."),
  ("Wing-tsit Chan","A Source Book in Chinese Philosophy","1963","Translation","Chapter 34 gathers the core Zhu Xi texts on the extension of knowledge."),
  ("Hoyt Cleveland Tillman","Confucian Discourse and Chu Hsi's Ascendancy","1992","Study","How the Cheng-Zhu programme of inquiry became Neo-Confucian orthodoxy."),
]),
"Being-Time": (["Dōgen"],[
  ("Dōgen","Treasury of the True Dharma Eye: Shōbōgenzō (ed. Kazuaki Tanahashi)","1240","Translation","The complete Shōbōgenzō; the 'Uji' (Being-Time) fascicle is the source."),
  ("Dōgen","The Heart of Dōgen's Shōbōgenzō (trans. Norman Waddell & Masao Abe)","1240","Translation","Key fascicles with introduction; a close rendering of 'Uji'."),
  ("Hee-Jin Kim","Eihei Dōgen: Mystical Realist","2004","Study","The standard study; reads Uji as a metaphysics of time, not a mystical figure."),
]),
}

if __name__ == "__main__":
    print("round-eighteen concepts covered:", len(EXTRA18))
