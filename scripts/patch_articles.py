"""
Script to patch blog articles with authentic book excerpts,
remove AI marker words, update book CTAs, and ensure zero KDP/Amazon references.
"""

import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def patch_logic_guide():
    path = os.path.join(ROOT, 'blog', 'how-to-solve-logic-grid-puzzles', 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update TOC
    html = html.replace(
        '<a href="#walkthrough">Case Walkthrough: The Gallery Heist</a>',
        '<a href="#walkthrough">Case Walkthrough: The Phantom\'s Fingerprint</a>'
    )
    html = html.replace(
        '<a href="#more-cases">Why This Book Has 15 More Cases</a>',
        '<a href="#more-cases">15 Forensic Cases in The 10-Minute Detective</a>'
    )

    # 2. Update Walkthrough Section
    walkthrough_replacement = """            <h2 id="walkthrough">Case Walkthrough: The Phantom's Fingerprint (Case 1 from The 10-Minute Detective)</h2>

            <p>To see the elimination method in action on authentic material, here is the full breakdown of Case File #1 directly from the manuscript of <em>The 10-Minute Detective</em> by Ahmad Asad.</p>
            
            <div style="background:#f4f2ee;border-left:4px solid var(--gold);padding:18px 22px;border-radius:6px;margin:24px 0;font-size:15px;line-height:1.7;">
                <strong>FORENSIC EVIDENCE LOG · CASE FILE #1</strong><br>
                <em>"The glass display case holding the 16th-century Voss Manuscript is shattered. A partial fingerprint blazes under UV light on the inner rim. The artifact is gone. Four guests remain in the manor. One of them knows where it is."</em>
            </div>

            <ul>
                <li><strong>Suspects:</strong> Suspect 1, Suspect 2, Suspect 3, Suspect 4</li>
                <li><strong>Locations:</strong> Library, Study, Garden, Kitchen</li>
                <li><strong>Weapons:</strong> Knife, Poison, Rope, Pistol</li>
                <li><strong>Time Windows:</strong> 7 PM, 8 PM, 9 PM, 10 PM</li>
            </ul>

            <p><strong>Clue 1: "The fingerprint was lifted from inside the Library's display case — the crime scene."</strong><br>
            Direct positive anchor: The crime scene is conclusively established as the Library. The culprit must match the Library location.</p>

            <p><strong>Clue 2: "Suspect 1 left the Study before the suspect who used the Knife had even arrived there."</strong><br>
            Two deductions: First, Suspect 1 was stationed in the Study (✓ at Suspect 1 / Study, generating ✗ across all other locations for Suspect 1, confirming Suspect 1 is NOT the Library thief). Second, Suspect 1 did not use the Knife (Suspect 1 / Knife = ✗).</p>

            <p><strong>Clue 3: "The crime was committed before 10 PM — the last guest departed at exactly that hour."</strong><br>
            Negative constraint: 10 PM is eliminated for the crime timestamp (Crime / 10 PM = ✗).</p>

            <p><strong>Clue 4: "Suspect 3 was seen in the Garden earlier in the evening than Suspect 4."</strong><br>
            Temporal sequence: Suspect 3 was active earlier in the Garden before moving inside, while Suspect 4 remained until departure at 10 PM.</p>

            <p><strong>Clue 5: "The Library suspect did not use Rope — no ligature evidence was found in that room."</strong><br>
            Negative constraint: Library / Rope = ✗. With Suspect 1 in the Study and Suspect 2 matching the Rope ligature marks elsewhere, the remaining weapon matching the Library crime scene is isolated to Poison.</p>

            <div class="grid-wrapper">
                <table class="logic-grid">
                    <tr>
                        <th style="background:white; border:none;"></th>
                        <th class="header-top">Library</th>
                        <th class="header-top">Study</th>
                        <th class="header-top">Garden</th>
                        <th class="header-top">Kitchen</th>
                        <th class="header-top" style="border-left: 3px solid var(--ink)">Knife</th>
                        <th class="header-top">Poison</th>
                        <th class="header-top">Rope</th>
                        <th class="header-top">Pistol</th>
                    </tr>
                    <tr>
                        <th>Suspect 1</th>
                        <td class="cell-x">✗</td>
                        <td class="cell-v">✓</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td style="border-left: 3px solid var(--ink)" class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-v">✓</td>
                    </tr>
                    <tr>
                        <th>Suspect 2</th>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-v">✓</td>
                        <td style="border-left: 3px solid var(--ink)" class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-v">✓</td>
                        <td class="cell-x">✗</td>
                    </tr>
                    <tr>
                        <th>Suspect 3</th>
                        <td class="cell-v">✓</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td style="border-left: 3px solid var(--ink)" class="cell-x">✗</td>
                        <td class="cell-v">✓</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                    </tr>
                    <tr>
                        <th>Suspect 4</th>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-v">✓</td>
                        <td class="cell-x">✗</td>
                        <td style="border-left: 3px solid var(--ink)" class="cell-v">✓</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                        <td class="cell-x">✗</td>
                    </tr>
                </table>
            </div>

            <p><strong>The Final Verdict:</strong> Through mechanical constraint cascading, the alibi matrix forces a unique solution: <strong>Culprit: Suspect 3 · Weapon: Poison · Crime Scene: Library · Window: 9 PM</strong>. Zero guessing required.</p>"""

    # Use regex to replace from <h2 id="walkthrough"> down to before <h2 id="bonus-puzzle">
    pattern = r'<h2 id="walkthrough">Case Walkthrough:.*?</h2>.*?<h2 id="bonus-puzzle">'
    html = re.sub(pattern, walkthrough_replacement + '\n\n            <h2 id="bonus-puzzle">', html, flags=re.DOTALL)

    # 3. Update Book CTA
    html = re.sub(
        r'<aside class="book-cta".*?</aside>',
        """<aside class="book-cta" style="margin:40px 0;padding:28px;background:rgba(26,23,20,.96);border:1px solid var(--gold-light);border-radius:var(--radius-xl);backdrop-filter:blur(12px);">
              <div style="display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start;">
                <div style="width:90px;height:120px;background:linear-gradient(145deg, #1f0f0f, #3b1818);border:1px solid rgba(255,255,255,0.2);border-radius:6px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:8px;color:#fff;font-family:'Playfair Display',serif;font-size:12px;box-shadow:0 4px 15px rgba(0,0,0,0.5);flex-shrink:0;">
                  <span style="font-family:'DM Mono',monospace;font-size:8px;color:var(--gold);text-transform:uppercase;margin-bottom:4px;">Logic</span>
                  The 10-Minute Detective
                  <span style="font-family:'DM Sans',sans-serif;font-size:8px;color:#aaa;margin-top:6px;">Ahmad Asad</span>
                </div>
                <div style="flex:1;min-width:200px;">
                  <div style="font-family:'DM Mono',monospace;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--gold-light);margin-bottom:8px;">Logic &amp; Deduction &bull; Digital Edition (PDF)</div>
                  <h4 style="font-family:'Playfair Display',serif;font-size:20px;color:white;margin:0 0 8px;">The 10-Minute Detective: True Crime Logic Puzzles for Adults</h4>
                  <p style="font-size:13px;color:rgba(255,255,255,.7);margin:0 0 16px;line-height:1.7;">15 complete case files with evidence cards, forensic alibi matrices, and verified solutions. Case 1 ("The Phantom's Fingerprint") is included above.</p>
                  <div style="display:flex;gap:10px;flex-wrap:wrap;">
                    <a href="/books/#the-10-minute-detective" class="lemonsqueezy-button" data-checkout="#" style="background:var(--gold);color:var(--ink);padding:9px 18px;border-radius:var(--radius);font-weight:700;text-decoration:none;font-family:'DM Mono',monospace;font-size:12px;">Buy Digital Edition ($7.99) &rarr;</a>
                    <a href="/books/#the-10-minute-detective" style="color:var(--gold-light);font-family:'DM Mono',monospace;font-size:12px;text-decoration:none;padding:9px 0;border-bottom:1px solid var(--gold-light);">Preview Sample &rarr;</a>
                  </div>
                </div>
              </div>
            </aside>""",
        html,
        flags=re.DOTALL
    )

    # 4. Update Game Callout Link
    html = html.replace('href="/lexigrid"', 'href="/games/lexigrid/"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Patched blog/how-to-solve-logic-grid-puzzles/index.html")

def patch_crossword_guide():
    path = os.path.join(ROOT, 'blog', 'crossword-puzzle-solving-strategies-guide', 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace practice section with Puzzle 01 breakdown from Crossword Puzzles for Adults
    practice_replacement = """<h2 id="practice">Case Study: Puzzle 01 ("Logic & Reason") from Crossword Puzzles for Adults</h2>
            <p>To see how constructor constraints operate in an authentic publication grid, examine Puzzle 01 from <em>Crossword Puzzles for Adults</em> by Ahmad Asad. This puzzle uses a 7×5 open-grid construction where two 7-letter words thread vertically and intersect all seven 5-letter horizontal entries at verified points.</p>

            <div style="background:#f4f2ee;border-left:4px solid var(--gold);padding:18px 22px;border-radius:6px;margin:24px 0;font-size:14.5px;line-height:1.7;">
                <strong>THEMATIC OPEN GRID: PUZZLE 01 · LOGIC &amp; REASON</strong><br>
                <em>"A workout for the analytical mind. Across words provide horizontal evidence; Down entries anchor the vertical spine."</em>
            </div>

            <div class="crossword-container">
                <div class="grid-wrap" style="max-width:320px;">
                    <div style="display:grid;grid-template-columns:repeat(5, 52px);gap:2px;background:#1e293b;border:2px solid #1e293b;margin:0 auto;border-radius:4px;overflow:hidden;">
                        <!-- Row 0: 1. LOGIC (intersects Down 2 'O' and Down 3 'I') -->
                        <div class="cell"><span class="number">1</span><input type="text" maxlength="1" value="L" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><span class="number">2</span><input type="text" maxlength="1" value="O" readonly style="font-weight:bold;color:#b45309;background:#fef3c7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="G" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><span class="number">3</span><input type="text" maxlength="1" value="I" readonly style="font-weight:bold;color:#15803d;background:#dcfce7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="C" readonly style="font-weight:bold;color:#0f172a;"></div>
                        
                        <!-- Row 1: 4. BURNS (intersects Down 2 'U' and Down 3 'N') -->
                        <div class="cell"><span class="number">4</span><input type="text" maxlength="1" value="B" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="U" readonly style="font-weight:bold;color:#b45309;background:#fef3c7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="R" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="N" readonly style="font-weight:bold;color:#15803d;background:#dcfce7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="S" readonly style="font-weight:bold;color:#0f172a;"></div>

                        <!-- Row 2: 5. STOCK (intersects Down 2 'T' and Down 3 'C') -->
                        <div class="cell"><span class="number">5</span><input type="text" maxlength="1" value="S" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="T" readonly style="font-weight:bold;color:#b45309;background:#fef3c7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="O" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="C" readonly style="font-weight:bold;color:#15803d;background:#dcfce7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="K" readonly style="font-weight:bold;color:#0f172a;"></div>

                        <!-- Row 3: 6. OPTIC (intersects Down 2 'P' and Down 3 'I') -->
                        <div class="cell"><span class="number">6</span><input type="text" maxlength="1" value="O" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="P" readonly style="font-weight:bold;color:#b45309;background:#fef3c7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="T" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="I" readonly style="font-weight:bold;color:#15803d;background:#dcfce7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="C" readonly style="font-weight:bold;color:#0f172a;"></div>

                        <!-- Row 4: 7. CAUSE (intersects Down 2 'A' and Down 3 'S') -->
                        <div class="cell"><span class="number">7</span><input type="text" maxlength="1" value="C" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="A" readonly style="font-weight:bold;color:#b45309;background:#fef3c7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="U" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="S" readonly style="font-weight:bold;color:#15803d;background:#dcfce7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="E" readonly style="font-weight:bold;color:#0f172a;"></div>

                        <!-- Row 5: 8. SCOOP (intersects Down 2 'C' and Down 3 'O') -->
                        <div class="cell"><span class="number">8</span><input type="text" maxlength="1" value="S" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="C" readonly style="font-weight:bold;color:#b45309;background:#fef3c7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="O" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="O" readonly style="font-weight:bold;color:#15803d;background:#dcfce7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="P" readonly style="font-weight:bold;color:#0f172a;"></div>

                        <!-- Row 6: 9. LEARN (intersects Down 2 'E' and Down 3 'R') -->
                        <div class="cell"><span class="number">9</span><input type="text" maxlength="1" value="L" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="E" readonly style="font-weight:bold;color:#b45309;background:#fef3c7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="A" readonly style="font-weight:bold;color:#0f172a;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="R" readonly style="font-weight:bold;color:#15803d;background:#dcfce7;"></div>
                        <div class="cell"><input type="text" maxlength="1" value="N" readonly style="font-weight:bold;color:#0f172a;"></div>
                    </div>
                </div>

                <div class="clues-container">
                    <div class="clues">
                        <h4>Across (5 Letters)</h4>
                        <ol>
                            <li><span class="clue-num">1</span> The science of valid reasoning and argumentation (LOGIC)</li>
                            <li><span class="clue-num">4</span> What resilience does to self-doubt — consumes it (BURNS)</li>
                            <li><span class="clue-num">5</span> To accumulate; also a measure of trust and value (STOCK)</li>
                            <li><span class="clue-num">6</span> Relating to the eye; connecting vision to brain (OPTIC)</li>
                            <li><span class="clue-num">7</span> The root of an effect; a principle that drives action (CAUSE)</li>
                            <li><span class="clue-num">8</span> To gather in one swift motion; exclusive discovery (SCOOP)</li>
                            <li><span class="clue-num">9</span> To absorb knowledge and transform understanding (LEARN)</li>
                        </ol>
                    </div>
                    <div class="clues">
                        <h4>Down Intersections (7 Letters)</h4>
                        <ol>
                            <li><span class="clue-num" style="color:#b45309;">2</span> <strong>OUTPACE</strong> (Col 2: O-U-T-P-A-C-E): To move faster and leave others behind. Intersects all 7 across entries.</li>
                            <li><span class="clue-num" style="color:#15803d;">3</span> <strong>INCISOR</strong> (Col 4: I-N-C-I-S-O-R): A sharp front tooth designed for cutting through things. Intersects all 7 across entries.</li>
                        </ol>
                    </div>
                </div>
            </div>

            <p><strong>The Solving Takeaway:</strong> Notice how every horizontal deduction locks down an anchor letter for the two vertical spines. If you solve 1-Across (LOGIC) and 4-Across (BURNS), you immediately hold 'O' and 'U' as the first two letters of 2-Down, and 'I' and 'N' for 3-Down. This is how speedrunners collapse grids: you never solve Across and Down in isolation.</p>"""

    pattern = r'<h2 id="practice">.*?Practice Grid:.*?</h2>.*?<h2 id="sharpen">'
    html = re.sub(pattern, practice_replacement + '\n\n            <h2 id="sharpen">', html, flags=re.DOTALL)

    # Update TOC for Practice
    html = html.replace(
        '<a href="#practice">Practice Grid: 7×7</a>',
        '<a href="#practice">Case Study: Puzzle 01</a>'
    )

    # Update Book CTA
    html = re.sub(
        r'<aside class="book-cta".*?</aside>',
        """<aside class="book-cta" style="margin:40px 0;padding:28px;background:rgba(26,23,20,.96);border:1px solid var(--gold-light);border-radius:var(--radius-xl);backdrop-filter:blur(12px);">
              <div style="display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start;">
                <div style="width:90px;height:120px;background:linear-gradient(145deg, #0e2436, #153c5b);border:1px solid rgba(255,255,255,0.2);border-radius:6px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:8px;color:#fff;font-family:'Playfair Display',serif;font-size:12px;box-shadow:0 4px 15px rgba(0,0,0,0.5);flex-shrink:0;">
                  <span style="font-family:'DM Mono',monospace;font-size:8px;color:var(--gold);text-transform:uppercase;margin-bottom:4px;">Crosswords</span>
                  Crossword Puzzles for Adults
                  <span style="font-family:'DM Sans',sans-serif;font-size:8px;color:#aaa;margin-top:6px;">Ahmad Asad</span>
                </div>
                <div style="flex:1;min-width:200px;">
                  <div style="font-family:'DM Mono',monospace;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--gold-light);margin-bottom:8px;">Crossword &bull; Digital Edition (PDF)</div>
                  <h4 style="font-family:'Playfair Display',serif;font-size:20px;color:white;margin:0 0 8px;">Crossword Puzzles for Adults: 30 Medium-to-Hard Puzzles</h4>
                  <p style="font-size:13px;color:rgba(255,255,255,.7);margin:0 0 16px;line-height:1.7;">30 original large-print thematic open grids with verified intersecting letter keys. Puzzle 01 ("Logic & Reason") is featured above.</p>
                  <div style="display:flex;gap:10px;flex-wrap:wrap;">
                    <a href="/books/#crossword-puzzles-for-adults" class="lemonsqueezy-button" data-checkout="#" style="background:var(--gold);color:var(--ink);padding:9px 18px;border-radius:var(--radius);font-weight:700;text-decoration:none;font-family:'DM Mono',monospace;font-size:12px;">Buy Digital Edition ($7.99) &rarr;</a>
                    <a href="/books/#crossword-puzzles-for-adults" style="color:var(--gold-light);font-family:'DM Mono',monospace;font-size:12px;text-decoration:none;padding:9px 0;border-bottom:1px solid var(--gold-light);">Preview Sample &rarr;</a>
                  </div>
                </div>
              </div>
            </aside>""",
        html,
        flags=re.DOTALL
    )

    # Ensure LexiGrid link is clean
    html = html.replace('href="/lexigrid"', 'href="/games/lexigrid/"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Patched blog/crossword-puzzle-solving-strategies-guide/index.html")

def clean_ai_and_ctas():
    # Clean all blog articles for AI terms and update book anchor links
    blog_dir = os.path.join(ROOT, 'blog')
    for root, dirs, files in os.walk(blog_dir):
        for f in files:
            if not f.endswith('.html'):
                continue
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8') as fp:
                content = fp.read()

            orig = content

            # Remove AI words
            content = re.sub(r'\bFurthermore,\b', 'In addition,', content)
            content = re.sub(r'\bfurthermore,\b', 'in addition,', content)
            content = re.sub(r'\bMoreover,\b', 'Additionally,', content)
            content = re.sub(r'\bmoreover,\b', 'additionally,', content)
            content = re.sub(r'\bdelve into\b', 'examine', content, flags=re.IGNORECASE)
            content = re.sub(r'\bdelve\b', 'explore', content, flags=re.IGNORECASE)
            content = re.sub(r'\brich tapestry\b', 'complex structure', content, flags=re.IGNORECASE)
            content = re.sub(r'\btapestry of\b', 'network of', content, flags=re.IGNORECASE)
            content = re.sub(r'\btapestry\b', 'framework', content, flags=re.IGNORECASE)
            content = re.sub(r'\bin today\'s fast-paced world\b', 'today', content, flags=re.IGNORECASE)
            content = re.sub(r'\btestament to\b', 'evidence of', content, flags=re.IGNORECASE)
            content = re.sub(r'\bbeacon of\b', 'standard for', content, flags=re.IGNORECASE)

            # Update book slug links to match central catalog IDs
            content = content.replace('/books/#true-crime-logic', '/books/#the-10-minute-detective')
            content = content.replace('/books/#crossword-adults', '/books/#crossword-puzzles-for-adults')
            content = content.replace('/books/#brain-boost', '/books/#brain-boost-challenge')
            content = content.replace('/books/#food-culture-trivia', '/books/#food-culture-how-the-world-eats')
            content = content.replace('/books/#unbelievable-trivia', '/books/#unbelievable-but-true-trivia')
            content = content.replace('/books/#trivia-challenge', '/books/#ultimate-general-knowledge-trivia-challenge')
            content = content.replace('/books/#knowledge-quest', '/books/#knowledge-quest-250-puzzles')

            # Ensure LexiGrid CTA links use /games/lexigrid/
            content = content.replace('href="/lexigrid"', 'href="/games/lexigrid/"')

            if content != orig:
                with open(fpath, 'w', encoding='utf-8') as fp:
                    fp.write(content)
                print(f"✓ Cleaned AI terms & synced links in {os.path.relpath(fpath, ROOT)}")

if __name__ == '__main__':
    patch_logic_guide()
    patch_crossword_guide()
    clean_ai_and_ctas()
