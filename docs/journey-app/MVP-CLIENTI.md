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

## 6. I documenti di progetto, ora letti

L'8 settembre i tre documenti sono stati caricati e letti. Da lì vengono i nomi dei sistemi, le cadenze e le milestone che prima erano dedotti.

| Cliente | Documento | Cosa ha cambiato |
|---|---|---|
| **Viglietti** | *Il piano dei 3 mesi* — Ambulatorio Veterinario Viglietti, Carloforte | I tre sistemi hanno il nome vero: i quattro agenti dei numeri, la comunicazione che si scrive da sola, l'agenda che smette di soffocare. Sei incontri con titolo, output e KPI. Le tre cose di agosto. La decisione Strada A / Strada B |
| **Di Blasi** | *Il piano di volo · Tappa 0* — per Enrico e Maria | Cinque milestone verificabili, non quattro cantieri dedotti. Sei tappe una ogni dieci giorni, calendario fino a gennaio. Le tre mosse dei 30 giorni con le loro scadenze |
| **Zanini** | *Percorso AI 2026* — metodo FARO | Non una cadenza generica: quattro fasi FARO, maturità L2 misurata a 46/100, investimento Fase 1 di 4.500 € in tre pagamenti |

### Cosa ho dovuto correggere

- **Viglietti non è in provincia di Olbia: la clinica è a Carloforte**, ed è un *Ambulatorio*, non una Clinica.
- **Antonio ha già firmato Snoots.** L'app lo dava come «da attivare»: il gestionale su cui poggia il percorso è deciso.
- **I «20 messaggi» non sono 80–90.** Il piano parla di venti richieste di appuntamento in coda; gli 80–90 messaggi quotidiani vengono dalla call e sono un'altra cosa.
- **La landing emergenze non è nel piano di Viglietti.** È nata in Tappa 1: va decisa, non data per acquisita.
- **La struttura di Di Blasi non era un'ipotesi:** sei tappe una ogni dieci giorni, confermate. Il chip «da confermare» è stato tolto.
- **Il Master di Milano è il 25 settembre**, confermato dal piano di Di Blasi. Il dubbio sulle date è chiuso.
- **Le cinque milestone di Di Blasi** hanno sostituito i quattro cantieri che avevo ricavato dalle call, che ne coglievano solo una parte.

---

## 7. I punti non verificati segnalati in dashboard

1. **Viglietti** — la decisione Strada A / Strada B, che il piano definisce «la scelta più importante dei prossimi tre mesi» da prendere area per area alla call 1, non risulta presa nelle note del 7 settembre.
2. **Viglietti** — la landing emergenze è fuori piano: entra nel percorso o resta un fuori programma?
3. **Viglietti** — due inviti «Spiegare percorso Mentorship» accettati il 13 e 15 luglio, senza evento né registrazione superstite.
4. **Di Blasi** — la Tappa 2 del 5 ottobre è accettata via email ma non esiste sul calendario BVB, mentre il piano chiede le sei date sul calendario condiviso.
5. **Di Blasi** — gli acquisti extra-UE non passano dal cassetto fiscale: vanno quantificati prima di fidarsi del dato di costo.
6. **Di Blasi** — l'agente che legge le performance delle persone richiede una dichiarazione sottoscritta prima dell'attivazione.
7. **Zanini** — l'incontro del 2 settembre è a calendario ma non ha registrazione.
8. **Zanini** — la governance dei dati sanitari, indicata nella proposta come attenzione da formalizzare fin dall'inizio, non risulta formalizzata.

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
