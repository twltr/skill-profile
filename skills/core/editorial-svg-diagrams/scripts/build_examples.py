#!/usr/bin/env python3
"""Build small explanation-first SVG figures with transparent canvases.

Every default SVG is transparent with a CSS prefers-color-scheme variant.
Each *.dark.svg is a deterministic explicit-dark fallback for fixed destinations.
Edit semantic drawing functions here; do not retouch the exported SVG in a raster editor.
"""
from __future__ import annotations
from html import escape
from pathlib import Path
import argparse

HERE = Path(__file__).resolve().parent.parent
ASSETS = HERE / 'assets'

LIGHT = {
    'ink':'#1C2936','muted':'#5A6672','guide':'#B2BDC7','border':'#BCC6CF',
    'blue':'#3979A5','teal':'#137B77','green':'#397654','ochre':'#95622F',
    'brown':'#8B6058','bluewash':'#E9F1F8','tealwash':'#E6F5F2',
    'greenwash':'#EAF4ED','neutralwash':'#F2F5F7','soft':'#778590',
    'whitetxt':'#FFFFFF',
}
DARK = {
    'ink':'#F1F4F6','muted':'#B2BAC1','guide':'#49545C','border':'#444B50',
    'blue':'#3979A5','teal':'#137D77','green':'#397654','ochre':'#95622F',
    'brown':'#8B6058','bluewash':'#14232E','tealwash':'#102825',
    'greenwash':'#14271C','neutralwash':'#171C20','soft':'#808990',
    'whitetxt':'#FFFFFF',
}
STROKES = {'ink','muted','guide','border','blue','teal','green','ochre','brown','soft'}


def colors_css(palette: dict, *, ind: int = 0) -> str:
    pad=' '*ind
    parts=[]
    for key,color in palette.items():
        parts.append(f'{pad}.f-{key} {{ fill: {color}; }}')
        if key in STROKES:
            parts.append(f'{pad}.s-{key} {{ stroke: {color}; }}')
    return '\n'.join(parts)


def svg_wrap(slug: str, width: int, height: int, body: str, title: str, desc: str, *, dark=False) -> str:
    light_or_dark = DARK if dark else LIGHT
    style = colors_css(light_or_dark)
    if not dark:
        style += '\n@media (prefers-color-scheme: dark) {\n'+colors_css(DARK, ind=2)+'\n}'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{slug}-title {slug}-desc">
<title id="{slug}-title">{escape(title)}</title>
<desc id="{slug}-desc">{escape(desc)}</desc>
<style><![CDATA[
  text {{ font-family: Arial, Helvetica, sans-serif; }}
  .label {{ font-size: 21px; font-weight: 600; }}
  .small {{ font-size: 16px; font-weight: 500; }}
  .tiny {{ font-size: 14px; font-weight: 500; }}
  .mono {{ font-family: Menlo, Consolas, monospace; }}
{style}
]]></style>
<defs>
  <marker id="{slug}-blue-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto" markerUnits="userSpaceOnUse"><path d="M1 1 L9 5 L1 9" fill="none" class="s-blue" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></marker>
  <marker id="{slug}-teal-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto" markerUnits="userSpaceOnUse"><path d="M1 1 L9 5 L1 9" fill="none" class="s-teal" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></marker>
</defs>
{body}
</svg>
'''


def text(x, y, label, cls='f-ink label', anchor='start', extra=''):
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}" {extra}>{escape(str(label))}</text>'


def rect(x,y,w,h,r,cls='f-neutralwash',extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" class="{cls}" {extra}/>'


def line(x1,y1,x2,y2,cls='s-guide',width=2,dash=''):
    return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" class="{cls}" stroke-width="{width}" stroke-linecap="round" {"stroke-dasharray="+chr(34)+dash+chr(34) if dash else ""}/>'


def path(d,cls='s-blue',width=3,marker='',dash=''):
    return f'<path d="{d}" fill="none" class="{cls}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round" {"marker-end="+chr(34)+"url(#"+marker+")"+chr(34) if marker else ""} {"stroke-dasharray="+chr(34)+dash+chr(34) if dash else ""}/>'


def tcp():
    slug='tcp'
    b=[]
    b += [text(146,32,'Client', 'f-ink label', 'middle'),text(650,32,'Server','f-ink label','middle')]
    b += [line(146,56,146,357,'s-guide',2.3,'7 10'),line(650,56,650,357,'s-guide',2.3,'7 10')]
    b += [rect(89,59,114,44,10,'f-blue'),text(146,88,'connect()','f-whitetxt small','middle')]
    for d,c,lab,x,y,mid in [
        ('M146 118 L650 163','s-blue','SYN',380,124,'tcp-blue-arrow'),
        ('M650 190 L146 235','s-teal','SYN-ACK',390,185,'tcp-teal-arrow'),
        ('M146 270 L650 315','s-blue','ACK',390,265,'tcp-blue-arrow')]:
        b.append(path(d,c,3.8,mid))
        b.append(text(x,y,lab,'f-ink label','middle'))
    b += [rect(587,336,126,43,10,'f-teal'), text(650,363,'accept()','f-whitetxt small','middle')]
    # There is no subtitle, prose caption, or background in the artboard.
    return 800,398,'\n'.join(b),'Three-way TCP handshake','Client sends SYN, server responds SYN-ACK, client confirms ACK; server accepts the established connection.'


def encapsulation():
    b=[]
    x=154; W=656; h=43
    rows=[('Anwendung',36,[('Hallo',W,'f-blue')]),
          ('TCP',121,[('Header',232,'f-teal'),('Hallo',W-232,'f-blue')]),
          ('IP',206,[('IP-Header',187,'f-green'),('TCP + Hallo',W-187,'f-teal')]),
          ('Ethernet',291,[('Ethernet',161,'f-ochre'),('IP + TCP + Hallo',W-246,'f-green'),('FCS',85,'f-brown')])]
    for index,(label,y,blocks) in enumerate(rows):
        b.append(text(8,y+29,label,'f-ink small'))
        cur=x
        for j,(caption,width,color) in enumerate(blocks):
            radius=7 if len(blocks)==1 else 0
            b.append(rect(cur,y,width,h,radius,color))
            b.append(text(cur+width/2,y+28,caption,'f-whitetxt small','middle'))
            cur+=width
        # stroke separators, not a huge surrounding wrapper
        for k,(caption,width,color) in enumerate(blocks[:-1]):
            xx=x+sum(v[1] for v in blocks[:k+1]); b.append(line(xx,y+4,xx,y+h-4,'s-border',1.0))
        if index<3:
            y2=y+h+23
            b.append(line(x+W/2,y+h+9,x+W/2,y2-1,'s-muted',2))
            b.append(path(f'M{x+W/2-5} {y2-7} L{x+W/2} {y2} L{x+W/2+5} {y2-7}', 's-muted',1.8))
    return 834,351,'\n'.join(b),'Packet encapsulation','Hallo application bytes are wrapped in TCP, IP and Ethernet headers; Ethernet also adds FCS.'


def entropy():
    b=[]
    start=12; cw=83; gap=10; bw=83; hi=77
    b.append(text(12,29,'Known position','f-ink small'))
    for i in range(8):
        x=start+i*(cw+gap)
        if i==2:
            b.append(rect(x,53,cw,hi,11,'f-tealwash'))
            b.append(f'<rect x="{x}" y="53" width="{cw}" height="{hi}" rx="11" fill="none" class="s-teal" stroke-width="2.5"/>')
            b.append(f'<circle cx="{x+cw/2}" cy="{53+hi/2}" r="15" class="f-teal"/>')
        else:
            b.append(f'<rect x="{x}" y="53" width="{cw}" height="{hi}" rx="11" fill="none" class="s-border" stroke-width="2"/>')
    b.append(text(383,163,'1 position   ·   0 bits','f-ink label','middle'))
    b.append(line(12,194,751,194,'s-border',1))
    b.append(text(12,232,'Unknown position','f-ink small'))
    for i in range(8):
        x=start+i*(cw+gap)
        b.append(rect(x,256,cw,hi,11,'f-tealwash'))
        b.append(f'<rect x="{x}" y="256" width="{cw}" height="{hi}" rx="11" fill="none" class="s-teal" stroke-width="2.5"/>')
        b.append(f'<circle cx="{x+cw/2}" cy="{256+hi/2}" r="13" class="f-teal" fill-opacity="0.65"/>')
    b.append(text(383,372,'8 positions   ·   3 bits','f-ink label','middle'))
    return 767,390,'\n'.join(b),'Knowledge and uncertainty','One highlighted known particle position has zero uncertainty; eight equally likely possible positions require three bits to specify one. Dots in bottom row denote alternatives, not eight particles.'


def monitor(x,y,col):
    return '\n'.join([
        f'<rect x="{x}" y="{y}" width="70" height="47" rx="6" fill="none" class="s-{col}" stroke-width="3"/>',
        line(x+35,y+47,x+35,y+57,'s-'+col,3),line(x+19,y+57,x+51,y+57,'s-'+col,3)
    ])


def endpoints():
    b=[]
    # modest icon panels are appropriate here: they represent physical endpoint objects
    for x,col,name,ip,port in [(16,'teal','PC X','192.168.1.10','8080'),(556,'blue','PC Y','192.168.1.20','53124')]:
        b.append(rect(x,22,194,220,16,'f-tealwash' if col=='teal' else 'f-bluewash'))
        b.append(f'<rect x="{x}" y="22" width="194" height="220" rx="16" fill="none" class="s-{col}" stroke-width="2.5"/>')
        b.append(monitor(x+62,47,col))
        b.append(text(x+97,139,name,'f-ink label','middle'))
        b.append(text(x+97,174,ip,'f-muted small mono','middle'))
        b.append(text(x+97,203,'Port '+port,'f-muted small','middle'))
    b.append(path('M556 100 H219','s-teal',3.6,'endpoint-teal-arrow'))
    b.append(text(384,87,'connect','f-ink small','middle'))
    b.append(path('M219 170 H556','s-blue',3,'endpoint-blue-arrow','6 7'))
    b.append(text(384,160,'Response','f-ink small','middle'))
    return 768,262,'\n'.join(b),'Two computers communicating via TCP','PC Y at 192.168.1.20:53124 connects to server PC X at 192.168.1.10:8080 and receives a reply.'


def layers():
    rows=[('7','Application','HTTP','blue'),('6','Presentation','Encoding','blue'),('5','Session','Session','blue'),('4','Transport','TCP / UDP','teal'),('3','Network','IP','green'),('2','Data Link','Ethernet','ochre'),('1','Physical','Signals','brown')]
    b=[]
    for i,(idx,name,proto,col) in enumerate(rows):
        yy=i*53+6
        b.append(rect(14,yy,566,45,8,'f-'+col))
        b.append(text(44,yy+30,idx,'f-whitetxt label'))
        b.append(text(90,yy+29,name,'f-whitetxt small'))
        b.append(text(548,yy+29,proto,'f-whitetxt small','end'))
    return 595,383,'\n'.join(b),'OSI layer stack','Seven OSI layers arranged top to bottom with simple example protocols or responsibilities.'


def architecture():
    b=[]
    # One meaningful data path, no prose or corner label noise.
    for x,name,color in [(25,'Client','blue'),(296,'API','teal'),(568,'Database','green')]:
        b.append(rect(x,74,193,115,12,'f-'+('bluewash' if color=='blue' else 'tealwash' if color=='teal' else 'greenwash')))
        b.append(f'<rect x="{x}" y="74" width="193" height="115" rx="12" fill="none" class="s-{color}" stroke-width="2.5"/>')
        b.append(text(x+96,130,name,'f-ink label','middle'))
    b.append(path('M218 131 H294','s-blue',3.5,'arch-blue-arrow'))
    b.append(path('M489 131 H566','s-teal',3.5,'arch-teal-arrow'))
    b.append(text(256,115,'HTTP','f-muted tiny','middle'))
    b.append(text(527,115,'SQL','f-muted tiny','middle'))
    return 787,221,'\n'.join(b),'Simple client API database architecture','Client uses HTTP to talk with an API; the API uses SQL with a database. This figure is fictional and illustrative.'


def starter():
    b=[rect(14,57,205,99,12,'f-bluewash'),rect(446,57,205,99,12,'f-tealwash')]
    b.append('<rect x="14" y="57" width="205" height="99" rx="12" fill="none" class="s-blue" stroke-width="2.4"/>')
    b.append('<rect x="446" y="57" width="205" height="99" rx="12" fill="none" class="s-teal" stroke-width="2.4"/>')
    b.append(text(116,113,'Sender','f-ink label','middle'))
    b.append(text(548,113,'Receiver','f-ink label','middle'))
    b.append(path('M219 106 H445','s-blue',3.5,'starter-blue-arrow'))
    return 665,213,'\n'.join(b),'Minimal two-node figure','A sender points to a receiver. Minimal labels, transparent background, no title inside the visible diagram.'


def outline(x,y,w,h,r,col,width=2.4):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="none" class="s-{col}" stroke-width="{width}"/>'


def time_budget():
    # Parts of a whole: segment widths are the data, the rows only name them.
    parts=[('Network',0.9,'blue'),('Render',0.6,'teal'),('Script',0.3,'ochre')]
    total=sum(v for _,v,_ in parts); x0=12; W=616
    b=[text(x0,34,'Page load','f-muted small'),
       text(x0+W,36,f'{total:.1f} s','f-ink label','end','style="font-size:30px;font-weight:700"')]
    cur=x0
    for i,(name,value,col) in enumerate(parts):
        w=W*value/total
        b.append(rect(round(cur,1),54,round(w-3,1),30,6,'f-'+col))
        cur+=w
        y=126+i*38
        b.append(rect(x0,y-14,14,14,3,'f-'+col))
        b.append(text(x0+26,y,name,'f-ink label'))
        b.append(text(x0+W,y,f'{value:.1f} s','f-ink label','end'))
    return 640,216,'\n'.join(b),'Where page load time goes','Page load of 1.8 seconds split proportionally: network 0.9 s, render 0.6 s, script 0.3 s. Values are illustrative.'


def login_routes():
    # Two parallel routes that end in one shared node; only the middle step differs.
    b=[]
    for cx,col,head,start,check,store in [
        (160,'blue','Password','Typed secret','Hash compare','server keeps a hash'),
        (480,'teal','Passkey','Device key','Signature check','server keeps a public key')]:
        x=cx-120
        b.append(text(cx,26,head,'f-ink label','middle'))
        b.append(rect(x,44,240,52,10,'f-neutralwash')); b.append(outline(x,44,240,52,10,'border',2))
        b.append(text(cx,77,start,'f-ink small','middle'))
        b.append(path(f'M{cx} 100 V122','s-'+col,3,f'loginroutes-{col}-arrow'))
        b.append(rect(x,126,240,68,10,'f-'+col+'wash')); b.append(outline(x,126,240,68,10,col))
        b.append(text(cx,156,check,'f-ink label','middle'))
        b.append(text(cx,180,store,'f-muted tiny','middle'))
        b.append(path(f'M{cx} 198 V236','s-'+col,3,f'loginroutes-{col}-arrow'))
    b.append(rect(40,240,560,52,10,'f-greenwash')); b.append(outline(40,240,560,52,10,'green'))
    b.append(text(320,273,'Session','f-ink label','middle'))
    return 640,304,'\n'.join(b),'Password and passkey login','Two parallel routes reach the same session. Password: typed secret, hash compare against a stored hash. Passkey: device key, signature check against a stored public key.'


def base64_roundtrip():
    # The same data in three notations; literal sample values sit inside the nodes.
    b=[]
    nodes=[(12,'Hi!','Text','border','neutralwash'),(290,'48 69 21','3 bytes','blue','bluewash'),(568,'SGkh','4 characters','teal','tealwash')]
    for x,value,role,col,wash in nodes:
        b.append(rect(x,24,180,64,10,'f-'+wash)); b.append(outline(x,24,180,64,10,col,2.2))
        b.append(text(x+90,64,value,'f-ink label mono','middle'))
        b.append(text(x+90,114,role,'f-muted small','middle'))
    for x1,x2,lab in [(196,286,'UTF-8'),(474,564,'Base64')]:
        b.append(text((x1+x2)/2,34,lab,'f-muted tiny','middle'))
        b.append(path(f'M{x1} 48 H{x2}','s-blue',3,'base64roundtrip-blue-arrow'))
        b.append(path(f'M{x2} 68 H{x1}','s-teal',3,'base64roundtrip-teal-arrow'))
    return 760,126,'\n'.join(b),'Base64 round trip','The text Hi! is the three bytes 48 69 21 in UTF-8 and the four characters SGkh in Base64; each step is reversible.'


def quadrant_glyphs():
    # Specimen grid: show the things themselves, each with its code.
    codes=['1000','0100','0010','0001','1001','0110','1110','1111']
    b=[]
    for i,code in enumerate(codes):
        tx=12+(i%4)*142; ty=10+(i//4)*130
        b.append(outline(tx,ty,130,118,10,'border',2))
        gx=tx+45; gy=ty+16
        for k,bit in enumerate(code):
            if bit=='1': b.append(rect(gx+(k%2)*20,gy+(k//2)*30,20,30,0,'f-teal'))
        b.append(outline(gx,gy,40,60,0,'guide',1.4))
        b.append(text(tx+65,ty+102,code,'f-ink small mono','middle'))
    return 580,268,'\n'.join(b),'Quadrant block characters as four bits','Eight of the sixteen quadrant patterns of one character cell. The four bits name the top-left, top-right, bottom-left and bottom-right quadrant.'


def backoff_formula():
    # An annotated formula above its behaviour. Every term is its own centred
    # <text>, so the brackets stay aligned whichever fallback font renders it.
    big='style="font-size:30px;font-weight:600"'
    b=[]
    for cx,term,col in [(70,'delay','ink'),(140,'=','ink'),(200,'min(','ink'),(275,'cap','ochre'),(318,',','ink'),(385,'base','blue'),(455,'×','ink'),(560,')','ink')]:
        b.append(text(cx,42,term,f'f-{col} mono','middle',big))
    b.append(f'<text x="515" y="42" class="f-teal mono" text-anchor="middle" {big}>2<tspan dy="-13" style="font-size:20px">n</tspan></text>')
    for x1,x2,lab,col in [(246,304,'ceiling','ochre'),(347,423,'first wait','blue'),(494,536,'doubles per retry','teal')]:
        b.append(path(f'M{x1} 56 V64 H{x2} V56','s-'+col,2))
        b.append(text((x1+x2)/2,86,lab,'f-ink tiny','middle'))
    # base = 1 s, cap = 30 s: 1, 2, 4, 8, 16, then held at the ceiling.
    base_y=206; scale=2.6
    b.append(line(96,base_y-30*scale,512,base_y-30*scale,'s-ochre',1.8,'5 7'))
    b.append(text(522,base_y-30*scale+5,'cap','f-ink tiny'))
    b.append(text(84,base_y+24,'n','f-muted tiny mono','end'))
    for n in range(7):
        raw=2**n; value=min(30,raw); x=104+n*58; h=round(value*scale,1)
        b.append(rect(x,round(base_y-h,1),36,h,3,'f-ochre' if raw>30 else 'f-teal'))
        b.append(text(x+18,base_y+24,n,'f-muted tiny mono','middle'))
    return 600,238,'\n'.join(b),'Capped exponential backoff','delay = min(cap, base times 2 to the power n). The wait doubles with every retry n until it reaches the ceiling cap; shown for base 1 second and cap 30 seconds.'


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,default=ASSETS)
    args=ap.parse_args()
    dest=args.out.resolve(); dest.mkdir(parents=True,exist_ok=True)
    figures={
        'tcp-handshake':tcp,
        'packet-encapsulation':encapsulation,
        'entropy-possibilities':entropy,
        'pc-connection':endpoints,
        'osi-layers':layers,
        'codebase-architecture':architecture,
        'starter':starter,
        'time-budget':time_budget,
        'login-routes':login_routes,
        'base64-roundtrip':base64_roundtrip,
        'quadrant-glyphs':quadrant_glyphs,
        'backoff-formula':backoff_formula,
    }
    for name,fn in figures.items():
        w,h,body,title,description=fn()
        for dark in [False,True]:
            slug={'tcp-handshake':'tcp','pc-connection':'endpoint','codebase-architecture':'arch','starter':'starter'}.get(name,name.replace('-',''))
            suffix='.dark.svg' if dark else '.svg'
            path=dest/(name+suffix)
            path.write_text(svg_wrap(slug,w,h,body,title,description,dark=dark),encoding='utf-8')
            print('wrote',path.name)


if __name__=='__main__':
    main()
