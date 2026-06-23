# -*- coding: utf-8 -*-
import json
from readings import DATA as _RD
from readings_extra import EXTRA as _EX
from readings_extra2 import EXTRA2 as _EX2
from readings_extra3 import EXTRA3 as _EX3
from readings_extra4 import EXTRA4 as _EX4
from readings_extra5 import EXTRA5 as _EX5
from readings_extra6 import EXTRA6 as _EX6
from readings_extra7 import EXTRA7 as _EX7
from readings_extra8 import EXTRA8 as _EX8
from readings_extra9 import EXTRA9 as _EX9
from readings_extra10 import EXTRA10 as _EX10
from readings_extra11 import EXTRA11 as _EX11
from readings_extra12 import EXTRA12 as _EX12
from readings_extra13 import EXTRA13 as _EX13
from readings_extra14 import EXTRA14 as _EX14
from readings_extra15 import EXTRA15 as _EX15
RD = {**_RD, **_EX, **_EX2, **_EX3, **_EX4, **_EX5, **_EX6, **_EX7, **_EX8, **_EX9, **_EX10, **_EX11, **_EX12, **_EX13, **_EX14, **_EX15}

ideas = json.load(open('ideas.json', encoding='utf-8'))
ids = {c['id'] for c in ideas['concepts']}

# coverage checks
missing = sorted(ids - set(RD.keys()))
extra   = sorted(set(RD.keys()) - ids)
if missing:
    raise SystemExit("NO READINGS for: " + ", ".join(missing))
if extra:
    raise SystemExit("READINGS reference unknown concept: " + ", ".join(extra))

# Honest reading order: lead with the primary text (Adler — read the source
# before commentary), then the inspectional/secondary apparatus. Stable, so the
# editor's authored sequence within each band is preserved. NOT an "influence
# rank" — a 1–3 item list can't carry one; influence lives at the atlas level.
KIND_ORDER = {"Primary": 0, "Translation": 1, "Intro": 2, "Study": 3, "Commentary": 4}

for c in ideas['concepts']:
    thinkers, readings = RD[c['id']]
    c['thinkers'] = thinkers
    ordered = sorted(readings, key=lambda r: KIND_ORDER.get(r[3], 9))
    c['readings'] = [
        {"author": a, "title": t, "year": y, "kind": k, "note": n}
        for (a, t, y, k, n) in ordered
    ]

# Derived "works the atlas keeps returning to": readings that land on two or more
# concepts. Pure aggregation — no editorial weighting, it just surfaces the texts
# the map leans on. Sorted by reach, then author, so the order is stable.
from collections import defaultdict
_occ = defaultdict(list)
for c in ideas['concepts']:
    for r in c['readings']:
        _occ[(r['author'], r['title'], r['year'])].append(c['id'])
ideas['recurring'] = sorted(
    ({"author": a, "title": t, "year": y, "count": len(cs), "concepts": sorted(cs)}
     for (a, t, y), cs in _occ.items() if len(cs) >= 2),
    key=lambda r: (-r['count'], r['author']),
)

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
