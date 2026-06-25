# Docs — the returnable map of *The Anatomy of Ideas*

One place to circle back to: **what we're aiming for**, **the agents we deploy to
keep it honest**, and **every decision we've locked in**. Start here.

> Source of truth for the app is `src/template.html`; `python3 build.py`
> regenerates the deployable `index.html` (never edit the built file). Smoke-test
> with `npm test`.

---

## 1. What we're aiming for (the north stars)

| Doc | What it fixes in place |
|---|---|
| [MISSION.md](MISSION.md) | The product thesis — what the atlas *is* and is *not*. The strategy north star. |
| [DESIGN-TASTE.md](DESIGN-TASTE.md) | The **visual** north star — the "spiritual aesthetic," the 3 anti-kitsch guardrails, the palette/type reference. The taste north star. |
| [LANDING-ART-DIRECTION.md](LANDING-ART-DIRECTION.md) | The resolved look for the **front door** — lapis-and-gold celestial atlas, four principles (awe/truth/honesty/restraint), distilled from the six-register moodboard. Downstream of DESIGN-TASTE; not yet ratified. |

## 2. The agents we deploy (reusable, read-only)

We work by deploying **parallel critique agents** and having the maintainer
synthesize. The reusable briefs and the panels we've already run:

- **The standing design roster** — [DESIGN-TASTE.md §4](DESIGN-TASTE.md): 5
  self-contained briefs to redeploy for any look pass (Typographer · Esoterica &
  symbol scholar · Colour & art director · Steve Jobs/restraint · Storyboard/
  user-journey). Run them before/while you touch the design.
- **Panels already run** (captured as their own docs, so the critique is
  re-readable):
  - [PRIOR-ART.md](PRIOR-ART.md) — 5 research agents (competitive landscape).
  - [CONCEPT-GAPS.md](CONCEPT-GAPS.md) — coverage audit vs. canonical indexes.
  - [TAB-REDESIGN-CRITIQUE.md](TAB-REDESIGN-CRITIQUE.md) — 8-agent panel judging
    all tabs against the mission.
  - MISSION.md itself — convergence of 4 strategy agents.

## 3. The decisions we've locked in (ADRs)

Numbered, append-only. New decisions get the next number; supersede, don't
rewrite. (ADR 0004 collided once across two concurrent sessions — keep numbers
unique.)

| ADR | Decision |
|---|---|
| [0001](decisions/0001-tab-information-architecture.md) | Tab IA: 7 views → 5 |
| [0002](decisions/0002-tab-names.md) | Tab names (Lens→Ideas, Constellation→Thinkers, …) |
| [0003](decisions/0003-hermetic-codex-art-direction.md) | Hermetic-codex art direction (the "book of secrets" north star; numerology dropped) |
| [0004](decisions/0004-lens-board-tarot-fan.md) | Lens board as a tarot fan |
| [0005](decisions/0005-tradition-region-marks.md) | Tradition marks → region marks (Thinkers side only) |

---

## How to use this when circling back

1. Re-read **§1** to reload the aim before any change.
2. Pull the relevant **§2** agent brief(s); run them read-only, in parallel,
   *before* implementing; synthesize yourself.
3. When a change settles a real tradeoff, write the next **§3** ADR.
4. This repo is sometimes edited by two sessions at once — commit
   `src/template.html` + built `index.html` **together**, and verify with
   `git show --stat HEAD`.
