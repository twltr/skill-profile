# Troubleshooting

## Looks Robotic
- Linear easing → use ease-out (entrance) or ease-in-out
- Straight paths → add 10-20px arc at midpoint
- Uniform timing → stagger 50-100ms between elements
- Everything synced → offset start/stop 50-150ms
- The action lacks emphasis → consider one supporting cue only if it improves clarity

## Feels Too Slow
- Duration exceeds type budget → check duration table
- ease-in-out when ease-out works → ease-out feels faster
- Too much anticipation → reduce to 10% or remove
- Stagger exceeded → total <500ms
- Overshoot settle too long → increase damping

## Feels Too Fast / Jarring
- Duration below minimum → modals 300ms+, pages 400ms+
- No easing → add ease-out minimum
- Missing resolution → add 50-100ms settle
- No anticipation on large motion → add 100-200ms wind-up

## Feels Cheap / Flat
- Primary motion is unclear → clarify its timing or direction before adding effects
- State hard to perceive after motion → strengthen the persistent label, icon or styling; add motion only if it improves clarity
- Same easing everywhere → vary primary vs secondary
- No follow-through on substantial motion → consider a brief settle; do not add delay to simple feedback
- No overshoot → add 3-10%

## Too Distracting
- Too many moving → 1/3 rule
- Amplitude too large → reduce to minimum
- Competing heroes → one per moment, dim rest
- Ambient too prominent → 10-20% amplitude, slower
- No breathing room → 100-200ms pause between beats

## Motion feels inconsistent
- If the brief or product establishes a personality, align easing and duration with it
- Define a shared palette or entrance pattern only when the project needs a distinct motion identity
- If no personality is established, use clear, task-focused motion; do not invent one to fill a gap

## Inconsistent Feel
- Different easing same-type → standardize per motion type
- Duration varies same type → use palette consistently
- Entry direction changes → one origin everywhere
- Overshoot inconsistent → apply rules consistently

## Performance (Dropped Frames)
- Animating width/height/margin → use transform
- Too many elements → <20 per viewport
- Complex shadows/filters → simplify or pre-render
- No GPU acceleration → transform + opacity
- All simultaneous → stagger to spread load

## Quick Diagnostic

1. No linear on spatial movement
2. Duration matches element type
3. Any supporting layers earn their place
4. Consistent personality when the brief or product establishes one
5. Directional easing correct
6. 1/3 screen rule
7. 1/3 element rule
8. Follow-through supports the action without unnecessary delay
9. Every motion has purpose
10. Fine on 100th viewing

## If the project uses a defined personality
- **Playful**: overshoot >25% = broken; not everything bounces; short+bounce = glitchy
- **Premium**: too subtle = invisible; too slow = waiting; zero = broken
- **Corporate**: too conservative = boring; playful easing breaks trust; identical = monotonous
- **Energetic**: max everywhere = nothing stands out; too many particles; no settle = chaos
