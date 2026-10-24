import urllib.request
import json
from datetime import datetime

# 1. Fetch current atomic year via a keyless public API
def get_current_year():
    try:
        url = "https://timeapi.io/api/time/current/zone?timeZone=UTC"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            return data['year']
    except Exception:
        return datetime.utcnow().year

current_year = get_current_year()
years_uptime = current_year - 2009

lolyou_runes = "ᛚᛟᛚᚹᛟᚢ"
gotfooled_runes = "ᚷᛟᛏᚠᛟᛟᛚᛖᛞ"

# 2. Your ASCII art grid (& = invisible background padding, others = Kali logo)
raw_ascii = [
    "&$XXXXXXXXXXXXXXXXXXXXXXXXXX$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XXXXxxxxXX$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XXXxxxxXX$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XXxxxxX$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Xx+X&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&$XXXXXXXXXxxxxxxxxx+++++++++x+X&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&$XXXXXXXXXXXXX$&&&&&&&&&&&&&&&&&&&&&&&&&&&xx&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&XXXXXX$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XXxxxx+X+$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&Xx++++++xxXX$$$&x+&&&&&&&&&&&&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XXxxxXX$&&&&&&&&&&&&&&&++X&&&&&&&&&&&&&$$&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&XXxXX$&&&&&&&&&&&&&&&&&&&&&&$;;;+x$&&&&&&&&&&&&$X$&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&XXXX&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$;;;;;;;;;+++x$&&&&&&&X$&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&XXX$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+;;;;;;+++++++++++xxX&&&&XX&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&$XX&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&;;;;;x&&&&&&&&&&&&X+++++xxX&XXX&&&&&&&&&&&&&&",
    "&&&&&&&&&&$X$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X;;;+$&&&&&&&&&&&&&&&&&&&XxxxxXx$XX&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&x;;;x&&&&&&&&&&&&&&&&&&&&&&&&&$XxxXXX&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X;;;+&&&&&&&&&&&&&&&&&&&&&&&&&&&&$xxxxX$&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+;;;&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XxxxXX$&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&;;;x&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XXxx$&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X;;;X&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XxXX$&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+;;x&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$X&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X;;;$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+;;;$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&x;;;x&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$+;;;x$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&+++++++xX&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$xx+++++++++xxxXX$$$&&&&&&&&&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$XXXxxxxxxxxxxxXXXX$&&&&&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XXxxxXXXXXXXX&&&&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XXxXX&&&XXXXXX&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XXXX&&&&&XXXX&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XXXX&&&&&&XXX&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XXX$&&&&&&XX&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XXX&&&&&&&X&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XXX&&&&&&&X",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$xX&&&&&&&X",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XX&&&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$XX&&&&&$",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$X$&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XX&&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&XX&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$X&&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&X$&&",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$&"
]

ascii_art = [line.ljust(95, '&') for line in raw_ascii]

specs = [
    '<tspan class="header">root@kali</tspan>',
    '<tspan class="value">---------</tspan>',
    '<tspan class="label">OS:</tspan><tspan class="value"> Kali GNU/Linux Rolling x86_64</tspan>',
    '<tspan class="label">Host:</tspan><tspan class="value"> MSI MAG B650 TOMAHAWK WIFI (MS-7D74)</tspan>',
    '<tspan class="label">Kernel:</tspan><tspan class="value"> 5.10.0-kali7-amd64</tspan>',
    f'<tspan class="label">Uptime:</tspan><tspan class="value"> {years_uptime} years, {lolyou_runes} months, {gotfooled_runes} days</tspan>',
    '<tspan class="label">Packages:</tspan><tspan class="value"> 2914 (dpkg)</tspan>',
    '<tspan class="label">Shell:</tspan><tspan class="value"> bash 5.0.16</tspan>',
    '<tspan class="label">Resolution:</tspan><tspan class="value"> 2560x1440</tspan>',
    '<tspan class="label">DE:</tspan><tspan class="value"> Xfce 4.16</tspan>',
    '<tspan class="label">WM:</tspan><tspan class="value"> Xfwm4</tspan>',
    '<tspan class="label">WM Theme:</tspan><tspan class="value"> Kali-Dark</tspan>',
    '<tspan class="label">Terminal:</tspan><tspan class="value"> qterminal</tspan>',
    '<tspan class="label">CPU:</tspan><tspan class="value"> AMD Ryzen 7 7800X3D (8) @ 4.200GHz</tspan>',
    '<tspan class="label">GPU:</tspan><tspan class="value"> NVIDIA GeForce RTX 4090</tspan>',
    '<tspan class="label">Memory:</tspan><tspan class="value"> 4118MiB / 15942MiB (25%)</tspan>',
    '<tspan class="label">Disk (/):</tspan><tspan class="value"> 342GiB / 1862GiB (18%)</tspan>',
    '',
    '<tspan class="value">[ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ]</tspan>'
]

def parse_ascii_line(line):
    result = []
    curr_type = None
    chunk = ""
    for ch in line:
        ch_escaped = '&amp;' if ch == '&' else ch
        t = 'bg' if ch == '&' else 'kali'
        if t == curr_type:
            chunk += ch_escaped
        else:
            if chunk:
                result.append(f'<tspan class="{curr_type}">{chunk}</tspan>')
            chunk = ch_escaped
            curr_type = t
    if chunk:
        result.append(f'<tspan class="{curr_type}">{chunk}</tspan>')
    return "".join(result)

svg_lines = []
start_y = 65
line_height = 13

for i, line_str in enumerate(ascii_art):
    y = start_y + (i * line_height)
    art_svg = parse_ascii_line(line_str)
    svg_lines.append(f'  <text x="20" y="{y}" class="text" xml:space="preserve">{art_svg}</text>')

# Specs configuration: 1.5x font size (16px), double line gap (36px spacing), pushed right to x="760"
spec_start_y = 75
spec_line_height = 36
spec_x = 760

spec_lines = []
for idx, spec_html in enumerate(specs):
    if spec_html:
        s_y = spec_start_y + (idx * spec_line_height)
        spec_lines.append(f'  <text x="{spec_x}" y="{s_y}" class="specs" xml:space="preserve">{spec_html}</text>')

ascii_block = "\n".join(svg_lines)
specs_block = "\n".join(spec_lines)
total_height = max(start_y + len(ascii_art) * line_height + 100, spec_start_y + len(specs) * spec_line_height + 100)

svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1550" height="{total_height}" viewBox="0 0 1550 {total_height}">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code&amp;display=swap');
    
    .bg {{ fill: #0d1117; color: #0d1117; }}
    .text {{ font-family: 'Fira Code', monospace; font-size: 16px; }}
    .specs {{ font-family: 'Fira Code', monospace; font-size: 16px; }}
    .kali {{ fill: #0088cc; }}
    .header {{ fill: #ffffff; font-weight: bold; }}
    .label {{ fill: #79c0ff; }}
    .value {{ fill: #c9d1d9; }}
    .prompt {{ fill: #ff7b72; }}
    .command {{ fill: #e5c07b; }}
    .output {{ fill: #56b6c2; }}
    .cursor {{ fill: #f0883e; }}
  </style>

  <rect width="100%" height="100%" rx="8" class="bg" />

  <text x="20" y="25" class="text prompt" xml:space="preserve">┌──(root㉿kali)-[/root]</text>
  <text x="20" y="40" class="text" xml:space="preserve"><tspan class="prompt">└─# </tspan><tspan class="command">neofetch</tspan></text>
  
{ascii_block}

{specs_block}

  <text x="20" y="{total_height - 65}" class="text prompt" xml:space="preserve">┌──(root㉿kali)-[/root]</text>
  <text x="20" y="{total_height - 50}" class="text" xml:space="preserve"><tspan class="prompt">└─# </tspan><tspan class="command">whoami</tspan></text>
  <text x="20" y="{total_height - 35}" class="text output" xml:space="preserve">QuantumTechCoder Official - Coder Hacker Tech Expert AI Orchestration</text>
  <text x="20" y="{total_height - 15}" class="text prompt" xml:space="preserve">┌──(root㉿kali)-[/root]</text>
  <text x="20" y="{total_height - 2}" class="text" xml:space="preserve"><tspan class="prompt">└─# </tspan><tspan class="cursor">█</tspan></text>
</svg>
"""

with open("neofetch.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("Successfully generated perfectly proportioned neofetch.svg!")
