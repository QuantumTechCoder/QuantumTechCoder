import os
import re
import urllib.request
import json
from datetime import datetime
from pathlib import Path

BASE = Path("profile_repo/assets")
LINKS_DIR = BASE / "links"
LINKS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Calculate live uptime from 2009
try:
    url = "https://timeapi.io/api/time/current/zone?timeZone=UTC"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as response:
        data = json.loads(response.read().decode())
        current_year = data['year']
except Exception:
    current_year = datetime.utcnow().year

years_uptime = current_year - 2009

COMMON_DEFS = """
<defs>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#00d9ff" stroke-opacity=".05"/></pattern>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="sglow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2"/></filter>
<pattern id="scan" width="4" height="3" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#000" fill-opacity=".2"/></pattern>
</defs>
"""

COMMON_STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&amp;family=Fira+Code:wght@400;600;700&amp;display=swap');
text { font-family: 'Fira Code', 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
.brand-orbitron { font-family: 'Orbitron', 'Fira Code', system-ui, sans-serif; font-weight: 900; }
.dim { fill: #6272a4; }
.cy { fill: #00d9ff; }
.fg { fill: #f8f8f2; }
.gr { fill: #50fa7b; }
.pk { fill: #ff79c6; }
.pp { fill: #bd93f9; }
.yl { fill: #f1fa8c; }
@keyframes blink { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: .3; } }
@keyframes gm { 0%, 92%, 100% { transform: translate(0,0); } 93% { transform: translate(3px,-1px); } 95% { transform: translate(-2px,1px); } 97% { transform: translate(1px,0); } }
@keyframes gc { 0%, 92%, 100% { transform: translate(0,0); } 93% { transform: translate(-3px,1px); } 95% { transform: translate(2px,-1px); } 97% { transform: translate(-1px,0); } }
.cursor { animation: blink 1.05s step-end infinite; }
.dot { animation: pulse 2s ease-in-out infinite; }
.gm { animation: gm 5s linear 1s infinite; }
.gc { animation: gc 5s linear 1s infinite; }
@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
</style>
"""

def generate_header():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="350" viewBox="0 0 880 350" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<path d="M16 16V350M864 16V350M16 16H864" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".4" filter="url(#glow)"/>
<rect x="16" y="16" width="848" height="334" fill="#03040a"/>
<rect x="16" y="16" width="848" height="334" fill="url(#grid)"/>

<!-- Top Status Bar -->
<rect x="16" y="16" width="848" height="34" fill="#00d9ff" fill-opacity=".08"/>
<line x1="16" y1="50" x2="864" y2="50" stroke="#00d9ff" stroke-opacity=".4"/>
<text x="32" y="38" letter-spacing="1" class="cy" font-size="11.5">SYS://QUANTUM // NODE:QUANTUMTECHCODER</text>
<text x="844" y="38" letter-spacing="1" class="dim" text-anchor="end" font-size="11.5">ONLINE · ALL SYSTEMS NOMINAL</text>
<circle class="dot" cx="600" cy="34" r="4" fill="#50fa7b"/>
<circle class="dot" cx="600" cy="34" r="4" fill="#50fa7b" filter="url(#sglow)"/>

<!-- Terminal Command Prompt -->
<text x="52" y="96" class="dim" font-size="15"><tspan class="gr">$</tspan> whoami</text>

<!-- Orbitron Brand Title - NO SPACES, EXACT MATCH -->
<g class="brand-orbitron" letter-spacing="3" font-size="50">
  <text x="52" y="162" fill="#00d9ff" opacity=".4" filter="url(#glow)">QuantumTechCoder</text>
  <g class="gm"><text x="54" y="162" fill="#ff79c6" opacity=".75">QuantumTechCoder</text></g>
  <g class="gc"><text x="50" y="162" fill="#00d9ff" opacity=".85">QuantumTechCoder</text></g>
  <text x="52" y="162" fill="#f8f8f2">QuantumTechCoder</text>
</g>

<!-- Bullet Subtitles -->
<text class="fg" x="52" y="210" font-size="14.5"><tspan class="cy">&gt;&gt;</tspan> Systems Explorer · Ethical Hacker · AI &amp; Full-Stack Architect</text>
<text class="fg" x="52" y="236" font-size="14.5"><tspan class="cy">&gt;&gt;</tspan> Low-level tinkerer, real-time WebRTC &amp; WebGL shader engineer</text>
<text class="fg" x="52" y="262" font-size="14.5"><tspan class="cy">&gt;&gt;</tspan> Building autonomous agents &amp; impossible developer tooling</text>

<!-- Prompt with Blinking Cursor -->
<text x="52" y="300" class="gr" font-size="15">$</text>
<rect class="cursor" x="70" y="286" width="10" height="18" fill="#00d9ff"/>
<rect class="cursor" x="70" y="286" width="10" height="18" fill="#00d9ff" filter="url(#sglow)"/>

<!-- Scanline Overlay -->
<rect x="16" y="51" width="848" height="299" fill="url(#scan)"/>
<path d="M16 16V350M864 16V350M16 16H864" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
<g fill="none" stroke="#00d9ff" stroke-width="2"><path d="M9 34V9H34"/><path d="M846 9H871V34"/></g>
</svg>"""

def generate_section(title: str, cmd: str, h: int = 100):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="{h}" viewBox="0 0 880 {h}" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<path d="M16 0V{h}M864 0V{h}" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".35" filter="url(#glow)"/>
<rect x="16" y="0" width="848" height="{h}" fill="#03040a"/>
<rect x="16" y="0" width="848" height="{h}" fill="url(#grid)"/>

<line x1="52" y1="18" x2="160" y2="18" stroke="#00d9ff" stroke-width="2" filter="url(#sglow)"/>
<text x="52" y="50" class="fg" font-weight="bold" font-size="19" letter-spacing="1">{title}</text>
<text x="52" y="78" class="dim" font-size="13.5"><tspan class="gr">$</tspan> {cmd}</text>

<path d="M16 0V{h}M864 0V{h}" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
</svg>"""

def generate_link_btn(icon: str, label: str, sub: str, pos: str, color: str = "#00d9ff"):
    # pos in ['first', 'mid', 'last']
    rail_svg = ""
    bx = 6
    bw = 164
    if pos == "first":
        rail_svg = '<path d="M16 0V76" fill="none" stroke="#00d9ff" stroke-width="1.2"/>'
        bx = 22
        bw = 148
    elif pos == "last":
        rail_svg = '<path d="M160 0V76" fill="none" stroke="#00d9ff" stroke-width="1.2"/>'
        bx = 6
        bw = 148

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="176" height="76" viewBox="0 0 176 76" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<rect width="176" height="76" fill="#03040a"/>
<rect x="{bx}" y="6" width="{bw}" height="64" rx="6" fill="#060a14" stroke="{color}" stroke-width="1.2" stroke-opacity=".7"/>
<circle cx="{bx + 22}" cy="38" r="13" fill="{color}" fill-opacity=".12"/>
<text x="{bx + 22}" y="43" text-anchor="middle" font-size="14">{icon}</text>
<text x="{bx + 42}" y="34" fill="#f8f8f2" font-weight="bold" font-size="12.5">{label}</text>
<text x="{bx + 42}" y="50" fill="{color}" font-size="10">{sub}</text>
{rail_svg}
</svg>"""

def generate_project_card(title: str, badge: str, desc1: str, desc2: str, tags: list, side: str, color: str = "#00d9ff"):
    # side in ['left', 'right']
    rail_svg = ""
    bx = 8
    bw = 424
    if side == "left":
        rail_svg = '<path d="M16 0V190" fill="none" stroke="#00d9ff" stroke-width="1.2"/>'
        bx = 22
        bw = 410
    else:
        rail_svg = '<path d="M424 0V190" fill="none" stroke="#00d9ff" stroke-width="1.2"/>'
        bx = 8
        bw = 410

    tags_svg = ""
    tx = 0
    for t in tags:
        tw = len(t) * 7 + 16
        tags_svg += f"""
        <rect x="{tx}" y="0" width="{tw}" height="20" rx="4" fill="#08101e" stroke="#1d2e47" stroke-width="1"/>
        <text x="{tx + tw/2}" y="14" text-anchor="middle" fill="#8be9fd" font-size="10">{t}</text>
        """
        tx += tw + 8

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="440" height="190" viewBox="0 0 440 190" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<rect width="440" height="190" fill="#03040a"/>
<rect x="{bx}" y="6" width="{bw}" height="178" rx="8" fill="#050811" stroke="{color}" stroke-width="1.2" stroke-opacity=".75"/>

<text x="{bx + 18}" y="36" fill="#ffffff" font-weight="bold" font-size="16.5">{title}</text>
<rect x="{bx + bw - 124}" y="20" width="112" height="22" rx="4" fill="{color}" fill-opacity=".12" stroke="{color}" stroke-width="1"/>
<text x="{bx + bw - 68}" y="35" text-anchor="middle" fill="{color}" font-weight="bold" font-size="9.5">{badge}</text>

<text x="{bx + 18}" y="70" fill="#a0aec0" font-size="12">{desc1}</text>
<text x="{bx + 18}" y="92" fill="#a0aec0" font-size="12">{desc2}</text>

<g transform="translate({bx + 18}, 136)">
{tags_svg}
</g>
{rail_svg}
</svg>"""

def generate_stats_panel():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="240" viewBox="0 0 880 240" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<path d="M16 0V240M864 0V240" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".35" filter="url(#glow)"/>
<rect x="16" y="0" width="848" height="240" fill="#03040a"/>
<rect x="16" y="0" width="848" height="240" fill="url(#grid)"/>

<!-- 4 Telemetry Metric Boxes -->
<g transform="translate(36, 16)">
  <!-- Box 1: Contributions -->
  <rect x="0" y="0" width="190" height="96" rx="8" fill="#060a14" stroke="#00d9ff" stroke-width="1" stroke-opacity=".6"/>
  <text x="20" y="32" class="dim" font-size="11">CONTRIBUTIONS</text>
  <text x="20" y="70" fill="#00d9ff" font-weight="bold" font-size="28">2,177+</text>

  <!-- Box 2: Commits -->
  <rect x="206" y="0" width="190" height="96" rx="8" fill="#060a14" stroke="#50fa7b" stroke-width="1" stroke-opacity=".6"/>
  <text x="226" y="32" class="dim" font-size="11">TOTAL COMMITS</text>
  <text x="226" y="70" fill="#50fa7b" font-weight="bold" font-size="28">110+</text>

  <!-- Box 3: Streak -->
  <rect x="412" y="0" width="190" height="96" rx="8" fill="#060a14" stroke="#ff79c6" stroke-width="1" stroke-opacity=".6"/>
  <text x="432" y="32" class="dim" font-size="11">CURRENT STREAK</text>
  <text x="432" y="70" fill="#ff79c6" font-weight="bold" font-size="28">🔥 6 Days</text>

  <!-- Box 4: Stars -->
  <rect x="618" y="0" width="190" height="96" rx="8" fill="#060a14" stroke="#f1fa8c" stroke-width="1" stroke-opacity=".6"/>
  <text x="638" y="32" class="dim" font-size="11">REPOSITORIES</text>
  <text x="638" y="70" fill="#f1fa8c" font-weight="bold" font-size="28">⭐ 15 Public</text>
</g>

<!-- Languages Bar -->
<g transform="translate(36, 134)">
  <rect width="808" height="88" rx="8" fill="#050811" stroke="#1d2e47" stroke-width="1"/>
  <text x="20" y="28" fill="#8be9fd" font-size="11" font-weight="bold">TOP SYSTEM STACKS &amp; RATIOS:</text>
  
  <!-- Stack Progress bar -->
  <rect x="20" y="40" width="768" height="12" rx="6" fill="#141c2b"/>
  <rect x="20" y="40" width="280" height="12" rx="6" fill="#3178c6"/> <!-- TS -->
  <rect x="300" y="40" width="210" height="12" rx="0" fill="#3572A5"/> <!-- Python -->
  <rect x="510" y="40" width="130" height="12" rx="0" fill="#f7df1e"/> <!-- JS -->
  <rect x="640" y="40" width="80" height="12" rx="0" fill="#f34b7d"/> <!-- C++ -->
  <rect x="720" y="40" width="68" height="12" rx="6" fill="#dea584"/> <!-- Rust -->

  <!-- Legend -->
  <g transform="translate(20, 72)" font-size="10.5">
    <circle cx="5" cy="-4" r="4" fill="#3178c6"/>
    <text x="14" y="0" class="fg">TypeScript 36%</text>

    <circle cx="160" cy="-4" r="4" fill="#3572A5"/>
    <text x="170" y="0" class="fg">Python 27%</text>

    <circle cx="290" cy="-4" r="4" fill="#f7df1e"/>
    <text x="300" y="0" class="fg">JavaScript 17%</text>

    <circle cx="430" cy="-4" r="4" fill="#f34b7d"/>
    <text x="440" y="0" class="fg">C++ 10%</text>

    <circle cx="530" cy="-4" r="4" fill="#dea584"/>
    <text x="540" y="0" class="fg">Rust / Shaders 10%</text>
  </g>
</g>

<path d="M16 0V240M864 0V240" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
</svg>"""

def generate_terminal_panel():
    # Read neofetch ASCII art and specs from kali_terminal_svg_maker.py
    lolyou_runes = "ᛚᛟᛚᚹᛟᚢ"
    gotfooled_runes = "ᚷᛟᛏᚠᛟᛟᛚᛖᛞ"
    
    specs = [
        '<tspan fill="#ffffff" font-weight="bold">root@kali</tspan>',
        '<tspan fill="#6272a4">---------</tspan>',
        '<tspan fill="#79c0ff">OS:</tspan><tspan fill="#f8f8f2"> Kali GNU/Linux Rolling x86_64</tspan>',
        '<tspan fill="#79c0ff">Host:</tspan><tspan fill="#f8f8f2"> MSI MAG B650 TOMAHAWK WIFI</tspan>',
        '<tspan fill="#79c0ff">Kernel:</tspan><tspan fill="#f8f8f2"> 5.10.0-kali7-amd64</tspan>',
        f'<tspan fill="#79c0ff">Uptime:</tspan><tspan fill="#f8f8f2"> {years_uptime} years, {lolyou_runes} months, {gotfooled_runes} days</tspan>',
        '<tspan fill="#79c0ff">Shell:</tspan><tspan fill="#f8f8f2"> bash 5.0.16 | Terminal: qterminal</tspan>',
        '<tspan fill="#79c0ff">Resolution:</tspan><tspan fill="#f8f8f2"> 2560x1440 | DE: Xfce 4.16</tspan>',
        '<tspan fill="#79c0ff">CPU:</tspan><tspan fill="#f8f8f2"> AMD Ryzen 7 7800X3D (8) @ 4.200GHz</tspan>',
        '<tspan fill="#79c0ff">GPU:</tspan><tspan fill="#f8f8f2"> NVIDIA GeForce RTX 4090</tspan>',
        '<tspan fill="#79c0ff">Memory:</tspan><tspan fill="#f8f8f2"> 4118MiB / 15942MiB (25%)</tspan>',
        '<tspan fill="#79c0ff">Disk (/):</tspan><tspan fill="#f8f8f2"> 342GiB / 1862GiB (18%)</tspan>',
        '',
        '<tspan fill="#50fa7b">[ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ]</tspan>'
    ]

    spec_lines = []
    sy = 96
    for sp in specs:
        if sp:
            spec_lines.append(f'<text x="440" y="{sy}" font-size="12.5">{sp}</text>')
        sy += 22

    specs_block = "\\n".join(spec_lines)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="460" viewBox="0 0 880 460" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<path d="M16 0V460M864 0V460" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".35" filter="url(#glow)"/>
<rect x="16" y="0" width="848" height="460" fill="#03040a"/>
<rect x="16" y="0" width="848" height="460" fill="url(#grid)"/>

<!-- Terminal Window Container -->
<rect x="36" y="16" width="808" height="428" rx="8" fill="#050811" stroke="#00d9ff" stroke-width="1.2" stroke-opacity=".6"/>

<!-- Terminal Top Bar -->
<rect x="36" y="16" width="808" height="28" rx="8" fill="#090f1d"/>
<circle cx="54" cy="30" r="4.5" fill="#ff5555"/>
<circle cx="68" cy="30" r="4.5" fill="#ffb86c"/>
<circle cx="82" cy="30" r="4.5" fill="#50fa7b"/>
<text x="440" y="34" text-anchor="middle" class="dim" font-size="11">root@kali: ~ (qterminal)</text>

<!-- Prompt 1 -->
<text x="56" y="66" fill="#ff5555" font-size="12">┌──(root㉿kali)-[/root]</text>
<text x="56" y="84" font-size="12"><tspan fill="#ff5555">└─# </tspan><tspan fill="#f1fa8c">neofetch</tspan></text>

<!-- Dragon ASCII block (scaled and stylized) -->
<g transform="translate(56, 102)" fill="#0088cc" font-size="9" letter-spacing="1">
  <text y="0">.............. :X- ..............</text>
  <text y="14">.......... =@@@@@@@@X: ..........</text>
  <text y="28">........ +@@@@@@@@@@@@% .........</text>
  <text y="42">....... :@@@@@@@@@@@@@@- ........</text>
  <text y="56">...... :@@@@@@@@@@@@@@@@= .......</text>
  <text y="70">..... +@@@@@@@@@@@@@@@@@@: ......</text>
  <text y="84">.... -@@@@@@@@@@@@@@@@@@@@- .....</text>
  <text y="98">... =@@@@@@@@@@@@@@@@@@@@@@: ....</text>
  <text y="112">.. +@@@@@@@@@@@@@@@@@@@@@@@@% ...</text>
  <text y="126">. :@@@@@@@@@@@@@@@@@@@@@@@@@@- ..</text>
  <text y="140">. =@@@@@@@@@@@@@@@@@@@@@@@@@@= ..</text>
  <text y="154">.. +@@@@@@@@@@@@@@@@@@@@@@@@- ...</text>
  <text y="168">... :X@@@@@@@@@@@@@@@@@@@@= .....</text>
  <text y="182">..... -%@@@@@@@@@@@@@@@@+ .......</text>
  <text y="196">....... :%@@@@@@@@@@@@+ .........</text>
  <text y="210">.......... =%@@@@@@X: ...........</text>
</g>

{specs_block}

<!-- Whoami Bottom Prompt -->
<text x="56" y="380" fill="#ff5555" font-size="12">┌──(root㉿kali)-[/root]</text>
<text x="56" y="398" font-size="12"><tspan fill="#ff5555">└─# </tspan><tspan fill="#f1fa8c">whoami</tspan></text>
<text x="56" y="416" fill="#50fa7b" font-size="12">QuantumTechCoder Official - Coder Hacker Tech Expert AI Orchestration</text>
<text x="56" y="432" font-size="12"><tspan fill="#ff5555">└─# </tspan><tspan fill="#00d9ff" class="cursor">█</tspan></text>

<path d="M16 0V460M864 0V460" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
</svg>"""

def generate_crypto_tip_jar():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="340" viewBox="0 0 880 340" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<path d="M16 0V340M864 0V340" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".35" filter="url(#glow)"/>
<rect x="16" y="0" width="848" height="340" fill="#03040a"/>
<rect x="16" y="0" width="848" height="340" fill="url(#grid)"/>

<!-- Frame -->
<rect x="36" y="18" width="808" height="304" rx="10" fill="#060913" stroke="#00d9ff" stroke-width="1.2" stroke-opacity=".7"/>

<!-- Header -->
<text x="60" y="54" fill="#ffffff" font-weight="bold" font-size="17">⚡ CRYPTO TIP JAR // MULTI-CHAIN EVM</text>
<text x="814" y="54" text-anchor="end" class="gr" font-size="11">● READY FOR TX</text>
<circle class="dot" cx="704" cy="50" r="3.5" fill="#50fa7b"/>

<line x1="60" y1="70" x2="820" y2="70" stroke="#1d2e47" stroke-width="1.2"/>
<text x="60" y="96" fill="#a0aec0" font-size="13">Fueling local GPU compute, late-night debugging marathons, and open-source tooling.</text>

<!-- Address Bar -->
<g transform="translate(60, 114)">
  <rect width="760" height="58" rx="8" fill="#020408" stroke="#00f7ff" stroke-width="1.2"/>
  <text x="20" y="22" fill="#6272a4" font-size="10">UNIVERSAL EVM ADDRESS (ONE ADDRESS FOR ALL CHAINS):</text>
  <text x="20" y="44" fill="#50fa7b" font-weight="bold" font-size="15">0x2cef0473f985156eDe84312Ce0BeB94B602d26E4</text>
  <rect x="670" y="15" width="70" height="28" rx="4" fill="#00d9ff" fill-opacity=".15" stroke="#00d9ff" stroke-width="1"/>
  <text x="705" y="33" text-anchor="middle" fill="#00f7ff" font-weight="bold" font-size="11">COPY</text>
</g>

<!-- Chains Support List -->
<text x="60" y="202" fill="#8be9fd" font-size="11" font-weight="bold">SUPPORTED BLOCKCHAINS &amp; LAYER 2s:</text>

<g transform="translate(60, 216)" font-size="11">
  <rect x="0" y="0" width="85" height="24" rx="4" fill="#0d1526" stroke="#3d4d6b" stroke-width="1"/>
  <text x="42" y="16" text-anchor="middle" fill="#f8f8f2">Ethereum</text>

  <rect x="95" y="0" width="80" height="24" rx="4" fill="#0d1526" stroke="#28a0f0" stroke-width="1"/>
  <text x="135" y="16" text-anchor="middle" fill="#64b5f6">Arbitrum</text>

  <rect x="185" y="0" width="80" height="24" rx="4" fill="#0d1526" stroke="#ff0420" stroke-width="1"/>
  <text x="225" y="16" text-anchor="middle" fill="#ff5252">Optimism</text>

  <rect x="275" y="0" width="65" height="24" rx="4" fill="#0d1526" stroke="#0052ff" stroke-width="1"/>
  <text x="307" y="16" text-anchor="middle" fill="#448aff">Base</text>

  <rect x="350" y="0" width="105" height="24" rx="4" fill="#0d1526" stroke="#8247e5" stroke-width="1"/>
  <text x="402" y="16" text-anchor="middle" fill="#b388ff">Polygon (POL)</text>

  <rect x="465" y="0" width="85" height="24" rx="4" fill="#0d1526" stroke="#f0b90b" stroke-width="1"/>
  <text x="507" y="16" text-anchor="middle" fill="#ffd54f">BNB Chain</text>

  <rect x="560" y="0" width="80" height="24" rx="4" fill="#0d1526" stroke="#e84142" stroke-width="1"/>
  <text x="600" y="16" text-anchor="middle" fill="#ef5350">Avalanche</text>

  <rect x="650" y="0" width="110" height="24" rx="4" fill="#0d1526" stroke="#00ff9f" stroke-width="1"/>
  <text x="705" y="16" text-anchor="middle" fill="#00ff9f">Linea · Scroll</text>
</g>

<text x="60" y="268" fill="#6272a4" font-size="11">ACCEPTED ASSETS: <tspan fill="#f8f8f2">ETH, BNB, POL, AVAX, ARB, OP, USDC, USDT, DAI, WETH, WBTC &amp; All ERC-20 / BEP-20 Tokens</tspan></text>
<text x="60" y="290" fill="#6272a4" font-size="10.5">🔒 Verified on <tspan fill="#00f7ff">Etherscan</tspan>, <tspan fill="#00f7ff">Basescan</tspan>, <tspan fill="#00f7ff">Arbiscan</tspan>, &amp; <tspan fill="#00f7ff">Polygonscan</tspan>. Low-gas L2 transfers warmly appreciated!</text>

<path d="M16 0V340M864 0V340" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
</svg>"""

def generate_footer():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="70" viewBox="0 0 880 70" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<path d="M16 0V56H864V0" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".4" filter="url(#glow)"/>
<rect x="16" y="0" width="848" height="56" fill="#03040a"/>
<rect x="16" y="0" width="848" height="56" fill="url(#grid)"/>

<text x="440" y="32" text-anchor="middle" font-size="11.5" fill="#6272a4">
  CONNECTION TERMINATED // HOST: QUANTUM // TALK IS CHEAP, SHOW ME THE CODE
</text>

<path d="M16 0V56H864V0" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
<g fill="none" stroke="#00d9ff" stroke-width="2"><path d="M9 40V65H34"/><path d="M846 65H871V40"/></g>
</svg>"""

# Generate all SVGs
(BASE / "header.svg").write_text(generate_header(), encoding="utf-8")
(BASE / "links.svg").write_text(generate_section("Links", "cat ~/.links"), encoding="utf-8")

# Links buttons with border rail alignment
(LINKS_DIR / "web.svg").write_text(generate_link_btn("🌐", "Website", "quantumtechcoder", "first", "#00d9ff"), encoding="utf-8")
(LINKS_DIR / "dev.svg").write_text(generate_link_btn("✍️", "DEV.to", "Articles &amp; Posts", "mid", "#00ff9f"), encoding="utf-8")
(LINKS_DIR / "gh.svg").write_text(generate_link_btn("💻", "GitHub", "@QuantumTechCoder", "mid", "#bd93f9"), encoding="utf-8")
(LINKS_DIR / "discord.svg").write_text(generate_link_btn("💬", "Discord", "quantumtechcoder", "mid", "#ff79c6"), encoding="utf-8")
(LINKS_DIR / "vault.svg").write_text(generate_link_btn("⚡", "Tip Jar", "Crypto EVM", "last", "#f1fa8c"), encoding="utf-8")

(BASE / "telemetry.svg").write_text(generate_section("Live Telemetry &amp; Stats", "sysctl -a telemetry"), encoding="utf-8")
(BASE / "stats.svg").write_text(generate_stats_panel(), encoding="utf-8")

(BASE / "projects.svg").write_text(generate_section("Featured Systems &amp; Projects", "ls -la ~/projects"), encoding="utf-8")

# Project cards with border rail alignment (left side rail on left cards, right side rail on right cards)
(BASE / "card-fractals.svg").write_text(generate_project_card(
    "FantasticFractals", "60 FPS WEBGL",
    "Real-time mathematical fractal visualizer (WebGL 2.0 &amp; React)",
    "Scientific library with NumPy computation &amp; 16K export.",
    ["WebGL", "React", "NumPy", "Python", "Shaders"], "left", "#00d9ff"
), encoding="utf-8")

(BASE / "card-airstream.svg").write_text(generate_project_card(
    "AirStream", "WEBRTC P2P",
    "Zero-limit peer-to-peer file transfer &amp; live clipboard",
    "Collaborative workspace on Cloudflare Pages &amp; OPFS.",
    ["WebRTC", "Cloudflare", "OPFS", "TypeScript"], "right", "#00ff9f"
), encoding="utf-8")

(BASE / "card-astra.svg").write_text(generate_project_card(
    "AstraForxBrowser", "CYBERPUNK DESKTOP",
    "High-octane browser engineered for terminal power users.",
    "Obsidian dark styling, CLI omnibox &amp; isolated incognito.",
    ["Electron", "Chromium", "JavaScript", "CLI"], "left", "#bd93f9"
), encoding="utf-8")

(BASE / "card-bytenews.svg").write_text(generate_project_card(
    "ByteNews", "EDGE FULL-STACK",
    "High-density, ultra-fast Hacker News platform.",
    "Built with Next.js App Router, Cloudflare D1 &amp; Prisma ORM.",
    ["Next.js", "Cloudflare D1", "Prisma", "Geist"], "right", "#ff79c6"
), encoding="utf-8")

(BASE / "stack.svg").write_text(generate_section("Technical Arsenal &amp; Stack", "cat ~/weapons.json"), encoding="utf-8")
(BASE / "terminal.svg").write_text(generate_terminal_panel(), encoding="utf-8")

(BASE / "vault.svg").write_text(generate_section("Crypto Tip Jar", "tip --crypto --evm"), encoding="utf-8")
(BASE / "crypto_vault.svg").write_text(generate_crypto_tip_jar(), encoding="utf-8")
(BASE / "footer.svg").write_text(generate_footer(), encoding="utf-8")

print("All profile assets updated with Orbitron, boundary rail alignment, and live terminal!")
