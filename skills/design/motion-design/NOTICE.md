# Source and local adaptation

Based on LottieFiles' Motion Design skill at
`b6606e101601ef027f01729a7289e97c329ad0cd`:
https://github.com/LottieFiles/motion-design-skill/tree/b6606e101601ef027f01729a7289e97c329ad0cd

The supplied [MIT license](LICENSE) is preserved. Local revisions on 2026-11-04
add an early functional-feedback example and reconcile the main method and
supporting guidance: static state clarity, accessibility and the actual brief
govern; expressive layers, archetypes, particles and shakes are optional when
they serve that brief. Reduced-motion behavior preserves the outcome. This
records an adapted package, not a byte-preserved snapshot or an animation trial.

## Currency check, 2026-11-10

- **Upstream:** `LottieFiles/motion-design-skill` HEAD is `f9a8a041b85185ee4881b3471d3415e939aac772`
  (2026-05-18). The only changes since our base are two README commits adding a
  banner image; `skills/motion-design/` is unchanged, so nothing was taken over.
- **Corrected facts:** the easing tables labeled CSS's `ease`
  (0.25, 0.1, 0.25, 1) as "Apple HIG / iOS default"; it is the browser default,
  and UIKit's `easeInOut` is (0.42, 0, 0.58, 1). The duplicate "Snappy UI" row
  (identical to MD3 Standard) was merged, MD3 rows now carry their token names,
  and (0.4, 0, 0.2, 1) is named as Material 2's standard curve. The spring note
  explained the table's absolute damping values with damping-ratio thresholds;
  it now gives the ratio formula and a worked value. The "Apple Spring
  stiffness 300 / damping 20" row was removed: Apple publishes no such default.
- **Platform currency:** SwiftUI's default animation has been a non-bouncing
  spring since iOS 17 (Apple's `Animation.default` documentation, WWDC23 "Animate
  with springs"); Material 3 Expressive adds spring tokens beside its easing and
  duration tokens (community documentation; confirm on m3.material.io before
  quoting values). CSS scroll-driven animations became Baseline when Firefox 159
  enabled them (web.dev, "New to the web platform in October", 2026-10-29).
  Framer Motion is now published as Motion; the description names both.
- **Internal consistency:** the main file required total stagger under 500ms
  while listing a 600ms dramatic budget; the rule now states the exception and
  its reason in the main file, the timing table and the checklist. The
  industry-curve and material tables were removed from `SKILL.md`, so the timing
  reference is their one owner. Context adaptation names WCAG 2.2.2, 2.3.1 and
  2.3.3 and the 120Hz frame budget. The description was reworded to drop
  "emotionally-driven", add springs and reduced motion, and use current library
  names.
