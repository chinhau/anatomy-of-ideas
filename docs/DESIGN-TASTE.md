# Design taste — the spiritual aesthetic of *The Anatomy of Ideas*

This is the canonical statement of **what good looks like** for this project, and
the **reusable roster of design-critique agents** we deploy to keep it honest.
It exists so that any future design pass starts from the same taste rather than
re-deriving it. It sits downstream of [ADR 0003](decisions/0003-hermetic-codex-art-direction.md)
(the art direction *decision*); this file is the art direction *applied as taste*.

---

## 1. The north star (one line)

> A Renaissance **book of secrets** rendered as a **dark sky-atlas**.

Esoteric **visual** language — astrology, tarot, alchemy — over **rigorous**
philosophy content. The feeling we are buying is **magical gravitas**: a serious,
hand-engraved codex of cosmology, *not* a fantasy-novel prop or a theme-park.

### What the "spiritual aesthetic" IS
- **Engraved, not lit.** Hairlines, copperplate hatching, ruled frames, ink on
  parchment over void-indigo. Depth comes from line weight, never from a bulb.
- **Cosmographic.** The atlas is a sky chart: graticules, astrolabe devices,
  seals/rosettes whose petals *count* real things.
- **Restrained luxury.** Gold is the rarest ink. Most of the page is quiet
  parchment-on-void; the eye earns each accent.
- **Scholarly first.** The mysticism is in the *binding and plates*, never in the
  claims. Content stays peer-reviewable.

### What it is NOT (the kitsch line)
- No glow, bloom, neon halo, gradient sheen, sparkle, or emoji.
- No fortune-telling framing, suit icons, "lucky numbers," or angel numbers
  (the whole **numerology** strand was tried and **cut** — do not re-propose it).
- No generic dark-SaaS idioms: bootstrap red/green/teal status colours, soft
  drop-shadow cards, pill badges that don't encode a datum.
- No "Harry Potter prop" pastiche — magical **gravitas**, not whimsy.

---

## 2. The three governing guardrails (anti-kitsch — load-bearing)

1. **Ornament must ENCODE a real, user-actionable datum — never garnish.**
   Before any flourish ships, answer: *what does a user read off this, and will
   they notice and use it?* Weak answer → cut it.
2. **Engraving logic, not glow.** Line / hatch / hairline / ruled frame. Never
   blur, bloom, gradient, sparkle, or emoji.
3. **Restraint as luxury.** `--gold` is reserved for **masthead / active tab /
   selection / seals** only. Everywhere gold becomes a default label ink, it
   stops being special.

> Precedent that sets the bar: the maintainer shipped per-card Roman-numeral
> foliation, looked at it, said "a little too much," and deleted the entire
> numerology strand. We *find the balance*; we do not maximize richness.

---

## 3. The materials palette (quick reference)

| Token | Hex | Role |
|---|---|---|
| `--gold` | `#d9b65f` | rarest ink — masthead / active / selection / seals only |
| `--vermilion` | `#b8472f` | rubrication / contested / alarm — sparing |
| `--ink` | `#7a6038` | the *demoted-label* brown (currently under-used) |
| `--parchment` / `--parchment-dim` | `#e9dcc0` / `#b6ad96` | primary / secondary text |
| `--muted` | `#9aa3bd` | tertiary, captions |
| `--rule` | `#2a3354` | hairlines / frames |
| `--hatch` | 45° 0.045-alpha repeat | engraved "tooth" texture |
| `--oppose/--echo/--affirm` | `#d8505c / #5fc7b8 / #86c08a` | semantic trio — **the weakest part of the palette** (reads as generic UI status; re-pitch toward mineral inks) |

Typefaces: **Cormorant Garamond** (display serif — titles, italic glosses;
floor ≈ 16px, it goes spindly below that) + **Inter** (all UI chrome / labels /
body). No third family.

---

## 4. The design-critique agent roster (reusable)

Deploy these as **parallel, read-only** `general-purpose` agents whenever we touch
the look. Each brief below is self-contained; paste it, point it at
`src/template.html` (the source of truth — CSS `<style>` block near the top,
`:root` tokens ~line 16; the built `index.html` is generated, never edit it), and
always hand it §1–§2 of this file as the bar. Ask for **prioritized `file:line`
findings + concrete fixes + a 3-sentence verdict**, and **no edits**.

1. **Typographer** — type pairing, modular scale, hierarchy, micro-typography
   (tracking/leading/optical size), Cormorant's small-size floor, weight
   discipline, gold-text leak.
2. **Esoterica & symbol scholar** — every glyph/seal/sigil: semantic correctness,
   Unicode coverage (tofu risk for SMP alchemical codepoints — prefer inline SVG
   or BMP), guardrail-1 honesty, codex-vs-kitsch authenticity.
3. **Colour & art director** — palette coherence, WCAG AA contrast, gold
   discipline, texture-vs-glow, region/metal-ink taxonomy.
4. **Steve Jobs / restraint** — holistic taste & busyness; names what to CUT;
   defends the *one thing* the product is and whether every element serves it.

> Cadence: run all four in parallel, then **the maintainer synthesizes** — the
> Jobs pass is a foil, not an auto-merge.

---

## 5. Convergent verdict (audit 2026-06-23)

Four agents above, run independently, agreed on the same handful of things. This
is our current punch-list of where the build *drifts from the taste* — useful as
both a TODO and a worked example of the taste in action:

- **Gold is leaking.** It drives ordinary section labels in 8+ places
  (`.dr-sec`, `#about-panel h3`, `.flt-sec`, `.dr-think b`, …) instead of
  active/selection/seal only. The idle `--ink #7a6038` token is the intended
  demoted-label colour — put it to work. *(Highest-leverage fix; breaks guardrail 3.)*
- **Glow violates engraving logic.** `feGaussianBlur` node halos (`#lglow`,
  `#cglow`) and 18–26px coloured box-shadow card halos are theme-park bloom →
  replace with crisp 1px engraved rings. *(Breaks guardrail 2.)*
- **The semantic trio is bootstrap.** red/teal/green status colours — `--echo`
  teal especially is alien to a period palette → re-pitch toward mineral inks.
- **SMP alchemical door-glyphs will tofu off-macOS.** Six Deck-of-Doors signs are
  Plane-1 codepoints with no coverage in Cormorant/Inter and an uncontrolled
  fallback → render as inline SVG (same engraving logic) or retreat to BMP.
- **The `↯` "opposes" mark misreads as lightning** and is inconsistent with the
  dossier's own `↔ / → / ←` grammar → reuse the directional arrows or a struck bar.
- **The status badge is the heartbeat — and it's diluted.** Strip `.q-status` to
  glyph + label + state ink; cut the `qs-residue` second-colour line and the
  `qs-conf` micro-caption that double the colour load in the busiest column.
- **A few pure-garnish ornaments** fail guardrail 1: the `⁂` dossier colophon,
  the `.dr-seal` second wax seal, the spinning `.rdie`.

The substrate the agents *praised* — void-indigo ground, hatch tooth, SVG seals
whose petals count the 11 questions, the region metal-ink school tints — is the
project's strongest asset and the truest expression of the taste. Protect it.
