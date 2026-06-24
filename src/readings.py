# -*- coding: utf-8 -*-
"""For each concept: a fuller roster of thinkers, and a ranked reading list.
Readings are ordered by influence/centrality (most essential first).
Reading tuple = (author, title, year, kind, note)
kind in: Primary | Commentary | Study | Intro | Translation
"""

# id -> (thinkers[], readings[(author,title,year,kind,note)])
DATA = {
# ---------------- REALITY ----------------
"Theory of Forms": (["Plato","Plotinus","Augustine"],[
  ("Plato","Republic (Books VI–VII)","c.375 BCE","Primary","The Sun, Line and Cave — the Forms unveiled."),
  ("Plato","Phaedo","c.380 BCE","Primary","The soul's recollection of the Forms."),
  ("Plato","Parmenides","c.370 BCE","Primary","Plato's own probing critique of the theory."),
]),
"Hylomorphism": (["Aristotle","Thomas Aquinas"],[
  ("Aristotle","Metaphysics (Books VII–IX)","c.350 BCE","Primary","Substance as matter informed by form."),
  ("Aristotle","Physics (Book II)","c.350 BCE","Primary","The doctrine of the four causes."),
]),
"Atomism": (["Democritus","Leucippus","Epicurus","Lucretius"],[
  ("Lucretius","On the Nature of Things","c.55 BCE","Primary","The fullest surviving atomist work, in verse."),
  ("Epicurus","Letter to Herodotus","c.300 BCE","Primary","Atoms and void, stated briefly."),
]),
"Being is One": (["Parmenides","Zeno of Elea","Melissus"],[
  ("Parmenides","On Nature (fragments)","c.475 BCE","Primary","The 'Way of Truth': what is, is one."),
  ("Plato","Parmenides","c.370 BCE","Primary","A dramatized stress-test of Eleatic monism."),
]),
"Everything Flows": (["Heraclitus","Cratylus"],[
  ("Heraclitus","Fragments","c.500 BCE","Primary","The river, the fire, the logos."),
  ("Charles Kahn","The Art and Thought of Heraclitus","1979","Study","The standard scholarly reconstruction."),
]),
"Materialism": (["d'Holbach","La Mettrie","Diderot"],[
  ("Baron d'Holbach","The System of Nature","1770","Primary","A thoroughgoing materialist universe."),
  ("Julien La Mettrie","Man a Machine","1747","Primary","The body — and mind — as mechanism."),
]),
"Idealism": (["George Berkeley"],[
  ("George Berkeley","A Treatise Concerning the Principles of Human Knowledge","1710","Primary","'To be is to be perceived.'"),
  ("George Berkeley","Three Dialogues between Hylas and Philonous","1713","Primary","The same case, in lively dialogue."),
]),
"Absolute Idealism": (["G.W.F. Hegel","F.W.J. Schelling","F.H. Bradley"],[
  ("G.W.F. Hegel","Phenomenology of Spirit","1807","Primary","Spirit's odyssey toward self-knowledge."),
  ("Charles Taylor","Hegel","1975","Study","The most navigable guide to a hard thinker."),
]),
"One Substance": (["Baruch Spinoza"],[
  ("Baruch Spinoza","Ethics","1677","Primary","One substance — God-or-Nature — proved geometrically."),
]),
"Process Reality": (["Alfred North Whitehead","Henri Bergson"],[
  ("Alfred North Whitehead","Process and Reality","1929","Primary","Reality as events and becomings."),
  ("Henri Bergson","Creative Evolution","1907","Primary","Duration and the élan vital."),
]),
"Śūnyatā (Emptiness)": (["Nāgārjuna","Chandrakīrti"],[
  ("Nāgārjuna","Mūlamadhyamakakārikā","c.200","Primary","The root verses on the Middle Way."),
  ("Jay Garfield (trans.)","The Fundamental Wisdom of the Middle Way","1995","Translation","Translation with lucid commentary."),
]),
"Dependent Origination": (["The Buddha","Buddhaghosa"],[
  ("(Pali Canon)","Saṃyutta Nikāya (Nidāna-saṃyutta)","c.250 BCE","Primary","The chain of conditioned arising."),
  ("Bhikkhu Bodhi","In the Buddha's Words","2005","Intro","A clear thematic anthology of the suttas."),
]),
"Brahman": (["Upanishadic sages","Ādi Śaṅkara"],[
  ("(Anonymous)","The Principal Upanishads","c.700 BCE","Primary","Chandogya & Brihadaranyaka on the absolute."),
  ("Ādi Śaṅkara","Brahma Sūtra Bhāṣya","c.800","Commentary","The classic non-dual reading."),
]),
"The Dao": (["Laozi","Zhuangzi"],[
  ("Laozi","Tao Te Ching","c.400 BCE","Primary","The nameless source and pattern beneath all things — named, it is already not the Way."),
  ("Zhuangzi","Zhuangzi","c.300 BCE","Primary","Playful, radical Daoist parables."),
]),
"Yin–Yang / Qi": (["Zou Yan","the I Ching tradition"],[
  ("(Anonymous)","I Ching (Book of Changes)","c.800 BCE","Primary","The Book of Changes: reality read as the turning of complementary opposites, an order found in the pattern of flux."),
  ("Fung Yu-lan","A Short History of Chinese Philosophy","1948","Study","Sets yin-yang in its philosophical context."),
]),
"Monadology": (["G.W. Leibniz"],[
  ("G.W. Leibniz","Monadology","1714","Primary","Reality as windowless minds in harmony."),
  ("G.W. Leibniz","Discourse on Metaphysics","1686","Primary","The system's earlier, fuller sketch."),
]),
# ---------------- KNOWLEDGE ----------------
"Allegory of the Cave": (["Plato"],[
  ("Plato","Republic (Book VII)","c.375 BCE","Primary","Shadows mistaken for the real, and the painful turn toward the light — knowledge as a waking that hurts."),
]),
"Rationalism": (["René Descartes","Baruch Spinoza","G.W. Leibniz"],[
  ("René Descartes","Meditations on First Philosophy","1641","Primary","Doubt rebuilt into certainty by reason."),
  ("G.W. Leibniz","New Essays on Human Understanding","1704","Primary","The rationalist reply to Locke."),
]),
"Empiricism": (["John Locke","George Berkeley","David Hume"],[
  ("David Hume","An Enquiry Concerning Human Understanding","1748","Primary","The sharpest, most readable statement."),
  ("John Locke","An Essay Concerning Human Understanding","1689","Primary","The founding empiricist treatise."),
]),
"The Cogito": (["René Descartes"],[
  ("René Descartes","Meditations on First Philosophy (II)","1641","Primary","'I think, therefore I am.'"),
  ("René Descartes","Discourse on the Method","1637","Primary","The first, plainer formulation."),
]),
"Tabula Rasa": (["John Locke"],[
  ("John Locke","An Essay Concerning Human Understanding (Book II)","1689","Primary","No innate ideas; experience writes the mind."),
]),
"Skepticism": (["Pyrrho","Sextus Empiricus"],[
  ("Sextus Empiricus","Outlines of Pyrrhonism","c.200","Primary","Suspend judgment, and find tranquility."),
]),
"Transcendental Idealism": (["Immanuel Kant"],[
  ("Immanuel Kant","Critique of Pure Reason","1781","Primary","We know appearances shaped by the mind."),
  ("Immanuel Kant","Prolegomena to Any Future Metaphysics","1783","Intro","Kant's own shorter way in."),
]),
"Falsifiability": (["Karl Popper"],[
  ("Karl Popper","The Logic of Scientific Discovery","1959","Primary","Science advances by bold, refutable conjectures."),
  ("Karl Popper","Conjectures and Refutations","1963","Primary","The idea applied across knowledge."),
]),
"Paradigm Shifts": (["Thomas Kuhn"],[
  ("Thomas Kuhn","The Structure of Scientific Revolutions","1962","Primary","Science changes by revolution, not accretion."),
]),
"Verification Principle": (["A.J. Ayer","Rudolf Carnap","Moritz Schlick"],[
  ("A.J. Ayer","Language, Truth and Logic","1936","Primary","The crisp English manifesto of positivism."),
]),
"Two Truths": (["Nāgārjuna","Chandrakīrti"],[
  ("Nāgārjuna","Mūlamadhyamakakārikā (ch. 24)","c.200","Primary","Conventional and ultimate truth distinguished."),
  ("Chandrakīrti","Madhyamakāvatāra","c.600","Commentary","The influential Prāsaṅgika elaboration."),
]),
"Pramāṇa": (["Akṣapāda Gautama","Dignāga","Dharmakīrti"],[
  ("Akṣapāda Gautama","Nyāya Sūtras","c.200","Primary","The valid means of knowledge enumerated."),
  ("B.K. Matilal","Perception","1986","Study","A modern bridge to Indian epistemology."),
]),
"Anekāntavāda": (["Mahāvīra","Umāsvāti"],[
  ("Umāsvāti","Tattvārtha Sūtra","c.200","Primary","The many-sidedness of reality, systematized."),
  ("Padmanabh Jaini","The Jaina Path of Purification","1979","Study","The standard scholarly overview."),
]),
# ---------------- SELF ----------------
"The Immortal Soul": (["Plato","Pythagoras"],[
  ("Plato","Phaedo","c.380 BCE","Primary","Four arguments for the soul's deathlessness."),
]),
"Substance Dualism": (["René Descartes"],[
  ("René Descartes","Meditations (VI)","1641","Primary","Mind and body as distinct substances."),
  ("Gilbert Ryle","The Concept of Mind","1949","Study","The famous attack: 'the ghost in the machine.'"),
]),
"Ātman = Brahman": (["Upanishadic sages","Ādi Śaṅkara"],[
  ("(Anonymous)","Chandogya Upanishad","c.700 BCE","Primary","'Tat tvam asi' — thou art that."),
  ("Ādi Śaṅkara","Upadeśasāhasrī","c.800","Commentary","The non-dual teaching distilled."),
]),
"Anattā (No-Self)": (["The Buddha","Nāgārjuna"],[
  ("(Pali Canon)","Anattalakkhaṇa Sutta","c.250 BCE","Primary","The discourse on not-self."),
  ("Walpola Rahula","What the Buddha Taught","1959","Intro","Still the clearest short introduction."),
]),
"Bundle Theory": (["David Hume"],[
  ("David Hume","A Treatise of Human Nature (I.IV.6)","1739","Primary","The self as a bundle of perceptions."),
]),
"The Unconscious": (["Sigmund Freud","Pierre Janet"],[
  ("Sigmund Freud","The Interpretation of Dreams","1900","Primary","Freud's royal road inward: the dream as the disguised speech of a mind mostly hidden from itself."),
  ("Sigmund Freud","Introductory Lectures on Psychoanalysis","1917","Intro","Freud lecturing on his own system."),
]),
"Collective Unconscious": (["Carl Jung"],[
  ("Carl Jung","The Archetypes and the Collective Unconscious","1959","Primary","Beneath the personal mind, Jung maps a shared layer of inherited images — myth and dream drawn from one well."),
  ("Carl Jung","Man and His Symbols","1964","Intro","Jung's last, deliberately accessible book."),
]),
"Behaviorist Mind": (["John B. Watson","B.F. Skinner","Ivan Pavlov"],[
  ("John B. Watson","Psychology as the Behaviorist Views It","1913","Primary","The behaviorist manifesto."),
  ("B.F. Skinner","Beyond Freedom and Dignity","1971","Primary","Conditioning over inner freedom."),
]),
"Functionalism": (["Hilary Putnam","Jerry Fodor","David Lewis"],[
  ("Hilary Putnam","The Nature of Mental States","1967","Primary","Mind as functional role, not substance."),
  ("Jaegwon Kim","Philosophy of Mind","1996","Intro","A clear textbook framing of the debate."),
]),
"Existential Self": (["Jean-Paul Sartre","Simone de Beauvoir"],[
  ("Jean-Paul Sartre","Being and Nothingness","1943","Primary","Existence precedes essence; we make ourselves."),
  ("Jean-Paul Sartre","Existentialism Is a Humanism","1946","Intro","The popular lecture version."),
]),
"Being-in-the-World": (["Martin Heidegger","Maurice Merleau-Ponty"],[
  ("Martin Heidegger","Being and Time","1927","Primary","Dasein as involved being-among-things."),
  ("Maurice Merleau-Ponty","Phenomenology of Perception","1945","Primary","The lived, embodied perspective."),
]),
"The Mirror Stage": (["Jacques Lacan"],[
  ("Jacques Lacan","Écrits ('The Mirror Stage')","1949","Primary","The 'I' formed through image and Other."),
]),
"Relational Self": (["Confucius","Mencius"],[
  ("Confucius","Analects","c.500 BCE","Primary","The self as woven from its relationships."),
  ("Herbert Fingarette","Confucius: The Secular as Sacred","1972","Study","A landmark modern rereading."),
]),
"Self-Actualization": (["Abraham Maslow","Carl Rogers"],[
  ("Abraham Maslow","Motivation and Personality","1954","Primary","The hierarchy of needs and its summit."),
  ("Carl Rogers","On Becoming a Person","1961","Primary","Growth from the therapist's chair."),
]),
# ---------------- ETHICS ----------------
"Eudaimonia": (["Aristotle"],[
  ("Aristotle","Nicomachean Ethics","c.340 BCE","Primary","Flourishing as the activity of virtue."),
]),
"The Golden Mean": (["Aristotle"],[
  ("Aristotle","Nicomachean Ethics (Book II)","c.340 BCE","Primary","Virtue as the mean between extremes."),
]),
"Stoic Virtue": (["Zeno of Citium","Epictetus","Marcus Aurelius","Seneca"],[
  ("Epictetus","Enchiridion (Handbook)","c.125","Primary","The pocket manual of Stoic practice."),
  ("Marcus Aurelius","Meditations","c.175","Primary","A Stoic emperor's private notebook."),
]),
"Epicurean Pleasure": (["Epicurus","Lucretius"],[
  ("Epicurus","Letter to Menoeceus","c.300 BCE","Primary","Pleasure rightly understood as tranquility."),
  ("Lucretius","On the Nature of Things","c.55 BCE","Primary","Epicurean ethics and physics in verse."),
]),
"Categorical Imperative": (["Immanuel Kant"],[
  ("Immanuel Kant","Groundwork of the Metaphysics of Morals","1785","Primary","Act on maxims you could universalize."),
  ("Immanuel Kant","Critique of Practical Reason","1788","Primary","The fuller moral architecture."),
]),
"Utilitarianism": (["Jeremy Bentham","John Stuart Mill","Henry Sidgwick"],[
  ("John Stuart Mill","Utilitarianism","1863","Primary","The refined, humane statement."),
  ("Jeremy Bentham","Introduction to the Principles of Morals and Legislation","1789","Primary","The original felicific calculus."),
]),
"Ren & Li": (["Confucius","Mencius","Xunzi"],[
  ("Confucius","Analects","c.500 BCE","Primary","Humaneness cultivated through ritual."),
  ("Mencius","Mencius","c.300 BCE","Primary","Human nature as innately good."),
]),
"Wu Wei": (["Laozi","Zhuangzi"],[
  ("Laozi","Tao Te Ching","c.400 BCE","Primary","Effortless action: moving with the grain of things, so the most is accomplished by forcing the least."),
  ("Edward Slingerland","Trying Not to Try","2014","Study","Wu wei meets modern psychology."),
]),
"Ahimsa": (["Mahāvīra","Mahatma Gandhi"],[
  ("(Jain canon)","Ācārāṅga Sūtra","c.400 BCE","Primary","The earliest doctrine of non-harm."),
  ("Mahatma Gandhi","An Autobiography","1929","Primary","Ahimsa lived as 'experiments with truth.'"),
]),
"Master & Slave Morality": (["Friedrich Nietzsche"],[
  ("Friedrich Nietzsche","On the Genealogy of Morality","1887","Primary","Nietzsche traces inherited morality to a slave's revolt against the strong — and dares a revaluation of values."),
  ("Friedrich Nietzsche","Beyond Good and Evil","1886","Primary","The prelude to the revaluation."),
]),
"Authenticity": (["Søren Kierkegaard","Jean-Paul Sartre","Martin Heidegger"],[
  ("Jean-Paul Sartre","Being and Nothingness","1943","Primary","Freedom, 'bad faith,' and owning one's life."),
  ("Søren Kierkegaard","Either/Or","1843","Primary","The choice that constitutes a self."),
]),
"Care Ethics": (["Carol Gilligan","Nel Noddings"],[
  ("Carol Gilligan","In a Different Voice","1982","Primary","Morality grounded in relationship and care."),
  ("Nel Noddings","Caring","1984","Primary","Care as the basis of ethics and education."),
]),
# ---------------- SOCIETY ----------------
"Philosopher-Kings": (["Plato"],[
  ("Plato","Republic","c.375 BCE","Primary","Justice in the soul and the ideal city."),
]),
"Social Contract": (["Thomas Hobbes","John Locke","Jean-Jacques Rousseau"],[
  ("Jean-Jacques Rousseau","The Social Contract","1762","Primary","'Man is born free; everywhere in chains.'"),
  ("John Locke","Two Treatises of Government","1689","Primary","Consent, rights, and limited government."),
]),
"Leviathan": (["Thomas Hobbes"],[
  ("Thomas Hobbes","Leviathan","1651","Primary","Order through an absolute sovereign."),
]),
"Natural Rights": (["John Locke","Mary Wollstonecraft"],[
  ("John Locke","Two Treatises of Government","1689","Primary","Life, liberty, and property as rights."),
  ("Mary Wollstonecraft","A Vindication of the Rights of Woman","1792","Primary","Natural rights extended, against their gendered limits."),
]),
"The General Will": (["Jean-Jacques Rousseau"],[
  ("Jean-Jacques Rousseau","The Social Contract","1762","Primary","Legitimacy as the people's collective will."),
]),
"Historical Materialism": (["Karl Marx","Friedrich Engels"],[
  ("Karl Marx & Friedrich Engels","The Communist Manifesto","1848","Primary","History as the history of class struggle."),
  ("Karl Marx","Capital, Volume I","1867","Primary","The deep critique of capital."),
]),
"Justice as Fairness": (["John Rawls"],[
  ("John Rawls","A Theory of Justice","1971","Primary","Principles chosen behind a veil of ignorance."),
  ("John Rawls","Justice as Fairness: A Restatement","2001","Primary","Rawls's late clarification."),
]),
"Power/Knowledge": (["Michel Foucault"],[
  ("Michel Foucault","Discipline and Punish","1975","Primary","How discipline produces the modern subject."),
  ("Michel Foucault","The History of Sexuality, Vol. I","1976","Primary","Power as productive, not merely repressive."),
]),
"Legalism": (["Han Feizi","Shang Yang","Li Si"],[
  ("Han Feizi","Han Feizi","c.230 BCE","Primary","Statecraft by strict, impartial law."),
  ("Shang Yang","The Book of Lord Shang","c.330 BCE","Primary","The hard logic of reward and punishment."),
]),
"Government by Virtue": (["Confucius","Mencius"],[
  ("Confucius","Analects","c.500 BCE","Primary","Rule by moral example, not coercion."),
  ("Mencius","Mencius","c.300 BCE","Primary","The people's welfare and the Mandate."),
]),
"Mohist Universal Love": (["Mozi"],[
  ("Mozi","Mozi ('Universal Love')","c.400 BCE","Primary","Impartial care as the path to order."),
]),
"Satyagraha": (["Mahatma Gandhi"],[
  ("Mahatma Gandhi","Hind Swaraj","1909","Primary","The case for nonviolent self-rule."),
  ("Mahatma Gandhi","An Autobiography","1929","Primary","Truth-force, tested in a life."),
]),
# ---------------- FREE WILL ----------------
"Hard Determinism": (["Baron d'Holbach","Sam Harris"],[
  ("Baron d'Holbach","The System of Nature","1770","Primary","Every choice as a link in a causal chain."),
  ("Sam Harris","Free Will","2012","Study","The brisk contemporary case against it."),
]),
"Libertarian Free Will": (["Thomas Reid","Robert Kane"],[
  ("Thomas Reid","Essays on the Active Powers of Man","1788","Primary","Agent causation and real freedom."),
  ("Robert Kane","The Significance of Free Will","1996","Study","A modern indeterminist defense."),
]),
"Compatibilism": (["David Hume","Harry Frankfurt","Daniel Dennett"],[
  ("David Hume","Enquiry Concerning Human Understanding (§8)","1748","Primary","Liberty reconciled with necessity."),
  ("Daniel Dennett","Elbow Room","1984","Study","The varieties of free will worth wanting."),
]),
"Amor Fati": (["Epictetus","Friedrich Nietzsche"],[
  ("Epictetus","Enchiridion","c.125","Primary","Will what happens; be free."),
  ("Friedrich Nietzsche","Ecce Homo","1908","Primary","'My formula for greatness… amor fati.'"),
]),
"Karma": (["Vedic & Upanishadic sages","Vyāsa"],[
  ("(Anonymous)","Bhagavad Gita","c.200 BCE","Primary","Act, but without grasping at the fruit."),
  ("(Anonymous)","The Principal Upanishads","c.700 BCE","Primary","The earliest doctrine of deeds and rebirth."),
]),
"Pre-established Harmony": (["G.W. Leibniz"],[
  ("G.W. Leibniz","Monadology","1714","Primary","Minds and bodies synchronized by God."),
  ("G.W. Leibniz","Discourse on Metaphysics","1686","Primary","The harmony first worked out."),
]),
"Condemned to be Free": (["Jean-Paul Sartre"],[
  ("Jean-Paul Sartre","Being and Nothingness","1943","Primary","No excuses: we are our choices."),
  ("Jean-Paul Sartre","Existentialism Is a Humanism","1946","Intro","Freedom and responsibility, plainly."),
]),
"Eternal Recurrence": (["Friedrich Nietzsche"],[
  ("Friedrich Nietzsche","The Gay Science (§341)","1882","Primary","'This life… once more and innumerable times.'"),
  ("Friedrich Nietzsche","Thus Spoke Zarathustra","1883","Primary","The thought dramatized."),
]),
"Illusion of the Doer": (["Ādi Śaṅkara"],[
  ("(Anonymous)","Ashtavakra Gita","date uncertain","Primary","The witness beyond the sense of agency."),
  ("Ādi Śaṅkara","Vivekachudamani","c.800","Commentary","Discriminating the Self from the doer."),
]),
# ---------------- SUFFERING ----------------
"Four Noble Truths": (["The Buddha"],[
  ("(Pali Canon)","Dhammacakkappavattana Sutta","c.250 BCE","Primary","The Buddha's first discourse."),
  ("Walpola Rahula","What the Buddha Taught","1959","Intro","The clearest short exposition."),
]),
"Nirvana": (["The Buddha","Nāgārjuna"],[
  ("(Pali Canon)","Dhammapada","c.250 BCE","Primary","Verses on the extinguishing of craving."),
  ("Bhikkhu Bodhi","In the Buddha's Words","2005","Intro","Source passages, thematically arranged."),
]),
"The Eightfold Path": (["The Buddha"],[
  ("(Pali Canon)","Magga-vibhaṅga Sutta","c.250 BCE","Primary","The eight factors, defined."),
  ("Bhikkhu Bodhi","The Noble Eightfold Path","1984","Intro","A practical, faithful walk-through."),
]),
"Non-Attachment": (["The Buddha","Patañjali"],[
  ("(Anonymous)","Bhagavad Gita","c.200 BCE","Primary","Action without clinging to results."),
  ("(Pali Canon)","Dhammapada","c.250 BCE","Primary","Letting go as the end of sorrow."),
]),
"Samsara & Moksha": (["Upanishadic sages","Patañjali"],[
  ("(Anonymous)","The Principal Upanishads","c.700 BCE","Primary","Bondage to rebirth and release from it."),
  ("(Anonymous)","Bhagavad Gita","c.200 BCE","Primary","Paths of action, devotion, and knowledge."),
]),
"Stoic Apatheia": (["Epictetus","Marcus Aurelius","Seneca"],[
  ("Epictetus","Discourses","c.108","Primary","Mastering judgment to free the mind."),
  ("Marcus Aurelius","Meditations","c.175","Primary","Daily practice of acceptance."),
]),
"Ataraxia": (["Epicurus","Pyrrho","Sextus Empiricus"],[
  ("Epicurus","Letter to Menoeceus","c.300 BCE","Primary","Calm as freedom from fear and pain."),
  ("Sextus Empiricus","Outlines of Pyrrhonism","c.200","Primary","Tranquility through suspended judgment."),
]),
"Denial of the Will": (["Arthur Schopenhauer"],[
  ("Arthur Schopenhauer","The World as Will and Representation","1818","Primary","Suffering from blind Will, and its denial."),
  ("Arthur Schopenhauer","Essays and Aphorisms","1851","Intro","The accessible late essays."),
]),
"The Absurd": (["Albert Camus"],[
  ("Albert Camus","The Myth of Sisyphus","1942","Primary","Camus on living without appeal in a silent universe — and the revolt that finds joy without pretending the silence answers."),
  ("Albert Camus","The Rebel","1951","Primary","From the absurd to rebellion and limits."),
]),
"Logotherapy": (["Viktor Frankl"],[
  ("Viktor Frankl","Man's Search for Meaning","1946","Primary","Frankl's case from the camps: whoever holds a why can bear almost any how — meaning found, not handed down."),
]),
"Flow": (["Mihály Csíkszentmihályi"],[
  ("Mihály Csíkszentmihályi","Flow: The Psychology of Optimal Experience","1990","Primary","Absorption as the shape of well-being."),
]),
# ---------------- ABSOLUTE ----------------
"The Unmoved Mover": (["Aristotle"],[
  ("Aristotle","Metaphysics (Book XII)","c.350 BCE","Primary","The first cause that moves without moving."),
  ("Aristotle","Physics (Book VIII)","c.350 BCE","Primary","Why motion needs a first source."),
]),
"The One": (["Plotinus","Proclus"],[
  ("Plotinus","The Enneads","c.270","Primary","All things emanate from, and yearn for, the One."),
]),
"The Ontological Argument": (["Anselm of Canterbury","Alvin Plantinga"],[
  ("Anselm of Canterbury","Proslogion","1078","Primary","That than which none greater can be conceived."),
  ("Alvin Plantinga","The Nature of Necessity","1974","Study","The modern modal reformulation."),
]),
"The Five Ways": (["Thomas Aquinas"],[
  ("Thomas Aquinas","Summa Theologiae (I, Q.2)","c.1270","Primary","Five rational paths to God."),
]),
"Pantheism": (["Baruch Spinoza"],[
  ("Baruch Spinoza","Ethics","1677","Primary","'Deus sive Natura' — God, or Nature."),
]),
"Pascal's Wager": (["Blaise Pascal"],[
  ("Blaise Pascal","Pensées","1670","Primary","Belief framed as a rational bet."),
]),
"Via Negativa": (["Pseudo-Dionysius","Maimonides","Meister Eckhart"],[
  ("Pseudo-Dionysius","The Mystical Theology","c.500","Primary","Knowing God by unsaying."),
  ("Maimonides","The Guide for the Perplexed","1190","Primary","Negative attributes of the divine."),
]),
"The Death of God": (["Friedrich Nietzsche"],[
  ("Friedrich Nietzsche","The Gay Science (§125)","1882","Primary","The madman's announcement."),
  ("Friedrich Nietzsche","Thus Spoke Zarathustra","1883","Primary","Living after the old values fall."),
]),
"Non-Theistic Absolute": (["Nāgārjuna","Chandrakīrti"],[
  ("Nāgārjuna","Mūlamadhyamakakārikā","c.200","Primary","An ultimate that is no creator-ground."),
  ("Jay Garfield (trans.)","The Fundamental Wisdom of the Middle Way","1995","Translation","Translation with commentary."),
]),
}

if __name__ == "__main__":
    print("concepts covered:", len(DATA))
