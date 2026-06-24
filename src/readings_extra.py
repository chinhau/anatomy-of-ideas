# -*- coding: utf-8 -*-
"""Thinkers + ranked readings for the concepts added in expand.py.
Same schema as readings.py: id -> (thinkers[], [(author,title,year,kind,note)])."""

EXTRA = {
# ---- MIND / CONSCIOUSNESS ----
"Stream of Consciousness": (["William James"],[
  ("William James","The Principles of Psychology","1890","Primary","The chapter that named the flowing mind."),
  ("William James","The Varieties of Religious Experience","1902","Primary","Consciousness at its edges."),
]),
"The Hard Problem": (["David Chalmers"],[
  ("David Chalmers","Facing Up to the Problem of Consciousness","1995","Primary","The paper that coined the 'hard problem.'"),
  ("David Chalmers","The Conscious Mind","1996","Primary","The full argument for irreducible experience."),
]),
"What It Is Like": (["Thomas Nagel"],[
  ("Thomas Nagel","What Is It Like to Be a Bat?","1974","Primary","The classic case for subjectivity."),
]),
"Panpsychism": (["Alfred North Whitehead","David Chalmers","Galen Strawson"],[
  ("Galen Strawson","Realistic Monism: Why Physicalism Entails Panpsychism","2006","Primary","The sharpest modern argument."),
  ("Alfred North Whitehead","Process and Reality","1929","Primary","Experience built into the fabric of events."),
]),
"Integrated Information": (["Giulio Tononi","Christof Koch"],[
  ("Giulio Tononi","Phi: A Voyage from the Brain to the Soul","2012","Primary","IIT for the general reader."),
  ("Christof Koch","The Feeling of Life Itself","2019","Study","A neuroscientist's case for IIT."),
]),
"The Intentional Stance": (["Daniel Dennett"],[
  ("Daniel Dennett","The Intentional Stance","1987","Primary","Minds as patterns we predict by."),
  ("Daniel Dennett","Consciousness Explained","1991","Primary","The 'multiple drafts' model of mind."),
]),
"Strange Loop": (["Douglas Hofstadter"],[
  ("Douglas Hofstadter","Gödel, Escher, Bach","1979","Primary","Self-reference as the root of mind."),
  ("Douglas Hofstadter","I Am a Strange Loop","2007","Primary","The self as a loop, stated directly."),
]),
"The Embodied Mind": (["Francisco Varela","Evan Thompson","Eleanor Rosch"],[
  ("Varela, Thompson & Rosch","The Embodied Mind","1991","Primary","Cognitive science meets Buddhist practice."),
  ("Evan Thompson","Mind in Life","2007","Study","The mature statement of enactivism."),
]),
"Universal Grammar": (["Noam Chomsky"],[
  ("Noam Chomsky","Aspects of the Theory of Syntax","1965","Primary","The innate language faculty."),
  ("Noam Chomsky","A Review of B. F. Skinner's Verbal Behavior","1959","Primary","The blow that ended behaviorism's reign."),
]),
"Dual-Process Mind": (["Daniel Kahneman","Amos Tversky"],[
  ("Daniel Kahneman","Thinking, Fast and Slow","2011","Primary","System 1 and System 2, for everyone."),
]),
"Neutral Monism": (["Bertrand Russell","William James","Ernst Mach"],[
  ("Bertrand Russell","The Analysis of Mind","1921","Primary","Mind and matter from one neutral stuff."),
  ("William James","Does 'Consciousness' Exist?","1904","Primary","The essay that seeded the view."),
]),
"Developmental Stages": (["Jean Piaget"],[
  ("Jean Piaget","The Origins of Intelligence in Children","1936","Primary","How the infant mind constructs the world."),
]),
"Cybernetics & Feedback": (["Norbert Wiener","Gregory Bateson"],[
  ("Norbert Wiener","Cybernetics","1948","Primary","Control and communication in animal and machine."),
  ("Gregory Bateson","Steps to an Ecology of Mind","1972","Study","Feedback applied to mind and society."),
]),
"The Butterfly Dream": (["Zhuangzi"],[
  ("Zhuangzi","Zhuangzi (Inner Chapters)","c.300 BCE","Primary","The butterfly dream and the fluid self."),
  ("Burton Watson (trans.)","The Complete Works of Zhuangzi","1968","Translation","The standard, readable English Zhuangzi."),
]),
# ---- MEANING ----
"Meaning Is Created": (["Jean-Paul Sartre","Albert Camus"],[
  ("Jean-Paul Sartre","Existentialism Is a Humanism","1946","Primary","We are the authors of our values."),
  ("Albert Camus","The Myth of Sisyphus","1942","Primary","Meaning made in the teeth of the absurd."),
]),
"Inherent Purpose (Telos)": (["Aristotle","Thomas Aquinas"],[
  ("Aristotle","Nicomachean Ethics","c.340 BCE","Primary","The human telos and the good."),
  ("Aristotle","Physics (Book II)","c.350 BCE","Primary","Final causes — the 'that for the sake of which.'"),
]),
"Ikigai": (["Japanese tradition","Mieko Kamiya"],[
  ("Mieko Kamiya","Ikigai ni tsuite (On the Meaning of Life)","1966","Primary","The foundational Japanese study."),
  ("Ken Mogi","The Little Book of Ikigai","2017","Intro","A short modern introduction."),
]),
"Positive Psychology": (["Martin Seligman","Mihály Csíkszentmihályi"],[
  ("Martin Seligman","Authentic Happiness","2002","Primary","The founding popular statement."),
  ("Martin Seligman","Flourish","2011","Primary","The PERMA model of well-being."),
]),
"The Examined Life": (["Socrates","Plato"],[
  ("Plato","Apology","c.399 BCE","Primary","Socrates on trial: the examined life."),
]),
# ---- TRANSFORMATION ----
"Cognitive Behavioral Therapy": (["Aaron Beck","Albert Ellis"],[
  ("Aaron Beck","Cognitive Therapy and the Emotional Disorders","1976","Primary","The clinical foundation of CBT."),
  ("Albert Ellis","Reason and Emotion in Psychotherapy","1962","Primary","REBT — the Stoic root made therapy."),
]),
"Mindfulness (MBSR)": (["Jon Kabat-Zinn"],[
  ("Jon Kabat-Zinn","Full Catastrophe Living","1990","Primary","The MBSR program in full."),
  ("Jon Kabat-Zinn","Wherever You Go, There You Are","1994","Intro","The gentle way in."),
]),
"Acceptance & Commitment": (["Steven C. Hayes"],[
  ("Steven C. Hayes","Acceptance and Commitment Therapy","1999","Primary","Psychological flexibility, defined."),
  ("Steven C. Hayes","Get Out of Your Mind and Into Your Life","2005","Intro","ACT for the general reader."),
]),
"Individuation": (["Carl Jung"],[
  ("Carl Jung","Two Essays on Analytical Psychology","1928","Primary","The path toward becoming whole."),
  ("Carl Jung","Memories, Dreams, Reflections","1962","Intro","Individuation lived, in his own voice."),
]),
"Yoga: Stilling the Mind": (["Patañjali"],[
  ("Patañjali","Yoga Sūtras","c.200","Primary","'Yoga is the stilling of the mind.'"),
  ("Edwin Bryant (trans.)","The Yoga Sutras of Patañjali","2009","Translation","Translation with deep commentary."),
]),
"Sudden Awakening": (["Huineng","Linji Yixuan"],[
  ("Huineng","The Platform Sutra of the Sixth Patriarch","c.700","Primary","The charter of sudden-awakening Chan."),
  ("(comp.) Linji","The Record of Linji","c.870","Primary","Zen's most ferocious teacher."),
]),
"Self-Cultivation": (["Wang Yangming"],[
  ("Wang Yangming","Instructions for Practical Living (Chuanxi lu, trans. Wing-tsit Chan)","1518","Primary","Innate knowing (liangzhi) and the unity of knowledge and action (zhixing heyi) — the Lu-Wang answer that rejects Zhu Xi's gewu."),
  ("Philip J. Ivanhoe","Readings from the Lu-Wang School of Neo-Confucianism","2009","Translation","Wang in the school that took the mind, not outer things, as the site of moral knowing."),
]),
"Integral Theory": (["Ken Wilber"],[
  ("Ken Wilber","Sex, Ecology, Spirituality","1995","Primary","The four-quadrant integral model."),
  ("Ken Wilber","A Brief History of Everything","1996","Intro","The accessible overview."),
]),
"Mystical Union (Fana)": (["Rumi","Ibn Arabi"],[
  ("Jalal al-Din Rumi","The Masnavi","c.1265","Primary","The great poem of longing and union."),
  ("Ibn Arabi","The Bezels of Wisdom","c.1229","Primary","The metaphysics of divine self-disclosure."),
]),
# ---- ISLAMIC & OTHER ----
"Unity of Being": (["Ibn Arabi"],[
  ("Ibn Arabi","The Meccan Revelations","c.1230","Primary","The vast summa of waḥdat al-wujūd."),
  ("William Chittick","The Sufi Path of Knowledge","1989","Study","The standard scholarly guide to Ibn Arabi."),
]),
"The Flying Man": (["Avicenna (Ibn Sina)"],[
  ("Avicenna","The Book of Healing (Kitāb al-Shifāʾ)","c.1027","Primary","The 'floating man' proves the self to itself."),
]),
"Faith Beyond Reason": (["Al-Ghazali"],[
  ("Al-Ghazali","The Incoherence of the Philosophers","1095","Primary","The great critique of philosophy's reach."),
  ("Al-Ghazali","Deliverance from Error","c.1108","Intro","His spiritual and intellectual autobiography."),
]),
"Language Games": (["Ludwig Wittgenstein"],[
  ("Ludwig Wittgenstein","Philosophical Investigations","1953","Primary","Meaning as use; the later Wittgenstein."),
  ("Ludwig Wittgenstein","Tractatus Logico-Philosophicus","1921","Primary","The picture theory he later overturned."),
]),
"Pragmatism": (["William James","Charles Peirce","John Dewey"],[
  ("William James","Pragmatism","1907","Primary","Truth as what works, in lectures."),
  ("Charles S. Peirce","How to Make Our Ideas Clear","1878","Primary","The pragmatic maxim at the source."),
]),
"Evolution by Natural Selection": (["Charles Darwin"],[
  ("Charles Darwin","On the Origin of Species","1859","Primary","Design without a designer."),
  ("Daniel Dennett","Darwin's Dangerous Idea","1995","Study","Evolution as 'universal acid' for philosophy."),
]),
"Political Realism": (["Niccolò Machiavelli"],[
  ("Niccolò Machiavelli","The Prince","1532","Primary","Power as it is, not as it ought to be."),
  ("Niccolò Machiavelli","Discourses on Livy","1531","Primary","The republican counterpart to The Prince."),
]),
"Qualified Non-Dualism": (["Ramanuja"],[
  ("Ramanuja","Sri Bhashya","c.1100","Primary","The qualified-non-dual reply to Shankara."),
]),
}

if __name__ == "__main__":
    print("extra concepts covered:", len(EXTRA))
