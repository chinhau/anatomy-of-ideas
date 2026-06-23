# Tab Redesign Critique — 8-Agent Panel vs. the Mission

**Date:** 2026-06-23 · **Panel:** data-visualization, data-science, philosophy
professor, shaman/contemplative, visual-design/UI, UX/IA, Steve Jobs, red team.
Each judged all 5 tabs (Questions · Timeline · Paths · Ideas · Thinkers) against
`MISSION.md`. Companion to `MISSION.md`, `PRIOR-ART.md`, `CONCEPT-GAPS.md`.

---

## The four findings every agent (or nearly every agent) reached

### 1. The 5-state epistemic status — the mission's signature claim — IS NOT BUILT.
Flagged independently by data-viz, data-science, professor, UI, UX, and red team.
`ideas.json` has no `status` field; the only state is a binary `contested` (6 of
263) plus `reading` status. **The product claims to show "how far thought has
travelled per question," but ships no travelled-distance variable.** Red team:
"you are claiming a verdict-per-question system you have not built." This is the
single highest-priority gap — everything else in the mission is downstream of it.
- **Fix (data-science + professor):** add `status` at the *question* (or
  sub-question) level first — 11 defensible judgments, not 263 false-precision
  ones — with `statusConfidence` (extend `contested`) + a cited one-line
  rationale. Encode as **color + shape** consistently across every tab; always
  show a text label in the dossier; mark low-confidence calls visibly.

### 2. The north-star feeling "you're not the first to wonder" appears NOWHERE in the UI.
Jobs, UX, and data-viz all hit this. It exists only in the mission doc. Jobs:
"You wrote your soul in the mission doc and forgot to put it in the room."
- **Fix:** put the line on screen — landing hero + a one-time first-run caption on
  Questions. Minimum-effort, maximum-impact.

### 3. The stale `<title>` "Five Maps of Thought" / "167 ideas" contradicts reality.
Every agent that read the source caught it (live title, browser tab, Google
result, shared links all lie; H1/og:title already fixed). **Fix today.**

### 4. A landing page is needed (with one caveat).
Strong consensus YES (data-viz, design, Jobs, shaman, professor). **UX dissents
partially:** prefers a *thin, dismissable one-line first-run layer* over a blocking
splash, to preserve "land in the work." Reconcilable: a fast hero that resolves
*into* the questions, honoring reduced-motion.
- **Hero candidates:** 11 status-colored "pulse-strips" ending at a now-line
  (data-viz); self-drawing question-constellation + "The great questions humans
  keep asking" (design); black screen + "Whatever you're wrestling with tonight,
  someone spent their life on it" + one button (Jobs).
- **Honest anchor number (data-science):** "11 questions · 425 thinkers · 4,399
  years (2375 BCE → 2024)." Avoid leading with "263 ideas" (invites "more ideas =
  more progress" misread).

## The tab-by-tab verdict (where agents converged)

| Tab | Verdict | Rationale |
|---|---|---|
| **Questions** | **KEEP — the soul.** | The only on-mission home; but it currently *displays* labels, should *teach* by showing each question's epistemic state on the home grid. |
| **Timeline** | **KEEP but RE-ENCODE (currently anti-mission).** | Recurrence-ordering + the `now` beam imply *false perennity*: "mind" is 88% post-1800 yet drawn with the same "ancient→now" silhouette as genuinely perennial "peace." Data-science + red team hammered this. Fix: **fixed lane order**, **color = status (not region)**, **per-lane density band**, distinguish *catalogue gaps* from *genuine silence*, honest caption ("lane height = recurrence, not even spread"). |
| **Paths → Arguments** | **KEEP.** | Position→counter is the *only* place that shows a question is unsettled by showing live disagreement. Most on-mission feature after Questions. |
| **Paths → Journeys** | **CUT / demote.** | data-viz + professor: a curated syllabus that smuggles the author's vantage / implies a canon; fails the decision test. Fold best reading lists into the dossier. |
| **Ideas (ego-graph)** | **KEEP but earn it** (Jobs: KILL). | Near-redundant with the dossier's relations + Timeline arcs. Make it answer "did this line go anywhere?" (descendants, last-touched). Jobs calls it the engineer's darling. |
| **Thinkers (constellation)** | **DEMOTE from a peer tab** (consensus). | Name-centric in an explicitly *idea*-centric atlas; positions imply relationships not in the data; the astrological scaffolding is the strongest "alchemy not philosophy" signal. data-viz/UX/Jobs: demote to a mode/filter or re-anchor to era×question *coverage* (not celebrity). |

**The structural read (UX + Jobs):** Timeline, Ideas, and Thinkers are *three
"explore-a-graph" surfaces* — "too many doors to the same room." The soul is
**Questions + Paths/Arguments**; the three graph views compete. Jobs' radical cut:
merge Timeline + Thinkers *into* the idea dossier as attributes of an answer
(when/who), kill the standalone Ideas graph. (A more conservative path: keep
Timeline re-encoded, demote Thinkers, fold Journeys away.)

## The aesthetic problem (design + red team)

The "Renaissance book of secrets" / hermetic-codex art direction (sigils,
ecliptic, zodiac-style region labels, rubrication) is *premium craft* but carries
a **mysticism tax**: rendering Quine and Gettier in the same gold-foil, sigil-
bordered frame as tarot/alchemy visually asserts an equivalence the text denies —
re-litigating the very mysticism drift the canon-audit corrected, at the visual
layer. "Aesthetics are an argument."
- **Fix (design):** *register shift, not redesign* — reframe as a **cartographer's
  / naturalist's / anatomical codex** (the literal "Anatomy"): same gold-on-dark,
  same serifs, but constellation → star-chart/celestial cartography, sigils →
  taxonomic marks, **kill the astrological ecliptic in Thinkers**. Reserve **gold
  exclusively for the "live" status** so the brand color = the mission's heartbeat.

## The philosopher's structural notes

- **mind vs self carve at the wrong joint:** philosophy-of-mind moves
  (Functionalism, Behaviorist Mind, Unconscious) sit under `self`. Cut:
  **mind = the machinery; self = the subject.**
- **No question owns language/meaning** — the deepest *structural* gap (not just
  coverage). `know` must visibly absorb "How does meaning work?" (Frege/Russell/
  Kripke/Austin) or the map reads as pre-1900.
- **`trans` + `peace` as 2 of 11 top questions may encode the detachment lean as
  architecture** — a load-bearing editorial choice wearing the costume of a
  neutral joint. Name it.
- Put **"one map, from one vantage" on the page**, not just in the doc — the single
  most trust-building sentence available.

## The shaman's soul notes (honest, within the bar)

- **"Travelled" is a settler's verb** — smuggles progress/distance. The questions
  aren't a road; consider "kept asking" / "returned to."
- **The honesty bar (named author + dated text) is also a literacy filter** — it
  excludes the oral/shamanic traditions by method, then calls the world's sources
  "thin." Be more honest: name the *bar itself* as the blind spot (a "map's edge"
  marker), without breaking it.
- **Mark practice as a verb** — ideas meant to be *done* (Stoic exercises,
  vipassanā, Examen, dhikr), as you already did for "Literature & Imagination."
- **A threshold gesture** before the doors: one line, one breath — arrival as
  *crossing*, not *loading*.

---

## Prioritized action list (synthesis)

**Tier 0 — do immediately, near-zero risk**
1. Fix the stale `<title>` ("Five Maps of Thought" / "167 ideas") to match reality.
2. Put "you're not the first to wonder" and "one map, from one vantage" *on screen*.

**Tier 1 — deliver the mission's signature (highest leverage)**
3. Add the 5-state `status` field (question-level first) + `statusConfidence` +
   cited rationale; encode as color+shape across Questions/Timeline/Ideas; label
   in dossier.
4. Re-encode the Timeline: fixed lane order, color = status, per-lane density band,
   gap-vs-silence distinction, honest "recurrence ≠ even spread" caption.
5. Build the landing/threshold hero (resolves into Questions; honors reduced-motion).

**Tier 2 — structural & editorial**
6. Cut/demote Journeys; demote Thinkers from a peer tab (mode/filter or
   coverage-anchored); decide Ideas-graph's fate (earn-it vs. Jobs' kill).
7. Re-cut mind/self; give language a visible home in `know`.
8. Register-shift the aesthetic (cartographic/anatomical, not occult); kill the
   astrological ecliptic; gold = "live."

**Tier 3 — soul & honesty depth**
9. Replace "travelled"; mark the bar as a literacy filter ("map's edge");
   badge practice-as-verb.

**Caution flagged by red team:** do NOT ship a landing page advertising the
5-state system *before* it exists — the first click would expose the gap. Build
status (Tier 1.3) before/with the landing page (Tier 1.5).
