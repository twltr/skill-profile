#!/usr/bin/env python3
"""Portable SVG preflight for accessible standalone vector diagrams.

This is a structural/geometry sanity check, not a visual collision detector and
not a complete security sanitizer for attacker-controlled files.
"""
from __future__ import annotations

import argparse
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SVG_NS = 'http://www.w3.org/2000/svg'
TAG_PREFIX = '{' + SVG_NS + '}'
URL_RE = re.compile(r'url\(\s*[\'\"]?([^\)\'\"]+)', re.I)
PROHIBITED = {'script', 'foreignObject', 'animate', 'animateMotion', 'animateTransform', 'set'}


def local(tag: str) -> str:
    return tag.rsplit('}', 1)[-1]


def number(value, fallback=None):
    try:
        return float(str(value).strip().removesuffix('px'))
    except (TypeError, ValueError):
        return fallback


def check_svg(path: Path):
    errors, warnings = [], []
    try:
        tree = ET.parse(path)
    except (OSError, ET.ParseError) as exc:
        return [f'Cannot parse SVG: {exc}'], warnings
    root = tree.getroot()
    if root.tag != TAG_PREFIX + 'svg':
        errors.append('Root element must be namespaced SVG with xmlns="http://www.w3.org/2000/svg".')
        return errors, warnings

    raw = root.attrib.get('viewBox')
    try:
        values = [float(v) for v in re.split(r'[\s,]+', raw.strip())]
        if (len(values) != 4 or not all(math.isfinite(v) for v in values)
                or values[2] <= 0 or values[3] <= 0):
            raise ValueError('viewBox must contain four finite numbers, with positive width and height')
        min_x, min_y, width, height = values
    except (AttributeError, ValueError) as exc:
        errors.append(f'Invalid/missing viewBox: {exc}')
        min_x = min_y = width = height = 0

    if root.attrib.get('role') != 'img':
        errors.append('Missing role="img" on the SVG root.')
    children = list(root)
    if not children or children[0].tag != TAG_PREFIX + 'title':
        errors.append('The first child of SVG should be <title>.')
    title = next((el for el in children if local(el.tag) == 'title'), None)
    desc = next((el for el in children if local(el.tag) == 'desc'), None)
    if title is None or not ''.join(title.itertext()).strip():
        errors.append('Provide a meaningful nonempty <title>.')
    if desc is None or not ''.join(desc.itertext()).strip():
        errors.append('Provide a meaningful nonempty <desc>.')

    seen_ids = set()
    refs = []
    items = list(root.iter())
    for el in items:
        tag = local(el.tag)
        if tag in PROHIBITED:
            errors.append(f'Nonportable or unsafe element not allowed: <{tag}>.')
        if tag in {'image', 'iframe'}:
            errors.append(f'External/image element not allowed in pure vector SVG: <{tag}>.')
        ident = el.attrib.get('id')
        if ident:
            if ident in seen_ids:
                errors.append(f'Duplicate id: {ident}')
            seen_ids.add(ident)
        for key, value in el.attrib.items():
            attr = local(key)
            if attr.lower().startswith('on'):
                errors.append(f'Script event attribute not allowed in <{tag}>: {attr}.')
            if attr in ('href', 'src'):
                if not value.startswith('#'):
                    errors.append(f'Nonlocal resource reference in <{tag}>: {value[:70]}')
                else:
                    refs.append(value[1:])
            for match in URL_RE.finditer(value):
                target = match.group(1).strip()
                if target.startswith('#'):
                    refs.append(target[1:])
                else:
                    errors.append(f'External url() resource in <{tag}>: {target[:70]}')
        if tag == 'style' and el.text:
            if '@import' in el.text.lower():
                errors.append('External CSS imports are not portable.')
            for match in URL_RE.finditer(el.text):
                if not match.group(1).strip().startswith('#'):
                    errors.append('External CSS url() is not portable.')
        if tag == 'text':
            fs = number(el.attrib.get('font-size'))
            if fs is not None and fs < 13:
                warnings.append('Text smaller than 13 SVG units; test print-size legibility.')
        if width > 0 and height > 0 and tag in {'rect', 'circle', 'line'}:
            # Simple first-order bound checks (paths, text outlines and markers need visual review).
            if tag == 'rect':
                x, y = number(el.get('x'), 0), number(el.get('y'), 0)
                w, h = number(el.get('width'), 0), number(el.get('height'), 0)
                bounds = (x, y, x+w, y+h)
            elif tag == 'circle':
                cx, cy, r = number(el.get('cx'), 0), number(el.get('cy'), 0), number(el.get('r'), 0)
                bounds = (cx-r, cy-r, cx+r, cy+r)
            else:
                coords = [number(el.get(k), 0) for k in ('x1','y1','x2','y2')]
                bounds = (min(coords[0], coords[2]), min(coords[1], coords[3]),
                          max(coords[0], coords[2]), max(coords[1], coords[3]))
            if bounds[0] < min_x - .1 or bounds[1] < min_y - .1 or bounds[2] > min_x+width+.1 or bounds[3] > min_y+height+.1:
                warnings.append(f'<{tag}> geometry extends beyond the viewBox (needs review).')

    aria_ids = root.attrib.get('aria-labelledby', '').split()
    if not aria_ids:
        errors.append('Missing aria-labelledby referencing both <title> and <desc> IDs.')
    else:
        if title is not None and title.get('id') not in aria_ids:
            errors.append('aria-labelledby must reference the <title> ID.')
        if desc is not None and desc.get('id') not in aria_ids:
            errors.append('aria-labelledby must reference the <desc> ID.')
    for ident in aria_ids + refs:
        if ident not in seen_ids:
            errors.append(f'Reference to nonexistent in-document id: {ident}')
    return errors, list(dict.fromkeys(warnings))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('svgs', nargs='+', type=Path, help='Input SVG files')
    ap.add_argument('--strict', action='store_true', help='Treat warnings as failures')
    args = ap.parse_args()
    failed = False
    for path in args.svgs:
        errors, warnings = check_svg(path)
        print(f'{path}: {"FAILED" if errors or (args.strict and warnings) else "OK"}')
        for error in errors:
            print('  ERROR:', error)
        for warning in warnings:
            print('  WARN: ', warning)
        failed |= bool(errors or (args.strict and warnings))
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
