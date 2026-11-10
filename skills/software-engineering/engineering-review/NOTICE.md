# Source influences

This repository-owned review method implements the owner's requirements: independent
authorship, separate implementation/documentation reviews, actual rendered UI,
questions to the implementer and visible PR/issue dispositions.

Theo's published Council, File PR and Leaving PR Comments were inspected at
`1085050f3baed1ac724caa4a8166145fb2ac88af` on 2026-11-04:

- https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/skills/council/SKILL.md
- https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/skills/file-pr/SKILL.md
- https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/skills/leaving-pr-comments/SKILL.md

The local method draws on independent feedback and checking corrected revisions.
It does not import a fixed three-provider council, numerical acceptance threshold,
unanimity requirement, forced public attribution format or automatic merge.
The included [MIT notice](LICENSE-Theo.txt) preserves upstream attribution for
adapted material without assigning a license to other repository-owned material.

The Codex-bundled Review Agent was inspected locally on 2026-11-04. Its change-scope,
merge-base and actionable-finding criteria informed the independently written
guidance here. No host-managed skill package is vendored. Engineering Review keeps
its broader independent UI/documentation review and traceable correction workflow;
the native host configuration owns whether the redundant bundled entry is enabled.

Anthropic's `code-review` (1.0.1) and `pr-review-toolkit` (1.0.1) plugins from
the official Claude Code plugin marketplace, both Apache-2.0, were inspected on
2026-11-10. Their ideas informed independently written guidance here: try to
refute each candidate before reporting it, rule out common false positives
(pre-existing issues, deliberately silenced warnings, what linters already
catch), quote and scope a guideline before citing it, keep confidence separate
from severity, give failure paths and silent fallbacks their own pass, post one
comment per issue, offer a ready-to-apply suggestion only when it fully fixes the
issue, and link code at a full commit hash. No text from those plugins is copied,
so their license file is not included. Not adopted: their fixed agent roster and
model assignments, the 0-100 confidence score with a reporting threshold, the
restriction to guideline-file and obvious-bug issues, a "strengths" section and
automatic simplification after review.
