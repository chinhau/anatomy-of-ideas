# -*- coding: utf-8 -*-
"""Thinkers + ranked readings for expand7.py (scripture-born concepts).

The scripture itself is the Primary source; named theologians supply the
classic exposition.
"""

EXTRA7 = {
"Agape": (["Paul of Tarsus","Augustine of Hippo"],[
  ("Paul of Tarsus","First Epistle to the Corinthians (ch. 13)","c.55","Primary","'Love is patient, love is kind' — agapē as self-giving love."),
  ("Anders Nygren","Agape and Eros","1930","Study","The classic contrast of self-giving agapē with acquisitive eros."),
]),
"Grace": (["Augustine of Hippo"],[
  ("Augustine of Hippo","On Grace and Free Will","c.427","Primary","Salvation as unmerited gift, not earned by works."),
  ("Augustine of Hippo","Confessions","c.400","Intro","The lived drama of grace and a will divided against itself."),
]),
"Original Sin": (["Augustine of Hippo"],[
  ("Augustine of Hippo","On the Merits and Forgiveness of Sins","c.412","Primary","The inherited fault that the will cannot undo on its own."),
  ("Book of Genesis","Genesis 3","c.-550","Intro","The Fall in the garden — the source narrative."),
]),
"Logos (The Word)": (["John the Evangelist","Philo of Alexandria"],[
  ("Gospel of John","John 1:1-14","c.95","Primary","'In the beginning was the Word' — the Logos through whom all is made."),
  ("Philo of Alexandria","On the Creation of the World","c.40","Study","The Logos as God's mediating reason, bridging Greek and Hebrew thought."),
]),
"Covenant": (["Hebrew Bible"],[
  ("Hebrew Bible","Exodus & Deuteronomy","c.-600","Primary","The binding pact between God and a people, with law as its seal."),
  ("Jon D. Levenson","Sinai and Zion","1985","Study","The covenant as the spine of Hebrew religion."),
]),
"Imago Dei": (["Hebrew Bible","Maimonides"],[
  ("Book of Genesis","Genesis 1:26-27","c.-550","Primary","Humankind made 'in the image of God.'"),
  ("Maimonides","The Guide for the Perplexed","c.1190","Study","The image read as the intellect, not the body."),
]),
"Tikkun Olam": (["Isaac Luria"],[
  ("Isaac Luria (Hayyim Vital, recorder)","Etz Hayim (The Tree of Life)","c.1573","Primary","Gathering the scattered divine sparks — repairing a broken world."),
]),
"Tawhid (Divine Unity)": (["The Quran","al-Ash'ari"],[
  ("The Quran","Surah al-Ikhlas (112)","c.650","Primary","'Say: He is God, the One' — absolute divine unity."),
  ("Abu al-Hasan al-Ash'ari","Kitab al-Luma","c.920","Study","The Ash'arite formulation of God's unity and attributes."),
]),
"Fitra": (["The Quran"],[
  ("The Quran","Surah ar-Rum (30:30)","c.650","Primary","Every soul born upon the fitra — an innate disposition to the truth."),
  ("al-Ghazali","Deliverance from Error","c.1108","Intro","The innate nature beneath acquired belief."),
]),
}

if __name__ == "__main__":
    print("round-seven concepts covered:", len(EXTRA7))
