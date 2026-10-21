#!/usr/bin/env python3
"""Rebuild the bundled editorial SVG examples using explicit geometric primitives.

This is intentionally straightforward Python -> SVG string generation so learners can
change coordinates and immediately observe the effect without an SVG framework.
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'assets'
PAPER = '#F7F9FC'
INK = '#172738'
MUTED = '#566779'
RULE = '#D5DFE7'
BLUE = '#356F9F'
TEAL = '#237C77'
GREEN = '#3E805C'
OCHRE = '#A67637'
BROWN = '#815B53'
FONT = 'Arial, Helvetica, sans-serif'
MONO = 'Consolas, Menlo, monospace'


def text(x, y, value, size=20, color=INK, weight=400, anchor='start', mono=False, opacity=None):
    opt = f' opacity="{opacity}"' if opacity is not None else ''
    family = MONO if mono else FONT
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" fill="{color}"{opt}>'
            f'{escape(str(value))}</text>')


def rect(x, y, w, h, fill, rx=0, stroke=None, sw=1.5, opacity=None):
    border = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    op = f' opacity="{opacity}"' if opacity is not None else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{border}{op}/>'


def line(x1, y1, x2, y2, color=RULE, width=2, dash=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="{width}"{ds} />')


def arrow_path(d, color=BLUE, marker='blue', width=3, dash=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="round" stroke-linejoin="round" marker-end="url(#{marker}-arrow)"{ds}/>' )


def svg_start(name, heading, description, w, h, dark=False):
    paper = '#111B27' if dark else PAPER
    defs = '''<defs>
      <marker id="blue-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
        <path d="M1 1 L9 5 L1 9Z" fill="#356F9F"/>
      </marker>
      <marker id="teal-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
        <path d="M1 1 L9 5 L1 9Z" fill="#237C77"/>
      </marker>
      <marker id="green-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
        <path d="M1 1 L9 5 L1 9Z" fill="#3E805C"/>
      </marker>
    </defs>'''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="{name}-title {name}-desc">\n'
            f'<title id="{name}-title">{escape(heading)}</title>\n'
            f'<desc id="{name}-desc">{escape(description)}</desc>\n'
            f'{defs}\n{rect(0, 0, w, h, paper)}\n')


def header(category, heading, subheading, dark=False):
    ink, muted = ('#F2F6FA', '#C6D2DB') if dark else (INK, MUTED)
    return '\n'.join([
        text(56, 42, category.upper(), 15, '#5B91B7' if dark else BLUE, 700),
        text(56, 85, heading, 34, ink, 700),
        text(56, 116, subheading, 17, muted)
    ])


def write(name, body):
    path = OUT / name
    path.write_text(body + '</svg>\n', encoding='utf-8')
    print(f'Wrote {path.name}')


def osi():
    s = svg_start('osi', 'Seven OSI networking layers',
        'Seven horizontal bands from application and presentation to physical, with protocol examples.', 1000, 806)
    s += header('Network reference', 'The seven OSI layers', 'From application meaning to physical signal transmission.')
    layers = [
        (7, 'Application', 'Anwendung', 'HTTP  |  DNS  |  SMTP', '#285E83'),
        (6, 'Presentation', 'Darstellung', 'Encoding  |  encryption concepts', '#337193'),
        (5, 'Session', 'Sitzung', 'Session management concepts', '#407E9A'),
        (4, 'Transport', 'Transportebene', 'TCP  |  UDP', '#237C77'),
        (3, 'Network', 'Vermittlung', 'IPv4  |  IPv6  |  ICMP', '#3E805C'),
        (2, 'Data Link', 'Sicherung', 'Ethernet  |  WLAN-MAC', '#986934'),
        (1, 'Physical', 'Bit\u00fcbertragung', 'Copper  |  optical fiber  |  radio', '#805B53'),
    ]
    for idx, (num, en, de, example, color) in enumerate(layers):
        y = 147 + idx*87
        s += rect(56, y, 888, 79, color, 12) + '\n'
        s += rect(68, y+12, 64, 55, '#FFFFFF', 9, opacity=.14) + '\n'
        s += text(100, y+49, num, 32, '#FFFFFF', 700, 'middle') + '\n'
        s += text(157, y+35, en + '  /  ' + de, 24, '#FFFFFF', 700) + '\n'
        s += text(157, y+60, example, 17, '#F2F8FA') + '\n'
    s += text(56, 789, 'Conceptual teaching model; real protocol stacks do not map perfectly to seven layers.', 14, MUTED)
    write('osi-layers.svg', s)


def actor(x, y, name, ip, kind, tint):
    s = rect(x, y, 278, 94, '#FFFFFF', 12, RULE, 1.5) + '\n'
    s += rect(x+16, y+18, 54, 54, tint, 9) + '\n'
    # A laptop-like icon: simple paths; no emoji or icon font dependency.
    s += (f'<rect x="{x+28}" y="{y+31}" width="29" height="19" rx="2" '
          f'fill="none" stroke="#FFFFFF" stroke-width="2" />')
    s += line(x+25, y+55, x+60, y+55, '#FFFFFF', 2) + '\n'
    s += text(x+88, y+38, name, 23, INK, 700)
    s += text(x+88, y+62, ip, 16, MUTED, mono=True)
    s += text(x+88, y+80, kind, 13, tint, 700)
    return s


def handshake():
    s = svg_start('tcp', 'TCP three-way handshake',
        'Client sends SYN, server responds SYN ACK, client confirms with ACK. These are TCP messages handled by the kernel.', 1024, 738)
    s += header('Sequence diagram', 'TCP connection setup', 'Two endpoints; the operating system handles the transport handshake.')
    s += actor(84, 150, 'Client Y', '192.168.1.20', 'ACTIVE OPEN', BLUE)
    s += actor(662, 150, 'Server X', '192.168.1.10', 'LISTENING :8080', TEAL)
    # Lifelines at centers of cards
    left, right = 223, 801
    s += line(left, 251, left, 617, '#C9D5DE', 2, '7 9') + '\n'
    s += line(right, 251, right, 617, '#C9D5DE', 2, '7 9') + '\n'
    for n, y, d, color, marker, label in [
        (1, 318, f'M {left} {318} H {right}', BLUE, 'blue', 'SYN'),
        (2, 425, f'M {right} {425} H {left}', TEAL, 'teal', 'SYN + ACK'),
        (3, 532, f'M {left} {532} H {right}', BLUE, 'blue', 'ACK'),
    ]:
        s += rect(54, y-24, 44, 44, '#E8EFF5', 22) + '\n'
        s += text(76, y+7, n, 22, INK, 700, 'middle') + '\n'
        s += arrow_path(d, color, marker) + '\n'
        width = 144 if n==2 else 98
        s += rect(512-width/2, y-37, width, 31, PAPER, 6) + '\n'
        s += text(512, y-15, label, 21, INK, 700, 'middle') + '\n'
    s += rect(84, 628, 856, 72, '#E5F3EE', 12, '#C4E3D5', 1) + '\n'
    s += (f'<circle cx="127" cy="664" r="17" fill="{GREEN}"/>\n')
    s += '<path d="M 118 663 L 125 670 L 138 656" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>\n'
    s += text(158, 659, 'Connection established', 23, INK, 700) + '\n'
    s += text(158, 683, 'accept() returns a connected socket; it is not another network message.', 16, MUTED)
    write('tcp-handshake.svg', s)


def encapsulation():
    s = svg_start('encap', 'Protocol encapsulation',
        'Four rows show application data, a TCP segment, an IP packet, and an Ethernet frame with Ethernet FCS.', 1040, 811)
    s += header('Structure diagram', 'How packets are encapsulated', 'Each lower layer wraps the higher-layer payload with its own information.')
    rows = [
       ('01   Application data', [('Payload: Hallo', 892, BLUE)]),
       ('02   TCP segment', [('TCP header', 252, TEAL), ('Payload: Hallo', 640, BLUE)]),
       ('03   IP packet', [('IP header', 184, GREEN), ('TCP header', 238, TEAL), ('Payload: Hallo', 470, BLUE)]),
       ('04   Ethernet frame', [('Eth. header', 171, OCHRE), ('IP header', 155, GREEN), ('TCP header', 205, TEAL), ('Payload', 235, BLUE), ('FCS', 126, BROWN)])
    ]
    for idx, (label, parts) in enumerate(rows):
        y = 146 + idx*144
        s += rect(56, y, 928, 128, '#FFFFFF', 12, RULE) + '\n'
        s += text(76, y+32, label.upper(), 16, MUTED, 700) + '\n'
        startx = 76
        for j, (caption, width, fill) in enumerate(parts):
            r = 7 if j in (0,len(parts)-1) else 0
            s += rect(startx, y+53, width, 58, fill, r) + '\n'
            s += text(startx+width/2, y+89, caption, 17 if width>=155 else 15, '#FFFFFF', 700, 'middle') + '\n'
            startx += width
    s += text(58, 755, 'Widths are schematic, not proportional to header sizes in bytes.', 15, MUTED) + '\n'
    s += text(58, 779, 'At the receiver, each layer interprets and removes its corresponding envelope.', 15, MUTED)
    write('packet-encapsulation.svg', s)


def architecture():
    s = svg_start('repo', 'Generic codebase architecture',
        'A client calls an API route, which delegates to a domain service that queries a database. API and service share one application process.', 1100, 711)
    s += header('Software architecture', 'One process, three responsibilities', 'Example topology; replace module names and edges with actual repository facts.')
    # External nodes and one shared process boundary
    s += rect(52, 252, 234, 198, '#FFFFFF', 13, RULE) + '\n'
    s += rect(52, 252, 234, 10, BLUE, 3) + '\n'
    s += text(75, 312, 'Client', 26, INK, 700) + '\n'
    s += text(75, 347, 'Browser / CLI', 19, MUTED) + '\n'
    s += text(75, 397, 'Sends requests', 16, BLUE, 700)

    s += rect(332, 165, 414, 394, '#E9F3F6', 16, '#9EC9D2', 1.5) + '\n'
    s += text(356, 200, 'APPLICATION PROCESS', 16, TEAL, 700) + '\n'
    s += text(356, 227, 'same runtime, separate modules', 16, MUTED) + '\n'
    s += rect(360, 263, 358, 94, '#FFFFFF', 10, '#B9D9DF') + '\n'
    s += text(384, 300, 'API route', 24, INK, 700) + '\n'
    s += text(384, 331, 'Parsing, validation, response', 17, MUTED) + '\n'
    s += rect(360, 425, 358, 94, '#FFFFFF', 10, '#B9D9DF') + '\n'
    s += text(384, 462, 'Domain service', 24, INK, 700) + '\n'
    s += text(384, 493, 'Business rules and orchestration', 17, MUTED) + '\n'

    s += rect(792, 252, 256, 198, '#FFFFFF', 13, RULE) + '\n'
    s += rect(792, 252, 256, 10, GREEN, 3) + '\n'
    s += text(815, 312, 'Database', 26, INK, 700) + '\n'
    s += text(815, 347, 'Persistent data', 19, MUTED) + '\n'
    s += text(815, 397, 'External dependency', 16, GREEN, 700)

    s += arrow_path('M 286 308 H 360', BLUE, 'blue', 3) + '\n'
    s += rect(291, 266, 66, 27, PAPER, 5) + '\n'
    s += text(324, 285, 'HTTP', 15, INK, 700, 'middle') + '\n'
    s += arrow_path('M 539 357 V 425', TEAL, 'teal', 3) + '\n'
    s += rect(551, 375, 125, 29, '#E9F3F6', 5) + '\n'
    s += text(613, 395, 'calls', 16, INK, 700, 'middle') + '\n'
    s += arrow_path('M 718 470 H 770 V 375 H 792', GREEN, 'green', 3) + '\n'
    s += rect(728, 329, 58, 31, PAPER, 5) + '\n'
    s += text(757, 351, 'SQL', 15, INK, 700, 'middle') + '\n'

    s += rect(52, 598, 996, 77, '#FFFFFF', 12, RULE) + '\n'
    s += text(77, 629, 'Read the boundaries carefully', 19, INK, 700) + '\n'
    s += text(77, 657, 'Modules are logical units here; the API and service are NOT separate deployments.', 17, MUTED)
    write('codebase-architecture.svg', s)


def starter():
    s = svg_start('starter', 'Minimal diagram starter',
        'Two labeled rounded boxes connected by a directional arrow.', 960, 475)
    s += header('Editable template', 'A clear idea, one arrow', 'Change labels and coordinates; keep the SVG valid and portable.')
    s += rect(70, 190, 320, 150, '#FFFFFF', 12, RULE) + '\n'
    s += rect(70, 190, 320, 10, BLUE, 4) + '\n'
    s += text(98, 250, 'Source', 28, INK, 700) + '\n'
    s += text(98, 288, 'An input, actor or module', 18, MUTED) + '\n'
    s += rect(570, 190, 320, 150, '#FFFFFF', 12, RULE) + '\n'
    s += rect(570, 190, 320, 10, TEAL, 4) + '\n'
    s += text(598, 250, 'Destination', 28, INK, 700) + '\n'
    s += text(598, 288, 'Another actor or component', 18, MUTED) + '\n'
    s += arrow_path('M 390 266 H 570', BLUE, 'blue', 3) + '\n'
    s += rect(431, 228, 98, 31, PAPER, 5) + '\n'
    s += text(480, 250, 'sends', 18, INK, 700, 'middle') + '\n'
    s += text(70, 412, 'This is pure SVG markup: editable text, reusable shapes, no external fonts or assets.', 17, MUTED)
    write('starter.svg', s)


if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    starter()
    osi()
    handshake()
    encapsulation()
    architecture()
