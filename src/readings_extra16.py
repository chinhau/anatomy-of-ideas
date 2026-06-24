# -*- coding: utf-8 -*-
"""Thinkers + readings for expand16.py (the metaethics backfill).

Citations were verified in a 2026-06-23 research pass. Primary sources where a
canonical text carries the position (Hume, Moore, Mackie, Ayer); Translation for
the Greek/Sanskrit sources read in English (Plato, Jaimini). The kalām entry has
no standard English of ʿAbd al-Jabbār's al-Mughnī, so it leads with the standard
secondary scholarship (Hourani, Fakhry)."""

EXTRA16 = {
"The Euthyphro Dilemma": (["Plato","Socrates"],[
  ("Plato","Euthyphro (trans. G.M.A. Grube, in Plato: Complete Works, ed. Cooper)","1997","Translation","The dialogue itself; Socrates presses the question on the seer Euthyphro at the courthouse steps."),
  ("Plato","Euthyphro, Apology, Crito, Phaedo (trans. H.N. Fowler, Loeb)","1914","Translation","Greek-facing scholarly edition of the trial dialogues."),
  ("Mark Murphy","Theological Voluntarism (Stanford Encyclopedia of Philosophy)","2002","Study","Maps the dilemma onto modern divine-command ethics and its replies."),
]),
"The Is–Ought Gap": (["David Hume"],[
  ("David Hume","A Treatise of Human Nature","1739","Primary","Book III.i.1 — the famous turn from 'is' and 'is not' to 'ought' and 'ought not'."),
  ("W.D. Hudson (ed.)","The Is/Ought Question","1969","Study","The classic anthology that named and debated 'Hume's Law'."),
]),
"Moral Error Theory": (["J.L. Mackie"],[
  ("J.L. Mackie","Ethics: Inventing Right and Wrong","1977","Primary","The arguments from relativity and from queerness against objective values."),
  ("Richard Joyce","The Myth of Morality","2001","Study","Defends and extends error theory toward moral fictionalism."),
]),
"The Open-Question Argument": (["G.E. Moore","W.D. Ross"],[
  ("G.E. Moore","Principia Ethica","1903","Primary","'Good' as a simple, indefinable non-natural property; the naturalistic fallacy."),
  ("W.D. Ross","The Right and the Good","1930","Primary","A non-naturalist companion: self-evident prima facie duties."),
  ("Thomas Baldwin","G.E. Moore","1990","Study","The standard critical study of Moore, including the open-question argument's fate."),
]),
"Emotivism": (["A.J. Ayer","C.L. Stevenson"],[
  ("A.J. Ayer","Language, Truth and Logic","1936","Primary","Chapter 6: moral judgements are not statements but expressions of feeling."),
  ("C.L. Stevenson","Ethics and Language","1944","Primary","Systematic emotivism — the persuasive, dynamic use of moral words."),
  ("Simon Blackburn","Ruling Passions","1998","Study","Quasi-realism: how an expressivist can earn back the talk of moral truth."),
]),
"Mīmāṃsā: Dharma from the Word": (["Jaimini","Kumārila Bhaṭṭa"],[
  ("Jaimini","The Pūrva Mīmāṃsā Sūtras of Jaimini (trans. Ganganatha Jha)","1916","Translation","The root sūtras: dharma is the object enjoined by the Vedic injunction (codanā)."),
  ("Francis X. Clooney","Thinking Ritually: Rediscovering the Pūrva Mīmāṃsā of Jaimini","1990","Study","The leading study of Jaimini's system of ritual obligation and the authority of the Word."),
  ("John A. Taber","Kumārila (Stanford Encyclopedia of Philosophy)","2017","Study","On the intrinsic validity (svataḥ prāmāṇya) of the authorless Veda."),
]),
"Ḥusn & Qubḥ: Reason vs. Command": (["ʿAbd al-Jabbār","al-Ashʿarī"],[
  ("George F. Hourani","Islamic Rationalism: The Ethics of ʿAbd al-Jabbār","1971","Study","The standard study of Muʿtazilite moral rationalism — good and evil knowable by reason."),
  ("George F. Hourani","Reason and Tradition in Islamic Ethics","1985","Study","Essays mapping the rationalist (Muʿtazila) and voluntarist (Ashʿarī) camps."),
  ("Majid Fakhry","Ethical Theories in Islam","1991","Study","Surveys the kalām divide over the source of moral value."),
]),
}

if __name__ == "__main__":
    print("round-sixteen concepts covered:", len(EXTRA16))
