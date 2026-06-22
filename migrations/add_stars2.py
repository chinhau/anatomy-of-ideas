# -*- coding: utf-8 -*-
"""Constellation reconciliation:
  1) upgrade 7 names to their correct diacritic form so the two layers agree on spelling
  2) add stars for the round-three thinkers, the new women, and the canonical figures
     that were ideas-only (so no thinker chip dead-ends)."""
import json
G=json.load(open('atlas_graph.json',encoding='utf-8'))

# --- 1) diacritic upgrades (rename node id + all link endpoints) ---
REN={"Nagarjuna":"Nāgārjuna","Dharmakirti":"Dharmakīrti","Dignaga":"Dignāga",
     "Mahavira":"Mahāvīra","Patanjali":"Patañjali","Vyasa":"Vyāsa",
     "Mihaly Csikszentmihalyi":"Mihály Csíkszentmihályi"}
for n in G['nodes']:
    if n['id'] in REN: n['id']=REN[n['id']]
for l in G['links']:
    if l['source'] in REN: l['source']=REN[l['source']]
    if l['target'] in REN: l['target']=REN[l['target']]

have={n['id'] for n in G['nodes']}

# --- 2) new stars: (id, group, dates, k, big) ---
NEW=[
 ("Emmanuel Levinas","phe","1906–1995","Ethics as first philosophy: the face of the Other lays an infinite claim on me.",True),
 ("Martin Buber","phe","1878–1965","Dialogical philosopher of I–Thou: we become persons only in genuine relation.",False),
 ("Carol Gilligan","pbc","1936–","Psychologist who recovered the 'different voice' of care in moral reasoning.",False),
 ("Nel Noddings","phu","1929–2022","Built an ethics and a pedagogy founded on caring relation.",False),
 ("Iris Murdoch","ana","1919–1999","Moral philosopher and novelist of attention and 'unselfing'.",True),
 ("Simone Weil","phe","1909–1943","Philosopher-mystic of attention, affliction and grace.",False),
 ("Martha Nussbaum","ana","1947–","Philosopher of capabilities, emotion and the fragility of goodness.",True),
 ("Amartya Sen","ana","1933–","Economist-philosopher; development as the expansion of real freedoms.",False),
 ("G.E.M. Anscombe","ana","1919–2001","Reopened virtue ethics and the philosophy of intention.",False),
 ("Philippa Foot","ana","1920–2010","Grounded virtue in human nature; first posed the trolley problem.",False),
 ("Alasdair MacIntyre","con","1929–2025","Communitarian critic of modern moralism; virtue needs tradition.",False),
 ("Thich Nhat Hanh","bud","1926–2022","Zen teacher who brought 'engaged Buddhism' and mindfulness West.",True),
 ("B.R. Ambedkar","ind","1891–1956","Jurist who reframed Buddhism as a path of social liberation.",False),
 ("Mary Wollstonecraft","enl","1759–1797","Founder of liberal feminism; extended natural rights to women.",True),
 ("Karma Lingpa","bud","1326–1386","The tertön who revealed the Bardo Thödol.",False),
 ("Alfred North Whitehead","ana","1861–1947","Process philosopher; reality as becoming, not static substance.",False),
 ("Meister Eckhart","med","c.1260–1328","Christian mystic of the soul's union with the Godhead.",False),
 ("Anselm of Canterbury","med","1033–1109","Scholastic who argued God's existence from the idea of God.",False),
 ("Harry Frankfurt","ana","1929–2023","Theorist of free will, higher-order desires and caring.",False),
 ("Sam Harris","ana","1967–","Neuroscientist-philosopher; critic of free will and of religion.",False),
 ("Linji Yixuan","chn","d.866","Founder of the Rinzai line of Chan; teacher of shock and immediacy.",False),
 ("Li Si","chn","c.280–208 BCE","Legalist chancellor who built the Qin's centralized order.",False),
 ("Zou Yan","chn","c.305–240 BCE","Systematizer of yin–yang and the five phases.",False),
]
added=0
for nid,grp,dates,k,big in NEW:
    if nid in have: continue
    G['nodes'].append({"id":nid,"group":grp,"type":"person","dates":dates,"k":k,"deg":0,"big":big})
    have.add(nid); added+=1

LINKS=[
 ("Emmanuel Levinas","Phenomenology","member"),("Martin Buber","Emmanuel Levinas","influence"),
 ("Edmund Husserl","Emmanuel Levinas","influence"),
 ("Martin Buber","Existentialism","member"),
 ("Carol Gilligan","Developmental Psychology","member"),
 ("Nel Noddings","Humanistic Psychology","member"),("Carol Gilligan","Nel Noddings","influence"),
 ("Plato","Iris Murdoch","influence"),("Simone Weil","Iris Murdoch","influence"),
 ("Plato","Simone Weil","influence"),
 ("Aristotle","Martha Nussbaum","influence"),("Amartya Sen","Martha Nussbaum","collab"),
 ("G.E.M. Anscombe","Ordinary Language Philosophy","member"),
 ("Ludwig Wittgenstein","G.E.M. Anscombe","influence"),
 ("G.E.M. Anscombe","Philippa Foot","influence"),
 ("Aristotle","Alasdair MacIntyre","influence"),
 ("Thich Nhat Hanh","Zen / Chan","member"),("Early Buddhism","B.R. Ambedkar","influence"),
 ("Mary Wollstonecraft","Enlightenment","member"),
 ("Karma Lingpa","Vajrayana","member"),("Padmasambhava","Karma Lingpa","influence"),
 ("Bertrand Russell","Alfred North Whitehead","collab"),
 ("Meister Eckhart","Scholasticism","member"),("Anselm of Canterbury","Scholasticism","member"),
 ("Sam Harris","Daniel Dennett","opposed"),("Harry Frankfurt","Sam Harris","opposed"),
 ("Linji Yixuan","Zen / Chan","member"),("Li Si","Legalism","member"),
 ("Zou Yan","Daoism","influence"),
]
pairs={(l['source'],l['target'],l['type']) for l in G['links']}
ladded=0
for a,b,t in LINKS:
    if a in have and b in have and (a,b,t) not in pairs:
        G['links'].append({"source":a,"target":b,"type":t}); ladded+=1

deg={n['id']:0 for n in G['nodes']}
for l in G['links']: deg[l['source']]+=1; deg[l['target']]+=1
for n in G['nodes']: n['deg']=deg[n['id']]
iso=[n['id'] for n in G['nodes'] if n['deg']==0]
json.dump(G,open('atlas_graph.json','w',encoding='utf-8'),ensure_ascii=False)
print(f"diacritic renames:{len(REN)} stars added:{added} links added:{ladded}")
print(f"constellation: {len(G['nodes'])} nodes {len(G['links'])} links | isolates: {iso or 'none'}")
