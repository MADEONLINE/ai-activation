# BraveVET Journey — Specifiche funzionali e architettura

**Web app per la gestione del percorso cliente di BraveVETBusiness**
Versione 1.0 — documento di proposta · Autore: BraveVETBusiness / Massimo Serreri

---

## 0. Come leggere questo documento

| Sezione | A chi serve |
|---|---|
| §1–§4 | Visione, ruoli, modello del percorso — leggere sempre |
| §5 | Mock-up delle schermate (wireframe testuale) |
| §6 | Flussi operativi passo-passo |
| §7–§10 | Architettura, dati, integrazioni, back office — per chi implementa |
| §11 | Sicurezza e privacy |
| §12–§16 | Riproducibilità, rilascio, KPI, rischi |

Il prototipo cliccabile che accompagna questo documento è in `mockup/journey-app/index.html`.

---

## 1. Sintesi

Oggi il percorso di un cliente BraveVETBusiness vive in strumenti separati: il calendario tiene gli appuntamenti, Google Meet ospita gli incontri, Fireflies registra e trascrive, Claude produce il report, la posta e WhatsApp reggono le richieste. Funziona, ma il cliente non vede mai il **quadro d'insieme** e BVB deve ricomporlo a mano ogni volta.

**BraveVET Journey** è una web app che diventa il luogo unico dove quel percorso è visibile e condiviso:

- **Una sola console per BVB.** Si scrive il nome del cliente, si entra nella sua dashboard. Nessun menu da esplorare.
- **Una dashboard per ogni cliente**, con accesso limitato al proprio profilo: dove sono arrivato, cosa abbiamo deciso, quando ci rivediamo, cosa devo fare.
- **Gli strumenti attuali restano gli stessi.** Calendario, Meet, Fireflies e Claude non vengono sostituiti: vengono collegati, e il loro risultato atterra automaticamente nella dashboard del cliente giusto.
- **Il percorso è un modello riproducibile.** Ogni nuovo cliente parte da un template di fasi già pronto: creare il suo spazio richiede meno di due minuti.

Clienti pilota: **Ericko Di Blasi**, **Antonio Viglietti**, a seguire **Marta**.

---

## 2. Obiettivi e non-obiettivi

### Obiettivi di prodotto

1. **Rendere puntuale l'esperienza.** Il cliente sa sempre a che punto è, senza chiederlo.
2. **Azzerare il lavoro di ricomposizione.** Registrazione → trascrizione → report → dashboard senza passaggi manuali.
3. **Un solo canale di progetto.** Richieste di appuntamento e richieste di informazioni non si perdono più tra mail e messaggi.
4. **Riproducibilità.** Lo stesso impianto vale per il secondo cliente come per il ventesimo.
5. **Semplicità.** Il cliente veterinario deve capire la sua dashboard in trenta secondi, senza istruzioni.

### Non-obiettivi (V1)

- Non è un CRM commerciale (non gestisce pipeline di vendita, preventivi, fatturazione).
- Non è un gestionale di clinica: non tocca dati sanitari o pazienti.
- Non sostituisce il calendario: lo rispecchia.
- Non ospita chat in tempo reale: la comunicazione è asincrona e legata al progetto.

---

## 3. Attori, ruoli e permessi

| Ruolo | Chi | Cosa può fare |
|---|---|---|
| **Owner BVB** | Massimo Serreri | Tutto: crea clienti, gestisce template di percorso, integrazioni, pubblica report, vede ogni dashboard |
| **Consulente BVB** | Collaboratori futuri | Come Owner ma solo sui clienti assegnati; non gestisce integrazioni e fatturazione |
| **Cliente** | Ericko, Antonio, Marta… | Vede **solo il proprio** profilo: mappa di avanzamento, incontri, report pubblicati, azioni assegnate, richieste. Può scrivere richieste e caricare documenti |
| **Ospite del cliente** (opzionale) | Socio o collaboratore della clinica | Sola lettura sul percorso del cliente che lo ha invitato, senza documenti riservati |
| **Sistema** | Automazioni | Scrive incontri, trascrizioni e bozze di report; non pubblica mai nulla al cliente senza approvazione umana |

**Regola d'oro dei permessi:** ogni richiesta al server è filtrata per `client_id`; un utente cliente non può ottenere dati di un altro cliente nemmeno cambiando l'indirizzo nel browser. Nessun contenuto generato automaticamente diventa visibile al cliente prima dell'approvazione di BVB.

---

## 4. Il percorso cliente: il modello riproducibile

Il percorso BVB viene formalizzato in un **template di fasi**. È il cuore della riproducibilità: si definisce una volta, si applica a ogni cliente, si adatta caso per caso.

### Template "Percorso Consulenza BVB" (default, 6 fasi)

| # | Fase | Cosa succede | Uscita (cosa la chiude) |
|---|---|---|---|
| 1 | **Primo contatto** | Richiesta arrivata, qualificazione, invio scheda conoscitiva | Scheda compilata + call fissata |
| 2 | **Discovery** | Call di scoperta: obiettivi, stato attuale, strumenti | Report di discovery pubblicato |
| 3 | **AI Activation** | Le 2 ore one-to-one: configurazione strumenti | Report di attivazione + accessi consegnati |
| 4 | **Attivazione operativa** | Il cliente usa gli strumenti sul lavoro reale; check a 15 giorni | Check completato, blocchi risolti |
| 5 | **Consulenze ricorrenti** | Incontri periodici su obiettivi concordati | Ogni incontro chiude con report e azioni |
| 6 | **Presidio** | Revisione trimestrale, misura dei risultati, rinnovo | Revisione firmata |

Ogni fase contiene: **incontri previsti**, **deliverable attesi**, **azioni per il cliente**, **azioni per BVB**. Una fase è `da fare` / `in corso` / `completata` / `in attesa del cliente`.

Il template è modificabile dal back office e versionato: cambiarlo non altera i percorsi già avviati, se non su richiesta esplicita.

---

## 5. Mock-up (wireframe testuale)

Sei schermate. Sono quelle rese cliccabili nel prototipo.

### 5.1 Console BVB — Home

```
┌──────────────────────────────────────────────────────────────────────────┐
│ BVB Journey        [ Cerca cliente… "eri" ]                    MS ▾      │
├──────────────────────────────────────────────────────────────────────────┤
│  ┌─ Suggerimenti ────────────────────┐                                   │
│  │ ● Ericko Di Blasi   Fase 4 · 65%  │  ← invio / clic → entra           │
│  │ ● Antonio Viglietti Fase 3 · 45%  │                                   │
│  │ ● Marta …           Fase 1 · 10%  │                                   │
│  └───────────────────────────────────┘                                   │
│                                                                          │
│  DA FARE OGGI                          PORTAFOGLIO (3 clienti attivi)    │
│  ┌────────────────────────────────┐    ┌────────────────────────────┐    │
│  │ 2 report da approvare          │    │ Ericko   ▓▓▓▓▓▓░░░  65%    │    │
│  │ 1 richiesta appuntamento       │    │ Antonio  ▓▓▓▓░░░░░  45%    │    │
│  │ 1 richiesta informazioni       │    │ Marta    ▓░░░░░░░░  10%    │    │
│  │ 1 azione cliente in ritardo    │    └────────────────────────────┘    │
│  └────────────────────────────────┘                                      │
│                                                                          │
│  PROSSIMI INCONTRI            │  ATTIVITÀ RECENTE                        │
│  Gio 11/09 15:00 Ericko       │  Fireflies ha trascritto "Antonio #3"    │
│  Lun 15/09 10:30 Antonio      │  Claude ha generato la bozza report      │
└──────────────────────────────────────────────────────────────────────────┘
```

La barra di ricerca è l'unico vero punto di ingresso: si digita il nome, si preme invio, si è dentro.

### 5.2 Console BVB — Dashboard del cliente

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ← Clienti │ ERICKO DI BLASI · Clinica … · dal 12/03/2026     [Vedi come  │
│                                                               il cliente]│
├──────────────────────────────────────────────────────────────────────────┤
│ MAPPA DI AVANZAMENTO                                                     │
│ ①Contatto ─ ②Discovery ─ ③Activation ─ ④Attivazione ─ ⑤Consulenze ─ ⑥Presidio │
│   ✔          ✔            ✔             ●in corso      ○           ○     │
├───────────────────────────────┬──────────────────────────────────────────┤
│ INCONTRI E REPORT             │ RICHIESTE DEL CLIENTE            (2)     │
│                               │ ┌──────────────────────────────────────┐ │
│ ● 04/09 · Check attivazione   │ │ 📅 "Possiamo anticipare a giovedì?"  │ │
│   Meet · 58' · Fireflies ✔    │ │    → [Proponi 3 slot] [Rispondi]     │ │
│   Report: BOZZA DA APPROVARE  │ │ ❓ "Come collego Fireflies a Meet?"  │ │
│   [Apri bozza] [Approva]      │ │    → [Rispondi] [Allega guida]       │ │
│                               │ └──────────────────────────────────────┘ │
│ ● 21/08 · Consulenza #2       │                                          │
│   Report pubblicato · 3 azioni│ AZIONI ASSEGNATE                         │
│                               │ ☑ Attivare account Claude    fatto       │
│ ● 12/08 · AI Activation       │ ☐ Portare dati fatturato     in ritardo  │
│   Report pubblicato           │ ☐ Test protocollo triage     entro 12/09 │
│                               │                                          │
│ [+ Registra incontro]         │ NOTE INTERNE (non visibili al cliente)   │
└───────────────────────────────┴──────────────────────────────────────────┘
```

### 5.3 Dashboard cliente (vista del cliente)

Stessa sostanza, meno superficie: niente note interne, niente bozze, niente altri clienti.

```
┌──────────────────────────────────────────────────────────────────────────┐
│ Il mio percorso con BRAVE Vet Business               Ericko Di Blasi ▾   │
├──────────────────────────────────────────────────────────────────────────┤
│ Sei nella fase 4 di 6 — Attivazione operativa                            │
│ ①──✔──②──✔──③──✔──④ ●in corso ──⑤──○──⑥──○                              │
│                                                                          │
│ ┌── PROSSIMO INCONTRO ─────────────┐ ┌── LE MIE AZIONI ────────────────┐ │
│ │ Giovedì 11 settembre · 15:00     │ │ ☑ Attivare account Claude       │ │
│ │ Check attivazione · 60'          │ │ ☐ Portare dati fatturato ⚠      │ │
│ │ [Entra su Meet] [Chiedi di       │ │ ☐ Test protocollo triage        │ │
│ │  spostare]                       │ │   entro il 12/09                │ │
│ └──────────────────────────────────┘ └─────────────────────────────────┘ │
│                                                                          │
│ I MIEI REPORT                          COMUNICAZIONI DI PROGETTO         │
│ 04/09 Check attivazione   [Leggi]      [ 📅 Chiedi un appuntamento ]     │
│ 21/08 Consulenza #2       [Leggi]      [ ❓ Fai una domanda        ]     │
│ 12/08 AI Activation       [Leggi]      Ultima risposta: ieri, 18:20      │
└──────────────────────────────────────────────────────────────────────────┘
```

### 5.4 Report di incontro (vista lettura)

```
REPORT — Check attivazione · 4 settembre 2026 · 58 minuti
Partecipanti: Massimo Serreri, Ericko Di Blasi
─────────────────────────────────────────────────────────
IN SINTESI            tre righe, quello che conta
DECISIONI PRESE       elenco puntato
AZIONI                chi · cosa · entro quando
TEMI APERTI           cosa vediamo la prossima volta
─────────────────────────────────────────────────────────
Fonti: trascrizione Fireflies · registrazione (30 gg)
[Scarica PDF]  [Chiedi un chiarimento su questo report]
```

### 5.5 Richiesta di appuntamento (vista cliente)

Tre campi, non uno di più: **motivo** (menu), **quando preferisci** (mattina / pomeriggio / indifferente + settimana), **nota libera**. Alla conferma il cliente vede lo stato: `inviata → in valutazione → slot proposti → confermata`.

### 5.6 Back office

```
BACK OFFICE
 ├── Clienti           anagrafiche, stato, consulente assegnato, inviti
 ├── Template percorso fasi, deliverable, azioni tipo, durate attese
 ├── Modelli di report struttura e prompt usati da Claude
 ├── Integrazioni      Calendario ✔ · Meet ✔ · Fireflies ✔ · Claude ✔
 │                     stato connessione, ultimo evento, log errori
 ├── Automazioni       regole: "incontro finito → trascrivi → bozza report"
 ├── Utenti e ruoli    chi vede cosa
 └── Privacy           conservazione registrazioni, consensi, esportazioni
```

---

## 6. Flussi utente

### 6.1 Onboarding di un nuovo cliente (BVB, ~2 minuti)

1. Console BVB → **Nuovo cliente** → nome, clinica, email, telefono.
2. Si sceglie il **template di percorso** (default: Percorso Consulenza BVB).
3. Il sistema crea lo spazio cliente: fasi, azioni tipo, cartella documenti.
4. BVB invia l'**invito**: il cliente riceve una mail con un link di accesso.
5. Alla prima entrata il cliente conferma i dati e accetta l'informativa privacy.
6. La fase 1 passa automaticamente a `in corso`.

### 6.2 Accesso alla dashboard

**BVB:** scrive il nome nella barra di ricerca (funziona anche con parti di nome o nome della clinica), invio → dashboard cliente. Nessun'altra navigazione richiesta.

**Cliente:** riceve un **link magico** via email (valido 15 minuti, monouso); da lì imposta una password o resta con l'accesso via link. Sessione di 30 giorni sul dispositivo, rinnovabile. Atterra sempre sulla **sua** dashboard, mai su una lista.

### 6.3 Tracciamento di un incontro (in gran parte automatico)

1. BVB fissa l'incontro sul **calendario**, invitando il cliente; il link **Meet** viene generato dal calendario stesso.
2. L'app legge l'evento e crea l'incontro in stato `pianificato` nel percorso del cliente; il cliente lo vede subito come "prossimo incontro".
3. **Fireflies** entra nella riunione e registra.
4. A riunione conclusa l'app riceve la trascrizione: l'incontro passa a `svolto`, con durata reale e partecipanti.
5. **Claude** riceve trascrizione + contesto del cliente (fase, obiettivi, azioni aperte, report precedenti) e produce la **bozza di report** nel formato standard.
6. La bozza arriva in **"Da approvare"** nella console BVB. Il cliente non vede nulla finché non si approva.

### 6.4 Report: creazione, revisione, pubblicazione

1. BVB apre la bozza affiancata alla trascrizione.
2. Corregge, taglia, aggiunge; assegna le **azioni** con scadenza e responsabile.
3. **Pubblica**. Il report diventa visibile nella dashboard cliente e parte una notifica email.
4. Il cliente legge, spunta le proprie azioni, può chiedere un chiarimento: la domanda nasce già agganciata a quel report.
5. Se l'incontro chiude una fase, BVB fa avanzare la mappa (o l'app lo propone in automatico quando tutti i deliverable della fase risultano completi).

### 6.5 Richiesta di appuntamento (cliente → BVB)

1. Il cliente preme **Chiedi un appuntamento**, sceglie motivo e preferenza temporale.
2. La richiesta arriva in console con stato `in valutazione`.
3. BVB propone fino a **3 slot** letti dalle disponibilità reali del calendario.
4. Il cliente sceglie uno slot; l'app crea l'evento sul calendario con link Meet e invito al cliente.
5. L'incontro compare come `pianificato` in entrambe le dashboard. Stato richiesta: `confermata`.

### 6.6 Richiesta di informazioni (cliente → BVB)

1. Il cliente preme **Fai una domanda**; può agganciarla a un report, a un'azione o lasciarla generale.
2. La richiesta entra in console con priorità e tempo di risposta atteso (SLA dichiarato: 1 giorno lavorativo).
3. BVB risponde; il thread resta dentro il progetto, consultabile in futuro.
4. Se la risposta richiede un incontro, un pulsante converte la domanda in richiesta di appuntamento senza riscrivere nulla.

### 6.7 Avanzamento di fase

Quando i deliverable di una fase sono tutti completati, l'app segnala a BVB: *"La fase 4 di Ericko sembra conclusa: la faccio avanzare?"*. L'avanzamento resta **una decisione umana**, ma suggerita. Al cambio fase, il cliente riceve una notifica con il senso del passaggio ("Sei entrato nelle consulenze ricorrenti: ecco cosa succede ora").

---

## 7. Architettura di alto livello

```
                    ┌──────────────────────────────────────────┐
   BVB ────────────▶│  WEB APP (browser)                       │
   Cliente ────────▶│  Console BVB · Dashboard cliente         │
                    └───────────────┬──────────────────────────┘
                                    │ HTTPS / sessione con ruolo
                    ┌───────────────▼──────────────────────────┐
                    │  BACKEND — API applicativa               │
                    │  • autenticazione e permessi per cliente │
                    │  • percorsi, incontri, report, richieste │
                    │  • motore di automazione (regole)        │
                    │  • coda di lavori asincroni              │
                    └──┬──────────┬──────────┬──────────┬──────┘
                       │          │          │          │
             ┌─────────▼──┐ ┌─────▼────┐ ┌───▼──────┐ ┌─▼────────────┐
             │ Calendario │ │  Meet    │ │Fireflies │ │   Claude     │
             │ eventi,    │ │ link     │ │trascriz. │ │ bozze report │
             │ disponib.  │ │ riunione │ │ audio    │ │ sintesi      │
             └────────────┘ └──────────┘ └──────────┘ └──────────────┘
                       │          │          │          │
                    ┌──▼──────────▼──────────▼──────────▼──────┐
                    │  DATI: database + archivio documenti     │
                    │  (UE) + log di audit                     │
                    └──────────────────────────────────────────┘
```

**Principi architetturali**

- **Un'unica base dati multi-cliente**, con separazione logica per `client_id` applicata a livello di query e di riga (row-level security). Un solo deployment serve tutti i clienti: è ciò che rende il modello riproducibile a costo quasi zero.
- **Le integrazioni sono adattatori sostituibili.** Fireflies e Claude stanno dietro un'interfaccia (`TranscriptionProvider`, `ReportGenerator`): se domani cambia lo strumento, cambia l'adattatore, non l'app.
- **Tutto ciò che è lento è asincrono.** Trascrizione e generazione report girano in coda con ritentativi: se Fireflies tarda, la dashboard non si blocca.
- **Nessuna scrittura verso il cliente senza approvazione.** Le automazioni producono sempre stati intermedi (`bozza`, `proposto`), mai contenuti pubblicati.

### Stack consigliato

| Livello | Scelta | Perché |
|---|---|---|
| Frontend | React + TypeScript, Vite | Ecosistema noto, due sole aree da costruire |
| Backend | Node.js/TypeScript (o Python/FastAPI) | Stesso linguaggio del frontend, integrazioni semplici |
| Database | PostgreSQL | Relazioni chiare, row-level security nativa |
| File | Object storage con regione UE | Documenti e PDF dei report |
| Code | Job queue (Redis/pg-boss) | Trascrizioni e generazione report |
| Hosting | PaaS europeo (Vercel/Fly/Render + Postgres UE) | Zero gestione server |
| Autenticazione | Magic link + password opzionale, 2FA per BVB | Attrito minimo per il cliente |

**Alternativa rapida (no-code / low-code):** back office su Airtable o Notion + automazioni su n8n + un frontend leggero per la sola dashboard cliente. Consigliata solo come **pilota a 4 settimane** sui primi tre clienti; oltre i 10 clienti conviene l'impianto sopra.

---

## 8. Modello dati

| Entità | Campi principali | Relazioni |
|---|---|---|
| **Client** | nome, clinica, email, telefono, stato, data inizio, consulente | ha 1 Journey, molti Meeting/Request/Document |
| **User** | email, ruolo (`owner`, `consultant`, `client`, `guest`), client_id | appartiene a Client se ruolo cliente |
| **JourneyTemplate** | nome, versione, elenco fasi tipo | genera Journey |
| **Journey** | client_id, template_id, fase corrente, % avanzamento | ha molte Stage |
| **Stage** | numero, titolo, stato, apertura/chiusura, deliverable attesi | ha molte Action, molti Meeting |
| **Meeting** | data, titolo, tipo, durata prevista/reale, stato, link Meet, id evento calendario, id trascrizione | ha 0/1 Report |
| **Transcript** | provider, id esterno, testo, partecipanti, url registrazione, scadenza | appartiene a Meeting |
| **Report** | stato (`bozza`/`in revisione`/`pubblicato`), sintesi, decisioni, temi aperti, autore, versione, generato_da | appartiene a Meeting, ha molte Action |
| **Action** | testo, responsabile (`cliente`/`BVB`), scadenza, stato | collegata a Stage e/o Report |
| **Request** | tipo (`appuntamento`/`informazione`), oggetto, testo, stato, priorità, riferimento | appartiene a Client, ha molti Message |
| **Message** | autore, testo, allegati, data | appartiene a Request |
| **Document** | titolo, tipo, visibilità (`cliente`/`interno`), file | appartiene a Client |
| **AuditLog** | chi, cosa, quando, su quale risorsa | trasversale |

Stati di `Meeting`: `pianificato → svolto → trascritto → refertato`. Stati di `Request`: `inviata → in valutazione → slot proposti / in risposta → conclusa`.

---

## 9. Integrazioni

### 9.1 Calendario

- **Lettura:** eventi con il cliente fra i partecipanti → creazione/aggiornamento automatico dell'incontro nella dashboard (aggiornamento a eventi, non a interrogazione periodica).
- **Scrittura:** conferma di uno slot proposto → creazione evento con invito al cliente e videochiamata annessa.
- **Disponibilità:** lettura degli spazi liberi per proporre slot reali, con regole BVB (finestre di lavoro, durata standard, cuscinetto fra incontri).

### 9.2 Google Meet

Il link nasce dall'evento di calendario. L'app lo mostra nella dashboard e attiva il pulsante **Entra su Meet** da 10 minuti prima dell'inizio. Nessuna gestione separata.

### 9.3 Fireflies (registrazione e trascrizione)

- Fireflies partecipa alla riunione secondo la configurazione già in uso.
- A trascrizione pronta, l'app la recupera e la **associa all'incontro giusto** confrontando id evento, orario e partecipanti; se l'abbinamento è incerto, l'incontro finisce in "Da abbinare" invece di indovinare.
- Vengono salvati: testo, partecipanti, durata reale, riferimento alla registrazione.
- La trascrizione integrale è **materiale interno**: al cliente arriva il report, non il verbale, salvo richiesta esplicita.

### 9.4 Claude (generazione dei report)

Ricetta di generazione, uguale per ogni cliente:

```
CONTESTO      profilo cliente, fase corrente, obiettivi dichiarati,
              azioni aperte, sintesi dei due report precedenti
INPUT         trascrizione dell'incontro
FORMATO       In sintesi · Decisioni · Azioni (chi/cosa/quando) · Temi aperti
REGOLE        italiano semplice e diretto; niente ricostruzioni non
              presenti nella trascrizione; azioni sempre con responsabile
              e data; segnalare esplicitamente ciò che è rimasto sospeso
```

Output: bozza in stato `bozza`, con evidenza di ciò che Claude non è riuscito a determinare. **La pubblicazione resta un gesto umano.** Claude viene usato anche per due compiti minori: proporre una risposta alle richieste di informazioni ricorrenti, e riassumere lo storico quando si riapre un cliente dopo mesi.

### 9.5 Sequenza completa, dall'incontro alla dashboard

```
Evento a calendario ──▶ Incontro "pianificato" ──▶ visibile al cliente
        │
     Meet ──▶ riunione ──▶ Fireflies registra e trascrive
                                   │
                        Incontro "trascritto"
                                   │
                        Claude ──▶ bozza di report
                                   │
                        BVB rivede, assegna azioni, PUBBLICA
                                   │
        Dashboard cliente: report + azioni + fase aggiornata + notifica
```

Tempo atteso fra fine riunione e bozza pronta: **10–20 minuti**, senza intervento umano.

---

## 10. Back office

Il back office è la parte che rende il sistema replicabile e mantenibile.

- **Clienti:** creazione, invito, sospensione, assegnazione consulente, archiviazione a fine percorso.
- **Template di percorso:** fasi, deliverable, azioni tipo, durate attese. Si possono avere più template (es. "Consulenza completa", "Solo AI Activation", "Percorso azienda").
- **Modelli di report:** struttura e istruzioni date a Claude, versionate. Cambiare qui migliora i report di tutti i clienti futuri.
- **Integrazioni:** stato delle connessioni, ultimo evento ricevuto, errori recenti, ri-autorizzazione con un clic.
- **Automazioni:** regole attivabili singolarmente (trascrizione automatica, bozza automatica, promemoria azioni in scadenza, promemoria incontro a 24 ore).
- **Utenti e ruoli**, **privacy** (§11), **esportazioni** (percorso completo di un cliente in PDF/JSON).

---

## 11. Sicurezza e privacy

**Accessi**
- Cliente: link magico monouso (15 minuti) + sessione ricordata; password facoltativa.
- BVB: password + secondo fattore obbligatorio.
- Ogni sessione porta con sé ruolo e `client_id`; il server autorizza ogni singola richiesta, mai il solo frontend.

**Dati**
- Cifratura in transito (TLS) e a riposo; dati e file ospitati in **Unione Europea**.
- **Segregazione per cliente** verificata anche a livello di database (row-level security).
- **Registro di audit** su ogni accesso a report e documenti: chi ha visto cosa e quando.

**Registrazioni e trascrizioni (il punto più delicato)**
- Consenso raccolto all'onboarding e ricordato all'inizio di ogni incontro registrato.
- Conservazione predefinita: **registrazione 30 giorni, trascrizione 12 mesi, report senza limite** (il report è il documento di progetto). Valori configurabili.
- Le trascrizioni non sono esposte al cliente per impostazione predefinita.
- Cancellazione su richiesta: un comando elimina registrazione e trascrizione mantenendo il report.

**GDPR**
- Base giuridica: esecuzione del contratto di consulenza; consenso separato per la registrazione.
- Informativa in app, esportazione dei propri dati e cancellazione dell'account su richiesta.
- Registro dei responsabili esterni (fornitori di calendario, riunioni, trascrizione, modelli linguistici).
- Dati aziendali del cliente veterinario trattati come **riservati**: nessun dato di clinica viene usato per addestrare modelli; si usano solo servizi con impegno di non addestramento.

**Continuità**
- Backup giornalieri con conservazione 30 giorni; prova di ripristino trimestrale.
- Se un'integrazione cade, l'app resta usabile: gli incontri si inseriscono a mano e la bozza di report si può scrivere direttamente.

---

## 12. Riproducibilità e scalabilità

**Il processo replicabile in cinque righe**

1. Nuovo cliente creato da template → spazio pronto in meno di due minuti.
2. Ogni incontro segue la stessa catena: calendario → Meet → Fireflies → Claude → approvazione → pubblicazione.
3. Ogni report ha la stessa struttura, quindi è confrontabile nel tempo e fra clienti.
4. Ogni fase ha deliverable dichiarati: "finito" significa la stessa cosa per tutti.
5. Ogni miglioramento (una fase in più, un prompt migliore) si applica dal back office e vale per tutti i clienti successivi.

**Scalabilità tecnica.** Un cliente in più significa righe in più, non un'installazione in più. L'impianto regge senza modifiche l'ordine delle centinaia di clienti; i costi variabili sono trascrizione e generazione dei report.

**Scalabilità organizzativa.** Il ruolo *Consulente* permette di far entrare collaboratori con visibilità limitata ai propri clienti: il metodo BVB resta nel template, non nella testa della singola persona. È questa la condizione perché il modello funzioni anche fuori dal caso veterinario: cambia il template di percorso, resta l'impianto.

**Costo marginale per cliente:** stimato **2–6 € al mese** (archiviazione, trascrizione, generazione report), a fronte del tempo di ricomposizione manuale oggi speso per ogni incontro.

---

## 13. Piano di rilascio

| Fase | Contenuto | Durata stimata |
|---|---|---|
| **MVP — Pilota** | Console BVB con ricerca cliente, dashboard cliente, mappa fasi, incontri manuali, report scritti in app, richieste appuntamento e informazioni, inviti clienti | 3–4 settimane |
| **V1 — Automazione** | Sincronizzazione calendario, abbinamento Fireflies, bozze report con Claude, notifiche email, azioni con scadenza | +3 settimane |
| **V2 — Solidità** | Back office completo, template multipli, proposta slot da disponibilità reali, esportazioni PDF, audit e retention configurabile | +3 settimane |
| **V3 — Estensioni** | Ospiti del cliente, documenti condivisi, indicatori di risultato del percorso, app installabile su telefono | a seguire |

Il pilota parte con **Ericko e Antonio**; Marta entra alla V1 come primo cliente onboardato interamente con il processo automatico — è la verifica che il modello sia davvero riproducibile.

---

## 14. Indicatori di successo

| Indicatore | Obiettivo |
|---|---|
| Tempo fra fine incontro e report pubblicato | da giorni a **meno di 24 ore** |
| Tempo BVB per produrre un report | **−70%** (revisione anziché scrittura) |
| Richieste di stato del percorso ("a che punto siamo?") | **verso zero** |
| Azioni cliente completate entro scadenza | **> 80%** |
| Tempo di creazione di un nuovo cliente | **< 2 minuti** |
| Clienti che entrano in dashboard almeno una volta a settimana | **> 70%** |

---

## 15. Rischi e contromisure

| Rischio | Contromisura |
|---|---|
| Il cliente non entra mai in dashboard | Le notifiche email contengono il contenuto essenziale e un link diretto; la dashboard è utile perché è l'unico posto dove chiedere un appuntamento |
| Report generato impreciso o inventato | Nessuna pubblicazione automatica; Claude segnala esplicitamente ciò che non ha potuto determinare; la trascrizione resta consultabile a fianco |
| Abbinamento sbagliato fra trascrizione e incontro | Coda "Da abbinare" invece di indovinare |
| Diffidenza sulla registrazione | Consenso esplicito, conservazione breve dichiarata, cancellazione su richiesta con un comando |
| Sovra-costruzione del prodotto | Perimetro V1 chiuso: niente CRM, niente fatturazione, niente chat |
| Dipendenza da un fornitore | Integrazioni dietro adattatori sostituibili |

---

## 16. Glossario

- **Percorso (Journey):** l'intero cammino di un cliente, dal primo contatto al presidio.
- **Fase (Stage):** uno dei sei passi del percorso.
- **Incontro (Meeting):** una sessione con il cliente, in presenza o su Meet.
- **Report:** il documento che chiude un incontro: sintesi, decisioni, azioni, temi aperti.
- **Azione (Action):** un impegno con responsabile e scadenza.
- **Richiesta (Request):** una comunicazione di progetto del cliente, di appuntamento o di informazione.
- **Template di percorso:** il modello riproducibile da cui nasce ogni nuovo percorso.

---

*Documento di proposta. Il prototipo cliccabile delle schermate è in `mockup/journey-app/index.html`.*
