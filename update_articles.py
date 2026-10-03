import re, json

def process_article(file_path, cat, short_title, svg_path, svg_alt, diagram_placement_regex, book_slug, book_title, book_price, book_genre, book_blurb, related_articles, expanded_content, expanded_placement_regex):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Breadcrumb
    breadcrumb = f"""<nav class="breadcrumb" aria-label="Breadcrumb" style="padding:12px 0;margin-bottom:20px;">
  <ol style="list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:4px;align-items:center;font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.5px;">
    <li><a href="/" style="color:var(--gold);text-decoration:none;">Home</a></li>
    <li style="color:var(--border-strong);">&nbsp;/&nbsp;</li>
    <li><a href="/blog/" style="color:var(--gold);text-decoration:none;">Blog</a></li>
    <li style="color:var(--border-strong);">&nbsp;/&nbsp;</li>
    <li style="color:var(--ink-muted);">{cat}</li>
    <li style="color:var(--border-strong);">&nbsp;/&nbsp;</li>
    <li style="color:var(--ink-soft);font-weight:600;">{short_title}</li>
  </ol>
</nav>
"""
    content = re.sub(r'(<h1[^>]*>)', breadcrumb + r'\1', content, count=1)

    # 2. LexiGrid callout (after 2nd H2)
    lexigrid = """<aside style="margin:36px 0;padding:24px;background:linear-gradient(135deg,#0f172a,#1e293b);border-radius:16px;border:1px solid rgba(129,140,248,.3);display:flex;align-items:center;gap:20px;flex-wrap:wrap;">
  <div style="font-size:40px;">&#9889;</div>
  <div style="flex:1;min-width:200px;">
    <div style="font-family:'DM Mono',monospace;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#818cf8;margin-bottom:6px;">Sharp Your Brain Right Now</div>
    <h4 style="font-family:'Playfair Display',serif;font-size:18px;color:white;margin:0 0 6px;">Play LexiGrid Daily Challenge</h4>
    <p style="font-size:13px;color:rgba(255,255,255,.65);margin:0;">Word swipe game built on pattern recognition and vocabulary recall &mdash; exactly the skills this article builds. Free, browser-based, no download.</p>
  </div>
  <a href="/lexigrid" style="background:#4f46e5;color:white;padding:10px 20px;border-radius:10px;font-weight:700;text-decoration:none;font-family:'DM Mono',monospace;font-size:12px;white-space:nowrap;">Play Free &rarr;</a>
</aside>
"""
    h2_matches = list(re.finditer(r'<h2[^>]*>.*?</h2>', content))
    if len(h2_matches) >= 2:
        pos = h2_matches[1].end()
        content = content[:pos] + '\n' + lexigrid + content[pos:]
        
    h2_matches = list(re.finditer(r'<h2[^>]*>.*?</h2>', content))

    # 3. Book CTA (after 5th H2)
    book_cta = f"""<aside style="margin:40px 0;padding:28px;background:rgba(26,23,20,.96);border:1px solid #E8C86E;border-radius:16px;">
  <div style="display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start;">
    <img src="/assets/images/books/book-{book_slug}.svg" alt="{book_title} book cover" width="100" height="130" style="border-radius:6px;flex-shrink:0;" loading="lazy">
    <div style="flex:1;min-width:200px;">
      <div style="font-family:'DM Mono',monospace;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#E8C86E;margin-bottom:8px;">{book_genre} &bull; PDF / Printable</div>
      <h4 style="font-family:'Playfair Display',serif;font-size:20px;color:white;margin:0 0 8px;">{book_title}</h4>
      <p style="font-size:13px;color:rgba(255,255,255,.7);margin:0 0 16px;line-height:1.7;">{book_blurb}</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <a href="/books/#{book_slug}" style="background:#C8930A;color:#1A1714;padding:9px 18px;border-radius:6px;font-weight:700;text-decoration:none;font-family:'DM Mono',monospace;font-size:12px;">Buy Digital Edition ({book_price}) &rarr;</a>
        <a href="/books/#{book_slug}" style="color:#E8C86E;font-family:'DM Mono',monospace;font-size:12px;text-decoration:none;padding:9px 0;border-bottom:1px solid #E8C86E;">Preview Sample &rarr;</a>
      </div>
    </div>
  </div>
</aside>
"""
    if len(h2_matches) >= 5:
        pos = h2_matches[4].end()
        content = content[:pos] + '\n' + book_cta + content[pos:]

    # 4. Related articles
    cards = []
    for url, rcat, length, title, hook in related_articles:
        cards.append(f"""<a href="{url}" style="display:block;text-decoration:none;border:1px solid #E0DAD0;border-radius:10px;padding:18px;background:#FDFAF5;transition:border-color .2s;" onmouseover="this.style.borderColor='#C8930A'" onmouseout="this.style.borderColor='#E0DAD0'">
  <div style="font-family:'DM Mono',monospace;font-size:9px;letter-spacing:1.5px;text-transform:uppercase;color:#C8930A;margin-bottom:8px;">{rcat} &bull; {length}</div>
  <h4 style="font-family:'Playfair Display',serif;font-size:15px;font-weight:700;color:#1A1714;margin:0 0 8px;line-height:1.35;">{title}</h4>
  <p style="font-size:12px;color:#7A7570;margin:0;">{hook}</p>
</a>""")
    related_html = f"""<section style="margin-top:56px;padding-top:40px;border-top:2px solid #E0DAD0;">
  <h3 style="font-family:'DM Mono',monospace;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#C8930A;margin-bottom:24px;">Related Guides</h3>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;">
    {chr(10).join(cards)}
  </div>
</section>
"""
    if '</article>' in content:
        content = content.replace('</article>', related_html + '\n</article>')
    elif '</main>' in content:
        content = content.replace('</main>', related_html + '\n</main>')

    # 5. BreadcrumbList JSON-LD
    json_ld_addition = f""",
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://snappgrid.com/" }},
            {{ "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://snappgrid.com/blog/" }},
            {{ "@type": "ListItem", "position": 3, "name": "{cat}", "item": "https://snappgrid.com/blog/category/{cat.lower().replace(' & ', '-').replace(' ', '-')}/" }},
            {{ "@type": "ListItem", "position": 4, "name": "{short_title}", "item": "https://snappgrid.com/blog/{file_path.split('/')[-2]}/" }}
          ]
        }}"""
    
    if '"@graph": [' in content:
        content = re.sub(r'(\s*\]\s*\}\s*</script>)', json_ld_addition + r'\1', content)
    else:
        content = re.sub(r'(\s*\]\s*</script>)', json_ld_addition + r'\1', content)

    # 6. Embed SVG diagram
    svg_html = f"""<figure style="margin:32px 0;">
  <img src="{svg_path}" alt="{svg_alt}" style="width:100%;height:auto;display:block;">
  <figcaption style="font-family:'DM Mono',monospace;font-size:12px;color:#7A7570;text-align:center;margin-top:12px;">{svg_alt}</figcaption>
</figure>
"""
    if diagram_placement_regex:
        content = re.sub(diagram_placement_regex, r'\g<0>\n' + svg_html, content, count=1)
        
    # Expanded content
    if expanded_content and expanded_placement_regex:
        content = re.sub(expanded_placement_regex, r'\g<0>\n' + expanded_content, content, count=1)

    with open(file_path + '.mod', 'w', encoding='utf-8') as f:
        f.write(content)

# Article 4
process_article(
    'd:/snappgrid-main/blog/science-of-trivia-memory-recall/index.html',
    'Trivia & Knowledge', 'Cognitive Science of Pub Quiz Mastery',
    '/assets/images/blog/memory-dual-coding.svg', 'Dual-coding memory architecture diagram showing encode, store, and retrieve stages for trivia recall',
    r'<h2 id="intro">.*?</h2>\s*<p>.*?</p>\s*<p>.*?</p>\s*<p>.*?</p>',
    'trivia-challenge', 'The Ultimate General Knowledge Trivia Challenge', '$6.99', 'Trivia',
    '420 questions across 12 subjects — history, science, geography, pop culture. Multiple choice, true/false, and quick-fire formats with score tracker.',
    [
        ('/blog/world-history-trivia-memorization-techniques/', 'Trivia & Knowledge', '14 min', 'World History Trivia Memorization Techniques', 'The chronological peg system that makes historical dates stick permanently.'),
        ('/blog/brain-training-neuroplasticity-puzzle-science/', 'Brain Health', '15 min', 'Beyond the Lumosity Hype', 'The neuroscience of cognitive reserve — why trivia practice is genuinely protective.'),
        ('/blog/science-trivia-facts-and-mnemonics/', 'Trivia & Knowledge', '14 min', 'Science Trivia Facts and Mnemonics', 'STEM fact clusters, periodic table memory tricks, and high-frequency physics laws.')
    ],
    '''<h2>The Associative Anchor Chain System</h2>
<p>The world's best pub quiz players do not have exceptional raw memory capacity. They have exceptional <em>association density</em>. Every fact in their mental library is linked to at least two other facts — a topic anchor and a sensory or emotional hook.</p>
<p>Here is the system. For any fact you want to retain: (1) state the fact aloud, (2) identify the category it belongs to, (3) invent a concrete visual that links the two. The visual does not need to be logical — it needs to be vivid and slightly absurd. The stranger the image, the stronger the encoding.</p>
<p>Example: The speed of light is 299,792,458 metres per second. Category: physics. Anchor image: a light bulb running a marathon at nearly 300 million metres per second and checking a watch that shows "299." Now the number 299 is retrievable via the image. The image is retrievable via the category tag "physics/speed." That is an associative anchor chain with two retrieval paths.</p>
<p>Apply this system during your reading sessions, not as a separate memorisation exercise. When you encounter a new trivia fact in a book like <em>The Ultimate General Knowledge Trivia Challenge</em>, pause for 8 seconds and build the chain before moving on. At 420 questions in that book, 8 seconds per fact costs just under an hour across the entire volume — and it converts passive reading into active, retrievable knowledge.</p>''',
    r'<h2 id="random-facts">.*?</h2>'
)

# Article 5
process_article(
    'd:/snappgrid-main/blog/world-history-trivia-memorization-techniques/index.html',
    'Trivia & Knowledge', 'World History Memorization Techniques',
    '/assets/images/blog/history-timeline-peg.svg', 'World history chronological peg system timeline from ancient Sumerian writing to the fall of the Berlin Wall',
    r'<h2 id="predictable-patterns">.*?</h2>',
    'forbidden-history', 'Forbidden History', '$6.99', 'Trivia',
    '630 questions covering suppressed stories, cover-ups, and the historical events that never made it into textbooks. 14 chapters of dark history.',
    [
        ('/blog/science-of-trivia-memory-recall/', 'Trivia & Knowledge', '16 min', 'Cognitive Science of Pub Quiz Mastery', 'The dual-coding and anchor chain system that makes historical dates stick.'),
        ('/blog/geography-trivia-mnemonics-guide/', 'Trivia & Knowledge', '13 min', 'Geography Trivia Mnemonics Guide', 'Spatial memory and route associations for countries, capitals, and borders.'),
        ('/blog/science-trivia-facts-and-mnemonics/', 'Trivia & Knowledge', '14 min', 'STEM Trivia Facts and Mnemonics', 'The same peg system applied to scientific discoveries and periodic table facts.')
    ],
    '''<h2>The Chronological Peg System: Ancient to Contemporary</h2>
<p>A peg system works by pre-loading your memory with a numbered scaffold. For history, the scaffold is centuries. Once the scaffold is in place, new facts hang on existing pegs rather than floating loose in undifferentiated memory.</p>
<p>Here are your primary history pegs:</p>
<ul style="line-height:2;">
  <li><strong>Before 500 BC — Classical Antiquity:</strong> Anchor image: a Greek column with a scroll. Pegged facts: Sumerian writing (~3000 BC), First Olympics (776 BC), Socrates (470–399 BC).</li>
  <li><strong>500 BC–500 AD — Imperial Age:</strong> Anchor image: an eagle carrying a shield. Pegged: Alexander the Great (356–323 BC), Julius Caesar (100–44 BC), Fall of Rome (476 AD).</li>
  <li><strong>500–1500 — Medieval:</strong> Anchor image: a knight in a castle. Pegged: Battle of Hastings (1066), Magna Carta (1215), Black Death (1347–1351).</li>
  <li><strong>1500–1800 — Exploration &amp; Revolution:</strong> Anchor image: a sailing ship with a compass. Pegged: Columbus (1492), Galileo (1564–1642), American Independence (1776).</li>
  <li><strong>1800–1945 — Industrial &amp; World Wars:</strong> Anchor image: a steam train on fire. Pegged: Napoleon's defeat (1815), WWI (1914–1918), WWII end (1945).</li>
  <li><strong>1945–Present — Contemporary:</strong> Anchor image: a television satellite dish. Pegged: Moon landing (1969), Berlin Wall (1989), Internet era (1990s).</li>
</ul>
<p>The retrieval test: close your eyes and name the anchor image for each peg. Then recall two historical events attached to each. After three practice runs on different days, this scaffold becomes permanent retrieval infrastructure — it does not decay because it is semantic network rather than isolated fact storage.</p>''',
    r'<h2 id="anchor-method">.*?</h2>'
)

# Article 6
process_article(
    'd:/snappgrid-main/blog/science-trivia-facts-and-mnemonics/index.html',
    'Trivia & Knowledge', 'STEM Trivia Facts & Mnemonics',
    '/assets/images/blog/stem-trivia-matrix.svg', 'STEM trivia matrix showing high-frequency pub quiz questions organised by Physics, Chemistry, Biology, Astronomy, and Earth Science at four difficulty levels',
    r'<h2 id="construction">.*?</h2>',
    'knowledge-quest', 'The Knowledge Quest', '$8.99', 'Mixed Puzzles',
    '250 diverse puzzles spanning trivia, word search, cryptograms, and scrambles across 10 fascinating subjects — with full answer key.',
    [
        ('/blog/science-of-trivia-memory-recall/', 'Trivia & Knowledge', '16 min', 'Cognitive Science of Pub Quiz Mastery', 'Build the memory architecture that turns STEM facts into instant recall.'),
        ('/blog/world-history-trivia-memorization-techniques/', 'Trivia & Knowledge', '14 min', 'World History Memorization Techniques', 'The same peg system extended to scientific discovery timelines.'),
        ('/blog/brain-training-neuroplasticity-puzzle-science/', 'Brain Health', '15 min', 'Beyond the Lumosity Hype', 'Why learning STEM facts is genuine cognitive training, not trivial pursuit.')
    ],
    '''<h2>Scientific Taxonomy as a Memory Scaffold</h2>
<p>The Linnaean classification system — Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species — is itself a peg system. Every biological organism slots into this hierarchy, which means learning taxonomy gives you a pre-built retrieval scaffold for thousands of biology facts.</p>
<p>The mnemonic: <strong>Dear King Philip Came Over For Good Soup</strong>. One sentence carries the entire hierarchy. Every biology trivia question that asks "what class does X belong to?" or "which phylum groups molluscs with arthropods?" becomes answerable the moment you can place the question in the correct level of the hierarchy.</p>
<p>The same scaffold principle applies to chemistry: the periodic table is organised by atomic number horizontally and by electron shell vertically. Period 2 elements (Li, Be, B, C, N, O, F, Ne) appear in roughly 60% of all chemistry pub quiz questions. Memorising Period 2 alone, in order, creates a scaffold for most chemistry question clusters you will encounter.</p>
<p>For physics: the four fundamental forces (gravitational, electromagnetic, strong nuclear, weak nuclear) are the top-level pegs. Almost every physics trivia question about force, energy, or matter attaches to one of these four. Knowing which force governs which phenomenon makes the question 80% answered before the answer choices appear.</p>
<p>High-frequency exam facts by STEM category:</p>
<ul style="line-height:2;">
  <li><strong>Physics:</strong> Speed of light (3×10⁸ m/s), E=mc², the three laws of thermodynamics, Heisenberg uncertainty principle.</li>
  <li><strong>Chemistry:</strong> Noble gases (Group 18), oxidation states, Avogadro's number (6.022×10²³), pH scale extremes.</li>
  <li><strong>Biology:</strong> DNA structure (Watson &amp; Crick, 1953), ATP as energy currency, the five kingdoms, CRISPR mechanism.</li>
  <li><strong>Astronomy:</strong> Eight planets in order, light-year definition, event horizon, the Hubble constant.</li>
  <li><strong>Earth Science:</strong> Richter scale is logarithmic, tectonic plate count (~15 major), Milankovitch cycles control ice ages.</li>
</ul>''',
    r'<h2 id="biology">.*?</h2>'
)
