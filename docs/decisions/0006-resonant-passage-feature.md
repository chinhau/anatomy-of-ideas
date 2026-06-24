# ADR 0006 — The resonant-passage feature (governed by an adversarial reversal)

**Status:** Accepted (scope + guardrails) · **Date:** 2026-06-23
· **Option A (note upgrades) shipped 2026-06-23 as `12234f7`** — see the Update
section at the foot of this file. The PD passage pilot itself is **not built**;
the ache wall and Option B remain deferred.
· Downstream of `docs/MISSION.md` (the honesty bar + 5-state epistemic spine) and
`docs/DESIGN-TASTE.md` (engraving-not-glow, restraint-as-luxury, guardrail 1:
*ornament must encode a real datum*).

## Context

The atlas was reframed around an emotional north star: the jolt of reading
Frankl (*Man's Search for Meaning*) or Fromm (*The Art of Loving*) and thinking
*"why am I only reading this NOW? — the question I carry was already answered, I
just never picked up the book, and I want to read THAT paragraph."* The proposed
feature: hand each reader a **resonant passage** per concept, then send them to
the book. The map is the backbone; the passage is the payload.

Two analysis rounds shaped the design:

1. **Research round (R1).** Five agents swept Goodreads/Kindle/Readwise,
   Reddit, Threads/BookTok, passage-products (The Marginalian, Poetry Foundation,
   Wikiquote, Blinkist) and bibliotherapy. They converged on: curate (never
   crowdsource); ~40–120-word paragraph; bind passage to an "ache"; an "ache
   wall" front door with a 15–25-item emotional taxonomy; heavy provenance +
   verification badges; passage embedded in faint context with an engraved
   underline; a "Barnum audit" to keep resonance honest; two doors.

2. **Adversarial round (R2).** Five agents were briefed to *break* that
   consensus. They largely succeeded, and this ADR follows R2, not R1.

## The R2 critiques that govern this decision

1. **"Encapsulate *the* answer" breaches our own honesty bar.** `MISSION.md`
   classifies *Is the will free?* and *What makes life worth living?* as
   **perennially open**, and self/anattā as **dissolved/reframed**. A single
   "encapsulating" passage hands the reader a *verdict dressed as a feeling* —
   "proven true" in a nicer outfit, the exact framing the mission already
   rejected. A passage optimised for *the jolt* also selects the rhetorically
   seductive over the argumentatively central (factor against representativeness).

2. **The copyright "well within norms" verdict was unsafe.** The feature *by
   design* selects "the single most resonant paragraph" — i.e. the **heart of the
   work**, the worst case under fair-use factor 3 (cf. *Harper & Row*). "Ancient =
   free" is false: the recognisable English of Aurelius/Plato/Tao Te Ching is
   usually an **in-copyright translation** with its own fresh term — the
   translation/edition date governs, not the author's. The "1931" cutoff is wrong
   for 2026 (US public domain = **published 1930 or earlier**, rolling +1/yr). A
   curated collection of "the best passage from each book" also leans toward the
   *licensed* anthology market (factor 4).

3. **293 passages will not complete.** The readings list — a *cheaper* artifact
   (no byte-match, no translator/edition, no copyright tier) — took 20 files and
   19 rounds and still needs ~10 commits every six months. Passages are several×
   the per-item cost. Realistic ceiling ≈ 25%; a drawer that is 80% empty slots
   reads as **abandonment**, the opposite of an atlas that is honest about gaps.

4. **The spec buries and over-designs the payload.** Mid-drawer (after gloss,
   contested, practice, foil) is below the fold — the graveyard slot for the thing
   we call the payload. "Faint context lines" are deliberately low-contrast body
   text (a WCAG failure our design bar rejects elsewhere), encode no
   user-actionable datum (guardrail 1), and optimise for a *screenshot*, not
   *reading*. The "ache wall" as a front door is a mood-intake gate that quiet-site
   readers skip.

## Decision

**Test before you clear, and clear before you build.** A 3-agent debate
(2026-06-23, logged below) reframed the whole question: now that Option A has
shipped, the passage feature's core premise — that an author's *verbatim* words
out-pull the atlas's own one-line gloss — is **untested**, and its control shipped
this morning. So do **not** build the gated pilot or spend any effort on copyright
clearance until a passage has actually beaten its note. Sequence the work:

### Phase 0 — the zero-code gate (do this first)
- Pick **3 concepts where the prose plausibly *is* the datum** and a clean
  **pre-1930 public-domain** source exists: **Bashō / Yūgen, Tolstoy / Ivan
  Ilyich's Mirror, Homer / The Heroic Code**.
- For each, author the candidate passage as **plain text beside the already-shipped
  note** — **no `ideas.json` change, no schema, no render, no CSS, no smoke test.**
- **Strip attribution** and run a single forced choice — on the maintainer after a
  cooling-off week, or on 5–8 readers — *"which one makes you want to open the
  book?"*
- **Decision rule, fixed now:** the passage must win **≥2 of 3, decisively**, or
  this ADR flips to **superseded-by-Option-A** and the drawer stays note-only. The
  qualitative verdict is the *primary* instrument, not a fallback — the site has no
  A/B infra and book-pointer clicks may be near-zero, so do not pretend to measure
  them.

**Why the maintainer verdict, not clicks:** Option A already delivers ~80% of the
jolt at ~2% of the cost (the 12 notes, `12234f7`). The note is the control; the
passage must out-pull it to earn its much larger per-item cost. With no analytics,
a blind forced-choice is the only honest decider.

### Phase 1 — the gated PD pilot (ONLY if Phase 0 passes)
Build a **small, gated, public-domain pilot** — passage-first, honesty-first.
**Scope it to literary/aesthetic concepts**, the segment where verbatim provably
beats a gloss and where the source is almost always PD anyway (so the in-copyright
fight is sidestepped, not fought):
- **~10–11 public-domain `mean` (meaning-of-life) concepts** whose resonant text
  exists in a **verified pre-1930 edition/translation**: e.g. Socrates / The
  Examined Life, Aristotle / Telos, Homer / The Heroic Code + The Nostos, Goethe /
  Faustian Striving, Tolstoy / Ivan Ilyich's Mirror, Gilgamesh / The Search for
  Immortality, Weber / The Iron Cage, Murasaki / Mono no Aware, Bashō / Yūgen,
  Snorri / Ragnarök.
- **No** ache wall, **no** `aches.json`, **no** ache taxonomy, **no** verification
  badges-as-feature, **no** context lines, **no** two-door model. All deferred.
- **Exercise the hardest rule on day one.** The literary/`mean` skew above
  conveniently dodges plural-or-none. To stop the pilot from grading itself on the
  easy case, it must include **≥1 `open` / `live-rivals` concept shipped with ≥2
  genuinely rival PD passages** (e.g. free will, or the self), proving the
  plural-or-none machinery before we trust it. Log the pilot's tradition/era
  distribution so the PD-availability bias toward Western/ancient texts is visible
  and corrected, not hidden — the MISSION's even-handedness is a release gate.

### The in-copyright "Goodreads-norm" question is deferred, not decided
The debate's loosen-vs-strict axis (whether to post short attributed *in-copyright*
quotes, as people do on Goodreads) is **left open on purpose** — it is untestable
in the abstract and Phase 1's literary-PD scope means we may never need it. Revisit
it **only** if we later crave a living thinker's exact words, and then only as an
explicit, recorded **risk-acceptance** (no DMCA safe harbor for a hand-curator;
statutory-damage tail risk; aphoristic works fail factor 3), never as a quiet drift
past the guardrail.

### Honesty guardrails (load-bearing)
- **Ban "answer / encapsulates / the answer"** from UI copy and from the data
  field name. Frame as **recognition, not resolution** — *"others have stood where
  you stand; here is how one of them saw it."*
- **Plural-or-none for unsettled concepts.** A single passage is permitted only
  for `handed-off` / `hardened` concepts. For `live-rivals` / `open` / `dissolved`
  concepts, ship **≥2 genuinely rival passages or none** — never one passage that
  smuggles a verdict. (The PD pilot above is mostly literary/`mean`, chosen partly
  to sidestep this on day one; the rule binds the moment the feature meets a
  contested concept.)
- **The passage inherits its concept's 5-state badge** inline, so an `open`
  passage visibly reads as unsettled.
- **Barnum check is an authoring discipline, not a shipped badge.** Cut any
  passage that could comfort anyone, makes no falsifiable claim, or uses
  second-person flattery ("at times you…"). Specificity over comfort.
- **Sacred / non-Western texts** (sutra, hadith, Analect, and the Japanese
  aesthetic concepts in the pilot) carry a one-line provenance note and are never
  routed as "answers your ache." Transmit, don't extract.

### Copyright rules (risk analysis, not legal advice)
- **Verbatim only** from a **verified pre-1930 source edition**, *including the
  translation's date* — maintain a whitelist keyed to the **exact source edition +
  a scan/URL** (not just author + translator), so the byte-match has a single
  authoritative target. Prefer Project Gutenberg / archive.org scans. Byte-match
  every verbatim passage against that source.
- **Critical/scholarly editions are a trap.** Loeb, Oxford Classical Texts,
  Teubner, and the like carry **fresh editorial copyright** even over an ancient
  author; a pre-1930 *author* is not a pre-1930 *edition*. Whitelist only plain
  PD reprints, never an apparatus-bearing critical edition.
- **US-law, best-effort — not a global clearance.** This analysis is US public
  domain only (published 1930 or earlier, rolling +1/yr). EU compilation /
  *sui generis* database rights, moral rights, and non-US terms are **not**
  cleared here; flag this for any zh/ru/non-US source or audience before relying
  on it. This ADR is risk analysis, not legal advice.
- **In-copyright works → paraphrase + citation + "read it in the book" pointer**,
  never styled as a quotation.
- **No affiliate links** beside in-copyright verbatim text (kills the commercial
  factor). The book link is a quiet pointer, not a conversion funnel.
- For any marquee in-copyright author later, get a one-time attorney opinion
  before launch.

### Placement & presentation
- The passage renders **first in the drawer, above the gloss** (demote the gloss
  to a one-line dek beneath it).
- **Render the passage section only where a passage exists** — no empty slots,
  ever; the gap is invisible, not a broken promise.
- Full-contrast display serif (Cormorant/EB Garamond), generous size, **one ruled
  hairline** above a quiet provenance colophon (author · work · translator/edition
  · locator) and the book pointer. No faint context, no glow, no decorative card.
- Mobile: passage-first, gloss tap-to-expand.

### Pipeline
Mirror the readings pipeline: author passages as Python tuples
(`passages_mean.py`) merged into `ideas.json`; new drawer render + CSS; extend
`tests/smoke.mjs` (assert passage-first order, gated rendering, provenance
present, no empty-slot leakage).

## Rejected / deferred alternatives

- **R1 "one encapsulating passage per all 293 concepts, ache wall front door,
  badges, two doors."** Over-scoped, honesty-breaching, legally exposed, and
  uncompletable by one maintainer — the foliation mistake at 10× the labour.
- **Ache wall + emotional taxonomy + `aches.json`.** Deferred. If revived, it is
  an optional second-session filter, never the entrance, and every ache must route
  to a named thinker's *falsifiable* idea (the argument is the anti-Barnum
  mechanism). Framing fix required: route *question → tension → thinkers*, never
  second-person "your pain."
- **Cheaper rival, since SHIPPED (Option A):** upgrade existing reading `note`s
  into one vivid "why this book, at your life-moment" sentence — ~80% of the value,
  ~2% of the work, zero new schema, zero copyright exposure. **This shipped first
  (`12234f7`, 12 notes); see the Update below.** It is now the *control* the PD
  passage pilot must out-pull (see the kill-criterion). If the snippet turns out to
  be a terminus rather than an on-ramp, stop at the pilot and supersede this ADR.

## Consequences

- The atlas gains its emotional payload without betraying the honesty bar or
  opening an uncompletable second content forever-job.
- The gated-rendering rule means the feature is always "done" for the concepts it
  covers; coverage grows by theme cluster, never toward a 293 target.
- `passages_*.py` becomes a new authored data source paralleling `readings_*`;
  keep it small and verified rather than comprehensive.
- The deferred ache wall remains the most likely future expansion, but only behind
  the honesty + framing guardrails above.

## Update — Option A shipped (`12234f7`, 2026-06-23)

The cheaper rival went first. **12 reading-`note` upgrades** landed in
`src/readings.py` / `readings_extra.py` / `readings_extra2.py` (rebuilt into
`ideas.json` + `index.html`): Allegory of the Cave, The Unconscious, Collective
Unconscious, Individuation, Master & Slave Morality, The Absurd, Logotherapy,
To Have or To Be, Cognitive Behavioral Therapy, The Dao, Wu Wei, Yin–Yang/Qi.
The source list was drawn from the sibling **Muse** book project's corpus minus
the business titles, plus a few directly-named thinkers; the gloss, 5-state badge
and reading order were untouched. `build.py` + `tests/smoke.mjs` → 130 assertions
pass (notes carry no test assertions by design).

**The VOICE RULE the upgrades follow** (from a 2-agent voice critique): vivid but
**third-person**, historically **attributed**, **one image**, **~15–25 words**;
NO second-person "you", NO verdict words ("proves") on perennially-open questions,
NO quit-lit / workplace framing (which would leak the Muse book's thesis into the
neutral atlas), NO legend-as-fact. *An engraved caption, not a back-cover blurb.*

**What this changes for the pilot:** the passage feature is no longer measured
against an empty drawer but against these notes. Per the Phase 0 gate in the
Decision, run the 3-concept zero-code blind test *before* building or clearing
anything; the PD pilot proceeds only if a passage beats its note ≥2 of 3,
otherwise this ADR is **superseded-by-Option-A**.

## R3 — the copyright-vs-product debate (2026-06-23)

After Option A shipped, a "people share quotes on Goodreads all the time" challenge
prompted a third 3-agent pass: (1) **loosen** to the Goodreads norm — short
attributed in-copyright quotes + buy-pointer + 48h takedown policy; (2) **keep
strict** — PD-only verbatim + paraphrase, because a hand-curator is a directly
liable publisher with no DMCA safe harbor and the 12 notes already capture the
marginal value; (3) **product axis** — the copyright fight is *premature*; test
whether a passage beats its note at all before spending on clearance.

The three converged on one non-obvious fact: **passages only earn their keep on
literary/aesthetic concepts where the prose *is* the datum** (yūgen, Ivan Ilyich,
Homer, mono no aware) — and those are overwhelmingly **pre-1930 public domain
already**. So the segment where passages plausibly win is the segment with no
copyright problem, and the loosen-vs-strict axis is largely moot. The synthesis
(above) sequences the work: **Phase 0 zero-code blind test → Phase 1 PD pilot only
if it passes → in-copyright question deferred to an explicit future risk-acceptance.**

## Provenance of this decision

R1 research and R2 adversarial debate were run as parallel multi-agent passes on
2026-06-23; the maintainer synthesises (the adversaries are a foil, not an
auto-merge). R3 (copyright-vs-product, above) followed the same day after Option A
shipped. Both early rounds repeatedly encountered an injected "companion turtle
Logos" persona + bogus skill/task commands in fetched web content; every agent
flagged and ignored it (logged in `docs/PRIOR-ART.md` and maintainer memory).
