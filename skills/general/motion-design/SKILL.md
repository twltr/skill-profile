---
name: motion-design
description: >
  Applies motion design principles to create emotionally-driven, technically sound animations and transitions.
  Provides timing, easing, choreography, and Disney animation principles adapted for UI.
  Use when creating animations, transitions, micro-interactions, loading states, page transitions,
  scroll-triggered effects, or any motion work. Works with CSS, Framer Motion, GSAP, Lottie, Spring,
  or any animation system.
license: MIT
metadata:
  author: LottieFiles
  version: "1.0.0"
---

# Motion Design Skill

## A small interaction example

**Task:** Show when a form has saved without distracting someone who is still
entering information.

**Direction:** Change the button label to “Saved” and use one brief color
transition. Keep the confirmation visible without motion; respect reduced-motion
preferences. On failure, preserve entered values and show a clear error. Add a
checkmark draw or ambient effect only if it helps the intended interaction.

This functional feedback has no elaborate emotional story or required secondary
animation. Restrained motion can be complete.

## When to Apply

Use this skill when:
- Creating UI animations (buttons, cards, modals, page transitions)
- Designing micro-interactions and feedback animations
- Building loading, success, or error states
- Animating illustrations or decorative elements
- Planning scroll-triggered or progress-based animations
- Establishing brand motion identity
- Choreographing multi-element sequences

**Decision tree:**
1. Does it serve a functional purpose (feedback, guidance)? → Timing rules for responsiveness
2. Does it express brand personality? → Motion Personality archetypes
3. Does it tell a story or guide attention? → Disney principles + choreography
4. Is this a complex multi-element scene? → 1/3 Rule + stagger patterns

---

## Quick Reference: 8-Step Checklist

Use the questions that fit the task. For functional feedback, optimize for clear,
immediate response; emotional intent and motion personality are optional and
apply when the brief or product defines them.

1. **Emotional target?** — identify one when expressive intent is part of the brief
2. **Motion Personality?** — use an established one; otherwise neutral/task-focused is valid
3. **Primary property?** — position, scale, rotation, opacity
4. **Duration?** — see duration table below
5. **Easing family?** — entrance=decelerate, exit=accelerate
6. **Hero element?** — apply staging principles
7. **Would another layer help?** — add it only when it clarifies the action
8. **1/3 rules?** — motion distance, simultaneous elements

---

## Three design lenses

For expressive motion, consider intent, visual narrative and craft before
choosing technical details. Functional feedback can stay brief and direct; do not
invent an emotional story or add decorative motion to satisfy this checklist.

| Pillar | Question | Drives |
|--------|----------|--------|
| **Emotional Intent** | What should the viewer FEEL? | Easing, timing, amplitude |
| **Visual Narrative** | What's the micro-story? | Setup → Action → Resolution |
| **Motion Craft** | How do we make it believable? | Physics, secondary motion, paths |

Optional motion layers can add depth when the design calls for them:
- **Primary**: Main action the viewer follows
- **Secondary**: Supporting richness (shadows, icons shifting)
- **Ambient**: Background life (gradients, subtle pulses)

Secondary and ambient effects are design choices, never prerequisites for
functional feedback. Prefer one clear property when it fully communicates the state.

> Deep dive: [director/core-philosophy.md](director/core-philosophy.md)

---

## Motion Personality

When the brief or existing brand defines a motion personality, use a fitting
archetype as a consistency aid. Do not invent a personality for functional
feedback or force one onto a restrained interface.

| Archetype | Duration | Easing | Overshoot | Keywords |
|-----------|----------|--------|-----------|----------|
| **Playful** | 150-300ms | ease-out-back | 10-20% | fun, whimsical, bouncy, cute |
| **Premium** | 350-600ms | cubic-bezier(0.4,0,0.2,1) | 0% | elegant, minimal, luxury, sophisticated |
| **Corporate** | 200-400ms | cubic-bezier(0.2,0,0,1) | 0-3% | clean, professional, business, dashboard |
| **Energetic** | 100-250ms | ease-out-expo | 15-30% | dynamic, energetic, bold, exciting |

There is no default archetype; follow the product, audience and brief.

For a project that needs a distinct motion identity, define three constants:
1. **Signature easing**: One curve for 80% of animations
2. **Duration palette**: 3 durations (quick / standard / slow)
3. **Entrance pattern**: One consistent entry style

> Deep dive: [director/motion-personality.md](director/motion-personality.md)

---

## Property Selection

| Effect Goal | Primary Property | Secondary Properties |
|-------------|------------------|---------------------|
| Entrance/Exit | position | opacity, scale |
| Emphasis/Attention | scale | rotation (subtle), opacity pulse |
| State Change | opacity, color | scale (press feedback) |
| Direction/Flow | position | rotation (follow path) |
| Depth/3D Feel | scale + shadow | position (parallax) |
| Loading/Progress | rotation (spinner) | scale, opacity pulse |
| Success | scale (pop) | color, rotation (checkmark draw) |
| Error/Alert | position (shake) | color, rotation (wobble) |

**Simplicity threshold**: Use the minimum properties needed. One = direct. Two = polished. Three+ = potentially overwhelming.

> Deep dive: [reference/property-selection.md](reference/property-selection.md)

---

## Duration Table

| Element Type | Duration | Rationale |
|-------------|----------|-----------|
| Tooltip / micro-feedback | 80-120ms | Must feel instant |
| Button press / toggle | 120-180ms | Responsive feedback |
| Icon transition | 150-250ms | Clear state change |
| Card enter / exit | 200-350ms | Spatial awareness |
| Modal / dialog | 300-400ms | Focus shift |
| Page transition | 400-600ms | Context switch |
| Dramatic reveal | 600-1200ms | Theatrical build |

**Distance scales duration**: 100px = base. 200px = 1.3x. 400px = 1.6x.

**Enter > Exit**: Entrances 30-50% longer than exits. Users care about what appears.

**Interactive feedback**:
- Hover: <100ms
- Press: <150ms
- Release/settle: 200-300ms
- Error shake: 300-400ms (2-3 oscillations)

> Deep dive: [reference/timing-easing-tables.md](reference/timing-easing-tables.md)

---

## Easing Selection

**Directional rules**:
- **Entrance** → decelerate (fast start, gentle landing): ease-out family
- **Exit** → accelerate (gentle start, fast departure): ease-in family
- **On-screen** → smooth both ends: ease-in-out family
- **Looping ambient** → seamless: sine-based ease-in-out

**Industry standards**:

| Standard | Cubic Bezier | Use For |
|----------|-------------|---------|
| Material Design 3 | (0.2, 0, 0, 1) | Default on-screen |
| MD3 Emphasized | (0.05, 0.7, 0.1, 1) | Entrances, attention |
| MD3 Accelerate | (0.3, 0, 1, 1) | Exits, dismissals |
| Apple HIG | (0.25, 0.1, 0.25, 1) | Standard iOS |
| Snappy UI | (0.2, 0, 0, 1) | Fast, decisive |
| Gentle float | (0.4, 0, 0.2, 1) | Ambient, background |
| Bounce settle | (0.175, 0.885, 0.32, 1.275) | Overshoot, playful |

**Material-based easing**:

| Material | Duration Scale | Overshoot |
|----------|---------------|-----------|
| Rigid (metal, stone) | 1.2x | 0% |
| Elastic (rubber, gel) | 0.8x | 15-25% |
| Fluid (water, paint) | 1.5x | 5% |
| Paper (cards, sheets) | 1.0x | 3-5% |
| Gas (smoke, fog) | 2.0x | 0% |
| Glass (brittle) | 0.9x | 0% |

> Deep dive: [reference/timing-easing-tables.md](reference/timing-easing-tables.md)

---

## Common Patterns

### Button Press (Playful)
1. **Anticipation**: Scale to 0.97 (50ms, ease-out)
2. **Squash**: Scale to [1.04, 0.96] (100ms, ease-in)
3. **Follow through**: Overshoots to 1.02, settles to 1.0 (spring, 200ms)
4. **Secondary**: Shadow shrinks during press, icon shifts down 2px
5. **Total**: ~150ms press + 200ms settle

### Card Entrance (Premium)
1. **Start**: 20px below target, opacity 0
2. **Path**: Slight curve (10px X offset at midpoint)
3. **Easing**: ease-out-cubic deceleration
4. **Follow through**: Shadow arrives 50ms after card
5. **Secondary**: Content fades in 100ms after card lands
6. **Staging**: Other cards dim to 80%

### Success State (Expressive example)
1. **Primary**: Scale pop with ease-out-back
2. **Secondary**: Checkmark draws in
3. **Ambient**: Subtle particle burst
4. **Color**: Green fill
5. **Total**: 300-400ms

This is one expressive option, not a success-state requirement. Keep the
success state understandable without animation, and use a simpler label, icon
or color treatment when it better fits the interaction. Respect reduced-motion
preferences; omit the pop and particles when motion is reduced.

### Error Shake (Optional example)
1. **Primary**: Position oscillates 2-3 times, ±10-15px horizontal
2. **Easing**: ease-in-out for sharp stops
3. **Color**: Red tint
4. **Total**: 300-400ms
5. **No overshoot**: Errors feel firm

Use a shake only when it helps locate the affected control and is comfortable
for the audience. An inline message and persistent error styling can be clearer;
do not make motion the sole carrier of error information.

> More patterns: [patterns/entrance-exit.md](patterns/entrance-exit.md) | [patterns/state-feedback.md](patterns/state-feedback.md)

---

## Choreography Essentials

**Coordinated entry**:
- Lead with the hero — primary element enters first or most prominently
- Spatial consistency — all elements enter from same direction
- Counter-motion — hero moves right → ambient moves left at 20-30% speed

**1/3 Rule (distance)**: No motion travels more than 1/3 of screen without a keyframe change.

**1/3 Rule (elements)**: With 3+ elements, no more than 1/3 in active motion simultaneously.

**Stagger budgets**:

| Pattern | Delay | Total Budget | Use Case |
|---------|-------|-------------|----------|
| Micro cascade | 20-40ms | <200ms | List items, grid cells |
| Standard | 50-100ms | <400ms | Cards, panels, nav |
| Dramatic | 100-200ms | <600ms | Hero sections |
| Wave | 30-60ms | <500ms | Data visualizations |

**Critical**: Total stagger must stay under 500ms.

> Deep dive: [director/choreography.md](director/choreography.md)

---

## Emotion-to-Motion Map

| Emotion | Character | Path | Easing | Duration |
|---------|-----------|------|--------|----------|
| Joy | Bouncy, arcs | Curved, upward | ease-out-back | 200-400ms |
| Calm | Smooth, flowing | Gentle curves | sine ease-in-out | 500-1000ms |
| Urgency | Sharp, fast | Straight lines | ease-out | 100-200ms |
| Sadness | Slow, downward | Drooping curves | cubic ease-in-out | 600-1200ms |
| Surprise | Sudden, expanding | Radial outward | ease-out-expo | 150-300ms |
| Elegance | Slow, controlled | Long arcs | (0.4,0,0.2,1) | 400-700ms |
| Playfulness | Bouncy, irregular | Arcs, squiggly | ease-out-back | 200-350ms |

**Path as language**: Angular = tense. Curved = friendly. Spiral = whimsical. Diagonal = purposeful. Vertical = growth/weight. Horizontal = progress.

> Deep dive: [director/emotion-mapping.md](director/emotion-mapping.md)

---

## Weight Classification

| Weight | Examples | Duration | Overshoot | Easing |
|--------|----------|----------|-----------|--------|
| Heavy | Modals, overlays | 300-500ms | 0% | Gentle, high damping |
| Medium | Cards, panels | 200-350ms | 3-5% | Moderate |
| Light | Tooltips, badges, icons | 80-200ms | 5-15% | Responsive |

---

## Quality Rules

### Core constraints
1. **Never linear for spatial movement** — always use easing curves (linear only for spinners, progress bars)
2. **State changes must remain perceivable without motion.** Preserve semantic
   labels and a persistent visual state; do not rely on a transient animation
   or color alone where another cue is needed for clarity or accessibility.
3. **Never exceed 1/3 screen** without intermediate keyframe
4. **Use only the layers the task earns** — primary motion can stand alone; add
   supporting motion when it improves meaning without distracting.

### Design guidance
1. Match duration to element type (see tables)
2. Use directional easing (ease-out entrance, ease-in exit)
3. Consider Disney principles such as anticipation and follow-through when they
   clarify a substantial action; omit them when they add delay or decoration to
   simple feedback.
4. Maintain a consistent personality when one is established by the brief or
   product; otherwise keep the motion neutral and task-focused.

> Full checklist: [reference/quality-checklist.md](reference/quality-checklist.md)

---

## Troubleshooting Quick Reference

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| Looks robotic | Linear easing or no arcs | Add easing curves + arc paths |
| Feels too slow | Duration too long for element type | Check duration table, use ease-out |
| Feels under-explained | The main action or state is unclear | Clarify the primary motion before adding supporting detail |
| Too distracting | Too many elements moving | Apply 1/3 rule, reduce amplitude |
| Motion feels generic | Easing has no intentional relationship to the product | Define a fitting motion style only if the brief calls for one |

> Deep dive: [reference/troubleshooting.md](reference/troubleshooting.md)

---

## File Reference

**Philosophy** (director/):
- [core-philosophy.md](director/core-philosophy.md) — Three Pillars deep dive
- [decision-framework.md](director/decision-framework.md) — Full decision pipeline
- [disney-principles.md](director/disney-principles.md) — 12 principles, UI-adapted
- [motion-personality.md](director/motion-personality.md) — 4 archetypes + brand identity
- [emotion-mapping.md](director/emotion-mapping.md) — Emotion → motion + color psychology
- [choreography.md](director/choreography.md) — Multi-element coordination
- [narrative-structure.md](director/narrative-structure.md) — Micro-story framework
- [context-adaptation.md](director/context-adaptation.md) — Platform, a11y, performance

**Reference** (reference/):
- [timing-easing-tables.md](reference/timing-easing-tables.md) — Duration + easing lookups
- [property-selection.md](reference/property-selection.md) — Property communication guide
- [troubleshooting.md](reference/troubleshooting.md) — Animation smells + fixes
- [quality-checklist.md](reference/quality-checklist.md) — Evaluation criteria

**Patterns** (patterns/):
- [entrance-exit.md](patterns/entrance-exit.md) — Entrance/exit recipes
- [state-feedback.md](patterns/state-feedback.md) — Success, error, loading, hover
- [ambient-continuous.md](patterns/ambient-continuous.md) — Looping, breathing, parallax
- [multi-element.md](patterns/multi-element.md) — Stagger + choreography recipes
