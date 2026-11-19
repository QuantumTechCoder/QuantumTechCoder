import os
import json
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

USER = "QuantumTechCoder"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

headers = {"User-Agent": "Mozilla/5.0"}
if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"

# 1. Fetch User Data
user_url = f"https://api.github.com/users/{USER}"
req = urllib.request.Request(user_url, headers=headers)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        user_data = json.loads(resp.read().decode("utf-8"))
except Exception as e:
    print(f"User API error: {e}")
    user_data = {"public_repos": 16, "followers": 6}

# 2. Fetch Repos for stars & languages
repos_url = f"https://api.github.com/users/{USER}/repos?per_page=100"
req2 = urllib.request.Request(repos_url, headers=headers)
try:
    with urllib.request.urlopen(req2, timeout=10) as resp:
        repos = json.loads(resp.read().decode("utf-8"))
except Exception as e:
    print(f"Repos API error: {e}")
    repos = []

total_stars = sum(r.get("stargazers_count", 0) for r in repos) if repos else 9
total_forks = sum(r.get("forks_count", 0) for r in repos) if repos else 2
public_repos = user_data.get("public_repos", len(repos) or 16)

# 3. Contributions GraphQL query if token available
contributions = 2177
commits = 110
prs = 10
streak_days = 6

if TOKEN:
    query = """
    query($user: String!) {
      user(login: $user) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
          }
          totalCommitContributions
          totalPullRequestContributions
        }
      }
    }
    """
    gql_req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": {"user": USER}}).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    try:
        with urllib.request.urlopen(gql_req, timeout=10) as gresp:
            gdata = json.loads(gresp.read().decode("utf-8"))
            cc = gdata.get("data", {}).get("user", {}).get("contributionsCollection", {})
            total_c = cc.get("contributionCalendar", {}).get("totalContributions")
            if total_c:
                contributions = total_c
            commits = cc.get("totalCommitContributions", commits)
            prs = cc.get("totalPullRequestContributions", prs)
    except Exception as e:
        print(f"GraphQL error: {e}")

now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# 4. Generate assets/stats.svg with fixed bounds
stats_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="880" height="230" viewBox="0 0 880 230" role="img">
<defs>
<pattern id="statGrid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#00d9ff" stroke-opacity=".05"/></pattern>
<filter id="sglow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600;700&amp;display=swap');
text {{ font-family: 'Fira Code', 'JetBrains Mono', monospace; }}
.dim {{ fill: #6272a4; }}
.fg {{ fill: #f8f8f2; }}
.cy {{ fill: #00d9ff; }}
.gr {{ fill: #50fa7b; }}
.pk {{ fill: #ff79c6; }}
.yl {{ fill: #f1fa8c; }}
</style>

<!-- Outer Rails and Transparent Margins (x=0..16 & x=864..880 are transparent) -->
<path d="M16 0V230M864 0V230" fill="none" stroke="#00d9ff" stroke-width="2.5" opacity=".35" filter="url(#sglow)"/>
<rect x="16" y="0" width="848" height="230" fill="#03040a"/>
<rect x="16" y="0" width="848" height="230" fill="url(#statGrid)"/>

<!-- 4 Telemetry Metric Boxes -->
<g transform="translate(36, 14)">
  <!-- Box 1: Contributions -->
  <rect x="0" y="0" width="190" height="92" rx="8" fill="#060a14" stroke="#00d9ff" stroke-width="1.2" stroke-opacity=".7"/>
  <text x="18" y="26" class="dim" font-size="10.5">CONTRIBUTIONS</text>
  <text x="18" y="60" fill="#00d9ff" font-weight="bold" font-size="24">{contributions:,}</text>
  <text x="18" y="78" fill="#6272a4" font-size="9.5">ALL-TIME CONTRIBUTIONS</text>

  <!-- Box 2: Commits & PRs -->
  <rect x="206" y="0" width="190" height="92" rx="8" fill="#060a14" stroke="#50fa7b" stroke-width="1.2" stroke-opacity=".7"/>
  <text x="224" y="26" class="dim" font-size="10.5">COMMITS &amp; PRS</text>
  <text x="224" y="60" fill="#50fa7b" font-weight="bold" font-size="18.5">{commits} Commits · {prs} PRs</text>
  <text x="224" y="78" fill="#6272a4" font-size="9.5">PRODUCTION PIPELINE</text>

  <!-- Box 3: Streak -->
  <rect x="412" y="0" width="190" height="92" rx="8" fill="#060a14" stroke="#ff79c6" stroke-width="1.2" stroke-opacity=".7"/>
  <text x="430" y="26" class="dim" font-size="10.5">ACTIVITY VELOCITY</text>
  <text x="430" y="60" fill="#ff79c6" font-weight="bold" font-size="20">🔥 {streak_days} Days Streak</text>
  <text x="430" y="78" fill="#6272a4" font-size="9.5">ACTIVE STREAK</text>

  <!-- Box 4: Stars & Repos (Compact, Guaranteed Inside Box) -->
  <rect x="618" y="0" width="190" height="92" rx="8" fill="#060a14" stroke="#f1fa8c" stroke-width="1.2" stroke-opacity=".7"/>
  <text x="636" y="26" class="dim" font-size="10.5">REPOSITORIES</text>
  <text x="636" y="60" fill="#f1fa8c" font-weight="bold" font-size="18">⭐ {total_stars} Stars · {public_repos} Repos</text>
  <text x="636" y="78" fill="#6272a4" font-size="9.5">PUBLIC OPEN-SOURCE</text>
</g>

<!-- Languages Breakdown Bar -->
<g transform="translate(36, 122)">
  <rect width="808" height="84" rx="8" fill="#050811" stroke="#1d2e47" stroke-width="1"/>
  <text x="18" y="24" fill="#8be9fd" font-size="11" font-weight="bold">TOP SYSTEM STACKS &amp; RATIOS:</text>
  <text x="790" y="24" text-anchor="end" fill="#6272a4" font-size="9">// synced: {now_str}</text>
  
  <rect x="18" y="36" width="772" height="10" rx="5" fill="#141c2b"/>
  <rect x="18" y="36" width="280" height="10" rx="5" fill="#3178c6"/> <!-- TS -->
  <rect x="298" y="36" width="210" height="10" rx="0" fill="#3572A5"/> <!-- Python -->
  <rect x="508" y="36" width="130" height="10" rx="0" fill="#f7df1e"/> <!-- JS -->
  <rect x="638" y="36" width="80" height="10" rx="0" fill="#e34c26"/> <!-- HTML -->
  <rect x="718" y="36" width="72" height="10" rx="5" fill="#dea584"/> <!-- Rust/C++ -->

  <!-- Legend -->
  <g transform="translate(18, 66)" font-size="10">
    <circle cx="5" cy="-4" r="3.5" fill="#3178c6"/>
    <text x="14" y="0" class="fg">TypeScript 36%</text>

    <circle cx="160" cy="-4" r="3.5" fill="#3572A5"/>
    <text x="170" y="0" class="fg">Python 27%</text>

    <circle cx="290" cy="-4" r="3.5" fill="#f7df1e"/>
    <text x="300" y="0" class="fg">JavaScript 17%</text>

    <circle cx="430" cy="-4" r="3.5" fill="#e34c26"/>
    <text x="440" y="0" class="fg">HTML 10%</text>

    <circle cx="530" cy="-4" r="3.5" fill="#dea584"/>
    <text x="540" y="0" class="fg">Rust / C++ 10%</text>
  </g>
</g>

<path d="M16 0V230M864 0V230" fill="none" stroke="#00d9ff" stroke-width="1.2"/>
</svg>"""

out_file = Path("profile_repo/assets/stats.svg")
out_file.parent.mkdir(parents=True, exist_ok=True)
out_file.write_text(stats_svg, encoding="utf-8")
print(f"Stats SVG generated at {out_file}")
