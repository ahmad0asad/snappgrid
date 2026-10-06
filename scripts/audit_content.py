import glob
import re

banned_ai = ['delve', 'tapestry', "in today's fast-paced world", 'testament to', 'furthermore', 'moreover', 'beacon']
banned_kdp = ['kdp', 'kindle', 'asin', 'amazon']

html_files = glob.glob('blog/**/*.html', recursive=True) + glob.glob('books/**/*.html', recursive=True) + ['index.html']

ai_found = 0
kdp_found = 0

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    for word in banned_ai:
        pattern = r'\b' + re.escape(word) + r'\b'
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            print(f"[AI_WORD] {f}: found '{matches[0]}'")
            ai_found += 1
            
    for word in banned_kdp:
        pattern = r'\b' + re.escape(word) + r'\b'
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            # Check context to allow geographical 'Amazon river', 'Amazon basin'
            if word == 'amazon':
                # check if it refers to Amazon store or Kindle
                if re.search(r'amazon\s+(com|review|store|buy|kindle|author)', content, re.IGNORECASE):
                    print(f"[KDP_AMZ STORE] {f}: found Amazon store reference")
                    kdp_found += 1
            else:
                print(f"[KDP_AMZ] {f}: found '{matches[0]}'")
                kdp_found += 1

print(f"\nAudit complete: {ai_found} AI words found, {kdp_found} KDP/Amazon store words found.")
