const ANSWERS=["CRANE","STALE","FLINT","BRAVE","GLYPH","QUERY","JUMPY","WALTZ","BOXER","VIXEN","JAZZY","QUIRK","MONKS","PROXY","BLAZE","CRYPT","DRAFT","EASEL","FROWN","GLOOM","HASTE","INTER","JOUST","KNAVE","LODGE","MOTTO","NYMPH","OPTIC","PLUMB","QUEST","RAVEN","SCALD","THORN","UNTIE","VAPOR","WHIRL","YACHT","ZONAL","ADORN","BLUNT","CHASM","DELTA","EXPEL","FIXED","GROAN","HAVOC","IMPEL","JELLY","KEEPS","LEMON","MIRTH","NATCH","OLIVE","PIVOT","QUELL","ROGUE","SINEW","TROVE","UPPER","VICAR","WRATH","YODEL","ZIPPY","ALPHA","BROOD","CLOTH","DWARF","EMBER","FROTH","GRIMY","HOUND","IRONY","JAUNT","KNEEL","LUNAR","MANGO","NERVE","OTTER","PLAIT","QUOTA","REPAY","SHRUG","TIDAL","ULTRA","VEINY","WOKEN","YOUNG","ZESTY","ABBOT","BIRCH","CLOWN","ELITE","FLICK","GRUEL","HYENA","IDIOM","JEWEL","KNACK","LILAC","MAGIC","NIGHT","OCTET","PIXEL","QUALM","RIVET","SNOWY","TUTOR","USHER","VIPER","WIDOW","BLOOM","COMET","DENIM","FLAIR","GUILD","HEATH","IGLOO","JOKER","LITHE","MANOR","NASAL","POLYP","QUEEN","REBUS","SKULL","TIMID","VIGOR","WRECK","YEARN","ABBEY","BASIC","CLASH","DINER","ETHOS","FOCUS","GORGE","HATCH","INFER","KARMA","LATCH","MEDAL","NOTCH","POKER","REBEL","SHADE","TITHE","UNCUT","VALVE","WEIGH","MAXIM","BRINE","CRIMP","DEPOT","ENVOY","FJORD","GRAFT","HAVEN","IMPLY","JUROR","LUSTY","MAPLE","NIFTY","OUTDO","PLAZA","QUAFF","ROOST","STERN","TIARA","VIOLA","WRING","ALTAR","BENCH","CRAVE","DWELT","EERIE","FUNGI","GRAZE","HIKER","INLAY","LANCE","OAKEN","PIZZA","RATIO","RISKY","SIREN","TACKY","VINYL","ZEBRA","ANNEX","BARGE","CEDAR","DIZZY","EVOKE","FEVER","GAVEL","HIPPO","LIBEL","MURKY","NIECE","PRAWN","ROVER","SHIRT","THUMB","VEXED","WITTY","AMINO","BOLTS","CELLO","DISCO","FIZZY","GLOVE","HERBY","LOBBY","MERRY","NUTTY","OCHRE","PERKY","RADAR","SCALP","SNIFF","TEPID","UPEND","VOCAB","WHISK","ATOLL","BLAND","CURLY","EPOCH","FLANK","GREED","HUMID","INGOT","JOKEY","KIOSK","LEAPT","MOULT","NOVEL","OXIDE","PENAL","RUDDY","SQUAT","TAPIR","VAGUE","APTLY","BRASH","CHEAP","DUNCE","ERUPT","FOAMY","GRUFF","HOLLY","ICING","KLUGE","MOPED","PSALM","REPOT","SALVO","UNFED","WEARY","ANGEL","BEIGE","CHIDE","DRIVE","EQUIP","FANCY","GLARE","HUSKY","JAUNT","LIGHT","NOBLE","OVARY","PREEN","QUILT","RELAX","SHEEN","TOWEL","USURP","VIVID","WARDS","ALIBI","BUMPY","CANDY","EXILE","FRONT","GRIPE","IRATE","LINGO","MUNCH","OZONE","PLAID","ABIDE","BIRTH","CATCH","DRIFT","FORTH","INPUT","JOINT","KNOCK","LOWER","MORAL","NURSE","ORBIT","PORCH","QUIET","RANCH","STORM","TOUCH","UNDER","VOTER","WASTE","EXTRA","YIELD","AGAIN","BOUND","DOING","EIGHT","FORCE","GUARD","HEART","IDEAL","LARGE","MINOR","NASAL","OCCUR","PLAIN","RIDER","SINCE","THIRD","UNITY","WORLD","EXACT","BRINK","DEALS","ELDER","FOUND","GRACE","HOUSE","IMAGE","JUDGE","KAYAK","MARSH","NICHE","OPTIC","ABBOT","BOXER","FLINT","BRAVE","QUERY","WALTZ","JAZZY","MONKS","BLAZE","DRAFT","FROWN","INTER","KNAVE","MOTTO","OPTIC","QUEST","SCALD","UNTIE","VAPOR","YACHT","ADORN","CHASM","EXPEL","GROAN","IMPEL","KEEPS","MIRTH","OLIVE","QUELL","SINEW","UPPER","WRATH","ZIPPY","BROOD","DWARF","FROTH","HOUND","JAUNT","LUNAR","NERVE","PLAIT","REPAY","TIDAL","VEINY","ZESTY","BIRCH","ELITE","GRUEL","IDIOM","KNACK","MAGIC","OCTET","QUALM","SNOWY","USHER","WIDOW","COMET","FLAIR","HEATH","JOKER","MANOR","POLYP","REBUS","TIMID","WRECK","ABBEY","CLASH","ETHOS","GORGE","INFER","LATCH","NOTCH","REBEL","TITHE","VALVE","MAXIM","CRIMP","ENVOY","GRAFT","JUROR","MAPLE","PLAZA","ROOST","TIARA","WRING","BENCH","DWELT","FUNGI","HIKER","LANCE","PIZZA","RISKY","TACKY","ZEBRA","BARGE","DIZZY","FEVER","HIPPO","MURKY","PRAWN","SHIRT","VEXED","AMINO","CELLO","FIZZY","HERBY","MERRY","OCHRE","RADAR","SNIFF","UPEND","WHISK","BLAND","EPOCH","GREED","INGOT","KIOSK","MOULT","OXIDE","RUDDY","TAPIR","BRASH","DUNCE","FOAMY","HOLLY","KLUGE","PSALM","SALVO","WEARY","BEIGE","DRIVE","FANCY","HUSKY","LIGHT","OVARY","QUILT","SHEEN","USURP","WARDS","BUMPY","EXILE","GRIPE","MUNCH","PLAID","BIRTH","DRIFT","JOINT","LOWER","NURSE","PORCH","RANCH","TOUCH","VOTER","YIELD","BOUND","EIGHT","GUARD","IDEAL","MINOR","PLAIN","SINCE","UNITY","EXACT","DEALS","FOUND","GRACE","JUDGE","MARSH"];

const VALID=new Set(["ABACI","ABACK","ABASE","ABASH","ABATE","ABBEY","ABBOT","ABHOR","ABIDE","ABOVE","ABUSE","ABYSS","ACUTE","ADAGE","ADDED","ADEPT","ADULT","AFTER","AGAIN","AGAPE","AGILE","AGING","AGLOW","AGONY","AHEAD","AIDED","ALIEN","ALLAY","ALLEY","ALLOT","ALLOW","ALLOY","ALOFT","ALONE","ALONG","ALOOF","ALOUD","ALPHA","AMONG","AMPLE","AMUSE","ANGEL","ANGER","ANGLE","ANGRY","ANIME","ANNEX","ANNOY","ANTIC","ANVIL","APART","APPLY","APRON","APTLY","ARBOR","ARDOR","ARISE","ARMOR","AROMA","AROSE","ARRAY","ARSON","ASHES","ASIDE","ASSET","ATOLL","ATONE","AUDIO","AUDIT","AVAIL","AWARD","AWASH","AWFUL","AWOKE","BAKED","BARGE","BASIC","BEACH","BEADY","BEARD","BEAST","BEGAN","BEGIN","BEING","BEIGE","BELLY","BELTS","BENCH","BIBLE","BIRCH","BISON","BLAND","BLAZE","BLEAT","BLIND","BLINK","BLOCK","BLOOD","BLOOM","BLOWN","BOARD","BOAST","BOGUS","BOLTS","BONDS","BONUS","BOOKS","BOOST","BOTCH","BOUND","BOXER","BRAWL","BRAVE","BREAK","BREED","BRICK","BRINE","BRINK","BROIL","BROKE","BROOD","BRASH","BROTH","BRUNT","BRUSH","BRUTE","BUDDY","BUILD","BUILT","BULGE","BULLY","BUMPY","BURST","BUYER","BYWAY","CABIN","CACHE","CADET","CAMEL","CANDY","CANON","CAPER","CARGO","CARRY","CATCH","CAUSE","CEDAR","CEASE","CHALK","CHAMP","CHANT","CHAOS","CHARM","CHART","CHASE","CHEAP","CHECK","CHEEK","CHEER","CHESS","CHEST","CHIDE","CHIEF","CHILD","CHOIR","CHOSE","CIVIC","CIVIL","CLASH","CLAMP","CLANG","CLAPS","CLASP","CLASS","CLEAN","CLEAR","CLERK","CLICK","CLIFF","CLING","CLOAK","CLOSE","CLOTH","CLOUD","COACH","COAST","COBRA","COILS","COINS","COMIC","COMMA","COMFY","COMET","COULD","COUNT","COURT","COVER","CRACK","CRAFT","CRANE","CRAMP","CRASH","CRAVE","CRAZY","CREAM","CREEK","CRIMP","CRISP","CROSS","CROWD","CROWN","CRUEL","CRUMB","CRUSH","CRYPT","CUBIC","CURLS","CURSE","CYCLE","DAILY","DAIRY","DAISY","DANCE","DEALT","DEALS","DECOY","DELAY","DELTA","DEMON","DENSE","DEPOT","DEPTH","DEVIL","DINER","DISCO","DITCH","DIZZY","DODGE","DOING","DOORS","DOUBT","DOUGH","DOZEN","DRAPE","DRAWL","DREAD","DREAM","DRESS","DRIFT","DRINK","DROOL","DROPS","DROVE","DRUMS","DRUNK","DRYER","DUCHY","DUMPY","DUNCE","DUNES","DWELT","DYING","EAGLE","EARTH","EATEN","EIGHT","ELDER","ELITE","EMBED","EMBER","ENDED","ENEMY","ENJOY","ENSUE","ENTER","ENTRY","ENVOY","EPOCH","EQUAL","EQUIP","ESSAY","ETHOS","EVADE","EVOKE","EVERY","EXACT","EXILE","EXPEL","EXTRA","EXUDE","FABLE","FAILS","FALSE","FANCY","FARCE","FATAL","FAULT","FEAST","FEIGN","FERAL","FETCH","FEVER","FIEND","FIFTH","FIFTY","FIGHT","FINAL","FIRST","FIXED","FJORD","FLAIR","FLAIL","FLAME","FLANK","FLARE","FLASH","FLASK","FLEET","FLESH","FLICK","FLIES","FLINT","FLOOD","FLOOR","FLOSS","FLOUT","FLOWN","FLUID","FLUSH","FOCAL","FOCUS","FOAMY","FOLIO","FOLLY","FORCE","FORGE","FORTH","FORUM","FOUND","FOXES","FOYER","FRAIL","FRANC","FRANK","FRAUD","FREAK","FRESH","FRIED","FROND","FRONT","FROST","FROZE","FROTH","FRUIT","FULLY","FUNGI","FUNNY","GAUNT","GAUZE","GAVEL","GENIE","GENRE","GHOST","GHOUL","GIANT","GIVEN","GLAND","GLASS","GLAZE","GLEAM","GLEAN","GLIDE","GLINT","GLOSS","GLUED","GLYPH","GRABS","GRACE","GRADE","GRAIN","GRAND","GRANT","GRASP","GRASS","GRATE","GRAVE","GRAZE","GREED","GREET","GRIEF","GRIMY","GRILL","GRIPE","GRITS","GROAN","GROIN","GROSS","GROUP","GROUT","GROWL","GROWN","GRUEL","GRUNT","GUARD","GUILD","GUILE","GUISE","GULCH","GUSTS","HABIT","HALVE","HAPPY","HARSH","HASTE","HAUNT","HAVEN","HEART","HEATH","HEIST","HENCE","HERTZ","HINGE","HIKED","HINTS","HIPPO","HOKEY","HOLES","HOLLY","HONEY","HONOR","HORSE","HOTEL","HOURS","HOUSE","HOVER","HOWLS","HUMAN","HUMID","HUMOR","HURRY","HYDRA","HYENA","HYPER","ICING","IDIOM","IMAGE","IMPLY","INDEX","INNER","INPUT","INTER","INTRO","ISSUE","IVORY","JADED","JAUNT","JOKER","JOUST","JUDGE","JUICE","JUICY","JUMBO","JUMPY","KARMA","KAYAK","KEEPS","KLUGE","KNAVE","KNEAD","KNEEL","KNIFE","KNOCK","KNOWN","LABEL","LANCE","LARGE","LASER","LATER","LAUGH","LAYER","LEAKY","LEAPT","LEGAL","LEVEL","LIBEL","LILAC","LINGO","LITHE","LOBBY","LODGE","LOVER","LOWER","LOYAL","LUCKY","LUNAR","LUSTY","LYING","MAFIA","MAGIC","MAJOR","MAKER","MANOR","MAPLE","MARSH","MATCH","MAYOR","MEDIA","MEDAL","MERRY","MESSY","METAL","MIGHT","MINOR","MODEL","MOGUL","MONEY","MONKS","MONTH","MORAL","MORON","MOTOR","MOULT","MOURN","MOUTH","MOVER","MOVIE","MUMMY","MUNCH","MURKY","NAIVE","NASTY","NAVAL","NEEDY","NIGHT","NINJA","NOBLE","NOISE","NORTH","NOTED","NUDGE","NURSE","NYMPH","OCCUR","OCEAN","OFFER","OFTEN","ONSET","OPTIC","ORBIT","ORGAN","OTHER","OUGHT","OUNCE","OUTER","OUTDO","OWNER","OZONE","PADDY","PAINT","PANDA","PANIC","PAPER","PARTY","PATCH","PATIO","PAUSE","PEACE","PEACH","PEARL","PEDAL","PENNY","PERCH","PERIL","PERKY","PETTY","PHASE","PHONE","PHOTO","PIANO","PIECE","PILOT","PINCH","PIXEL","PIZZA","PLANE","PLANK","PLANT","PLATE","PLAID","PLAZA","PLEAD","PLEAT","PLUMB","PLUMP","PLUNK","PLUSH","POACH","POINT","POKER","POLKA","POLYP","PORCH","POSIT","POUCH","POUND","POWER","PRAWN","PRESS","PRICK","PRIDE","PRIME","PRINT","PRIOR","PRIZE","PROBE","PRONE","PROOF","PROSE","PROUD","PSALM","PUNCH","PUPIL","PURGE","PUSHY","PUTTY","PYLON","QUALM","QUERY","QUICK","QUIET","QUITE","QUOTA","QUEEN","QUILL","RABBI","RABID","RADAR","RADIO","RAISE","RALLY","RAMEN","RANCH","RAPID","RASPY","RATED","REACH","REACT","REALM","REBUS","REBEL","REEDY","REGAL","REIGN","RELAX","REPAY","REPEL","RERUN","RESET","RESIN","RIDER","RIGHT","RIPEN","RIVAL","RIVET","RIVER","ROCKY","ROGUE","ROOST","ROUGH","ROUND","ROVER","ROUTE","RUGBY","RULER","RURAL","RUSTY","SADLY","SAINT","SALAD","SALON","SALTY","SANDY","SASSY","SAUCE","SAUNA","SCALD","SCAMP","SCANT","SCARE","SCARF","SCENE","SCONE","SCOPE","SCORE","SCOUR","SCOUT","SCOWL","SCRAM","SCREW","SCUFF","SEIZE","SERVE","SEVEN","SEWER","SHADE","SHAFT","SHAME","SHAPE","SHARK","SHARP","SHAWL","SHEEN","SHEEP","SHELF","SHELL","SHIFT","SHIRT","SHINE","SHOCK","SHONE","SHOOT","SHORE","SHORT","SHOUT","SHOVE","SHOWN","SHRED","SHRUB","SHRUG","SIEGE","SIGMA","SILLY","SINEW","SINCE","SIXTH","SIXTY","SIZED","SIREN","SKATE","SKIER","SKIMP","SKULL","SKIRT","SLACK","SLAIN","SLANG","SLANT","SLASH","SLAVE","SLEEK","SLEPT","SLICE","SLIDE","SLIME","SLINK","SLOPE","SLOTH","SLUMP","SLUNK","SMALL","SMART","SMASH","SMEAR","SMELL","SMILE","SMITE","SMOKE","SNAIL","SNAKE","SNARE","SNEAK","SNARL","SNORE","SNOWY","SOLAR","SOLVE","SONIC","SORRY","SOUTH","SPACE","SPARE","SPARK","SPASM","SPAWN","SPELL","SPICY","SPILL","SPITE","SPLIT","SPOKE","SPOON","SPOUT","SPREE","SPRIG","SQUAD","SQUAT","SQUID","STACK","STAFF","STAGE","STAIN","STAIR","STALE","STAMP","STAND","STARE","START","STATE","STEAD","STEAK","STEAL","STEEP","STEER","STERN","STICK","STIFF","STILL","STING","STOIC","STOLE","STOMP","STONE","STOOD","STOOP","STORM","STORY","STOUT","STOVE","STRAP","STRAW","STRAY","STRIP","STRUT","STUCK","STUDY","STUMP","STUNT","SUAVE","SUGAR","SUITE","SUNNY","SUPER","SURGE","SWAMP","SWATH","SWEAR","SWEAT","SWEEP","SWEET","SWEPT","SWIFT","SWIRL","SWOON","SWORD","SWORE","SWUNG","SYNTH","TABLE","TACKY","TALON","TANGO","TAPIR","TASTE","TAUNT","TAWNY","TEACH","TEASE","TEPID","TENSE","TERSE","THANK","THEIR","THEME","THERE","THESE","THICK","THING","THINK","THORN","THREE","THREW","THROW","THUMB","TIARA","TIDAL","TIGER","TIGHT","TIMID","TIPSY","TITAN","TODAY","TOKEN","TONIC","TOPIC","TOPAZ","TOTAL","TOTEM","TOUCH","TOUGH","TOWEL","TOXIC","TRACE","TRACK","TRADE","TRAIL","TRAIN","TRAMP","TRASH","TRAWL","TREAD","TREAT","TREND","TRIAL","TRICK","TRIED","TROUT","TROVE","TRUMP","TRUST","TRUTH","TULLE","TUNIC","TURBO","TWANG","TWEAK","TWICE","TWIRL","TWIST","TYING","UDDER","ULTRA","UNCUT","UNIFY","UNITE","UNTIL","UNTIE","UPSET","UPEND","URBAN","USAGE","USUAL","USHER","UTTER","VALOR","VALID","VALUE","VALVE","VAPOR","VAULT","VEINY","VENOM","VENUE","VERGE","VERSE","VICAR","VIGOR","VIGIL","VINYL","VIOLA","VIPER","VIRAL","VITAL","VOCAL","VODKA","VOILA","VOCAB","VOMIT","VOTER","VOUCH","VOWEL","VEXED","VIVID","WARDS","WAGER","WAGON","WALTZ","WASTE","WATCH","WATER","WAVER","WEIRD","WHALE","WHEAT","WHERE","WHILE","WHIRL","WHITE","WHOLE","WHOSE","WIDER","WITCH","WITTY","WOKEN","WOMAN","WOMEN","WOODS","WORLD","WORRY","WORSE","WORST","WORTH","WOUND","WRING","WRIST","WRECK","WROTE","WRATH","YACHT","YEARN","YIELD","YOUNG","YODEL","ZEBRA","ZESTY","ZIPPY","ZONAL"]);

let answer,dayNum,guesses,currentRow,currentTile,gameOver,hardMode,soundOn,audioCtx;
let stats={played:0,wins:0,streak:0,maxStreak:0,dist:{}};

function initAudio(){
  if(!audioCtx){try{audioCtx=new(window.AudioContext||window.webkitAudioContext)();}catch(e){}}
  if(audioCtx&&audioCtx.state==='suspended')audioCtx.resume();
}
function tone(freq,dur,type,vol,t0){
  type=type||'sine';vol=vol||0.18;t0=t0||0;
  if(!soundOn||!audioCtx)return;
  try{
    const o=audioCtx.createOscillator(),g=audioCtx.createGain();
    o.connect(g);g.connect(audioCtx.destination);
    o.type=type;o.frequency.value=freq;
    const t=audioCtx.currentTime+t0;
    g.gain.setValueAtTime(vol,t);g.gain.exponentialRampToValueAtTime(0.001,t+dur);
    o.start(t);o.stop(t+dur+0.01);
  }catch(e){}
}
function sndKey(){tone(800,0.04,'sine',0.06);}
function sndDelete(){tone(400,0.05,'sine',0.06);}
function sndSubmit(){tone(600,0.08,'sine',0.1);}
function sndInvalid(){tone(200,0.1,'sawtooth',0.15);tone(180,0.1,'sawtooth',0.12,0.1);}
function sndReveal(type,col){
  if(type==='correct'){
    const n=[[523,659,784,1047],[587,740,880],[523,659,784],[659,784,1047],[523,784],[523,659]];
    (n[Math.min(col||0,5)]||n[0]).forEach((f,i)=>tone(f,0.15,'sine',0.22,i*0.07));
  } else if(type==='present'){tone(440,0.12,'sine',0.15);tone(554,0.12,'sine',0.15,0.08);}
  else{tone(280,0.12,'sine',0.12);}
}
function sndWin(){[523,587,659,784,880,1047,784,1047,1319].forEach((f,i)=>tone(f,0.18,'sine',0.28,i*0.09));}
function sndLose(){[440,370,311,277].forEach((f,i)=>tone(f,0.28,'sine',0.22,i*0.14));}

function getDayNum(){
  const launch=new Date('2026-06-01'),today=new Date();today.setHours(0,0,0,0);
  return Math.max(0,Math.floor((today-launch)/86400000))%ANSWERS.length;
}
function loadStats(){
  try{const s=JSON.parse(localStorage.getItem('sg_wordle_stats')||'{}');if(s.played!==undefined)stats=Object.assign({played:0,wins:0,streak:0,maxStreak:0,dist:{}},s);}catch(e){}
}
function saveStats(){try{localStorage.setItem('sg_wordle_stats',JSON.stringify(stats));}catch(e){}}
function updateStats(won,row){
  stats.played++;
  if(won){stats.wins++;stats.streak++;if(stats.streak>stats.maxStreak)stats.maxStreak=stats.streak;stats.dist[row]=(stats.dist[row]||0)+1;}
  else{stats.streak=0;}
  saveStats();renderStats();
}
function renderStats(){
  const wp=stats.played>0?Math.round(stats.wins/stats.played*100):0;
  document.getElementById('stat-played').textContent=stats.played;
  document.getElementById('stat-win').textContent=wp+'%';
  document.getElementById('stat-streak').textContent=stats.streak;
  document.getElementById('stat-max').textContent=stats.maxStreak;
}
function loadGameState(){
  try{const s=JSON.parse(localStorage.getItem('sg_wordle_state')||'{}');if(s.dayNum===dayNum)return s;}catch(e){}return null;
}
function saveGameState(){
  try{localStorage.setItem('sg_wordle_state',JSON.stringify({dayNum,guesses,currentRow,currentTile,gameOver}));}catch(e){}
}
function init(){
  dayNum=getDayNum();answer=ANSWERS[dayNum];
  document.getElementById('puzzle-label').textContent='#'+String(dayNum+1).padStart(3,'0');
  soundOn=localStorage.getItem('sg_sound')!=='off';
  hardMode=localStorage.getItem('sg_hard')==='on';
  updateSoundBtn();updateHardBtn();
  loadStats();renderStats();
  const saved=loadGameState();
  if(saved){guesses=saved.guesses;currentRow=saved.currentRow;currentTile=saved.currentTile;gameOver=saved.gameOver;}
  else{guesses=Array.from({length:6},()=>Array(5).fill(''));currentRow=0;currentTile=0;gameOver=false;}
  buildBoard();buildKeyboard();
  for(let r=0;r<Math.min(currentRow,6);r++)applyRowColors(r);
  if(currentRow<6&&!gameOver)renderCurrentRow();
  if(gameOver){
    const won=guesses.slice(0,currentRow).some(g=>g.join('')===answer);
    setTimeout(()=>showResults(won,currentRow),400);
  }
  startCountdown();
}
function buildBoard(){
  const board=document.getElementById('board');board.innerHTML='';
  for(let r=0;r<6;r++){
    const row=document.createElement('div');row.className='board-row';row.id='row-'+r;
    for(let c=0;c<5;c++){const tile=document.createElement('div');tile.className='tile';tile.id='t-'+r+'-'+c;row.appendChild(tile);}
    board.appendChild(row);
  }
}
const KROWS=[['Q','W','E','R','T','Y','U','I','O','P'],['A','S','D','F','G','H','J','K','L'],['ENTER','Z','X','C','V','B','N','M','DEL']];
function buildKeyboard(){
  KROWS.forEach((row,ri)=>{
    const el=document.getElementById('kb-row-'+(ri+1));el.innerHTML='';
    row.forEach(key=>{
      const btn=document.createElement('button');
      btn.className='kb-key'+(key.length>1?' wide':'');
      btn.textContent=key==='DEL'?'⌫':key;btn.id='key-'+key;
      btn.addEventListener('click',()=>{initAudio();handleKey(key==='DEL'?'BACKSPACE':key);});
      el.appendChild(btn);
    });
  });
}
function renderCurrentRow(){
  for(let c=0;c<5;c++){
    const tile=document.getElementById('t-'+currentRow+'-'+c),letter=guesses[currentRow][c];
    tile.textContent=letter;tile.className='tile'+(letter?' filled active-row':'');
  }
}
function handleKey(k){
  if(gameOver)return;k=k.toUpperCase();
  if(k==='BACKSPACE'){if(currentTile>0){currentTile--;guesses[currentRow][currentTile]='';renderCurrentRow();sndDelete();}return;}
  if(k==='ENTER'){submitGuess();return;}
  if(/^[A-Z]$/.test(k)&&currentTile<5){
    guesses[currentRow][currentTile]=k;
    const tile=document.getElementById('t-'+currentRow+'-'+currentTile);
    tile.textContent=k;tile.className='tile filled active-row';
    tile.style.animation='none';void tile.offsetHeight;tile.style.animation='tilePopIn 0.1s ease';
    currentTile++;sndKey();saveGameState();
  }
}
function submitGuess(){
  if(currentTile<5){shakeRow(currentRow);showToast('Not enough letters');sndInvalid();return;}
  const word=guesses[currentRow].join('');
  if(!VALID.has(word)&&!ANSWERS.includes(word)){shakeRow(currentRow);showToast('Not in word list');sndInvalid();return;}
  if(hardMode&&currentRow>0){const v=checkHardMode(word);if(v){shakeRow(currentRow);showToast(v);sndInvalid();return;}}
  sndSubmit();revealRow(currentRow);
}
function checkHardMode(word){
  for(let r=0;r<currentRow;r++){
    const g=guesses[r],result=scoreGuess(g.join(''));
    for(let c=0;c<5;c++){
      if(result[c]==='correct'&&word[c]!==g[c])return'Letter '+g[c]+' must be in position '+(c+1);
      if(result[c]==='present'&&!word.includes(g[c]))return'Guess must contain '+g[c];
    }
  }
  return null;
}
function scoreGuess(word){
  const result=Array(5).fill('absent'),ans=answer.split(''),w=word.split(''),used=Array(5).fill(false);
  for(let i=0;i<5;i++){if(w[i]===ans[i]){result[i]='correct';used[i]=true;w[i]=null;}}
  for(let i=0;i<5;i++){if(result[i]==='correct')continue;for(let j=0;j<5;j++){if(!used[j]&&w[i]===ans[j]){result[i]='present';used[j]=true;break;}}}
  return result;
}
const keyState={};const RANK={correct:3,present:2,absent:1};
function updateKeyboard(word,result){
  for(let i=0;i<5;i++){
    const letter=word[i],newState=result[i],cur=keyState[letter];
    if(!cur||RANK[newState]>RANK[cur]){keyState[letter]=newState;const btn=document.getElementById('key-'+letter);if(btn)btn.className='kb-key '+newState+(letter.length>1?' wide':'');}
  }
}
function revealRow(row){
  const word=guesses[row].join(''),result=scoreGuess(word);
  result.forEach((res,c)=>{
    const tile=document.getElementById('t-'+row+'-'+c);
    setTimeout(()=>{tile.className='tile reveal '+res;sndReveal(res,row);},c*300);
  });
  setTimeout(()=>{
    updateKeyboard(word,result);currentRow++;currentTile=0;
    const won=result.every(r=>r==='correct');
    if(won||currentRow>=6){
      gameOver=true;saveGameState();updateStats(won,currentRow);
      setTimeout(()=>{
        if(won){bounceRow(currentRow-1);setTimeout(sndWin,200);}else{setTimeout(sndLose,100);}
        setTimeout(()=>showResults(won,currentRow),won?700:200);
      },5*300+400);
    }else{saveGameState();setTimeout(renderCurrentRow,100);}
  },5*300+100);
}
function applyRowColors(row){
  const word=guesses[row].join('');if(!word)return;
  const result=scoreGuess(word);
  result.forEach((res,c)=>{const tile=document.getElementById('t-'+row+'-'+c);tile.textContent=word[c];tile.className='tile '+res;});
  updateKeyboard(word,result);
}
function shakeRow(row){
  for(let c=0;c<5;c++){const tile=document.getElementById('t-'+row+'-'+c);tile.style.animation='none';void tile.offsetHeight;tile.style.animation='tileShake 0.4s ease';setTimeout(()=>tile.style.animation='',400);}
}
function bounceRow(row){
  for(let c=0;c<5;c++){setTimeout(()=>{const tile=document.getElementById('t-'+row+'-'+c);tile.style.animation='none';void tile.offsetHeight;tile.style.animation='tileBounce 0.5s ease';setTimeout(()=>tile.style.animation='',500);},c*80);}
}
let toastTimer;
function showToast(msg,cls,dur){
  const el=document.getElementById('toast');el.textContent=msg;el.className='toast visible'+(cls?' '+cls:'');
  clearTimeout(toastTimer);toastTimer=setTimeout(()=>el.className='toast',dur||2000);
}
const TITLES=['','Genius!','Magnificent!','Impressive!','Splendid!','Great!','Phew!'];
const EMOJIS=['','🏆','🤩','😮','😊','😅','😮‍💨'];
function showResults(won,rows){
  document.getElementById('res-emoji').textContent=won?(EMOJIS[rows]||'🎉'):'😞';
  document.getElementById('res-title').textContent=won?(TITLES[rows]||'You got it!'):'Better luck tomorrow!';
  document.getElementById('res-word').textContent=answer;
  document.getElementById('res-sub').textContent=won?'You solved it in '+rows+' tr'+(rows===1?'y':'ies')+'!':'The word was '+answer+'. Try again tomorrow!';
  const wp=stats.played>0?Math.round(stats.wins/stats.played*100):0;
  document.getElementById('res-played').textContent=stats.played;
  document.getElementById('res-win').textContent=wp+'%';
  document.getElementById('res-streak').textContent=stats.streak;
  const maxVal=Math.max(...Object.values(stats.dist),1);
  document.getElementById('dist-chart').innerHTML=[1,2,3,4,5,6].map(n=>{
    const val=stats.dist[n]||0,pct=Math.max(8,Math.round(val/maxVal*100)),isCur=won&&currentRow===n;
    return`<div class="dist-row"><div class="dist-num">${n}</div><div class="dist-bar${isCur?' current':''}${val===0?' zero':''}" style="width:${pct}%"><span>${val}</span></div></div>`;
  }).join('');
  document.getElementById('share-grid').innerHTML=guesses.slice(0,currentRow).map(g=>{
    const res=scoreGuess(g.join(''));
    return`<div class="share-row">${res.map(r=>`<div class="share-sq sq-${r[0]}"></div>`).join('')}</div>`;
  }).join('');
  document.getElementById('results-overlay').classList.add('visible');
}
function closeResults(){document.getElementById('results-overlay').classList.remove('visible');}
function handleShare(){
  const won=guesses.slice(0,currentRow).some(g=>g.join('')===answer);
  const emap={correct:'🟩',present:'🟨',absent:'⬛'};
  const grid=guesses.slice(0,currentRow).map(g=>scoreGuess(g.join('')).map(r=>emap[r]).join('')).join('\n');
  const score=won?currentRow:'X';
  const text=`SnappGrid Wordle #${dayNum+1} ${score}/6${hardMode?'\n⚡ Hard Mode':''}\n\n${grid}\n\nsnappgrid.com/games/wordle/`;
  const btn=document.getElementById('share-btn');
  if(navigator.clipboard){navigator.clipboard.writeText(text).then(()=>{btn.textContent='✓ Copied!';btn.classList.add('copied');sndReveal('correct',0);setTimeout(()=>{btn.textContent='📋 Copy results';btn.classList.remove('copied');},2000);});}
  else{const ta=document.createElement('textarea');ta.value=text;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);btn.textContent='✓ Copied!';setTimeout(()=>btn.textContent='📋 Copy results',2000);}
}
function toggleSound(){initAudio();soundOn=!soundOn;localStorage.setItem('sg_sound',soundOn?'on':'off');updateSoundBtn();if(soundOn)sndKey();}
function updateSoundBtn(){const btn=document.getElementById('sound-btn');btn.textContent=(soundOn?'🔊':'🔇')+' Sound';btn.classList.toggle('sound-off',!soundOn);btn.classList.toggle('active',soundOn);}
function toggleHard(){if(currentRow>0&&!gameOver){showToast('Enable hard mode at the start');return;}hardMode=!hardMode;localStorage.setItem('sg_hard',hardMode?'on':'off');updateHardBtn();if(hardMode)showToast('⚡ Hard mode on!');}
function updateHardBtn(){document.getElementById('hard-btn').classList.toggle('active',hardMode);}
function startCountdown(){
  function tick(){const now=new Date(),next=new Date(now);next.setHours(24,0,0,0);const diff=next-now;const h=Math.floor(diff/3600000),m=Math.floor((diff%3600000)/60000),s=Math.floor((diff%60000)/1000);const el=document.getElementById('countdown');if(el)el.textContent=String(h).padStart(2,'0')+':'+String(m).padStart(2,'0')+':'+String(s).padStart(2,'0');}
  tick();setInterval(tick,1000);
}
document.addEventListener('keydown',e=>{if(e.ctrlKey||e.metaKey||e.altKey)return;initAudio();if(e.key==='Enter')handleKey('ENTER');else if(e.key==='Backspace')handleKey('BACKSPACE');else if(/^[a-zA-Z]$/.test(e.key))handleKey(e.key.toUpperCase());});
function toggleNav(){const nl=document.getElementById('nav-links'),hb=document.getElementById('hamburger');nl.classList.toggle('open');hb.setAttribute('aria-expanded',nl.classList.contains('open'));}
document.getElementById('yr').textContent=new Date().getFullYear();
(function(){const KEY='snappgrid_date',today=new Date().toDateString(),stored=localStorage.getItem(KEY);if(stored&&stored!==today){localStorage.setItem(KEY,today);const t=document.getElementById('refresh-toast');if(t){t.classList.add('visible');setTimeout(()=>t.classList.remove('visible'),8000);}}else{localStorage.setItem(KEY,today);}setInterval(()=>{if(localStorage.getItem(KEY)!==new Date().toDateString()){localStorage.setItem(KEY,new Date().toDateString());const t=document.getElementById('refresh-toast');if(t){t.classList.add('visible');setTimeout(()=>t.classList.remove('visible'),8000);}}},60000);})();
init();
