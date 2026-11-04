# Quality Checklist

## Visual Quality
- [ ] Elements >40px for motion, >100px for detail
- [ ] Readable at full speed without slow-motion
- [ ] Any secondary or ambient layer has a clear purpose and does not distract
- [ ] Counter-motion for balance where needed
- [ ] Natural arcs (unless intentionally mechanical)
- [ ] 1/3 rule (distance): no unbroken motion >1/3 container
- [ ] 1/3 rule (density): max 1/3 elements active simultaneously

## Technical Quality
- [ ] No linear easing on spatial movement
- [ ] Duration matches element type table
- [ ] Ease-out entrances, ease-in exits
- [ ] Duration proportional to distance
- [ ] Entrance duration >= exit duration
- [ ] State changes remain clear in the settled UI and without motion
- [ ] Stagger total <500ms
- [ ] Follow-through or child-element delay only when it clarifies the action

## Emotional Quality
- [ ] Intended perception or emotion identified before properties
- [ ] If the brief establishes a motion personality, it matches the product
- [ ] Setup → action → resolution structure when it helps explain the motion
- [ ] Intensity matches interaction importance
- [ ] Consistent: same interaction = same motion
- [ ] Appropriate on 100th viewing

## Performance Quality
- [ ] Primary motion uses transform + opacity
- [ ] <20 animated elements per viewport
- [ ] No layout-triggering properties animated
- [ ] Elements staggered, not simultaneous
- [ ] Maintains 60fps (30fps acceptable for ambient)

## Accessibility Quality
- [ ] prefers-reduced-motion alternative provided
- [ ] No vestibular triggers without alternative
- [ ] Same interaction = same animation
- [ ] Critical info not motion-only
- [ ] Animations >5s are pausable

## Severity Tiers

### Core constraints
- Linear easing on spatial movement
- State communicated only by motion, transient feedback or color where another cue is needed
- Exceeds 1/3 screen rule
- Missing primary layer
- Stagger >500ms
- Layout property animation causing jank

### HIGH
- A supporting motion layer adds no useful meaning
- Duration mismatch with element type
- Wrong directional easing
- Inconsistent personality when one is established
- No follow-through when it would clarify substantial motion
- Missing reduced-motion alternative

### MEDIUM
- Ambient motion distracts from the primary action
- No anticipation phase when it would clarify substantial motion
- Overshoot mismatch
- Could use better arcs
- Missing counter-motion
