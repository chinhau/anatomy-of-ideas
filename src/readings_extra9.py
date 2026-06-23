# -*- coding: utf-8 -*-
"""Thinkers + ranked readings for expand9.py (Hermetic & Esoteric tier + Norse).

Every entry names a real, dated source and an identifiable author or corpus;
modern scholarly studies (Jonas, Jung, Hanegraaff-tradition) accompany the
primary texts.
"""

EXTRA9 = {
"As Above, So Below": (["Hermes Trismegistus (corpus)"],[
  ("Hermes Trismegistus (attrib.)","The Emerald Tablet","c.800","Primary","'That which is below is like that which is above' — the law of correspondence."),
  ("Corpus Hermeticum","Poimandres & the Hermetic treatises","c.200","Study","The Greco-Egyptian source of Hermetic cosmology."),
]),
"Gnosis (The Divine Spark)": (["Valentinus"],[
  ("Valentinus / Nag Hammadi","The Gospel of Truth","c.150","Primary","The divine spark, the sleep of the world, and awakening through gnosis."),
  ("Hans Jonas","The Gnostic Religion","1958","Study","The classic modern reconstruction of Gnostic thought."),
]),
"The Magnum Opus": (["Zosimos of Panopolis"],[
  ("Zosimos of Panopolis","The Visions of Zosimos","c.300","Primary","Alchemical transformation read as the soul's death and rebirth."),
  ("C. G. Jung","Psychology and Alchemy","1944","Study","Alchemy decoded as a projection of inner individuation."),
]),
"The Perennial Philosophy": (["Agostino Steuco","Aldous Huxley"],[
  ("Agostino Steuco","De perenni philosophia","1540","Primary","The coinage: a single wisdom recurring across all ages."),
  ("Aldous Huxley","The Perennial Philosophy","1945","Intro","The 20th-century statement that all mystics meet at one summit."),
]),
"Ragnarök (Twilight of the Gods)": (["Snorri Sturluson"],[
  ("Snorri Sturluson","The Prose Edda","c.1220","Primary","The doom of the gods — and the green world that rises after."),
  ("Anonymous","The Poetic Edda: Völuspá","c.1000","Study","The seeress's prophecy of the world's end and renewal."),
]),
}

if __name__ == "__main__":
    print("round-nine concepts covered:", len(EXTRA9))
