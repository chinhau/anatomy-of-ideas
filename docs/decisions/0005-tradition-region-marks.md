# ADR 0005 — Tradition marks become region marks

**Status:** Accepted · **Date:** 2026-06-23
· Downstream of [ADR 0003](0003-hermetic-codex-art-direction.md) and `docs/DESIGN-TASTE.md`.

## Context

The maintainer wanted to draw the philosophical/spiritual traditions the atlas
covers (Yin-Yang, Christian, Jungian, …) into the **visual** aesthetic — symbols
"grounded in real data" but applied "more as ambient texture." The original
sketch ("Set A") was ~6 bespoke inline-SVG tradition marks (ensō, bagua,
armillary, ouroboros, …) with a swatch fallback, placed in the constellation
legend and the person dossier.

Two independent critiques (a storyboard/user-journey agent, then a data check)
killed Set A *as conceived*:

1. **The taxonomy doesn't fit.** Concepts carry one of **38 `trad` codes**
   (`src/ideas.json`; largest is "Literature & Imagination" = 44, with many
   singletons: Norse, Nahua, Egyptian…). "~6 marks + swatch fallback" makes the
   fallback the *rule*, turning the bespoke six into a cherry-picked, faintly
   orientalist minority — exactly the "ornament must ENCODE a real datum, never
   garnish" line (guardrail 1) and the kitsch line of ADR 0003 / DESIGN-TASTE §1.
2. **Wrong placement.** In the constellation, node colour **already equals the
   group/tradition** (`aGroup[n.group].color`), so legend marks would *duplicate*
   an existing channel; and a mark beside the canonical wax seal in the dossier
   stacks two engraved devices (the seal is the dossier's strongest single
   signal). The view where colour means *question* (concept maps) is where a
   tradition mark would be additive — but that view wasn't in scope.
3. **No clean region partition for concepts.** Region (West / Psyche / East) is a
   **gap-free, pre-defined** datum only for the **17 person-groups** in
   `src/atlas_graph.json`. Concept `trad` codes (disciplines like "Psychology,"
   "Cognitive Science," cross-cultural "Literature & Imagination") resist any
   region partition; forcing one would be invented garnish.

## Decision

Ship **three region marks — West / Psyche / East — on the Thinkers side only**,
where region is real, pre-defined, and gap-free. No invented taxonomy; no
concept-level marks.

**Reuse, don't invent.** The codebase already speaks an engraved region
vocabulary: `REGION_SIGIL` (`src/template.html`) — West = astrolabe arc, Psyche =
crescent, East = ensō circle — used as the portrait-niche fallback for schools
and faceless thinkers. The new `regionMark(reg,name)` helper renders the **same
shapes** small and inline, so the dossier line and legend headings carry the
shorthand the portrait niche already uses.

Placement:
- **Person dossier** `#dr-q` line — region mark prepended before the existing
  colour-dot + school label; hover/SR label is the romantic region name
  (Occident / Psyche / Orient).
- **Thinkers legend** region headings (Occident / Psyche / Orient) — mark
  prepended to each of the three headings.

Honesty rules honored:
- **Region is read off the shape**, so the mark is stroked in quiet `--ink`
  (`#7a6038`, the demoted-label brown), never gold — keeps gold rare (guardrail 3)
  and puts the under-used `--ink` token to work (DESIGN-TASTE §5).
- **Engraving logic, not glow** (guardrail 2): single-stroke, round caps, no
  blur/drop-shadow on the small mark.
- **Encodes a real, coarse datum** the colour system doesn't surface obviously:
  which of the three worlds a thinker belongs to (guardrail 1). Three marks,
  three regions — gap-free, so no row is left looking unfinished.

## Rejected alternatives

- **6-way "schools" partition over all 269 concepts.** Richest ("all ideas"), but
  the partition would be authored by us with several forced assignments — the
  garnish risk ADR 0003 exists to prevent.
- **Marks in the constellation legend rows / beside the wax seal.** Duplicates the
  node colour and stacks devices on the dossier's strongest signal.
- **Pause Set A entirely.** Considered; the region-mark scope is unimpeachable
  enough to ship now.

## Shipped alongside (copy/type fixes, same session)

- Lens-board title **"Eleven doors in" → "Eleven doors"** (the dangling "in" the
  maintainer disliked; the subtitle already says "one way into each").
- Landing headline **"You're not the first to wonder"** no longer wraps awkwardly:
  `text-wrap:balance` on `.gate-line`; the masthead **eyebrow** is differentiated
  to "An atlas of the great questions" (promoting the gate's own eyebrow to the
  persistent header) so the motto isn't duplicated, with `white-space:nowrap` to
  keep it one row.

## Consequences

- The tradition/region visual language is now consistent end-to-end (niche
  fallback, dossier line, legend heading all share `REGION_SIGIL`).
- Concepts gain no tradition mark; if concept-level traditional texture is wanted
  later, it needs a defensible coarse taxonomy decided first (see Rejected).
- `--ink` gets its first real use; a future pass may demote the still-gold legend
  region headings to `--ink` too (DESIGN-TASTE §5 punch-list).
