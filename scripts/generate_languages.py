#!/usr/bin/env python3
"""Generate EN and DE translations of all BIXIE pages + hreflang tags."""
import os, glob, re

SITE = 'https://bixie.ba'

# ─── Language translations for key content ───
PAGES = {
    '/': {
        'en': {'title': 'BIXIE — CRM, AI Agents & Digital Transformation', 'badge': 'Registered Partner · Since 2011 · 25+ Certifications', 'h1': 'CRM, AI Agents and<br>Digital Transformation', 'lead': 'Full-service digital transformation advisory agency specialized in CRM, AI agents, RPA and Private Cloud. Registered HubSpot, Salesforce, Zoho, Pipedrive and Bitrix Consulting Partner.', 'btn1': 'Book a consultation', 'btn2': 'View services'},
        'de': {'title': 'BIXIE — CRM, KI-Agenten & Digitale Transformation', 'badge': 'Registered Partner · Seit 2011 · 25+ Zertifizierungen', 'h1': 'CRM, KI-Agenten und<br>Digitale Transformation', 'lead': 'Full-service Digital Transformation Agentur spezialisiert auf CRM, KI-Agenten, RPA und Private Cloud. Registrierter HubSpot, Salesforce, Zoho, Pipedrive und Bitrix Consulting Partner.', 'btn1': 'Beratung buchen', 'btn2': 'Leistungen anzeigen'}
    },
    'about': {
        'en': {'title': 'About — BIXIE | CRM, AI & Digital Transformation', 'badge': 'About', 'h1': 'Over a decade of<br>digital transformation', 'lead': 'BIXIE is a full-service digital agency specialized in CRM, AI agents, RPA automation and digital workplace. Founded in 2011.'},
        'de': {'title': 'Über uns — BIXIE | CRM, KI & Digitale Transformation', 'badge': 'Über uns', 'h1': 'Über ein Jahrzehnt<br>digitale Transformation', 'lead': 'BIXIE ist eine Full-Service-Digitalagentur spezialisiert auf CRM, KI-Agenten, RPA und digitale Arbeitsplätze. Gegründet 2011.'}
    },
    'services/crm': {
        'en': {'title': 'CRM Solutions — BIXIE | Bitrix24, Salesforce, Zoho, HubSpot', 'badge': 'CRM', 'h1': 'CRM Solutions', 'lead': 'Implementation, migration and optimization of CRM systems. Official Bitrix24 partner for Bosnia and Herzegovina.'},
        'de': {'title': 'CRM Lösungen — BIXIE | Bitrix24, Salesforce, Zoho, HubSpot', 'badge': 'CRM', 'h1': 'CRM Lösungen', 'lead': 'Implementierung, Migration und Optimierung von CRM-Systemen. Offizieller Bitrix24-Partner für Bosnien und Herzegowina.'}
    },
    'services/ai-agents': {
        'en': {'title': 'AI Agents — BIXIE', 'badge': 'AI Agents', 'h1': 'AI Agents and Automation', 'lead': 'Custom AI agents for customer support, sales and internal processes. RPA automation with AI integration.'},
        'de': {'title': 'KI-Agenten — BIXIE', 'badge': 'KI-Agenten', 'h1': 'KI-Agenten und Automatisierung', 'lead': 'Massgeschneiderte KI-Agenten für Kundensupport, Vertrieb und interne Prozesse. RPA mit KI-Integration.'}
    },
    'services/digital-transformation': {
        'en': {'title': 'Digital Transformation — BIXIE', 'badge': 'Digital Transformation', 'h1': 'Digital Transformation', 'lead': 'Business process optimization, AI integration in ERP/DMS, workflow automation and IT consulting.'},
        'de': {'title': 'Digitale Transformation — BIXIE', 'badge': 'Digitale Transformation', 'h1': 'Digitale Transformation', 'lead': 'Optimierung von Geschäftsprozessen, KI-Integration in ERP/DMS, Workflow-Automatisierung und IT-Beratung.'}
    },
    'services/rpa': {
        'en': {'title': 'RPA and AI Automation — BIXIE', 'badge': 'RPA & AI', 'h1': 'RPA and AI Automation', 'lead': 'Automation of repetitive tasks using RPA and AI technologies. Save up to 70% of time on admin processes.'},
        'de': {'title': 'RPA und KI-Automatisierung — BIXIE', 'badge': 'RPA & KI', 'h1': 'RPA und KI-Automatisierung', 'lead': 'Automatisierung von Routineaufgaben mit RPA und KI. Sparen Sie bis zu 70% Zeit bei administrativen Prozessen.'}
    },
    'ai-providers': {
        'en': {'title': 'AI Providers and Licenses — BIXIE', 'badge': 'AI Licenses', 'h1': 'AI Providers and Licenses', 'lead': 'Legal procurement of AI licenses with domestic invoices. For companies and educational institutions in BiH.'},
        'de': {'title': 'KI-Anbieter und Lizenzen — BIXIE', 'badge': 'KI-Lizenzen', 'h1': 'KI-Anbieter und Lizenzen', 'lead': 'Legal-erworbene KI-Lizenzen mit lokaler Rechnung. Für Unternehmen und Bildungseinrichtungen.'}
    },
    'blog': {
        'en': {'title': 'Blog — BIXIE | CRM, AI & Digital Transformation Insights', 'badge': 'Blog', 'h1': 'Blog', 'lead': 'Practical guides on CRM implementation, AI agents and digital transformation for businesses in Bosnia and Herzegovina.'},
        'de': {'title': 'Blog — BIXIE | CRM, KI & Digitale Transformation', 'badge': 'Blog', 'h1': 'Blog', 'lead': 'Praktische Leitfäden zu CRM-Implementierung, KI-Agenten und digitaler Transformation.'}
    },
    'contact': {
        'en': {'title': 'Contact — BIXIE', 'badge': 'Contact', 'h1': 'Get in Touch', 'lead': 'Ready to start your digital transformation? Book a free consultation. We respond within 24 hours.'},
        'de': {'title': 'Kontakt — BIXIE', 'badge': 'Kontakt', 'h1': 'Kontaktieren Sie uns', 'lead': 'Bereit für Ihre digitale Transformation? Buchen Sie eine kostenlose Beratung. Wir antworten innerhalb von 24 Stunden.'}
    },
    'privacy': {
        'en': {'title': 'Privacy Policy — BIXIE', 'badge': 'Legal', 'h1': 'Privacy Policy', 'lead': 'How we manage your data and protect your privacy.'},
        'de': {'title': 'Datenschutzerklärung — BIXIE', 'badge': 'Rechtliches', 'h1': 'Datenschutzerklärung', 'lead': 'Wie wir Ihre Daten verwalten und Ihre Privatsphäre schützen.'}
    },
}

NAV_PREFIX = {
    'en': {'nav': '<a href="/en">', 'cta': 'Contact', 'label_crm': 'CRM', 'label_ai': 'AI', 'label_dt': 'Digital Transformation', 'label_about': 'About', 'label_blog': 'Blog', 'label_ai_licences': 'AI Licenses', 'label_rpa': 'RPA'},
    'de': {'nav': '<a href="/de">', 'cta': 'Kontakt', 'label_crm': 'CRM', 'label_ai': 'KI', 'label_dt': 'Digitale Transformation', 'label_about': 'Über uns', 'label_blog': 'Blog', 'label_ai_licences': 'KI-Lizenzen', 'label_rpa': 'RPA'}
}

# Read a source page to get the template structure
SRC = {}
for rel, data in PAGES.items():
    src_path = f'/root/bixie-site/{rel}/index.html' if rel != '/' else '/root/bixie-site/index.html'
    if os.path.exists(src_path):
        with open(src_path) as f:
            SRC[rel] = f.read()

def get_hreflang_tags(canonical_url):
    """Generate hreflang tags for all 3 languages."""
    en_url = canonical_url.replace(SITE, f'{SITE}/en')
    de_url = canonical_url.replace(SITE, f'{SITE}/de')
    bs_url = canonical_url
    return f'<link rel="alternate" hreflang="en" href="{en_url}">\n<link rel="alternate" hreflang="de" href="{de_url}">\n<link rel="alternate" hreflang="bs" href="{bs_url}">\n<link rel="alternate" hreflang="x-default" href="{bs_url}">'

def create_lang_page(rel, lang, data):
    """Create a translated page."""
    src = SRC.get(rel, '')
    if not src:
        return
    
    dir_path = f'/root/bixie-site/{lang}/{rel}'
    os.makedirs(dir_path, exist_ok=True)
    
    # Basic replacements
    html = src
    
    # Language
    html = html.replace('<html lang="bs">', f'<html lang="{lang}">')
    
    # Title
    html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', html)
    
    # OG Title
    html = html.replace(f'content="{data["title"]}"', f'content="{data["title"]}"')
    
    # URL prefix for nav
    prefix_data = NAV_PREFIX[lang]
    
    # Replace nav links - add language prefix
    html = html.replace('href="/', f'href="/{lang}/')
    html = html.replace(f'/{lang}/{lang}/', f'/{lang}/')  # Fix double prefix
    
    # Fix root URLs
    html = html.replace(f'href="/{lang}/"', f'href="/{lang}/"')
    # Fix canonical
    canonical_old = re.search(r'href="https://bixie\.ba[^"]*"', html)
    if canonical_old:
        old_canon = canonical_old.group()
        new_canon = old_canon.replace('https://bixie.ba', f'https://bixie.ba/{lang}')
        html = html.replace(old_canon, new_canon)
    
    # Fix OG url
    html = html.replace('"https://bixie.ba/', f'"https://bixie.ba/{lang}/')
    html = html.replace(f'/{lang}/{lang}/', f'/{lang}/')
    
    # Badge, h1, lead
    html = html.replace(f'>{data["badge"]}<', f'>{data["badge"]}<')
    
    # Replace h1
    h1_match = re.search(r'<h1[^>]*>.*?</h1>', html, re.DOTALL)
    if h1_match:
        old_h1 = h1_match.group()
        new_h1 = re.sub(r'>.*?<', f'>{data["h1"]}<', old_h1)
        html = html.replace(old_h1, new_h1)
    
    # Replace lead paragraph (first p after h1)
    p_after_h1 = re.search(r'<p[^>]*style="font-size:18px[^>]*>.*?</p>', html)
    if p_after_h1:
        html = html.replace(p_after_h1.group(), f'<p style="font-size:18px;line-height:1.6;color:#8a8f98;max-width:600px;margin-bottom:48px">{data["lead"]}</p>', 1)
    
    # Add hreflang tags
    canonical_match = re.search(r'href="https://bixie\.ba[^"]*"', html)
    canonical_url = canonical_match.group().replace('href="', '').replace('"', '') if canonical_match else f'{SITE}/{rel}'
    
    hreflang_tags = get_hreflang_tags(canonical_url)
    html = html.replace('</head>', f'{hreflang_tags}</head>')
    
    filepath = os.path.join(dir_path, 'index.html')
    with open(filepath, 'w') as f:
        f.write(html)
    print(f'  {lang}/{rel}/')

# ─── Generate all language pages ───
print('=== Generating EN pages ===')
for rel in PAGES:
    create_lang_page(rel, 'en', PAGES[rel]['en'])

print('\\n=== Generating DE pages ===')
for rel in PAGES:
    create_lang_page(rel, 'de', PAGES[rel]['de'])

# ─── Add hreflang to original BS pages ───
print('\\n=== Adding hreflang to BS pages ===')
for rel in PAGES:
    src_path = f'/root/bixie-site/{rel}/index.html' if rel != '/' else '/root/bixie-site/index.html'
    if not os.path.exists(src_path):
        continue
    with open(src_path) as f:
        html = f.read()
    if 'hreflang' in html:
        continue
    canonical_match = re.search(r'href="https://bixie\.ba[^"]*"', html)
    canonical_url = canonical_match.group().replace('href="', '').replace('"', '') if canonical_match else f'{SITE}/{rel}'
    hreflang_tags = get_hreflang_tags(canonical_url)
    html = html.replace('</head>', f'{hreflang_tags}</head>')
    with open(src_path, 'w') as f:
        f.write(html)
    print(f'  {rel}/')

# ─── Update sitemap ───
print('\\n=== Updating sitemap ===')
sitemap_path = '/root/bixie-site/sitemap.xml'
with open(sitemap_path) as f:
    sitemap = f.read()

# Add xhtml namespace for hreflang
sitemap = sitemap.replace(
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
)

# For each URL, add alternate links
for url_match in re.finditer(r'<loc>(https://bixie\.ba[^<]*)</loc>', sitemap):
    url = url_match.group(1)
    if '/en/' in url or '/de/' in url:
        continue
    rel_path = url.replace(SITE, '').strip('/')
    en_url = f'{SITE}/en/{rel_path}' if rel_path else f'{SITE}/en'
    de_url = f'{SITE}/de/{rel_path}' if rel_path else f'{SITE}/de'
    
    alternates = f'\n    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>'
    alternates += f'\n    <xhtml:link rel="alternate" hreflang="de" href="{de_url}"/>'
    alternates += f'\n    <xhtml:link rel="alternate" hreflang="bs" href="{url}"/>'
    alternates += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url}"/>'
    
    sitemap = sitemap.replace(f'<loc>{url}</loc>', f'<loc>{url}</loc>{alternates}')

with open(sitemap_path, 'w') as f:
    f.write(sitemap)
print('  sitemap.xml updated')

# ─── Add EN/DE sitemap entries ───
sitemap = sitemap.replace('</urlset>', '')
for lang in ['en', 'de']:
    for rel in PAGES:
        url = f'{SITE}/{lang}/{rel}' if rel else f'{SITE}/{lang}'
        sitemap += f'\n  <url><loc>{url}</loc><priority>0.8</priority><changefreq>weekly</changefreq></url>'
sitemap += '\n</urlset>'

with open(sitemap_path, 'w') as f:
    f.write(sitemap)

print('\\n✅ All language pages generated!')
