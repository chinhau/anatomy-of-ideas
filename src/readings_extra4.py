# -*- coding: utf-8 -*-
"""Thinkers + ranked readings for expand4.py (the literary canon + de Beauvoir).

For composite / oral works (the Gita, the Sundiata epic) the 'thinkers' field
names the tradition or traditional ascription rather than a sole author.
"""

EXTRA4 = {
# ---------- ANTIQUITY → ROMANTICISM ----------
"The Heroic Code": (["Homer"],[
  ("Homer","The Iliad","c.-750","Primary","Achilles and the glory that outlasts a short life."),
]),
"The Nostos": (["Homer"],[
  ("Homer","The Odyssey","c.-725","Primary","The long way home as the truer measure of a life."),
]),
"The Tragic Flaw": (["Sophocles"],[
  ("Sophocles","Oedipus Rex","c.-429","Primary","The fall that turns on a single blind error."),
  ("Aristotle","Poetics","c.-335","Study","Where hamartia and catharsis are named."),
]),
"Antigone's Law": (["Sophocles"],[
  ("Sophocles","Antigone","c.-441","Primary","Unwritten law against the edict of the state."),
]),
"Hubris and Nemesis": (["Aeschylus"],[
  ("Aeschylus","The Persians","-472","Primary","Pride overreaches and the balance falls."),
  ("Aeschylus","The Oresteia","-458","Primary","The long working-out of justice and retribution."),
]),
"Carpe Diem": (["Horace"],[
  ("Horace","Odes, I.11","c.-23","Primary","'Seize the day, trusting tomorrow as little as you can.'"),
]),
"The Descent and Return": (["Virgil"],[
  ("Virgil","The Aeneid, Book VI","c.-19","Primary","The journey through the underworld and back."),
]),
"Love That Moves the Stars": (["Dante Alighieri"],[
  ("Dante Alighieri","The Divine Comedy: Paradiso","c.1320","Primary","'The Love that moves the sun and the other stars.'"),
  ("Dante Alighieri","The Divine Comedy: Inferno","c.1314","Intro","The descent that opens the whole journey."),
]),
"The Quixotic Ideal": (["Miguel de Cervantes"],[
  ("Miguel de Cervantes","Don Quixote","1605","Primary","The ideal that ennobles the deluded knight."),
]),
"Hamlet's Doubt": (["William Shakespeare"],[
  ("William Shakespeare","Hamlet","c.1601","Primary","Thought that 'unstrings' the will to act."),
]),
"Theatre of the World": (["William Shakespeare"],[
  ("William Shakespeare","As You Like It","c.1599","Primary","'All the world's a stage' — the seven ages of man."),
]),
"The Heroic Rebel": (["John Milton"],[
  ("John Milton","Paradise Lost","1667","Primary","Satan's defiant 'better to reign in Hell.'"),
]),
"Marriage of Heaven and Hell": (["William Blake"],[
  ("William Blake","The Marriage of Heaven and Hell","1790","Primary","'Without contraries is no progression.'"),
]),
"The Modern Prometheus": (["Mary Shelley"],[
  ("Mary Shelley","Frankenstein; or, The Modern Prometheus","1818","Primary","The creator undone by what he makes."),
]),
"Faustian Striving": (["Johann Wolfgang von Goethe"],[
  ("Johann Wolfgang von Goethe","Faust, Part One","1808","Primary","The wager on restless, endless striving."),
  ("Johann Wolfgang von Goethe","Faust, Part Two","1832","Primary","Striving redeemed at the last."),
]),
"Negative Capability": (["John Keats"],[
  ("John Keats","Selected Letters (to George and Tom Keats, Dec. 1817)","1817","Primary","Dwelling 'in uncertainties, mysteries, doubts.'"),
]),
"Spontaneous Overflow": (["William Wordsworth"],[
  ("William Wordsworth","Preface to Lyrical Ballads","1800","Primary","Poetry as feeling 'recollected in tranquillity.'"),
]),

# ---------- MODERN & CONTEMPORARY ----------
"The Underground Man": (["Fyodor Dostoevsky"],[
  ("Fyodor Dostoevsky","Notes from Underground","1864","Primary","Spite that chooses against its own interest, to be free."),
]),
"The Grand Inquisitor": (["Fyodor Dostoevsky"],[
  ("Fyodor Dostoevsky","The Brothers Karamazov","1880","Primary","The parable of freedom traded for bread and authority."),
]),
"Ivan Ilyich's Mirror": (["Leo Tolstoy"],[
  ("Leo Tolstoy","The Death of Ivan Ilyich","1886","Primary","A respectable life exposed as a lie by dying."),
]),
"The Inscrutable Whale": (["Herman Melville"],[
  ("Herman Melville","Moby-Dick","1851","Primary","The blank, indifferent mask we read for meaning."),
]),
"Involuntary Memory": (["Marcel Proust"],[
  ("Marcel Proust","In Search of Lost Time: Swann's Way","1913","Primary","The madeleine and the past returning whole."),
]),
"The Metamorphosis": (["Franz Kafka"],[
  ("Franz Kafka","The Metamorphosis","1915","Primary","Stripped of use, the self becomes vermin to its own."),
]),
"The Faceless Law": (["Franz Kafka"],[
  ("Franz Kafka","The Trial","1925","Primary","Condemned by a law one can never reach or read."),
]),
"The Infinite Library": (["Jorge Luis Borges"],[
  ("Jorge Luis Borges","The Library of Babel (in Ficciones)","1941","Primary","Every possible book, and so total noise."),
]),
"Funes the Memorious": (["Jorge Luis Borges"],[
  ("Jorge Luis Borges","Funes the Memorious (in Ficciones)","1942","Primary","Total memory that makes thought impossible."),
]),
"The Soma Solution": (["Aldous Huxley"],[
  ("Aldous Huxley","Brave New World","1932","Primary","A people pacified by pleasure, not pain."),
]),
"The Ministry of Truth": (["George Orwell"],[
  ("George Orwell","Nineteen Eighty-Four","1949","Primary","Rewriting the past, shrinking language until dissent is unthinkable."),
]),
"Rememory": (["Toni Morrison"],[
  ("Toni Morrison","Beloved","1987","Primary","The traumatic past as a place that will not stay past."),
]),
"The Ones Who Walk Away": (["Ursula K. Le Guin"],[
  ("Ursula K. Le Guin","The Ones Who Walk Away from Omelas","1973","Primary","The happiness that rests on one child's torment."),
]),
"The Handmaid's Body": (["Margaret Atwood"],[
  ("Margaret Atwood","The Handmaid's Tale","1985","Primary","A theocracy that reduces women to wombs."),
]),
"Story of Your Life": (["Ted Chiang"],[
  ("Ted Chiang","Story of Your Life (in Stories of Your Life and Others)","1998","Primary","Foreknowledge lived freely and at once."),
]),

# ---------- GLOBAL & WOMEN WRITERS ----------
"Mono no Aware": (["Murasaki Shikibu"],[
  ("Murasaki Shikibu","The Tale of Genji","c.1010","Primary","The pathos of passing things, the world's first novel."),
]),
"The Disinterested Deed": (["Vyasa (attrib.)"],[
  ("Vyasa (trad. ascription)","The Bhagavad Gita (within the Mahabharata)","c.-200","Primary","Action without attachment to its fruits."),
]),
"The Conference of the Birds": (["Attar of Nishapur"],[
  ("Farid ud-Din Attar","The Conference of the Birds","1177","Primary","The seeker that turns out to be the sought."),
]),
"The Servile Will": (["Omar Khayyam"],[
  ("Omar Khayyam","Rubáiyát (Edward FitzGerald, trans.)","c.1120","Primary","Pieces moved across the board of fate."),
]),
"Bhakti": (["Mirabai"],[
  ("Mirabai","Collected Bhajans / Padavali","c.1540","Primary","Ecstatic devotion that overrides caste and shame."),
]),
"Yūgen": (["Matsuo Bashō"],[
  ("Matsuo Bashō","The Narrow Road to the Deep North (Oku no Hosomichi)","c.1694","Primary","The eternal flashing in the ordinary instant."),
  ("Matsuo Bashō","Frog Haiku","1686","Intro","'Old pond — a frog leaps in, the sound of water.'"),
]),
"Destiny Through Adversity": (["Epic of Sundiata (Mande griot tradition)"],[
  ("Mande griot tradition (D. T. Niane, transcr.)","Sundiata: An Epic of Old Mali","c.1235","Primary","The crippled child who rises to found an empire."),
]),
"A Madman's Diary": (["Lu Xun"],[
  ("Lu Xun","A Madman's Diary","1918","Primary","Tradition seen as a society that eats its own."),
]),
"Negritude": (["Aimé Césaire"],[
  ("Aimé Césaire","Notebook of a Return to the Native Land","1939","Primary","Blackness reclaimed as a positive, shared value."),
]),
"Things Fall Apart": (["Chinua Achebe"],[
  ("Chinua Achebe","Things Fall Apart","1958","Primary","A coherent African world, shattered by colonialism."),
]),
"Solitude as Origin": (["Gabriel García Márquez"],[
  ("Gabriel García Márquez","One Hundred Years of Solitude","1967","Primary","A walled-off lineage doomed to repeat its fate."),
]),

# ---------- de Beauvoir (philosophy, not lit) ----------
"Woman as the Other": (["Simone de Beauvoir"],[
  ("Simone de Beauvoir","The Second Sex","1949","Primary","'One is not born, but rather becomes, a woman.'"),
]),
}

if __name__ == "__main__":
    print("round-four concepts covered:", len(EXTRA4))
