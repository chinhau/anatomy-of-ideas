# ADR 0002 — Tab names: Lens → Ideas, Constellation → Thinkers, Reading paths → Journeys

**Status:** Accepted · **Date:** 2026-06-23 · **Builds on:** ADR 0001

## Context

ADR 0001 reduced the tab bar from seven views to five
(`Questions · Timeline · Paths · Lens · Constellation`) and merged Threads +
Journeys into a Paths sub-toggle (`Arguments` / `Reading paths`). Immediately
after, the question was whether those *labels* were the most suitable — several
were insider/metaphor names ("Lens", "Constellation") rather than plain nouns
describing what the view contains.

We ran a three-agent naming critique. Points of convergence:

- **Constellation → Thinkers** (unanimous). "Constellation" is a metaphor for
  the contents (people); "Thinkers" says what you'll actually find. It also
  pairs cleanly with "Ideas" as the two halves of the atlas (ideas vs. people).
- **Lens → Ideas** (majority). "Lens" describes the *technique* (focus+context),
  not the *subject*. Renaming to "Ideas" makes the idea-graph self-describing and
  sets up the Ideas/Thinkers pairing.
- **Reading paths → Journeys** (sub-toggle). Inside the Paths tab, "Arguments"
  and "Reading paths" both contain the word "paths/path-like" and read as
  redundant with the parent tab name. "Journeys" is distinct and evocative.

Questions, Timeline, Paths, and the "Arguments" sub-pane were kept — already
plain nouns that say what they hold.

## Decision

Final tab bar (peers, no numerals):

```
Questions · Timeline · Paths · Ideas · Thinkers
```

Paths sub-toggle: `Arguments · Journeys`.

**Only the visible labels / captions / i18n strings changed.** Internal mode ids
(`lens`, `constellation`), function names (`buildLens`, `showIdeaInLens`,
`buildConstellation`), section ids (`#m-lens`, `#m-constellation`), and all
deep-link hashes (`#/lens/…`, `#/constellation/…`, `#/paths/journeys/…`) stay as
they were. This keeps the rename low-risk and back-compatible — no URL or code
churn, purely a presentation change.

## What changed (files)

- `src/template.html` — tab button `data-i18n` labels (`Ideas`, `Thinkers`),
  the `#paths-journeys` sub-toggle label (`Journeys`), and the CAPTIONS bold
  labels (`<b>Ideas</b>`, `<b>Thinkers</b>`, `<b>Journeys</b>`).
- `src/i18n.json` — ui label keys renamed (`Lens`→`Ideas`, `Constellation`→
  `Thinkers`, `Reading paths`→`Journeys`) with zh/ru translations
  (觀念/Идеи, 思想家/Мыслители, 旅程/Путешествия); caption bold labels updated.
- `tests/smoke.mjs` — comment/message strings only ("Reading paths"→"Journeys");
  test logic unchanged (it targets stable ids). **108 assertions still pass.**
- `README.md` — "five views" section relabelled.

## Alternatives considered

- **Keep "Lens" / "Constellation".** They are evocative and on-brand, but they
  describe the lens/metaphor rather than the contents; newcomers can't predict
  what's behind them. Rejected in favour of self-describing nouns.
- **Rename internal ids too** (full consistency). Rejected: high churn, breaks
  existing deep links, no user-visible benefit — labels are what users see.

## Revert

Names are a thin layer on top of ADR 0001. The full seven-tab version remains at
tag **`v-seven-tabs`** (commit `f0c0754`). To revert *just* the names, restore
the label strings in the four files above from the 7→5 commit.
