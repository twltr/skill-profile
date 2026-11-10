# Core Philosophy

Treat the ranges and examples below as starting points for the brief, not mandatory
presets. Legible state, accessibility and the purpose of the interaction govern.

## Three Pillars

### Pillar 1: Emotional Intent
Name what the motion should help a person perceive or do. Choose an emotion only
when the brief calls for expressive motion; functional feedback can simply be clear
and immediate.

| Emotion | Character | Timing | Easing |
|---------|----------|--------|--------|
| Trust | Smooth, predictable | 300-400ms | Gentle curves |
| Delight | Bouncy, surprising | 200-300ms | Overshoot |
| Urgency | Sharp, direct | 100-200ms | Snappy ease-out |
| Calm | Slow, flowing | 500-1000ms | Sine curves |
| Surprise | Sudden, explosive | 150-300ms | Exponential |
| Confidence | Direct, decisive | 200-400ms | Strong ease-out |

### Pillar 2: Visual Narrative

| Phase | Duration Share | Purpose |
|-------|--------------|---------|
| Setup | 20-30% | Establish context, prepare viewer |
| Action | 30-40% | Primary motion, hero moment |
| Resolution | 30-40% | Settle, breathe, confirm |

Use setup → action → resolution when it helps explain the motion. A simple tooltip
or save confirmation does not require three authored phases.

### Pillar 3: Motion Craft
- Easing curves match emotional intent
- Duration proportional to element size and distance
- Arcs for organic, straight for mechanical
- Optional secondary motion (shadows, related elements) when it supports the action
- For coordinated multi-element motion, stagger only when it clarifies hierarchy;
  synchronized feedback or one element can be the right choice.

## Optional Motion Layers

| Layer | Role | Amplitude |
|-------|------|-----------|
| Primary | Main action viewer follows | 100% |
| Secondary | Supporting richness | 30-50% |
| Ambient | Background life | 10-20% |

- Secondary offset 50-100ms from primary, different easing
- Ambient is continuous/slow, never demands attention
Add a secondary or ambient layer when it clarifies hierarchy or adds useful
character. A focused action may use only its primary motion.

## Long Travel
For motion crossing a large part of the screen, consider intermediate beats,
direction or speed changes only when they improve comprehension. Do not add
keyframes solely to satisfy a distance quota.

## The Attention Budget
- One hero motion per scene moment
- Max 2-3 elements in active motion simultaneously
- Ambient doesn't count against budget
- Choose staggering or synchronization according to the relationship being shown
