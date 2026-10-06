#!/usr/bin/env python3
"""
patch_website.py

Executes tasks 3 and 4:
1. Patches <head> of all HTML files:
   - Favicon links (32x32, 16x16, ico), apple-touch-icon, site.webmanifest, theme-color
   - Open Graph / Twitter image metadata pointing to https://snappgrid.com/og-image.jpg (1200x630)
2. Updates navigation headers across all pages:
   - Inserts <img src="/favicon-32x32.png" width="32" height="32" alt="SnappGrid Logo" class="nav-logo">
     inside the brand header link next to the SnappGrid title.
3. Updates CSS (both external and inline <style>) to ensure perfect vertical alignment, spacing, and responsive rendering.
"""

import glob
import os
import re
import sys

FAVICON_BLOCK = """  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#0f172a">"""

OG_TWITTER_BLOCK = """  <meta property="og:image" content="https://snappgrid.com/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://snappgrid.com/og-image.jpg">"""

NAV_LOGO_IMG = '<img src="/favicon-32x32.png" width="32" height="32" alt="SnappGrid Logo" class="nav-logo">'

BRAND_CSS_INLINE = """
/* SnappGrid Brand Nav Logo Alignment */
.nav-logo, .nav-brand, .logo { display: inline-flex; align-items: center; gap: 10px; }
.nav-logo img, .nav-brand img, .logo img, img.nav-logo { display: inline-block; vertical-align: middle; border-radius: 4px; flex-shrink: 0; }
"""

def patch_head(head_content):
    # 1. Strip existing favicon, touch icon, manifest, theme-color tags
    cleaned = re.sub(r'[ \t]*<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*>\r?\n?', '', head_content, flags=re.IGNORECASE)
    cleaned = re.sub(r'[ \t]*<link[^>]*rel=["\']apple-touch-icon(?:-precomposed)?["\'][^>]*>\r?\n?', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'[ \t]*<link[^>]*rel=["\']manifest["\'][^>]*>\r?\n?', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'[ \t]*<meta[^>]*name=["\']theme-color["\'][^>]*>\r?\n?', '', cleaned, flags=re.IGNORECASE)

    # 2. Strip existing og:image, og:image:width, og:image:height, twitter:image, twitter:card tags
    cleaned = re.sub(r'[ \t]*<meta[^>]*property=["\']og:image(?::(?:width|height))?["\'][^>]*>\r?\n?', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'[ \t]*<meta[^>]*(?:name|property)=["\']twitter:image["\'][^>]*>\r?\n?', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'[ \t]*<meta[^>]*name=["\']twitter:card["\'][^>]*>\r?\n?', '', cleaned, flags=re.IGNORECASE)

    # 3. Insert Favicon block after canonical or title
    m_fav = re.search(r'(<link[^>]*rel=["\']canonical["\'][^>]*>|<title>.*?</title>)', cleaned, re.IGNORECASE | re.DOTALL)
    if m_fav:
        pos = m_fav.end()
        cleaned = cleaned[:pos] + "\n" + FAVICON_BLOCK + cleaned[pos:]
    else:
        cleaned = FAVICON_BLOCK + "\n" + cleaned

    # 4. Insert OG & Twitter block after og:url, og:type, or canonical
    m_og = re.search(r'(<meta[^>]*property=["\']og:url["\'][^>]*>|<meta[^>]*property=["\']og:type["\'][^>]*>|<meta[^>]*property=["\']og:description["\'][^>]*>)', cleaned, re.IGNORECASE)
    if m_og:
        pos = m_og.end()
        cleaned = cleaned[:pos] + "\n" + OG_TWITTER_BLOCK + cleaned[pos:]
    else:
        idx = cleaned.find(FAVICON_BLOCK)
        if idx != -1:
            pos = idx + len(FAVICON_BLOCK)
            cleaned = cleaned[:pos] + "\n" + OG_TWITTER_BLOCK + cleaned[pos:]
        else:
            cleaned = OG_TWITTER_BLOCK + "\n" + cleaned

    return cleaned


def patch_nav_header(content):
    first_h1 = content.find('<h1')
    first_main = content.find('<main')
    first_article = content.find('<article')
    candidates = [pos for pos in [first_h1, first_main, first_article] if pos != -1]
    split_pos = min(candidates) if candidates else len(content)
    header_part = content[:split_pos]
    body_part = content[split_pos:]

    if NAV_LOGO_IMG in header_part:
        return content

    def replace_brand_link(match):
        open_tag = match.group(1)
        inner_content = match.group(2)
        close_tag = match.group(3)

        if NAV_LOGO_IMG in inner_content:
            return match.group(0)

        inner_stripped = inner_content.strip()
        if inner_stripped.startswith('←'):
            title_text = inner_stripped.lstrip('←').strip()
            new_inner = f"← {NAV_LOGO_IMG} {title_text}"
        else:
            new_inner = f"{NAV_LOGO_IMG} {inner_stripped}"

        return f"{open_tag}{new_inner}{close_tag}"

    brand_link_pattern = re.compile(
        r'(<a\b[^>]*href=["\']/["\'][^>]*>)\s*('
        r'←?\s*(?:Snapp(?:<span[^>]*>)?Grid(?:</span>)?|SnappGrid)'
        r')\s*(</a>)',
        re.IGNORECASE
    )

    new_header_part = brand_link_pattern.sub(replace_brand_link, header_part, count=1)
    return new_header_part + body_part


def patch_inline_style(content):
    if 'img.nav-logo' in content or '.nav-logo img' in content:
        return content
    
    # Check if there is a <style> tag
    style_end = content.find('</style>')
    if style_end != -1:
        content = content[:style_end] + BRAND_CSS_INLINE + content[style_end:]
    return content


def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Patch <head>
    head_match = re.search(r'(<head[^>]*>)(.*?)(</head>)', content, re.IGNORECASE | re.DOTALL)
    if head_match:
        open_head, head_body, close_head = head_match.groups()
        new_head_body = patch_head(head_body)
        content = content[:head_match.start()] + open_head + new_head_body + close_head + content[head_match.end():]

    # 2. Patch navigation header
    content = patch_nav_header(content)

    # 3. Patch inline <style> if needed
    content = patch_inline_style(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def update_css_files(base_dir):
    css_path = os.path.join(base_dir, 'css', 'style.css')
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        if '.nav-logo img' not in c:
            c += "\n" + BRAND_CSS_INLINE
            with open(css_path, 'w', encoding='utf-8') as f:
                f.write(c)
            print("Updated css/style.css with brand logo alignment rules")

    root_css_path = os.path.join(base_dir, 'style.css')
    if os.path.exists(root_css_path):
        with open(root_css_path, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        if '.nav-logo img' not in c:
            c += "\n" + BRAND_CSS_INLINE
            with open(root_css_path, 'w', encoding='utf-8') as f:
                f.write(c)
            print("Updated style.css with brand logo alignment rules")


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_files = sorted(glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True))

    update_css_files(base_dir)

    count = 0
    for f in html_files:
        rel = os.path.relpath(f, base_dir)
        if 'google' in rel:
            continue
        patch_file(f)
        count += 1
        print(f"Patched: {rel}")

    print(f"\nSuccessfully patched {count} HTML files.")

if __name__ == '__main__':
    main()
