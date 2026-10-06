#!/usr/bin/env python3
"""
remove_wordle_connections.py

Removes all references and links to "Wordle" and "Connections" from:
- Navigation bars
- Footers
- Game selector dropdowns and next-puzzle cards
- Homepage game card grid
- sitemap.xml
"""

import os
import re
import sys

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    orig = content

    # 1. Remove <li> elements that contain links to wordle or connections
    content = re.sub(
        r'\s*<li><a\b[^>]*href=["\'][^"\']*(?:wordle|connections)[^"\']*["\'][^>]*>.*?</a></li>\s*',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 2. In index.html: remove the Connections game-card in the puzzle grid
    content = re.sub(
        r'\s*<a\b[^>]*href=["\']/games/connections/["\'][^>]*class=["\']game-card["\'][^>]*>.*?</a>\s*',
        '\n',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    # 3. In game hub pages: update the next-section cards
    # For Crossword index:
    if 'games' in filepath and 'crossword' in filepath and 'archive' not in filepath:
        crossword_next = """<div class="next-section" style="max-width:1100px;margin:0 auto;padding:0 clamp(16px,4vw,60px) 60px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;">
  <a href="/games/wordsearch/" class="next-card"><div class="next-card-label">Also today</div><div class="next-card-title">Word Search</div><div class="next-card-desc">Find hidden words in the daily letter grid.</div><div class="next-card-arrow">→</div></a>
  <a href="/games/sudoku/" class="next-card"><div class="next-card-label">Also today</div><div class="next-card-title">Sudoku</div><div class="next-card-desc">Fill every row, column, and 3×3 box.</div><div class="next-card-arrow">→</div></a>
  <a href="/games/trivia/" class="next-card"><div class="next-card-label">Also today</div><div class="next-card-title">Trivia</div><div class="next-card-desc">10 daily questions across mixed topics.</div><div class="next-card-arrow">→</div></a>
</div>"""
        content = re.sub(
            r'<div class="next-section".*?</div>\s*(?=<div class="refresh-toast"|<footer>)',
            crossword_next + '\n',
            content,
            flags=re.DOTALL
        )

    # For Sudoku index:
    if 'games' in filepath and 'sudoku' in filepath and 'archive' not in filepath:
        sudoku_next = """<div class="next-section" style="max-width:1100px;margin:0 auto;padding:0 clamp(16px,4vw,60px) 60px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;">
  <a href="/games/crossword/" class="next-card"><div class="next-card-label">Also today</div><div class="next-card-title">Crossword</div><div class="next-card-desc">Fill the 5×5 grid with across and down clues.</div><div class="next-card-arrow">→</div></a>
  <a href="/games/wordsearch/" class="next-card"><div class="next-card-label">Also today</div><div class="next-card-title">Word Search</div><div class="next-card-desc">Find hidden words in the daily letter grid.</div><div class="next-card-arrow">→</div></a>
  <a href="/games/trivia/" class="next-card"><div class="next-card-label">Also today</div><div class="next-card-title">Trivia</div><div class="next-card-desc">10 daily questions across mixed topics.</div><div class="next-card-arrow">→</div></a>
</div>"""
        content = re.sub(
            r'<div class="next-section".*?</div>\s*(?=<div class="refresh-toast"|<footer>)',
            sudoku_next + '\n',
            content,
            flags=re.DOTALL
        )

    # For Trivia index:
    if 'games' in filepath and 'trivia' in filepath and 'archive' not in filepath:
        trivia_next = """  <div class="next-section" style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:60px;">
    <a href="/games/crossword/" class="next-card"><div class="next-card-label">Also today</div><div class="next-card-title">Crossword</div><div class="next-card-desc">Fill the 5×5 grid with across and down clues.</div><div class="next-card-arrow">→</div></a>
    <a href="/games/wordsearch/" class="next-card"><div class="next-card-label">Also today</div><div class="next-card-title">Word Search</div><div class="next-card-desc">Find hidden words in the daily letter grid.</div><div class="next-card-arrow">→</div></a>
    <a href="/games/sudoku/" class="next-card"><div class="next-card-label">Also today</div><div class="next-card-title">Sudoku</div><div class="next-card-desc">Fill every row, column, and 3×3 box.</div><div class="next-card-arrow">→</div></a>
  </div>"""
        content = re.sub(
            r'\s*<div class="next-section".*?</div>\s*(?=</div>\s*<div class="refresh-toast")',
            '\n' + trivia_next + '\n',
            content,
            flags=re.DOTALL
        )

    # 4. In blog/2: remove next-card for connections
    if 'blog' in filepath and os.path.basename(filepath) == '2':
        content = re.sub(
            r'<!-- Connections Link -->\s*<a href="https://snappgrid.com/connections" class="next-card">.*?</a>\s*',
            '',
            content,
            flags=re.DOTALL
        )

    # Fallback removal for any remaining <a> linking to /games/wordle/ or /games/connections/ in nav or footer
    content = re.sub(
        r'<a\b[^>]*href=["\'][^"\']*(?:wordle|connections)[^"\']*["\'][^>]*>.*?</a>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
        return True
    return False


def clean_sitemap(sitemap_path):
    if not os.path.exists(sitemap_path):
        return
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    content = re.sub(
        r'\s*<url>\s*<loc>https://snappgrid\.com/games/connections/?(?:archive/)?</loc>.*?</url>',
        '',
        content,
        flags=re.DOTALL
    )

    if content != orig:
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated: sitemap.xml (removed connections URLs)")


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_files = [
        'index.html',
        'games/crossword/index.html',
        'games/crossword/archive/index.html',
        'games/sudoku/index.html',
        'games/sudoku/archive/index.html',
        'games/trivia/index.html',
        'games/trivia/archive/index.html',
        'games/wordsearch/index.html',
        'games/wordsearch/archive/index.html',
        'blog/2'
    ]

    for rel in target_files:
        full = os.path.join(base_dir, rel.replace('/', os.sep))
        if os.path.exists(full):
            process_file(full)

    clean_sitemap(os.path.join(base_dir, 'sitemap.xml'))

if __name__ == '__main__':
    main()
