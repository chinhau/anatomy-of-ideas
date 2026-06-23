# -*- coding: utf-8 -*-
"""Thinkers + ranked readings for expand6.py (the clean tier of Korean thought).

Every entry names an identifiable author and a real, dated text.
"""

EXTRA6 = {
"The Four-Seven Debate": (["Yi Hwang (Toegye)","Gi Daeseung"],[
  ("Yi Hwang (Toegye)","Ten Diagrams on Sage Learning (Seonghak sipdo)","1568","Primary","The mature statement of li-primacy in moral psychology."),
  ("Yi Hwang & Gi Daeseung","The Four-Seven Correspondence","c.1559","Study","The eight-year exchange of letters that framed the debate."),
]),
"Principle Rides on Force": (["Yi I (Yulgok)"],[
  ("Yi I (Yulgok)","Essentials of Sage Learning (Seonghak jibyo)","1575","Primary","Principle and material force as one: qi acts, li rides."),
]),
"Hwajaeng (Reconciling Disputes)": (["Wŏnhyo"],[
  ("Wŏnhyo","Commentary on the Awakening of Mahāyāna Faith (Daeseung gisillon so)","c.671","Primary","The 'one mind' that reconciles the doctrinal schools."),
]),
"Sudden Enlightenment, Gradual Cultivation": (["Jinul"],[
  ("Jinul","Secrets on Cultivating the Mind (Susimgyeol)","c.1205","Primary","Sudden insight followed by gradual practice — Seon and doctrine joined."),
]),
"In Is Heaven (Innaecheon)": (["Choe Je-u"],[
  ("Choe Je-u","Eastern Scripture (Donggyeong daejeon)","1880","Primary","The founding text of Donghak: Heaven borne within every person."),
]),
}

if __name__ == "__main__":
    print("round-six concepts covered:", len(EXTRA6))
