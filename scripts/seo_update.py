#!/usr/bin/env python3
"""Add canonical URLs and JSON-LD structured data to all BIXIE pages."""
import os, glob, re

SITE = 'https://bixie.ba'

STRUCTURED_DATA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "BIXIE",
  "url": "https://bixie.ba",
  "logo": "https://bixie.ba/og-image.png",
  "description": "CRM, AI Agenti i Digitalna Transformacija za firme u Bosni i Hercegovini.",
  "address": { "@type": "PostalAddress", "streetAddress": "Maglajska 1", "addressLocality": "Sarajevo", "addressCountry": "BA" },
  "contactPoint": { "@type": "ContactPoint", "telephone": "+387-33-922-622", "email": "hello@bixie.ba", "contactType": "sales" },
  "sameAs": ["https://www.linkedin.com/company/bixie"]
}
</script>'''

def get_canonical(filepath):
    """Get canonical URL for a file."""
    rel = filepath.replace('/root/bixie-site/', '').replace('/index.html', '')
    if rel == '' or rel == 'index.html':
        return f'{SITE}/'
    return f'{SITE}/{rel}'

def get_title(filepath):
    """Extract existing title."""
    with open(filepath) as f:
        content = f.read()
    m = re.search(r'<title>(.*?)</title>', content)
    return m.group(1) if m else 'BIXIE'

def update_file(filepath):
    with open(filepath) as f:
        html = f.read()
    
    canonical = get_canonical(filepath)
    title = get_title(filepath)
    
    # 1. Add canonical if missing
    if 'rel="canonical"' not in html:
        html = html.replace('</head>', f'  <link rel="canonical" href="{canonical}">\n</head>')
        print(f'  + canonical: {canonical}')
    
    # 2. Add structured data if missing (before </head>)
    if 'application/ld+json' not in html and 'schema.org' not in html:
        html = html.replace('</head>', f'{STRUCTURED_DATA}\n</head>')
        print(f'  + JSON-LD structured data')
    
    # 3. Fix html lang if needed
    html = re.sub(r'<html lang="[^"]*">', '<html lang="bs">', html)
    
    with open(filepath, 'w') as f:
        f.write(html)

# Process all HTML files
files = glob.glob('/root/bixie-site/**/index.html', recursive=True)
files += glob.glob('/root/bixie-site/*.html', recursive=False)
files = [f for f in files if '.git/' not in f]

print(f'Ažuriram {len(files)} fajlova...')
for f in sorted(files):
    print(f'  {f.replace("/root/bixie-site/", "")}')
    update_file(f)

print('\\nGotovo!')
