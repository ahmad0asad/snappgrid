/**
 * SnappGrid Centralized Catalog Configuration
 * Single Source of Truth for all 9 Original Manuscripts by Ahmad Asad
 */

const BOOKS_CATALOG = [
  {
    id: 'the-10-minute-detective',
    title: 'The 10-Minute Detective: True Crime Logic Puzzles for Adults',
    subtitle: '15 Forensic Case Files with Evidence, Clues & Deduction Grids',
    category: 'Logic & Deduction',
    genreColor: '#C0392B',
    coverBg: 'linear-gradient(145deg, #1f0f0f, #3b1818)',
    spineColor: '#8E1B1B',
    price: '$7.99',
    pages: '96 Pages',
    puzzles: '15 Full Case Files',
    difficulty: 'Progressive (Tiers 1–3)',
    blurb: 'Step into the shoes of a lead investigator. Each case presents evidence logs, suspect profiles, forensic clues, and a multi-grid alibi tracking matrix. Eliminate the impossible until only the truth remains.',
    features: [
      '15 full case files with evidence cards',
      '4x4 alibi tracking matrices',
      'Progressive difficulty across 3 tiers',
      'Complete verified solution keys'
    ],
    pdfUrl: '/assets/books/the-10-minute-detective.pdf',
    checkoutUrl: '#',
    companionUrl: '/blog/how-to-solve-logic-grid-puzzles/',
    sampleType: 'logic-matrix',
    sampleTitle: "Case 1: The Phantom's Fingerprint",
    sampleSubtitle: "Voss Manuscript Theft · Library Crime Scene",
    sampleData: {
      intro: "The glass display case holding the 16th-century Voss Manuscript is shattered. A partial fingerprint blazes under UV light on the inner rim. The artifact is gone. Four guests remain in the manor. One of them knows where it is.",
      clues: [
        "The fingerprint was lifted from inside the Library's display case — the crime scene.",
        "Suspect 1 left the Study before the suspect who used the Knife had even arrived there.",
        "The crime was committed before 10 PM — the last guest departed at exactly that hour.",
        "Suspect 3 was seen in the Garden earlier in the evening than Suspect 4.",
        "The Library suspect did not use Rope — no ligature evidence was found in that room."
      ],
      suspects: ['Suspect 1', 'Suspect 2', 'Suspect 3', 'Suspect 4'],
      weapons: ['Knife', 'Poison', 'Rope', 'Pistol'],
      locations: ['Library', 'Study', 'Garden', 'Kitchen'],
      times: ['7 PM', '8 PM', '9 PM', '10 PM'],
      solution: {
        culprit: 'Suspect 3',
        weapon: 'Poison',
        location: 'Library',
        time: '9 PM'
      }
    }
  },
  {
    id: 'critical-thinking-puzzle-book',
    title: 'Critical Thinking Puzzle Book',
    subtitle: '113 Pages of Mini Sudoku, Nonograms, Binary & Futoshiki',
    category: 'Logic & Math Grids',
    genreColor: '#16A085',
    coverBg: 'linear-gradient(145deg, #0d2621, #134239)',
    spineColor: '#116B59',
    price: '$8.99',
    pages: '113 Pages',
    puzzles: '100+ Grid Challenges',
    difficulty: 'Progressive',
    blurb: 'A pure workout for analytical clarity. Five distinct visual logic systems: 6x6 Mini Sudoku, 10x10 Nonograms, 10x10 Binary Puzzles, 6x6 Futoshiki inequalities, and mathematical Number Sequences.',
    features: [
      '6x6 Mini Sudoku & 10x10 Nonograms',
      '10x10 Binary Puzzles (0s & 1s)',
      '6x6 Futoshiki inequality grids',
      'Step-by-step solutions for every puzzle'
    ],
    pdfUrl: '/assets/books/critical-thinking-puzzle-book.pdf',
    checkoutUrl: '#',
    companionUrl: '/blog/advanced-logic-grid-deduction-techniques/',
    sampleType: 'math-grid',
    sampleTitle: 'Futoshiki FT-01 & Binary BP-01',
    sampleSubtitle: 'Playable 6x6 Inequality & 10x10 Binary Grids',
    sampleData: {
      futoshiki: {
        id: 'FT-01',
        size: 6,
        rules: 'Fill 1–6 with no repeats in any row or column. Respect every inequality sign.',
        initial: [
          [6, 1, 0, 4, 0, 0],
          [0, 0, 6, 5, 0, 0],
          [0, 0, 4, 0, 0, 1],
          [1, 3, 0, 2, 0, 4],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 3, 1, 0, 6]
        ],
        hSigns: {
          '0,0': '>', '0,2': '<',
          '1,0': '<', '1,2': '>',
          '2,4': '>',
          '3,1': '<',
          '4,0': '>', '4,2': '<', '4,4': '<'
        },
        vSigns: {
          '0,0': 'v', '0,3': '^',
          '1,0': '^', '1,1': '^', '1,2': 'v',
          '2,0': 'v', '2,2': '^', '2,3': 'v', '2,4': '^',
          '4,3': 'v', '4,4': '^'
        }
      },
      binary: {
        id: 'BP-01',
        size: 10,
        rules: 'No more than two identical numbers adjacent. Each row & column has equal 0s and 1s. No two rows or columns are identical.',
        initial: [
          [1, 0, 0, null, null, null, null, 0, null, 0],
          [null, 1, 1, null, null, 0, null, 1, 0, 1],
          [null, 1, 1, null, 0, null, null, 1, 1, 1],
          [null, 1, null, null, 0, null, 1, null, null, null],
          [1, null, null, null, null, 0, null, null, null, null],
          [null, null, null, null, null, 1, 1, null, 1, 0],
          [null, null, null, 1, null, 1, null, null, null, 0],
          [null, 0, null, 1, 0, 0, null, null, null, null],
          [1, 1, null, 0, 0, null, 0, 1, null, 0],
          [null, 0, null, 0, 1, null, null, null, 1, 1]
        ]
      }
    }
  },
  {
    id: 'crossword-puzzles-for-adults',
    title: 'Crossword Puzzles for Adults: 30 Medium-to-Hard Puzzles to Sharpen the Mind',
    subtitle: 'Large-Print Clues · Intersecting Open Grids · Brain Health Focus',
    category: 'Crosswords & Wordplay',
    genreColor: '#2980B9',
    coverBg: 'linear-gradient(145deg, #0e2436, #153c5b)',
    spineColor: '#1F618D',
    price: '$7.99',
    pages: '80 Pages',
    puzzles: '30 Thematic Grids',
    difficulty: 'Medium-to-Hard',
    blurb: 'Designed for serious solvers who appreciate thoughtful themes and clean construction. Thirty open 7x7 intersecting grids celebrating philosophy, cognitive science, and human discovery.',
    features: [
      '30 large-print thematic open grids',
      'Dual 7-letter vertical spines',
      'Neuroplasticity and cognitive health focus',
      'Complete verified solution keys'
    ],
    pdfUrl: '/assets/books/crossword-puzzles-for-adults.pdf',
    checkoutUrl: '#',
    companionUrl: '/blog/crossword-puzzle-solving-strategies-guide/',
    sampleType: 'crossword-grid',
    sampleTitle: 'Puzzle 01: Logic & Reason',
    sampleSubtitle: 'A workout for the analytical mind',
    sampleData: {
      across: [
        { num: 1, row: 0, answer: 'LOGIC', clue: 'The science of valid reasoning and argumentation' },
        { num: 4, row: 1, answer: 'BURNS', clue: 'What resilience does to self-doubt — consumes it' },
        { num: 5, row: 2, answer: 'STOCK', clue: 'To accumulate; also a measure of trust and value' },
        { num: 6, row: 3, answer: 'OPTIC', clue: 'Relating to the eye; the nerve connecting vision to brain' },
        { num: 7, row: 4, answer: 'CAUSE', clue: 'The root of an effect; a principle that drives action' },
        { num: 8, row: 5, answer: 'SCOOP', clue: 'To gather in one swift motion; an exclusive discovery' },
        { num: 9, row: 6, answer: 'LEARN', clue: "To absorb knowledge and transform one's understanding" }
      ],
      down: [
        { num: 2, col: 1, answer: 'OUTPACE', clue: 'To move faster and leave others behind' },
        { num: 3, col: 3, answer: 'INCISOR', clue: 'A sharp front tooth designed for cutting through things' }
      ]
    }
  },
  {
    id: 'brain-boost-challenge',
    title: 'Brain Boost Challenge: 30-Day Brain Training',
    subtitle: 'Daily Cognitive Workout for Speed, Focus & Mental Agility',
    category: 'Cognitive Training',
    genreColor: '#8E44AD',
    coverBg: 'linear-gradient(145deg, #221230, #381a52)',
    spineColor: '#6C3483',
    price: '$7.99',
    pages: '100+ Pages',
    puzzles: '30 Daily Regimens',
    difficulty: 'Progressive Challenge',
    blurb: 'A 30-day structured regimen engaging pattern matrices, multi-constraint logic deduction, ciphers, number models, and visual search arrays. Built to stimulate neuroplasticity.',
    features: [
      'Pattern matrices & numerical progression',
      'Multi-constraint logic deduction tables',
      'Ciphers, scrambles & visual search arrays',
      'Daily reflection & mental clarity tracking'
    ],
    pdfUrl: '/assets/books/brain-boost-challenge.pdf',
    checkoutUrl: '#',
    companionUrl: '/blog/brain-training-neuroplasticity-puzzle-science/',
    sampleType: 'brain-matrix',
    sampleTitle: 'Matrix Puzzle 1 & Hobbies Logic Puzzle',
    sampleSubtitle: 'Structural Reasoning & Constraint Deduction',
    sampleData: {
      matrix: {
        title: 'Matrix Puzzle 1: Row/Column Progression',
        grid: [
          [2, 6, 10, 14],
          [5, 9, 13, 17],
          [8, 12, 16, 20],
          [11, 15, 19, '?']
        ],
        explanation: 'Each row progresses by +4; each column increments downwards by +3. Therefore, 19 + 4 = 23 (and 20 + 3 = 23).',
        answer: '23'
      },
      logic: {
        title: 'Logic Puzzle 1: Hobbies Deduction',
        category: 'Hobbies',
        clues: [
          'Anna is not Reading',
          'Ben prefers Cycling',
          'Clara avoids Cooking',
          'David cannot choose Painting or Gaming'
        ],
        question: 'Who has Cycling?',
        answer: 'Ben',
        explanation: "By direct positive confirmation in Clue 2: 'Ben prefers Cycling'."
      }
    }
  },
  {
    id: 'forbidden-history',
    title: "Forbidden History: Shocking Trivia They Didn't Teach You in School",
    subtitle: '630 Verified Facts Across 14 Uncensored Chapters',
    category: 'History & Trivia',
    genreColor: '#D35400',
    coverBg: 'linear-gradient(145deg, #2e1709, #4a240c)',
    spineColor: '#A04000',
    price: '$6.99',
    pages: '170+ Pages',
    puzzles: '630 Questions',
    difficulty: 'Moderate to Shocking',
    blurb: 'History stripped of textbook sanitization. 14 chapters covering brutal antiquities, bizarre executions, secret pacts, strange deaths, and forgotten disasters across a 5-round scoring framework.',
    features: [
      '630 verified historical questions',
      '14 deeply researched chapters',
      '5-round scoring framework per chapter',
      'Answer keys & Knowledge Rank scorecard'
    ],
    pdfUrl: '/assets/books/forbidden-history.pdf',
    checkoutUrl: '#',
    companionUrl: '/blog/world-history-trivia-memorization-techniques/',
    sampleType: 'trivia-round',
    sampleTitle: 'Chapter 1: The Dark Side of the Ancient World',
    sampleSubtitle: 'Round 1 Fact Bombs & Scored Review',
    sampleData: {
      factBombs: [
        'The Roman general Crassus crucified 6,000 captured rebels along the Appian Way after defeating Spartacus in 71 BC, lining 200 kilometres of road.',
        'The Aztecs sacrificed an estimated 20,000 people in a single four-day ceremony in 1487 to dedicate the Great Pyramid of Tenochtitlán.',
        'The ancient Persian execution method "scaphism" involved trapping victims between two boats, feeding them milk and honey, and letting insects devour them over 17 days.'
      ],
      questions: [
        {
          q: 'How long did the Appian Way crucifixions orchestrated by Crassus extend?',
          options: ['50 km', '100 km', '200 km', '500 km'],
          correct: 2,
          explanation: 'Crassus lined 6,000 crosses along 200 km of the Appian Way from Rome to Capua.'
        },
        {
          q: 'How many captives were sacrificed in the 1487 Aztec pyramid dedication?',
          options: ['2,000', '5,000', '20,000', '50,000'],
          correct: 2,
          explanation: 'Historical accounts record approximately 20,000 victims over four continuous days.'
        },
        {
          q: 'What was the intended duration of execution by Persian scaphism?',
          options: ['A few hours', '2 to 3 days', 'Around 17 days', 'Several months'],
          correct: 2,
          explanation: 'Scaphism was engineered as a prolonged death, famously taking around 17 days.'
        },
        {
          q: 'True or False: Carthaginian infant sacrifice is confirmed by charred remains found in Tophet burial urns.',
          options: ['True', 'False'],
          correct: 0,
          explanation: 'True. Archaeological excavation at the Tophet of Carthage confirmed thousands of infant urn burials.'
        },
        {
          q: 'At what age did Spartan boys begin the brutal state-mandated Agōgē military training?',
          options: ['Age 5', 'Age 7', 'Age 10', 'Age 12'],
          correct: 1,
          explanation: 'Spartan boys were taken from their mothers at age seven to enter the Agōgē.'
        }
      ]
    }
  },
  {
    id: 'food-culture-how-the-world-eats',
    title: 'Food, Culture & How the World Eats',
    subtitle: '720 Questions Across 16 Culinary Regions & Traditions',
    category: 'Culture & Culinary Trivia',
    genreColor: '#27AE60',
    coverBg: 'linear-gradient(145deg, #0e2918, #184729)',
    spineColor: '#1E8449',
    price: '$6.99',
    pages: '190+ Pages',
    puzzles: '720 Questions',
    difficulty: 'All Levels',
    blurb: 'A culinary journey exploring gastronomic science, ancient fermentation, origin disputes, and cultural etiquette. 16 regional chapters celebrating food traditions from Italy to the Levant.',
    features: [
      '720 trivia & cultural questions',
      '16 regional chapters with Fact Bombs',
      'Culinary science, terroir & food history',
      'Engaging solo or dinner-party game rounds'
    ],
    pdfUrl: '/assets/books/food-culture-how-the-world-eats.pdf',
    checkoutUrl: '#',
    companionUrl: '/blog/science-trivia-facts-and-mnemonics/',
    sampleType: 'trivia-round',
    sampleTitle: 'Chapter 1: The Soul of Italian Food',
    sampleSubtitle: 'Terroir, Regional Rules & Culinary Heritage',
    sampleData: {
      factBombs: [
        'There are over 350 distinct pasta shapes officially recognised in Italy, each engineered for specific sauce viscosities.',
        'True Parmigiano-Reggiano must be produced within a strictly regulated zone of northern Italy and aged a minimum of 12 months with every wheel certified.',
        'Espresso is not a bean or roast type — it is a pressure-brewing method derived from the Italian verb "esprimere" (to press out).'
      ],
      questions: [
        {
          q: 'How many pasta shapes are officially recognised in Italian culinary tradition?',
          options: ['Over 100', 'Over 200', 'Over 350', 'Over 500'],
          correct: 2,
          explanation: 'Over 350 distinct pasta shapes exist, designed with specific ridges, thickness, and hollows for sauces.'
        },
        {
          q: 'What is the literal Italian meaning of the word "espresso"?',
          options: ['Fast coffee', 'To press out', 'Dark roast', 'Morning cup'],
          correct: 1,
          explanation: 'From the Italian verb "esprimere", meaning to squeeze or press out under pressure.'
        },
        {
          q: 'True or False: Italians consume approximately 23 kg of pasta per person each year.',
          options: ['True', 'False'],
          correct: 0,
          explanation: 'True. Italy leads the world in per capita pasta consumption at ~23 kg/year.'
        },
        {
          q: 'What does the dessert name "Tiramisu" translate to in Italian?',
          options: ['Sweet cloud', 'Pick me up / Lift me up', 'Midnight dream', 'Golden coffee'],
          correct: 1,
          explanation: 'Tiramisu means "pick me up" or "lift me up", referencing its shot of espresso and sugar.'
        },
        {
          q: 'Where did the habanero chilli actually originate according to botanical genetics?',
          options: ['Oaxaca, Mexico', 'Yucatán Peninsula', 'Amazon basin', 'Guatemala'],
          correct: 2,
          explanation: 'Genetic analysis traces the habanero chilli back to origin in the Amazon basin.'
        }
      ]
    }
  },
  {
    id: 'unbelievable-but-true-trivia',
    title: 'Unbelievable But True Trivia',
    subtitle: '630 Shocking Facts from Science, Nature & Human History',
    category: 'General Science & Curiosities',
    genreColor: '#C8922A',
    coverBg: 'linear-gradient(145deg, #2b1f09, #47320c)',
    spineColor: '#9A6B1A',
    price: '$6.99',
    pages: '180+ Pages',
    puzzles: '630 Questions',
    difficulty: 'Mixed Curiosities',
    blurb: 'Facts stranger than fiction. 14 chapters covering bizarre biology, physics anomalies, linguistics, unusual laws, and unbelievable historical coincidences that challenge human intuition.',
    features: [
      '630 verified counterintuitive facts',
      '14 themed science & curiosity chapters',
      'Fact Reveal, True/False & Quick Fire',
      'Ideal for curious solo minds or pub quiz hosts'
    ],
    pdfUrl: '/assets/books/unbelievable-but-true-trivia.pdf',
    checkoutUrl: '#',
    companionUrl: '/blog/science-of-trivia-memory-recall/',
    sampleType: 'trivia-round',
    sampleTitle: 'Nature & Animal Anomalies',
    sampleSubtitle: 'Counter-Intuitive Truths of Biology',
    sampleData: {
      factBombs: [
        'Octopuses possess three hearts: two pump blood to the gills while one pumps to the body. When they swim, the body heart halts.',
        'Mantis shrimps can strike with the acceleration of a .22 calibre bullet and perceive 16 distinct colour receptor channels (humans have 3).',
        'Honey never spoils. Archaeologists have excavated 3,000-year-old honey from ancient Egyptian tombs that remained perfectly preserved and edible.'
      ],
      questions: [
        {
          q: 'How many hearts does an octopus have?',
          options: ['One', 'Two', 'Three', 'Four'],
          correct: 2,
          explanation: 'Octopuses have three hearts: two branchial hearts for gills and one systemic heart for the body.'
        },
        {
          q: 'How many photoreceptor colour channels do mantis shrimps possess?',
          options: ['3 channels', '7 channels', '12 channels', '16 channels'],
          correct: 3,
          explanation: 'Mantis shrimps have 16 distinct colour-receptive cones, far outstripping human trichromatic vision.'
        },
        {
          q: 'Why does honey excavated from 3,000-year-old Egyptian tombs remain edible?',
          options: ['High artificial salt content', 'Low moisture, high acidity and natural hydrogen peroxide', 'Wax sealing preserves vacuum', 'High alcohol fermentation'],
          correct: 1,
          explanation: 'Honey has very low moisture (<18%), acidic pH (~3.9), and bee enzymes generate trace hydrogen peroxide, preventing bacterial growth.'
        },
        {
          q: 'What happens to an octopus’s main body heart while swimming?',
          options: ['It beats three times faster', 'It temporarily stops beating', 'It reverses blood flow', 'It pumps oxygen directly to brain'],
          correct: 1,
          explanation: 'The systemic heart stops while swimming, which is why octopuses prefer crawling over swimming.'
        },
        {
          q: 'True or False: The Amazon River basin discharges roughly 20% of all river water entering the world’s oceans.',
          options: ['True', 'False'],
          correct: 0,
          explanation: 'True. The Amazon discharges roughly 209,000 m³/s, accounting for approximately one-fifth of global ocean runoff.'
        }
      ]
    }
  },
  {
    id: 'ultimate-general-knowledge-trivia-challenge',
    title: 'The Ultimate General Knowledge Trivia Challenge',
    subtitle: '420 Questions Across 12 Academic & Cultural Subjects',
    category: 'Pub Quiz & General Knowledge',
    genreColor: '#2A6EA6',
    coverBg: 'linear-gradient(145deg, #0e2033, #163654)',
    spineColor: '#1B4F72',
    price: '$6.99',
    pages: '140+ Pages',
    puzzles: '420 Questions',
    difficulty: 'Tiered (Easy to Expert)',
    blurb: '420 questions systematically structured across 12 disciplines: World Geography, Ancient History, Science, Literature, Cinema, and Music. Scored rounds with progressive knowledge tiers.',
    features: [
      '420 questions across 12 subjects',
      '35 points per chapter scoring system',
      'Multiple choice, true/false & quick fire',
      'Full answer key and knowledge tier ranking'
    ],
    pdfUrl: '/assets/books/ultimate-general-knowledge-trivia-challenge.pdf',
    checkoutUrl: '#',
    companionUrl: '/blog/geography-trivia-mnemonics-guide/',
    sampleType: 'trivia-round',
    sampleTitle: 'Chapter 1: World Geography',
    sampleSubtitle: 'Global Landmasses, Oceans & Geological Extremes',
    sampleData: {
      factBombs: [
        "The Pacific Ocean covers more area than all of Earth's landmasses combined.",
        "Lake Baikal in Russia holds approximately one-fifth (20%) of the world's unfrozen surface fresh water.",
        "The Atacama Desert in northern Chile is the driest non-polar desert on Earth, with weather stations that recorded zero rainfall for decades."
      ],
      questions: [
        {
          q: "What fraction of the world's unfrozen surface fresh water is held in Lake Baikal?",
          options: ['One tenth', 'One fifth (20%)', 'One third', 'One half'],
          correct: 1,
          explanation: 'Lake Baikal holds roughly 20% of the world’s unfrozen surface fresh water, more than all North American Great Lakes combined.'
        },
        {
          q: 'What is recognized as the driest non-polar desert on Earth?',
          options: ['Sahara', 'Gobi', 'Arabian', 'Atacama'],
          correct: 3,
          explanation: 'The Atacama Desert in Chile is blocked by the Andes on one side and the Chilean Coastal Range on the other.'
        },
        {
          q: 'Which ocean covers more total surface area than all landmasses on Earth combined?',
          options: ['Atlantic', 'Indian', 'Pacific', 'Southern'],
          correct: 2,
          explanation: 'The Pacific Ocean spans ~165 million km², exceeding the entire dry land surface area of Earth (~149 million km²).'
        },
        {
          q: 'Which nation possesses the longest total coastline in the world?',
          options: ['Russia', 'Australia', 'Norway', 'Canada'],
          correct: 3,
          explanation: 'Canada holds the longest coastline globally, measuring over 202,000 kilometres.'
        },
        {
          q: 'True or False: The Amazon River flows into the Atlantic Ocean.',
          options: ['True', 'False'],
          correct: 0,
          explanation: 'True. The Amazon flows east across South America into the Atlantic Ocean.'
        }
      ]
    }
  },
  {
    id: 'knowledge-quest-250-puzzles',
    title: 'The Knowledge Quest: 250 Mixed Puzzles Across 10 Subjects',
    subtitle: 'Word Searches, Caesar Cryptograms, Scrambles & Trivia',
    category: 'Mixed Brain Games',
    genreColor: '#5A3A8A',
    coverBg: 'linear-gradient(145deg, #1c1033, #2e1852)',
    spineColor: '#4A235A',
    price: '$8.99',
    pages: '160+ Pages',
    puzzles: '250 Mixed Challenges',
    difficulty: 'Mixed Variety',
    blurb: '250 diverse brain games spanning 10 core knowledge domains: World Geography, World History, Science & Nature, Inventions, Arts & Literature, and Pop Culture. A dynamic multi-format puzzle book.',
    features: [
      '250 mixed puzzles across 10 subjects',
      'Caesar cipher cryptograms (+7 shift)',
      '12x12 thematic word searches & anagrams',
      'Word scrambles & true/false fact checks'
    ],
    pdfUrl: '/assets/books/knowledge-quest-250-puzzles.pdf',
    checkoutUrl: '#',
    companionUrl: '/blog/pop-culture-cinema-trivia-mastery/',
    sampleType: 'mixed-quest',
    sampleTitle: 'Chapter 1: World Geography Cryptogram & Scrambles',
    sampleSubtitle: 'Caesar Cipher (+7 Shift) & Geographic Anagrams',
    sampleData: {
      cryptogram: {
        cipherText: 'A O L   D V Y S K   P Z   H   I V V R   H U K   A O V Z L   D O V   K V   U V A   A Y H C L S   Y L H K   V U S F   V U L   W H N L',
        attribution: '— Saint Augustine',
        shift: 7,
        plainText: 'THE WORLD IS A BOOK AND THOSE WHO DO NOT TRAVEL READ ONLY ONE PAGE',
        hint: 'Shift each letter backward by 7 in the alphabet (e.g., H → A, O → H, L → E).'
      },
      scrambles: [
        { scrambled: 'A – I – C – F – C – A – P', answer: 'PACIFIC', clue: 'Earth’s largest ocean basin' },
        { scrambled: 'D – A – A – A – N – C', answer: 'CANADA', clue: 'Second largest country by land area' },
        { scrambled: 'A – A – Z – O – M – N', answer: 'AMAZON', clue: 'Great river flowing into the Atlantic' },
        { scrambled: 'A – A – H – R – S – A', answer: 'SAHARA', clue: 'Vast hot desert in Northern Africa' },
        { scrambled: 'K – Y – N – A – E', answer: 'KENYA', clue: 'East African nation on the equator' },
        { scrambled: 'S – P – A – L', answer: 'ALPS', clue: 'Major European mountain range' }
      ]
    }
  }
];

// Helper lookup map
const BOOKS_BY_ID = BOOKS_CATALOG.reduce((acc, book) => {
  acc[book.id] = book;
  return acc;
}, {});

// Export for module or global use
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { BOOKS_CATALOG, BOOKS_BY_ID };
}
