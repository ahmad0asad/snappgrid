import re

with open('d:/snappgrid-main/games/lexigrid/index.html', 'r', encoding='utf-8') as f:
    old_content = f.read()

dict_match = re.search(r'const RAW_DICTIONARY\s*=\s*"([^"]+)";', old_content)
raw_dict = dict_match.group(1)

stages_match = re.search(r'(const STAGES = \[\];[\s\S]*?(?=const BIOMES = \[))', old_content)
biomes_match = re.search(r'(const BIOMES = \[\s*\{[\s\S]*?\];)', old_content)
achvs_match = re.search(r'(const ACHVS = \[\s*\{[\s\S]*?\];)', old_content)
letter_pts_match = re.search(r'(const LETTER_PTS = \{[^}]*\};)', old_content)
ad_provider_match = re.search(r'(const AdProvider = \{[\s\S]*?\};\s*)(?=const AudioEngine)', old_content)
audio_engine_match = re.search(r'(const AudioEngine = \{[\s\S]*?\};\s*)(?=const fxCanvas)', old_content)

new_content = f"""<!DOCTYPE html>
<html lang="en" data-theme="slate">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>LexiGrid — Free Word Puzzle Game | SnappGrid</title>
  <link rel="canonical" href="https://snappgrid.com/lexigrid">
  <meta property="og:title" content="LexiGrid — Free Word Puzzle Game | SnappGrid">
  <meta property="og:description" content="Swipe adjacent letters to build words on a live grid. Play free — 3 game modes, no download needed.">
  <meta property="og:url" content="https://snappgrid.com/lexigrid">
  <script src="https://cdn.jsdelivr.net/npm/pixi.js@8.6.1/dist/pixi.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/EasePack.min.js"></script>
  <style>
    /* 5 biome CSS variables */
    :root {{ --bg:#0f172a; --tile-active:#4f46e5; --trail-color:#f59e0b; --text:#f1f5f9; --accent:#818cf8; --board-glow:rgba(79,70,229,.35); --ambient1:rgba(79,70,229,.15); --ambient2:rgba(129,140,248,.10); --scanline:transparent; }}
    [data-theme="cyber"]   {{ --bg:#05050a; --tile-active:#06b6d4; --trail-color:#ec4899; --text:#e0f2fe; --accent:#22d3ee; --board-glow:rgba(6,182,212,.42); --ambient1:rgba(6,182,212,.13); --ambient2:rgba(236,72,153,.09); --scanline:rgba(0,255,255,.025); }}
    [data-theme="amber"]   {{ --bg:#18181b; --tile-active:#ea580c; --trail-color:#eab308; --text:#fafaf9; --accent:#fb923c; --board-glow:rgba(234,88,12,.50); --ambient1:rgba(234,88,12,.18); --ambient2:rgba(234,179,8,.12); --scanline:transparent; }}
    [data-theme="emerald"] {{ --bg:#022c22; --tile-active:#059669; --trail-color:#34d399; --text:#ecfdf5; --accent:#6ee7b7; --board-glow:rgba(5,150,105,.45); --ambient1:rgba(5,150,105,.16); --ambient2:rgba(52,211,153,.10); --scanline:transparent; }}
    [data-theme="cosmic"]  {{ --bg:#1e1b4b; --tile-active:#9333ea; --trail-color:#a855f7; --text:#f5f3ff; --accent:#c084fc; --board-glow:rgba(147,51,234,.45); --ambient1:rgba(147,51,234,.18); --ambient2:rgba(168,85,247,.12); --scanline:transparent; }}

    /* Reset */
    * {{ box-sizing:border-box; user-select:none; touch-action:none; -webkit-tap-highlight-color:transparent; margin:0; padding:0; }}
    html,body {{ width:100%; height:100%; overflow:hidden; font-family:'Segoe UI',system-ui,sans-serif; background:var(--bg); color:var(--text); display:flex; flex-direction:column; }}

    /* Ambient bg mesh */
    body::before {{ content:''; position:fixed; inset:0; z-index:0; pointer-events:none;
      background: radial-gradient(ellipse 65% 55% at 15% 25%, var(--ambient1) 0%, transparent 70%),
                  radial-gradient(ellipse 55% 65% at 85% 75%, var(--ambient2) 0%, transparent 70%);
      animation:ambientShift 14s ease-in-out infinite alternate; }}
    @keyframes ambientShift {{ 0%{{opacity:1;transform:scale(1)}} 50%{{opacity:.7;transform:scale(1.04)}} 100%{{opacity:1;transform:scale(1)}} }}
    body::after {{ content:''; position:fixed; inset:0; z-index:1; pointer-events:none;
      background:repeating-linear-gradient(0deg,var(--scanline) 0px,transparent 1px,transparent 3px); }}

    /* Loading screen */
    #loadingScreen {{ position:fixed; inset:0; background:var(--bg); display:flex; flex-direction:column; align-items:center; justify-content:center; z-index:9999; transition:opacity .5s; }}
    #loadingScreen h2 {{ font-size:36px; font-weight:900; color:var(--accent); text-shadow:0 0 30px var(--accent); margin:8px 0 4px; letter-spacing:2px; }}
    #loadingScreen p {{ color:rgba(255,255,255,.4); font-size:13px; }}

    /* Back link */
    #back-link {{ position:fixed; top:10px; left:10px; color:var(--text); text-decoration:none; font-size:11px; letter-spacing:1.5px; text-transform:uppercase; opacity:.5; z-index:100; padding:4px 8px; border:1px solid rgba(255,255,255,.12); border-radius:6px; transition:opacity .2s; }}
    #back-link:hover {{ opacity:.9; }}

    /* HUD */
    #hud {{ position:relative; z-index:50; padding:8px 14px; display:flex; justify-content:space-between; align-items:center; background:rgba(0,0,0,.40); backdrop-filter:blur(14px); border-bottom:1px solid rgba(255,255,255,.07); flex-shrink:0; }}
    .hud-stat {{ display:flex; flex-direction:column; align-items:center; background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.09); border-radius:10px; padding:3px 9px; min-width:46px; font-size:9px; font-weight:700; letter-spacing:.6px; text-transform:uppercase; color:rgba(255,255,255,.45); gap:1px; }}
    .hud-val {{ font-size:17px; font-weight:800; color:var(--accent); font-variant-numeric:tabular-nums; }}
    .hud-val.pop {{ animation:hudPop .35s cubic-bezier(.34,1.56,.64,1); }}
    @keyframes hudPop {{ 0%{{transform:scale(1)}} 50%{{transform:scale(1.45);color:var(--trail-color)}} 100%{{transform:scale(1)}} }}

    /* Game area */
    #game-area {{ flex:1; position:relative; z-index:2; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:10px; }}

    /* PixiJS board mount */
    #pixi-mount {{ position:relative; line-height:0; }}
    #pixi-mount::before {{ content:''; position:absolute; inset:-20px; z-index:-1; border-radius:50%;
      background:radial-gradient(ellipse 88% 38% at 50% 115%, var(--board-glow) 0%, transparent 70%);
      filter:blur(20px); animation:floorPulse 4s ease-in-out infinite alternate; pointer-events:none; }}
    @keyframes floorPulse {{ from{{opacity:.5}} to{{opacity:1}} }}

    /* Word display */
    #word-display {{ height:50px; font-size:28px; font-weight:900; letter-spacing:3px; display:flex; align-items:center; justify-content:center; text-transform:uppercase; color:var(--trail-color); text-shadow:0 0 20px var(--trail-color); transition:color .15s,text-shadow .15s; }}

    /* Objective */
    #objective-text {{ font-size:12px; color:rgba(255,255,255,.4); text-align:center; }}

    /* Floating score tags */
    #float-container {{ position:fixed; inset:0; pointer-events:none; z-index:500; }}
    .float-tag {{ position:absolute; font-weight:900; pointer-events:none; }}

    /* Modals */
    .modal {{ position:fixed; inset:0; background:rgba(0,0,0,.72); backdrop-filter:blur(14px); display:none; align-items:center; justify-content:center; z-index:1000; flex-direction:column; padding:20px; }}
    .modal.active {{ display:flex; }}
    .modal-content {{ background:rgba(12,20,40,.92); backdrop-filter:blur(22px); padding:28px; border-radius:20px; border:1px solid rgba(255,255,255,.12); box-shadow:0 30px 80px rgba(0,0,0,.60),inset 0 1px 0 rgba(255,255,255,.08); max-width:420px; width:100%; text-align:center; max-height:85vh; overflow-y:auto; }}
    .btn {{ background:var(--tile-active); color:#fff; border:none; padding:11px 22px; font-size:14px; border-radius:10px; cursor:pointer; font-weight:700; margin:5px; box-shadow:0 4px 0 rgba(0,0,0,.35); transition:transform .08s,filter .1s,box-shadow .08s; }}
    .btn:hover {{ filter:brightness(1.12); }}
    .btn:active {{ transform:translateY(3px); box-shadow:0 1px 0 rgba(0,0,0,.35); }}

    /* Achievement toast */
    #achievement-toast {{ position:fixed; bottom:-120px; left:50%; transform:translateX(-50%); background:rgba(12,20,40,.92); backdrop-filter:blur(18px); border:1px solid var(--accent); box-shadow:0 0 30px rgba(129,140,248,.25); padding:13px 24px; border-radius:40px; color:white; display:flex; align-items:center; gap:12px; transition:bottom .45s cubic-bezier(.175,.885,.32,1.275); z-index:9999; white-space:nowrap; }}
    #achievement-toast.show {{ bottom:36px; }}

    /* Stage grid */
    .stage-grid {{ display:grid; grid-template-columns:repeat(5,1fr); gap:10px; margin-top:18px; }}
    .stage-btn {{ background:rgba(0,0,0,.3); border:2px solid #333; border-radius:8px; padding:12px 0; font-weight:bold; cursor:default; color:#555; display:flex; flex-direction:column; align-items:center; font-size:13px; }}
    .stage-btn.unlocked {{ border-color:var(--accent); color:#fff; cursor:pointer; background:rgba(255,255,255,.05); }}
    .stars-row {{ font-size:9px; margin-top:3px; color:#555; }}
    .stars-row.lit {{ color:gold; }}

    /* Calendar */
    .calendar {{ display:grid; grid-template-columns:repeat(7,1fr); gap:5px; margin-top:12px; }}
    .cal-day {{ width:30px; height:30px; display:flex; align-items:center; justify-content:center; background:rgba(255,255,255,.05); border-radius:6px; font-size:11px; border:1px solid rgba(255,255,255,.07); }}
    .cal-day.done {{ background:#059669; color:white; border-color:#34d399; }}
  </style>
</head>
<body>
  <div id="loadingScreen">
    <div style="font-size:52px">🔤</div>
    <h2>LexiGrid</h2>
    <p>Preparing dictionary…</p>
  </div>

  <a href="/" id="back-link">← SnappGrid</a>

  <header id="hud">
    <div class="hud-stat"><span>Score</span><span id="ui-score" class="hud-val">0</span></div>
    <div class="hud-stat" id="ui-moves-box"><span>Moves</span><span id="ui-moves" class="hud-val">20</span></div>
    <div class="hud-stat" id="ui-time-box" style="display:none"><span>Time</span><span id="ui-time" class="hud-val">120</span></div>
    <div class="hud-stat"><span>Combo</span><span id="ui-combo" class="hud-val">1x</span></div>
    <div class="hud-stat"><span>💎</span><span id="ui-shards" class="hud-val">0</span></div>
    <div style="display:flex;gap:5px">
      <button class="btn" style="padding:5px 9px;font-size:13px;margin:0" onclick="toggleMute()" id="btn-mute">🔊</button>
      <button class="btn" style="padding:5px 9px;font-size:13px;margin:0" onclick="showModal('vault-modal')">🎨</button>
      <button class="btn" style="padding:5px 9px;font-size:13px;margin:0" onclick="showModal('menu-modal')">☰</button>
    </div>
  </header>

  <main id="game-area">
    <div id="pixi-mount"></div>
    <div id="word-display"></div>
    <div id="objective-text"></div>
  </main>

  <!-- Menu Modal -->
  <div id="menu-modal" class="modal active">
    <div class="modal-content">
      <h1 style="color:var(--accent);margin-bottom:4px;font-size:38px">LexiGrid</h1>
      <p style="color:#888;margin-bottom:24px;font-size:13px">SnappGrid Originals</p>
      <button class="btn" style="width:100%" onclick="openStageSelect()">🗺 Adventure Mode</button>
      <button class="btn" style="width:100%" onclick="startGame('collapse')">💥 Collapse Mode</button>
      <button class="btn" style="width:100%" onclick="startGame('blitz')">⚡ Blitz (120s)</button>
      <button class="btn" style="width:100%" onclick="startGame('daily')">📅 Daily Challenge</button>
      <div style="margin-top:18px;display:flex;justify-content:center;gap:8px">
        <button class="btn" onclick="showStatsModal()">📊 Stats</button>
        <button class="btn" onclick="populateAchvModal();showModal('achievements-modal')">🏆 Achvs</button>
      </div>
    </div>
  </div>

  <!-- Stage Modal -->
  <div id="stage-modal" class="modal">
    <div class="modal-content" style="max-width:500px">
      <h2>Adventure Stages</h2>
      <div id="stage-grid" class="stage-grid"></div>
      <button class="btn" style="margin-top:18px" onclick="showModal('menu-modal')">← Back</button>
    </div>
  </div>

  <!-- End Modal -->
  <div id="end-modal" class="modal">
    <div class="modal-content">
      <h2 id="end-title">Stage Clear!</h2>
      <p id="end-desc" style="color:#aaa;margin:8px 0"></p>
      <div id="end-stars" style="font-size:28px;letter-spacing:8px;margin:12px 0"></div>
      <button class="btn" onclick="shareResult()">📤 Share</button>
      <button class="btn" id="end-next-btn" onclick="showModal('menu-modal')">Continue</button>
    </div>
  </div>

  <!-- Vault Modal -->
  <div id="vault-modal" class="modal">
    <div class="modal-content">
      <h2>🎨 Theme Vault</h2>
      <p style="color:#888;font-size:13px;margin-bottom:16px">Spend 💎 LexiShards to unlock themes.</p>
      <div id="themes-list" style="display:flex;flex-direction:column;gap:10px"></div>
      <button class="btn" style="margin-top:18px" onclick="hideModal()">Close</button>
    </div>
  </div>

  <!-- Stats Modal -->
  <div id="stats-modal" class="modal">
    <div class="modal-content">
      <h2>📊 Daily Streak</h2>
      <p id="streak-text" style="color:#aaa"></p>
      <div class="calendar" id="calendar-grid"></div>
      <button class="btn" style="margin-top:18px" onclick="hideModal()">Close</button>
    </div>
  </div>

  <!-- Achievements Modal -->
  <div id="achievements-modal" class="modal">
    <div class="modal-content">
      <h2>🏆 Achievements</h2>
      <div id="achievements-list" style="max-height:300px;overflow-y:auto;text-align:left;display:flex;flex-direction:column;gap:10px;margin-top:14px"></div>
      <button class="btn" style="margin-top:18px" onclick="hideModal()">Close</button>
    </div>
  </div>

  <!-- Achievement Toast -->
  <div id="achievement-toast">
    <div style="font-size:22px">🏆</div>
    <div>
      <div id="toast-title" style="font-weight:bold;font-size:15px"></div>
      <div id="toast-desc" style="font-size:12px;opacity:.75"></div>
    </div>
  </div>

  <div id="float-container"></div>

  <script>
    const RAW_DICTIONARY = "{raw_dict}";

    class TrieNode {{ constructor() {{ this.c = {{}}; this.e = false; }} }}
    class Trie {{
      constructor() {{ this.root = new TrieNode(); }}
      insert(w) {{ let n=this.root; for(let ch of w){{if(!n.c[ch])n.c[ch]=new TrieNode();n=n.c[ch];}} n.e=true; }}
      check(w) {{ let n=this.root; for(let ch of w){{if(!n.c[ch])return 0;n=n.c[ch];}} return n.e?2:1; }}
    }}
    const dictTrie = new Trie();

    {stages_match.group(1)}
    {biomes_match.group(1)}
    {achvs_match.group(1)}
    {letter_pts_match.group(1)}
    {ad_provider_match.group(1)}
    {audio_engine_match.group(1)}

    let rand = Math.random;
    function mulberry32(a){{ return function(){{ var t=a+=0x6D2B79F5; t=Math.imul(t^t>>>15,t|1); t^=t+Math.imul(t^t>>>7,t|61); return((t^t>>>14)>>>0)/4294967296; }}; }}
    const VOWELS='AAAAEEEEIIIOOOUU', CONS='BBCCDDFFGGHHJKLLMMNNPPRRSSTTVVWWXYYZ';
    function getRandomLetter(){{ return(rand()<.4)?VOWELS[Math.floor(rand()*VOWELS.length)]:CONS[Math.floor(rand()*CONS.length)]; }}
    let COLS=4, ROWS=4, isSubmitting=false, isDragging=false, comboTimer=null, gameTimer=null, focusedTile=-1;
    let STATE = {{ mode:'menu', stage:null, score:0, moves:20, time:120, combo:1, shards:parseInt(localStorage.getItem('lexigrid_shards')||0), board:[], path:[], wordsSubmitted:parseInt(localStorage.getItem('lexigrid_words')||0) }};

    let app, boardContainer, trailGfx, moteContainer;
    let tileSprites = []; 
    const TILE_GAP = 6;
    let BOARD_SIZE=0, TILE_SIZE=0;

    const PALETTES = {{
      slate:   {{ bg:0x1e293b, top:0x283548, active:0x4f46e5, accent:0x818cf8, trail:0xf59e0b, shadow:0x080e1c, frozen:0x93c5fd, bomb:0x7f1d1d, bombBorder:0xef4444, mult2:0xf59e0b, mult3:0xef4444 }},
      cyber:   {{ bg:0x0c1220, top:0x112030, active:0x06b6d4, accent:0x22d3ee, trail:0xec4899, shadow:0x020810, frozen:0x7dd3fc, bomb:0x450a0a, bombBorder:0xf87171, mult2:0xfbbf24, mult3:0xf97316 }},
      amber:   {{ bg:0x27272a, top:0x323236, active:0xea580c, accent:0xfb923c, trail:0xeab308, shadow:0x111113, frozen:0x93c5fd, bomb:0x3b1515, bombBorder:0xfca5a5, mult2:0xfbbf24, mult3:0xf97316 }},
      emerald: {{ bg:0x064e3b, top:0x0a6650, active:0x059669, accent:0x6ee7b7, trail:0x34d399, shadow:0x021a14, frozen:0x7dd3fc, bomb:0x2d0a0a, bombBorder:0xf87171, mult2:0xfbbf24, mult3:0xf97316 }},
      cosmic:  {{ bg:0x2e2663, top:0x3d3280, active:0x9333ea, accent:0xc084fc, trail:0xa855f7, shadow:0x0d0b25, frozen:0x93c5fd, bomb:0x3b0d5c, bombBorder:0xf87171, mult2:0xfbbf24, mult3:0xf97316 }}
    }};
    function pal(){{ return PALETTES[document.documentElement.getAttribute('data-theme')||'slate']||PALETTES.slate; }}

    async function initPixi() {{
      const mount = document.getElementById('pixi-mount');
      BOARD_SIZE = Math.min(window.innerWidth * 0.88, window.innerHeight * 0.50, 420);
      TILE_SIZE  = Math.floor((BOARD_SIZE - TILE_GAP * (COLS + 1)) / COLS);
      const SZ   = TILE_SIZE * COLS + TILE_GAP * (COLS + 1);
      mount.style.width = mount.style.height = SZ + 'px';

      app = new PIXI.Application();
      await app.init({{
        width: SZ, height: SZ,
        backgroundAlpha: 0,
        antialias: true,
        resolution: window.devicePixelRatio || 2,
        autoDensity: true
      }});
      const cv = app.canvas;
      cv.style.width = cv.style.height = SZ + 'px';
      cv.style.display = 'block';
      cv.style.touchAction = 'none';
      mount.appendChild(cv);

      const chassis = new PIXI.Graphics();
      chassis.roundRect(0, 0, SZ, SZ, 16);
      chassis.fill({{ color:0x0a1220, alpha:0.55 }});
      chassis.stroke({{ color:0xffffff, alpha:0.07, width:1 }});
      app.stage.addChild(chassis);

      boardContainer = new PIXI.Container();
      app.stage.addChild(boardContainer);
      trailGfx = new PIXI.Graphics();
      app.stage.addChild(trailGfx);
      moteContainer = new PIXI.Container();
      app.stage.addChild(moteContainer);

      initMotes(SZ);
      app.ticker.add(tickMotes);
      setupInput(cv);
    }}

    function makeTileSprite(td, col, row) {{
      const p = pal(), S = TILE_SIZE, R = 11;
      const x = TILE_GAP + col * (S + TILE_GAP);
      const y = TILE_GAP + row * (S + TILE_GAP);
      const ct = new PIXI.Container();
      ct.x = x; ct.y = y;

      const sh = new PIXI.Graphics();
      sh.roundRect(2, 7, S-2, S-1, R); sh.fill({{ color: p.shadow, alpha: 0.7 }});
      ct.addChild(sh);

      const bg = new PIXI.Graphics();
      paintTile(bg, td.type, false, S, R, p);
      ct.addChild(bg);

      const shine = new PIXI.Graphics();
      shine.roundRect(0, 0, S, S*0.45, R); shine.fill({{ color:0xffffff, alpha:0.09 }});
      ct.addChild(shine);

      const lbl = new PIXI.Text({{
        text: td.type==='wild' ? '?' : td.letter,
        style: new PIXI.TextStyle({{
          fontFamily: 'Segoe UI, system-ui, sans-serif',
          fontSize: Math.floor(S * 0.41), fontWeight: '800',
          fill: td.type==='frozen' ? 0xbae6fd : (td.type==='wild' ? p.trail : 0xf1f5f9),
          dropShadow: {{ color:0x000000, blur:4, distance:1, alpha:.7 }}
        }})
      }});
      lbl.anchor.set(0.5); lbl.x = S/2; lbl.y = S/2 - 2;
      ct.addChild(lbl);

      if (td.type !== 'bomb' && td.type !== 'wild') {{
        const pts = LETTER_PTS[td.letter] || 1;
        const badge = new PIXI.Text({{ text: String(pts), style: new PIXI.TextStyle({{ fontFamily:'Segoe UI,sans-serif', fontSize:Math.floor(S*.14), fontWeight:'700', fill:0xffffff }}) }});
        badge.alpha = 0.4; badge.anchor.set(1,1); badge.x = S-4; badge.y = S-4;
        ct.addChild(badge);
      }}

      if (td.type === 'bomb') {{
        const cb = new PIXI.Text({{ text: String(td.countdown||5), style: new PIXI.TextStyle({{ fontFamily:'Segoe UI,sans-serif', fontSize:Math.floor(S*.2), fontWeight:'900', fill:0xffffff }}) }});
        cb.name = 'cb'; cb.anchor.set(0.5,0); cb.x=S/2; cb.y=4;
        ct.addChild(cb);
      }}

      ct.eventMode = 'static';
      ct.hitArea = new PIXI.Rectangle(0, 0, S, S);
      boardContainer.addChild(ct);
      const sp = {{ container:ct, bg, lbl, tileData:td, pxX:x, pxY:y }};
      return sp;
    }}

    function paintTile(g, type, selected, S, R, p) {{
      g.clear();
      if (selected) {{
        g.roundRect(0,0,S,S,R); g.fill({{ color:p.active }}); g.stroke({{ color:p.accent, alpha:.8, width:2 }});
      }} else if (type==='mult2') {{
        g.roundRect(0,0,S,S,R); g.fill({{ color:p.bg }}); g.stroke({{ color:p.mult2, alpha:.9, width:2 }});
      }} else if (type==='mult3') {{
        g.roundRect(0,0,S,S,R); g.fill({{ color:p.bg }}); g.stroke({{ color:p.mult3, alpha:.9, width:2 }});
      }} else if (type==='frozen') {{
        g.roundRect(0,0,S,S,R); g.fill({{ color:0x1d4ed8, alpha:.4 }}); g.stroke({{ color:p.frozen, alpha:.7, width:2 }});
      }} else if (type==='bomb') {{
        g.roundRect(0,0,S,S,R); g.fill({{ color:p.bomb }}); g.stroke({{ color:p.bombBorder, alpha:.85, width:2 }});
      }} else {{
        g.roundRect(0,0,S,S,R); g.fill({{ color:p.top }});
        g.stroke({{ color:0xffffff, alpha:.07, width:1 }});
      }}
    }}

    function refreshSprite(sp) {{
      const p = pal(), S = TILE_SIZE, R = 11;
      const t = sp.tileData;
      const sel = STATE.path.includes(t);
      paintTile(sp.bg, t.type, sel, S, R, p);
      sp.lbl.text = (t.type==='wild') ? (t.actualLetter||'?') : t.letter;
      sp.lbl.style.fill = t.type==='frozen' ? 0xbae6fd : (t.type==='wild' ? p.trail : 0xf1f5f9);
      const cb = sp.container.getChildByName('cb');
      if (cb) cb.text = String(t.countdown);
    }}

    function canvasCoords(e, cv) {{
      const r = cv.getBoundingClientRect();
      const sx = (app.canvas.width / app.renderer.resolution) / r.width;
      const sy = (app.canvas.height / app.renderer.resolution) / r.height;
      return {{ x:(e.clientX - r.left)*sx, y:(e.clientY - r.top)*sy }};
    }}
    function hitTest(lx, ly) {{
      for (const sp of tileSprites) {{
        if (lx>=sp.pxX && lx<=sp.pxX+TILE_SIZE && ly>=sp.pxY && ly<=sp.pxY+TILE_SIZE) return sp;
      }}
      return null;
    }}
    function setupInput(cv) {{
      cv.addEventListener('pointerdown', e=>{{ if(isSubmitting)return; AudioEngine.init(); const {{x,y}}=canvasCoords(e,cv); const sp=hitTest(x,y); if(sp){{isDragging=true;STATE.path=[];enterTile(sp);}} e.preventDefault(); }},{{passive:false}});
      window.addEventListener('pointermove', e=>{{ if(!isDragging||isSubmitting)return; const {{x,y}}=canvasCoords(e,app.canvas); const sp=hitTest(x,y); if(sp)enterTile(sp); }});
      window.addEventListener('pointerup', ()=>{{ if(isDragging){{isDragging=false;submitWord();}} }});
    }}

    function enterTile(sp) {{
      const t = sp.tileData;
      if (STATE.path.includes(t)) {{
        const idx = STATE.path.indexOf(t);
        if (idx < STATE.path.length-1) {{
          const removed = STATE.path.splice(idx+1);
          removed.forEach(pt => {{ const s=tileSprites.find(x=>x.tileData===pt); if(s){{gsap.to(s.container,{{scaleX:1,scaleY:1,duration:.15,ease:'back.out(2)'}});refreshSprite(s);}} }});
          AudioEngine.note(STATE.path.length-1); drawTrail();
        }}
        return;
      }}
      if (STATE.path.length > 0) {{
        const last = STATE.path[STATE.path.length-1];
        if (Math.abs(last.r-t.r)>1 || Math.abs(last.c-t.c)>1) return;
      }}
      STATE.path.push(t);
      if (t.type==='wild') {{
        let p=STATE.path.map(x=>x.actualLetter).join('').slice(0,-1);
        t.actualLetter='A';
        for(let ch of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'){{if(dictTrie.check(p+ch)>0){{t.actualLetter=ch;break;}}}}
      }} else t.actualLetter=t.letter;
      gsap.killTweensOf(sp.container,{{scaleX:true,scaleY:true}});
      gsap.to(sp.container,{{scaleX:.87,scaleY:1.15,duration:.08,ease:'power2.out',onComplete:()=>gsap.to(sp.container,{{scaleX:1,scaleY:1,duration:.3,ease:'back.out(2.5)'}}),}});
      refreshSprite(sp);
      AudioEngine.note(STATE.path.length-1);
      drawTrail();
      const word = STATE.path.map(x=>x.actualLetter).join('');
      const wd = document.getElementById('word-display');
      wd.innerText = word;
      const st = dictTrie.check(word);
      wd.style.color = st===2?'#4ade80':(st===1?'var(--trail-color)':'#f87171');
      wd.style.textShadow = st===2?'0 0 20px #4ade80':(st===1?'0 0 20px var(--trail-color)':'0 0 20px #f87171');
    }}

    function drawTrail() {{
      trailGfx.clear();
      if (STATE.path.length < 2) return;
      const p = pal();
      const word = STATE.path.map(x=>x.actualLetter).join('');
      const valid = dictTrie.check(word);
      const color = valid===2 ? 0x4ade80 : (valid===1 ? p.trail : 0xf87171);
      const pts = STATE.path.map(t=>{{ const sp=tileSprites.find(s=>s.tileData===t); if(!sp)return null; return {{x:sp.pxX+TILE_SIZE/2, y:sp.pxY+TILE_SIZE/2}}; }}).filter(Boolean);
      if (pts.length < 2) return;
      trailGfx.moveTo(pts[0].x,pts[0].y);
      for(let i=1;i<pts.length;i++)trailGfx.lineTo(pts[i].x,pts[i].y);
      trailGfx.stroke({{color,width:14,alpha:.22,cap:'round',join:'round'}});
      trailGfx.moveTo(pts[0].x,pts[0].y);
      for(let i=1;i<pts.length;i++)trailGfx.lineTo(pts[i].x,pts[i].y);
      trailGfx.stroke({{color,width:4.5,alpha:.95,cap:'round',join:'round'}});
      const L=pts[pts.length-1];
      trailGfx.circle(L.x,L.y,7); trailGfx.fill({{color,alpha:.85}});
    }}

    function clearPath() {{
      STATE.path.forEach(t=>{{ const sp=tileSprites.find(s=>s.tileData===t); if(sp){{gsap.to(sp.container,{{scaleX:1,scaleY:1,duration:.2}});refreshSprite(sp);}} }});
      STATE.path=[];
      trailGfx.clear();
      const wd=document.getElementById('word-display');
      wd.innerText=''; wd.style.color=''; wd.style.textShadow='';
    }}

    function pixiToScreen(lx, ly) {{
      const r = app.canvas.getBoundingClientRect();
      const lw = app.canvas.width / app.renderer.resolution;
      const lh = app.canvas.height / app.renderer.resolution;
      return {{ x: r.left + lx * (r.width/lw), y: r.top + ly * (r.height/lh) }};
    }}

    function submitWord() {{
      if(STATE.path.length < 3) {{ clearPath(); return; }}
      isSubmitting = true;
      let word = STATE.path.map(x=>x.actualLetter).join('');
      if(dictTrie.check(word) === 2) {{
          checkAchv('first_word');
          if(word.length >= 6) checkAchv('long_word');
          STATE.wordsSubmitted++; localStorage.setItem('lexigrid_words', STATE.wordsSubmitted);
          if(STATE.wordsSubmitted >= 100) checkAchv('lifetime_100');
          
          AudioEngine.valid();
          if (word.length >= 5) {{
             gsap.to(document.getElementById('pixi-mount'), {{x:7,duration:.04,ease:'power1.inOut',yoyo:true,repeat:4,onComplete:()=>gsap.set(document.getElementById('pixi-mount'),{{x:0}})}});
          }}
          let base = [0,0,0,100,200,400,700,1100,1600][Math.min(word.length, 8)];
          let mult = 1, usedWild = false;
          STATE.path.forEach(t => {{
              if(t.type==='mult2') mult *= 2; if(t.type==='mult3') mult *= 3;
              if(t.type==='wild') usedWild = true;
          }});
          if(usedWild) checkAchv('wildcard_use');
          
          let pts = Math.floor(base * mult * STATE.combo);
          STATE.score += pts;
          if(STATE.score >= 1000) checkAchv('score_1000');
          
          let lastSp = tileSprites.find(s=>s.tileData===STATE.path[STATE.path.length-1]);
          if(lastSp) {{
              const sc = pixiToScreen(lastSp.pxX+TILE_SIZE/2, lastSp.pxY+TILE_SIZE/2);
              floatScore(pts, sc.x, sc.y, word.length>=5);
              burstAt(lastSp.pxX+TILE_SIZE/2, lastSp.pxY+TILE_SIZE/2);
          }}
          
          STATE.shards += (word.length==4?5:(word.length==5?15:(word.length>=6?35:0)));
          localStorage.setItem('lexigrid_shards', STATE.shards);
          if(STATE.shards >= 500) checkAchv('shards_500');
          
          STATE.combo = Math.min(3, STATE.combo + 0.5);
          if(STATE.combo >= 2.5) checkAchv('combo_5');
          clearTimeout(comboTimer);
          comboTimer = setTimeout(() => {{ STATE.combo = 1; updateHUD(); }}, 5000);
          
          let toRemove = [];
          STATE.path.forEach(t => {{
              const sp = tileSprites.find(s=>s.tileData===t);
              if(t.type==='frozen') {{
                  if(!t.cracked) {{ t.cracked = true; refreshSprite(sp); AudioEngine.shatter(); }}
                  else {{ toRemove.push(t); checkAchv('ice_break'); if(sp) iceShatter(sp); }}
              }} else {{
                  toRemove.push(t);
              }}
              if(t.type==='bomb') {{ 
                  AudioEngine.shatter(); 
                  if(sp) bombBlast(sp); 
                  checkAchv('bomb_defuse'); 
              }}
          }});
          
          STATE.board.flat().forEach(t => {{
              if(t.type==='bomb' && !toRemove.includes(t)) {{
                  t.countdown--; 
                  const sp = tileSprites.find(s=>s.tileData===t);
                  if(sp) refreshSprite(sp);
                  if(t.countdown<=0) {{
                      STATE.score = Math.max(0, STATE.score - 500); t.type = 'normal'; if(sp)refreshSprite(sp); AudioEngine.invalid();
                      gsap.to(document.getElementById('pixi-mount'), {{x:7,duration:.04,ease:'power1.inOut',yoyo:true,repeat:4,onComplete:()=>gsap.set(document.getElementById('pixi-mount'),{{x:0}})}});
                  }}
              }}
          }});
          
          collapse(toRemove);
          if(STATE.mode !== 'blitz') STATE.moves--;
          checkWinLoss();
      }} else {{ AudioEngine.invalid(); clearPath(); isSubmitting = false; }}
      updateHUD();
    }}

    function createTile(r, c) {{
      let letter = getRandomLetter();
      return {{ id: r*100+c+rand(), r, c, letter, type: 'normal', countdown: 0, actualLetter: letter }};
    }}

    function collapse(toRemove) {{
      toRemove.forEach(t => {{
          const sp = tileSprites.find(s=>s.tileData===t);
          if(sp) {{
              gsap.to(sp.container, {{alpha:0, scaleX:1.3, scaleY:1.3, duration:.2, onComplete:() => {{
                  boardContainer.removeChild(sp.container);
                  tileSprites = tileSprites.filter(x=>x!==sp);
              }}}});
          }}
      }});
      for(let c=0; c<COLS; c++) {{
          let write = ROWS - 1;
          for(let r=ROWS-1; r>=0; r--) {{
              let t = STATE.board[r][c];
              if(!toRemove.includes(t)) {{ 
                  STATE.board[write][c] = t; 
                  t.r = write; 
                  const sp = tileSprites.find(s=>s.tileData===t);
                  if(sp) {{
                      const newY = TILE_GAP + write * (TILE_SIZE + TILE_GAP);
                      sp.pxY = newY;
                      gsap.to(sp.container, {{y:newY, duration:.35, ease:'bounce.out', delay:.18}});
                  }}
                  write--; 
              }}
          }}
          for(let r=write; r>=0; r--) {{ 
              let t = createTile(r, c); 
              STATE.board[r][c] = t; 
              const sp = makeTileSprite(t, c, r);
              const targetY = sp.pxY;
              sp.container.y = targetY - (ROWS * (TILE_SIZE + TILE_GAP));
              gsap.to(sp.container, {{y:targetY, duration:.35, ease:'bounce.out', delay:.18}});
              tileSprites.push(sp);
          }}
      }}
      clearPath(); setTimeout(() => {{ isSubmitting = false; }}, 400);
    }}

    const motePool = [];
    function initMotes(SZ) {{
      for(let i=0;i<20;i++) {{
        const g=new PIXI.Graphics();
        const r=Math.random()*1.5+.4;
        g.circle(0,0,r); g.fill({{color:0x818cf8,alpha:1}});
        g.x=Math.random()*SZ; g.y=Math.random()*SZ; g.alpha=Math.random()*.25+.06;
        motePool.push({{g,vx:(Math.random()-.5)*.4,vy:(Math.random()-.5)*.4,SZ}});
        moteContainer.addChild(g);
      }}
    }}
    function tickMotes() {{
      motePool.forEach(m=>{{ m.g.x+=m.vx; m.g.y+=m.vy; if(m.g.x<0)m.g.x=m.SZ; if(m.g.x>m.SZ)m.g.x=0; if(m.g.y<0)m.g.y=m.SZ; if(m.g.y>m.SZ)m.g.y=0; }});
    }}
    function burstAt(lx, ly) {{
      const p=pal();
      for(let i=0;i<12;i++) {{
        const g=new PIXI.Graphics(); g.circle(0,0,Math.random()*3+1.5); g.fill({{color:p.trail,alpha:1}});
        g.x=lx; g.y=ly; app.stage.addChild(g);
        const a=Math.random()*Math.PI*2,spd=Math.random()*5+3;
        gsap.to(g,{{x:lx+Math.cos(a)*spd*16,y:ly+Math.sin(a)*spd*16,alpha:0,duration:.7+Math.random()*.4,ease:'power2.out',onComplete:()=>app.stage.removeChild(g)}});
      }}
    }}
    function iceShatter(sp) {{
      const cx=sp.pxX+TILE_SIZE/2, cy=sp.pxY+TILE_SIZE/2;
      for(let i=0;i<8;i++) {{
        const g=new PIXI.Graphics(); const sz=Math.random()*8+3;
        g.rect(-sz/2,-sz/2,sz,sz); g.fill({{color:0x93c5fd,alpha:1}}); g.rotation=Math.random()*Math.PI*2;
        g.x=cx; g.y=cy; app.stage.addChild(g);
        const a=Math.random()*Math.PI*2,spd=Math.random()*4+2;
        gsap.to(g,{{x:cx+Math.cos(a)*spd*20,y:cy+Math.sin(a)*spd*20+45,rotation:Math.random()*8,alpha:0,duration:.9,ease:'power2.out',onComplete:()=>app.stage.removeChild(g)}});
      }}
    }}
    function bombBlast(sp) {{
      const cx=sp.pxX+TILE_SIZE/2, cy=sp.pxY+TILE_SIZE/2;
      const ring=new PIXI.Graphics(); ring.circle(0,0,12); ring.stroke({{color:0xef4444,alpha:.9,width:3}});
      ring.x=cx; ring.y=cy; app.stage.addChild(ring);
      gsap.to(ring,{{pixi:{{scaleX:7,scaleY:7}},alpha:0,duration:.55,ease:'power2.out',onComplete:()=>app.stage.removeChild(ring)}});
      for(let i=0;i<16;i++) {{
        const g=new PIXI.Graphics(); g.circle(0,0,2.5); g.fill({{color:0xfca5a5,alpha:1}});
        g.x=cx; g.y=cy; app.stage.addChild(g);
        const a=Math.random()*Math.PI*2,spd=Math.random()*7+4;
        gsap.to(g,{{x:cx+Math.cos(a)*spd*20,y:cy+Math.sin(a)*spd*20+30,alpha:0,duration:.8,ease:'power2.out',onComplete:()=>app.stage.removeChild(g)}});
      }}
    }}
    function floatScore(pts, sx, sy, big) {{
      const el=document.createElement('div'); el.className='float-tag';
      el.style.cssText=`left:${{sx}}px;top:${{sy}}px;color:${{big?'#4ade80':'var(--trail-color)'}};font-size:${{big?'32px':'26px'}};`;
      el.innerText=`+${{pts}}${{big?' ✨':''}}`;
      document.getElementById('float-container').appendChild(el);
      gsap.to(el,{{y:-70,x:(Math.random()-.5)*40,alpha:0,scale:big?1.4:.95,rotation:(Math.random()-.5)*16,duration:1.15,ease:'power2.out',onComplete:()=>el.remove()}});
    }}

    function checkWinLoss() {{
      if(STATE.mode === 'adventure') {{
          let st = STAGES[STATE.stage-1], won = false;
          if(st.target && STATE.score >= st.target) won = true;
          if(st.frozen && STATE.board.flat().filter(t=>t.type==='frozen').length===0) won = true;
          if(st.bomb && STATE.board.flat().filter(t=>t.type==='bomb').length===0) won = true;
          if(won) endGame(true); else if(STATE.moves <= 0) endGame(false);
      }} else if (STATE.mode !== 'blitz' && STATE.moves <= 0) endGame(false);
    }}
    
    function endGame(won) {{
      AdProvider.gameplayStop(); clearInterval(gameTimer);
      let starsStr = won ? (STATE.moves >= STAGES[STATE.stage-1].moves*0.5 ? '⭐⭐⭐' : (STATE.moves >= STAGES[STATE.stage-1].moves*0.25 ? '⭐⭐' : '⭐')) : '❌';
      document.getElementById('end-title').innerText = won ? "Stage Clear!" : "Game Over";
      document.getElementById('end-desc').innerText = won ? `You earned 100 💎!` : `Better luck next time.`;
      document.getElementById('end-stars').innerText = STATE.mode==='adventure' ? starsStr : `Score: ${{STATE.score}}`;
      
      if(won && STATE.mode === 'adventure') {{
          STATE.shards += 100; localStorage.setItem('lexigrid_shards', STATE.shards);
          let adv = JSON.parse(localStorage.getItem('lexigrid_adventure')||'{{}}');
          adv[STATE.stage] = Math.max(adv[STATE.stage]||0, starsStr.length);
          localStorage.setItem('lexigrid_adventure', JSON.stringify(adv));
          AudioEngine.play([523, 659, 784, 1047], 'sine', 0.2);
          
          let clearedCount = Object.keys(adv).length;
          if(clearedCount >= 3) checkAchv('adventure_3');
          if(Object.values(adv).filter(x=>x===3).length >= 5) checkAchv('adventure_3stars');
      }}
      if(STATE.mode === 'daily') {{
          let log = JSON.parse(localStorage.getItem('lexigrid_daily_log')||'[]');
          let today = new Date().toISOString().split('T')[0];
          if(!log.includes(today)) {{ log.push(today); localStorage.setItem('lexigrid_daily_log', JSON.stringify(log)); }}
          if(log.length >= 7) checkAchv('streak_7');
      }}
      showModal('end-modal');
    }}
    
    function checkAchv(id) {{
      let a = JSON.parse(localStorage.getItem('lexigrid_achievements')||'[]');
      if(!a.includes(id)) {{
          a.push(id); localStorage.setItem('lexigrid_achievements', JSON.stringify(a));
          let ac = ACHVS.find(x=>x.id===id);
          document.getElementById('toast-title').innerText = ac.n;
          document.getElementById('toast-desc').innerText = ac.d;
          document.getElementById('achievement-toast').classList.add('show');
          AudioEngine.achievement();
          setTimeout(()=>document.getElementById('achievement-toast').classList.remove('show'), 4000);
      }}
    }}
    function populateAchvModal() {{
      let list = document.getElementById('achievements-list'); list.innerHTML='';
      let a = JSON.parse(localStorage.getItem('lexigrid_achievements')||'[]');
      ACHVS.forEach(ac => {{
          let d = document.createElement('div');
          d.style.padding = '10px'; d.style.background = 'rgba(255,255,255,0.05)'; d.style.borderRadius = '8px';
          d.innerHTML = `<b>${{a.includes(ac.id)?'✅':'🔒'}} ${{ac.n}}</b><br><small>${{ac.d}}</small>`;
          list.appendChild(d);
      }});
    }}

    function updateHUD() {{
      const scoreEl = document.getElementById('ui-score');
      const prev = scoreEl.innerText;
      scoreEl.innerText = STATE.score;
      if (String(STATE.score) !== prev) {{
          scoreEl.classList.remove('pop'); void scoreEl.offsetWidth;
          scoreEl.classList.add('pop');
          setTimeout(() => scoreEl.classList.remove('pop'), 300);
      }}
      document.getElementById('ui-moves').innerText = STATE.moves;
      document.getElementById('ui-time').innerText = STATE.time;
      document.getElementById('ui-combo').innerText = STATE.combo + 'x';
      document.getElementById('ui-shards').innerText = STATE.shards;
    }}
    function showModal(id) {{ document.querySelectorAll('.modal').forEach(m=>m.classList.remove('active')); document.getElementById(id).classList.add('active'); }}
    function hideModal() {{ document.querySelectorAll('.modal').forEach(m=>m.classList.remove('active')); }}
    
    function openStageSelect() {{
      let grid = document.getElementById('stage-grid'); grid.innerHTML='';
      let adv = JSON.parse(localStorage.getItem('lexigrid_adventure')||'{{}}');
      STAGES.forEach(st => {{
          let unlocked = st.id===1 || adv[st.id-1];
          let btn = document.createElement('div');
          btn.className = `stage-btn ${{unlocked?'unlocked':''}}`;
          btn.innerHTML = `<div>${{st.id}}</div><div class="stars-row ${{adv[st.id]?'lit':''}}">${{'⭐'.repeat(adv[st.id]||0)}}</div>`;
          if(unlocked) btn.onclick = () => startGame('adventure', st.id);
          grid.appendChild(btn);
      }});
      showModal('stage-modal');
    }}

    function refreshAllTiles() {{
      tileSprites.forEach(sp=>refreshSprite(sp)); drawTrail();
    }}
    
    function setupThemes() {{
      let list = document.getElementById('themes-list'); list.innerHTML='';
      let unlocked = JSON.parse(localStorage.getItem('lexigrid_themes')||'["slate"]');
      BIOMES.forEach(b => {{
          let btn = document.createElement('button'); btn.className = 'btn';
          let isU = unlocked.includes(b.id) || b.cost===0;
          btn.innerText = `${{b.name}} ${{isU ? '' : '(100💎)'}}`;
          btn.onclick = () => {{
              if(isU) {{ document.documentElement.setAttribute('data-theme', b.id); localStorage.setItem('lexigrid_theme', b.id); hideModal(); refreshAllTiles(); }}
              else if(STATE.shards >= 100) {{
                  STATE.shards -= 100; localStorage.setItem('lexigrid_shards', STATE.shards);
                  unlocked.push(b.id); localStorage.setItem('lexigrid_themes', JSON.stringify(unlocked));
                  setupThemes(); updateHUD();
              }}
          }};
          list.appendChild(btn);
      }});
      document.documentElement.setAttribute('data-theme', localStorage.getItem('lexigrid_theme')||'slate');
    }}
    
    function showStatsModal() {{
      let cal = document.getElementById('calendar-grid'); cal.innerHTML='';
      let log = JSON.parse(localStorage.getItem('lexigrid_daily_log')||'[]');
      for(let i=1; i<=30; i++) {{
          let d = document.createElement('div');
          d.className = 'cal-day ' + (log.length>=i ? 'done' : '');
          d.innerText = i; cal.appendChild(d);
      }}
      document.getElementById('streak-text').innerText = `Current Streak: ${{log.length}} days`;
      showModal('stats-modal');
    }}
    
    function toggleMute() {{
      let m = localStorage.getItem('lexigrid_muted')==='1'; localStorage.setItem('lexigrid_muted', m ? '0' : '1');
      document.getElementById('btn-mute').innerText = m ? '🔊' : '🔇';
    }}
    function shareResult() {{
      let text = `LexiGrid ${{STATE.mode}} 🟩\\nScore: ${{STATE.score}}\\nhttps://snappgrid.com/lexigrid`;
      if(navigator.clipboard) navigator.clipboard.writeText(text);
      let btn = document.getElementById('end-next-btn');
      btn.innerText = "Copied!"; setTimeout(()=>btn.innerText="Continue", 2000);
    }}
    
    function initBoard() {{
      boardContainer.removeChildren(); tileSprites=[];
      STATE.board = [];
      for(let r=0; r<ROWS; r++) {{
          let row = [];
          for(let c=0; c<COLS; c++) {{ let t = createTile(r, c); row.push(t); }}
          STATE.board.push(row);
      }}
      
      if(STATE.mode === 'adventure') {{
          let st = STAGES[STATE.stage-1];
          let specialCount = (st.frozen||0) + (st.bomb||0);
          let flat = STATE.board.flat().sort(() => rand() - 0.5);
          for(let i=0; i<specialCount; i++) {{
              if(i < (st.frozen||0)) flat[i].type = 'frozen';
              else {{ flat[i].type = 'bomb'; flat[i].countdown = 5; }}
          }}
      }} else if(STATE.mode !== 'daily') {{
          let flat = STATE.board.flat();
          flat[Math.floor(rand()*16)].type = 'wild';
          flat[Math.floor(rand()*16)].type = (rand()>0.5?'mult2':'mult3');
      }}
      
      for(let r=0; r<ROWS; r++) {{
          for(let c=0; c<COLS; c++) {{
              let t = STATE.board[r][c];
              let sp = makeTileSprite(t, c, r);
              tileSprites.push(sp);
          }}
      }}
    }}

    function startGame(mode, stageId=null) {{
      STATE.mode = mode; STATE.stage = stageId;
      STATE.score = 0; STATE.combo = 1; STATE.path = [];
      COLS = (mode==='blitz' && localStorage.getItem('lexigrid_expert')==='1') ? 5 : 4; ROWS = COLS;
      document.documentElement.style.setProperty('--cols', COLS);
      document.documentElement.style.setProperty('--rows', ROWS);
      
      if(mode === 'daily') {{
          let d = new Date(); rand = mulberry32(d.getFullYear()*10000 + (d.getMonth()+1)*100 + d.getDate());
      }} else rand = Math.random;
      
      if(mode === 'blitz') {{ STATE.time = 120; document.getElementById('ui-time-box').style.display='flex'; document.getElementById('ui-moves-box').style.display='none'; }}
      else {{ STATE.moves = (stageId ? STAGES[stageId-1].moves : 20); document.getElementById('ui-time-box').style.display='none'; document.getElementById('ui-moves-box').style.display='flex'; }}
      
      initBoard(); updateHUD(); hideModal();
      document.getElementById('objective-text').innerText = stageId ? STAGES[stageId-1].desc : (mode==='collapse'?"Survive!":(mode==='daily'?"Daily Challenge":"Score max in 120s!"));
      
      clearInterval(gameTimer);
      if(mode === 'blitz') {{
          gameTimer = setInterval(() => {{
              STATE.time--; updateHUD();
              if(STATE.time<=0) endGame(false);
          }}, 1000);
      }}
      AdProvider.gameplayStart();
    }}

    window.addEventListener('keydown', e => {{
      if(e.key==='Escape') {{ clearPath(); return; }}
      
      const total = tileSprites.length;
      if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key)) {{
          e.preventDefault();
          if(focusedTile < 0) focusedTile = 0;
          else if(e.key==='ArrowRight') focusedTile = Math.min(focusedTile + 1, total - 1);
          else if(e.key==='ArrowLeft')  focusedTile = Math.max(focusedTile - 1, 0);
          else if(e.key==='ArrowDown')  focusedTile = Math.min(focusedTile + COLS, total - 1);
          else if(e.key==='ArrowUp')    focusedTile = Math.max(focusedTile - COLS, 0);
          updateTileFocus();
          return;
      }}
      if(e.key==='Enter' || e.key===' ') {{
          e.preventDefault();
          if(focusedTile >= 0 && STATE.board) {{
              const row = Math.floor(focusedTile / COLS);
              const col = focusedTile % COLS;
              const tile = STATE.board[row] && STATE.board[row][col];
              if(tile) {{
                  if(STATE.path.includes(tile) && STATE.path.length > 1) submitWord();
                  else if(!STATE.path.includes(tile)) {{
                      const sp = tileSprites.find(s=>s.tileData===tile);
                      if(sp) enterTile(sp);
                  }}
              }}
          }}
      }}
    }});
    
    function updateTileFocus() {{
      tileSprites.forEach(sp => {{
          gsap.to(sp.container, {{alpha:1, scaleX:1, scaleY:1, duration:0.1}});
      }});
      if(focusedTile < 0) return;
      const row = Math.floor(focusedTile / COLS);
      const col = focusedTile % COLS;
      const tile = STATE.board[row] && STATE.board[row][col];
      if(tile) {{
          const sp = tileSprites.find(s=>s.tileData===tile);
          if(sp) {{
              gsap.to(sp.container, {{alpha:0.8, scaleX:0.95, scaleY:0.95, duration:0.1}});
          }}
      }}
    }}

    window.addEventListener('load', async () => {{
      RAW_DICTIONARY.split(' ').forEach(w=>dictTrie.insert(w.toUpperCase()));
      await initPixi();
      setupThemes();
      document.getElementById('btn-mute').innerText = localStorage.getItem('lexigrid_muted')==='1'?'🔇':'🔊';
      document.getElementById('loadingScreen').style.opacity='0';
      setTimeout(()=>document.getElementById('loadingScreen').style.display='none',500);
      AdProvider.gameLoadingFinished();
    }});
  </script>
</body>
</html>"""

with open('d:/snappgrid-main/games/lexigrid/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
