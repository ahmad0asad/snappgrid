import glob, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = sorted(glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True))

print("=== BRANDING AUDIT REPORT ===")

required_head_items = [
    ('/favicon.ico', 'favicon.ico link'),
    ('/favicon-32x32.png', 'favicon-32x32.png link'),
    ('/favicon-16x16.png', 'favicon-16x16.png link'),
    ('/apple-touch-icon.png', 'apple-touch-icon link'),
    ('/site.webmanifest', 'manifest link'),
    ('#0f172a', 'theme-color'),
    ('https://snappgrid.com/og-image.jpg', 'og:image / twitter:image'),
    ('1200', 'og:image:width'),
    ('630', 'og:image:height'),
    ('summary_large_image', 'twitter:card')
]

for f in html_files:
    rel = os.path.relpath(f, base_dir)
    if 'google' in rel:
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()

    # Check head
    head_m = re.search(r'<head[^>]*>(.*?)</head>', c, re.DOTALL | re.IGNORECASE)
    if not head_m:
        print(f"[FAIL] {rel}: No <head> tag found!")
        continue

    head_text = head_m.group(1)
    missing = []
    for item, desc in required_head_items:
        if item not in head_text:
            missing.append(desc)

    # Check nav logo in body
    body_idx = c.find('<body')
    first_h1 = c.find('<h1', body_idx)
    first_main = c.find('<main', body_idx)
    cand = [p for p in [first_h1, first_main] if p != -1]
    split_pos = min(cand) if cand else len(c)
    nav_area = c[body_idx:split_pos] if body_idx != -1 else ""

    has_brand_link = bool(re.search(r'<a\b[^>]*href=["\']/["\'][^>]*>.*?Snapp.*?</a>', nav_area, re.DOTALL | re.IGNORECASE))
    has_nav_logo = bool(re.search(r'<a\b[^>]*href=["\']/["\'][^>]*>.*?favicon-32x32\.png.*?</a>', nav_area, re.DOTALL | re.IGNORECASE))

    # Print status
    brand_status = "NAV LOGO PRESENT" if has_nav_logo else ("NO BRAND LINK" if not has_brand_link else "MISSING NAV LOGO")
    print(f"[{'PASS' if not missing else 'FAIL'}] {rel:55s} | Head: {'OK' if not missing else 'ERR'} | Nav: {brand_status}")
    if missing:
        print(f"       -> Missing head items: {', '.join(missing)}")
