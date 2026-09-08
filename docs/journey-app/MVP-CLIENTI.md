# MVP su clienti reali — Viglietti, Di Blasi, Zanini

Prototipo: `mockup/journey-app/index.html` · Versione 3, costruita sui dati già presenti nei sistemi BVB all'8 settembre 2026. Nessun dato inventato, nessun campo compilato a mano.

---

## 1. Le fonti

| Fonte | Cosa ha fornito |
|---|---|
| **Google Calendar** | 20 eventi con i tre clienti, link Meet, stato degli inviti |
| **Gmail** | proposte, piani, fatture, report inviati, testimonianze, e i report che gli agenti di un cliente producono da soli |
| **Fireflies** | **17 call trascritte** — 211 minuti Viglietti, 328 Di Blasi, 281 Zanini — con sintesi e action item con marca temporale |
| **Google Drive** | note automatiche delle call, cruscotto di controllo di gestione |

Ogni scheda in dashboard porta la sua fonte in chiaro: `Fireflies 07/09`, `Gmail 07/08`, `Calendar`.

---

## 2. I tre percorsi, tre forme diverse

| | **Antonio Viglietti** | **Enrico Di Blasi** | **Stefania Zanini** |
|---|---|---|---|
| Clinica | Clinica Veterinaria Viglietti | Clinica Veterinaria Di Blasi | Ambulatorio Veterinario Zanini, Bertiolo |
| Relazione dal | 22 giugno 2026 | 31 marzo 2026 | 22 giugno 2026 |
| Forma del percorso | Mentorship AI, **6 tappe** | Mentorship AI, **6 tappe** | Mentorship AI, **affiancamento ogni 15 giorni** |
| Stato | 1 tappa svolta, 5 da fissare | 1 tappa svolta, Tappa 2 da riconfermare | 7 incontri, 2° mese fatturato |
| Call registrate | 4 | 6 | 7 |
| Dove è arrivato | primo prototipo (landing emergenze) in test | Snoots collegato, agenti fermi sui dati | **agenti in produzione**, report ogni giorno |
| Cosa lo blocca | migrazione da Aruba, tappe non prenotate | migrazione dati, account non ancora suoi | i bilanci dal commercialista, nessun incontro fissato |

**La regola di conteggio è la stessa per tutti: la mappa misura il pacchetto venduto, non la frequentazione.** Per Viglietti e Di Blasi le tappe sono i sei incontri prenotabili con il link Calendly; le call precedenti stanno sotto «Prima del percorso» e non entrano nel conteggio. Per Zanini non esistono tappe numerate: il percorso è a cadenza quindicinale e la mappa mostra la sequenza reale degli incontri.

---

## 3. Cosa fa emergere l'app, cliente per cliente

### Antonio Viglietti — il percorso non è a calendario
Il link Calendly è partito il 7 agosto e nessuno dei cinque slot è stato scelto. Con dieci giorni minimi tra un incontro e l'altro, novembre si copre solo se la Tappa 2 entra entro fine settembre. Intanto il sistema emergenze costruito in Tappa 1 ha già risposto a tre richieste vere l'8 settembre: il prototipo funziona mentre il percorso è fermo.

### Enrico Di Blasi — il cliente più avanti sui numeri, il più indietro sull'infrastruttura
Ha un anno di controllo di gestione alle spalle: fotografia del business a giugno, report del primo semestre a luglio, cruscotto 2026 corretto ad agosto. Ha pagato settembre in anticipo il 10 agosto. Ma gli account non sono ancora suoi — n8n da riconnettere, Brevo e GitHub da aprire — e la migrazione dei dati, attesa entro il 10 settembre, è la condizione perché il primo agente KPI parta. Restano lì anche i 6.600 € di discrepanze sugli acquisti di farmaci emersi il 20 luglio.

**Nota sulla Tappa 2:** Enrico ha accettato via email un invito per lunedì 5 ottobre 11:00–13:00, ma **quell'evento non esiste sul calendario di lavoro BVB**. In dashboard è marcato *da riconfermare*, non dato per prenotato.

### Stefania Zanini — il caso in produzione
È l'unica in cui il sistema lavora già da solo: sei tipi di report escono ogni giorno e ogni settimana e arrivano a lei e a BVB — KPI economici, mix servizi e clienti, performance settimanale, performance dei collaboratori, andamento per giorno della settimana, briefing clientela su quattro giorni. Sono numeri veri: 25.776 € di fatturato nella settimana 24–30 agosto, 5.258 € e 37 clienti il 3 settembre.

Il lavoro non è più costruire ma **rendere stabile**: mail che a volte non partono, agenti da riavviare a mano, 385 voci di tariffario ancora da classificare per centro di ricavo. E due blocchi che non sono tecnici: i conti economici 2024 e 2025 chiesti al commercialista il 20 luglio e sollecitati il 4 e l'8 settembre, e **nessun prossimo incontro a calendario** — l'ultimo è del 2 settembre, la cadenza è quindicinale.

---

## 4. Le azioni: prese dalle call, non riscritte

Le azioni in dashboard sono gli action item estratti da Fireflies, con tre aggiunte:

1. **Ogni azione porta al minuto esatto** in cui è stata decisa (`app.fireflies.ai/view/<id>?t=<secondi>`). Il cliente non deve fidarsi: può risentire.
2. **Ogni azione ha un proprietario dichiarato** — cliente o BVB — e le due liste sono visibili a entrambi. Il cliente vede anche cosa sta facendo BRAVE: è ciò che rende il percorso condiviso.
3. **Lo stato è assegnato solo dove esiste una prova nei sistemi.** Un'azione è completata se c'è l'email, il documento o il report che lo dimostra: il report della Tappa 1 di Enrico è "fatto" perché la mail è partita il 7 settembre alle 14:17; l'account Brevo di Stefania è "fatto" perché i report escono da Brevo. È in ritardo se una data dichiarata è passata. Tutto il resto resta aperto.

---

## 5. Le due viste

**Lato BVB** — console con portafoglio, cose da fare oggi calcolate dai dati e prossimi appuntamenti; poi, per cliente, mappa del percorso con l'avviso di rischio, incontri con registrazione e materiali, storia di come è nato il cliente, le due liste di azioni, i materiali consegnati, le note interne e i cantieri aperti.

**Lato cliente** — la stessa sostanza senza il retro: niente note interne, niente fatture, niente altri clienti. In cima **una sola cosa da fare**, diversa per ciascuno: prenotare le tappe per Antonio, completare la migrazione dei dati per Enrico, ottenere i bilanci dal commercialista per Stefania.

**Back office** — provenienza dei dati, integrazioni per cliente con lo stato vero, regole di automazione e la lista dei punti da confermare.

---

## 6. Che cosa NON è stato letto

**Nessun documento di progetto è stato aperto.** Proposte, piani e report vivono come **allegati PDF** dentro le email, e gli allegati Gmail non sono accessibili agli strumenti collegati; su Drive non ci sono. Quello che l'app sa dei progetti viene dal **corpo delle email** e dalle **trascrizioni delle call**, non dai documenti.

Documenti citati ma mai letti:

| Cliente | Documento | Cosa se ne sa |
|---|---|---|
| Viglietti | `proposta-Viglietti.pdf` (22/06) | esiste, allegato all'email del punto T0 |
| Viglietti | `piano-mentorship-viglietti_2.pdf` (07/08) | esiste, insieme al link Calendly e alla Fattura 96/2026 |
| Di Blasi | allegato di «Il piano di volo» (07/08) | dodici pagine; a pagina 11 le tre cose che servono nei trenta giorni successivi |
| Di Blasi | proposta di controllo di gestione (31/03), proposta formativa (31/03), report H1 2026 (20/07) | esistono, con oggetto e data |
| Zanini | report T0 e proposta di mentorship | **previsti** da un action item del 22 giugno; nessuna email di consegna trovata |

Conseguenza diretta: **la struttura a sei tappe di Di Blasi è dedotta**, non letta. L'evento del 7 settembre è una prenotazione Calendly dello stesso tipo di quella di Viglietti, il cui piano parla di sei slot; da lì l'ipotesi. In dashboard la mappa porta il chip *Struttura da confermare* e la spiegazione sotto. Per Viglietti, dove il piano è citato ma non letto, vale lo stesso per i nomi dei tre sistemi.

Basta una delle due per chiudere il punto: caricare quei PDF su Drive, oppure incollarne l'indice.

---

## 7. I punti non verificati segnalati in dashboard

Sono in dashboard, marcati *Da confermare*, invece che risolti a intuito:

1. **Viglietti** — i nomi ufficiali dei tre sistemi vanno letti da `piano-mentorship-viglietti_2.pdf`: gli allegati Gmail non sono leggibili dagli strumenti collegati e il file non è su Drive.
2. **Viglietti** — due inviti «Spiegare percorso Mentorship» accettati il 13 e 15 luglio, senza evento né registrazione superstite.
3. **Di Blasi** — la Tappa 2 del 5 ottobre risulta accettata via email ma non esiste sul calendario BVB.
4. **Di Blasi** — la struttura a sei tappe è dedotta dal tipo di prenotazione Calendly, non letta dal piano.
5. **Zanini** — l'incontro del 2 settembre è a calendario ma non ha registrazione: da verificare se si è svolto.
6. **Zanini** — report T0 e proposta di mentorship risultano previsti da un action item, ma l'email di consegna non è stata trovata.

---

## 8. Cosa serve per far vivere l'MVP

Oggi il prototipo mostra una fotografia. Per farla aggiornare da sola, nell'ordine:

1. **Google Calendar** in lettura → gli incontri entrano ed escono da soli *(mezza giornata)*.
2. **Fireflies** in lettura → registrazione, durata e action item si agganciano all'incontro giusto *(un giorno)*.
3. **Claude** → dalla trascrizione nasce la bozza di report con le azioni già attribuite; la pubblicazione resta un gesto umano *(un giorno)*.
4. **Gmail** in lettura sui messaggi con il cliente → materiali e report automatici compaiono nell'archivio senza caricarli *(mezza giornata)*.
5. **Accesso del cliente** — link via email, sessione ricordata, visibilità limitata al proprio profilo *(un giorno)*.

Cinque giorni di lavoro. Le richieste di appuntamento e di informazioni sono l'unica parte nuova da costruire: tutto il resto esiste già, sparso.

---

## 9. Perché è riproducibile

Il passaggio da uno a tre clienti non ha richiesto una seconda applicazione né un secondo impianto: sono state aggiunte due righe di dati, lette dalle stesse quattro fonti. Per il quarto cliente serve:

- il suo indirizzo email, che collega calendario, posta e registrazioni;
- la forma del percorso — a tappe prenotabili o a cadenza;
- il documento di piano nel suo archivio.

Le tre dashboard non sono state compilate. Sono state **lette**.
