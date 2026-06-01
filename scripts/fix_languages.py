#!/usr/bin/env python3
"""Fix language pages: root, nav links, hreflang."""
import re, os

SITE = 'https://bixie.ba'

def fix_page(filepath, lang, is_root=False):
    with open(filepath) as f:
        html = f.read()
    
    # Fix language
    html = html.replace('<html lang="bs">', f'<html lang="{lang}">')
    
    # Fix nav links - replace href="/ with href="/lang/
    # But be careful not to double-prefix
    html = re.sub(r'href="/', f'href="/{lang}/', html)
    # Fix double-prefixed
    html = html.replace(f'/{lang}/{lang}/', f'/{lang}/')
    # Fix hreflang links that got prefixed
    html = html.replace(f'hreflang="{lang}"', 'HREFLANG_KEEP')
    html = re.sub(r'hreflang="[^"]*"', lambda m: m.group(0).replace(f'/{lang}/', '/'), html)
    html = html.replace('HREFLANG_KEEP', f'hreflang="{lang}"')
    
    # Fix canonical
    canonical_match = re.search(r'href="https://bixie\.ba[^"]*"', html)
    if canonical_match:
        old = canonical_match.group()
        new = old.replace('https://bixie.ba', f'https://bixie.ba/{lang}')
        html = html.replace(old, new)
    
    # Fix OG url
    html = html.replace('"https://bixie.ba/', f'"https://bixie.ba/{lang}/')
    html = html.replace(f'/{lang}/{lang}/', f'/{lang}/')
    
    # Fix JSON-LD url
    html = html.replace('"url": "https://bixie.ba"', f'"url": "https://bixie.ba/{lang}"')
    
    # Add hreflang
    canonical_match = re.search(r'href="https://bixie\.ba[^"]*"', html)
    canon_url = canonical_match.group().replace('href="', '').replace('"', '') if canonical_match else f'{SITE}/{lang}'
    
    en_url = canon_url.replace(f'/{lang}/', '/en/').replace(f'/{lang}', '/en')
    de_url = canon_url.replace(f'/{lang}/', '/de/').replace(f'/{lang}', '/de')
    bs_url = canon_url.replace(f'/{lang}/', '/').replace(f'/{lang}', '')
    
    hreflang = f'<link rel="alternate" hreflang="en" href="{en_url}">\n<link rel="alternate" hreflang="de" href="{de_url}">\n<link rel="alternate" hreflang="bs" href="{bs_url}">\n<link rel="alternate" hreflang="x-default" href="{bs_url}">'
    
    # Remove existing hreflang and add new
    html = re.sub(r'<link rel="alternate".*?>\n?', '', html)
    html = html.replace('</head>', f'{hreflang}</head>')
    
    # Fix title for language
    if lang == 'en':
        html = re.sub(r'<title>BIXIE(.*?)</title>', '<title>BIXIE\\1</title>', html)
    elif lang == 'de':
        html = re.sub(r'<title>BIXIE(.*?)</title>', '<title>BIXIE\\1</title>', html)
    
    with open(filepath, 'w') as f:
        f.write(html)

import glob

for lang in ['en', 'de']:
    for f in glob.glob(f'/root/bixie-site/{lang}/**/index.html', recursive=True):
        fix_page(f, lang)
        short = f.replace('/root/bixie-site/', '')
        print(f'  Fixed: {short}')

print('\\n✅ Language pages fixed!')
