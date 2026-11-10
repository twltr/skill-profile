# Source and local adaptation

The ten files captured from the local installation before adaptation matched the public
[OpenData skill snapshot](https://github.com/tryopendata/skills/tree/f97583ecb7eeb8a0c2a193fe9b80e55806d29823/plugins/opendesign/skills/svg-design)
byte for byte at commit `f97583ecb7eeb8a0c2a193fe9b80e55806d29823`.
[source-manifest.json](source-manifest.json) records the original Git blob hashes.
The snapshot's [MIT license](LICENSE.txt), copyright 2026 OpenData, is preserved.
This identifies a matching source; the original installation route was not recovered.

On 2026-11-04, the local adaptation narrows the skill to logos, icons, brand assets
and visual graphics for websites and interfaces. Explanatory diagrams belong to
Editorial SVG Diagrams; full page composition belongs to Frontend Design. The
opening now starts from design intent. Icon canvas and stroke defaults apply to
icons rather than every SVG. Local cross-references replace the optional `ce`
plugin references, and native metadata supplies a descriptive UI label.

The eight technical references and preview asset are retained from the matched
snapshot. The editing-workflow reference also records the local preview-host
adaptation below. This import does not claim that the logo workflow or host
support passed a fresh model trial.

## 2026-11-04 workflow and example revision

Added a small logo-design example and replaced the mandatory `AskUserQuestion`
call with a brief-driven interaction using the current host's supported means.
The preview workflow now respects the available host instead of opening a
foreground window with a platform-specific command. Conditional cross-references
state the handoff and fallback. The editing-workflow reference is locally adapted;
the other technical references and preview asset retain the matched source.

The Skill Profile owns this complete local variant under `skills/design/svg-design/`.
Installed directories are deployment copies; future local changes belong here.

## 2026-11-10 quality pass

The cross-reference for surrounding page design no longer tells this leaf to use
a sibling skill; it hands that work back with the graphic's constraints, as a
leaf in the Design tree loads no other skill. The boundary sentences naming
Frontend Design and Editorial SVG Diagrams are unchanged.
