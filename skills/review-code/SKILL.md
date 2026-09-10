---
name: review-code
description: Review a specified code change when the user requests a review or project rules require one. Check requirements, correctness and Engineering standards; ordinary self-checking after an edit does not start this full workflow.
---

# Review Code

Determine whether the selected change delivers the intended behavior and what
material risks remain, with findings the author can reproduce and act on.

Start this full review only for a review assignment or a binding project gate.
The normal verification of your own changes remains part of implementation.

## Fix the review boundary

Identify the requested repository, change and comparison base. Inspect actual
Git or review state: committed changes, staged edits and unstaged edits are
different inputs. Include the working tree when that is the request; do not
silently substitute a HEAD-only diff. Resolve the base and record the scope
before interpreting an empty diff as a clean change. Ask only when available
context cannot establish what the user wants reviewed.

Locate the originating requirements and applicable repository standards. Read
the relevant bodies and discussions through the available source interface.
If a source is missing, distinguish an unverifiable requirement from an absent
requirement; continue only the checks whose basis is known and state the limit.

## Review two questions, form one judgment

1. **Does it deliver the requested behavior?** Trace the changed paths through
   callers, state and outputs. Check omitted requirements, altered contracts,
   error handling and behavior added without a corresponding requirement.
2. **Is its construction safe to maintain and operate?** Check ownership,
   dependency direction, model truth, data/authority boundaries and the failure
   cases affected by the change. Treat design smells as hypotheses: an extra
   abstraction or similar code is not a defect without a concrete consequence.
   Apply the repository's actual conventions rather than importing a new
   architectural vocabulary.

Inspect the surrounding code and tests necessary to verify each candidate
finding. Follow dynamic entrypoints where relevant. Run targeted, authorized
checks when they settle a question; a lack of evidence is not itself proof
of a bug. Distinguish failures introduced here from pre-existing defects.
Verify any delegated claim yourself before it becomes a finding.

## Report what matters

For each finding, give the trigger, actual consequence, expected behavior or
standard, and the narrowest useful source location. Where feasible include a
reproduction or the check that demonstrated it. Separate confirmed defects
from open design questions and state uncertainty explicitly.

Combine both review perspectives into one prioritized result. Merge duplicates
and lead with the issues that could cause the greatest concrete harm. Do not
repeat formatting issues already handled by tooling or invent findings to fill
a quota. No findings means no confirmed findings within the stated scope, not
a guarantee about unexamined behavior.

Return findings, the checked scope, evidence and residual gaps. Stop at the
review result unless repair is part of the user's request; a review does not
authorize a commit, merge, publication or production action.

Adapted source methods are credited in [NOTICE.md](NOTICE.md).
