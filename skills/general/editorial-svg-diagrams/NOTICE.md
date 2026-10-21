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
