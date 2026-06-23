# Prior Art & Competitive Landscape — The Anatomy of Ideas

**Date:** 2026-06-23 · **Method:** five parallel research agents (academic/DH network
maps, popular philosophy maps, the great-ideas/Syntopicon lineage, knowledge-atlas
UX exemplars, and a dedicated YouTube/Reddit/X sweep). Companion to `MISSION.md`.

**Bottom line:** No existing public project does all four of *idea-centric +
honest + interactive + globally comprehensive across enduring questions*. The
closest living peer (Önduygu) is Western-only and desktop-bound; the deepest
ancestor (Adler's Syntopicon) is a closed 1952 Western print canon. That
combination is our unoccupied niche.

---

## 1. The landscape, by family

### A. The idea-indexed ancestors (closest in *spirit*)
- **Mortimer Adler's *Syntopicon*** (1952) — [Wikipedia](https://en.wikipedia.org/wiki/A_Syntopicon).
  THE central ancestor: indexed the Great Books by **102 Great Ideas** (Angel→World),
  each with intro essay → outline of sub-topics → references → cross-references →
  further reading. Proved thought *can* be mapped by idea. **Died of three
  diseases we can cure:** closed Western/male canon, frozen-at-1952 print, and
  implicit (non-navigable) cross-links. Its 5-part node schema is worth echoing.
- **The Great Conversation** (Hutchins/Adler) — the "thought as a millennia-long
  dialogue" framing behind the Syntopicon. We adopt the metaphor, make it literal
  and cross-cultural.
- **Perennial-questions textbooks** (*Philosophy's Big Questions*, Columbia UP, etc.)
  — organize by question, present positions even-handedly, sometimes cross-cultural.
  Linear print, ~8 questions, no graph. Validates question-first over noun-first.

### B. The living idea-centric peers (closest in *form*)
- **Deniz Cem Önduygu — "History of Philosophy: Summarized & Visualized"** —
  [denizcemonduygu.com/philo](https://www.denizcemonduygu.com/philo/). **Our one true
  peer.** Nodes are *statements/ideas*; edges are **signed agree/disagree**;
  per-claim references; hand-curated 10+ yrs; endorsed by Dennett & Carroll. 2025
  Kumu philosopher-node offshoot ([Daily Nous](https://dailynous.com/2025/01/31/new-interactive-visualization-of-philosophy/)).
  **Gaps = our differentiators:** Western-only, desktop/Chrome-only, no
  great-questions scaffold, sentence-soup density.
- **Visualizing SEP** — [visualizingsep.com](https://www.visualizingsep.com/) —
  idea/article focus+context graph of the SEP (domains via InPhO). Auto-derived; no
  curation/honesty layer; desktop-only.
- **InPhO** — [inphoproject.org](https://www.inphoproject.org/) — machine-built,
  expert-verified philosophy ontology; idea-relatedness as a first-class object;
  open API. Dry UI; relatedness is statistical co-occurrence, not curated argument.
- **philosophytree.org** — interactive, free, strong **non-Western coverage**
  (Greece/Rome, Middle East, S.Asia, E.Asia, Africa, Americas), Explorer +
  Random Idea. **But** ~80 concepts only, school/thinker-organized (not by
  question), **no visible author or sourcing** (fails our honesty bar). *Newest
  near-peer found; worth a hands-on look.*

### C. Name- / citation- / influence-centric (adjacent, not idea-centric)
- **Six Degrees of Francis Bacon** ([site](http://sixdegreesoffrancisbacon.com)) —
  inferred-then-crowd-corrected social graph of early-modern Britain; per-edge
  source citations + crowd correction worth stealing for provenance.
- **Mapping the Republic of Letters** (Stanford) — correspondence/geography flows;
  explicit about archival gaps (a model for honesty); spawned Palladio.
- **Pantheon** ([pantheon.world](https://pantheon.world/)) — 85k famous people by
  time/place/occupation; transparent fame index; coordinated multi-view UX;
  "born on this day" hook. Fame ≠ significance; no ideas/edges.
- **Kieran Healy co-citation graph**, **Simon Raper / Drunks & Lampposts**,
  **The Philosopher's Web** (Kumu), **arXiv reference networks**,
  **academictree.org/philosophy** (advisor genealogy) — all
  name/citation/genealogy-centric. The Wikipedia "problem with Hegel" (sparse
  infobox metadata distorts centrality) is a cautionary argument *for* curation.

### D. References & video canons (deliberately non-visual)
- **SEP / IEP** — dominant authorities; deep prose, no visualization → the vacuum
  we fill; cite as depth-sources for credibility.
- **HoPWAG** (Peter Adamson) — "without any gaps," genuinely global, but linear
  audio, no glanceable structure.
- **Crash Course / Wi-Phi / School of Life / Information Is Beautiful / Superscholar
  poster / Histography** — accessible, popular, but static/linear, no idea-level
  cross-linking. The viral Superscholar poster proves public appetite for "a map
  of philosophy."

### E. Atlas-of-knowledge UX exemplars (learn structure/feeling, any domain)
- **A History of the World in 100 Objects** — bounded curation (a finite "N
  landmark ideas" set builds trust + completability).
- **WikiGalaxy/Wikiverse** — *cautionary*: beautiful 3D, but "you can't get to the
  page you want." Spatial metaphor as ambient framing, never as navigation.
- **Murray's *Human Accomplishment*** — *cautionary*: "neutral counting" launders
  source bias into apparent objectivity (80%+ Western men). If we ever rank/size,
  surface the bias in the UI.
- **Our World in Data** — honesty/visible-sourcing *as the product* → trust moat.
- **The Pudding / Nicky Case** — authored scrollytelling + cognitive gating
  ("withhold, let them predict, then reveal") manufactures the "you're not the
  first to wonder" beat.
- **Cyc / Freebase** — *cautionary*: chasing completeness is infeasible and cold;
  curated opinionated slices win.

---

## 2. SWOT — where our value lies

### Strengths (what we have that peers don't)
- **Idea-centric + question-structured.** Organized around 11 enduring questions,
  not people, books, or alphabetized nouns. Almost everyone else is
  name/citation/event-centric.
- **Genuinely global + even-handed.** 425 thinkers across traditions, on a strict
  inclusion bar (named modern author + dated text) — directly answering the canon
  critique that sank the Syntopicon, Murray, and most influence graphs.
- **Honesty bar as a feature.** Discrete dots not interpolated lines; narrow
  `contested` tag; "one map from one vantage." Önduygu/Our World in Data show
  honesty earns trust; the scraped graphs lack it.
- **Curated, not scraped.** Avoids the Wikipedia "problem with Hegel" popularity
  bias baked into Pantheon, Philosopher's Web, Histography.
- **Self-contained, free, mobile-considerate single HTML.** Peers are desktop/
  Chrome-only; un-maintained interactive sites rot — our one-file form is durable.
- **Multiple coordinated views** (Questions/Timeline/Paths/Ideas/Thinkers) vs. a
  single hairball.

### Weaknesses (honest internal gaps)
- **Solo-maintained, hand-curated** → slower to scale, coverage uneven (women
  under-represented; oral/shamanic cosmologies thin; Western/S.Asian weighting).
- **Curation = subjectivity**; the interpretive edges ("builds on/rejects") are
  one author's readings (we disclose this, but it's a limit).
- **No social/contribution layer** (Six Degrees' crowd-correction; OSP's scale).
- **Discoverability ≈ zero** — no audience yet; peers have Daily Nous/Open Culture
  amplification.
- **Edges are not yet stance-typed** (Önduygu's signed agree/disagree is richer
  than our current relations).

### Opportunities
- **An unoccupied niche** confirmed across 5 research families + YouTube/Reddit/X:
  no one is idea-centric AND honest AND interactive AND global.
- **Position as "the interactive, even-handed, globally-sourced successor to
  Adler's Syntopicon."** Strong, citable lineage hook.
- **Demand is real and recurring** — every time such a tool surfaces it's
  amplified enthusiastically; the consistent community complaint (Western-only,
  influence-not-argument, desktop-only) is *exactly our differentiator set*.
- **Concrete features to steal:** signed agree/disagree edges (Önduygu); per-edge
  source citations + crowd correction (Six Degrees); "on this day in ideas" hook
  (Pantheon); a bounded "N landmark ideas" tour (100 Objects); surprising-kinship
  feature (Art Palette); cognitive gating (Nicky Case).
- **The authorities don't visualize** (SEP/IEP/HoPWAG) — cite them, fill the gap.

### Threats
- **"Influence-graph fatigue"** — community finds Wikipedia-derived node-link
  spaghetti pretty-but-shallow; we must lead with *argument/structure*, not just
  connection, to avoid being lumped in.
- **A funded/known peer adds our differentiators** — Önduygu could go global or
  add questions; a well-resourced team could out-execute a solo project.
- **Beauty-over-wayfinding trap** (WikiGalaxy) — our visual ambition must never
  outrun navigability.
- **Bias-laundering perception** — any ranking/sizing risks the Murray critique
  unless caveats are visible.
- **Maintenance/abandonment risk** of a solo project (mitigated by the durable
  single-file form).

---

## 3. The value, in one line

> The first **honest, interactive, globally-sourced map of the questions humanity
> keeps asking** — Adler's Great-Conversation ambition, freed from its 1952
> limits (closed Western canon, frozen print, implicit links) and organized so a
> newcomer can *feel* "I'm not the first to wonder this."

## 4. Coverage note (platforms swept)
Web (academic + popular), GitHub/Reddit/X (prior viz research), and a dedicated
**YouTube + Reddit + X sweep** were all run. The only new artifact the social
sweep added was **philosophytree.org**; the rest amplified the projects above.
Adjacent media (narrated history-of-ideas YouTube channels) confirm audience
appetite but are not interactive prior art.
