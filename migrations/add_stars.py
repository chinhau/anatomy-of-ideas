# -*- coding: utf-8 -*-
"""Add the new thinkers (the three clusters + the latest voices + the
consciousness figures that were ideas-only) as stars in the constellation,
wire sensible links, and recompute node degrees."""
import json

G = json.load(open('atlas_graph.json', encoding='utf-8'))
have = {n['id'] for n in G['nodes']}
schools = {n['id'] for n in G['nodes'] if n['type']=='school'}

# id, group, dates, k, big
NEW = [
 # performance trap
 ("Guy Debord","con","1931–1994","Situationist who saw modern life as a 'society of the spectacle' where images replace lived experience.",True),
 ("Byung-Chul Han","con","1959–","Korean-German critic of the 'burnout society': in the name of freedom, we exploit ourselves.",True),
 ("Mark Fisher","con","1968–2017","Diagnosed 'capitalist realism' — the sense there is no alternative — and its mental-health toll.",False),
 ("Erving Goffman","pbc","1922–1982","Sociologist who saw the self as a performance staged for others, front-stage and back.",True),
 ("David Graeber","con","1961–2020","Anthropologist who coined 'bullshit jobs' and rethought debt, work and value.",False),
 # withdrawal
 ("Diogenes","grk","c.412–323 BCE","The Cynic who lived in a jar and mocked convention — freedom through radical self-sufficiency.",False),
 # death
 ("Ernest Becker","phu","1924–1974","Argued civilization is a vast defense against the terror of death.",False),
 # consciousness / latest
 ("David Chalmers","ana","1966–","Framed the 'hard problem' of consciousness and defended the reality of experience.",True),
 ("Thomas Nagel","ana","1937–","Asked what it is like to be a bat — subjectivity resists objective reduction.",True),
 ("Thomas Metzinger","ana","1958–","Argues no one ever had a self — only a transparent 'ego tunnel'.",False),
 ("Derek Parfit","ana","1942–2017","Argued personal identity 'is not what matters' — a Western echo of no-self.",True),
 ("Andy Clark","ana","1957–","Philosopher of the extended and predictive mind.",False),
 ("Bernardo Kastrup","ana","1974–","Defends analytic idealism: reality is fundamentally mental.",False),
 ("Anil Seth","pbc","1972–","Neuroscientist: consciousness as a 'controlled hallucination' of predictive brains.",False),
 ("Donald Hoffman","pbc","1955–","Cognitive scientist: perception is a fitness-tuned interface, not a window on truth.",False),
 ("Iain McGilchrist","pbc","1953–","Psychiatrist of the divided brain and its two ways of being.",False),
 ("Benjamin Libet","pbc","1916–2007","Whose readiness-potential experiments challenged conscious free will.",False),
 ("Bernard Baars","pbc","1946–","Proposed the global-workspace theory of consciousness.",False),
 ("Stanislas Dehaene","pbc","1965–","Maps the 'global neuronal workspace' — how information becomes conscious.",False),
 ("Giulio Tononi","pbc","1960–","Built Integrated Information Theory: consciousness is integrated information.",False),
 ("Christof Koch","pbc","1956–","Pursues the neural correlates of consciousness; champion of IIT.",False),
 ("Douglas Hofstadter","pbc","1945–","Sees the self as a 'strange loop' — a pattern that refers to itself.",False),
 ("Francisco Varela","pbc","1946–2001","Co-founded enactivism; bridged cognitive science and Buddhist practice.",False),
 ("Norbert Wiener","pbc","1894–1964","Founded cybernetics — control and communication by feedback.",False),
 ("Yuval Noah Harari","con","1976–","Historian: humans cooperate at scale through shared fictions.",True),
 ("Christine Rosen","con","fl. 2020s","Critic of disembodied digital life and the 'extinction of experience'.",False),
 # earlier-round figures missing as stars
 ("Ibn Arabi","med","1165–1240","Sufi metaphysician of waḥdat al-wujūd, the unity of all being.",False),
 ("Jon Kabat-Zinn","phu","1944–","Adapted Buddhist mindfulness into clinical MBSR.",False),
 ("Steven Hayes","pbc","1948–","Developed Acceptance and Commitment Therapy and psychological flexibility.",False),
 ("Charles Darwin","c19","1809–1882","Natural selection: design without a designer, reframing life and mind.",True),
]

added = 0
for nid, grp, dates, k, big in NEW:
    if nid in have: continue
    G['nodes'].append({"id":nid,"group":grp,"type":"person","dates":dates,"k":k,"deg":0,"big":big})
    have.add(nid); added += 1

# links: (a, b, type) — only added if both endpoints exist
LINKS = [
 ("Diogenes","Cynicism","member"),("Diogenes","Stoicism","influence"),
 ("Guy Debord","Marxism","member"),("Karl Marx","Guy Debord","influence"),
 ("Michel Foucault","Byung-Chul Han","influence"),("Martin Heidegger","Byung-Chul Han","influence"),
 ("Herbert Marcuse","Mark Fisher","influence"),("Jean Baudrillard","Mark Fisher","influence"),
 ("Karl Marx","Mark Fisher","influence"),
 ("Erving Goffman","Social Psychology","member"),("Erving Goffman","Judith Butler","influence"),
 ("David Graeber","Karl Marx","influence"),
 ("Ernest Becker","Existential Psychology","member"),("Sigmund Freud","Ernest Becker","influence"),
 ("Martin Heidegger","Ernest Becker","influence"),
 ("David Chalmers","Analytic Philosophy","member"),("Thomas Nagel","David Chalmers","influence"),
 ("Thomas Nagel","Analytic Philosophy","member"),
 ("David Chalmers","Daniel Dennett","opposed"),("John Searle","Daniel Dennett","opposed"),
 ("Thomas Metzinger","Analytic Philosophy","member"),
 ("Derek Parfit","Analytic Philosophy","member"),("Derek Parfit","Early Buddhism","influence"),
 ("Andy Clark","Analytic Philosophy","member"),("Anil Seth","Andy Clark","collab"),
 ("Bernardo Kastrup","Analytic Philosophy","member"),
 ("Anil Seth","Cognitive Psychology","member"),("Donald Hoffman","Cognitive Psychology","member"),
 ("Iain McGilchrist","Cognitive Psychology","member"),("Benjamin Libet","Cognitive Psychology","member"),
 ("Bernard Baars","Cognitive Psychology","member"),("Stanislas Dehaene","Cognitive Psychology","member"),
 ("Bernard Baars","Stanislas Dehaene","influence"),
 ("Giulio Tononi","Cognitive Psychology","member"),("Christof Koch","Cognitive Psychology","member"),
 ("Giulio Tononi","Christof Koch","collab"),
 ("Douglas Hofstadter","Cognitive Psychology","member"),
 ("Francisco Varela","Cognitive Psychology","member"),("Early Buddhism","Francisco Varela","influence"),
 ("Norbert Wiener","Cognitive Psychology","influence"),
 ("Yuval Noah Harari","Charles Darwin","influence"),
 ("Ibn Arabi","Sufism","member"),
 ("Jon Kabat-Zinn","Humanistic Psychology","member"),("Early Buddhism","Jon Kabat-Zinn","influence"),
 ("Steven Hayes","Cognitive Psychology","member"),
 ("Charles Darwin","Functionalism (Psych)","influence"),("Charles Darwin","William James","influence"),
]
existing_pairs = {(l['source'],l['target'],l['type']) for l in G['links']}
ladded = 0
for a,b,t in LINKS:
    if a in have and b in have and (a,b,t) not in existing_pairs:
        G['links'].append({"source":a,"target":b,"type":t}); ladded += 1

# recompute degree
deg = {n['id']:0 for n in G['nodes']}
for l in G['links']:
    deg[l['source']] = deg.get(l['source'],0)+1
    deg[l['target']] = deg.get(l['target'],0)+1
for n in G['nodes']:
    n['deg'] = deg.get(n['id'],0)

json.dump(G, open('atlas_graph.json','w',encoding='utf-8'), ensure_ascii=False)
print(f"stars added: {added}  links added: {ladded}")
print(f"constellation now: {len(G['nodes'])} nodes, {len(G['links'])} links")
