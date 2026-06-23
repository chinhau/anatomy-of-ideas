# -*- coding: utf-8 -*-
"""Round-four expansion: the literary & imaginative canon.

Adds the "lit" tradition — ideas whose native medium is the artwork (epic,
poem, play, novel, parable): philosophy *enacted* in a story rather than
*argued* in a treatise. These figures enter by the same rule as everyone
else — a single idea sharp enough to name — not by fame. The badge marks a
method, not a lesser rank.

Also fills one long-standing gap with a proper concept: Simone de Beauvoir,
who until now appeared only as a secondary thinker.

Imports `expand3` (which has already applied rounds 1-3 and rebuilt) and
extends further, then rebuilds once more so ideas.json carries everything.
"""
import concepts
import expand    # round one
import expand2   # round two
import expand3   # round three

concepts.TRAD.update({"lit": "Literature & Imagination"})

# ---- the literary canon: (id, qid, trad, era, gloss, thinkers) ----
NEW_C4 = [
 # ---------- ANTIQUITY → ROMANTICISM (West) ----------
 ("The Heroic Code","mean","lit",-750,"A mortal life wins meaning by earning undying glory; we trade length of days for a deathless name.",["Homer"]),
 ("The Nostos","mean","lit",-725,"The deepest longing is not glory but return — to home, hearth, and the self one left behind.",["Homer"]),
 ("The Tragic Flaw","peace","lit",-429,"A great soul falls not through vice but a single fatal error; suffering is how we come to see.",["Sophocles"]),
 ("Antigone's Law","just","lit",-441,"An unwritten higher law can outrank the state's command; conscience may rightly defy power.",["Sophocles"]),
 ("Hubris and Nemesis","live","lit",-458,"Overreaching pride invites a balancing fall; the order of things corrects those who forget they are mortal.",["Aeschylus"]),
 ("Carpe Diem","live","lit",-23,"Seize the day; since death is certain and tomorrow unowned, gather life's joys now.",["Horace"]),
 ("The Descent and Return","trans","lit",-19,"To be remade you must first go down into the dark and face the dead.",["Virgil"]),
 ("Love That Moves the Stars","abs","lit",1320,"The same Love that draws the soul upward moves the sun and stars; the cosmos is ordered by desire for God.",["Dante Alighieri"]),
 ("The Quixotic Ideal","know","lit",1605,"A noble illusion can ennoble the dreamer; idealism and madness blur where the world mocks the ideal.",["Miguel de Cervantes"]),
 ("Hamlet's Doubt","self","lit",1601,"Consciousness turned upon itself can paralyse action; thinking too precisely on the event unstrings the will.",["William Shakespeare"]),
 ("Theatre of the World","self","lit",1599,"All the world's a stage; identity is the sequence of parts we play, not a fixed core beneath.",["William Shakespeare"]),
 ("The Heroic Rebel","free","lit",1667,"Better to reign in Hell than serve in Heaven; the will to refuse can outshine obedience.",["John Milton"]),
 ("Marriage of Heaven and Hell","real","lit",1790,"Energy and reason, good and evil are necessary contraries; without contraries there is no progression.",["William Blake"]),
 ("The Modern Prometheus","trans","lit",1818,"To seize the power to create life is to unleash what we cannot govern; the maker is undone by the made.",["Mary Shelley"]),
 ("Faustian Striving","mean","lit",1808,"Endless striving redeems us; whoever strives on without rest, even erring, may yet be saved.",["Johann Wolfgang von Goethe"]),
 ("Negative Capability","know","lit",1817,"The deepest knowing rests easy in uncertainty and mystery, without irritable reaching after fact and reason.",["John Keats"]),
 ("Spontaneous Overflow","mind","lit",1800,"Poetry is the spontaneous overflow of powerful feeling, recollected in tranquillity; imagination remakes experience.",["William Wordsworth"]),

 # ---------- MODERN & CONTEMPORARY (West) ----------
 ("The Underground Man","self","lit",1864,"A spiteful inner voice insists we will act against our own interest just to prove we are free.",["Fyodor Dostoevsky"]),
 ("The Grand Inquisitor","free","lit",1880,"People flee the burden of freedom; they will trade liberty for bread, mystery, and authority.",["Fyodor Dostoevsky"]),
 ("Ivan Ilyich's Mirror","mean","lit",1886,"A dying man discovers his whole respectable life was a lie — and only now begins to live.",["Leo Tolstoy"]),
 ("The Inscrutable Whale","abs","lit",1851,"Nature wears a blank, indifferent mask; we hurl meaning at it and it stares back, unreadable.",["Herman Melville"]),
 ("Involuntary Memory","mind","lit",1913,"The deep past returns whole and unbidden through a taste or scent, beyond the reach of willed recall.",["Marcel Proust"]),
 ("The Metamorphosis","self","lit",1915,"Stripped of his use, a man becomes vermin to his own family; identity is what others can still use.",["Franz Kafka"]),
 ("The Faceless Law","just","lit",1925,"Guilt needs no crime; an unreachable authority condemns us by a law we can never read.",["Franz Kafka"]),
 ("The Infinite Library","know","lit",1941,"All possible books already exist; total knowledge and total noise become indistinguishable.",["Jorge Luis Borges"]),
 ("Funes the Memorious","mind","lit",1942,"Perfect, total memory destroys thought; to think at all is to forget differences and abstract.",["Jorge Luis Borges"]),
 ("The Soma Solution","live","lit",1932,"Tyranny by pleasure: a people pacified not by pain but by comfort, distraction, and a perfect drug.",["Aldous Huxley"]),
 ("The Ministry of Truth","just","lit",1949,"Power rewrites the past and shrinks language until dissent becomes literally unthinkable.",["George Orwell"]),
 ("Rememory","self","lit",1987,"The traumatic past is not gone but a place that persists; the self must re-member what it was forced to dismember.",["Toni Morrison"]),
 ("The Ones Who Walk Away","just","lit",1973,"A perfect city rests on one child's torment; the just refuse the bargain and simply walk away.",["Ursula K. Le Guin"]),
 ("The Handmaid's Body","just","lit",1985,"Patriarchy perfected: a theocracy that reduces women to wombs and renames the theft a sacred duty.",["Margaret Atwood"]),
 ("Story of Your Life","free","lit",1998,"To know your whole future is not to escape it; you live it freely and foreknown at once.",["Ted Chiang"]),

 # ---------- GLOBAL & WOMEN WRITERS ----------
 ("Mono no Aware","mean","lit",1010,"The pathos of things: beauty is precious because it passes, and grief is the proof we loved the world.",["Murasaki Shikibu"]),
 ("The Disinterested Deed","live","lit",-200,"Act for the act's own sake; do your duty wholly, yet renounce all claim upon its fruits.",["Vyasa (attrib.)"]),
 ("The Conference of the Birds","abs","lit",1177,"Thirty birds cross seven valleys to find their king — and discover the sought is the seeker itself.",["Attar of Nishapur"]),
 ("The Servile Will","free","lit",1120,"The cup of fate is poured before we taste it; we are pieces moved across the board, then dropped in the box.",["Omar Khayyam"]),
 ("Bhakti","abs","lit",1540,"The soul as the god's lover: an ecstatic, personal surrender that overrides caste, marriage, and shame.",["Mirabai"]),
 ("Yūgen","mean","lit",1686,"The eternal flashes in the ordinary instant — an old pond, a frog's plunge, the sound of water.",["Matsuo Bashō"]),
 ("Destiny Through Adversity","live","lit",1235,"The crippled child who cannot walk becomes king; greatness is forged against obstacles, not in their absence.",["Epic of Sundiata (Mande griot tradition)"]),
 ("A Madman's Diary","just","lit",1918,"A lone sane man sees that the society around him is the cannibal; to save the children is to refuse inherited cruelty.",["Lu Xun"]),
 ("Negritude","self","lit",1939,"Blackness reclaimed as a positive value and a shared poetic consciousness against the colonizer's gaze.",["Aimé Césaire"]),
 ("Things Fall Apart","just","lit",1958,"Every society has its own logic and dignity; colonialism shatters it not by argument but by uprooting meaning.",["Chinua Achebe"]),
 ("Solitude as Origin","self","lit",1967,"A lineage walled off from the world is doomed to repeat itself; isolation breeds the same fate over and over.",["Gabriel García Márquez"]),
]
concepts.C.extend(NEW_C4)

# ---- one overdue philosopher concept (not lit): Simone de Beauvoir ----
NEW_C4_PHIL = [
 ("Woman as the Other","self","phe",1949,"One is not born, but becomes, a woman; she is cast as man's Other, never the absolute subject.",["Simone de Beauvoir"]),
]
concepts.C.extend(NEW_C4_PHIL)

# ---- links: (a, b, type)  builds / rejects / echoes ----
NEW_R4 = [
 # antiquity → romanticism
 ("The Heroic Code","Eudaimonia","echoes"),
 ("The Nostos","The Heroic Code","rejects"),
 ("The Tragic Flaw","Hubris and Nemesis","builds"),
 ("The Tragic Flaw","Four Noble Truths","echoes"),
 ("Antigone's Law","Social Contract","rejects"),
 ("Satyagraha","Antigone's Law","echoes"),
 ("Hubris and Nemesis","The Golden Mean","echoes"),
 ("Carpe Diem","Epicurean Pleasure","builds"),
 ("Carpe Diem","Amor Fati","echoes"),
 ("The Descent and Return","Samsara & Moksha","echoes"),
 ("The Descent and Return","The Art of Dying","echoes"),
 ("Love That Moves the Stars","The Five Ways","builds"),
 ("Love That Moves the Stars","The One","echoes"),
 ("The Quixotic Ideal","Allegory of the Cave","echoes"),
 ("Hamlet's Doubt","The Cogito","echoes"),
 ("The Presentation of Self","Theatre of the World","builds"),
 ("The Heroic Rebel","Condemned to be Free","echoes"),
 ("The Heroic Rebel","Master & Slave Morality","echoes"),
 ("Marriage of Heaven and Hell","Yin–Yang / Qi","echoes"),
 ("The Modern Prometheus","Hubris and Nemesis","builds"),
 ("Faustian Striving","The Modern Prometheus","echoes"),
 ("Faustian Striving","Self-Actualization","echoes"),
 ("Negative Capability","Skepticism","echoes"),
 ("Spontaneous Overflow","Stream of Consciousness","echoes"),
 ("Spontaneous Overflow","Self-Reliance","echoes"),
 # modern & contemporary
 ("Existential Self","The Underground Man","builds"),
 ("The Underground Man","Hard Determinism","rejects"),
 ("The Underground Man","Condemned to be Free","echoes"),
 ("The Grand Inquisitor","Condemned to be Free","rejects"),
 ("The Grand Inquisitor","The Death of God","echoes"),
 ("Ivan Ilyich's Mirror","Being-toward-Death","echoes"),
 ("Ivan Ilyich's Mirror","Authenticity","builds"),
 ("The Inscrutable Whale","The Death of God","echoes"),
 ("The Inscrutable Whale","The Absurd","echoes"),
 ("Involuntary Memory","Stream of Consciousness","echoes"),
 ("Involuntary Memory","Funes the Memorious","echoes"),
 ("The Metamorphosis","The Presentation of Self","echoes"),
 ("The Metamorphosis","The Faceless Law","echoes"),
 ("The Faceless Law","Power/Knowledge","echoes"),
 ("The Faceless Law","The Ministry of Truth","echoes"),
 ("The Infinite Library","Idealism","echoes"),
 ("Funes the Memorious","Tabula Rasa","rejects"),
 ("The Soma Solution","The Ministry of Truth","rejects"),
 ("The Soma Solution","The Burnout Society","echoes"),
 ("The Ministry of Truth","Power/Knowledge","builds"),
 ("The Ministry of Truth","Shared Fictions","echoes"),
 ("Rememory","The Unconscious","echoes"),
 ("Rememory","The Denial of Death","echoes"),
 ("The Ones Who Walk Away","Utilitarianism","rejects"),
 ("The Ones Who Walk Away","Justice as Fairness","echoes"),
 ("The Handmaid's Body","Gender Performativity","echoes"),
 ("The Handmaid's Body","Woman as the Other","builds"),
 ("Story of Your Life","Hard Determinism","echoes"),
 ("Story of Your Life","Amor Fati","echoes"),
 # global & women writers
 ("Mono no Aware","Non-Attachment","echoes"),
 ("Mono no Aware","Yūgen","echoes"),
 ("The Disinterested Deed","Karma","builds"),
 ("The Disinterested Deed","Wu Wei","echoes"),
 ("The Conference of the Birds","Mystical Union (Fana)","builds"),
 ("The Conference of the Birds","Brahman","echoes"),
 ("The Servile Will","Hard Determinism","echoes"),
 ("The Servile Will","Karma","rejects"),
 ("Bhakti","Mystical Union (Fana)","echoes"),
 ("Bhakti","Brahman","rejects"),
 ("Yūgen","Wu Wei","echoes"),
 ("Yūgen","Flow","echoes"),
 ("Destiny Through Adversity","Amor Fati","echoes"),
 ("Destiny Through Adversity","Eudaimonia","echoes"),
 ("A Madman's Diary","Government by Virtue","rejects"),
 ("A Madman's Diary","Things Fall Apart","echoes"),
 ("Negritude","Things Fall Apart","echoes"),
 ("Negritude","Master & Slave Morality","echoes"),
 ("Things Fall Apart","Power/Knowledge","echoes"),
 ("Solitude as Origin","Eternal Recurrence","echoes"),
 ("Solitude as Origin","Relational Self","rejects"),
 # de Beauvoir
 ("Gender Performativity","Woman as the Other","builds"),
 ("Woman as the Other","Existential Self","builds"),
 ("Woman as the Other","Care Ethics","echoes"),
]
concepts.R.extend(NEW_R4)

concepts.main()
