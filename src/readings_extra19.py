# -*- coding: utf-8 -*-
"""Thinkers + readings for expand19.py (the Islamic golden-age / falsafa backfill).

Citations verified in a 2026-06-24 research pass. Marmura is the workhorse
translator (al-Ghazālī's Incoherence; Avicenna's Metaphysics of the Healing);
Butterworth for the political/Averroes texts; Walzer for al-Fārābī. Each leads
with the standard parallel-text Translation plus a Study/Intro. Dates are the
canonical composition of the Arabic source, not the translation."""

EXTRA19 = {
"Occasionalism": (["Al-Ghazali"],[
  ("al-Ghazālī","The Incoherence of the Philosophers (Tahāfut al-Falāsifa, trans. Michael E. Marmura)","1095","Translation","The 17th Discussion: there is no necessary connection between cause and effect."),
  ("Frank Griffel","Al-Ghazālī's Philosophical Theology","2009","Study","Dismantles the 'al-Ghazālī ended Islamic science' caricature; reads his occasionalism with care."),
  ("Frank Griffel","Al-Ghazali (Stanford Encyclopedia of Philosophy)","2020","Intro","Current, reliable orientation to his life and the causation argument."),
]),
"Harmony of Religion and Philosophy": (["Averroes (Ibn Rushd)"],[
  ("Averroes","Decisive Treatise & Epistle Dedicatory (Faṣl al-Maqāl, trans. Charles E. Butterworth)","1180","Translation","The argument that the Law obliges the philosopher to interpret, and that truth cannot contradict truth."),
  ("Averroes","The Incoherence of the Incoherence (Tahāfut al-Tahāfut, trans. Simon van den Bergh)","1180","Translation","The point-by-point rebuttal of al-Ghazālī, with extensive notes."),
  ("Oliver Leaman","Averroes and His Philosophy","1998","Study","On Ibn Rushd's own program — distinct from the Latin 'Averroism' it inspired."),
]),
"The Virtuous City": (["al-Fārābī"],[
  ("al-Fārābī","On the Perfect State (Mabādiʾ Ārāʾ Ahl al-Madīna al-Fāḍila, trans. Richard Walzer)","940","Translation","The standard critical edition of the virtuous-city cosmology and politics."),
  ("al-Fārābī","The Political Writings (trans. Charles E. Butterworth)","2001","Primary","The practical-political treatises that complement the cosmological work."),
  ("Christopher A. Colmo","Breaking with Athens: Alfarabi as Founder","2005","Study","On the Plato/Aristotle synthesis and the philosopher-prophet."),
]),
"The Necessary Being": (["Avicenna (Ibn Sina)"],[
  ("Avicenna","The Metaphysics of The Healing (Kitāb al-Shifāʾ: Ilāhiyyāt, trans. Michael E. Marmura)","1027","Translation","The essence/existence distinction and the proof of the Necessary Existent (Bks I & VIII)."),
  ("Jon McGinnis","Avicenna","2010","Study","The standard English study of Avicenna's metaphysics and contingency proof."),
  ("Peter Adamson","Philosophy in the Islamic World (A History of Philosophy Without Any Gaps, vol. 3)","2016","Intro","The accessible survey placing Avicenna in the whole falsafa thread."),
]),
}

if __name__ == "__main__":
    print("round-nineteen concepts covered:", len(EXTRA19))
