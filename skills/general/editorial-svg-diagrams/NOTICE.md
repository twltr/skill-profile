# Source and local adaptation

Imported from the `skill.zip` supplied by Tobi on 2026-10-21 as the replacement
for the former Diagram Design skill. The original package contains 14 files;
[source-manifest.json](source-manifest.json) records their SHA-256 hashes and
the archive hash. The original archive is retained in the local profile backup.

The supplied package contains no license or authorship declaration. No license
or third-party attribution is inferred or added. This import records the user's
authorized use in the personal profile and local agent installations; rights for
further redistribution are not established by this notice.

Review adaptations preserve the supplied diagram method and example artwork:

- Shortened discovery metadata and made automatic invocation explicit.
- Made this skill the complete diagram owner and resolved helper paths from
  the installed skill directory.
- Kept missing-renderer verification open and clarified backend selection.
- Rejected non-finite viewBox/export scale values and script event attributes.

The structural preflight remains a linter, not a hostile-input sanitizer or a
substitute for visual inspection.

## 2026-10-23 visual-first revision

Imported the user-supplied revised skill.zip and editorial-svg-testgrafiken.zip.
source-manifest-20261023.json records archive and original file hashes. The
three accepted test figures and their dark variants are included as explicit
regression references. The earlier source manifest remains historical evidence.

Local adaptations retain supported invocation metadata and the existing
finite-number / event-attribute validation fixes. Helper paths are resolved
from the skill directory. The light/dark foreground sentence was corrected
to use dark foreground on light surfaces and light foreground on dark surfaces.
Whitespace-only lines in the accepted SVG examples were normalized; their
geometry and text are unchanged. No additional license or redistribution rights
are inferred from this import.

## 2026-10-23 representation and geometry clarification

User feedback made per-figure representation choice and clean geometric
construction explicit: compare useful alternatives before drawing, align peer
elements and spacing, plan clear connector routes, and judge the rendered result
beyond structural lint. This changes the authoring method, not the imported
example artwork, provenance records or invocation policy.
