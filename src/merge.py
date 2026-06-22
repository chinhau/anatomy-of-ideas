# -*- coding: utf-8 -*-
import json
from readings import DATA as _RD
from readings_extra import EXTRA as _EX
from readings_extra2 import EXTRA2 as _EX2
from readings_extra3 import EXTRA3 as _EX3
RD = {**_RD, **_EX, **_EX2, **_EX3}

ideas = json.load(open('ideas.json', encoding='utf-8'))
ids = {c['id'] for c in ideas['concepts']}

# coverage checks
missing = sorted(ids - set(RD.keys()))
extra   = sorted(set(RD.keys()) - ids)
if missing:
    raise SystemExit("NO READINGS for: " + ", ".join(missing))
if extra:
    raise SystemExit("READINGS reference unknown concept: " + ", ".join(extra))

for c in ideas['concepts']:
    thinkers, readings = RD[c['id']]
    c['thinkers'] = thinkers
    c['readings'] = [
        {"author": a, "title": t, "year": y, "kind": k, "note": n}
        for (a, t, y, k, n) in readings
    ]

json.dump(ideas, open('ideas.json','w',encoding='utf-8'), ensure_ascii=False)

tn = sum(len(c['thinkers']) for c in ideas['concepts'])
rn = sum(len(c['readings']) for c in ideas['concepts'])
print(f"Merged. concepts={len(ideas['concepts'])} thinkers(total)={tn} readings(total)={rn}")
print(f"avg thinkers/concept={tn/len(ideas['concepts']):.1f} avg readings/concept={rn/len(ideas['concepts']):.1f}")
# show one sample
import textwrap
s=[c for c in ideas['concepts'] if c['id']=='Anattā (No-Self)'][0]
print("SAMPLE", s['id'], "| thinkers:", s['thinkers'])
for r in s['readings']:
    print("   -", r['kind'], "|", r['author'], "—", r['title'], f"({r['year']})")
