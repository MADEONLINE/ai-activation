# Video corso n8n → Circle "Materiale d'aula" (Super Master AI)

Stato al 2026-09-03: **preparazione completata, pubblicazione in attesa del link playlist completo**.

## Cosa è stato verificato

| Elemento | Esito |
|---|---|
| Playlist YouTube `PLP9ff7QQLVdg` | ID non valido (12 caratteri; gli ID playlist sono lunghi 34). YouTube risponde con pagina di errore. Serve il link completo. |
| Canale @bravevetbusiness | Le 30 playlist del canale hanno tutte prefisso `PLfpcaQNiEmv…`, quindi la playlist richiesta non è su quel canale (o il link è troncato). |
| Circle community | id 347146, token API v1 funzionante (v2 admin non abilitato per questo token) |
| Spazio "Materiale d'aula" | id 2612944, tipo `course`, gruppo "MASTER AI" (1060136), 19 membri, **0 sezioni e 0 lezioni** |
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
