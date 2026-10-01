#!/usr/bin/env python3
"""Generates profile-card.svg (neofetch-style GitHub profile card).
Edit the INFO section below, run:  python3 generate_card.py
No extra libraries needed."""
from html import escape

# ───────────────────────── EDIT HERE ─────────────────────────
HANDLE = "Pulya_or_Pulia@github"

INFO = [
    ("OS",                    "Windows / Linux"),
    ("Uptime",                "∞ years"),
    ("Host",                  "Student"),
    ("Kernel",                "Developer"),
    ("IDE",                   "IDE", "VS Code"),
    None,
    ("Languages.Programming", "Python, C++"),
    ("Languages.Computer",    "HTML, CSS, JSON"),
    ("Languages.Real",        "Uzbek, Russian, English"),
    None,
    ("Hobbies.Software",      "Programming, Open Source, Building Projects"),
    ("Hobbies.Hardware",      "PCs, Tech, Electronics"),
    ("Hobbies.Others",        "Learning, Exploring, Creating"),
    "Contact",
    ("Email",                 "pulyaa1998@mail.ru, puliaa1998@gmail.com"),
    ("Telegram",              "@pulya_or_pulia"),
    ("Instagram",             "@pulya_or_pulia"),
    ("Discord",               "@pulya_or_pulia"),
    "GitHub Stats",
    ("Repos",                 "8"),
    ("Stars",                 "5"),
    ("Commits",               "29"),
    ("Followers",             "1"),
]
# ─────────────────────────────────────────────────────────────

ART = r"""
######*=             +@@
@@@==*@@@  ++.  -+=  *@@  ++    =+- .=+*++:
@@@==*@@@ -@@+  %@@  *@@  #@@  +@@. =+==+@@%
@@@###*=  -@@+  %@@  *@@   %@%-@@-  #@@%%@@@
@@@        @@@+#@@@  *@@    @@@@+  :@@%=*@@@
===         +*+:-==  :==     @@#    .+*+:-==
                           @@@+

               -+++=.   -+= =+.
             -@@%+*@@%  %@@@**:
             %@@   *@@- %@@
             -@@%+*@@%  %@@
               -+*+=.   -==
     #######=                 =#######

  ######*=             #@%  *@@
  @@@==*@@% .++   =+-  %@@  =**  .=+*++:
  @@@==*@@% =@@-  @@@  %@@  #@@  -+==+@@%
  @@@###*-  =@@-  @@@  %@@  #@@  #@@%%@@@
  @@@       :@@%+#@@@  %@@  #@@  @@%=+@@@
  ==-        .+*+.-=-  -==  -==   +*+:-==
""".strip("\n").split("\n")

FS, CW, LH = 13, 7.8, 17          # font size, char width, line height
PAD, GAP, W = 28, 26, 58          # padding, gap between columns, right column chars
LW = max(len(l) for l in ART)
FONT = "'Fira Code','JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono','DejaVu Sans Mono',monospace"

def header(title):
    base = f"- {title} -"
    return base + "\u2500" * (W - len(base) - 3) + "-_-"

rows = [("h", header(HANDLE))]
for it in INFO:
    if it is None:
        rows.append(("dot", "."))
    elif isinstance(it, str):
        rows.append(("h", header(it)))
    else:
        k, v = it
        dots = max(2, W - 5 - len(k) - len(v))
        rows.append(("kv", (k, "." * dots, v)))

n = max(len(rows), len(ART))
width = round(PAD * 2 + LW * CW + GAP + W * CW)
height = PAD * 2 + n * LH
rx0 = PAD + LW * CW + GAP
art_off = (n - len(ART)) // 2

out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
out.append(f"""<style>
text{{font-family:{FONT};font-size:{FS}px;white-space:pre}}
.a{{fill:#c9d1d9}} .h{{fill:#c9d1d9}} .k{{fill:#ffa657}} .c{{fill:#c9d1d9}} .d{{fill:#6e7681}} .v{{fill:#a5d6ff}}
.l{{animation:in .45s ease both}}
@keyframes in{{from{{opacity:0;transform:translateX(-6px)}}to{{opacity:1;transform:none}}}}
.cur{{fill:#58a6ff;animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
</style>""")
out.append(f'<rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="12" fill="#0d1117" stroke="#30363d"/>')

for i, line in enumerate(ART):
    if not line.strip():
        continue
    y = PAD + (i + art_off + 1) * LH - 4
    out.append(f'<text class="a l" x="{PAD}" y="{y}" xml:space="preserve" style="animation-delay:{0.04*i:.2f}s">{escape(line)}</text>')

for i, (t, c) in enumerate(rows):
    y = PAD + (i + 1) * LH - 4
    d = f'style="animation-delay:{0.06*i+0.2:.2f}s"'
    if t == "h":
        out.append(f'<text class="h l" x="{rx0:.1f}" y="{y}" xml:space="preserve" {d}>{escape(c)}</text>')
    elif t == "dot":
        out.append(f'<text class="d l" x="{rx0:.1f}" y="{y}" {d}>.</text>')
    else:
        k, dots, v = c
        out.append(
            f'<text class="l" x="{rx0:.1f}" y="{y}" xml:space="preserve" {d}>'
            f'<tspan class="d">. </tspan><tspan class="k">{escape(k)}</tspan><tspan class="c">:</tspan>'
            f'<tspan class="d"> {dots} </tspan><tspan class="v">{escape(v)}</tspan></text>')

# blinking cursor under the art
cy = PAD + (n) * LH - 12
out.append(f'<rect class="cur" x="{PAD}" y="{cy}" width="{CW:.1f}" height="{LH-4}"/>')
out.append("</svg>")
open("profile-card.svg", "w", encoding="utf-8").write("\n".join(out))
print("profile-card.svg created:", width, "x", height)
