#!/usr/bin/env python3
"""Update all bixie.ba pages to new BIXIE teal theme + shared CSS."""
import os, re

SITE = '/root/bixie-site'
OLD_INDIGO = '#5e6ad2'
OLD_PURPLE = '#7170ff'
OLD_HOVER = '#828fff'
NEW_TEAL = '#00736a'
NEW_HOVER = '#008a7f'

# Collect all HTML files
html_files = []
for root, dirs, files in os.walk(SITE):
    if '.git' in root: continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} HTML files")

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original = content
    changed = False
    
    # 1. Replace old colors
    if OLD_INDIGO in content:
        content = content.replace(OLD_INDIGO, NEW_TEAL)
        changed = True
    if OLD_PURPLE in content:
        content = content.replace(OLD_PURPLE, NEW_TEAL)
        changed = True
    if OLD_HOVER in content:
        content = content.replace(OLD_HOVER, NEW_HOVER)
        changed = True
    
    # 2. Add style.css link if not present
    if '<link rel="stylesheet" href="/style.css">' not in content:
        content = content.replace(
            '<link rel="icon"',
            '<link rel="stylesheet" href="/style.css">\n<link rel="icon"'
        )
        changed = True
    
    # 3. Update nav logo from SVG+B text to image
    old_logo = re.search(
        r'<a href="/" style="display:flex;align-items:center;gap:8px;text-decoration:none;font-size:18px;font-weight:510[^"]*">\s*<svg[^>]*>.*?</svg>\s*BIXIE\s*</a>',
        content, re.DOTALL
    )
    if old_logo:
        new_logo = '<a href="/" class="logo"><img src="/images/logo/bixie-logo.png" alt="BIXIE" style="height:36px"></a>'
        content = content.replace(old_logo.group(), new_logo)
        changed = True
    
    # 4. Update footer logo similarly
    old_footer_logo = re.search(
        r'<a href="/" style="display:flex;align-items:center;gap:8px;text-decoration:none;font-size:16px;font-weight:510;color:#f7f8f8;margin-bottom:12px"><svg[^>]*>.*?</svg>BIXIE</a>',
        content, re.DOTALL
    )
    if old_footer_logo:
        new_footer_logo = '<a href="/" style="display:flex;align-items:center;gap:10px;text-decoration:none;font-size:16px;font-weight:600;color:#f3f4f6;margin-bottom:14px"><img src="/images/logo/bixie-logo.png" alt="BIXIE" style="height:28px"></a>'
        content = content.replace(old_footer_logo.group(), new_footer_logo)
        changed = True
    
    # 5. Remove inline style block that duplicates CSS (replace with link)
    old_style_tag = re.search(r'<link href="https://fonts\.googleapis\.com[^>]*>[\s\S]*?<style>[\s\S]*?</style>', content)
    # Only do this if there's a large inline style block (not the small ones in blog posts)
    style_match = re.search(r'<style>', content)
    if style_match:
        # Check if there's a large style block (> 500 chars) - these are the old full CSS
        large_style = re.search(r'<style>\s*\*\{margin:0;padding:0;box-sizing:border-box\}[\s\S]{300,}?</style>', content)
        if large_style:
            # Replace with just the font link + style.css
            font_link = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
            css_link = '<link rel="stylesheet" href="/style.css">'
            replacement = f'{font_link}\n{css_link}'
            content = content.replace(large_style.group(), replacement)
            changed = True
        else:
            # Small inline style - just ensure style.css is present
            pass
    
    # 6. Remove duplicate style.css links
    content = content.replace(
        '<link rel="stylesheet" href="/style.css">\n<link rel="stylesheet" href="/style.css">',
        '<link rel="stylesheet" href="/style.css">'
    )
    
    # 7. Google Fonts link cleanup - if style.css included, ensure Inter is loaded
    if '<link href="https://fonts.googleapis.com' not in content and '<link rel="stylesheet" href="/style.css">' in content:
        font_link = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
        content = content.replace(
            '<link rel="stylesheet" href="/style.css">',
            f'{font_link}\n<link rel="stylesheet" href="/style.css">'
        )
        changed = True
    
    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ Updated: {os.path.relpath(fpath, SITE)}")
    # else: print(f"  - Skipped: {os.path.relpath(fpath, SITE)}")

print("\n✅ Done! All pages updated to BIXIE teal theme.")
