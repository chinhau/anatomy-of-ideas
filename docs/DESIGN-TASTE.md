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
| `--oppose/--echo/--affirm` | `#c75a45 / #7da0e0 / →parchment-dim` | relation inks — minium red (rejects) + muted azurite (echoes); **builds is neutral parchment**, carried by dash + glyph, not hue |
| status inks (5-state) | `#c98a52 / #9a8fb0 / #d9b65f / #c3c7cf / #9aa3bd` | epistemic taxonomy — handed-off (raw sienna) / hardened (amethyst) / live-rivals (gold, heartbeat) / open (silver) / dissolved (muted); a *separate axis* from relations |

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
5. **Storyboard / user-journey critic** — judges the *end-to-end journey*, not the
   pixels: narrative coherence, onboarding/legibility (is the first-contact point
   right? are tooltips enough?), friction & failure points (empty states, mobile,
   "why does this element mean *that*?"), and the emotional arc. Brief it with §1
   *and the data model* — it earns its keep by catching when a planned ornament
   duplicates an existing encoding or rests on a taxonomy the data won't support
   (it reshaped ADR 0005: it killed the 6-bespoke-tradition-mark plan before a
   line was written). Run it **before** implementing, alongside or ahead of the
   four visual agents.

> Cadence: run the visual agents in parallel; run the storyboard critic before
> implementing. Then **the maintainer synthesizes** — the Jobs pass is a foil,
> not an auto-merge.

---

## 5. Convergent verdict (audit 2026-06-23 · status refreshed 2026-06-23)

Four agents above, run independently, agreed on the same handful of things. This
was our punch-list of where the build *drifts from the taste*. **All seven items
are now resolved** (status refreshed 2026-06-23; several were closed by
palette/engraving/structure work that post-dated the audit). The list is kept
below as a worked record of the taste in action — each item ✓ DONE with the
commit or current-state evidence — rather than a live TODO.

- **✓ Gold leak — DONE.** The flagged section labels (`.dr-sec`, `#about-panel h3`,
  `.flt-sec`, `.dr-think b`, …) were already on `--ink` in HEAD; the second-tier
  static-label gold (`.caption b`, `.reading .rk`, `.hchip b`, `.flt-head`,
  `.recur-i .rc-n`, the read-state card markers, the `.dr-figure` region-tint
  fallback, the `⁂` colophon tint) was demoted to `--ink`, and the "builds"
  separator `.lt-sep.b` to `--parchment-dim`, in commit `812fa8b`. Gold is now
  active / selection / seal / CTA / masthead eyebrow only.
- **✓ Glow → engraving — DONE (`8a76b35`).** `#lglow`/`#cglow` were already gone;
  the live halos — `.dr-sigil`'s 5px region bloom, `.dr-seal`'s gold glow, and the
  `#cameo` portrait's `feGaussianBlur` gold-halo chain — were removed, and `.dr-seal`
  given the same crisp zero-blur relief as the brand-mark/gate-seal. The deck-card
  elevation shadows (black, downward, tightly clipped) are kept on purpose: lifted
  physical cards, not bloom.
- **✓ Semantic inks de-bootstrapped — DONE.** Relations are now minium red
  `#c75a45` / azurite `#7da0e0` (the "teal" the audit flagged is gone) / neutral
  parchment-dim; the 5-state status inks are mineral (raw sienna / amethyst / gold /
  silver / muted — see §3). No bootstrap red/teal/green remains anywhere.
- **✓ SMP door-glyphs avoided — DONE.** The Deck-of-Doors signs never reach a
  font: each renders as **inline SVG** (`.lb-glyph`, `viewBox="0 0 24 24"`,
  `stroke:currentColor`) and the petal-count device as the `.lb-rose` SVG rosette
  — pure engraving logic, no Plane-1 codepoints to tofu.
- **✓ The `↯` lightning mark is gone — DONE.** The opposes relation now reads as
  `≠` on cards and follows the dossier's own `↔ / → / ←` grammar in the relations
  list (`↔` for echoes, directional `→ / ←` otherwise). No zigzag glyph remains.
- **✓ Status badge stripped — DONE.** `.q-status` is now just `qs-mark` (glyph) +
  `qs-label` + state ink; the `qs-residue` second-colour line and the `qs-conf`
  micro-caption are gone, so the busiest column carries one colour, not three.
- **✓ Garnish ornaments cut — DONE (`27d05b1`).** The three guardrail-1 failures —
  the `⁂` dossier colophon, the second `.dr-seal` wax seal (a duplicate of the
  masthead rosette), and the spinning `.rdie` die — were removed outright. (This
  also retired the `.dr-seal` relief added in `8a76b35`, since the seal is gone.)

The substrate the agents *praised* — void-indigo ground, hatch tooth, SVG seals
whose petals count the 11 questions, the region metal-ink school tints — is the
project's strongest asset and the truest expression of the taste. Protect it.
