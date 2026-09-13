#!/usr/bin/env python3
"""Rebuild the profile with Python's standard library: python3 scripts/render_readme.py.

Edit ROWS to update the profile and assets/rose.txt to update the ASCII art.
The SVG contains text, with no external fonts, images, or dependencies.
"""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROWS = [
    ("section", "Professional", ""),
    ("field", "Current role", "DevOps Engineer"),
    ("field", "Certification", "Google Cloud"),
    ("field", "", "Professional Cloud DevOps Engineer"),
    ("field", "Remote from", "Goiânia - Goiás - Brazil"),
    ("blank", "", ""),
    ("section", "Open source projects", ""),
    ("field", "Contributing", "runtz.dev"),
    ("blank", "", ""),
    ("section", "Setup", ""),
    ("field", "Laptop", "Xiaomi Book Pro 2016"),
    ("field", "", "4K OLED / 16:10"),
    ("field", "Keyboard", "Keychron RK84 / tri-mode"),
    ("field", "Switches", "Sealsat Silent"),
    ("field", "Keycaps", "Ink Lotus Flowers PBT"),
    ("field", "Mouse", "Attack Shark X11 / tri-mode"),
    ("field", "Microphone", "Fifine A8"),
    ("field", "Headset", "Ugreen Max5c"),
    ("field", "Monitors", "2x Dell P2425H"),
    ("blank", "", ""),
    ("section", "Home lab", ""),
    ("field", "CPU", "Xeon E5-2697A / 16 cores / 32 threads"),
    ("field", "RAM", "64 GB DDR4"),
    ("field", "OS disk", "1x 512 GB NVMe"),
    ("field", "Extra disks", "2x 1 TB SSD"),
    ("field", "OS", "Ubuntu Server 26.04 LTS"),
    ("field", "Kubernetes", "kubeadm / tainted"),
    ("field", "Exposure", "Cloudflare Tunnel"),
    ("field", "Ingress", "STRRL/"),
    ("field", "", "cloudflare-tunnel-ingress-controller"),
    ("field", "Storage", "OpenEBS"),
    ("field", "Network", "Flannel"),
]


def main():
    rose = (ROOT / "assets/rose.txt").read_text().splitlines()
    assert all(line.isascii() for line in rose), "The rose must use ASCII characters."
    art_width = max(map(len, rose))
    assert art_width <= 64

    width, height = 1120, 864
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">DevOps Engineer — screenfetch profile</title>',
        '<desc id="desc">An ASCII rose on the left. Professional experience, desk setup, home lab, and open source contributions on the right.</desc>',
        '<rect x="0.5" y="0.5" width="1119" height="863" rx="14" fill="#0d1117" stroke="#30363d"/>',
        '<path d="M1 48H1119" stroke="#21262d"/>',
        '<g font-family="DejaVu Sans Mono, Liberation Mono, Consolas, monospace" font-size="13" fill="#c9d1d9">',
        '<text x="560" y="29" text-anchor="middle" fill="#8b949e" font-size="11">profile ~ screenfetch</text>',
        '<text x="30" y="82"><tspan fill="#7ee787">~</tspan><tspan fill="#8b949e"> $ </tspan><tspan>screenfetch</tspan></text>',
    ]
    for i, line in enumerate(rose):
        parts.append(f'<text x="30" y="{216 + i * 12.8:g}" font-size="10.5" xml:space="preserve" fill="#e6edf3">{escape(line)}</text>')

    for i, (kind, label, value) in enumerate(ROWS):
        y = 125 + i * 20
        if kind == "blank":
            continue
        if kind == "section":
            parts.append(f'<text x="478" y="{y}" fill="#00FFB8" font-weight="bold">-- {escape(label)}</text>')
        else:
            if label:
                parts.append(f'<text x="478" y="{y}" fill="#00FFB8">{escape(label)}:</text>')
            parts.append(f'<text x="596" y="{y}">{escape(value)}</text>')

    parts.append('</g>')
    parts.append('</svg>')
    (ROOT / 'assets/screenfetch.svg').write_text('\n'.join(parts) + '\n')

    readme = '\n'.join([
        '<!-- Edit scripts/render_readme.py and run python3 scripts/render_readme.py to update this profile. -->',
        '',
        '<p align="center">',
        '  <img src="./assets/screenfetch.svg" width="1120" alt="Screenfetch profile: an ASCII rose beside my DevOps role, certification, setup, home lab, and open source contribution.">',
        '</p>',
        '',
    ])
    (ROOT / 'README.md').write_text(readme)
    print(f'Generated README.md and assets/screenfetch.svg; rose: {art_width} columns × {len(rose)} lines.')


if __name__ == '__main__':
    main()
