#!/usr/bin/env python3
"""Render a transparent SVG on two explicit background surfaces for visual QA.

Provide an explicit dark variant for accurate dark-theme contrast; do not infer
an external SVG inherits the host app's theme.
"""
from __future__ import annotations
import argparse
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import cairosvg


def render(path:Path, width:int):
    png=cairosvg.svg2png(url=str(path),output_width=width)
    return Image.open(BytesIO(png)).convert('RGBA')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('svg',type=Path)
    p.add_argument('--dark',type=Path,help='explicit palette dark variant (e.g. figure.dark.svg)')
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--width',type=int,default=850)
    args=p.parse_args()
    dark=args.dark
    if dark is None:
        candidate=args.svg.with_name(args.svg.stem+'.dark.svg')
        if candidate.exists():dark=candidate
    if dark is None: raise SystemExit('Provide a --dark variant to verify actual dark contrast.')
    rendered=[render(args.svg,args.width),render(dark,args.width)]
    w=args.width
    h=max(im.height for im in rendered)
    if h<10: raise SystemExit('Malformed/empty SVG preview')
    gap=20; pad=25;top=58
    canvas=Image.new('RGB',(w*2+2*pad+gap,h+top+pad),'#28303A')
    d=ImageDraw.Draw(canvas)
    fonts=['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf','/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf']
    try: font=ImageFont.truetype(next(p for p in fonts if Path(p).exists()),21)
    except StopIteration: font=ImageFont.load_default()
    for idx,(im,bg,label) in enumerate(zip(rendered,['#FFFFFF','#111316'],['Light surface','Dark surface'])):
        x=pad+idx*(w+gap)
        d.text((x,18),label,fill='white',font=font)
        paper=Image.new('RGBA',(w,h),bg)
        paper.alpha_composite(im,(0,(h-im.height)//2))
        canvas.paste(paper.convert('RGB'),(x,top))
    args.out.parent.mkdir(parents=True,exist_ok=True)
    canvas.save(args.out)
    print('wrote:',args.out)

if __name__=='__main__': main()
