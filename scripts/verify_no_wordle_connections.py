#!/usr/bin/env python3
"""
verify_no_wordle_connections.py

Verifies that zero references or links to "Wordle" and "Connections" remain in:
1. Navigation bars (<nav>, .nav-links, .navbar, .site-nav)
2. Dropdown menus (.dropdown, .dropdown-content)
3. Footers (<footer>, .footer-links, .footer-inner, .footer-content)
4. Game selector cards/grids (.next-section, .game-card, .play-grid)
5. Any <a> href across all HTML files
"""

import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = sorted(glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True))

print("=== VERIFYING REMOVAL OF WORDLE & CONNECTIONS ===")

total_violations = 0

for f in html_files:
    rel = os.path.relpath(f, base_dir)
    if 'google' in rel:
        continue

    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()

    file_violations = []

    # 1. Check all <nav> blocks
    nav_blocks = re.findall(r'<nav\b[^>]*>.*?</nav>', c, re.DOTALL | re.IGNORECASE)
    for i, n in enumerate(nav_blocks):
        if re.search(r'\b(?:wordle|connections)\b', n, re.IGNORECASE):
            file_violations.append(f"<nav> #{i+1} contains Wordle/Connections")

    # 2. Check all <header> blocks
    header_blocks = re.findall(r'<header\b[^>]*>.*?</header>', c, re.DOTALL | re.IGNORECASE)
    for i, h in enumerate(header_blocks):
        if re.search(r'\b(?:wordle|connections)\b', h, re.IGNORECASE):
            file_violations.append(f"<header> #{i+1} contains Wordle/Connections")

    # 3. Check all <footer> blocks
    footer_blocks = re.findall(r'<footer\b[^>]*>.*?</footer>', c, re.DOTALL | re.IGNORECASE)
    for i, foot in enumerate(footer_blocks):
        if re.search(r'\b(?:wordle|connections)\b', foot, re.IGNORECASE):
            file_violations.append(f"<footer> #{i+1} contains Wordle/Connections")

    # 4. Check all dropdowns or next-sections or game cards
    card_blocks = re.findall(r'<(?:div|section)\b[^>]*class=["\'][^"\']*(?:next-section|game-card|dropdown|play-grid)[^"\']*["\'][^>]*>.*?</(?:div|section)>', c, re.DOTALL | re.IGNORECASE)
    for i, cb in enumerate(card_blocks):
        if re.search(r'\b(?:wordle|connections)\b', cb, re.IGNORECASE):
            file_violations.append(f"Game card/dropdown #{i+1} contains Wordle/Connections")

    # 5. Check any <a> tag with href containing wordle or connections
    bad_links = re.findall(r'<a\b[^>]*href=["\'][^"\']*(?:wordle|connections)[^"\']*["\'][^>]*>.*?</a>', c, re.DOTALL | re.IGNORECASE)
    if bad_links:
        for bl in bad_links:
            file_violations.append(f"Link pointing to wordle/connections: {bl.strip()[:80]}")

    if file_violations:
        total_violations += len(file_violations)
        print(f"[FAIL] {rel}:")
        for v in file_violations:
            print(f"       - {v}")
    else:
        print(f"[CLEAN] {rel}")

print(f"\nVerification complete: {total_violations} violation(s) found.")
if total_violations == 0:
    print("SUCCESS: Zero occurrences of Wordle and Connections in navigation, headers, footers, or game links!")
else:
    sys.exit(1)
