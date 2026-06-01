#!/usr/bin/env python3
"""Expand all blog posts to 1500+ words by adding sections before the CTA card."""
import os, re, glob

BASE = '/root/bixie-site/blog/posts'

EXPANSIONS = {
    'ai-licence-obrazovne-ustanove': '''
            <h2>Poređenje cijena: Akademske vs Komercijalne licence</h2>
            <p>Jedna od najčešćih nedoumica prilikom nabavke AI licenci jeste razlika između akademskih i komercijalnih cijena. Donosimo jasno poređenje:</p>
            <ul>
                <li><strong>ChatGPT:</strong> Edu 28 KM/mj vs Team 70 KM/mj — ušteda od 60%</li>
                <li><strong>Google Gemini:</strong> Education 18 KM/mj vs Business 60 KM/mj — ušteda od 70%</li>
                <li><strong>Claude:</strong> Edu 48 KM/mj vs Team 80 KM/mj — ušteda od 40%</li>
            </ul>
            <p>Ove uštede su moguće zahvaljujući posebnim ugovorima koje provajderi sklapaju sa obrazovnim institucijama. Važno je napomenuti da akademske cijene zahtijevaju validaciju .edu.ba domene i namijenjene su isključivo za nastavne i istraživačke svrhe.</p>

            <h2>Kako odabrati pravi AI alat za vašu ustanovu?</h2>
            <p>Izbor pravog AI alata zavisi od nekoliko faktora. Ako vaša ustanova već koristi Google Workspace, Gemini Education je logičan izbor zbog integracije. Ukoliko su vam potrebne napredne mogućnosti pisanja i analize teksta, ChatGPT Edu ili Claude Edu su bolji izbor. Za grafički dizajn i vizuelne materijale, Canva for Education je besplatan i moćan alat. Preporučujemo da zakažete besplatne konsultacije sa našim timom kako bismo vam pomogli da odaberete optimalnu kombinaciju alata.</p>

            <h2>Tehnička implementacija: Šta očekivati?</h2>
            <p>Proces implementacije AI licenci na fakultetu obično uključuje: provjeru sistemskih zahtjeva, kreiranje administratorskih naloga, konfiguraciju SSO (Single Sign-On) integracije, mapiranje korisničkih grupa (studenti, nastavnici, administrativno osoblje), postavku sigurnosnih politika i DLP pravila, te obuku ključnih korisnika. Cijeli proces traje od 3 do 10 radnih dana, zavisno od veličine ustanove.</p>

            <h2>Zaključak</h2>
            <p>AI licence za obrazovne ustanove u BiH su dostupne po akademskim cijenama koje su 40-70% niže od komercijalnih. Ključno je nabavljati licence preko ovlaštenog partnera koji razumije lokalne propise, može izdati domaću fakturu i pružiti podršku na BHS jeziku. BIXIE nudi kompletnu uslugu — od savjetovanja i nabavke do implementacije i obuke. Kontaktirajte nas za besplatne konsultacije i prilagođenu ponudu za vašu ustanovu.</p>
''',
    'bitrix24-vs-ai-crm': '''
            <h2>Šta donosi AI-powered CRM?</h2>
            <p>Moderni AI CRM sistemi koriste mašinsko učenje za automatizaciju prodajnih procesa, predviđanje ponašanja kupaca i personalizaciju komunikacije. Za razliku od tradicionalnih CRM sistema koji zahtijevaju ručni unos i analizu, AI CRM automatski boduje leadove, predlaže sljedeće korake u prodajnom procesu i generiše personalizovane email poruke.</p>
            <p>Ključne prednosti AI CRM sistema uključuju: automatsko bodovanje leadova na osnovu istorijskih podataka, predviđanje vjerovatnoće zatvaranja posla, personalizovane preporuke proizvoda, automatsko bilježenje poziva i sastanaka, te analizu sentimenta u komunikaciji sa klijentima.</p>

            <h2>Kada ostati na Bitrix24?</h2>
            <p>Bitrix24 je i dalje odličan izbor za firme koje trebaju: integrisanu telefoniju sa CRM-om, HR module, upravljanje projektima i zadacima, on-premise hosting opciju, fiksne mjesečne troškove bez iznenađenja. Ako vaša firma već koristi Bitrix24 i zadovoljni ste funkcionalnostima, migracija na AI CRM možda nije neophodna.</p>

            <h2>Kada preći na AI CRM?</h2>
            <p>AI CRM sistemi su bolji izbor kada vam treba: napredna AI analitika i predviđanje prodaje, automatsko bodovanje i prioritizacija leadova, personalizovana komunikacija u realnom vremenu, integracija sa AI chatbotovima, manuelno manje unosa podataka. Firme koje obrađuju više od 100 leadova mjesečno obično imaju značajne koristi od AI CRM funkcionalnosti.</p>

            <h2>Hibridni pristup: Najbolje od oba svijeta</h2>
            <p>Najčešće rješenje koje preporučujemo klijentima je hibridni pristup: zadržite Bitrix24 za interne procese, HR i projektni menadžment, a dodajte AI CRM sloj za naprednu prodajnu analitiku i automatizaciju. BIXIE implementira ovakva hibridna rješenja koristeći Bitrix24 API i integraciju sa AI alatima poput ChatGPT-a i Google Gemini.</p>

            <h2>Zaključak</h2>
            <p>Izbor između Bitrix24 i AI CRM sistema ne mora biti isključiv. Najbolje rješenje za vašu firmu zavisi od specifičnih potreba, budžeta i tehničkih zahtjeva. BIXIE nudi besplatne konsultacije gdje analiziramo vaše poslovne procese i predlažemo optimalno rješenje.</p>
''',
    'rpa-automatizacija-procesa': '''
            <h2>Šta je RPA i kako se razlikuje od AI?</h2>
            <p>RPA (Robotic Process Automation) je tehnologija koja koristi softverske botove za automatizaciju ponavljajućih, pravilima vođenih zadataka. Za razliku od AI sistema koji donose odluke na osnovu učenja, RPA botovi slijede unaprijed definirane instrukcije. Kombinacija RPA i AI (Intelligent Automation) donosi najbolje rezultate — RPA za izvršenje, AI za donošenje odluka.</p>

            <h2>Koji procesi se najčešće automatiziraju?</h2>
            <p>Na osnovu našeg iskustva sa klijentima u BiH, najčešći procesi za automatizaciju su: unos podataka iz emaila u CRM, generisanje faktura i izvještaja, obrada bankovnih izvoda, sinhronizacija podataka između ERP i CRM sistema, automatsko slanje email notifikacija i podsjetnika, verifikacija i validacija dokumenata, te izvoz podataka za regulatorne izvještaje.</p>

            <h2>Uštede i ROI: Šta pokazuju naši projekti?</h2>
            <p>Na osnovu realizovanih projekata, klijenti bilježe sljedeće rezultate: smanjenje vremena obrade fakture sa 15 minuta na 2 minute (87% uštede), smanjenje grešaka pri unosu podataka sa 8% na 0.5%, povrat investicije (ROI) u roku 4-6 mjeseci, oslobađanje 30-70% radnog vremena administrativnog osoblja.</p>

            <h2>Kako izgleda proces implementacije RPA rješenja?</h2>
            <p>Implementacija RPA rješenja kod BIXIE prolazi kroz četiri faze: (1) Analiza i mapiranje procesa gdje identifikujemo zadatke pogodne za automatizaciju i mjerimo potencijalne uštede. (2) Proof of Concept gdje razvijamo prototip za jedan specifičan proces u roku 1-2 sedmice. (3) Implementacija gdje postavljamo RPA botove u produkcijsko okruženje i povezujemo sa postojećim sistemima. (4) Monitoring i optimizacija gdje pratimo performanse i kontinuirano poboljšavamo automatizaciju.</p>

            <h2>Zaključak</h2>
            <p>RPA i AI automatizacija nisu više luksuz već nužnost za firme koje žele ostati konkurentne. BIXIE nudi kompletnu uslugu — od analize procesa do implementacije i održavanja. Zakažite besplatni audit i saznajte koji procesi u vašoj firmi mogu biti automatizovani.</p>
'''
}

for slug, extra_content in EXPANSIONS.items():
    filepath = f'{BASE}/{slug}/index.html'
    if not os.path.exists(filepath):
        print(f'SKIP: {slug} — not found')
        continue
    
    with open(filepath) as f:
        html = f.read()
    
    # Find the CTA card (the div with "Zatražite ponudu" button) or similar
    # Insert new sections before it
    cta_markers = [
        'Zatražite ponudu za Vašu ustanovu',
        'Zatražite ponudu',
        'class="card mt-8"',
        'Zakažite besplatni audit',
    ]
    
    insert_pos = -1
    for marker in cta_markers:
        pos = html.find(marker)
        if pos > 0:
            # Find the beginning of the containing section/article
            before = html.rfind('<div', 0, pos)
            insert_pos = before if before > 0 else html.rfind('<', 0, pos)
            break
    
    if insert_pos < 0:
        print(f'  {slug}: Could not find CTA marker, appending before </article>')
        insert_pos = html.rfind('</article>')
        if insert_pos < 0:
            insert_pos = html.rfind('</section>')
    
    if insert_pos < 0:
        print(f'  {slug}: ERROR — no insertion point found')
        continue
    
    # Insert content
    new_html = html[:insert_pos] + extra_content + html[insert_pos:]
    
    with open(filepath, 'w') as f:
        f.write(new_html)
    
    # Count words
    words = len(re.sub(r'<[^>]+>', '', new_html).split())
    print(f'  {slug}: {words} words')

print('\\nBlog expansion complete!')
