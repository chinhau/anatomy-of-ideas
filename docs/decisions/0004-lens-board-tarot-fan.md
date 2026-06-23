# ADR 0004 — Lens board as a tarot fan

**Status:** Accepted · **Date:** 2026-06-23

## Context

The Ideas tab (internal mode `lens`) opens on an empty-state **board** of eleven
"doors" — one curated gateway concept per question — before you drop into the
ego-graph. The board has been through three forms:

1. **Static grid** of 11 cells (ADR-era "Eleven Doors In"; "settle, then breathe"
   motion, see memory `project_lens-feature.md`).
2. **Deck of Doors** (commit `5abe8ff`): one front emblem-plate card plus three
   peeking back cards, riffled **one at a time** via chevrons / hue pips / arrow
   keys / swipe.

Form 2 read as a deck but behaved like a linear pager — you stepped ±1 through
doors with left/right chevrons. The maintainer disliked the paging: it hides ten
of eleven choices behind a "next" button and doesn't match the deck metaphor it
wears. The brief: make it **feel like reshuffling a tarot deck**, with all eleven
doors choosable at once.

Note: neither form 1's grid nor form 2's deck riffle was ever captured in an ADR —
only in commit messages and inline comments. This ADR closes that gap.

## Decision

**The board is a fanned hand of eleven cards.** (Form 3.)

- **Fan layout** (`fanGeo` / `layoutFan` in `src/template.html`): all 11 doors
  spread in a shallow smile arc. The per-card tilt is fixed (`FAN_STEP`); the
  horizontal gap and arc dip are derived from the **live container width** so the
  spread always fits edge to edge (11 cards, responsive down to mobile).
- **Pick any card directly.** Every card is a real button; clicking it enters that
  door (`enterDoor`). No chevrons, no pips, no "next" — paging is gone.
- **Lift to read.** Hover or keyboard focus lifts a card clear of the fan,
  straightens it, gilds the cartouche gold, and unfurls its gloss. The gloss stays
  **furled at rest** (`max-height:0`) so the resting fan reads as faces, not walls
  of text — you draw a card to read it.
- **Riffle to re-deal** (`riffleDeck`): a single hairline button gathers the fan
  into a squared stack, gives it two quick interleaving cuts, then deals it back
  out into a **freshly shuffled order** (Fisher–Yates on slot positions). Door
  *identity* is by content, not position, so shuffling positions is harmless and
  makes the gesture meaningful — this is the "reshuffling tarot deck" feel.
- **Deal-in on arrival** (`dealFan`): the fan deals out staggered, slot by slot,
  each time the board appears (`showLensBoard`).
- **Keyboard reach:** arrow keys walk the fan by visual position; every card is
  natively tabbable.

## Consequences

- **Motion vs. "stillness is the feature."** ADR-era guidance (the 2-agent panel in
  `project_lens-feature.md`) rejected *perpetual* board motion in favour of
  "aliveness in the *arrival*, not perpetual chaos." The fan honours that: motion is
  **on-demand** (deal on entry, riffle on click) and the deck comes fully to rest.
  The maintainer explicitly chose a **"richer, more physical"** riffle here,
  knowingly spending more motion than the old rule's default — scoped to this one
  triggered gesture, not ambient.
- **Reduced motion / no `requestAnimationFrame`** (e.g. jsdom): `dealFan` and
  `riffleDeck` fall back to an instant flat layout — the fan still lays out and
  re-orders, just without the deal/cut animation. Mandatory static fallback kept.
- **A11y:** all eleven doors are reachable and labelled; the lifted card is the
  focus affordance. Removing the pager removes the "9 hidden behind next" problem.
- **Tests:** `tests/smoke.mjs` still asserts 11 `.lb-cell` doors and that clicking a
  door dismisses the board; 125 assertions pass.

## How to revert / find

The per-door astrolabe device (petal + rim-tick count = concepts behind that
question) and the fixed correspondence glyph are unchanged from the Deck of Doors
(`doorDevice`, `DOOR_SIGN`). To restore the one-at-a-time riffle deck, the
chevron/pip version is at commit `5abe8ff` (`paintDeck`/`setDeck`/`DECK_FALL`,
`.lb-chev`/`.lb-pip`). Build via `python3 build.py`, test via `npm test`.
