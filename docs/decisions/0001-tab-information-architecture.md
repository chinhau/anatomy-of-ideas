# ADR 0001 — Tab information architecture: 7 views → 5

**Status:** Accepted · **Date:** 2026-06-23

## Context

The atlas shipped with **seven** top-level view tabs, each carrying a Roman
numeral (I–VII) that implied an authored, mandatory reading sequence:

```
I Questions · II Timeline · III Idea Web · IV Threads
· V Constellation · VI Lens · VII Journeys
```

Ahead of launch we ran a four-agent critique (onboarding UX, information
architecture, editorial narrative, and a "Jobs-style" simplicity pass) on the
tab order. Points of convergence across all four:

- **Questions should stay first and default** — it is the thesis statement.
- **Idea Web was in the wrong place.** Three of four flagged it: a dense
  force-directed "hairball" that intimidates newcomers early. The simplicity
  pass argued it should be cut entirely, because **Lens is the better node-link
  graph** (focus+context, and it has the "Eleven Doors In" gateway as an empty
  state).
- **Threads and Journeys are near-twins** — both are "someone authored a path
  for you to walk." They read as two competing tabs for one idea.
- **Constellation is the people layer**, sitting awkwardly mid-way through the
  idea-graph tabs.

The simplicity pass also argued the **Roman numerals should go**: they imply a
fixed sequence, but the views are peers you dip into freely.

## Decision

We took the **reduce** direction (the simplicity pass), not a pure reorder:

1. **Cut the Idea Web** view entirely. Lens is the surviving node-link graph.
   Idea-clicks that used to land in the Web now land in the Lens ego-graph
   (`showIdeaInLens()` in `src/template.html`).
2. **Merge Threads + Journeys into one "Paths" tab** with an Arguments /
   Reading-paths sub-toggle (`setPathsPane()`). The two panes (`#thr-wrap`,
   `#jrn-wrap`) live in one `#m-paths` section; only the active one is shown.
3. **Drop the Roman numerals** from the tabs and from the caption strip
   ("Map I…VII" → the view's name in gold).

Resulting tab bar (peers, no numerals):

```
Questions · Timeline · Paths · Lens · Constellation
```

Ordering rationale: Questions (thesis / default) → Timeline (orientation) →
Paths (curated reading) → Lens (the graph) → Constellation (the people layer,
the "zoom out").

## Deep links / back-compat

- New canonical hashes: `#/paths/threads/<i>.<step>` and `#/paths/journeys/<i>`.
- **Legacy `#/threads/<i>.<step>` and `#/journeys/<i>` still resolve** into the
  merged Paths view (handled in `parseHash`), so old bookmarks keep working.

## What changed (files)

- `src/template.html` — tab bar markup; `#m-paths` section (merged panes +
  sub-toggle); removed `#m-web` section + all Idea Web JS (`buildWeb`,
  `webHighlight`, `fitWeb`, `webRelabel`, the `w*` simulation vars) and CSS;
  `views`/`setMode`/`parseHash` rewired; `setPathsPane()` + `showIdeaInLens()`
  added; captions de-numbered.
- `src/i18n.json` — new `Paths` / `Arguments` / `Reading paths` UI labels;
  captions de-numbered, `paths` + `journeys` captions added (zh/ru), `web`
  caption removed.
- `tests/smoke.mjs` — mode list 7→5; Paths sub-toggle assertions; deep-link test
  covers new + legacy hashes; the cold-boot localization regression now exercises
  Lens instead of the removed Web. **108 assertions pass** (was 94).
- `README.md` — "five views" section rewritten.

## Alternatives considered

- **A — pure reorder, keep all 7 tabs.** Lower risk, satisfied 3 of 4 agents,
  but kept two pairs of near-twins and the misleading numerals. Rejected as a
  half-measure.
- **Keep Idea Web, move it later.** The editorial agent liked the Web as a
  thesis-image ("look how connected everything is"). Rejected: Lens delivers the
  same "everything connects" feeling with less intimidation, and two node-link
  graphs is one too many.

## How to come back to the 7-tab version

The full seven-tab version is preserved at commit **`f0c0754`**, tagged
**`v-seven-tabs`**. To inspect or restore:

```bash
git show v-seven-tabs:src/template.html      # peek without checking out
git checkout v-seven-tabs -- src/template.html src/i18n.json tests/smoke.mjs
python3 build.py                             # regenerate index.html
```
