# ADR 0003 — Hermetic-codex art direction

**Status:** Accepted · **Date:** 2026-06-23

## Context

The atlas had a coherent dark-scholarly look, but its visual language was
generic. We wanted the design **heavily influenced by astrology, numerology,
the occult, and tarot** — while keeping the **scholarship rigorous and the
content untouched**. This is a hard constraint: a prior four-agent canon audit
had already flagged "drift toward mysticism" as a *content* risk, so the line
between occult *visuals* and rigorous *content* must stay crisp. The brief was
explicitly "just the design aspect."

Four parallel design-research agents (one per influence) were launched to
redesign the visual layer. They converged **independently** on a single north
star rather than four competing themes.

## Decision

**One art direction, not four themes:** the site is

> a Renaissance *book of secrets* rendered as a dark sky-atlas.

The warrant is the Warburg/Yates lineage — magic-as-rigorous-cosmology, the
memory-theatre as a data structure — which is what the atlas already *is*. The
four influences **nest** under this one direction:

- **Astrology** = cosmographic substrate (astrolabe graticule behind the
  constellation, planetary-metal ink tints).
- **Tarot** = compositional grammar only (bordered emblem-plate cards, Roman
  numerals). **No suit icons, no fortune framing.**
- **Numerology** = invisible structure (real counts → layout; manuscript
  foliation; φ scale). **Never "lucky numbers."**
- **Occult / alchemy** = binding texture (engraved hairlines, copperplate
  hatching, vermilion rubrication, seal roundels, alchemical Unicode glyphs).

### Three governing guardrails (anti-kitsch)

1. **Ornament must ENCODE meaning, never garnish.** Every numeral, seal, or
   tint stands for a real datum (a count, a rank, a canonical flag, a region).
2. **Engraving logic** (line / hatch / hairline), **NOT** glow / gradient /
   sparkle / emoji.
3. **Restraint as luxury** — gold is reserved for masthead, active tab,
   selection, and seals only.

### Build approach

A **phased build** (option A): roughly one phase per work session, each
committed and pushed to `main` (GitHub Pages serves the repo-root
`index.html`). All UI edits live in `src/template.html`; `python3 build.py`
regenerates `index.html`; `npm test` smoke-tests it.

## What shipped (phases)

- **Phase 1 — "Signature moves"** (commit **`74fd22d`**, deployed): astrolabe
  graticule behind the constellation; vermilion drop-cap versals on the
  Questions framing; guilloché seal roundel (`sealMarkup()`) marking the 34
  `big` canonical thinkers; region-grouped metal-ink school palette in
  `atlas_graph.json` (West = indigo-steel, Psyche = plum-rose, East =
  clay-amber); relationship glyphs (＋/↯/≈) split out from gold on cards;
  contrast fixes (`--muted` → `#9aa3bd`, gold-twin question hue → `#C99A33`).

- **Phase 2 — "Engraved chrome + texture"** (commit **`ae41ed4`**, deployed):
  the shared layer — copperplate hatching (`--hatch` token) behind the stage +
  drawer; masthead engraved title-plate (brand seal mark + double hairline
  rule); concept cards as emblem-plates (inset double-rule); drawer colophon
  (⁂ asterism via `.dr-body::after`).

- **Phase 3 — "Number & frame"** (commit **`2e6890c`**, deployed): manuscript
  foliation. Roman-numeral folios (`toRoman()` helper, `.c-folio`) index each
  concept by era *within its question*, and each question by its place in the
  eleven (`.q-folio`). The 6 `contested` concepts now surface a vermilion
  dagger † (`.c-contested`), closing a long-open canon-audit item ("contested
  ideas were invisible"). The drawer portrait/sigil niche (`.dr-fig-wrap`)
  became a double-rule engraved cameo over a hatched ground. Both
  language-relabel paths in `applyLang` were updated so folios and the dagger
  survive a language switch.

## Deferred (not started)

These are higher-blast-radius or per-view internals, held until phases 1–3 can
be judged live as a whole:

- **φ type/spacing scale** — a global change to every measurement; risky.
- **Ogdoad octagon layout** for the eleven questions — the boldest numerology
  move.
- **Timeline** centuries as ruled ledger staves; **Lens "Doors"** board as
  framed emblem-plates; **node-link edges** as engraved hairline curves.

## Alternatives considered

- **Four separate themes** (one per influence). Rejected: the agents converged
  away from it; four competing visual systems would read as kitsch and would
  fight the guardrails.
- **One-pass full redesign** instead of phases. Rejected in favour of phased
  delivery so each move can be deployed and judged before the next.
- **Single-view prototype** before committing site-wide. Rejected: the
  signature moves (graticule, seals, palette) are cross-cutting and only read
  as a system when shared.

## Why content stays out of scope

The redesign touches **design language only**. Concept text, the canon, the
honesty bar, and the scholarship are untouched. The canon-audit "drift toward
mysticism" finding is a content concern; this ADR governs visuals, and the
three guardrails exist precisely to keep occult *style* from leaking into
scholarly *substance*. The one place the two meet — surfacing the `contested`
flag (Phase 3) — moves in the rigorous direction: it makes scholarly
contestation *more* visible, not less.
