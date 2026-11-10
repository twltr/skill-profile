# Source and local adaptation

Based on Anthropic's Frontend Design skill at
`2235be7c60b551f5de82ade908fd3816455afcda`:
https://github.com/anthropics/skills/tree/2235be7c60b551f5de82ade908fd3816455afcda/skills/frontend-design

The supplied Apache-2.0 license remains in [LICENSE.txt](LICENSE.txt).
On 2026-11-04 the local method replaced invented client history with the actual
brief and added a small fictional brief-to-design example. The original visual
design guidance remains, with local conditional method boundaries. This is an
adaptation, not a byte-preserved copy or evidence of a rendered model trial.

## 2026-11-10 comparison with the current official copy

Compared with Anthropic's `frontend-design` plugin 1.1.1 in
`anthropics/claude-plugins-official` (marketplace snapshot
`dceb15d50832e6adf380bedc26dde03d251324b9`; `SKILL.md` SHA-256
`d91970639e9f5c37682ac7ab60094d35f1c7c1f38d731bd56396563aee10c1d3`), also
Apache-2.0. Its `LICENSE.txt` is byte-identical to ours, so no license change
was needed.

Adopted from the official copy:

- typography: one or two clearly distinct families, a scale in the tradition of
  *The Elements of Typographic Style*, line length under about 80 characters and
  more line-height for serif body text;
- the three typographic tells to avoid (single-word headline accent, all-caps
  labels, unnecessary labels);
- the calibration list extended from three to five defaults (the #D97757 accent,
  the SaaS card kit, template chrome);
- motion guidance: unprompted motion only to draw attention, responsive motion
  welcome when it shows what changed;
- the plan's fourth field as "principles" instead of a mandatory signature
  element, and alignment as part of the layout;
- the quality floor's contrast and palette harmony, and the toy-versus-dashboard
  contrast for grounding in the subject.

Kept from our adaptation: the actual-brief opening instead of the "client who
rejected proposals" persona, "match complexity to the vision", the rendered-state
check and the Puppeteer delegation hint (clarified as the core skill, not the
browser library). Dropped: "do the planning in your thinking", which contradicts
saying what the review changed, and "not taking a risk can be a risk", which the
official copy also retired. The worked example now shows the plan, the review
catching a default and the revision. The writing section is condensed and states
its boundary to dedicated microcopy work. The description was reworded to say
what the method produces.
