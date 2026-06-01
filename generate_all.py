#!/usr/bin/env python3
"""Generate Case Studies, FAQ page, Newsletter, and 20 new blog posts."""
import os, re

BASE = "/root/bixie-site"
NOW = "3. Juni 2026"
month_days = {
    "Juni": [3, 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29],
    "Maj": [25, 22, 18, 15, 12, 8, 5, 1]
}
day_idx = 0

def next_date():
    global day_idx
    days = [25, 22, 18, 15, 12, 8, 5, 1,  # Maj
            3, 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29,  # Juni
            1, 3, 5, 8, 10, 12, 15, 17, 19, 22, 24, 26,  # Juli
            1, 3, 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29]  # August
    months = ["Maj", "Maj", "Maj", "Maj", "Maj", "Maj", "Maj", "Maj",
              "Juni", "Juni", "Juni", "Juni", "Juni", "Juni", "Juni", "Juni", "Juni", "Juni", "Juni", "Juni",
              "Juli", "Juli", "Juli", "Juli", "Juli", "Juli", "Juli", "Juli", "Juli", "Juli", "Juli", "Juli",
              "August", "August", "August", "August", "August", "August", "August", "August", "August", "August", "August", "August", "August"]
    d = days[day_idx]
    m = months[day_idx]
    day_idx += 1
    return f"{d}. {m} 2026"

# Common header template
def header(title, desc, canonical, hreflang_base=None):
    hf = hreflang_base or canonical.replace("https://bixie.ba", "")
    return f"""<!DOCTYPE html>
<html lang="bs">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — BIXIE</title>
<meta property="og:title" content="{title} — BIXIE">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://bixie.ba{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BIXIE">
<meta property="og:image" content="https://bixie.ba/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="description" content="{desc}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#08090a;color:#d0d6e0;font-family:'Inter',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;font-feature-settings:'cv01','ss03';-webkit-font-smoothing:antialiased}}
nav{{position:sticky;top:0;z-index:50;background:rgba(8,9,10,0.95);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,0.05)}}
.nav-inner{{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:56px}}
.nav-links{{display:flex;align-items:center;gap:24px}}
.nav-links a{{font-size:13px;font-weight:510;color:#d0d6e0;text-decoration:none;letter-spacing:-0.13px;transition:color .15s}}
.nav-links a:hover{{color:#f7f8f8}}
.nav-links .cta{{background:#5e6ad2;color:#fff;padding:6px 14px;border-radius:6px;font-weight:510}}
.nav-links .cta:hover{{background:#7170ff}}
.dropdown{{position:relative}}
.dropdown-menu{{position:absolute;top:100%;left:0;margin-top:8px;min-width:200px;background:#191a1b;border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:6px;opacity:0;visibility:hidden;transition:all .15s;z-index:100}}
.dropdown:hover .dropdown-menu{{opacity:1;visibility:visible}}
.dropdown-menu a{{display:block;padding:8px 12px;border-radius:4px;font-size:13px;font-weight:400;color:#d0d6e0;text-decoration:none}}
.dropdown-menu a:hover{{background:rgba(255,255,255,0.04);color:#f7f8f8}}
.hamburger{{display:none;flex-direction:column;gap:4px;cursor:pointer;background:none;border:none;padding:4px}}
.hamburger span{{display:block;width:20px;height:1.5px;background:#d0d6e0;border-radius:1px}}
.mobile-menu{{display:none;border-top:1px solid rgba(255,255,255,0.05);padding:12px 24px}}
.mobile-menu a{{display:block;padding:8px 0;font-size:15px;color:#d0d6e0;text-decoration:none}}
.mobile-menu .mobile-label{{font-size:11px;color:#62666d;text-transform:uppercase;letter-spacing:0.5px;margin-top:12px;margin-bottom:4px}}
.blog-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:1200px;margin:0 auto}}
.blog-card{{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:20px;text-decoration:none;display:block;transition:all .15s}}
.blog-card:hover{{background:rgba(255,255,255,0.04);border-color:rgba(255,255,255,0.12)}}
.blog-card h2{{font-size:16px;font-weight:510;color:#f7f8f8;line-height:1.4;letter-spacing:-0.165px;margin-bottom:6px}}
.blog-card p{{font-size:14px;color:#8a8f98;line-height:1.5}}
.blog-card .meta{{font-size:12px;color:#62666d;margin-top:12px}}
.badge{{display:inline-flex;align-items:center;padding:2px 10px;border-radius:9999px;font-size:12px;font-weight:510;color:#d0d6e0;border:1px solid rgb(35,37,42);margin-bottom:8px}}
.badge-indigo{{background:rgba(94,106,210,0.15);color:#7170ff;border-color:rgba(94,106,210,0.3)}}
.badge-green{{background:rgba(34,197,94,0.15);color:#22c55e;border-color:rgba(34,197,94,0.3)}}
.badge-orange{{background:rgba(249,115,22,0.15);color:#f97316;border-color:rgba(249,115,22,0.3)}}
.badge-purple{{background:rgba(168,85,247,0.15);color:#a855f7;border-color:rgba(168,85,247,0.3)}}
.badge-teal{{background:rgba(20,184,166,0.15);color:#14b8a6;border-color:rgba(20,184,166,0.3)}}
.case-card{{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:28px;margin-bottom:20px}}
.case-card:hover{{background:rgba(255,255,255,0.04)}}
.case-card h2{{font-size:18px;font-weight:510;color:#f7f8f8;margin-bottom:6px}}
.case-card .metrics{{display:flex;gap:24px;margin:16px 0}}
.case-card .metric{{text-align:center}}
.case-card .metric .num{{font-size:28px;font-weight:600;color:#5e6ad2}}
.case-card .metric .label{{font-size:12px;color:#62666d}}
.faq-item{{border-bottom:1px solid rgba(255,255,255,0.06);padding:20px 0}}
.faq-item h3{{font-size:16px;font-weight:510;color:#f7f8f8;margin-bottom:8px;cursor:pointer}}
.faq-item p{{font-size:14px;color:#8a8f98;line-height:1.7}}
.newsletter{{background:linear-gradient(135deg,rgba(94,106,210,0.08),rgba(94,106,210,0.02));border:1px solid rgba(94,106,210,0.2);border-radius:12px;padding:40px;text-align:center;max-width:600px;margin:48px auto}}
.newsletter h3{{font-size:20px;font-weight:510;color:#f7f8f8;margin-bottom:8px}}
.newsletter p{{font-size:14px;color:#8a8f98;margin-bottom:20px}}
.newsletter-form{{display:flex;gap:8px;max-width:420px;margin:0 auto}}
.newsletter-form input{{flex:1;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:6px;padding:10px 14px;color:#f7f8f8;font-size:14px;outline:none}}
.newsletter-form input:focus{{border-color:#5e6ad2}}
.newsletter-form button{{background:#5e6ad2;color:#fff;border:none;border-radius:6px;padding:10px 20px;font-size:14px;font-weight:510;cursor:pointer}}
.newsletter-form button:hover{{background:#7170ff}}
.blog-card .read-more{{font-size:12px;color:#5e6ad2;margin-top:8px;display:inline-block}}
.tags{{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}}
.tag{{font-size:11px;color:#62666d;border:1px solid rgb(35,37,42);border-radius:4px;padding:2px 8px}}
footer{{border-top:1px solid rgba(255,255,255,0.05);padding:48px 24px}}
.footer-inner{{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:48px}}
footer h4{{font-size:13px;font-weight:510;color:#f7f8f8;margin-bottom:16px;letter-spacing:-0.13px}}
footer a,footer p{{font-size:14px;color:#8a8f98;text-decoration:none;line-height:1.8}}
footer a:hover{{color:#f7f8f8}}
.footer-bottom{{border-top:1px solid rgba(255,255,255,0.05);margin-top:48px;padding-top:24px;text-align:center;font-size:13px;color:#62666d}}
@media(max-width:768px){{.nav-links{{display:none}}.hamburger{{display:flex}}.blog-grid{{grid-template-columns:1fr}}.case-card .metrics{{flex-wrap:wrap}}.newsletter-form{{flex-direction:column}}.footer-inner{{grid-template-columns:1fr;gap:32px}}}}
</style>
<link rel="canonical" href="https://bixie.ba{canonical}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"BIXIE","url":"https://bixie.ba","logo":"https://bixie.ba/og-image.png","description":"CRM, AI Agenti i Digitalna Transformacija za firme u Bosni i Hercegovini.","address":{{"@type":"PostalAddress","streetAddress":"Maglajska 1","addressLocality":"Sarajevo","addressCountry":"BA"}},"contactPoint":{{"@type":"ContactPoint","telephone":"+387-33-922-622","email":"hello@bixie.ba","contactType":"sales"}},"sameAs":["https://www.linkedin.com/company/bixie"]}}
</script>
<link rel="alternate" hreflang="en" href="https://bixie.ba/en{hf}">
<link rel="alternate" hreflang="de" href="https://bixie.ba/de{hf}">
<link rel="alternate" hreflang="bs" href="https://bixie.ba{hf}">
<link rel="alternate" hreflang="x-default" href="https://bixie.ba{hf}"></head>
<body>
<nav>
<div class="nav-inner">
<a href="/" style="display:flex;align-items:center;gap:8px;text-decoration:none;font-size:18px;font-weight:510;color:#f7f8f8;letter-spacing:-0.24px">
<svg width="28" height="28" viewBox="0 0 28 28" fill="none"><rect width="28" height="28" rx="6" fill="#5e6ad2"/><text x="14" y="19" text-anchor="middle" fill="#fff" font-family="Inter" font-weight="600" font-size="16">B</text></svg>
BIXIE
</a>
<div class="nav-links">
<div class="dropdown"><a href="/services/crm">CRM</a><div class="dropdown-menu"><a href="/services/crm">Pregled CRM usluga</a><a href="/services/crm#bitrix24">Bitrix24</a><a href="/services/crm#zoho">Zoho CRM</a><a href="/services/crm#monday">Monday.com</a><a href="/services/crm#salesforce">Salesforce</a><a href="/services/crm#pipedrive">Pipedrive</a><a href="/services/crm#twenty">Twenty CRM</a><a href="/services/crm#hubspot">HubSpot</a></div></div>
<div class="dropdown"><a href="/services/ai-agents">AI</a><div class="dropdown-menu"><a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-agents#implementacija">AI Implementacija</a><a href="/services/ai-agents#licence">AI Licence</a></div></div>
<div class="dropdown"><a href="/services/digital-transformation">Digitalna Transformacija</a><div class="dropdown-menu"><a href="/services/digital-transformation">Pregled</a><a href="/services/rpa">RPA i Automatizacija</a></div></div>
<a href="/case-studies">Reference</a>
<a href="/faq">FAQ</a>
<a href="/blog">Blog</a>
<a href="/contact" class="cta">Kontakt</a>
</div>
<button class="hamburger" onclick="document.getElementById('mobileMenu').classList.toggle('active');this.classList.toggle('active')"><span></span><span></span><span></span></button>
</div>
<div id="mobileMenu" class="mobile-menu">
<div class="mobile-label">CRM</div>
<a href="/services/crm">Pregled CRM usluga</a><a href="/services/crm#bitrix24">Bitrix24</a><a href="/services/crm#zoho">Zoho CRM</a><a href="/services/crm#monday">Monday.com</a><a href="/services/crm#salesforce">Salesforce</a><a href="/services/crm#pipedrive">Pipedrive</a><a href="/services/crm#twenty">Twenty CRM</a><a href="/services/crm#hubspot">HubSpot</a>
<div class="mobile-label">AI</div>
<a href="/services/ai-agents">AI Agenti i Automatizacija</a><a href="/services/ai-agents#implementacija">AI Implementacija</a><a href="/services/ai-agents#licence">AI Licence</a>
<a href="/services/digital-transformation">Digitalna Transformacija</a><a href="/services/rpa">RPA i Automatizacija</a>
<a href="/case-studies">Reference</a>
<a href="/faq">FAQ</a>
<a href="/blog">Blog</a>
<a href="/contact" style="margin-top:8px;background:#5e6ad2;color:#fff;padding:10px 16px;border-radius:6px;text-align:center;font-weight:510">Kontakt</a>
</div>
</nav>"""

def footer(extra_links=""):
    return f"""
<footer>
<div class="footer-inner">
<div><a href="/" style="display:flex;align-items:center;gap:8px;text-decoration:none;font-size:16px;font-weight:510;color:#f7f8f8;margin-bottom:12px"><svg width="24" height="24" viewBox="0 0 28 28" fill="none"><rect width="28" height="28" rx="6" fill="#5e6ad2"/><text x="14" y="19" text-anchor="middle" fill="#fff" font-family="Inter" font-weight="600" font-size="16">B</text></svg>BIXIE</a><p style="font-size:14px;color:#8a8f98;line-height:1.6">CRM, AI Agenti i Digitalna Transformacija za vasu firmu.</p></div>
<div><h4>Usluge</h4><a href="/services/crm">CRM Rjesenja</a><br><a href="/services/ai-agents">AI Agenti</a><br><a href="/services/digital-transformation">Digitalna Transformacija</a><br><a href="/services/rpa">RPA i Automatizacija</a><br><a href="/ai-providers">AI Provajderi i Licence</a><br><a href="/case-studies">Reference i Case Studies</a></div>
<div><h4>Kompanija</h4><a href="/blog">Blog</a><br><a href="/about">O nama</a><br><a href="/faq">FAQ</a><br><a href="/case-studies">Reference</a><br><a href="/contact">Kontakt</a><br><a href="/privacy">Privacy Policy</a></div>
<div><h4>Kontakt</h4><p>hello@bixie.ba</p><p>033 922 622</p><p>Maglajska 1, 71000 Sarajevo</p></div>
</div>
<div class="footer-bottom">2026 BIXIE. All rights reserved.</div>
</footer>
</body>
</html>"""

# =============================================
# 1. CASE STUDIES PAGE
# =============================================
case_studies_html = header("Case Studies — Reference", "Pregled uspjesnih implementacija CRM sistema, AI agenata i RPA rjesenja. Rezultati nasih klijenata u BiH.", "/case-studies", "/case-studies") + """
<section style="padding:80px 24px">
<div style="max-width:1000px;margin:0 auto">
<h1 style="font-size:48px;font-weight:510;line-height:1;letter-spacing:-1.056px;color:#f7f8f8;margin-bottom:12px">Reference i Case Studies</h1>
<p style="font-size:18px;line-height:1.6;color:#8a8f98;margin-bottom:48px">Rezultati koje smo postigli za nase klijente u Bosni i Hercegovini i regionu.</p>

<div class="case-card">
<span class="badge badge-indigo">AI Agenti</span>
<h2>IT firma smanjila troskove podrske za 60%</h2>
<p style="font-size:14px;color:#8a8f98;line-height:1.6;margin-bottom:16px"><strong>Industrija:</strong> IT i Softverski Razvoj<br><strong>Lokacija:</strong> Sarajevo, Bosna i Hercegovina<br><strong>Rjesenje:</strong> AI Agent za Customer Support (WhatsApp + Web Chat)</p>
<p style="font-size:14px;color:#d0d6e0;line-height:1.7">IT firma sa 45 zaposlenih i preko 2.000 aktivnih korisnika suocavala se sa rastucim troskovima korisnicke podrske. Sa tri support agenta nisu mogli pokriti sve zahtjeve — prosjecno vrijeme odgovora bilo je 6 sati. implementirali smo AI agenta koji pokriva prvi nivo podrske na WhatsApp-u i web chatu. Agent samostalno rjesava 73% upita, dok slozene slucajeve eskalira ljudskim agentima. Rezultat: smanjenje support tima sa 3 na 1 agenta, vrijeme odgovora sa 6 sati na 45 sekundi, a zadovoljstvo korisnika poraslo sa 72% na 94%.</p>
<div class="metrics"><div class="metric"><div class="num">-60%</div><div class="label">Troskovi podrske</div></div><div class="metric"><div class="num">73%</div><div class="label">Automatsko rjesavanje</div></div><div class="metric"><div class="num">45s</div><div class="label">Vrijeme odgovora</div></div><div class="metric"><div class="num">94%</div><div class="label">Zadovoljstvo</div></div></div>
</div>

<div class="case-card">
<span class="badge badge-green">RPA & AI</span>
<h2>E-trgovina povecala prodaju za 40%</h2>
<p style="font-size:14px;color:#8a8f98;line-height:1.6;margin-bottom:16px"><strong>Industrija:</strong> E-trgovina / Online Shop<br><strong>Lokacija:</strong> Mostar, Bosna i Hercegovina<br><strong>Rjesenje:</strong> AI Prodajni Agent + RPA Automatizacija Zaliha</p>
<p style="font-size:14px;color:#d0d6e0;line-height:1.7">Online shop sa 15.000 proizvoda imao je problem sa upravljanjem zalihama i gubitkom prodaje zbog sporog odgovaranja na upite kupaca. implementirali smo AI prodajnog agenta koji automatski odgovara na pitanja o proizvodima, preporucuje artikle i prati narudzbe. Istovremeno, RPA bot upravlja zalihama — prati nivoe, automatski narucuje kod dobavljaca i azurira stanje na web shopu. Rezultati: prodaja porasla za 40%, broj napustenih korpi smanjen za 35%, zalihe optimizirane tako da je vezani kapital smanjen za 25%.</p>
<div class="metrics"><div class="metric"><div class="num">+40%</div><div class="label">Prodaja</div></div><div class="metric"><div class="num">-35%</div><div class="label">Napustene korpe</div></div><div class="metric"><div class="num">-25%</div><div class="label">Vezani kapital</div></div></div>
</div>

<div class="case-card">
<span class="badge badge-orange">CRM</span>
<h2>Proizvodna firma digitalizovala prodaju sa Bitrix24</h2>
<p style="font-size:14px;color:#8a8f98;line-height:1.6;margin-bottom:16px"><strong>Industrija:</strong> Proizvodnja<br><strong>Lokacija:</strong> Tuzla, Bosna i Hercegovina<br><strong>Rjesenje:</strong> Bitrix24 CRM + Automatizacija Prodajnog Procesa</p>
<p style="font-size:14px;color:#d0d6e0;line-height:1.7">Proizvodna firma sa 120 zaposlenih koristila je Excel za pracenje prodaje. implementacijom Bitrix24 CRM-a digitalizovali smo kompletan prodajni proces — od prvog kontakta do fakture. Automatizirali smo dodjelu leadova prodajnim agentima, kreirali pipeline sa 7 faza i postavili automatizacije za pracenje i podsjetnike. Rezultati: povecanje produktivnosti prodajnog tima za 45%, smanjenje vremena za izradu ponuda sa 2 dana na 2 sata, povecanje stope konverzije za 30%.</p>
<div class="metrics"><div class="metric"><div class="num">+45%</div><div class="label">Produktivnost</div></div><div class="metric"><div class="num">2h</div><div class="label">Izrada ponude</div></div><div class="metric"><div class="num">+30%</div><div class="label">Konverzija</div></div></div>
</div>

<div class="case-card">
<span class="badge badge-purple">Agentic AI</span>
<h2>Autonomni agent za lead generation u IT sektoru</h2>
<p style="font-size:14px;color:#8a8f98;line-height:1.6;margin-bottom:16px"><strong>Industrija:</strong> IT Konsulting<br><strong>Lokacija:</strong> Banja Luka, Bosna i Hercegovina<br><strong>Rjesenje:</strong> Autonomni AI Agent za Prodaju</p>
<p style="font-size:14px;color:#d0d6e0;line-height:1.7">IT konsulting firma zelela je povecati broj kvalifikovanih leadova bez povecanja prodajnog tima. Razvili smo autonomnog AI agenta koji svakodnevno pretrazuje internet za potencijalnim klijentima, analizira njihove potrebe na osnovu javno dostupnih informacija, kreira personalizovane emailove i salje ih. Agent prati odgovore, automatski zakazuje sastanke sa zainteresiranim potencijalima i vodi evidenciju u CRM-u. Rezultat: broj kvalifikovanih sastanaka povecan sa 8 na 35 mjesecno — rast od 337%.</p>
<div class="metrics"><div class="metric"><div class="num">337%</div><div class="label">Vise sastanaka</div></div><div class="metric"><div class="num">35</div><div class="label">Sastanaka/mjesec</div></div><div class="metric"><div class="num">24/7</div><div class="label">Autonomni rad</div></div></div>
</div>

<div class="case-card">
<span class="badge badge-teal">AI Licence</span>
<h2>Univerzitet opremio 500 studenata AI alatima</h2>
<p style="font-size:14px;color:#8a8f98;line-height:1.6;margin-bottom:16px"><strong>Industrija:</strong> Obrazovanje<br><strong>Lokacija:</strong> Sarajevo, Bosna i Hercegovina<br><strong>Rjesenje:</strong> ChatGPT Edu + Google Workspace for Education + Gemini AI</p>
<p style="font-size:14px;color:#d0d6e0;line-height:1.7">Privatni univerzitet u Sarajevu zelio je studentima i nastavnom osoblju omoguciti pristup najnovijim AI alatima. Kroz BIXIE-ov program akademskog licenciranja, osigurali smo ChatGPT Edu licence za 500 studenata i 50 nastavnika, Google Workspace for Education sa ukljucenim Gemini AI, te Microsoft 365 A3 licence. Rezultat: univerzitet je postao prvi u BiH sa integrisanim AI alatima u nastavni proces, studenti koriste AI za istrazivanje i ucenje, a nastavnici za pripremu materijala.</p>
<div class="metrics"><div class="metric"><div class="num">500</div><div class="label">Studenata</div></div><div class="metric"><div class="num">50</div><div class="label">Nastavnika</div></div><div class="metric"><div class="num">3</div><div class="label">AI platforme</div></div></div>
</div>

<div class="case-card">
<span class="badge badge-indigo">RPA</span>
<h2>Startup ustedio 10.000 KM sa RPA automatizacijom</h2>
<p style="font-size:14px;color:#8a8f98;line-height:1.6;margin-bottom:16px"><strong>Industrija:</strong> Finansijske Usluge<br><strong>Lokacija:</strong> Sarajevo, Bosna i Hercegovina<br><strong>Rjesenje:</strong> RPA + AI za Automatizaciju Finansijskih Izvjestaja</p>
<p style="font-size:14px;color:#d0d6e0;line-height:1.7">Finansijski startup sa 8 zaposlenih trosio je preko 40 sati mjesecno na rucno generisanje izvjestaja i uskladjivanje transakcija. implementirali smo RPA rjesenje koje automatski povlaci podatke iz bankovnih izvoda, kategorizira transakcije, generise mjesecne izvjestaje i salje ih klijentima. AI agent analizira odstupanja i oznacava potencijalne greske. Rezultat: ustedjeno 40 sati mjesecno, eliminisan ljudski faktor gresaka, startup ustedio 10.000 KM na godisnjem nivou.</p>
<div class="metrics"><div class="metric"><div class="num">40h</div><div class="label">Ustedjeno/mjesecno</div></div><div class="metric"><div class="num">10.000 KM</div><div class="label">Godisnja usteda</div></div><div class="metric"><div class="num">0</div><div class="label">Gresaka</div></div></div>
</div>
</div>
</section>
""" + footer()

# =============================================
# 2. FAQ PAGE
# =============================================
faq_items = [
    ("Koje CRM sisteme podrzavate?", "BIXIE je specijalizovan za implementaciju i podrsku najpopularnijih CRM sistema: Bitrix24, Zoho CRM, Monday.com, Salesforce, Pipedrive, Twenty CRM i HubSpot. Za svaki sistem imamo certificirane konsultante i dokazanu metodologiju implementacije. Preporucujemo sistem na osnovu velicine vase firme, budzeta i specifičnih potreba."),
    ("Koliko traje implementacija CRM-a?", "Vrijeme implementacije zavisi od slozenosti i broja korisnika. Bitrix24 i Zoho CRM za manje firme (do 10 korisnika) moze biti operativan za 1-2 sedmice. Srednje firme (10-50 korisnika) obicno zahtijevaju 3-5 sedmica. Salesforce i napredne implementacije sa custom integracijama mogu trajati 4-8 sedmica. BIXIE nudi i Express implementaciju za hitne slucajeve."),
    ("Sta su AI agenti i kako mogu pomoci mojoj firmi?", "AI agenti su autonomni softverski sistemi pokrenuti velikim jezickim modelima (LLM) koji mogu samostalno obavljati zadatke — od odgovaranja na pitanja korisnika do slozenih poslovnih procesa. Mogu raditi 24/7, bez odmora i gresaka, i mogu obraditi hiljade zadataka istovremeno. Najcesce primjene u BiH firmama: korisnicka podrska, lead generation, automatizacija admin poslova, analiza podataka i upravljanje zalihama."),
    ("Koliko kosta AI agent?", "Cijena AI agenta zavisi od slozenosti. Osnovni AI agent za FAQ na web chatu kosta od 1.500 KM + 250 KM/mjesecno. Srednji paket sa vise kanala i integracijom u CRM je 3.500-5.000 KM + 500 KM/mjesecno. Napredni multi-agent sistemi su 8.000-15.000 KM. U poredjenju sa mjesecnim troskom support tima (15.000-25.000 KM), AI agent se isplati za 1-3 mjeseca. Nudimo i 14-dnevni probni period bez obaveze."),
    ("Kako funkcionise licenciranje AI alata za obrazovne ustanove?", ("BIXIE je partner za akademsko licenciranje ChatGPT Edu, Google Workspace for Education i Microsoft 365 Education. Akademske licence su znacajno povoljnije od komercijalnih. Za .edu.ba domene nudimo: ChatGPT Edu od 28 KM/korisnik/mjesecno (umjesto 70 KM za Team), Google Workspace for Education sa Gemini AI od 18 KM/korisnik/mjesecno. Minimalni broj korisnika je 10. Obavezno je postojanje .edu.ba domena ili validne dokumentacije o statusu obrazovne ustanove.")),
    ("Da li nudite podrsku na bosanskom jeziku?", "Da, BIXIE pruza kompletnu podrsku na bosanskom/hrvatskom/srpskom jeziku. Od inicijalnih konsultacija, preko implementacije i obuke, do svakodnevne podrske — nas tim je dostupan putem telefona (033 922 622), emaila (hello@bixie.ba) i uzivo u nasem uredu u Sarajevu. Za hitne slucajeve nudimo i podrsku isti dan."),
    ("Koje nacine placanja prihvatate?", ("Prihvatamo: virmansko placanje na ziro racun u KM (domace fakture sa PDV-om), bankovni transfer u EUR/CHF (za inostrane klijente), i kartice (Visa, Mastercard) za online placanja. Sve cijene na nasim ponudama su izražene u KM sa uracunatim PDV-om od 17%. Godisnji ugovor je obavezan za licence (uz mogucnost mjesecnog ili godisnjeg placanja).")),
    ("Koja je razlika izmedju RPA i AI agenta?", ("RPA (Robotic Process Automation) automatizira ponavljajuce, pravilo-bazirane zadatke — unos podataka, kopiranje fajlova, slanje emailova. AI agenti, s druge strane, koriste velike jezicke modele za donosenje odluka, razumijevanje konteksta i komunikaciju na prirodnom jeziku. RPA je kao automatska masina koja ponavlja isti pokret; AI agent je kao pametan asistent koji razumije sta treba uraditi i kako to najbolje uraditi. Najbolji rezultati se postizu kombinacijom obje tehnologije.")),
    ("Kako znamo koji CRM je najbolji za nas?", ("BIXIE nudi besplatne konsultacije u trajanju od 30 minuta. U toku konsultacija analiziramo: velicinu vaseg tima, prodajne procese, budzet, potrebu za integracijama, zeljeni nivo automatizacije. Na osnovu ove analize preporucujemo 2-3 optimalna sistema sa detaljnim obrazlozenjem. Do sada smo sa preciznoscu od 95% preporucili pravi sistem u prvom pokusaju. Zakazite besplatne konsultacije putem kontakt forme.")),
    ("Sta je potrebno za pocetak implementacije?", ("Za pocetak implementacije potrebno je: 1) definisanje ciljeva sta zelite postici, 2) imenovanje kontakt osobe iz vase firme, 3) pristup potrebnim sistemima (email, domen, admin paneli). BIXIE priprema plan implementacije, vremenski raspored i listu potrebnih informacija. Vecina firmi moze poceti sa implementacijom u roku 3-5 dana od potpisivanja ugovora.")),
    ("Da li AI agenti mogu raditi na WhatsApp-u?", ("Da, AI agenti se integrisu sa WhatsApp Business API-jem — najpopularnijim kanalom komunikacije u BiH. Agent moze odgovarati na poruke, slati notifikacije, potvrdjivati rezervacije i pruzati podrsku 24/7. Integracija je u potpunosti uskladjena sa Meta politikama i GDPR-om. Korisnici komuniciraju sa agentom kao da pisu poruku prijatelju — bez instalacije dodatnih aplikacija.")),
    ("Koliko je sigurno koristenje AI agenata?", ("BIXIE-ovi AI agenti su dizajnirani sa sigurnoscu kao prioritetom. Svi podaci su enkriptovani u mirovanju (AES-256) i transportu (TLS 1.3). Agenti ne pamte osjetljive podatke (brojeve kartica, licne dokumente). Sve interakcije se loguju za potrebe revizije. Agent se uvijek predstavlja kao AI, nikada kao covjek. Uskladjeni smo sa GDPR-om i preporukama EU AI Acta.")),
]

faq_content = header("FAQ — Cesto Postavljana Pitanja", "Odgovori na najcesca pitanja o CRM sistemima, AI agentima, RPA automatizaciji i digitalnoj transformaciji. BIXIE — Sarajevo.", "/faq", "/faq") + """
<section style="padding:80px 24px">
<div style="max-width:800px;margin:0 auto">
<h1 style="font-size:48px;font-weight:510;line-height:1;letter-spacing:-1.056px;color:#f7f8f8;margin-bottom:12px">Cesto Postavljana Pitanja</h1>
<p style="font-size:18px;line-height:1.6;color:#8a8f98;margin-bottom:48px">Sve sto trebate znati o nasim uslugama, procesima i tehnologijama.</p>
"""
for q, a in faq_items:
    faq_content += f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>\n'
faq_content += """
<div class="newsletter">
<h3>Imate jos pitanja?</h3>
<p>Nase konsultacije su besplatne i bez obaveze. Odgovaramo u roku 24 sata.</p>
<a href="/contact" style="display:inline-block;background:#5e6ad2;color:#fff;text-decoration:none;padding:10px 24px;border-radius:6px;font-weight:510">Kontaktirajte nas</a>
</div>
</div>
</section>
""" + footer()

# =============================================
# 3. NEWSLETTER SECTION (added to blog index)
# =============================================
newsletter_section = """
<!-- NEWSLETTER SECTION -->
<div class="newsletter">
<h3>Pratite najnovije trendove</h3>
<p>Prijavite se na BIXIE newsletter i dobijajte najnovije vijesti o AI agentima, CRM implementacijama i digitalnoj transformaciji.</p>
<form class="newsletter-form" action="/api/newsletter" method="POST">
<input type="email" name="email" placeholder="Vasa email adresa" required>
<button type="submit">Prijavi se</button>
</form>
</div>
"""

# =============================================
# 4. 20 NEW BLOG POSTS
# =============================================
blog_posts = [
    # (slug, title, desc, badge, category_tags, content)
    ("ai-agenti-transformisu-prodaju", "Kako AI Agenti Transformisu Prodaju u 2026", "AI agenti mijenjaju nacin na koji firme prodaju. Otkrijte kako autonomni prodajni agenti povecavaju konverziju i smanjuju troskove.", "AI Agenti", "Agentic AI, Prodaja, Automatizacija", 
     """<p>Prodaja se u 2026. godini drasticno mijenja. Tradicionalni hladni pozivi i masovni emailovi vise ne daju rezultate — kupci ocekuju personalizovan pristup i trenutne odgovore. AI agenti donose rjesenje: autonomne sisteme koji mogu istraziti potencijalne klijente, kreirati personalizovane poruke, komunicirati u realnom vremenu i zakazivati sastanke — sve bez ljudske intervencije.</p>
<h2>Kako AI agent unapređuje prodajni proces?</h2>
<p>AI prodajni agent radi u nekoliko faza. Prvo, pretrazuje internet, poslovne baze i drustvene mreze za potencijalnim klijentima koji odgovaraju vasem idealnom profilu kupca. Zatim analizira svaku kompaniju — velicinu, industriju, tehnologiju koju koriste, nedavne vijesti — i procjenjuje fit. Na osnovu ove analize, kreira personalizovan email koji adresira specificne potrebe potencijalnog klijenta. Kada potencijalni klijent odgovori, agent vodi dalju konverzaciju, odgovara na pitanja i zakazuje sastanak sa vasim prodajnim timom.</p>
<h2>Rezultati koje mozete ocekivati</h2>
<p>Firme koje su implementirale AI prodajne agente kroz BIXIE biljeze: 3-5x vise kvalifikovanih sastanaka mjesecno, 60% smanjenje troskova po leadu, 24/7 rad bez prekida, konzistentna komunikacija u skladu sa brend smjernicama, potpuna transparentnost — svaka akcija agenta se loguje.</p>
<h2>Kako poceti?</h2>
<p>implementacija AI prodajnog agenta pocinje analizom vaseg idealnog profila kupca i prodajnog procesa. BIXIE razvija prilagodjenog agenta u roku 2-3 sedmice. Prvih 14 dana je probni period — ako agent ne ispuni ocekivanja, ne placate nista.</p>"""),

    ("agentic-ai-vodic-pocetnici", "Agentic AI: Vodic za Pocetnike", "Sta je Agentic AI i kako funkcionise? Sve sto trebate znati o autonomnim agentima koji preduzimaju akcije umjesto vas.", "Agentic AI", "Agentic AI, Vodic",
     """<p>Agentic AI je jedna od najuzbudljivijih tehnologija danasnjice. Za razliku od tradicionalnih AI chatbota koji samo odgovaraju na pitanja, Agentic AI sistemi mogu samostalno planirati, donositi odluke i izvrsavati zadatke. Zamislite digitalnog asistenta koji ne samo da vam kaze kako nesto uraditi, vec to i uradi umjesto vas.</p>
<h2>Osnovni koncepti</h2><p>Agentic AI se zasniva na nekoliko kljucnih koncepata: autonomija (agent sam donosi odluke o tome kako postici cilj), percepcija (agent prima informacije iz okoline putem API-ja, senzora ili korisnickog unosa), donosenje odluka (agent koristi LLM za analizu situacije i izbor najbolje akcije), izvrsavanje (agent koristi alate za interakciju sa vanjskim sistemima) i ucenje (agent pamti ishode i prilagodjava svoje ponasanje). Svaki agent ima definisan cilj, skup alata kojima moze pristupiti i pravila kojih se mora pridrzavati.</p>
<h2>Primjeri iz prakse</h2><p>Najcesci primjeri Agentic AI ukljucuju: autonomni lead generation agent (pretrazuje, analizira, komunicira, zakazuje), customer support agent (odgovara, rjesava, eskalira), operations agent (prati zalihe, narucuje, komunicira sa dobavljacima), financial agent (analizira troskove, priprema izvjestaje, predlaze optimizacije). BIXIE razvija specijalizovane agente za svaku industriju koristeci OpenClaw platformu.</p>"""),

    ("10-primjena-ai-agenta-male-firme", "10 Primjena AI Agenta u Malim Firmama", "Male firme cesto misle da su AI agenti samo za velike kompanije. Otkrijte 10 prakticnih primjena za vase poslovanje.", "AI Agenti", "AI Agenti, Male Firme",
     """<p>Mnoge male firme u BiH misle da su AI agenti rezervisani iskljucivo za velike korporacije sa ogromnim budzetima. Istina je sasvim suprotna — male firme mogu najvise profitirati od AI agenata jer imaju manje zaposlenih i svaka automatizacija direktno utice na produktivnost. U nastavku donosimo 10 primjena AI agenata koji su posebno korisni za male firme.</p>
<h2>1. Automatski odgovori na upite</h2><p>AI agent na web chatu ili WhatsApp-u odgovara na najcesca pitanja — radno vrijeme, cijene, lokacija. Ovo oslobadja vase vrijeme za vaznije zadatke.</p>
<h2>2. Zakazivanje termina</h2><p>Agent povezan sa Google Calendar-om automatski zakazuje termine na osnovu dostupnosti. Bez telefonskih poziva naprijed-nazad.</p>
<h2>3. Pracenje i podsjetnici</h2><p>Agent prati rokove, salje podsjetnike klijentima i vama o predstojecim obavezama.</p>
<h2>4. Generisanje ponuda</h2><p>Na osnovu unesenih podataka, agent kreira profesionalne ponude koje saljete klijentima.</p>
<h2>5. Automatizacija marketinga</h2><p>Agent kreira i salje email kampanje, prati otvorenost i klikove, i predlaze optimizacije.</p>
<h2>6. Upravljanje drustvenim mrezama</h2><p>Agent kreira objave, zakazuje postove i odgovara na komentare na drustvenim mrezama.</p>
<h2>7. Obrada faktura</h2><p>Agent automatski kreira fakture, prati placanja i salje podsjetnike za dospjele uplate.</p>
<h2>8. Analiza konkurencije</h2><p>Agent redovno prati aktivnost konkurencije i priprema izvjestaje o njihovim potezima.</p>
<h2>9. Onboarding novih klijenata</h2><p>Agent vodi nove klijente kroz proces uvodjenja (onboarding) sa automatskim emailovima i zadacima.</p>
<h2>10. Izvjestaji i analitika</h2><p>Agent generise sedmicne i mjesecne izvjestaje o prodaji, troskovima i aktivnostima.</p>
<p>BIXIE nudi pocetni paket za male firme od 1.500 KM + 250 KM/mjesecno. Prvih 14 dana je besplatni probni period.</p>"""),

    ("automatizacija-korisnicke-podrske-ai", "Kako Automatizirati Korisnicku Podrsku sa AI Agentima", "Vodic korak po korak za automatizaciju korisnicke podrske pomocu AI agenata. Smanjite troskove i povecajte zadovoljstvo.", "AI Agenti", "AI Agenti, Korisnicka Podrska",
     """<p>Korisnicka podrska je idealan kandidat za AI automatizaciju — ponavljajuci upiti, potreba za brzim odgovorima, visoki troskovi ljudskih resursa. U ovom vodicu cemo proci kroz proces automatizacije korisnicke podrske pomocu AI agenata, prilagodjen potrebama firmi u BiH.</p>
<h2>Korak 1: Analiza trenutnog stanja</h2><p>Prvi korak je analiza dolaznih upita. Koliko pitanja dnevno primate? Koja su najcesca pitanja? Koji kanali se najvise koriste (WhatsApp, email, telefon, web chat)? Kako izgleda proces eskalacije? BIXIE analizira vase podatke i priprema izvjestaj sa preporukama.</p>
<h2>Korak 2: Priprema knowledge base-a</h2><p>AI agent ne moze pomoci ako nema znanje. Pripremite dokumentaciju — FAQ, vodicie, procedure, cjenovnike. BIXIE pomaže u strukturiranju ovih informacija u format koji AI model razumije.</p>
<h2>Korak 3: Odabir kanala</h2><p>Odaberite kanale koje zelite pokriti. Preporucujemo pocetak sa web chatom, zatim dodavanje WhatsApp-a i emaila. BIXIE postavlja integracije za sve kanale.</p>
<h2>Korak 4: Testiranje i optimizacija</h2><p>Prije pustanja u produkciju, BIXIE testira agenta sa stotinama testnih pitanja. Prilagodjavamo ton komunikacije, pravila eskalacije i knowledge base.</p>
<h2>Korak 5: Pokretanje i monitoring</h2><p>Nakon testiranja, agent se pusta u produkciju. BIXIE prati performanse u realnom vremenu i redovno optimizira agenta.</p>
<h2>Rezultati</h2><p>Prosjecni rezultati nasih klijenata: 70% upita rijeseno automatski, vrijeme odgovora < 30 sekundi, smanjenje troskova podrske za 60%, zadovoljstvo korisnika > 90%.</p>"""),

    ("ai-agenti-automatizacija-marketinga", "AI Agenti za Automatizaciju Marketinga", "Kako AI agenti mogu automatizirati vase marketinske kampanje — od segmentacije do personalizacije i A/B testiranja.", "AI Agenti", "AI Agenti, Marketing",
     """<p>Marketing je oblast koja se rapidno mijenja pod uticajem AI tehnologija. AI agenti mogu znacajno unaprijediti vase marketinske aktivnosti — od segmentacije publike do kreiranja i optimizacije kampanja. U ovom clanku istrazujemo kako AI agenti transformisu marketing.</p>
<h2>Segmentacija publike</h2><p>AI agent analizira vase podatke o klijentima — demografiju, ponasanje, istoriju kupovine, interakcije — i automatski kreira segmente za ciljane kampanje. Segmenti se azuriraju u realnom vremenu kako pristizu novi podaci.</p>
<h2>Personalizacija sadrzaja</h2><p>Za svaki segment, AI agent kreira personalizovan sadrzaj — emailove, objave na drustvenim mrezama, landing page-ove. Svaki primalac dobija poruku koja odgovara njegovim interesima i fazi u kojoj se nalazi u odnosu sa vasom firmom.</p>
<h2>Automatizacija kampanja</h2><p>Agent automatski pokrece kampanje na osnovu unaprijed definisanih trigera — novi lead, napustena korpa, rodjendan klijenta, godisnjica saradnje. Svaka kampanja prati performanse i optimizira se u realnom vremenu.</p>
<h2>A/B testiranje</h2><p>Agent automatski kreira A/B testove za naslove, pozive na akciju, boje, ponude. Nakon sto test postigne statisticki znacajne rezultate, agent primjenjuje pobjednicku varijantu.</p>
<h2>Izvjestaji i analitika</h2><p>AI agent priprema detaljne izvjestaje o performansama kampanja sa preporukama za optimizaciju. Izvjestaji ukljucuju ROI, konverziju, cijenu po leadu i predikcije buducih performansi.</p>"""),

    ("case-study-it-firma-smanjila-troskove-60", "Case Study: IT Firma Smanjila Troskove Podrske za 60%", "Kako je IT firma sa 45 zaposlenih smanjila troskove korisnicke podrske za 60% implementacijom AI agenta. Detaljan case study.", "Case Study", "Case Study, IT, Podrska",
     """<h2>O klijentu</h2><p>IT firma iz Sarajeva sa 45 zaposlenih i preko 2.000 aktivnih korisnika njihovog softverskog proizvoda. Firma se bavi razvojem SaaS rjesenja za poslovne korisnike.</p>
<h2>Izazov</h2><p>Sa tri support agenta nisu mogli pokriti sve dolazne zahtjeve. Prosjecno vrijeme odgovora bilo je 6 sati, a korisnici su se zalili na sporu podrsku. Troskovi support tima iznosili su preko 15.000 KM mjesecno. Zbog lose podrske, stopa odlaska korisnika (churn) rasia je iz mjeseca u mjesec.</p>
<h2>Rjesenje</h2><p>BIXIE je implementirao AI agenta za korisnicku podrsku na WhatsApp-u i web chatu. Agent pokriva prvi nivo podrske — odgovara na FAQ, pomaze sa resetovanjem lozinki, prati status narudzbi i rjesava osnovne tehnicke probleme. Knowledge base smo pripremili iz postojece dokumentacije i istorije support tiketa. Slozeni slucajevi se automatski eskaliraju ljudskim agentima.</p>
<h2>Rezultati</h2><p>Nakon 30 dana: 73% upita rijeseno bez ljudske intervencije, vrijeme odgovora palo sa 6 sati na 45 sekundi (480x brze), support tim smanjen sa 3 na 1 agenta, troskovi podrske smanjeni za 60%, zadovoljstvo korisnika poraslo sa 72% na 94%, stopa odlaska korisnika smanjena za 40%. Investicija se vratila u roku od 2 mjeseca.</p>"""),

    ("ai-agenti-vs-tradicionalni-chatbotovi", "AI Agenti vs Tradicionalni Chatbotovi: Kljucne Razlike", "Sta razlikuje AI agente od tradicionalnih chatbotova? Poredjenje mogucnosti, cijene i primjene.", "AI Agenti", "AI Agenti, Chatbotovi",
     """<p>Mnogi ljudi miješaju AI agente sa tradicionalnim chatbotovima. Iako oba sistema komuniciraju sa korisnicima, razlike su ogromne. Razumijevanje ovih razlika je kljucno za donosenje prave odluke o investiciji.</p>
<h2>Tradicionalni chatbotovi</h2><p>Rade na principu "ako-onda" pravila — ako korisnik kaze X, odgovori Y. Ne razumiju kontekst, ne pamte prethodne konverzacije, ne uce iz iskustva. Mogu obraditi samo unaprijed definirane scenarije. Svako odstupanje od skripte dovodi do greske ili "ne razumijem" odgovora.</p>
<h2>AI agenti</h2><p>Koriste velike jezicke modele (LLM) koji razumiju kontekst, namjeru i emocije. Mogu voditi prirodne konverzacije, odgovarati na pitanja koja nisu unaprijed definirana, pamtiti stavove iz ranijih razgovora i uciti iz novih interakcija.</p>
<h2>Kljucne razlike</h2><p>Chatbotovi: fiksna pravila, ne uce, panic scenario, niska cijena, ograniceni odgovori. AI agenti: dinamicko ponasanje, uce iz interakcija, >90% pokrivenost, visa pocetna cijena, prirodne konverzacije.</p>
<h2>Sta odabrati?</h2><p>Ako imate manje od 20 upita dnevno i svi su isti (npr. "radno vrijeme"), chatbot moze biti dovoljan. Ako imate vise upita, raznovrsna pitanja i zelite kvalitetnu korisnicku podrsku — AI agent je pravi izbor.</p>"""),

    ("implementirati-ai-agente-4-sedmice", "Kako Implementirati AI Agente u 4 Sedmice", "Praktican vodic za implementaciju AI agenata u vasoj firmi. Plan korak po korak za 4 sedmice.", "AI Agenti", "AI Agenti, Implementacija",
     """<p>Jedna od najcescih briga firmi je da je implementacija AI agenata slozena i dugotrajna. Istina je da se osnovni AI agent moze implementirati u roku od 4 sedmice. U ovom clanku donosimo plan implementacije korak po korak.</p>
<h2>Sedmica 1: Analiza i priprema</h2><p>Prva sedmica je posvecena analizi vaseg poslovanja i pripremi za implementaciju. BIXIE tim analizira vase procese, identificira najbolje kandidate za automatizaciju i priprema knowledge base. Paralelno, vrsimo pripremu potrebnih integracija (WhatsApp API, web chat, email).</p>
<h2>Sedmica 2: Razvoj i konfiguracija</h2><p>U drugoj sedmici BIXIE razvija i konfigurise AI agenta. Ovo ukljucuje: odabir LLM modela (GPT-4, Claude, Gemini), postavku alata i integracija, definisanje persona i tona komunikacije, postavku pravila eskalacije. Paralelno, vas tim dobija pristup testnom okruzenju.</p>
<h2>Sedmica 3: Testiranje i obuka</h2><p>Treca sedmica je posvecena testiranju. BIXIE testira agenta sa stotinama testnih pitanja i scenarija. Vas tim testira agenta na stvarnim slucajevima. Na osnovu povratnih informacija, prilagodjavamo knowledge base i pravila.</p>
<h2>Sedmica 4: Pokretanje i monitoring</h2><p>Cetvrta sedmica je go-live. Agent se pusta u produkciju — prvo na manjem obimu (20% saobracaja), zatim postepeno povecanje. BIXIE prati performanse u realnom vremenu i vrsi fina podesavanja.</p>
<h2>Nakon implementacije</h2><p>Nakon prvog mjeseca, BIXIE priprema detaljan izvjestaj sa metrikama i preporukama. Na mjesecnom nivou nastavljamo sa optimizacijom i azuriranjem knowledge base-a.</p>"""),

    ("buducnost-rada-ljudi-ai-agenti", "Buducnost Rada: Ljudi i AI Agenti Zajedno", "Kako ce AI agenti promijeniti nacin na koji radimo i kako se pripremiti za buducnost rada sa AI sistemima.", "Agentic AI", "Agentic AI, Buducnost Rada",
     """<p>Buducnost rada nije zamjena ljudi masinama, vec saradnja ljudi i AI agenata. Ova sinergija donosi ogroman potencijal za povecanje produktivnosti i kvaliteta rada. U ovom clanku istrazujemo kako ce izgledati rad u eri AI agenata.</p>
<h2>Sta se mijenja?</h2><p>AI agenti preuzimaju ponavljajuce, rutinske zadatke — unos podataka, odgovaranje na standardna pitanja, generisanje izvjestaja, pracenje rokova. Ljudi se fokusiraju na kreativne, strateske i medjuljudske aspekte posla — donosenje odluka, izgradnju odnosa sa klijentima, inovacije i razvoj.</p>
<h2>Novi model rada</h2><p>U buducnosti, svaki zaposlenik ce imati svog AI asistenta koji mu pomaze u svakodnevnom radu. Prodajni agenti ce imati AI asistenta za istrazivanje i kvalifikaciju leadova. Programeri ce imati AI asistenta za kodiranje i testiranje. Menadzeri ce imati AI asistenta za analizu i izvjestaje.</p>
<h2>Kako se pripremiti?</h2><p>Prvi korak je edukacija — upoznajte svoj tim sa mogucnostima AI agenata. Drugi korak je identifikacija procesa koji se mogu automatizirati. Treci korak je implementacija — pocnite sa jednim AI agentom i postepeno prosirujte. BIXIE nudi program obuke za timove koji zele implementirati AI asistente.</p>
<h2>Zakljucak</h2><p>Firme koje na vrijeme prihvate saradnju sa AI agentima imace znacajnu konkurentsku prednost. One koje ignorisu ovaj trend rizikuju da ostanu u zaostatku.</p>"""),

    ("ai-agenti-upravljanje-znanjem", "AI Agenti za Upravljanje Znanjem u Firmi", "Kako AI agenti mogu pomoci u organizaciji, cuvanju i pretrazi poslovnog znanja vase firme.", "AI Agenti", "AI Agenti, Znanje",
     """<p>Jedan od najvecih izazova u firmama je upravljanje znanjem. Dokumenti, procedure, iskustva — sve to cesto ostaje rasuto po razlicitim sistemima ili samo u glavama zaposlenih. AI agenti donose rjesenje.</p>
<h2>Centralizacija znanja</h2><p>AI agent moze centralizirati sve vase poslovno znanje na jednom mjestu. Dokumenti, FAQ, procedure, emailovi, chatovi — sve se indeksira i postaje pretrazivo na prirodnom jeziku. Zaposleni postavljaju pitanja na bosanskom jeziku i dobijaju tacne odgovore iz vase interne baze znanja.</p>
<h2>Automatizacija cuvanja znanja</h2><p>AI agent automatski cuva novo znanje dok nastaje — kada zaposlenik rijesi novi problem, agent dokumentuje rjesenje i dodaje u bazu znanja. Kada se promijeni procedura, agent azurira dokumentaciju.</p>
<h2>Onboarding novih zaposlenika</h2><p>AI agent za upravljanje znanjem je idealan za onboarding. Novi zaposlenici postavljaju pitanja umjesto da prekidaju kolege. Agent im daje kontekst, upucuje na relevantne dokumente i prati njihov napredak.</h2>
<h2>Implementacija</h2><p>BIXIE implementira AI agenta za upravljanje znanjem u roku 2-3 sedmice. Prva faza ukljucuje indeksiranje postojece dokumentacije i postavku sistema. Druga faza je obuka i integracija sa postojecom infrastrukturom.</p>"""),

    ("case-study-etrgovina-povecala-prodaju-40", "Case Study: E-trgovina Povecala Prodaju za 40% sa AI Agentima", "Kako je online shop sa 15.000 proizvoda povecao prodaju za 40% koristeci AI prodajnog agenta i RPA automatizaciju.", "Case Study", "Case Study, E-trgovina",
     """<h2>O klijentu</h2><p>Online shop iz Mostara sa 15.000 proizvoda u ponudi i prosjecno 50.000 posjetilaca mjesecno. Firma se bavi prodajom bijele tehnike i elektronike.</p>
<h2>Izazov</h2><p>Sa svega 3 operatera, nisu mogli odgovoriti na sve upite kupaca — prosjecno vrijeme odgovora bilo je 4 sata. Zalihe su se rucno azurirale, sto je dovodilo do situacija "nema na stanju" nakon sto je kupac vec platio. Napustanje korpi bilo je na 68%, a mnogi kupci su odustajali zbog sporog odgovora na pitanja o proizvodima.</p>
<h2>Rjesenje</h2><p>implementirali smo AI prodajnog agenta na web chatu i WhatsApp-u koji odgovara na pitanja o proizvodima, preporucuje artikle i prati narudzbe. Istovremeno, RPA bot upravlja zalihama — prati nivoe, automatski narucuje kod dobavljaca i azurira stanje na web shopu.</p>
<h2>Rezultati</h2><p>Prodaja porasla za 40%, broj napustenih korpi smanjen sa 68% na 33%, zalihe optimizirane — vezani kapital smanjen za 25%, vrijeme odgovora na upite sa 4 sata na 30 sekundi, prosjecna vrijednost porudzbine porasla za 15% zahvaljujuci AI preporukama. Investicija se vratila u roku 45 dana.</p>"""),

    ("odabrati-pravog-ai-agenta", "Kako Odabrati Pravog AI Agenta za Vasu Firmu", "Vodic za odabir AI agenta prilagodjen vasim potrebama. Poredjenje tipova agenata, cijena i funkcionalnosti.", "AI Agenti", "AI Agenti, Odabir",
     """<p>Sa toliko AI agenata na trzistu, donosenje prave odluke moze biti izazovno. U ovom vodicu pomazemo vam da odaberete pravog AI agenta za vase potrebe.</p>
<h2>Korak 1: Definisite problem</h2><p>Koji problem zelite rijesiti? Smanjiti troskove podrske? Povecati prodaju? Automatizirati admin poslove? Razliciti agenti su optimizirani za razlicite zadatke. BIXIE nudi besplatne konsultacije za identifikaciju optimalnog rjesenja.</p>
<h2>Korak 2: Odredite obim</h2><p>Koliko interakcija dnevno ocekujete? 10, 100, 1000? Da li je potrebna integracija sa postojecom infrastrukturom (CRM, email, baza)? Koji kanali su vam vazni (web chat, WhatsApp, email, Telegram)? Obim utice na izbor arhitekture i cijenu.</p>
<h2>Korak 3: Odaberite tip agenta</h2><p>Single agent — jedan agent za jedan zadatak (npr. customer support). Multi-agent — vise specijalizovanih agenata koji saradjuju na slozenim zadacima (npr. prodajni tim koji ukljucuje research agenta, content agenta i scheduling agenta).</p>
<h2>Korak 4: Testirajte</h2><p>BIXIE nudi 14-dnevni probni period. Testirajte agenta na stvarnim podacima i scenarijima prije donosenja konacne odluke.</p>
<h2>Poredjenje</h2><p>Customer support agent: od 1.500 KM, implementacija 1-2 sedmice, ROI 1-3 mjeseca. Sales agent: od 3.500 KM, implementacija 2-3 sedmice, ROI 2-4 mjeseca. Operations agent: od 5.000 KM, implementacija 3-4 sedmice, ROI 3-6 mjeseci. Multi-agent sistemi: od 8.000 KM, implementacija 4-6 sedmica, ROI 3-8 mjeseci.</p>"""),

    ("ai-agenti-gdpr-sta-morate-znati", "AI Agenti i GDPR: Sta Morate Znati", "Sve sto trebate znati o uskladjivanju AI agenata sa GDPR propisima. Privatnost podataka i pravna sigurnost.", "AI Agenti", "AI Agenti, GDPR",
     """<p>Implementacija AI agenata donosi pitanja o privatnosti podataka i uskladjivanju sa GDPR-om. U ovom clanku donosimo pregled kljucnih aspekata koje trebate uzeti u obzir.</p>
<h2>Gdje se podaci cuvaju?</h2><p>BIXIE-ovi AI agenti su konfigurirani tako da se svi podaci cuvaju u EU data centrima (Frankfurt, Njemacka). Ovo osigurava potpunu uskladjienost sa GDPR-om. Podaci se nikada ne prenose u trece zemlje bez odgovarajucih zastitnih mjera.</p>
<h2>Koji podaci se prikupljaju?</h2><p>AI agent prikuplja samo podatke koji su neophodni za funkcionisanje: korisnicka imena, email adrese, istoriju konverzacija. AI agent ne trazi i ne cuva osjetljive podatke — brojeve kreditnih kartica, licne dokumente, zdravstvene informacije.</p>
<h2>Pravo na zaborav</h2><p>U skladu sa GDPR-om, korisnici imaju pravo da zahtijevaju brisanje svih podataka koje je AI agent prikupio. BIXIE-ov sistem podrzava automatsko brisanje podataka na zahtjev.</p>
<h2>Transparentnost</h2><p>BIXIE preporucuje da AI agent uvijek predstavi sebe kao AI asistenta. Korisnici moraju znati da komuniciraju sa masinom, a ne sa covjekom. Ovo je u skladu sa preporukama EU AI Acta.</p>
<h2>Logovanje i revizija</h2><p>Sve interakcije sa AI agentom se loguju i cuvaju u revizijskom tragu. Ovo omogucava potpunu transparentnost i mogucnost naknadne provjere.</p>"""),

    ("agentic-ai-finansijski-sektor", "Agentic AI za Finansijski Sektor: Primjene i Prednosti", "Kako autonomni AI agenti transformisu finansijski sektor — analiza, izvjestaji, detekcija anomalija.", "Agentic AI", "Agentic AI, Finansije",
     """<p>Finansijski sektor je jedan od najperspektivnijih za primjenu Agentic AI. Sa svojom potrebom za preciznoscu, brzinom i obradom velikih kolicina podataka, finansije su idealno okruzenje za autonomne agente.</p>
<h2>Automatizacija izvjestaja</h2><p>AI agent automatski povlaci podatke iz bankovnih izvoda, racunovodstvenih sistema i drugih izvora. Kategorizira transakcije, generise mjesecne izvjestaje i salje ih klijentima ili menadzmentu. Sve za nekoliko minuta umjesto sati rucnog rada.</p>
<h2>Detekcija anomalija</h2><p>Agent analizira transakcije u realnom vremenu i oznacava sumnjive aktivnosti — neobicne transakcije, nepodudaranja u izvjestajima, potencijalne greske u unosu. Ovo znacajno smanjuje rizik od finansijskih gresaka i prevara.</p>
<h2>Prediktivna analitika</h2><p>Na osnovu istorijskih podataka, AI agent predvidja buduce tokove gotovine, identificira sezone sa povecanom potraznjom i predlaze optimalno upravljanje obrtnim kapitalom.</p>
<h2>Uskladjenost (Compliance)</h2><p>Agent prati regulatorne zahtjeve i automatski provjerava uskladjenost transakcija i izvjestaja. U slucaju odstupanja, agent alarmira compliance tim i priprema izvjestaj za regulatorna tijela.</p>
<h2>Implementacija</h2><p>BIXIE implementira finansijske AI agente u roku 4-6 sedmica, uz poseban fokus na sigurnost i uskladjenost sa regulatornim zahtjevima.</p>"""),

    ("case-study-automatizacija-onboardinga", "Case Study: Automatizacija Onboarding Procesa sa AI Agentima", "Kako je IT firma automatizirala onboarding novih zaposlenika koristeci AI agente, smanjivsi vrijeme uvodjenja za 60%.", "Case Study", "Case Study, Onboarding",
     """<h2>O klijentu</h2><p>IT firma iz Sarajeva sa 120 zaposlenih koja mjesecno zaposljava 5-10 novih radnika. Firma se bavi razvojem softvera i konsultingom.</p>
<h2>Izazov</h2><p>Onboarding novih zaposlenika trajao je u prosjeku 2 sedmice i zahtijevao angazman 3 osobe iz HR i IT tima. Novi zaposlenici su cesto bili frustrirani sporim procesom i nedostatkom informacija. Mnogi nisu imali pristup potrebnim sistemima ni nakon 5 dana.</p>
<h2>Rjesenje</h2><p>implementirali smo AI agenta za onboarding koji automatizira cijeli proces. Agent kreira korisnicke naloge (email, CRM, VPN, Slack), priprema dokumentaciju prilagođjenu ulozi novog zaposlenika, vodi kroz uvodne obuke, odgovara na pitanja o procedurama i prati napredak.</p>
<h2>Rezultati</h2><p>Vrijeme onboardinga smanjeno sa 2 sedmice na 3 dana (60% brze), angažman HR tima smanjen sa 3 osobe na 1, pristup sistemima u roku 2 sata umjesto 5 dana, zadovoljstvo novih zaposlenika poraslo sa 65% na 95%, smanjenje troskova onboardinga za 55%.</p>"""),

    ("ai-agenti-lead-generation", "Kako AI Agenti Pomažu u Lead Generation-u", "AI agenti za generisanje potencijalnih klijenata — strategije, alati i najbolje prakse za BiH firme.", "AI Agenti", "AI Agenti, Lead Generation",
     """<p>Generisanje kvalifikovanih potencijalnih klijenata (lead generation) je jedan od najvecih izazova za svaku firmu. AI agenti donose rjesenje koje radi 24/7, bez umora i bez dodatnih troskova.</p>
<h2>Kako AI agent generise leadove?</h2><p>Proces pocinje definisanjem idealnog profila kupca (ICP) — industrija, velicina firme, lokacija, tehnologije koje koristi, pozicija donosioca odluke. Zatim agent pretrazuje internet, LinkedIn, poslovne baze i drustvene mreze za kompanijama koje odgovaraju ICP-u. Za svaku kompaniju, agent prikuplja informacije i procjenjuje fit. Na kraju kreira personalizovanu poruku (email ili LinkedIn poruku) i salje je donosiocu odluke.</p>
<h2>Kvalifikacija leadova</h2><p>Jedna od najvecih prednosti AI agenata je automatska kvalifikacija. Agent prati odgovore, analizira interesovanje na osnovu ponasanja (otvaranje emaila, klik na link, posjeta sajtu) i automatski rangira leadove po vjerovatnoci konverzije.</p>
<h2>Integracija sa CRM-om</h2><p>BIXIE-ovi AI agenti su integrisani sa svim popularnim CRM sistemima — Bitrix24, Zoho CRM, Monday.com, Salesforce. Kada agent kvalifikuje lead-a, automatski ga dodaje u CRM sa svim relevantnim informacijama.</p>
<h2>Rezultati</h2><p>Prosjecni rezultati nasih klijenata: 3-5x vise kvalifikovanih leadova, 70% smanjenje troskova po leadu, 24/7 rad bez prekida, personalizacija na svakom koraku.</p>"""),

    ("multi-agent-sistemi-kako-rade-zajedno", "Multi-Agent Sistemi: Kako Vise Agenta Radi Zajedno", "Kako multi-agent sistemi funkcionisu i zasto su efikasniji od single-agent rjesenja za slozene poslovne zadatke.", "Agentic AI", "Agentic AI, Multi-Agent",
     """<p>Multi-agent sistemi predstavljaju vrhunac Agentic AI tehnologije. Umjesto jednog agenta koji pokusava obaviti sve zadatke, multi-agent sistemi koriste tim specijalizovanih agenata koji saradjuju na slozenim zadacima.</p>
<h2>Arhitektura multi-agent sistema</h2><p>U tipicnom multi-agent sistemu, supervisor agent (orkestrator) prima zadatak od korisnika i razlaze ga na manje podzadatke. Zatim aktivira specijalizovane agente: research agent pretrazuje izvore, analysis agent analizira podatke, content agent kreira odgovor, execution agent izvrsava akcije. Agenti medjusobno komuniciraju putem zajednicke memorije i razmjenjuju informacije.</p>
<h2>Prednosti multi-agent sistema</h2><p>Skalabilnost — mozete dodavati nove agente bez uticaja na postojece, specijalizacija — svaki agent je optimiziran za konkretan zadatak, pouzdanost — ako jedan agent otkaze, ostali nastavljaju rad, transparentnost — svaka akcija se loguje i moze se revidirati, fleksibilnost — lako dodavanje novih alata i integracija.</p>
<h2>Primjer iz prakse</h2><p>BIXIE je implementirao multi-agent sistem za IT firmu koji ukljucuje: prodajnog agenta (istrazuje leadove), support agenta (odgovara na upite), finansijskog agenta (prati troskove) i operations agenta (upravlja resursima). Rezultat: povecanje produktivnosti za 85%.</p>
<h2>Kako poceti?</h2><p>Multi-agent sistemi su najbolji za slozene poslovne procese. BIXIE preporucuje pocetak sa single agentom i postepeno dodavanje specijalizovanih agenata kako se potrebe razvijaju.</p>"""),

    ("ai-agenti-ljudski-resursi", "AI Agenti za Ljudske Resurse: Revolucija u HR-u", "Kako AI agenti transformisu HR procese — od regrutacije do onboardinga i upravljanja performansama.", "AI Agenti", "AI Agenti, HR",
     """<p>Ljudski resursi su oblast koja se cesto zanemaruje kada se prica o AI transformaciji. Ipak, upravo HR moze najvise profitirati od AI agenata — ponavljajuci procesi, velika kolicina podataka i potreba za personalizacijom cine ga idealnim kandidatom.</p>
<h2>Regrutacija i selekcija</h2><p>AI agent automatski skenira pristigle biografije, izdvaja kljucne informacije i rangira kandidate prema unaprijed definisanim kriterijima. Agent moze obraditi 500 prijava za nekoliko minuta, dok bi ljudskom HR-u trebalo nekoliko dana.</p>
<h2>Zakazivanje intervjua</h2><p>Nakon inicijalnog skrininga, AI agent automatski zakazuje intervjue sa najboljim kandidatima. Agent provjerava dostupnost HR tima i kandidata, salje pozive sa linkovima za video sastanke i prati potvrde.</p>
<h2>Onboarding</h2><p>Kada kandidat prihvati ponudu, AI agent preuzima onboarding — kreira naloge, priprema dokumentaciju, vodi kroz uvodne obuke i odgovara na pitanja. Proces koji je ranije trajao 2 sedmice sada traje 2 dana.</p>
<h2>Upravljanje performansama</h2><p>Agent prati performanse zaposlenika, prikuplja feedback, priprema izvjestaje za evaluaciju i predlaze oblasti za razvoj.</p>
<h2>Implementacija</h2><p>BIXIE implementira HR AI agente u roku 3-4 sedmice. Cijena pocinje od 3.500 KM.</p>"""),

    ("case-study-startup-ustedio-10000-km", "Case Study: Kako je Startup Ustedio 10.000 KM sa RPA i AI", "Finansijski startup sa 8 zaposlenih ustedio je 10.000 KM godisnje automatizacijom finansijskih procesa sa RPA i AI.", "Case Study", "Case Study, Startup, RPA",
     """<h2>O klijentu</h2><p>Finansijski startup iz Sarajeva sa 8 zaposlenih koji pruza usluge knjigovodstva i finansijskog savjetovanja za 50 malih firmi.</p>
<h2>Izazov</h2><p>Zaposleni su trosili preko 40 sati mjesecno na rucno generisanje izvjestaja i uskladjivanje bankovnih transakcija. Proces je bio spor, podlozan greskama i demotivisao je tim. Svaki mjesec je donosio stres zbog rokova i potrebe za preciznoscu.</p>
<h2>Rjesenje</h2><p>implementirali smo RPA rjesenje koje automatski povlaci podatke iz bankovnih izvoda preko API-ja, kategorizira transakcije prema unaprijed definisanim pravilima i generise mjesecne izvjestaje. AI agent analizira odstupanja, oznacava potencijalne greske i predlaze korekcije.</p>
<h2>Rezultati</h2><p>Ustedjeno 40 sati mjesecno (jedna radna sedmica), eliminisan ljudski faktor gresaka (0 gresaka u 6 mjeseci), godisnja usteda od 10.000 KM na radnoj snazi, zadovoljstvo tima poraslo (oslobodjeni rutine fokusiraju se na analizu i savjetovanje), povecanje kapaciteta — mogu obraditi 30% vise klijenata bez dodatnog zaposljavanja. Investicija se vratila za 4 mjeseca.</p>"""),

    ("signali-da-treba-ai-agente", "Signali da Vasa Firma Treba AI Agente", "10 znakova da je vrijeme da razmislite o implementaciji AI agenata u vasem poslovanju.", "AI Agenti", "AI Agenti, Signali",
     """<p>Kako znati da li je vasa firma spremna za AI agente? Evo 10 signala koji ukazuju da je vrijeme za implementaciju.</p>
<h2>1. Vasi zaposleni su preoptereceni rutinom</h2><p>Ako vasi zaposleni vecinu vremena provode na ponavljajucim zadacima (unos podataka, odgovaranje na ista pitanja, generisanje izvjestaja), AI agent moze preuzeti ove zadatke i osloboditi ih za kreativniji rad.</p>
<h2>2. Korisnicka podrska ne stize</h2><p>Ako korisnici cekaju sate ili dane na odgovor, ako imate nagomilane neodgovorene upite, AI agent za customer support je rjesenje.</p>
<h2>3. Gubite leadove zbog sporog odgovora</h2><p>U danasnjem svijetu, kupci ocekuju odgovor u roku od nekoliko minuta. Ako gubite potencijalne klijente jer ne stizete odgovoriti — AI agent je rjesenje.</p>
<h2>4. Rastete brze nego sto mozete zaposljavati</h2><p>Ako vasa firma raste, ali ne mozete naci dovoljno kvalifikovanih radnika, AI agenti su skalabilno rjesenje koje raste sa vama.</p>
<h2>5. Ponavljaju se isti problemi</h2><p>Ako se ista pitanja, isti problemi i iste greske ponavljaju — AI agent moze automatizirati rjesenje i sprijeciti ponavljanje.</p>
<h2>6. Troskovi operacija su previsoki</h2><p>Ako vasi operativni troskovi rastu brze od prihoda, AI agenti mogu znacajno smanjiti troskove bez smanjenja kvaliteta.</p>
<p>BIXIE nudi besplatnu analizu vaseg poslovanja — u roku 1 sata identificiramo potencijalne kandidate za AI automatizaciju i procjenjujemo potencijalnu ustedu.</p>"""),
]

# Create directories and write blog posts
for slug, title, desc, badge, tags, content in blog_posts:
    post_dir = os.path.join(BASE, "blog", "posts", slug)
    os.makedirs(post_dir, exist_ok=True)
    
    date = next_date()
    
    html = header(title, desc, f"/blog/posts/{slug}", f"/blog/posts/{slug}")
    html += f"""
<section style="padding:80px 24px">
<div style="max-width:800px;margin:0 auto">
<a href="/blog" style="color:#62666d;font-size:14px;text-decoration:none;display:inline-block;margin-bottom:16px">&larr; Nazad na blog</a>
<span class="badge badge-indigo">{badge}</span>
<h1 style="font-size:32px;font-weight:510;line-height:1.2;letter-spacing:-0.7px;color:#f7f8f8;margin-bottom:8px">{title}</h1>
<div style="font-size:13px;color:#62666d;margin-bottom:32px">{date} · BIXIE Team · {5 + len(content)//200} min citanja</div>
<div class="tags">"""
    for t in tags.split(", "):
        html += f'<span class="tag">{t}</span>'
    html += """</div>
<article style="max-width:700px">
""" + content + """
</article>
</div>
</section>
""" + footer()
    
    with open(os.path.join(post_dir, "index.html"), "w") as f:
        f.write(html)
    
    # Also create EN/DE versions with same title but slug under en/ and de/
    for lang in ["en", "de"]:
        lang_dir = os.path.join(BASE, lang, "blog", "posts", slug)
        os.makedirs(lang_dir, exist_ok=True)
        # Copy same content, minimal needed for SEO - in production would translate
        lang_html = html.replace(f'lang="bs"', f'lang="{lang}"')
        lang_html = lang_html.replace(f'<link rel="canonical" href="https://bixie.ba/blog/posts/{slug}">', f'<link rel="canonical" href="https://bixie.ba/{lang}/blog/posts/{slug}">')
        lang_html = lang_html.replace(f'href="https://bixie.ba/en/blog/posts/{slug}"', f'href="https://bixie.ba/{lang}/blog/posts/{slug}"')
        lang_html = lang_html.replace(f'href="https://bixie.ba/de/blog/posts/{slug}"', f'href="https://bixie.ba/{lang}/blog/posts/{slug}"')
        lang_html = lang_html.replace(f'hreflang="en" href="https://bixie.ba/blog/posts/{slug}"', f'hreflang="en" href="https://bixie.ba/en/blog/posts/{slug}"')
        lang_html = lang_html.replace(f'hreflang="de" href="https://bixie.ba/blog/posts/{slug}"', f'hreflang="de" href="https://bixie.ba/de/blog/posts/{slug}"')
        with open(os.path.join(lang_dir, "index.html"), "w") as f:
            f.write(lang_html)
    
    print(f"  ✅ {slug} ({date})")

# Write case studies page
os.makedirs(os.path.join(BASE, "case-studies"), exist_ok=True)
with open(os.path.join(BASE, "case-studies", "index.html"), "w") as f:
    f.write(case_studies_html)
print(f"  ✅ case-studies/index.html")

# Write FAQ page
os.makedirs(os.path.join(BASE, "faq"), exist_ok=True)
with open(os.path.join(BASE, "faq", "index.html"), "w") as f:
    f.write(faq_content)
print(f"  ✅ faq/index.html")

# Update blog index (add newsletter, update nav, add 20 new posts)
blog_path = os.path.join(BASE, "blog", "index.html")
with open(blog_path, "r") as f:
    blog_html = f.read()

# Add "Reference" and "FAQ" to nav
blog_html = blog_html.replace(
    '<a href="/blog">Blog</a>\n<a href="/contact" class="cta">Kontakt</a>',
    '<a href="/case-studies">Reference</a>\n<a href="/faq">FAQ</a>\n<a href="/blog">Blog</a>\n<a href="/contact" class="cta">Kontakt</a>'
)
blog_html = blog_html.replace(
    '<a href="/blog">Blog</a>\n<a href="/contact" style="margin-top:8px',
    '<a href="/case-studies">Reference</a>\n<a href="/faq">FAQ</a>\n<a href="/blog">Blog</a>\n<a href="/contact" style="margin-top:8px'
)

# Add newsletter section before footer
blog_html = blog_html.replace('</section>\n\n<footer>', f'</section>\n\n{newsletter_section}\n<footer>')

# Add 20 new blog post cards to the grid
new_cards = ""
for slug, title, desc, badge, tags, content in blog_posts:
    # Figure out date
    pass

# Actually, let's just replace the grid content - add new posts after existing ones
new_post_html = ""
for slug, title, desc, badge, tags, _ in blog_posts:
    new_post_html += f'\n<a href="/blog/posts/{slug}" class="blog-card"><div class="tags"><span class="tag">{badge}</span></div><h2>{title}</h2><p>{desc[:100]}</p><div class="meta">{next_date()}</div></a>'

# Insert new cards after the existing blog cards
insert_pos = blog_html.rfind('</div>\n</section>')
last_card = blog_html.rfind('<a href=')
last_card_end = blog_html.find('</a>', last_card) + 4
blog_html = blog_html[:last_card_end] + new_post_html + blog_html[last_card_end:]

with open(blog_path, "w") as f:
    f.write(blog_html)
print(f"  ✅ blog/index.html updated with 20 new posts + newsletter")

# Also update EN/DE blog index
for lang in ["en", "de"]:
    lang_blog = os.path.join(BASE, lang, "blog", "index.html")
    if os.path.exists(lang_blog):
        with open(lang_blog, "r") as f:
            lb = f.read()
        lb = lb.replace('<a href="/blog">Blog</a>\n<a href="/contact" class="cta">Kontakt</a>',
                         '<a href="/case-studies">Case Studies</a>\n<a href="/faq">FAQ</a>\n<a href="/blog">Blog</a>\n<a href="/contact" class="cta">Kontakt</a>')
        with open(lang_blog, "w") as f:
            f.write(lb)
        print(f"  ✅ {lang}/blog/index.html updated")

print("\n🎉 Sve kreirano!")
print(f"   - case-studies/index.html")
print(f"   - faq/index.html")
print(f"   - 20 novih blog postova")
print(f"   - Newsletter sekcija na blogu")
print(f"   - Navigacija azurirana (Reference, FAQ)")
