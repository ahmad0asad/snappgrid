// scripts/refresh-sitemap-dates.js
//
// Updates <lastmod> to today's date for sitemap entries whose <changefreq>
// is in AUTO_UPDATE_FREQS. Pages outside that list (e.g. monthly: homepage,
// blog, about, contact, privacy) are left untouched -- their lastmod should
// only change when you actually edit that page's content.
//
// Run manually:  node scripts/refresh-sitemap-dates.js
// Run via CI:    see .github/workflows/daily-sitemap-refresh.yml

const fs = require('fs');
const path = require('path');

// Adjust this if your sitemap.xml lives somewhere other than the repo root
// (e.g. './public/sitemap.xml' or './dist/sitemap.xml')
const SITEMAP_PATH = path.join(__dirname, '..', 'sitemap.xml');

// Which changefreq values get auto-touched.
// Add 'weekly' here if you want the archive pages bumped daily too
// (they do gain a new puzzle entry each day, even though changefreq says weekly).
const AUTO_UPDATE_FREQS = ['daily'];

function todayISO() {
  return new Date().toISOString().split('T')[0];
}

function refreshSitemap() {
  if (!fs.existsSync(SITEMAP_PATH)) {
    console.error(`Sitemap not found at ${SITEMAP_PATH}`);
    process.exit(1);
  }

  let xml = fs.readFileSync(SITEMAP_PATH, 'utf8');
  const today = todayISO();
  let updatedCount = 0;

  xml = xml.replace(/<url>([\s\S]*?)<\/url>/g, (block) => {
    const freqMatch = block.match(/<changefreq>(.*?)<\/changefreq>/);
    const freq = freqMatch ? freqMatch[1] : null;

    if (freq && AUTO_UPDATE_FREQS.includes(freq)) {
      updatedCount++;
      return block.replace(/<lastmod>.*?<\/lastmod>/, `<lastmod>${today}</lastmod>`);
    }
    return block;
  });

  fs.writeFileSync(SITEMAP_PATH, xml, 'utf8');
  console.log(`Sitemap refreshed: ${updatedCount} URL(s) updated to ${today}`);
}

refreshSitemap();
