#!/usr/bin/env python3
"""Generate EN and DE versions of ALL BIXIE pages."""
import os, glob, re, shutil

SITE = 'https://bixie.ba'
BASE = '/root/bixie-site'

# List of all rel paths (relative to root)
ALL_PATHS = ['', 'about', 'services/crm', 'services/ai-agents', 'services/digital-transformation', 'services/rpa', 'ai-providers', 'blog', 'contact', 'privacy']

def copy_and_localize(lang):
    """Copy each BS page to lang/ dir and localize links."""
    for rel in ALL_PATHS:
        # Source
        if rel == '':
            src = f'{BASE}/index.html'
        else:
            src = f'{BASE}/{rel}/index.html'
        
        if not os.path.exists(src):
            print(f'  SKIP (no source): {rel}')
            continue
        
        # Destination
        dst_dir = f'{BASE}/{lang}/{rel}'
        os.makedirs(dst_dir, exist_ok=True)
        dst = f'{dst_dir}/index.html'
        
        # Read
        with open(src) as f:
            html = f.read()
        
        # 1. Language
        html = html.replace('<html lang="bs">', f'<html lang="{lang}">')
        
        # 2. Replace href="/ with href="/lang/
        html = re.sub(r'href="/', f'href="/{lang}/', html)
        
        # 3. Fix double prefixes that might have been created
        html = html.replace(f'/{lang}/{lang}/', f'/{lang}/')
        
        # 4. Fix canonical
        html = re.sub(
            r'href="https://bixie\.ba/(?!en/|de/)([^"]*)"',
            f'href="https://bixie.ba/{lang}/\\1"',
            html
        )
        # Fix root canonical
        html = html.replace(f'https://bixie.ba/{lang}/"', f'https://bixie.ba/{lang}"')
        html = html.replace(f'https://bixie.ba/{lang}/', f'https://bixie.ba/{lang}/')
        
        # 5. Fix OG url
        html = re.sub(
            r'"https://bixie\.ba/(?!en/|de/)([^"]*)"',
            f'"https://bixie.ba/{lang}/\\1"',
            html
        )
        html = html.replace(f'"https://bixie.ba/{lang}/"', f'"https://bixie.ba/{lang}"')
        
        # 6. Fix JSON-LD
        html = html.replace('"url": "https://bixie.ba"', f'"url": "https://bixie.ba/{lang}"')
        
        # 7. Title translation for known pages
        if lang == 'en':
            title_translations = {
                'O nama — BIXIE | CRM, AI i Digitalna Transformacija': 'About — BIXIE | CRM, AI & Digital Transformation',
                'AI Provajderi i Licence — BIXIE | ChatGPT, Gemini, Claude': 'AI Providers and Licenses — BIXIE',
                'RPA i AI Automatizacija — BIXIE': 'RPA and AI Automation — BIXIE',
                'Privacy Policy — BIXIE | Zaštita podataka': 'Privacy Policy — BIXIE',
                'Kontakt — BIXIE': 'Contact — BIXIE',
                'Blog — BIXIE': 'Blog — BIXIE',
                'CRM Rješenja — BIXIE': 'CRM Solutions — BIXIE',
                'AI Agenti — BIXIE': 'AI Agents — BIXIE',
                'Digitalna Transformacija — BIXIE': 'Digital Transformation — BIXIE',
            }
            for old, new in title_translations.items():
                html = html.replace(f'<title>{old}</title>', f'<title>{new}</title>')
                html = html.replace(f'content="{old}"', f'content="{new}"')
        elif lang == 'de':
            title_translations = {
                'O nama — BIXIE | CRM, AI i Digitalna Transformacija': 'Über uns — BIXIE | CRM, KI & Digitale Transformation',
                'AI Provajderi i Licence — BIXIE | ChatGPT, Gemini, Claude': 'KI-Anbieter und Lizenzen — BIXIE',
                'RPA i AI Automatizacija — BIXIE': 'RPA und KI-Automatisierung — BIXIE',
                'Privacy Policy — BIXIE | Zaštita podataka': 'Datenschutzerklärung — BIXIE',
                'Kontakt — BIXIE': 'Kontakt — BIXIE',
                'Blog — BIXIE': 'Blog — BIXIE',
                'CRM Rješenja — BIXIE': 'CRM Lösungen — BIXIE',
                'AI Agenti — BIXIE': 'KI-Agenten — BIXIE',
                'Digitalna Transformacija — BIXIE': 'Digitale Transformation — BIXIE',
            }
            for old, new in title_translations.items():
                html = html.replace(f'<title>{old}</title>', f'<title>{new}</title>')
                html = html.replace(f'content="{old}"', f'content="{new}"')
        
        # 8. Add hreflang
        # Get the canonical URL
        canon_match = re.search(r'href="https://bixie\.ba[^"]*"', html)
        if canon_match:
            canon = canon_match.group().replace('href="', '').replace('"', '')
        else:
            canon = f'{SITE}/{lang}/{rel}' if rel else f'{SITE}/{lang}'
        
        en_url = canon.replace(f'/{lang}/', '/en/').replace(f'/{lang}', '/en') if lang != 'en' else canon
        de_url = canon.replace(f'/{lang}/', '/de/').replace(f'/{lang}', '/de') if lang != 'de' else canon
        bs_url = canon.replace(f'/{lang}/', '/').replace(f'/{lang}', '')
        
        # Remove existing hreflang
        html = re.sub(r'<link rel="alternate".*?>\n?', '', html)
        
        hreflang = f'<link rel="alternate" hreflang="en" href="{en_url}">\n<link rel="alternate" hreflang="de" href="{de_url}">\n<link rel="alternate" hreflang="bs" href="{bs_url}">\n<link rel="alternate" hreflang="x-default" href="{bs_url}">'
        html = html.replace('</head>', f'{hreflang}</head>')
        
        # Write
        with open(dst, 'w') as f:
            f.write(html)
        print(f'  ✅ {lang}/{rel}')

# Generate
for lang in ['en', 'de']:
    print(f'\\n=== {lang.upper()} ===')
    # Clean and recreate
    lang_dir = f'{BASE}/{lang}'
    if os.path.exists(lang_dir):
        shutil.rmtree(lang_dir)
    copy_and_localize(lang)

print('\\n✅ All language pages generated!')

# Also add hreflang to all BS pages (hvala, blog posts, etc.)
print('\\n=== Adding hreflang to remaining BS pages ===')
for f in glob.glob(f'{BASE}/**/index.html', recursive=True):
    if '/.git/' in f or f'/en/' in f or f'/de/' in f:
        continue
    if 'hreflang' in open(f).read():
        continue
    with open(f) as fh:
        html = fh.read()
    
    # Get canonical
    canon_match = re.search(r'href="https://bixie\.ba[^"]*"', html)
    if not canon_match:
        continue
    canon = canon_match.group().replace('href="', '').replace('"', '')
    
    en_url = canon.replace('https://bixie.ba', 'https://bixie.ba/en')
    de_url = canon.replace('https://bixie.ba', 'https://bixie.ba/de')
    
    hreflang = f'<link rel="alternate" hreflang="en" href="{en_url}">\n<link rel="alternate" hreflang="de" href="{de_url}">\n<link rel="alternate" hreflang="bs" href="{canon}">\n<link rel="alternate" hreflang="x-default" href="{canon}">'
    html = html.replace('</head>', f'{hreflang}</head>')
    
    with open(f, 'w') as fh:
        fh.write(html)
    rel_path = f.replace(BASE, '').lstrip('/')
    print(f'  {rel_path}')
