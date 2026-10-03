"""
SnappGrid Programmatic SVG Asset Generator
Generates all branded diagrams, charts, and book previews for snappgrid.com
Pure Python stdlib — no external dependencies required.
"""

import os, textwrap

OUT_BLOG  = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'blog')
OUT_BOOKS = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'books')
os.makedirs(OUT_BLOG,  exist_ok=True)
os.makedirs(OUT_BOOKS, exist_ok=True)

def save(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓  {os.path.relpath(path)}")

def svg_wrap(width, height, content, title="", dark=True):
    bg = "#0f172a" if dark else "#f7f3ec"
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="{title}">
  <title>{title}</title>
  <defs>
    <linearGradient id="hdr" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#818cf8"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <rect width="{width}" height="{height}" rx="12" fill="{bg}"/>
{content}
</svg>'''

# ─────────────────────────────────────────────────────────────
# 1. LOGIC GRID — 3×3 solved deduction matrix
# ─────────────────────────────────────────────────────────────
def logic_grid_3x3():
    rows = ["Marcus", "Diana", "Elena"]
    cols = ["Rooftop", "Storage", "Entrance"]
    # ✓ = solution, ✗ = eliminated
    cells = [
        ["✗", "✗", "✓"],  # Marcus → Entrance
        ["✗", "✓", "✗"],  # Diana  → Storage
        ["✓", "✗", "✗"],  # Elena  → Rooftop
    ]
    cell_colors = [
        ["#7f1d1d","#7f1d1d","#14532d"],
        ["#7f1d1d","#14532d","#7f1d1d"],
        ["#14532d","#7f1d1d","#7f1d1d"],
    ]
    cell_fg = [
        ["#fca5a5","#fca5a5","#86efac"],
        ["#fca5a5","#86efac","#fca5a5"],
        ["#86efac","#fca5a5","#fca5a5"],
    ]

    CW, CH = 110, 52
    OX, OY = 140, 90
    parts = []

    # Title
    parts.append(f'<rect width="560" height="40" rx="8" fill="url(#hdr)"/>')
    parts.append(f'<text x="280" y="26" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="14" font-weight="700" fill="white">Logic Grid: The Gallery Heist — Solved</text>')

    # Column headers
    for ci, col in enumerate(cols):
        x = OX + ci * CW + CW // 2
        parts.append(f'<rect x="{OX + ci*CW}" y="{OY - 32}" width="{CW-2}" height="28" rx="5" fill="#1e293b"/>')
        parts.append(f'<text x="{x}" y="{OY - 14}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" font-weight="600" fill="#94a3b8">{col}</text>')

    # Row headers + cells
    for ri, row in enumerate(rows):
        y = OY + ri * CH
        parts.append(f'<rect x="10" y="{y}" width="124" height="{CH-2}" rx="5" fill="#1e293b"/>')
        parts.append(f'<text x="72" y="{y + CH//2 + 4}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" font-weight="600" fill="#94a3b8">{row}</text>')
        for ci in range(3):
            cx = OX + ci * CW
            clr = cell_colors[ri][ci]
            fg  = cell_fg[ri][ci]
            sym = cells[ri][ci]
            parts.append(f'<rect x="{cx}" y="{y}" width="{CW-2}" height="{CH-2}" rx="5" fill="{clr}" opacity="0.85"/>')
            parts.append(f'<text x="{cx + CW//2}" y="{y + CH//2 + 7}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="22" font-weight="900" fill="{fg}" filter="url(#glow)">{sym}</text>')

    # Legend
    LY = OY + 3 * CH + 20
    parts.append(f'<rect x="10" y="{LY}" width="540" height="36" rx="6" fill="#1e293b" opacity="0.6"/>')
    parts.append(f'<text x="28" y="{LY+14}" font-family="Segoe UI,sans-serif" font-size="10" fill="#86efac">✓ Confirmed</text>')
    parts.append(f'<text x="130" y="{LY+14}" font-family="Segoe UI,sans-serif" font-size="10" fill="#fca5a5">✗ Eliminated</text>')
    parts.append(f'<text x="240" y="{LY+14}" font-family="Segoe UI,sans-serif" font-size="10" fill="#94a3b8">Reading: Elena → Rooftop | Diana → Storage | Marcus → Front Entrance</text>')
    parts.append(f'<text x="28" y="{LY+28}" font-family="Segoe UI,sans-serif" font-size="9" fill="#64748b">SnappGrid · snappgrid.com · From "The 10-Minute Detective" Logic Puzzle Series</text>')

    h = OY + 3 * CH + 70
    return svg_wrap(560, h, "\n".join(parts), "Solved 3x3 Logic Deduction Grid — The Gallery Heist")

# ─────────────────────────────────────────────────────────────
# 2. 3D LOGIC GRID — stacked 3-tier matrix
# ─────────────────────────────────────────────────────────────
def logic_grid_3d():
    parts = []
    parts.append('<rect width="620" height="420" rx="12" fill="#0f172a"/>')
    parts.append('<rect width="620" height="38" rx="0" fill="url(#hdr)"/>')
    parts.append('<text x="310" y="24" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="700" fill="white">3-Tier Logic Matrix — Advanced Deduction Structure</text>')

    tiers = [
        ("Tier A: Suspects × Locations", 58, ["Marcus","Diana","Elena"], ["Rooftop","Storage","Entrance"], [[0,0,1],[0,1,0],[1,0,0]]),
        ("Tier B: Suspects × Motives",  198, ["Marcus","Diana","Elena"], ["Debt","Vendetta","Fraud"],    [[0,1,0],[0,0,1],[1,0,0]]),
        ("Tier C: Locations × Motives", 338, ["Rooftop","Storage","Entrance"], ["Debt","Vendetta","Fraud"], [[1,0,0],[0,0,1],[0,1,0]]),
    ]

    CW, CH = 95, 36
    for label, ty, rows, cols, mat in tiers:
        parts.append(f'<text x="16" y="{ty}" font-family="Segoe UI,sans-serif" font-size="10" font-weight="700" fill="#818cf8">{label}</text>')
        OX, OY = 116, ty + 8
        for ci, c in enumerate(cols):
            parts.append(f'<text x="{OX + ci*CW + CW//2}" y="{OY - 2}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" fill="#64748b">{c}</text>')
        for ri, row in enumerate(rows):
            y = OY + ri * CH
            parts.append(f'<text x="{OX - 4}" y="{y + CH//2 + 3}" text-anchor="end" font-family="Segoe UI,sans-serif" font-size="9" fill="#64748b">{row}</text>')
            for ci in range(len(cols)):
                cx = OX + ci * CW
                confirmed = mat[ri][ci]
                fill = "#14532d" if confirmed else "#1e293b"
                sym  = "✓" if confirmed else "·"
                fg   = "#86efac" if confirmed else "#334155"
                parts.append(f'<rect x="{cx}" y="{y}" width="{CW-3}" height="{CH-3}" rx="4" fill="{fill}" opacity="0.9"/>')
                parts.append(f'<text x="{cx + CW//2}" y="{y + CH//2 + 5}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="16" font-weight="900" fill="{fg}">{sym}</text>')
        # Tier separator
        if ty < 300:
            sep_y = ty + 3 * CH + 20
            parts.append(f'<line x1="16" y1="{sep_y}" x2="604" y2="{sep_y}" stroke="#1e293b" stroke-width="1.5"/>')

    parts.append('<text x="16" y="412" font-family="Segoe UI,sans-serif" font-size="9" fill="#475569">SnappGrid · snappgrid.com · Advanced Logic Deduction Technique</text>')
    return svg_wrap(620, 420, "\n".join(parts), "3-Tier Advanced Logic Grid Matrix")

# ─────────────────────────────────────────────────────────────
# 3. CROSSWORD CLUE ANATOMY DIAGRAM
# ─────────────────────────────────────────────────────────────
def crossword_anatomy():
    parts = []
    parts.append('<rect width="600" height="360" rx="12" fill="#0f172a"/>')
    parts.append('<rect width="600" height="38" rx="0" fill="url(#hdr)"/>')
    parts.append('<text x="300" y="24" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="700" fill="white">Crossword Clue Anatomy: Decoding Constructor Tricks</text>')

    # Clue display
    clue = "Capital city of France, once the seat of a Sun King (5)"
    parts.append('<rect x="16" y="50" width="568" height="48" rx="8" fill="#1e293b"/>')
    parts.append(f'<text x="300" y="70" text-anchor="middle" font-family="Georgia,serif" font-size="15" fill="#f1f5f9">"{clue}"</text>')
    parts.append('<text x="300" y="88" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10" fill="#64748b">Cryptic-style surface reading — hides the real structure</text>')

    # Annotated segments
    segs = [
        (16,  108, 130, 36, "#1d4ed8", "#93c5fd", "DEFINITION", "Capital city\nof France"),
        (152, 108, 160, 36, "#7c3aed", "#c4b5fd", "HIDDEN ANSWER", "once the seat of\na Sun King"),
        (320, 108, 100, 36, "#065f46", "#86efac", "WORDPLAY IND.", "once…"),
        (430, 108, 154, 36, "#92400e", "#fde68a", "LETTER COUNT", "(5)"),
    ]
    for x, y, w, h, bg, fg, label, desc in segs:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{bg}" opacity="0.85"/>')
        parts.append(f'<text x="{x + w//2}" y="{y + 12}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="8" font-weight="700" fill="{fg}">{label}</text>')
        for li, line in enumerate(desc.split("\n")):
            parts.append(f'<text x="{x + w//2}" y="{y + 24 + li*11}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" fill="white">{line}</text>')

    # Mini crossword cells showing answer PARIS
    answer = "P A R I S"
    letters = answer.split()
    CX, CY, CS = 160, 165, 38
    for i, lt in enumerate(letters):
        cx = CX + i * (CS + 4)
        parts.append(f'<rect x="{cx}" y="{CY}" width="{CS}" height="{CS}" rx="4" fill="#1e3a5f" stroke="#4f46e5" stroke-width="1.5"/>')
        parts.append(f'<text x="{cx + CS//2}" y="{CY + CS//2 + 6}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="18" font-weight="900" fill="#818cf8">{lt}</text>')
    parts.append('<text x="300" y="225" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" fill="#64748b">Answer: PARIS — confirmed via crossing letters at positions 1, 3, 5</text>')

    # Frequency table
    headers = ["Letter", "Frequency", "Best Fill Pairs"]
    data = [("E","12.7%","EEL, ERE, ERA"),("A","8.2%","ALE, ATE, APE"),("R","6.0%","RAN, ROE, RUE"),("I","5.5%","ICE, INN, IRE"),("S","5.4%","SUN, SAP, SUE")]
    TX, TY = 16, 240
    parts.append(f'<rect x="{TX}" y="{TY}" width="568" height="104" rx="8" fill="#0f172a" stroke="#1e293b" stroke-width="1"/>')
    parts.append('<text x="300" y="258" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10" font-weight="700" fill="#818cf8">High-Frequency Crossword Letters — Grid Fill Reference</text>')
    col_xs = [30, 160, 300]
    for ci, hdr in enumerate(headers):
        parts.append(f'<text x="{col_xs[ci]}" y="{TY+28}" font-family="Segoe UI,sans-serif" font-size="9" font-weight="700" fill="#64748b">{hdr}</text>')
    for ri, row in enumerate(data):
        ry = TY + 42 + ri * 13
        bg = "#111827" if ri % 2 == 0 else ""
        for ci, val in enumerate(row):
            parts.append(f'<text x="{col_xs[ci]}" y="{ry}" font-family="Segoe UI,sans-serif" font-size="9" fill="#94a3b8">{val}</text>')

    parts.append('<text x="16" y="355" font-family="Segoe UI,sans-serif" font-size="9" fill="#475569">SnappGrid · snappgrid.com · From "Crossword Puzzles for Adults"</text>')
    return svg_wrap(600, 360, "\n".join(parts), "Crossword Clue Anatomy Diagram")

# ─────────────────────────────────────────────────────────────
# 4. COGNITIVE CURVE CHART — fluid intelligence vs. age
# ─────────────────────────────────────────────────────────────
def cognitive_curve():
    parts = []
    W, H = 620, 380
    parts.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0f172a"/>')
    parts.append(f'<rect width="{W}" height="38" rx="0" fill="url(#hdr)"/>')
    parts.append(f'<text x="{W//2}" y="24" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="700" fill="white">Cognitive Reserve: Fluid Intelligence vs. Age</text>')

    # Axes
    OX, OY, AW, AH = 60, 50, 520, 260
    BX, BY = OX, OY + AH

    parts.append(f'<line x1="{BX}" y1="{OY}" x2="{BX}" y2="{BY}" stroke="#334155" stroke-width="1.5"/>')
    parts.append(f'<line x1="{BX}" y1="{BY}" x2="{BX+AW}" y2="{BY}" stroke="#334155" stroke-width="1.5"/>')

    # Y axis labels
    for pct, label in [(0,"20"),(25,"40"),(50,"60"),(75,"80"),(100,"100")]:
        y = BY - int(AH * pct / 100)
        parts.append(f'<text x="{BX-8}" y="{y+4}" text-anchor="end" font-family="Segoe UI,sans-serif" font-size="9" fill="#64748b">{label}</text>')
        parts.append(f'<line x1="{BX}" y1="{y}" x2="{BX+AW}" y2="{y}" stroke="#1e293b" stroke-width="0.8" stroke-dasharray="3,3"/>')

    # X axis labels — age 20 to 80
    ages = list(range(20, 85, 10))
    for i, age in enumerate(ages):
        x = BX + int(AW * i / (len(ages)-1))
        parts.append(f'<text x="{x}" y="{BY+14}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" fill="#64748b">{age}</text>')

    # Axis labels
    parts.append(f'<text x="{BX + AW//2}" y="{BY+28}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10" fill="#94a3b8">Age</text>')
    parts.append(f'<text x="14" y="{OY + AH//2}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10" fill="#94a3b8" transform="rotate(-90,14,{OY+AH//2})">Cognitive Score (%)</text>')

    # Curve data — (age_frac, score_frac)
    def pt(age_f, score_f):
        return (BX + int(AW * age_f), BY - int(AH * score_f))

    # "No practice" — steady decline from 95 → 35
    no_practice = [(0,.95),(0.17,.90),(0.33,.82),(0.5,.68),(0.67,.54),(0.83,.43),(1.0,.35)]
    pts_np = [pt(a,s) for a,s in no_practice]
    path_np = f"M {pts_np[0][0]},{pts_np[0][1]} " + " ".join(f"L {x},{y}" for x,y in pts_np[1:])

    # Shaded area under "practice" curve
    practice = [(0,.95),(0.17,.93),(0.33,.90),(0.5,.85),(0.67,.80),(0.83,.74),(1.0,.70)]
    pts_p = [pt(a,s) for a,s in practice]
    path_p = f"M {pts_p[0][0]},{pts_p[0][1]} " + " ".join(f"L {x},{y}" for x,y in pts_p[1:])

    # Filled gap area
    shade_pts = [f"{x},{y}" for x,y in pts_p] + [f"{x},{y}" for x,y in reversed(pts_np)]
    parts.append(f'<polygon points="{" ".join(shade_pts)}" fill="#4f46e5" opacity="0.15"/>')

    parts.append(f'<path d="{path_np}" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6,3"/>')
    parts.append(f'<path d="{path_p}"  fill="none" stroke="#4ade80" stroke-width="2.5"/>')

    # Dots
    for x, y in pts_p:
        parts.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#4ade80" opacity="0.8"/>')

    # Labels on curves
    lx, ly = pt(0.5, 0.68)
    parts.append(f'<text x="{lx+8}" y="{ly}" font-family="Segoe UI,sans-serif" font-size="9" fill="#ef4444">No regular puzzle practice</text>')
    lx2, ly2 = pt(0.5, 0.87)
    parts.append(f'<text x="{lx2+8}" y="{ly2}" font-family="Segoe UI,sans-serif" font-size="9" fill="#4ade80">Daily puzzle practice</text>')

    # Annotation
    parts.append(f'<rect x="{BX + 300}" y="{OY + 160}" width="160" height="50" rx="6" fill="#1e293b" opacity="0.9"/>')
    parts.append(f'<text x="{BX + 380}" y="{OY + 176}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" font-weight="700" fill="#818cf8">Cognitive Reserve Gap</text>')
    parts.append(f'<text x="{BX + 380}" y="{OY + 189}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" fill="#94a3b8">Up to 35% score</text>')
    parts.append(f'<text x="{BX + 380}" y="{OY + 200}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" fill="#94a3b8">difference by age 70</text>')

    parts.append(f'<text x="16" y="{H-8}" font-family="Segoe UI,sans-serif" font-size="9" fill="#475569">SnappGrid · snappgrid.com · Based on published neuroplasticity research (Cattell-Horn fluid intelligence model)</text>')
    return svg_wrap(W, H, "\n".join(parts), "Cognitive Reserve Fluid Intelligence Curve Chart")

# ─────────────────────────────────────────────────────────────
# 5. MEMORY ARCHITECTURE — dual-coding recall diagram
# ─────────────────────────────────────────────────────────────
def memory_architecture():
    parts = []
    W, H = 600, 340
    parts.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0f172a"/>')
    parts.append(f'<rect width="{W}" height="38" rx="0" fill="url(#hdr)"/>')
    parts.append(f'<text x="{W//2}" y="24" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="700" fill="white">Dual-Coding Memory Architecture for Trivia Recall</text>')

    # Three columns
    cols = [
        (50,  80, 160, "#1d4ed8", "#93c5fd", "ENCODE", ["Verbal Label", "Visual Anchor", "Emotional Hook"]),
        (220, 80, 160, "#7c3aed", "#c4b5fd", "STORE",  ["Semantic Net", "Episodic Layer", "Schema Cluster"]),
        (390, 80, 160, "#065f46", "#86efac", "RETRIEVE",["Cue → Tag", "Spread Activate", "Reconstruct"]),
    ]
    for cx, cy, cw, bg, fg, title, items in cols:
        parts.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="220" rx="8" fill="{bg}" opacity="0.2" stroke="{fg}" stroke-width="1" stroke-opacity="0.4"/>')
        parts.append(f'<text x="{cx + cw//2}" y="{cy + 20}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" font-weight="700" fill="{fg}">{title}</text>')
        for i, item in enumerate(items):
            iy = cy + 48 + i * 56
            parts.append(f'<rect x="{cx+10}" y="{iy}" width="{cw-20}" height="42" rx="6" fill="{bg}" opacity="0.6"/>')
            parts.append(f'<text x="{cx + cw//2}" y="{iy + 18}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10" font-weight="600" fill="white">{item}</text>')
            parts.append(f'<text x="{cx + cw//2}" y="{iy + 32}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="8" fill="{fg}" opacity="0.8">{"→ Tag memory traces" if i==0 else ("→ Long-term potentiation" if i==1 else "→ Context reinstatement")}</text>')

    # Arrows between columns
    for ax in [210, 380]:
        parts.append(f'<line x1="{ax}" y1="190" x2="{ax+14}" y2="190" stroke="#4f46e5" stroke-width="2" marker-end="url(#arr)"/>')

    # "Key insight" banner
    parts.append(f'<rect x="16" y="{H-46}" width="{W-32}" height="36" rx="6" fill="#1e293b"/>')
    parts.append(f'<text x="{W//2}" y="{H-30}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10" font-weight="700" fill="#f59e0b">Key Insight: Tip-of-the-tongue failure = retrieval failure, not storage failure</text>')
    parts.append(f'<text x="{W//2}" y="{H-17}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" fill="#94a3b8">Fix: rebuild the retrieval CUE, not the memory itself</text>')
    return svg_wrap(W, H, "\n".join(parts), "Dual-Coding Memory Architecture for Trivia Recall")

# ─────────────────────────────────────────────────────────────
# 6. HISTORY TIMELINE
# ─────────────────────────────────────────────────────────────
def history_timeline():
    events = [
        ("3000 BC","Sumerian Writing","Ancient"),
        ("776 BC","First Olympics","Ancient"),
        ("44 BC","Julius Caesar","Ancient"),
        ("476 AD","Fall of Rome","Medieval"),
        ("1066","Battle of Hastings","Medieval"),
        ("1492","Columbus","Early Modern"),
        ("1776","US Independence","Modern"),
        ("1848","Year of Revolutions","Modern"),
        ("1914","WWI Begins","Modern"),
        ("1945","WWII Ends","Contemporary"),
        ("1969","Moon Landing","Contemporary"),
        ("1989","Berlin Wall Falls","Contemporary"),
    ]
    era_colors = {"Ancient":"#7c3aed","Medieval":"#1d4ed8","Early Modern":"#065f46","Modern":"#92400e","Contemporary":"#be185d"}
    W, H = 780, 280
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0f172a"/>')
    parts.append(f'<rect width="{W}" height="38" rx="0" fill="url(#hdr)"/>')
    parts.append(f'<text x="{W//2}" y="24" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="700" fill="white">World History Trivia: Chronological Peg System</text>')

    # Timeline axis
    TY = 130
    parts.append(f'<line x1="30" y1="{TY}" x2="{W-30}" y2="{TY}" stroke="#334155" stroke-width="2"/>')

    # Arrow head
    parts.append(f'<polygon points="{W-30},{TY} {W-42},{TY-5} {W-42},{TY+5}" fill="#334155"/>')

    n = len(events)
    for i, (date, label, era) in enumerate(events):
        x = 40 + int((W - 80) * i / (n - 1))
        above = i % 2 == 0
        dot_y = TY
        line_y1 = dot_y - 30 if above else dot_y + 4
        line_y2 = dot_y - 60 if above else dot_y + 55
        text_y  = dot_y - 70 if above else dot_y + 68
        date_y  = dot_y - 82 if above else dot_y + 80

        clr = era_colors.get(era, "#64748b")
        parts.append(f'<circle cx="{x}" cy="{dot_y}" r="5" fill="{clr}" stroke="white" stroke-width="1.5"/>')
        parts.append(f'<line x1="{x}" y1="{line_y1}" x2="{x}" y2="{line_y2}" stroke="{clr}" stroke-width="1.2" stroke-dasharray="2,2"/>')

        # Label box
        lw = max(len(label) * 6, 60)
        lx = max(30, min(x - lw//2, W - lw - 10))
        ly = text_y - 12 if above else text_y - 12
        parts.append(f'<rect x="{lx}" y="{ly}" width="{lw}" height="22" rx="4" fill="{clr}" opacity="0.85"/>')
        parts.append(f'<text x="{lx + lw//2}" y="{ly + 14}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="8.5" font-weight="600" fill="white">{label}</text>')
        parts.append(f'<text x="{x}" y="{date_y}" text-anchor="middle" font-family="Segoe UI,mono,sans-serif" font-size="8" fill="#64748b">{date}</text>')

    # Era legend
    LY = H - 30
    lx = 16
    for era, clr in era_colors.items():
        parts.append(f'<rect x="{lx}" y="{LY}" width="10" height="10" rx="2" fill="{clr}"/>')
        parts.append(f'<text x="{lx + 14}" y="{LY + 8}" font-family="Segoe UI,sans-serif" font-size="8" fill="#94a3b8">{era}</text>')
        lx += len(era) * 5 + 34

    return svg_wrap(W, H, "\n".join(parts), "World History Chronological Peg System Timeline")

# ─────────────────────────────────────────────────────────────
# 7. STEM TRIVIA MATRIX
# ─────────────────────────────────────────────────────────────
def stem_matrix():
    categories = ["Physics", "Chemistry", "Biology", "Astronomy", "Earth Sci."]
    difficulties = ["Easy", "Medium", "Hard", "Expert"]
    cat_colors = ["#1d4ed8","#065f46","#7c3aed","#92400e","#0e7490"]
    sample_facts = [
        ["Speed of light","Periodic Table","DNA double helix","# of planets=8","Richter Scale"],
        ["Newton's 3 Laws","Noble gases","Mitosis phases","Light-year def.","Tectonic plates"],
        ["E=mc²","Electron shells","Photosynthesis eq.","Event horizon","Wegener theory"],
        ["Heisenberg","Oxidation states","CRISPR mechanism","Olbers' paradox","Milankovitch"],
    ]
    CW, CH = 110, 46
    OX, OY = 70, 80
    W = OX + len(categories) * CW + 20
    H = OY + len(difficulties) * CH + 60
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0f172a"/>')
    parts.append(f'<rect width="{W}" height="38" rx="0" fill="url(#hdr)"/>')
    parts.append(f'<text x="{W//2}" y="24" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="700" fill="white">STEM Trivia Matrix — High-Frequency Pub Quiz Clusters</text>')

    for ci, (cat, clr) in enumerate(zip(categories, cat_colors)):
        cx = OX + ci * CW
        parts.append(f'<rect x="{cx}" y="{OY - 26}" width="{CW-2}" height="22" rx="5" fill="{clr}" opacity="0.8"/>')
        parts.append(f'<text x="{cx + CW//2}" y="{OY - 11}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" font-weight="700" fill="white">{cat}</text>')

    diff_colors = ["#14532d","#854d0e","#7f1d1d","#3b0764"]
    for ri, (diff, dclr) in enumerate(zip(difficulties, diff_colors)):
        ry = OY + ri * CH
        parts.append(f'<rect x="4" y="{ry}" width="62" height="{CH-2}" rx="5" fill="{dclr}" opacity="0.7"/>')
        parts.append(f'<text x="35" y="{ry + CH//2 + 4}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" font-weight="600" fill="white">{diff}</text>')
        for ci, fact in enumerate(sample_facts[ri]):
            clr = cat_colors[ci]
            cx = OX + ci * CW
            parts.append(f'<rect x="{cx}" y="{ry}" width="{CW-2}" height="{CH-2}" rx="5" fill="{clr}" opacity="0.15" stroke="{clr}" stroke-width="0.8" stroke-opacity="0.4"/>')
            # Wrap fact text
            words = fact.split()
            line1 = " ".join(words[:3])
            line2 = " ".join(words[3:]) if len(words) > 3 else ""
            parts.append(f'<text x="{cx + CW//2}" y="{ry + (CH//2 - 4 if line2 else CH//2 + 4)}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="8.5" fill="#e2e8f0">{line1}</text>')
            if line2:
                parts.append(f'<text x="{cx + CW//2}" y="{ry + CH//2 + 8}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="8.5" fill="#e2e8f0">{line2}</text>')

    parts.append(f'<text x="16" y="{H-8}" font-family="Segoe UI,sans-serif" font-size="9" fill="#475569">SnappGrid · snappgrid.com · From "The Ultimate General Knowledge Trivia Challenge"</text>')
    return svg_wrap(W, H, "\n".join(parts), "STEM Trivia Matrix — High-Frequency Pub Quiz Clusters")

# ─────────────────────────────────────────────────────────────
# 8. GEOGRAPHY SCHEMATIC — world regions
# ─────────────────────────────────────────────────────────────
def geography_schematic():
    W, H = 640, 340
    regions = [
        (70, 90, 80, 65, "#1d4ed8", "North\nAmerica"),
        (60, 175, 60, 70, "#065f46", "South\nAmerica"),
        (250,70, 90, 60, "#7c3aed", "Europe"),
        (230,145,100,80, "#92400e", "Africa"),
        (360,80, 80, 70, "#be185d", "Middle\nEast"),
        (440,70,120, 90, "#0e7490", "Asia"),
        (460,175,100,60, "#854d0e", "SE Asia /\nOceania"),
        (130,90, 90, 55, "#334155", "Atlantic\nOcean"),
        (320,150,80, 90, "#334155", "Indian\nOcean"),
    ]
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0c1a2e"/>')
    parts.append(f'<rect width="{W}" height="38" rx="0" fill="url(#hdr)"/>')
    parts.append(f'<text x="{W//2}" y="24" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="700" fill="white">World Geography Schematic — Region & Capital Reference</text>')

    for rx, ry, rw, rh, clr, label in regions:
        is_ocean = clr == "#334155"
        parts.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="8" fill="{clr}" opacity="{0.25 if is_ocean else 0.75}"/>')
        if not is_ocean:
            parts.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="8" fill="none" stroke="{clr}" stroke-width="1.5" opacity="0.8"/>')
        lines = label.split("\n")
        for li, line in enumerate(lines):
            parts.append(f'<text x="{rx + rw//2}" y="{ry + rh//2 - (len(lines)-1)*7 + li*14}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="{9 if is_ocean else 10}" font-weight="{"400" if is_ocean else "700"}" fill="{"#334155" if is_ocean else "white"}">{line}</text>')

    # Capital quick-fire section
    facts = [("Paris","France","Europe"),("Tokyo","Japan","Asia"),("Brasília","Brazil","S.America"),
             ("Nairobi","Kenya","Africa"),("Ottawa","Canada","N.America"),("Wellington","NZ","Oceania")]
    parts.append(f'<rect x="0" y="265" width="{W}" height="56" rx="0" fill="#0f172a"/>')
    parts.append(f'<rect x="0" y="265" width="{W}" height="2" fill="#1e293b"/>')
    parts.append(f'<text x="{W//2}" y="282" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" font-weight="700" fill="#818cf8">⚡ Capital Quick-Fire — Common Exam Traps</text>')
    for i, (cap, country, region) in enumerate(facts):
        fx = 18 + i * 104
        parts.append(f'<text x="{fx}" y="298" font-family="Segoe UI,sans-serif" font-size="9" font-weight="700" fill="white">{cap}</text>')
        parts.append(f'<text x="{fx}" y="310" font-family="Segoe UI,sans-serif" font-size="8" fill="#64748b">{country}</text>')
        parts.append(f'<text x="{fx}" y="320" font-family="Segoe UI,sans-serif" font-size="7.5" fill="#334155">{region}</text>')

    return svg_wrap(W, H, "\n".join(parts), "World Geography Schematic — Region and Capital Reference")

# ─────────────────────────────────────────────────────────────
# 9. CINEMA DECADE MATRIX
# ─────────────────────────────────────────────────────────────
def cinema_matrix():
    decades = ["1950s","1960s","1970s","1980s","1990s","2000s","2010s","2020s"]
    genres  = ["Drama","Comedy","Action","Sci-Fi","Horror","Animation"]
    hits = {
        ("1950s","Drama"):   "All About Eve",
        ("1960s","Comedy"):  "Some Like It Hot",
        ("1970s","Action"):  "Jaws",
        ("1970s","Sci-Fi"):  "Star Wars (1977)",
        ("1980s","Action"):  "Die Hard",
        ("1980s","Sci-Fi"):  "E.T.",
        ("1980s","Animation"):"The Little Mermaid",
        ("1990s","Drama"):   "Schindler's List",
        ("1990s","Sci-Fi"):  "The Matrix",
        ("2000s","Animation"):"Shrek / Finding Nemo",
        ("2000s","Drama"):   "No Country for Old Men",
        ("2010s","Action"):  "Avengers: Endgame",
        ("2010s","Drama"):   "Parasite (2019)",
        ("2020s","Sci-Fi"):  "Dune: Part Two",
    }
    CW, CH = 82, 38
    OX, OY = 76, 80
    W = OX + len(decades) * CW + 16
    H = OY + len(genres) * CH + 44
    parts = []
    parts.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0f172a"/>')
    parts.append(f'<rect width="{W}" height="38" rx="0" fill="url(#hdr)"/>')
    parts.append(f'<text x="{W//2}" y="24" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="700" fill="white">Cinema Decade Matrix — Box-Office Landmark Reference</text>')

    decade_colors = ["#1e3a5f","#1d4437","#3b1a6b","#7c1d1d","#1a3d5c","#2d1b3d","#0f3d2e","#1a1a3d"]
    for di, decade in enumerate(decades):
        dx = OX + di * CW
        clr = decade_colors[di % len(decade_colors)]
        parts.append(f'<rect x="{dx}" y="{OY-24}" width="{CW-2}" height="20" rx="4" fill="{clr}"/>')
        parts.append(f'<text x="{dx + CW//2}" y="{OY-10}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" font-weight="700" fill="#94a3b8">{decade}</text>')

    genre_colors = ["#4f46e5","#059669","#dc2626","#7c3aed","#c2410c","#d97706"]
    for gi, genre in enumerate(genres):
        gy = OY + gi * CH
        clr = genre_colors[gi]
        parts.append(f'<rect x="4" y="{gy}" width="{OX-8}" height="{CH-2}" rx="4" fill="{clr}" opacity="0.7"/>')
        parts.append(f'<text x="{(OX-4)//2}" y="{gy + CH//2 + 4}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" font-weight="600" fill="white">{genre}</text>')

        for di, decade in enumerate(decades):
            dx = OX + di * CW
            hit = hits.get((decade, genre), "")
            has_hit = bool(hit)
            bg_alpha = "0.7" if has_hit else "0.06"
            bg_clr = clr if has_hit else "#94a3b8"
            parts.append(f'<rect x="{dx}" y="{gy}" width="{CW-2}" height="{CH-2}" rx="4" fill="{bg_clr}" opacity="{bg_alpha}"/>')
            if has_hit:
                words = hit.split()
                line1 = " ".join(words[:2])
                line2 = " ".join(words[2:]) if len(words) > 2 else ""
                parts.append(f'<text x="{dx + CW//2}" y="{gy + (CH//2 - 3 if line2 else CH//2 + 4)}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="7.5" font-weight="600" fill="white">{line1}</text>')
                if line2:
                    parts.append(f'<text x="{dx + CW//2}" y="{gy + CH//2 + 8}" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="7" fill="white" opacity="0.9">{line2}</text>')

    parts.append(f'<text x="16" y="{H-8}" font-family="Segoe UI,sans-serif" font-size="9" fill="#475569">SnappGrid · snappgrid.com · Highlighted cells = landmark releases for each genre/decade pairing</text>')
    return svg_wrap(W, H, "\n".join(parts), "Cinema Decade Matrix — Box-Office Landmark Reference")

# ─────────────────────────────────────────────────────────────
# 10. BOOK 3D SVG MOCKUPS (all 8 books)
# ─────────────────────────────────────────────────────────────
BOOKS = [
    ("true-crime-logic",    "The 10-Minute\nDetective",      "linear-gradient(145deg,#2d1b3d,#4a1942)", "#8A2A5A", "#c084fc", "Logic Grid"),
    ("brain-boost",         "Brain Boost\nChallenge",         "linear-gradient(145deg,#0f2744,#1a3f6f)", "#2A6EA6", "#60a5fa", "Brain Training"),
    ("crossword-adults",    "Crossword Puzzles\nfor Adults",  "linear-gradient(145deg,#3d2a0f,#6b4a1a)", "#C8922A", "#fbbf24", "Crossword"),
    ("food-culture-trivia", "Food, Culture &\nHow the World Eats","linear-gradient(145deg,#0f3328,#1a5540)", "#2A8A6E", "#34d399", "Trivia"),
    ("forbidden-history",   "Forbidden\nHistory",             "linear-gradient(145deg,#2d0f0f,#4a1a1a)", "#8A2A2A", "#f87171", "Trivia"),
    ("knowledge-quest",     "The Knowledge\nQuest",           "linear-gradient(145deg,#1f1040,#362070)", "#5A3A8A", "#a78bfa", "Mixed Puzzles"),
    ("trivia-challenge",    "The Ultimate\nTrivia Challenge",  "linear-gradient(145deg,#0f2744,#1a4060)", "#2A6EA6", "#38bdf8", "Trivia"),
    ("unbelievable-trivia", "Unbelievable\nBut True Trivia",  "linear-gradient(145deg,#3d2a0f,#5a3d10)", "#C8922A", "#fde68a", "Trivia"),
]

def book_mockup(slug, title, grad, spine_hex, accent_hex, genre):
    W, H = 260, 320
    # Spine gradient from hex
    spine_r = int(spine_hex[1:3],16)
    spine_g = int(spine_hex[3:5],16)
    spine_b = int(spine_hex[5:7],16)
    accent_r = int(accent_hex[1:3],16)
    accent_g = int(accent_hex[3:5],16)
    accent_b = int(accent_hex[5:7],16)
    # Parse gradient stops from the string
    stops = [("#2d1b3d","#4a1942"),("#0f2744","#1a3f6f"),("#3d2a0f","#6b4a1a"),
             ("#0f3328","#1a5540"),("#2d0f0f","#4a1a1a"),("#1f1040","#362070"),
             ("#0f2744","#1a4060"),("#3d2a0f","#5a3d10")]
    book_idx = list(b[0] for b in BOOKS).index(slug)
    c1, c2 = stops[book_idx]

    parts = []
    parts.append(f'<rect width="{W}" height="{H}" rx="12" fill="#111827"/>')
    # Drop shadow
    parts.append(f'<rect x="28" y="32" width="168" height="224" rx="4" fill="rgba(0,0,0,0.5)" filter="blur(14px)"/>')
    # Spine
    parts.append(f'<rect x="16" y="24" width="18" height="224" rx="3 0 0 3" fill="{spine_hex}" opacity="0.9"/>')
    # Book face gradient using linearGradient
    parts.append(f'''<defs><linearGradient id="bk{book_idx}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient></defs>''')
    parts.append(f'<rect x="34" y="24" width="152" height="224" rx="0 4 4 0" fill="url(#bk{book_idx})"/>')
    # Glint
    parts.append(f'<rect x="34" y="24" width="152" height="40" rx="0 4 0 0" fill="rgba(255,255,255,0.05)"/>')
    # Border
    parts.append(f'<rect x="34" y="24" width="152" height="224" rx="0 4 4 0" fill="none" stroke="{accent_hex}" stroke-width="0.8" opacity="0.4"/>')
    # Genre badge
    parts.append(f'<rect x="44" y="34" width="{len(genre)*6+10}" height="16" rx="8" fill="{spine_hex}" opacity="0.8"/>')
    parts.append(f'<text x="{44 + (len(genre)*6+10)//2}" y="45" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="7.5" font-weight="700" fill="{accent_hex}">{genre.upper()}</text>')
    # Title
    lines = title.split("\n")
    for li, line in enumerate(lines):
        parts.append(f'<text x="110" y="{115 + li*22}" text-anchor="middle" font-family="Georgia,serif" font-size="{16 if len(line)>14 else 18}" font-weight="700" fill="white">{line}</text>')
    # Author
    parts.append(f'<text x="110" y="180" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10" fill="{accent_hex}">Ahmad Asad</text>')
    # SnappGrid logo strip
    parts.append(f'<rect x="34" y="218" width="152" height="30" rx="0 0 4 0" fill="{spine_hex}" opacity="0.5"/>')
    parts.append(f'<text x="110" y="237" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="9" font-weight="700" fill="rgba(255,255,255,0.7)">SnappGrid · Digital Edition</text>')
    # Bottom accent line
    parts.append(f'<rect x="60" y="195" width="100" height="2" rx="1" fill="{accent_hex}" opacity="0.5"/>')

    return svg_wrap(W, H, "\n".join(parts), f"{title.replace(chr(10),' ')} — Book Cover Mockup")

# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────
def main():
    print("\nSnappGrid Asset Generator -- Starting\n")
    assets = [
        ("logic-grid-3x3-solved.svg",     logic_grid_3x3,        OUT_BLOG),
        ("logic-grid-3d-advanced.svg",     logic_grid_3d,         OUT_BLOG),
        ("crossword-clue-anatomy.svg",     crossword_anatomy,     OUT_BLOG),
        ("cognitive-reserve-curve.svg",    cognitive_curve,       OUT_BLOG),
        ("memory-dual-coding.svg",         memory_architecture,   OUT_BLOG),
        ("history-timeline-peg.svg",       history_timeline,      OUT_BLOG),
        ("stem-trivia-matrix.svg",         stem_matrix,           OUT_BLOG),
        ("geography-world-schematic.svg",  geography_schematic,   OUT_BLOG),
        ("cinema-decade-matrix.svg",       cinema_matrix,         OUT_BLOG),
    ]
    for filename, fn, out_dir in assets:
        svg = fn()
        save(os.path.join(out_dir, filename), svg)

    print("\n📚 Book Cover Mockups\n")
    for slug, title, grad, spine, accent, genre in BOOKS:
        svg = book_mockup(slug, title, grad, spine, accent, genre)
        save(os.path.join(OUT_BOOKS, f"book-{slug}.svg"), svg)

    print(f"\n✅ Done — {len(assets) + len(BOOKS)} assets written to:")
    print(f"   assets/images/blog/  ({len(assets)} diagrams)")
    print(f"   assets/images/books/ ({len(BOOKS)} book covers)\n")

if __name__ == "__main__":
    main()
