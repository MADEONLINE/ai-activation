# Video corso n8n → Circle "Materiale d'aula" (Super Master AI)

Stato al 2026-09-03: **pubblicato**.

## Cosa è stato pubblicato

Playlist sorgente: "N8N per la Clinica Veterinaria" (https://www.youtube.com/playlist?list=PLP9ff7QQLVdg), 7 video.

Spazio Circle "Materiale d'aula" (id 2612944), 5 sezioni e 12 lezioni, tutte pubblicate con commenti abilitati:

| Sezione | Lezione | id | Video |
|---|---|---|---|
| Prima di iniziare (1167426) | Guida al percorso: come usare questo video corso | 4471571 | |
| Modulo 1 · Capire n8n (1167438) | 01 · N8N: basi e utilizzo in clinica | 4471598 | -eQG7texouE (19:07) |
| | 02 · Introduzione a n8n e panoramica iniziale | 4471599 | 0Kf4UxL-vaM (5:05) |
| | 03 · L'interfaccia di n8n: panoramica | 4471600 | vRhCuxS-SCg (7:24) |
| Modulo 2 · Costruire il primo workflow (1167439) | 04 · Creare il primo workflow su n8n | 4471601 | kyx1sIf21DQ (9:35) |
| | 05 · Configurare un workflow in n8n | 4471602 | LALAend8B-Y (8:52) |
| Modulo 3 · n8n e Claude nel sistema agentico (1167440) | 06 · Connettere Claude e n8n | 4471603 | N4i3BgmdBSo (6:02) |
| | 07 · Creare un servizio veterinario con l'IA | 4471604 | uZkpLQGWow8 (18:49) |
| Materiali a supporto (1167441) | Glossario essenziale di n8n | 4471605 | |
| | Quattro automazioni dalla clinica | 4471606 | |
| | Checklist: il tuo primo workflow in clinica | 4471607 | |
| | Domande, supporto e prossimi passi | 4471608 | |

Post di annuncio nello spazio "SUPER MASTER AI": https://brave-vet-business.circle.so/c/super-master-ai/nuovo-video-corso-in-piattaforma-n8n-per-la-clinica-veterinaria

Email inviata da info@bravemedia.biz in BCC a 34 partecipanti (vedi `destinatari.md`).

## Limite noto: player video dentro la lezione

L'API v1 di Circle rimuove iframe, immagini e qualsiasi markup di embed dal corpo delle lezioni: resta solo testo e link. Ogni lezione video ha quindi in testa un link evidenziato "▶ GUARDA IL VIDEO" che apre YouTube. Per avere il player dentro Circle basta aprire ciascuna delle 7 lezioni in modifica e incollare l'URL del video nel campo "Featured media" (o nel corpo, dove l'editor lo converte in embed). In alternativa, con un token Admin API v2 abilitato, l'operazione si può fare via API con `rich_text_body`.

Il contenuto HTML di tutte le lezioni è rigenerabile con `build_lessons.py` (scratch) ed è riportato in `lezioni.json`.

## Cosa è stato verificato

| Elemento | Esito |
|---|---|
| Playlist YouTube `PLP9ff7QQLVdg` | Valida: "N8N per la Clinica Veterinaria", 7 video (i singoli video non sono leggibili da server senza login, quindi le descrizioni YouTube non sono state usate). |
| Circle community | id 347146, token API v1 funzionante (v2 admin non abilitato per questo token) |
| Spazio "Materiale d'aula" | id 2612944, tipo `course`, gruppo "MASTER AI" (1060136); prima della pubblicazione: 19 membri, 0 sezioni, 0 lezioni |
| Spazio "Spazio di confronto" | id 2612943, tipo `chat`, stesso gruppo: qui va il messaggio al gruppo |
| Spazio "SUPER MASTER AI" | id 2643395, tipo `basic` (feed post) |
| API v1 course | `GET/POST /api/v1/course_sections` e `/api/v1/course_lessons` rispondono 200 |
| Ponte HTTP | workflow n8n `pKVCQZvzRDfib8yh` "CLAUDE TEMP — HTTP Proxy (Circle/YouTube)" (da eliminare a fine lavoro) |

## Piano di pubblicazione (da eseguire appena arriva il link)

1. Leggere la playlist: titolo, ordine, id video, durata, descrizione di ogni video.
2. Creare in "Materiale d'aula" la sezione **"n8n — Video corso"** (`POST /api/v1/course_sections`, `name`, `space_id=2612944`).
3. Per ogni video creare una lezione (`POST /api/v1/course_lessons`, `section_id`, `name`, `status=published`, `body_html`) con:
   - titolo numerato ("01 · …") coerente con l'ordine della playlist;
   - embed YouTube in testa alla lezione;
   - blocco "In questa lezione" (3-5 punti), "Perché ti serve" (collegamento al sistema agentico), "Prima di proseguire" (azione pratica di 5 minuti), durata e link diretto al video;
   - commenti abilitati per raccogliere domande.
4. Pubblicare il messaggio in "Spazio di confronto" (testo in `post-spazio-di-confronto.md`).
5. Inviare l'email ai partecipanti (testo in `email-partecipanti.html`, destinatari in `destinatari.md`) in BCC da info@bravemedia.biz oppure come campagna Brevo.

## Template lezione (body_html)

```html
<div style="font-family:Arial,sans-serif;color:#374151;line-height:1.6">
  <p><iframe width="100%" height="420" src="https://www.youtube.com/embed/{VIDEO_ID}" title="{TITOLO}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>
  <p><strong>Durata:</strong> {DURATA} · <a href="https://www.youtube.com/watch?v={VIDEO_ID}">Apri su YouTube</a></p>
  <h3>In questa lezione</h3>
  <ul>{PUNTI}</ul>
  <h3>Perché ti serve nel sistema agentico</h3>
  <p>{COLLEGAMENTO}</p>
  <h3>Prima di proseguire (5 minuti)</h3>
  <p>{AZIONE}</p>
</div>
```

## Nota sugli accessi

Lo spazio "Materiale d'aula" ha 19 membri, tutti aggiunti tra il 1° e il 26 maggio 2026 (edizione 1). I partecipanti dell'edizione 2 (iscritti da luglio) risultano creati come membri della community (es. Federico Andrei, creato il 27/08/2026, invito non ancora accettato) ma vanno verificati uno per uno nello spazio prima dell'invio dell'email, altrimenti il link porta a una pagina non accessibile.
