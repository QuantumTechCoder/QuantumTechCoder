import os
from pathlib import Path

BASE = Path("profile_repo/assets")
LINKS_DIR = BASE / "links"
LINKS_DIR.mkdir(parents=True, exist_ok=True)

orbitron_b64 = Path("orbitron_b64.txt").read_text(encoding="utf-8").strip()

COMMON_DEFS = """
<defs>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#00d9ff" stroke-opacity=".05"/></pattern>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>
<filter id="sglow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2"/></filter>
<pattern id="scan" width="4" height="3" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#000" fill-opacity=".2"/></pattern>
</defs>
"""

COMMON_STYLE = f"""
<style>
@font-face {{
  font-family: 'Orbitron';
  font-style: normal;
  font-weight: 900;
  src: url(data:font/woff2;base64,{orbitron_b64}) format('woff2');
}}
text {{ font-family: 'Fira Code', 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
.brand-orbitron {{ font-family: 'Orbitron', monospace, sans-serif; font-weight: 900; }}
.dim {{ fill: #6272a4; }}
.cy {{ fill: #00d9ff; }}
.fg {{ fill: #f8f8f2; }}
.gr {{ fill: #50fa7b; }}
.pk {{ fill: #ff79c6; }}
.pp {{ fill: #bd93f9; }}
.yl {{ fill: #f1fa8c; }}
@keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
@keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
@keyframes gm {{ 0%, 92%, 100% {{ transform: translate(0,0); }} 93% {{ transform: translate(3px,-1px); }} 95% {{ transform: translate(-2px,1px); }} 97% {{ transform: translate(1px,0); }} }}
@keyframes gc {{ 0%, 92%, 100% {{ transform: translate(0,0); }} 93% {{ transform: translate(-3px,1px); }} 95% {{ transform: translate(2px,-1px); }} 97% {{ transform: translate(-1px,0); }} }}
.cursor {{ animation: blink 1.05s step-end infinite; }}
.dot {{ animation: pulse 2s ease-in-out infinite; }}
.gm {{ animation: gm 5s linear 1s infinite; }}
.gc {{ animation: gc 5s linear 1s infinite; }}
@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>
"""

def generate_header():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="340" viewBox="0 0 880 340" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<!-- Outer Rails (x=16 and x=864) -->
<path d="M16 16V340M864 16V340M16 16H864" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".4" filter="url(#glow)"/>
<rect x="16" y="16" width="848" height="324" fill="#03040a"/>
<rect x="16" y="16" width="848" height="324" fill="url(#grid)"/>

<!-- Top Status Bar -->
<rect x="16" y="16" width="848" height="34" fill="#00d9ff" fill-opacity=".08"/>
<line x1="16" y1="50" x2="864" y2="50" stroke="#00d9ff" stroke-opacity=".4"/>
<text x="32" y="38" letter-spacing="1" class="cy" font-size="11.5">SYS://QUANTUM // NODE:QUANTUMTECHCODER</text>
<text x="844" y="38" letter-spacing="1" class="dim" text-anchor="end" font-size="11.5">ONLINE · ALL SYSTEMS NOMINAL</text>
<circle class="dot" cx="600" cy="34" r="4" fill="#50fa7b"/>
<circle class="dot" cx="600" cy="34" r="4" fill="#50fa7b" filter="url(#sglow)"/>

<!-- Terminal Command Prompt -->
<text x="52" y="94" class="dim" font-size="14.5"><tspan class="gr">$</tspan> whoami</text>

<!-- Embedded Base64 Orbitron Brand Title - NO SPACES -->
<g class="brand-orbitron" letter-spacing="2" font-size="46">
  <text x="52" y="156" fill="#00d9ff" opacity=".35" filter="url(#glow)">QuantumTechCoder</text>
  <g class="gm"><text x="54" y="156" fill="#ff79c6" opacity=".75">QuantumTechCoder</text></g>
  <g class="gc"><text x="50" y="156" fill="#00d9ff" opacity=".85">QuantumTechCoder</text></g>
  <text x="52" y="156" fill="#f8f8f2">QuantumTechCoder</text>
</g>

<!-- Bullet Subtitles -->
<text class="fg" x="52" y="202" font-size="14"><tspan class="cy">&gt;&gt;</tspan> Systems Explorer · Ethical Hacker · AI &amp; Full-Stack Architect</text>
<text class="fg" x="52" y="228" font-size="14"><tspan class="cy">&gt;&gt;</tspan> Low-level tinkerer, real-time WebRTC &amp; WebGL shader engineer</text>
<text class="fg" x="52" y="254" font-size="14"><tspan class="cy">&gt;&gt;</tspan> Building autonomous agents &amp; impossible developer tooling</text>

<!-- Prompt with Blinking Cursor -->
<text x="52" y="292" class="gr" font-size="15">$</text>
<rect class="cursor" x="70" y="278" width="10" height="18" fill="#00d9ff"/>
<rect class="cursor" x="70" y="278" width="10" height="18" fill="#00d9ff" filter="url(#sglow)"/>

<!-- Scanline Overlay -->
<rect x="16" y="51" width="848" height="289" fill="url(#scan)"/>
<path d="M16 16V340M864 16V340M16 16H864" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
<g fill="none" stroke="#00d9ff" stroke-width="2"><path d="M9 34V9H34"/><path d="M846 9H871V34"/></g>
</svg>"""

def generate_section(title: str, cmd: str, h: int = 90):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="{h}" viewBox="0 0 880 {h}" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<path d="M16 0V{h}M864 0V{h}" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".35" filter="url(#glow)"/>
<rect x="16" y="0" width="848" height="{h}" fill="#03040a"/>
<rect x="16" y="0" width="848" height="{h}" fill="url(#grid)"/>

<line x1="52" y1="16" x2="160" y2="16" stroke="#00d9ff" stroke-width="2" filter="url(#sglow)"/>
<text x="52" y="46" class="fg" font-weight="bold" font-size="18" letter-spacing="1">{title}</text>
<text x="52" y="72" class="dim" font-size="13"><tspan class="gr">$</tspan> {cmd}</text>

<path d="M16 0V{h}M864 0V{h}" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
</svg>"""

def generate_link_btn(icon: str, label: str, sub: str, pos: str, color: str = "#00d9ff"):
    # 5 buttons of width 176 each (5 * 176 = 880)
    # The left rail is at x=16, right rail at 176*4 + 160 = 864
    rail_svg = ""
    bg_svg = ""
    bx = 4
    bw = 168

    if pos == "first":
        # x=0..16 is TRANSPARENT, background starts at 16
        bg_svg = '<rect x="16" y="0" width="160" height="72" fill="#03040a"/>'
        rail_svg = '<path d="M16 0V72" fill="none" stroke="#00d9ff" stroke-width="1.2"/>'
        bx = 20
        bw = 152
    elif pos == "last":
        # x=160..176 is TRANSPARENT, background ends at 160
        bg_svg = '<rect x="0" y="0" width="160" height="72" fill="#03040a"/>'
        rail_svg = '<path d="M160 0V72" fill="none" stroke="#00d9ff" stroke-width="1.2"/>'
        bx = 4
        bw = 152
    else:
        bg_svg = '<rect x="0" y="0" width="176" height="72" fill="#03040a"/>'

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="176" height="72" viewBox="0 0 176 72" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
{bg_svg}
<rect x="{bx}" y="4" width="{bw}" height="64" rx="6" fill="#060a14" stroke="{color}" stroke-width="1.2" stroke-opacity=".75"/>
<circle cx="{bx + 20}" cy="36" r="12" fill="{color}" fill-opacity=".12"/>
<text x="{bx + 20}" y="41" text-anchor="middle" font-size="13">{icon}</text>
<text x="{bx + 38}" y="32" fill="#f8f8f2" font-weight="bold" font-size="12">{label}</text>
<text x="{bx + 38}" y="48" fill="{color}" font-size="9.5">{sub}</text>
{rail_svg}
</svg>"""

def generate_project_card(title: str, badge: str, desc1: str, desc2: str, tags: list, side: str, color: str = "#00d9ff"):
    # 2 cards of 440 each (2 * 440 = 880)
    # Left card: x=0..16 TRANSPARENT, rail at 16
    # Right card: x=424..440 TRANSPARENT, rail at 424 (440+424=864)
    rail_svg = ""
    bg_svg = ""
    bx = 6
    bw = 428

    if side == "left":
        bg_svg = '<rect x="16" y="0" width="424" height="180" fill="#03040a"/>'
        rail_svg = '<path d="M16 0V180" fill="none" stroke="#00d9ff" stroke-width="1.2"/>'
        bx = 22
        bw = 412
    else:
        bg_svg = '<rect x="0" y="0" width="424" height="180" fill="#03040a"/>'
        rail_svg = '<path d="M424 0V180" fill="none" stroke="#00d9ff" stroke-width="1.2"/>'
        bx = 6
        bw = 412

    tags_svg = ""
    tx = 0
    for t in tags:
        tw = len(t) * 7 + 16
        tags_svg += f"""
        <rect x="{tx}" y="0" width="{tw}" height="20" rx="4" fill="#08101e" stroke="#1d2e47" stroke-width="1"/>
        <text x="{tx + tw/2}" y="14" text-anchor="middle" fill="#8be9fd" font-size="10">{t}</text>
        """
        tx += tw + 8

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="440" height="180" viewBox="0 0 440 180" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
{bg_svg}
<rect x="{bx}" y="4" width="{bw}" height="172" rx="8" fill="#050811" stroke="{color}" stroke-width="1.2" stroke-opacity=".75"/>

<text x="{bx + 16}" y="34" fill="#ffffff" font-weight="bold" font-size="16">{title}</text>
<rect x="{bx + bw - 118}" y="18" width="106" height="22" rx="4" fill="{color}" fill-opacity=".12" stroke="{color}" stroke-width="1"/>
<text x="{bx + bw - 65}" y="33" text-anchor="middle" fill="{color}" font-weight="bold" font-size="9">{badge}</text>

<text x="{bx + 16}" y="66" fill="#a0aec0" font-size="12">{desc1}</text>
<text x="{bx + 16}" y="86" fill="#a0aec0" font-size="12">{desc2}</text>

<g transform="translate({bx + 16}, 128)">
{tags_svg}
</g>
{rail_svg}
</svg>"""

def generate_stack_panel():
    # Technical Arsenal completely enclosed inside the 880px boundary
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="250" viewBox="0 0 880 250" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<path d="M16 0V250M864 0V250" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".35" filter="url(#glow)"/>
<rect x="16" y="0" width="848" height="250" fill="#03040a"/>
<rect x="16" y="0" width="848" height="250" fill="url(#grid)"/>

<!-- Section Title -->
<line x1="52" y1="16" x2="160" y2="16" stroke="#00d9ff" stroke-width="2" filter="url(#sglow)"/>
<text x="52" y="44" class="fg" font-weight="bold" font-size="18" letter-spacing="1">Technical Arsenal &amp; Weapons</text>
<text x="52" y="68" class="dim" font-size="12.5"><tspan class="gr">$</tspan> cat ~/weapons.json</text>

<!-- Category Rows Inside Rails -->
<g transform="translate(36, 86)">
  <!-- Systems & Kernel -->
  <text x="16" y="20" class="cy" font-size="11" font-weight="bold">SYSTEMS &amp; KERNEL:</text>
  <g transform="translate(160, 4)" font-size="11">
    <rect x="0" y="0" width="65" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="32" y="15" text-anchor="middle" fill="#f8f8f2">Linux</text>
    <rect x="73" y="0" width="65" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="105" y="15" text-anchor="middle" fill="#f8f8f2">Debian</text>
    <rect x="146" y="0" width="60" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="176" y="15" text-anchor="middle" fill="#f8f8f2">Arch</text>
    <rect x="214" y="0" width="60" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="244" y="15" text-anchor="middle" fill="#00f7ff">Kali</text>
    <rect x="282" y="0" width="70" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="317" y="15" text-anchor="middle" fill="#f8f8f2">Docker</text>
    <rect x="360" y="0" width="85" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="402" y="15" text-anchor="middle" fill="#50fa7b">Kubernetes</text>
    <rect x="453" y="0" width="75" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="490" y="15" text-anchor="middle" fill="#ff79c6">Arduino</text>
    <rect x="536" y="0" width="105" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="588" y="15" text-anchor="middle" fill="#f1fa8c">Raspberry Pi</text>
  </g>

  <!-- Core Languages -->
  <text x="16" y="58" class="gr" font-size="11" font-weight="bold">LANGUAGES &amp; RUNTIMES:</text>
  <g transform="translate(160, 42)" font-size="11">
    <rect x="0" y="0" width="85" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="42" y="15" text-anchor="middle" fill="#3178c6">TypeScript</text>
    <rect x="93" y="0" width="80" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="133" y="15" text-anchor="middle" fill="#f7df1e">JavaScript</text>
    <rect x="181" y="0" width="65" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="213" y="15" text-anchor="middle" fill="#3572A5">Python</text>
    <rect x="254" y="0" width="55" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="281" y="15" text-anchor="middle" fill="#dea584">Rust</text>
    <rect x="317" y="0" width="55" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="344" y="15" text-anchor="middle" fill="#f34b7d">C++</text>
    <rect x="380" y="0" width="55" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="407" y="15" text-anchor="middle" fill="#e76f00">Java</text>
    <rect x="443" y="0" width="60" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="473" y="15" text-anchor="middle" fill="#512bd4">.NET</text>
    <rect x="511" y="0" width="65" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="543" y="15" text-anchor="middle" fill="#654ff0">Wasm</text>
  </g>

  <!-- Web, Edge & Cloud -->
  <text x="16" y="96" class="pk" font-size="11" font-weight="bold">WEB, EDGE &amp; CLOUD:</text>
  <g transform="translate(160, 80)" font-size="11">
    <rect x="0" y="0" width="65" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="32" y="15" text-anchor="middle" fill="#61dafb">React</text>
    <rect x="73" y="0" width="65" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="105" y="15" text-anchor="middle" fill="#f8f8f2">Next.js</text>
    <rect x="146" y="0" width="65" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="178" y="15" text-anchor="middle" fill="#ff3e00">Svelte</text>
    <rect x="219" y="0" width="75" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="256" y="15" text-anchor="middle" fill="#38bdf8">Tailwind</text>
    <rect x="302" y="0" width="70" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="337" y="15" text-anchor="middle" fill="#f8f8f2">Three.js</text>
    <rect x="380" y="0" width="85" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="422" y="15" text-anchor="middle" fill="#f38020">Cloudflare</text>
    <rect x="473" y="0" width="85" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="515" y="15" text-anchor="middle" fill="#336791">PostgreSQL</text>
    <rect x="566" y="0" width="75" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="603" y="15" text-anchor="middle" fill="#47a248">MongoDB</text>
  </g>

  <!-- AI & Reverse Engineering -->
  <text x="16" y="134" class="yl" font-size="11" font-weight="bold">AI &amp; REVERSE ENG:</text>
  <g transform="translate(160, 118)" font-size="11">
    <rect x="0" y="0" width="70" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="35" y="15" text-anchor="middle" fill="#f8f8f2">Ollama</text>
    <rect x="78" y="0" width="105" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="130" y="15" text-anchor="middle" fill="#00ff9f">Local LLMs</text>
    <rect x="191" y="0" width="65" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="223" y="15" text-anchor="middle" fill="#bd93f9">NumPy</text>
    <rect x="264" y="0" width="95" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="311" y="15" text-anchor="middle" fill="#ff79c6">Nmap/Zenmap</text>
    <rect x="367" y="0" width="65" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="399" y="15" text-anchor="middle" fill="#f8f8f2">Wireshark</text>
    <rect x="440" y="0" width="80" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="480" y="15" text-anchor="middle" fill="#00f7ff">Ghidra</text>
    <rect x="528" y="0" width="85" height="22" rx="4" fill="#08101e" stroke="#25354e" stroke-width="1"/><text x="570" y="15" text-anchor="middle" fill="#50fa7b">Antigravity</text>
  </g>
</g>

<path d="M16 0V250M864 0V250" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
</svg>"""

def generate_crypto_tip_jar():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="320" viewBox="0 0 880 320" role="img">
{COMMON_DEFS}
{COMMON_STYLE}
<path d="M16 0V320M864 0V320" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".35" filter="url(#glow)"/>
<rect x="16" y="0" width="848" height="320" fill="#03040a"/>
<rect x="16" y="0" width="848" height="320" fill="url(#grid)"/>

<!-- Frame inside x=36 to x=844 -->
<rect x="36" y="16" width="808" height="288" rx="10" fill="#060913" stroke="#00d9ff" stroke-width="1.2" stroke-opacity=".7"/>

<text x="60" y="52" fill="#ffffff" font-weight="bold" font-size="17">⚡ CRYPTO TIP JAR // MULTI-CHAIN EVM</text>
<text x="814" y="52" text-anchor="end" class="gr" font-size="11">● READY FOR TX</text>
<circle class="dot" cx="704" cy="48" r="3.5" fill="#50fa7b"/>

<line x1="60" y1="68" x2="820" y2="68" stroke="#1d2e47" stroke-width="1.2"/>
<text x="60" y="94" fill="#a0aec0" font-size="13">Fueling local GPU compute, late-night debugging marathons, and open-source tooling.</text>

<!-- Address Bar -->
<g transform="translate(60, 110)">
  <rect width="760" height="56" rx="8" fill="#020408" stroke="#00f7ff" stroke-width="1.2"/>
  <text x="18" y="21" fill="#6272a4" font-size="10">UNIVERSAL EVM ADDRESS (ONE ADDRESS FOR ALL CHAINS):</text>
  <text x="18" y="42" fill="#50fa7b" font-weight="bold" font-size="15">0x2cef0473f985156eDe84312Ce0BeB94B602d26E4</text>
  <rect x="670" y="14" width="70" height="28" rx="4" fill="#00d9ff" fill-opacity=".15" stroke="#00d9ff" stroke-width="1"/>
  <text x="705" y="32" text-anchor="middle" fill="#00f7ff" font-weight="bold" font-size="11">COPY</text>
</g>

<!-- Chains Support List -->
<text x="60" y="194" fill="#8be9fd" font-size="11" font-weight="bold">SUPPORTED BLOCKCHAINS &amp; LAYER 2s:</text>

<g transform="translate(60, 208)" font-size="11">
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

<text x="60" y="258" fill="#6272a4" font-size="11">ACCEPTED ASSETS: <tspan fill="#f8f8f2">ETH, BNB, POL, AVAX, ARB, OP, USDC, USDT, DAI, WETH, WBTC &amp; All ERC-20 / BEP-20 Tokens</tspan></text>
<text x="60" y="278" fill="#6272a4" font-size="10.5">🔒 Verified on <tspan fill="#00f7ff">Etherscan</tspan>, <tspan fill="#00f7ff">Basescan</tspan>, <tspan fill="#00f7ff">Arbiscan</tspan>, &amp; <tspan fill="#00f7ff">Polygonscan</tspan>. Low-gas L2 transfers warmly appreciated!</text>

<path d="M16 0V320M864 0V320" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
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

# Write all assets
(BASE / "header.svg").write_text(generate_header(), encoding="utf-8")
(BASE / "links.svg").write_text(generate_section("Links", "cat ~/.links"), encoding="utf-8")

# 5 Link buttons with boundary rail alignment
(LINKS_DIR / "web.svg").write_text(generate_link_btn("🌐", "Website", "quantumtechcoder", "first", "#00d9ff"), encoding="utf-8")
(LINKS_DIR / "dev.svg").write_text(generate_link_btn("✍️", "DEV.to", "Articles &amp; Posts", "mid", "#00ff9f"), encoding="utf-8")
(LINKS_DIR / "gh.svg").write_text(generate_link_btn("💻", "GitHub", "@QuantumTechCoder", "mid", "#bd93f9"), encoding="utf-8")
(LINKS_DIR / "discord.svg").write_text(generate_link_btn("💬", "Discord", "quantumtechcoder", "mid", "#ff79c6"), encoding="utf-8")
(LINKS_DIR / "vault.svg").write_text(generate_link_btn("⚡", "Tip Jar", "Crypto EVM", "last", "#f1fa8c"), encoding="utf-8")

(BASE / "telemetry.svg").write_text(generate_section("Live Telemetry &amp; Stats", "sysctl -a telemetry"), encoding="utf-8")
(BASE / "projects.svg").write_text(generate_section("Featured Systems &amp; Projects", "ls -la ~/projects"), encoding="utf-8")

# Project cards with boundary rail alignment
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

(BASE / "stack.svg").write_text(generate_stack_panel(), encoding="utf-8")
(BASE / "vault.svg").write_text(generate_section("Crypto Tip Jar", "tip --crypto --evm"), encoding="utf-8")
(BASE / "crypto_vault.svg").write_text(generate_crypto_tip_jar(), encoding="utf-8")
(BASE / "footer.svg").write_text(generate_footer(), encoding="utf-8")

print("All profile assets regenerated cleanly with embedded Orbitron and aligned boundary rails!")
