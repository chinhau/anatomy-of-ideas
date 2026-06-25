# Landing & threshold art-direction spec

The distilled target for the landing redesign (and the art direction it
propagates to all four tabs). It sits **downstream of**
[`DESIGN-TASTE.md`](DESIGN-TASTE.md) (the canonical taste) and
[ADR 0003](decisions/0003-hermetic-codex-art-direction.md) (the art-direction
decision). This file is narrower: it is the **resolved look for the front door**,
distilled from a six-register moodboard pass (2026-06-24), and the brief the
mockup rebuild aims at.

It is **not yet ratified** — a landing *direction* (A/B/C or a splice) is still the
maintainer's call. Once chosen, this graduates into an ADR. Until then it is the
shared target so each rebuild starts from the same picture instead of re-deriving it.

---

## 1. The refined north star (one line)

> A **lapis-and-gold celestial atlas, drawn by a visible hand, that strikes itself
> into being in a single move.**

This sharpens — does not replace — the DESIGN-TASTE north star ("a Renaissance book
of secrets rendered as a dark sky-atlas"). It adds three things the moodboard made
concrete: a **warmer, deeper blue** (illuminated-manuscript lapis, not flat navy), a
**visible authoring hand** (marginalia honesty), and a **single signature gesture**
(ensō restraint) rather than a pile of effects.

It also arbitrates the governing vision ("a sanctum people come to for ancient
knowledge"): **awe earned from truth**, the register of great libraries and
illuminated manuscripts up close — *not* spectacle. Harry-Potter glow and
MapleStory game-UI stay out.

**The stakes (the bar to build to).** The ambition is genuinely maximal: a
threshold that expands the person who crosses it — that makes 4,000 years of
humanity's hardest questions *land* as immensity. We aim as high as that. The
discipline is that we get there through **truth, not spectacle**: the awe must come
from the real depth (the actual 425 thinkers, real lineages, real unresolved
rivalries), because spectacle dazzles once and dies on the second visit, while
earned reverence survives the tenth. So: **maximal in the aim, disciplined in the
means.** Push immensity and reverence as far as they go; deliver them through one
true, earned gesture — never a light show.

---

## 2. The four principles (each maps to concrete craft)

| Principle | Means | Craft rule |
|---|---|---|
| **Awe** | reverence + depth + immensity | Lapis-deepened void + **struck** gold leaf. Gold is luminous because a *raking band* crosses a fixed surface — **never** a glow/bloom filter. |
| **Truth** | awe must be earned by real depth | Every mark encodes a real datum: the actual graticule, real star/thinker positions, brightness = thinker-count. No decorative stars. |
| **Honesty** | one vantage, offered to argue with | A faint **marginalia / working-hand** layer so it reads as *a* scholar's map, not a corporate infographic. |
| **Restraint** | the ensō discipline | The signature is **one** gesture (the graticule ruling itself; the seal striking gold), not stacked transitions. One thing, done completely. |

These are the DESIGN-TASTE guardrails (encode-a-datum / engraving-not-glow /
restraint-as-luxury) re-expressed for the front door.

---

## 3. The palette move: deepen the void toward lapis

The illuminated-manuscript register (ultramarine ground + burnished gold + parchment)
is the historical "sacred-celestial" palette. Our void+gold is already this — just
colder. The proposal is to warm/deepen `--void-2` toward saturated lapis so gold
sits on it the way leaf sits on ultramarine.

| Token | Current | Candidate | Note |
|---|---|---|---|
| `--void` | `#070b16` | unchanged | the near-black ground stays |
| `--void-2` | `#0e1530` | ~`#101d44` (lapis) | a **knob to tune against the live build**, not a final value — push only as far as gold still reads as the rarest ink |
| `--gold` | `#d9b65f` | unchanged | rendered as *struck leaf* (specular sweep), not a fill that glows |

Everything else in the DESIGN-TASTE palette table holds. The lapis shift is the one
new variable, and it is **opt-in / reversible** — if it cheapens the void, revert.

## 4. The struck-gold technique (load-bearing, restated)

Gold = a **specular highlight / raking-light band** that sweeps **once** across a
**fixed** gold surface — via `feSpecularLighting`, a moving `<linearGradient>` stop,
or a `clip-path` reveal. This is the anti-kitsch move that reads luminous while
honoring the no-glow guardrail. It is the title/pole reveal in B and the
brown→gold strike in C. All three directions reach for it.

Engraving (stroke-dashoffset draw-on) stays the **entry verb**; paper-grain via
`feTurbulence` = 0 bytes. Baseline ships at ~0 added bytes; bytes only buy optional
ceiling-raisers (a font weight, a metal texture, opt-in sound).

---

## 5. Provenance — the six registers (moodboard, 2026-06-24)

Each register contributed one thing; the spec is the through-line, not any single one.

| Register | What was found | Contribution |
|---|---|---|
| **Celestial atlas** (Cellarius; navy radial planisphere) | gold/blue hemisphere charts; a pole-centred graticule on void | The **flagship B look**, already in our palette — proof it photographs as awe, no glow. |
| **Alchemy emblem** (Rosarium; concentric labyrinth) | fine-line ink, concentric rings, low amplitude | **The fix for C's gear-seal** — more rings + finer strokes + lower petal amplitude = cosmos, not cog. |
| **Tarot Marseille** | framed card + Roman numeral + title-plate | A **structure idea**: the 11 great questions as titled plates. |
| **Zen ensō** | one brushstroke, the deliberate gap | **Restraint corrective** — one gesture can carry a whole screen. |
| **Grimoire** | handwritten marginalia, diagrams woven into script | The **honesty texture** — a real working hand; "one vantage, argued-with." |
| **Illuminated manuscript** | lapis ground + burnished gold leaf + parchment | The **reverence palette**; validates struck-gold-not-glow (leaf catches raking light). |

---

## 6. Direction implications

The synthesis sharpens **B (Dark Sky-Atlas)** as the lead: a lapis-and-gold
celestial atlas, drawn by a visible hand, that strikes itself into being. Concretely
for the rebuild:

- **B** — adopt the lapis `--void-2`; keep brightness = thinker-count (real datum);
  thin the constellation **away from centre** so the headline doesn't collide
  (known mockup nit); add a faint marginalia layer (honesty) used sparingly.
- **C** — if pursued, the gear-seal is fixed by the alchemy-emblem reference:
  more concentric rings, finer strokes, lower rosette amplitude.
- **A** — the page-turn grammar is intact; the plain static end-frame needs the
  lapis+gold reverence treatment to not read flat.
- **Splice (the standing recommendation):** lead with **B**, borrow **C's struck-gold
  band** for the title/pole reveal and **C's *solve et coagula*** as the tab-to-tab
  transition grammar.

---

## 7. Open questions (resolve before the production build)

1. **Font conflict.** Live gate + mockups use Cinzel + EB Garamond + Inter;
   DESIGN-TASTE §3 mandates Cormorant Garamond + Inter (no third family). Needs a
   ruling — keep Cinzel for the celestial/display voice and amend the doc, or
   collapse to Cormorant. **Unresolved.**
2. **Lapis hex.** §3 candidate `#101d44` must be tuned against the live build; push
   only as far as gold stays the rarest ink.
3. **Marginalia dosage.** The honesty layer is powerful and easy to overdo — it must
   stay faint enough to never compete with the seal/constellation. One ensō, not a
   crowded page.

---

## 8. Reference trail (Pinterest / Are.na, 2026-06-24)

Search terms that produced the strongest period sources (re-runnable):
`celestial atlas engraving` · `alchemical emblem engraving manuscript` ·
`tarot marseille engraving line art` · `zen enso sumi ink minimal` ·
`grimoire spell book page sacred geometry ink` · `illuminated manuscript gold leaf
astronomy`. Hazard noted: AI-celestial imagery (Midjourney house style) defaults to
glowing-sun mandalas with ornate borders — the spectacle register this spec rules
out; useful only as a what-not-to-do boundary.
