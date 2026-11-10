#!/usr/bin/env python3
"""Explainer-oriented SVG lint: catch fixed background and text-as-image regressions.

Not a typography/layout oracle. Complements preflight_svg.py and visual inspection.
"""
from __future__ import annotations
import argparse
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def local(tag): return tag.rsplit('}',1)[-1]

def numeric(s):
    if s is None: return None
    try: return float(re.sub(r'px$','',s.strip()))
    except ValueError: return None


def check(path, *, max_words=35, max_labels=24, allow_background=False):
    tree=ET.parse(path)
    root=tree.getroot()
    viewbox=root.attrib.get('viewBox', '').replace(',',' ').split()
    errors=[]; warnings=[]
    if len(viewbox)==4:
        try: vx,vy,vw,vh=map(float,viewbox)
        except ValueError: vx=vy=vw=vh=0
    else: vx=vy=vw=vh=0
    text_nodes=[]
    for n in root.iter():
        tag=local(n.tag)
        if tag=='text':
            txt=' '.join(' '.join(n.itertext()).split())
            if txt: text_nodes.append(txt)
        if tag !='rect' or not vw or not vh: continue
        x=numeric(n.get('x')) or 0
        y=numeric(n.get('y')) or 0
        w=numeric(n.get('width'))
        h=numeric(n.get('height'))
        # Empty attrs and percentage backgrounds both count.
        matches=(w is not None and w>=vw*.98 and h is not None and h>=vh*.98 and x<=vx+vw*.02 and y<=vy+vh*.02)
        percent_matches=n.get('width')=='100%' and n.get('height')=='100%'
        fill=n.get('fill')
        classes=n.get('class','')
        has_fill = fill not in ('none','transparent') or ('f-' in classes and fill is None)
        if (matches or percent_matches) and has_fill:
            if allow_background:
                warnings.append('Full-canvas background present (explicitly allowed).')
            else:
                errors.append('Full-canvas rect detected: default explanation figures must be transparent.')
    wc=sum(len(s.split()) for s in text_nodes)
    if wc>max_words: warnings.append(f'{wc} visible words, target <= {max_words}; remove prose from artwork.')
    if len(text_nodes)>max_labels: warnings.append(f'{len(text_nodes)} visible labels, target <= {max_labels}; split or simplify.')
    for s in text_nodes:
        if len(s)>80: warnings.append(f'Paragraph-like SVG label: {s[:90]!r}')
    return errors,warnings, len(text_nodes), wc


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('paths',type=Path,nargs='+')
    p.add_argument('--strict',action='store_true',help='also fail warnings')
    p.add_argument('--allow-background',action='store_true')
    p.add_argument('--max-words',type=int,default=35)
    p.add_argument('--max-labels',type=int,default=24)
    a=p.parse_args(); rc=0
    for f in a.paths:
        try: errors,warnings,n,w=check(f,max_words=a.max_words,max_labels=a.max_labels,allow_background=a.allow_background)
        except (OSError,ET.ParseError) as exc:
            print(f'{f}: FAIL parse: {exc}'); rc=1;continue
        print(f'{f}: {"FAIL" if (errors or a.strict and warnings) else "OK"} ({n} labels, {w} words)')
        for e in errors: print('  ERROR:',e)
        for warn in warnings: print('  WARN:',warn)
        if errors or a.strict and warnings: rc=1
    return rc

if __name__=='__main__': sys.exit(main())
