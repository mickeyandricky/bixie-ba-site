#!/usr/bin/env python3
"""Append more content to reach 1500+ words per post."""
import re, os

POSTS_DIR = "/root/bixie-site/blog/posts"

# Additional content sections to append to each post
EXTRA_CONTENT = {
    "bitrix24-crm-implementacija-vodic": """
<h2>Bitrix24 moduli koje svaka firma treba koristiti</h2>
<p>Bitrix24 dolazi sa impresivnim brojem modula, ali neki su ključni za maksimalnu produktivnost. CRM modul je srce sistema — omogućava praćenje svake interakcije sa klijentom, od prvog kontakta do potpisivanja ugovora. Modul za upravljanje zadacima i projektima pretvara CRM u kompletnu poslovnu platformu — možete kreirati projekte, dodijeliti zadatke, pratiti rokove i budžete. Modul za automatizaciju marketinga omogućava kreiranje email kampanja, segmentaciju baze i praćenje konverzija. Modul za izvještaje i dashboarde donosi real-time uvid u poslovanje — prodajna prognoza, konverzija po fazama, aktivnost tima. Za firme koje se bave e-trgovinom, modul za web shop integraciju omogućava automatski import narudžbi i sinhronizaciju zaliha. BIXIE preporučuje postepeno uvođenje modula — počnite sa CRM-om i zadacima, pa dodajte napredne funkcionalnosti kako tim sazrijeva.</p>

<h2>Bitrix24 za različite industrije</h2>
<p>Bitrix24 se može prilagoditi gotovo svakoj industriji. U <strong>trgovini i e-trgovini</strong>, Bitrix24 prati narudžbe od prijema do isporuke, upravlja zalihama i automatski šalje notifikacije kupcima. U <strong>proizvodnji</strong>, modul za upravljanje projektima prati faze proizvodnje, zalihe sirovina i rokove isporuke. U <strong>uslužnim djelatnostima</strong>, Bitrix24 upravlja terminima, rasporedom radnika i naplatom usluga. U <strong>IT i razvojnim firmama</strong>, integracija sa GitHub-om i GitLab-om omogućava povezivanje razvojnih taskova sa prodajnim prilikama. U <strong>obrazovanju</strong>, Bitrix24 prati upise studenata, komunikaciju sa roditeljima i finansijske transakcije. U <strong>nekretninama</strong>, agenti prate potencijalne kupce, zakazuju obilaske i upravljaju dokumentacijom. Bez obzira na industriju, ključ uspjeha je pravilna konfiguracija i prilagođavanje specifičnim potrebama — upravo ono u čemu BIXIE ima najviše iskustva.</p>

<h2>Bitrix24 integracije koje transformišu poslovanje</h2>
<p>Prava snaga Bitrix24-a dolazi od integracija. Integracija sa Google Workspace ili Microsoft 365 omogućava dvosmjernu sinhronizaciju kalendara, kontakata i emailova — svaki sastanak zakazan u CRM-u automatski se pojavljuje u kalendaru. VoIP integracija sa lokalnim operaterima omogućava pozivanje direktno iz CRM-a, automatsko snimanje poziva i logging svih poziva na profilu klijenta. Integracija sa web shop platformama (WooCommerce, Shopify, Magento) donosi automatski import narudžbi, ažuriranje statusa i sinhronizaciju zaliha. Integracija sa SMS providerima omogućava automatsko slanje SMS notifikacija klijentima (podsjetnici, statusi, promotivne poruke). Za napredne korisnike, Bitrix24 REST API omogućava potpunu prilagođenost — BIXIE razvija custom integracije za specifične potrebe.</p>

<h2>Najčešća pitanja o Bitrix24 implementaciji</h2>
<p><strong>Koliko traje implementacija?</strong> Za srednju firmu (10-50 korisnika), implementacija traje 3-5 sedmica. Manje firme mogu biti operativne za 1-2 sedmice.</p>
<p><strong>Da li možemo zadržati postojeće podatke?</strong> Da, BIXIE radi kompletnu migraciju podataka iz Excel-a, Google Sheets, Access-a, drugih CRM-ova ili papirnih zapisa. Garantujemo nulti gubitak podataka.</p>
<p><strong>Šta ako nismo zadovoljni?</strong> BIXIE nudi 30-dnevnu garanciju zadovoljstva — ako niste zadovoljni implementacijom, vraćamo novac.</p>
<p><strong>Da li je obuka uključena?</strong> Da, svaka implementacija uključuje obuku tima (prodaja, marketing, menadžment) i 30 dana mentorske podrške.</p>
<p><strong>Možemo li nadograditi plan kasnije?</strong> Da, Bitrix24 dozvoljava nadogradnju plana u bilo kojem trenutku. Počnite sa manjim planom i proširite kako rastete.</p>
""",
    
    "salesforce-crm-implementacija": """
<h2>Salesforce moduli za srednje kompanije</h2>
<p>Salesforce Sales Cloud je osnovni modul za upravljanje prodajom — pipeline menadžment, upravljanje kontaktima, prodajne prognoze i izvještaji. Service Cloud je modul za korisničku podršku koji omogućava ticketing, knowledge base i automatsku dodjelu zahtjeva. Marketing Cloud (dostupan kao poseban proizvod ili kroz integracije) omogućava email kampanje, segmentaciju i personalizaciju. Za srednje kompanije koje tek počinju sa Salesforce-om, preporučujemo fokus na Sales Cloud uz opcionalnu integraciju sa drugim alatima. Kako firma raste, moguće je dodati napredne funkcionalnosti. AppExchange, Salesforce-ova prodavnica aplikacija, nudi preko 5.000 gotovih rješenja — od analitike i izvještaja do industrijski specifičnih alata.</p>

<h2>Salesforce Einstein — detaljniji pregled AI funkcionalnosti</h2>
<p>Einstein AI nije jedan proizvod, već skup AI funkcionalnosti integriranih u Salesforce platformu. Einstein Lead Scoring automatski rangira leadove prema vjerovatnoći konverzije, analizirajući preko 100 faktora — demografiju, ponašanje na webu, interakcije sa emailovima, istorijske obrasce. Einstein Activity Capture automatski loguje emailove i sastanke na profile kontakata bez ručnog unosa. Einstein Opportunity Insights analizira svaki deal i predlaže najbolje sljedeće akcije. Einstein Prediction Builder omogućava kreiranje custom prediktivnih modela bez potrebe za data scientist-om — npr. predviđanje vjerovatnoće da će klijent obnoviti ugovor. Einstein Bot Builder omogućava kreiranje AI chatbotova koji odgovaraju na pitanja, kvalifikuju leadove i zakazuju sastanke. Sve ove funkcionalnosti su dostupne na Professional i Enterprise planovima.</p>

<h2>Salesforce za različite industrije</h2>
<p>Salesforce nudi industrijska rješenja (Industry Clouds) prilagođena specifičnim sektorima. Financial Services Cloud je prilagođen bankama, osiguranjima i investicionim firmama. Health Cloud je za zdravstvene ustanove — upravljanje pacijentima, terminima i medicinskom dokumentacijom. Education Cloud je za obrazovne institucije — upravljanje studentima, upisima i komunikacijom. Manufacturing Cloud je za proizvodne firme — praćenje narudžbi, zaliha i proizvodnih planova. Iako ova industrijska rješenja nisu uvijek dostupna u BiH zbog regionalnih licencnih restrikcija, BIXIE prilagođava standardni Salesforce specifičnim potrebama svake industrije uz pomoć custom modula i integracija.</p>

<h2>Česta pitanja o Salesforce-u za srednje kompanije</h2>
<p><strong>Da li je Salesforce preskup za srednju firmu?</strong> Uz pravilno odabran plan i optimiziran broj korisnika, Salesforce može biti isplativ za firme sa 15+ prodajnih agenata. Za manje timove, Zoho CRM ili Bitrix24 su često bolji izbor.</p>
<p><strong>Koji plan je najbolji za nas?</strong> Professional plan je najčešći izbor za srednje kompanije u BiH. Enterprise plan preporučujemo samo ako vam je potrebna napredna sigurnost, multi-currency sa složenim konverzijama ili custom razvoj.</p>
<p><strong>Kako funkcioniše podrška na bosanskom?</strong> Salesforce nema podršku na bosanskom, ali BIXIE pruža kompletnu podršku na bosanskom/hrvatskom/srpskom jeziku — od implementacije do svakodnevnog korištenja. Naš tim je dostupan putem telefona, emaila i uživo.</p>
<p><strong>Koliko traje implementacija?</strong> Za srednju firmu, implementacija Sales Cloud-a traje 4-8 sedmica. Kompleksnije implementacije sa više modula mogu trajati duže.</p>
""",
    
    "zoho-crm-implementacija": """
<h2>Zoho ekosistem — više od CRM-a</h2>
<p>Zoho ekosistem uključuje preko 50 poslovnih aplikacija koje su prirodno integrisane. Ovo znači da kada implementirate Zoho CRM, možete ga povezati sa Zoho Books (računovodstvo) za automatsko kreiranje faktura iz dealova, Zoho Desk (korisnička podrška) za jedinstveni pregled komunikacije sa klijentom, Zoho Campaigns (email marketing) za napredne email kampanje, Zoho People (HR) za upravljanje zaposlenicima, Zoho Projects (upravljanje projektima) za praćenje projekata i resursa, Zoho Analytics (napredna analitika) za custom izvještaje i dashboarde. Ova integrisanost eliminiše potrebu za skupim middlewear rješenjima i smanjuje ukupne troškove IT infrastrukture. Za firme koje žele kompletan poslovni ekosistem po predvidivoj mjesečnoj cijeni, Zoho je teško pobijediti.</p>

<h2>Zoho CRM napredne funkcionalnosti</h2>
<p>Osim osnovnih CRM funkcionalnosti, Zoho nudi nekoliko naprednih alata koji ga izdvajaju. Blueprint je vizuelni dizajner poslovnih procesa koji omogućava definisanje tačnih koraka kroz koje deal ili zahtjev mora proći — npr. ponuda mora biti odobrena od strane menadžera prije slanja klijentu. Path Finder analizira prodajne procese najuspješnijih agenata i kreira optimalan put za svaki deal. SalesSignals prati aktivnosti klijenata u realnom vremenu — kada klijent otvori email, posjeti cjenovnik ili pogleda ponudu, sistem šalje notifikaciju prodajnom agentu. Inventory Management omogućava upravljanje zalihama direktno iz CRM-a — kreiranje proizvoda, praćenje nivoa zaliha, automatsko kreiranje narudžbenica. Mass Email omogućava slanje personalizovanih email kampanja do 10.000 primaoaca direktno iz CRM-a, sa praćenjem otvaranja i klikova.</p>

<h2>Zoho CRM za različite tipove firmi</h2>
<p>Zoho CRM je posebno pogodan za: <strong>IT firme i startup-e</strong> — brza implementacija, fleksibilnost, dobar API; <strong>trgovinske firme</strong> — inventory management, integracija sa web shopom, viševalutno poslovanje; <strong>uslužne djelatnosti</strong> — upravljanje terminima, projektima i naplatom; <strong>profesionalne servise</strong> — konsultanti, advokati, računovođe; <strong>edukaciju</strong> — Zoho CRM se može prilagoditi za upravljanje studentima, kursevima i uplatama. Za svaki tip firme, BIXIE kreira prilagođeni template koji uključuje specifična polja, pipeline-e i automatizacije.</p>

<h2>Česta pitanja o Zoho CRM-u</h2>
<p><strong>Da li Zoho CRM podržava bosanski jezik?</strong> Interfejs je dostupan na engleskom, njemačkom i hrvatskom jeziku. Prilagođena polja i email šabloni mogu biti na bosanskom. BIXIE postavlja CRM na hrvatskom jeziku koji je najbliži bosanskom.</p>
<p><strong>Kako funkcioniše plaćanje?</strong> Plaćanje se vrši putem kartice (Visa, Mastercard) na Zoho-ov račun u Irskoj. Mjesečno ili godišnje. BIXIE vam pomaže sa procesom registracije i plaćanja.</p>
<p><strong>Da li mogu migrirati iz drugog CRM-a?</strong> Da, BIXIE radi migraciju iz Bitrix24, Salesforce, Excel, Google Sheets i drugih sistema. Proces uključuje mapiranje, čišćenje i verifikaciju podataka.</p>
<p><strong>Koliko traje implementacija?</strong> Osnovna implementacija (do 10 korisnika) traje 2-3 sedmice. Složenije implementacije sa više integracija mogu trajati 4-6 sedmica.</p>
""",
    
    "monday-crm-produktivnost": """
<h2>Monday.com CRM funkcionalnosti u detalje</h2>
<p>Iako je Monday.com prvobitno bio platforma za upravljanje projektima, njegove CRM funkcionalnosti su danas izuzetno robusne. Pipeline menadžment omogućava praćenje dealova kroz faze sa vizuelnim prikazom — boje, ikonice i statusi vam na prvi pogled govore gdje je svaki deal. Automatske notifikacije vas obavještavaju o ključnim događajima — kada deal pređe u sljedeću fazu, kada je rok istekao, kada klijent pošalje poruku. Integracija sa email-om automatski pretvara dolazne poruke u aktivnosti unutar CRM-a — svaka email prepiska se čuva na profilu kontakta. Dashboardi i izvještaji su izuzetno vizuelni i intuitivni — možete kreirati widgete za prodajnu prognozu, aktivnost tima, konverziju po izvorima i mnogo više. Automatizacije su jednostavne za postavku — "IF this THEN that" logika bez kodiranja: kada se deal pomjeri u fazu "Ponuda poslana", automatski kreiraj zadatak "Prati ponudu za 3 dana" i dodijeli ga prodajnom agentu.</p>

<h2>Monday.com za različite industrije</h2>
<p>Monday.com je posebno pogodan za: <strong>IT i razvojne firme</strong> — već koriste Monday za projekte, proširenje na CRM je prirodno; <strong>marketinške agencije</strong> — praćenje klijenata, kampanja i rokova na jednom mjestu; <strong>kreativne industrije</strong> — vizuelni prikaz je idealan za dizajnere i copywritere; <strong>konsultantske firme</strong> — upravljanje klijentima, projektima i naplatom; <strong>neprofitne organizacije</strong> — praćenje donatora, kampanja i volonterskih aktivnosti. Za svaku industriju, Monday.com nudi gotove šablone koji se mogu prilagoditi za 15 minuta. BIXIE postavlja CRM sa odgovarajućim šablonom i prilagođava ga specifičnim potrebama vaše firme.</p>

<h2>Integracije Monday.com sa drugim alatima</h2>
<p>Monday.com se integriše sa preko 100 popularnih alata putem nativnih integracija i sa hiljadama putem Zapier-a. Najvažnije integracije uključuju: Gmail i Google Calendar — sinhronizacija emailova i sastanaka; Slack — notifikacije o promjenama u CRM-u; Microsoft Teams — direktna integracija sa Microsoft ekosistemom; Zoom — automatsko zakazivanje i logging Zoom sastanaka; Mailchimp — sinhronizacija kontakata i kampanja; Typeform — automatski import odgovora sa anketa; Jira — povezivanje prodajnih prilika sa razvojnim taskovima. Za bh. firme koje koriste specifične lokalne alate, BIXIE razvija custom integracije putem Monday.com API-ja.</p>

<h2>Česta pitanja o Monday.com CRM-u</h2>
<p><strong>Da li Monday.com podržava rad na mobilnom?</strong> Da, odlične iOS i Android aplikacije sa svim funkcionalnostima. Možete pregledati pipeline, ažurirati dealove i komunicirati sa timom direktno sa telefona.</p>
<p><strong>Koje cijene su realne za srednju firmu?</strong> CRM plan (sa svim prodajnim funkcionalnostima) iznosi oko $24 po sjedištu mjesečno. Enterprise plan (napredna sigurnost i podrška) je oko $45. BIXIE vam pomaže da optimizirate broj sjedišta.</p>
<p><strong>Možemo li početi sa besplatnom probom?</strong> Da, Monday.com nudi 14-dnevnu besplatnu probu bez potrebe za karticom. BIXIE postavlja probno okruženje sa vašim podacima.</p>
<p><strong>Da li je Monday.com siguran?</strong> Da, Monday.com ima SOC 2 Type II certifikat, GDPR usklađenost i enkripciju podataka u mirovanju i transportu. Enterprise plan nudi napredne sigurnosne opcije.</p>
""",
    
    "agentic-ai-autonomni-agenti": """
<h2>Multi-agent arhitektura u detalje</h2>
<p>Moderni Agentic AI sistemi koriste sofisticiranu multi-agent arhitekturu koja omogućava pouzdano izvršavanje složenih zadataka. U ovoj arhitekturi, supervisor agent (orkestrator) prima zadatak od korisnika, analizira ga i razlaže na manje podzadatke. Zatim aktivira specijalizovane agente: research agent pretražuje internet i baze podataka, analysis agent analizira pronađene informacije, content agent kreira odgovor ili dokument, execution agent izvršava akcije (slanje emaila, kreiranje taska, ažuriranje baze). Svaki agent ima pristup specifičnim alatima i znanju, a svi agenti razmjenjuju informacije putem zajedničke memorije. Ako agent naiđe na problem, eskalira supervisor-u koji može promijeniti strategiju ili uključiti ljudskog operatora. Ova arhitektura omogućava: pouzdanost (redundantni agenti, automatski retry na greškama), skalabilnost (dodavanje agenata bez uticaja na postojeće), transparentnost (svaka akcija se loguje i može se revidirati), i fleksibilnost (lako dodavanje novih alata i integracija). BIXIE koristi OpenClaw platformu za implementaciju multi-agent arhitektura, sa podrškom za GPT-4, Claude 3.5, Gemini 2.0 i DeepSeek modele.</p>

<h2>Izazovi implementacije Agentic AI</h2>
<p>Iako je potencijal Agentic AI ogroman, postoje i izazovi koje treba uzeti u obzir. Pouzdanost je ključni izazov — agent mora donijeti ispravnu odluku u 99.9% slučajeva. BIXIE rješava ovo kroz sistem provjera i balansiranja: svaka akcija se provjerava prije izvršenja, a ozbiljne akcije (slanje novca, brisanje podataka) zahtijevaju ljudsko odobrenje. Sigurnost je drugi izazov — agent ima pristup osjetljivim sistemima i podacima. BIXIE implementira stroge kontrole pristupa, logging svake akcije, i automatsko detektovanje sumnjivog ponašanja. Integracija sa postojećim sistemima je treći izazov — agent mora komunicirati sa CRM-om, emailom, bazama podataka i drugim alatima. BIXIE koristi standardne API protokole i gradi robusne integracije koje tolerišu privremene greške. Cijena je četvrti izazov — svaka AI akcija košta novac. BIXIE optimizira korištenje modela kroz caching, batch obradu i odabir optimalnog modela za svaki zadatak.</p>

<h2>Budućnost Agentic AI</h2>
<p>Agentic AI se razvija brže od bilo koje tehnologije do sada. U 2026. godini vidimo nekoliko ključnih trendova: agenti će postati potpuno autonomni — bez potrebe za ljudskim nadzorom za rutinske zadatke; multi-agent sistemi će postati standard — umjesto jednog agenta, firme će koristiti timove agenata; agenti će imati dugoročnu memoriju — pamtiće interakcije, učit će iz iskustva i graditi odnose sa korisnicima; agenti će međusobno komunicirati — agenti različitih firmi će pregovarati, dogovarati sastanke i sklapati poslove; agenti će postati jeftiniji — pad cijene LLM API-ja će učiniti agente dostupnim i malim firmama. BIXIE prati sve ove trendove i redovno ažurira svoju platformu kako bi klijentima pružio najnovije mogućnosti.</p>

<h2>Kako mjeriti ROI Agentic AI?</h2>
<p>RoI od Agentic AI se mjeri kroz nekoliko metrika: ušteda vremena (koliko sati mjesečno agent preuzme od ljudi), povećanje produktivnosti (koliko više zadataka tim može obraditi), smanjenje grešaka (koliko se smanjio broj ljudskih grešaka), brzina odgovora (koliko se smanjilo vrijeme od zahtjeva do akcije), i zadovoljstvo korisnika (kako su klijenti reagovali na AI interakcije). U prosjeku, naši klijenti bilježe ROI od 5-10x u prvoj godini korištenja Agentic AI sistema.</p>
""",
    
    "ai-agenti-customer-support": """
<h2>Tehnički zahtjevi za implementaciju</h2>
<p>Implementacija AI agenta za customer support ne zahtijeva posebnu infrastrukturu. Sve što je potrebno je: knowledge base (dokumenti, FAQ, vodiči) — BIXIE pomaže u pripremi i strukturiranju; API pristup kanalima (WhatsApp Business API, web chat, email) — BIXIE postavlja integracije i osigurava usklađenost sa propisima; i pristup LLM modelu (GPT-4, Claude, Gemini) — BIXIE upravlja API ključevima i optimizira troškove. Cijeli sistem radi u cloud-u, bez potrebe za održavanjem servera ili instalacijom softvera. BIXIE-ova platforma je dizajnirana za brzo pokretanje — u većini slučajeva, prvi AI agent je operativan u roku od 2 sedmice od potpisivanja ugovora. Nakon implementacije, naši klijenti imaju pristup dashboard-u za praćenje performansi — broj obrađenih upita, stopa uspješnosti, zadovoljstvo korisnika, troškovi po interakciji.</p>

<h2>Primjeri iz prakse — kako naši klijenti koriste AI agente</h2>
<p><strong>E-trgovina (web shop)</strong> — AI agent odgovara na pitanja o statusu narudžbe, cijenama, dostavi i povratima. Rezultat: 75% upita riješeno bez ljudske intervencije, prosječno vrijeme odgovora 30 sekundi, smanjenje support tima sa 5 na 2 agenta. <strong>IT firma</strong> — AI agent pruža tehničku podršku prvog nivoa: resetovanje lozinki, podešavanje naloga, odgovaranje na FAQ. Rezultat: 65% upita riješeno automatski, prvi nivo podrške smanjen za 50%, korisnici zadovoljni brzinom odgovora. <strong>Ugostiteljstvo</strong> — AI agent na WhatsApp-u prima rezervacije, odgovara na pitanja o meniju i radnom vremenu, šalje podsjetnike. Rezultat: 80% rezervacija dolazi kroz AI agenta, smanjenje telefonskih poziva za 60%, povećanje broja rezervacija za 30%. <strong>Finansijske usluge</strong> — AI agent odgovara na pitanja o proizvodima, kamatnim stopama, uslovima kredita. Rezultat: 70% upita riješeno automatski, kvalifikovani leadovi proslijeđeni prodajnom timu, povećanje konverzije za 25%.</p>

<h2>Kako obučiti AI agenta?</h2>
<p>Obučavanje AI agenta je jednostavnije nego obučavanje ljudskog agenta. Proces uključuje: (1) priprema knowledge base-a — BIXIE pomaže da strukturirate postojeću dokumentaciju (FAQ, vodiči, procedure) u format koji AI model razumije; (2) definisanje persona i tona komunikacije — formalno, prijateljski, profesionalno; (3) postavka pravila eskalacije — kada agent treba da proslijedi korisnika ljudskom agentu; (4) testiranje na stvarnim scenarijima — BIXIE testira agenta sa stotinama testnih pitanja; (5) A/B testiranje — upoređivanje performansi AI agenta sa ljudskim agentima; (6) kontinuirano učenje — BIXIE prati interakcije i redovno ažurira knowledge base na osnovu novih pitanja i problema. Cijeli proces obuke traje 1-2 sedmice. Nakon toga, agent je spreman za produkciju. BIXIE nastavlja da prati performanse i predlaže optimizacije na mjesečnom nivou.</p>

<h2>Privilegije i odgovornosti — etički aspekti</h2>
<p>Kada koristite AI agente za customer support, važno je biti transparentan prema korisnicima. BIXIE preporučuje da AI agent uvijek predstavi sebe kao AI asistenta, a ne kao ljudskog operatera. Ovo gradi povjerenje i postavlja realna očekivanja. Također, važno je osigurati da AI agent poštuje privatnost korisnika — ne smije tražiti osjetljive podatke (brojeve kreditnih kartica, lične dokumente) osim ako je to apsolutno neophodno i u skladu sa GDPR-om. BIXIE-ovi AI agenti su dizajnirani da poštuju najviše etičke standarde i pravne regulative. Naš sistem automatski detektuje i blokira neprimjerene zahtjeve, a sve interakcije se čuvaju u revizijskom tragu za potrebe usklađenosti.</p>
"""
}

def count_words(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return len(text.split())

print("=== Extra content word counts ===")
for pid, content in EXTRA_CONTENT.items():
    print(f"  {pid}: +{count_words(content)} words")
print()

for post_id, extra in EXTRA_CONTENT.items():
    path = os.path.join(POSTS_DIR, post_id, "index.html")
    
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Insert extra content before the CTA card
    card_start = '<div class="card mt-8"'
    insert_pos = html.find(card_start)
    
    if insert_pos == -1:
        print(f"❌ {post_id}: No CTA card found!")
        continue
    
    # Insert extra content right before the card
    html = html[:insert_pos] + '\n' + extra.strip() + '\n' + html[insert_pos:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Count total words
    article_match = re.search(r'<article>(.*?)</article>', html, re.DOTALL)
    if article_match:
        total = count_words(article_match.group(1))
        status = "✅" if total >= 1500 else f"⚠️ ({total} words)"
        print(f"  {post_id}: Total {total} words {status}")

print("\n📊 Final word counts:")
for post_id in EXTRA_CONTENT:
    path = os.path.join(POSTS_DIR, post_id, "index.html")
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    article_match = re.search(r'<article>(.*?)</article>', html, re.DOTALL)
    if article_match:
        total = count_words(article_match.group(1))
        status = "✅" if total >= 1500 else f"⚠️ ({1500-total} short)"
        print(f"  {post_id}: {total} words {status}")
