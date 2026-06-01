#!/usr/bin/env python3
"""Generate all missing BIXIE pages directly."""
import os

# Read the CRM page as base for nav + footer
with open('/root/bixie-site/services/crm/index.html') as f:
    base = f.read()

# Extract nav and footer
nav_start = base.find('<nav')
nav_end = base.find('</nav>') + len('</nav>')
nav_block = base[nav_start:nav_end]

footer_start = base.find('<footer')
footer_block = base[footer_start:]

# Extract head up to </head>
head_end = base.find('</head>')
head_block = base[:head_end]

# Also get the style block
style_start = base.find('<style>')
style_end = base.find('</style>') + len('</style>')
style_block = base[style_start:style_end]

# Enhanced nav with new links
new_nav = nav_block.replace(
    '<a href="/services/digital-transformation">Digitalna Transformacija</a>\n<a href="/blog">Blog</a>',
    '<div class="dropdown"><a href="/services/digital-transformation">Digitalna Transformacija</a><div class="dropdown-menu"><a href="/services/digital-transformation">Pregled</a><a href="/services/rpa">RPA i Automatizacija</a></div></div>\n<a href="/about">O nama</a>\n<a href="/ai-providers">AI Licence</a>\n<a href="/blog">Blog</a>'
)
# Update mobile menu
new_nav = new_nav.replace(
    '<a href="/services/digital-transformation" style="margin-top:8px">Digitalna Transformacija</a><a href="/blog">Blog</a>',
    '<a href="/services/digital-transformation">Digitalna Transformacija</a><a href="/services/rpa">RPA i Automatizacija</a>\n<a href="/about">O nama</a>\n<a href="/ai-providers">AI Licence</a><a href="/blog">Blog</a>'
)

# Enhanced footer
new_footer = footer_block.replace(
    '<a href="/services/digital-transformation">Digitalna Transformacija</a>',
    '<a href="/services/digital-transformation">Digitalna Transformacija</a><br><a href="/services/rpa">RPA i Automatizacija</a><br><a href="/ai-providers">AI Provajderi i Licence</a>'
)
new_footer = new_footer.replace(
    '<a href="/contact">Kontakt</a>',
    '<a href="/about">O nama</a><br><a href="/blog">Blog</a><br><a href="/contact">Kontakt</a><br><a href="/privacy">Privacy Policy</a>'
)

# ─── Update all existing pages ───
def update_existing(filepath):
    with open(filepath) as f:
        content = f.read()
    old_nav = content[content.find('<nav'):content.find('</nav>')+len('</nav>')]
    old_footer = content[content.find('<footer'):]
    content = content.replace(old_nav, new_nav)
    content = content.replace(old_footer, new_footer)
    with open(filepath, 'w') as f:
        f.write(content)

import glob
for f in glob.glob('/root/bixie-site/**/index.html', recursive=True):
    if '.git/' not in f:
        update_existing(f)
        print(f'  Update: {f.replace("/root/bixie-site/", "")}')

print('\\n--- Existing pages updated ---\\n')

# ─── Create new pages ───
def make_page(dir_name, title, og_title, og_desc, meta_desc, canonical_url, badge, h1, lead, body_html):
    dir_path = f'/root/bixie-site/{dir_name}'
    os.makedirs(dir_path, exist_ok=True)
    
    # Use head from CRM, modified
    head = base[:base.find('<title>')]
    head += f'<title>{title}</title>\n'
    head += f'<meta property="og:title" content="{og_title}">\n'
    head += f'<meta property="og:description" content="{og_desc}">\n'
    head += f'<meta property="og:url" content="https://bixie.ba/{canonical_url}">\n'
    head += base[base.find('<meta property="og:type"'):base.find('<meta name="description"')]
    head += f'<meta name="description" content="{meta_desc}">\n'
    head += style_block + '\n'
    head += f'<link rel="canonical" href="https://bixie.ba/{canonical_url}">\n'
    head += base[base.find('<script type="application/ld+json"'):base.find('</head>')]
    
    html = head + '</head>\n<body>\n'
    html += new_nav + '\n'
    
    # Hero section
    html += f'<section style="padding:80px 24px">\n'
    html += f'<div style="max-width:1200px;margin:0 auto">\n'
    html += f'<span class="badge badge-indigo">{badge}</span>\n'
    html += f'<h1 style="font-size:48px;font-weight:510;line-height:1;letter-spacing:-1.056px;color:#f7f8f8;margin-bottom:16px">{h1}</h1>\n'
    html += f'<p style="font-size:18px;line-height:1.6;color:#8a8f98;max-width:600px;margin-bottom:48px">{lead}</p>\n'
    html += body_html
    html += '</div>\n</section>\n'
    html += new_footer
    
    filepath = os.path.join(dir_path, 'index.html')
    with open(filepath, 'w') as f:
        f.write(html)
    wc = len(html.split())
    print(f'✅ Created: {dir_name}/ ({wc} words)')

# 1. O NAMA
make_page('about',
    'O nama — BIXIE | CRM, AI i Digitalna Transformacija',
    'O nama — BIXIE | Više od decenije digitalne transformacije',
    'BIXIE je agencija specijalizovana za CRM, AI agente, RPA automatizaciju i digitalnu transformaciju. Registered partner Bitrix24, Zoho, Salesforce.',
    'BIXIE je digitalna transformacija agencija sa 15+ godina iskustva. CRM, AI, RPA i cloud rješenja za firme u BiH i svijetu.',
    'about', 'O nama',
    'Vi\u0161e od decenije<br>digitalne transformacije',
    'BIXIE je full-service digitalna agencija specijalizovana za CRM, AI agente, RPA automatizaciju i digitalno radno mjesto. Osnovani 2011. godine.',
    '''
<div class="grid-3" style="margin-bottom:48px">
<div class="card"><h3>15+ Godina Iskustva</h3><p>Od 2011. uspješno implementiramo digitalna rješenja za firme u BiH, Švicarskoj, Njemačkoj i regiji.</p></div>
<div class="card"><h3>25+ Certifikacija</h3><p>Registered partner za Bitrix24, Zoho, Salesforce, Pipedrive i HubSpot. Licencirani za Microsoft i Google Cloud.</p></div>
<div class="card"><h3>100+ Realizovanih Projekata</h3><p>CRM implementacije, AI integracije, RPA automatizacije i cloud migracije za različite industrije.</p></div>
</div>
<h2 style="font-size:24px;font-weight:510;color:#f7f8f8;letter-spacing:-0.288px;margin-bottom:24px">Šta radimo</h2>
<div class="grid-2" style="margin-bottom:48px">
<div class="card" style="border-left:3px solid #5e6ad2"><h3>CRM Implementacija</h3><p>Bitrix24, Zoho, Salesforce, HubSpot, Pipedrive. Migracija i integracija sa postojećim sistemima.</p></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>AI Agenti i Automatizacija</h3><p>Custom AI agenti, RPA, nabavka AI licenci (ChatGPT, Gemini, Claude). Kompletna AI podrška.</p></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>Digitalno Radno Mjesto</h3><p>Digital Office sa kolaboracijom, task menadžmentom i dokumentima na jednom mjestu.</p></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>Private & Hybrid Cloud</h3><p>Cloud infrastruktura sa sigurnosnim slojevima. Hibridni model za maksimalnu zaštitu.</p></div>
</div>
<div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:32px;text-align:center">
<h2 style="font-size:24px;font-weight:510;color:#f7f8f8;margin-bottom:8px">Zašto BIXIE?</h2>
<p style="font-size:16px;color:#8a8f98;max-width:600px;margin:0 auto 24px">Ne prodajemo softver — rješavamo poslovne probleme. Svaki projekat počinjemo analizom procesa.</p>
<div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center">
<span class="badge" style="padding:8px 20px;font-size:14px;border-color:rgba(94,106,210,0.3);color:#7170ff;background:rgba(94,106,210,0.08)">Lokalna podrška</span>
<span class="badge" style="padding:8px 20px;font-size:14px;border-color:rgba(255,255,255,0.1)">BHS jezik</span>
<span class="badge" style="padding:8px 20px;font-size:14px;border-color:rgba(255,255,255,0.1)">24h SLA</span>
<span class="badge" style="padding:8px 20px;font-size:14px;border-color:rgba(255,255,255,0.1)">GDPR</span>
</div>
</div>
''')

# 2. RPA
make_page('services/rpa',
    'RPA i AI Automatizacija — BIXIE',
    'RPA i AI Automatizacija — BIXIE | Automatizacija procesa',
    'RPA automatizacija poslovnih procesa sa AI. Automatizacija unosa podataka, obrade dokumenata i izvještaja.',
    'RPA i AI automatizacija za BiH. Automatiziramo ponavljajuće zadatke, unos podataka i obradu dokumenata.',
    'services/rpa', 'RPA i AI',
    'RPA i AI Automatizacija<br>Poslovnih Procesa',
    'Automatizacija ponavljajućih zadataka kombinacijom RPA i AI tehnologija. Uštede do 70% vremena na administraciji.',
    '''
<div class="grid-3" style="margin-bottom:48px">
<div class="card" style="border-left:3px solid #5e6ad2"><h3>Unos Podataka</h3><p>Automatsko preuzimanje iz emaila, PDF-ova i Excel tabela u CRM/ERP.</p></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>Obrada Dokumenata</h3><p>AI ekstrakcija podataka iz faktura i ugovora. Automatska kategorizacija.</p></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>Izvještaji</h3><p>Automatsko generisanje izvještaja sa slanjem na email i dashboard.</p></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>Email Automatizacija</h3><p>Sortiranje, odgovaranje i AI klasifikacija email poruka.</p></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>CRM Automatizacija</h3><p>Automatski leadovi, kontakti i aktivnosti u Bitrix24, Zoho, Salesforce.</p></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>Workflow</h3><p>Povezivanje sistema. Approval workflow i notifikacije bez kodiranja.</p></div>
</div>
<h2 style="font-size:24px;font-weight:510;color:#f7f8f8;letter-spacing:-0.288px;margin-bottom:24px">Proces implementacije</h2>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:48px">
<div class="card" style="text-align:center"><div style="font-size:32px;font-weight:600;color:#5e6ad2">01</div><h3>Analiza</h3><p>Mapiranje procesa i identifikacija zadataka za automatizaciju.</p></div>
<div class="card" style="text-align:center"><div style="font-size:32px;font-weight:600;color:#5e6ad2">02</div><h3>PoC</h3><p>Prototip za 1-2 sedmice za jedan specifičan proces.</p></div>
<div class="card" style="text-align:center"><div style="font-size:32px;font-weight:600;color:#5e6ad2">03</div><h3>Implementacija</h3><p>RPA botovi i AI agenti u produkcijsko okruženje.</p></div>
<div class="card" style="text-align:center"><div style="font-size:32px;font-weight:600;color:#5e6ad2">04</div><h3>Monitoring</h3><p>Nadzor i kontinuirano poboljšanje automatizacije.</p></div>
</div>
<div style="text-align:center;margin-top:48px;padding:32px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.08);border-radius:8px">
<p style="font-size:16px;color:#8a8f98;margin-bottom:16px">Želite besplatni audit vaših procesa?</p>
<a href="/contact" class="btn-primary">Zakažite audit</a>
</div>
''')

# 3. AI PROVIDERS
make_page('ai-providers',
    'AI Provajderi i Licence — BIXIE | ChatGPT, Gemini, Claude',
    'AI Provajderi i Licence — BIXIE | Nabavka AI licenci u BiH',
    'Nabavka AI licenci za firme i edukaciju. ChatGPT, Gemini, Claude, DeepSeek sa domaćom fakturom i PDV-om.',
    'AI licence u BiH — ChatGPT, Gemini, Claude, DeepSeek, Mistral. Legalna nabavka, domaća faktura sa PDV-om.',
    'ai-providers', 'AI Licence',
    'AI Provajderi i Licence',
    'Legalna nabavka AI licenci uz domaću žiralnu fakturu. Za firme i obrazovne ustanove u BiH.',
    '''
<h2 style="font-size:24px;font-weight:510;color:#f7f8f8;letter-spacing:-0.288px;margin-bottom:24px">Zvanične AI Licence</h2>
<div class="grid-3" style="margin-bottom:48px">
<div class="card" style="border-left:3px solid #5e6ad2"><h3>ChatGPT Team / Edu</h3><p>OpenAI sa Enterprise sigurnošću. Podaci se ne koriste za trening.</p><div style="margin-top:12px"><span class="badge">Edu: 28 KM/mj</span><span class="badge">Business: 70 KM/mj</span></div></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>Google Gemini</h3><p>Google AI u Workspace-u. Business i Education planovi.</p><div style="margin-top:12px"><span class="badge">Edu: 18 KM/mj</span><span class="badge">Business: 60 KM/mj</span></div></div>
<div class="card" style="border-left:3px solid #5e6ad2"><h3>Claude (Anthropic)</h3><p>AI sa fokusom na sigurnost. Team i Enterprise planovi.</p><div style="margin-top:12px"><span class="badge">Edu: 48 KM/mj</span><span class="badge">Business: 80 KM/mj</span></div></div>
</div>
<h2 style="font-size:24px;font-weight:510;color:#f7f8f8;letter-spacing:-0.288px;margin-bottom:24px">Managed AI (Bloom Wrapper)</h2>
<div class="grid-3" style="margin-bottom:48px">
<div class="card"><h3>DeepSeek R1/V3</h3><p>Managed pristup DeepSeek modelima.</p><div style="margin-top:12px"><span class="badge">Edu: 20/mj</span><span class="badge">Business: 45/mj</span></div></div>
<div class="card"><h3>Mistral Large 2 EU</h3><p>Evropski AI na EU serverima. GDPR.</p><div style="margin-top:12px"><span class="badge">Edu: 35/mj</span><span class="badge">Business: 65/mj</span></div></div>
<div class="card"><h3>Kimi / MiniMax</h3><p>Managed Kimi i MiniMax modeli.</p><div style="margin-top:12px"><span class="badge">Edu: 28/mj</span><span class="badge">Business: 55/mj</span></div></div>
</div>
<div style="text-align:center;padding:24px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.08);border-radius:8px">
<p style="font-size:14px;color:#62666d;margin-bottom:16px">Cijene u KM + PDV (17%). Min. 12 mjeseci. Plaćanje žiralno.</p>
<a href="/contact" class="btn-primary">Zatražite ponudu</a>
</div>
''')

# 4. PRIVACY
make_page('privacy',
    'Privacy Policy — BIXIE | Zaštita podataka',
    'Privacy Policy — BIXIE',
    'Privacy Policy i uslovi korištenja BIXIE usluga.',
    'Privacy Policy, uslovi korištenja i GDPR izjava za BIXIE agenciju.',
    'privacy', 'Legal',
    'Privacy Policy',
    'Kako upravljamo vašim podacima i štitimo privatnost.',
    '''
<div style="color:#8a8f98;font-size:15px;line-height:1.8;max-width:800px">
<h2 style="font-size:20px;font-weight:510;color:#f7f8f8;margin:32px 0 12px">1. Podaci koje prikupljamo</h2>
<p>Prilikom korištenja stranice i usluga prikupljamo: ime i prezime, email, telefon, kompaniju, IP adresu.</p>
<h2 style="font-size:20px;font-weight:510;color:#f7f8f8;margin:32px 0 12px">2. Svrha obrade</h2>
<p>Koristimo ih za odgovor na upite, realizaciju ugovora i slanje informacija uz vašu saglasnost.</p>
<h2 style="font-size:20px;font-weight:510;color:#f7f8f8;margin:32px 0 12px">3. Čuvanje</h2>
<p>Lične podatke čuvamo do 5 godina od posljednje komunikacije.</p>
<h2 style="font-size:20px;font-weight:510;color:#f7f8f8;margin:32px 0 12px">4. Vaša prava</h2>
<p>Pristup, ispravka, brisanje, prenosivost. Zahtjev: hello@bixie.ba</p>
<h2 style="font-size:20px;font-weight:510;color:#f7f8f8;margin:32px 0 12px">5. Kontakt</h2>
<p>hello@bixie.ba | 033 922 622 | Maglajska 1, 71000 Sarajevo</p>
</div>
''')

print('\\n✅ Sve stranice kreirane!')
