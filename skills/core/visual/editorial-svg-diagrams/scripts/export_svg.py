#!/usr/bin/env python3
"""Export validated self-contained SVG to PNG or PDF for documentation and print.

Prefer CairoSVG when installed; otherwise use Inkscape command line if present.
Preflight blocks common non-portable resources but is not a hostile-SVG sanitizer.
"""
from __future__ import annotations

import argparse
import math
import shutil
import subprocess
import sys
from pathlib import Path
from preflight_svg import check_svg


def size_of_svg(path: Path):
    import xml.etree.ElementTree as ET
    root = ET.parse(path).getroot()
    values = [float(x) for x in root.attrib['viewBox'].replace(',', ' ').split()]
    return values[2], values[3]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('svg', type=Path)
    ap.add_argument('--format', choices=['png', 'pdf'], default='png')
    ap.add_argument('--out', type=Path)
    ap.add_argument('--scale', type=float, default=2.0, help='PNG scale multiplier, default 2')
    ap.add_argument('--width', type=int, help='PNG output width in pixels (overrides scale)')
    args = ap.parse_args()
    if args.format == 'pdf' and args.width:
        ap.error('--width only applies to PNG')
    if not math.isfinite(args.scale) or args.scale <= 0 or (args.width is not None and args.width <= 0):
        ap.error('--scale must be finite and positive; --width must be positive')

    svg = args.svg.resolve()
    out = (args.out or svg.with_suffix('.' + args.format)).resolve()
    if svg == out:
        ap.error('Output cannot overwrite SVG source')
    errors, warnings = check_svg(svg)
    for message in warnings:
        print('WARN:', message, file=sys.stderr)
    if errors:
        print('SVG failed preflight:', *errors, sep='\n  ', file=sys.stderr)
        return 1

    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        import cairosvg
        opts = {'url': str(svg), 'write_to': str(out)}
        if args.format == 'png':
            if args.width:
                opts['output_width'] = args.width
            else:
                opts['scale'] = args.scale
            cairosvg.svg2png(**opts)
        else:
            cairosvg.svg2pdf(**opts)
        print('Exported with CairoSVG:', out)
        return 0
    except ImportError:
        pass
    except Exception as exc:
        print(f'CairoSVG export failed: {exc}', file=sys.stderr)
        return 1

    cli = shutil.which('inkscape')
    if cli:
        command = [cli, str(svg), '--export-filename=' + str(out), '--export-type=' + args.format]
        if args.format == 'png':
            w, _ = size_of_svg(svg)
            command.append('--export-width=' + str(args.width or int(round(w * args.scale))))
        result = subprocess.run(command, capture_output=True, text=True, timeout=120)
        if result.returncode:
            print('Inkscape export failed:', result.stderr, file=sys.stderr)
            return result.returncode
        print('Exported with Inkscape:', out)
        return 0

    print('Missing exporter. Install Python package cairosvg or Inkscape CLI.', file=sys.stderr)
    return 1


if __name__ == '__main__':
    sys.exit(main())
