# MVP su cliente reale — Antonio Viglietti

Prototipo: `mockup/journey-app/index.html` · Versione 2, costruita sui dati già presenti nei sistemi BVB (nessun dato inventato).

---

## 1. Da dove viene ogni cosa

Tutto ciò che compare nelle due dashboard è stato letto dai sistemi in uso l'8 settembre 2026.

| Fonte | Cosa ha fornito |
|---|---|
| **Google Calendar** | 5 incontri con Antonio (28/05, 22/06, 06/08, 07/09, 08/09), link Meet, stato degli inviti |
| **Gmail** | proposta e report T0 (22/06), piano dei tre mesi + link Calendly + Fattura 96/2026 (07/08), report e presentazione della Tappa 1 (08/09), testimonianza Super Master (20/06), 3 email generate dal sistema emergenze (08/09) |
| **Fireflies** | 4 call trascritte — 28/05 (22′), 22/06 (28′), 06/08 (30′), 07/09 (132′) — con sintesi e action item con marca temporale |
| **Google Drive** | note automatiche delle tre call, archiviate nella cartella dei meeting |

### Le quattro call registrate con Antonio

| Data | Incontro | Durata | Registrazione |
|---|---|---|---|
| 28/05/2026 | Super Master AI — istruzioni abilitanti (call di gruppo, 7 partecipanti) | 22 min | `01KSPH3AGGMX7DWPCHAGC9TE37` |
| 22/06/2026 | Profilazione — il punto T0 | 28 min | `01KVQ223R6587R8MGCDBRC7BQV` |
| 06/08/2026 | Intro al Mentorship AI (con Marta Dessena) | 30 min | `01KZ6KPKEVY7K3CC5CSPNS7NMY` |
| 07/09/2026 | **Tappa 1** del percorso — ecosistema, strumenti, primo prototipo | 132 min | `01M1VS9MDFZNP98DDA6W4FVJMN` |

### Tappa 1 non è la prima call

Distinzione che vale la pena tenere ferma, perché la prima versione della dashboard la confondeva:

- **Prima call registrata con Antonio: 28 maggio 2026.** È una sessione di gruppo del Super Master AI in cui Antonio interviene e dichiara le proprie motivazioni.
- **Tappa 1 del percorso: 7 settembre 2026.** Che sia la prima delle sei tappe è confermato da due elementi indipendenti: l'evento a calendario è una prenotazione Calendly del tipo *Consulenza AI - Mentor AI*, cioè lo stesso link dei sei slot inviato il 7 agosto; e il documento inviato il giorno dopo si chiama `Report-Tappa-1-Mentorship-AI-Viglietti.pdf`.

**Il conteggio delle tappe resta stretto:** contano solo i sei incontri del pacchetto, quelli prenotabili con il link Calendly. Le tre call precedenti — 102 minuti complessivi — stanno sotto «Prima del percorso» come contesto della relazione e non entrano nella mappa di avanzamento. È la regola giusta anche per i clienti successivi: la mappa misura il pacchetto venduto, non la frequentazione.

### Un buco nei dati: luglio

Il 13 e il 15 luglio Antonio accetta due inviti intitolati «Antonio Viglietti Spiegare percorso Mentorship». **Nessun evento corrispondente sopravvive a calendario e non esiste alcuna registrazione.** L'ipotesi più semplice è che siano stati riprogrammati e confluiti nell'intro del 6 agosto — l'evento del 6 agosto viene infatti creato il 31 luglio. Resta un'ipotesi: in dashboard la voce è marcata **Da confermare**, ed è l'unico modo onesto di trattarla.

---

## 2. Il percorso reale di Antonio

**Prima del percorso.** Super Master AI a Milano (giugno) → testimonianza → call di profilazione del 22 giugno → email «Il tuo punto T0» con `proposta-Viglietti.pdf` → call intro del 6 agosto con Marta → email del 7 agosto con `piano-mentorship-viglietti_2.pdf`, il link Calendly e la prima fattura.

**Il percorso.** Mentorship AI: **6 incontri tra settembre e novembre 2026**, con la regola dichiarata nel piano — *almeno dieci giorni tra un incontro e l'altro*.

**Stato all'8 settembre:** Tappa 1 svolta il 7 settembre. **Le altre cinque non sono ancora a calendario**, benché il link Calendly sia partito il 7 agosto. È il primo fatto che l'app fa emergere da sola, e la ragione per cui la scadenza di novembre è a rischio.

---

## 3. I tre cantieri aperti

Ricavati dalle call, non dichiarati a mano. I nomi ufficiali vanno letti dal piano (vedi §6).

| Cantiere | Stato | Cosa lo blocca |
|---|---|---|
| **Sistema emergenze — Carloforte** | in test | credenziali SMTP e pubblicazione (Netlify o GitHub). Tre risposte già generate l'8 settembre: Gatto, Gatta europea, Cane meticcio |
| **Sistema dati ed economia** | fermo | la migrazione della fatturazione elettronica da Aruba, «il primo domino», doveva chiudersi ad agosto. Avvio con dati reali previsto a gennaio |
| **Comunicazione e marketing** | da avviare | serve l'account Brevo; è la fase con Marta Dessena |

---

## 4. Le azioni, prese dalle call

Le 20 azioni in dashboard sono gli action item estratti da Fireflies, con due aggiunte rispetto a un semplice elenco:

1. **Ogni azione porta al minuto esatto** in cui è stata decisa (`app.fireflies.ai/view/<id>?t=<secondi>`). Antonio non deve fidarsi: può risentire.
2. **Ogni azione ha un proprietario dichiarato** — Antonio o BVB — e le due liste sono visibili a entrambi. Il cliente vede anche cosa sta facendo BRAVE: è ciò che rende il percorso condiviso e non una lista di compiti.

Lo stato è assegnato solo dove esiste una prova nei sistemi:

- **completate** le tre azioni BVB con l'email corrispondente (report T0 del 22/06, link Calendly del 07/08, report Tappa 1 dell'08/09);
- **in corso** le azioni sul sistema emergenze, perché oggi il flusso ha prodotto tre risposte reali;
- **in ritardo** la migrazione da Aruba (attesa da agosto) e la prenotazione delle cinque tappe (link consegnato il 7 agosto);
- tutte le altre restano **aperte**. Nessuna è stata dichiarata conclusa per verosimiglianza.

---

## 5. Le due viste

**Lato BVB** — anagrafica e percorso, quattro numeri di sintesi presi dai dati (1 di 6 tappe svolte, 5 da fissare, 132′ di Tappa 1, 3 richieste già gestite dal sistema emergenze), mappa delle sei tappe con l'avviso sul rischio novembre, prossimo appuntamento, incontri con registrazione e materiali, storia di come è nato il cliente, le due liste di azioni, note interne, i tre cantieri.

**Lato cliente** — la stessa sostanza senza il retro: niente note interne, niente fattura, niente altri clienti. In cima una sola cosa da fare («prenota le cinque tappe», con il link Calendly reale), poi cosa è successo in Tappa 1, l'elenco delle quattro call con il link per rivederle, i sistemi in costruzione, le sue azioni con il rimando al minuto, i materiali ricevuti e i due pulsanti di comunicazione.

**Back office** — l'elenco delle integrazioni con lo stato vero: attive Calendar, Calendly, Meet, Fireflies, Gmail e Claude; in test n8n; da attivare Brevo, GitHub e Snoots, tutte e tre in attesa di un'azione di Antonio.

---

## 6. L'unico punto non verificato

Il piano dei tre mesi è un PDF allegato alla mail del 7 agosto (`piano-mentorship-viglietti_2.pdf`) e non è leggibile dagli strumenti collegati: gli allegati Gmail non sono accessibili e il file non è su Drive. Di conseguenza **i nomi ufficiali dei tre sistemi e il contenuto previsto di ogni tappa** sono ricostruiti dalle call, non copiati dal piano.

Per chiudere il punto basta una delle due: caricare quel PDF su Drive, oppure incollarne l'indice. A quel momento le sei tappe prendono il titolo giusto e la mappa di avanzamento diventa esatta.

---

## 7. Cosa serve per far vivere l'MVP

Oggi il prototipo mostra i dati reali fotografati all'8 settembre. Per farli aggiornare da soli, nell'ordine:

1. **Google Calendar** in lettura → gli incontri entrano ed escono da soli (mezza giornata di lavoro).
2. **Fireflies** in lettura → registrazione, durata e action item si agganciano all'incontro giusto (un giorno).
3. **Claude** → dalla trascrizione nasce la bozza di report con le azioni già attribuite; la pubblicazione resta un gesto umano (un giorno).
4. **Gmail** in lettura sui messaggi con il cliente → i materiali inviati compaiono nell'archivio senza caricarli a mano (mezza giornata).
5. **Accesso di Antonio** — link via email, sessione ricordata, visibilità limitata al suo profilo (un giorno).

Cinque giorni di lavoro per avere l'MVP vivo su un cliente. Le richieste di appuntamento e informazioni (i due pulsanti) sono l'unica parte nuova da costruire: tutto il resto esiste già, sparso.

---

## 8. Perché è riproducibile

Il secondo cliente non richiede una seconda applicazione. Serve:

- il suo indirizzo email, che collega calendario, posta e registrazioni;
- il template di percorso adatto (Mentorship AI a 6 tappe, o un altro);
- il documento di piano nel suo archivio.

Il resto — incontri, report, azioni, materiali — si popola da solo dalle stesse quattro fonti. È esattamente ciò che è successo qui: la dashboard di Antonio non è stata compilata, è stata **letta**.
