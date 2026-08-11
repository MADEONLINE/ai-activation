# Dossier di build — Assistente Commercialista AI

*Motore: `ai-solution-architect` · uso **INTERNO** · non inviare al cliente*
*Legenda: `[F]` fatto detto in call · `[A]` ipotesi/stima analista · `[R]` da ricerca con fonte*
*Tariffa di listino: **€350/h a persona** · costo interno: **€800/gg a persona** (€100/h)*
*Prezzo = ore di catalogo × tariffa (`preventivo-engine.md`) — nessun pricing a valore*
*Data di redazione: agosto 2026 · normativa verificata al 11/08/2026*

> **AVVERTENZA SULLA SORGENTE — leggila prima di usare questo dossier.**
> L'input ricevuto **non è la trascrizione di una call con un cliente reale**: è la
> **griglia di scoperta** (sei domande) più il mandato "assistente commercialista AI
> con workflow agentici". Di conseguenza **la §1 è quasi tutta `n/d`** e tutto ciò
> che segue è costruito sull'**archetipo di studio commercialista italiano** `[A]`,
> non su uno studio specifico.
> **Cosa vale comunque:** l'architettura, il catalogo dei workflow, il monte-ore, i
> tier e l'intero Allegato A (AI Act) sono **riusabili così come sono** su qualsiasi
> studio. **Cosa non vale finché non si fa la call:** ogni cifra è una *stima su
> perimetro non verificato* — dimensione dello studio, gestionale, volumi e accessi
> ai dati cambiano il buffer e quindi il prezzo. **Non consegnare un fisso prima
> dello sprint diagnostico.**
> Questo dossier è quindi anche un **template di categoria**: la griglia della §1.1
> è lo strumento con cui si riempie il caso reale in 45 minuti di call.

---

## 0 · Verdetto (BLUF)

**Archetipo portante:** **A2 Automazione di workflow** (il sistema nervoso dello
studio: scadenze, chiusura mensile, invii, solleciti) + **A7 pipeline documentale**
+ **A4 knowledge di studio** + **A5 skill di studio**; **A6 ponte gestionale** come
**Fase 2 a gate**, mai nell'MVP.
**Go/no-go:** 🟢 **GO** sul disegno — 🟡 **condizionato sul prezzo**: il pacchetto
completo pesa troppo sul fatturato di uno studio medio, quindi si **sequenzia**
(Essential adesso, Pro dopo 6–9 mesi), non si sconta.
**Sprint diagnostico:** 12 h → **€4.200** (scalabile per intero).
**Attivazione — tier target:** Essential **92 h quotate → €32.200** come ingresso;
Pro **169 h → €59.150** come punto d'arrivo a 12 mesi.
**Canone:** presidio base 2 h/mese → €700/mese (Essential) · attivo 4 h/mese →
€1.400/mese (Pro), + infra pass-through €150–350/mese `[A]`.
**La mossa che cambia l'economia del deal:** il **kit di conformità AI Act**
costruito dentro il progetto (§Allegato A) diventa un **servizio che lo studio
rivende ai propri clienti** — da costo di compliance a linea di ricavo. È l'ancora
di valore più forte che abbiamo su questo segmento.
**Prossima azione:** vendere lo sprint, che include la **verifica degli accessi** e
l'**inventario dei sistemi AI** (adempimento art. 4 già scaduto, quindi utile da solo).

---

## 1 · Findings

### 1.1 · La griglia delle sei domande (lo strumento d'intake, da riempire in call)

Le sei domande fornite **sono** la griglia di scoperta. Ecco cosa estrarre da
ciascuna e in quale workflow si traduce — questa tabella è il vero deliverable
riusabile della §1.

| # | Domanda al commercialista | Cosa devi estrarre davvero | Dove finisce |
|---|---|---|---|
| 1 | **Qual è la prima cosa che fai appena arrivi in ufficio?** | Il rituale di orientamento: cosa guarda per capire "come sta lo studio oggi" — posta/PEC, scadenzario, pratiche ferme, telefonate arretrate. Quanti minuti ci mette, quante fonti apre. | **W1 · Cruscotto del mattino** |
| 2 | **Quale roba proprio non vorresti fare?** | Il dolore emotivo, non quello razionale. Di norma: data entry, rincorrere i clienti per i documenti, quadrature, ricerca normativa a mano. *Questa è la domanda che vende.* | **W2 · Sollecito documenti** · **W3 · Prima nota** · **W4 · Ricerca normativa** |
| 3 | **Cosa fai ogni mese?** | Il ciclo ricorrente per cliente: IVA (liquidazione/LIPE), prima nota, ritenute, F24, controllo registri. Chi lo fa, con che checklist, quanto tempo per cliente × numero clienti. | **W5 · Chiusura mensile guidata** |
| 4 | **Cosa invii ai tuoi clienti?** | Gli output ricorrenti: F24, prospetto IVA, situazione periodica, richieste documenti, circolari normative. Con che canale, con che template, chi li impagina. | **W6 · Pacchetto cliente mensile** |
| 5 | **Scadenze** | Come vive lo scadenzario: dentro il gestionale, su Excel, in testa. Chi lo aggiorna, come si avvisa il cliente, cosa succede quando salta. | **W7 · Motore scadenze + promemoria** |
| 6 | **Pagamenti** | **Due cicli diversi, da separare sempre:** (a) i pagamenti del *cliente allo Stato* (F24, deleghe, ravvedimento); (b) gli **incassi dello studio** (parcelle, insoluti, DSO). Il (b) quasi nessuno lo presidia ed è quello che ripaga il progetto. | **W7** (a) · **W8 · Ciclo attivo dello studio** (b) |

> **Domanda da aggiungere alla griglia, mancante e decisiva:** *"Chi, nello studio,
> ha già in mano un pezzo di questo lavoro e sarebbe contento di mollarlo?"* — serve
> a trovare il **referente interno** (campo 5), che è il singolo fattore che più
> abbassa cost-to-serve e churn.

### 1.2 · I nove campi del build

1. **Identità & contesto** — Studio commercialista italiano `[A]`. Soci `n/d` ·
   collaboratori `n/d` · numero clienti `n/d` · fatturato `n/d` · mix
   contabilità/consulenza `n/d`. **Tutto da riempire in call: senza il numero di
   clienti e di collaboratori il monte-ore non è difendibile.**
2. **Dolore / job-to-be-done** — `n/d` sul caso specifico. Ipotesi di categoria
   `[A]`: il tempo del socio è assorbito dal presidio degli adempimenti e dal
   rincorrere i clienti, non dalla consulenza — che è l'unica parte che marginano
   davvero. La leva è **restituire ore qualificate**, non "fare più in fretta".
3. **Processo as-is** — `n/d`. Da ricostruire con le sei domande. Atteso `[A]`:
   ciclo mensile ripetuto identico per N clienti, con checklist informale, memoria
   personale e Excel a fare da collante tra gestionale, PEC e Drive.
4. **Dati & sistemi** — `n/d`. Il mercato italiano è concentrato: **Zucchetti e
   TeamSystem servono insieme oltre il 70% degli studi** `[R]`, accanto a Wolters
   Kluwer (Genya/Profis), Sistemi, Buffetti, Datev Koinos `[R]`. Entrambi i poli
   principali stanno aprendo layer di integrazione verso API esterne, ma
   **l'operatività diretta piena è attesa entro fine 2026 su Genya e Ago** `[R]` —
   cioè **non è ancora scontata oggi**. → **Rischio numero uno, §5.**
5. **Referente interno** — `n/d`. **Da qualificare in call**: senza, il canone va
   dimensionato più alto e la probabilità di churn sale.
6. **Committment & budget** — `n/d`. Nota di categoria `[A]`: negli studi il
   decisore economico (socio anziano) e il champion (socio giovane o responsabile
   contabilità) quasi mai coincidono → §7.
7. **Vincoli & rischi** — **Noti e pesanti anche senza call:** segreto
   professionale; dati fiscali e personali dei clienti; **art. 13 L. 132/2025**, in
   vigore dal 10 ottobre 2025, che impone di usare l'AI solo come *supporto* e di
   **informare preventivamente il cliente** in modo chiaro, semplice ed esaustivo
   `[R]`; **art. 4 AI Act** (alfabetizzazione) già applicabile dal 2 febbraio 2025
   `[R]`; **art. 50 AI Act** (trasparenza) applicabile **dal 2 agosto 2026**,
   insieme al regime sanzionatorio nazionale `[R]`. Il commercialista **resta
   titolare del trattamento** e risponde dell'inserimento di dati dei clienti in
   sistemi AI non conformi `[R]`. → **Allegato A.**
   Vincolo operativo aggiuntivo `[A]`: **stagionalità estrema** (giugno–luglio e
   novembre sono muri) — il go-live non si mette mai a ridosso di una scadenza.
8. **Obiettivi & metrica di valore** — `n/d` sul caso. Metriche strumentabili dal
   sistema stesso `[A]`, quindi utilizzabili come prova di valore e come eventuale
   upside: ore/mese sul ciclo di chiusura, giorni medi di ritardo nella consegna dei
   documenti da parte dei clienti, % scadenze presidiate senza intervento manuale,
   **DSO dello studio** sulle proprie parcelle.
9. **Citazioni utili** — **nessuna disponibile** (non c'è call). *Da raccogliere: le
   citazioni testuali sulla domanda 2 sono quelle che poi reggono la proposta.*

---

## 2 · Architettura

L'errore da non fare su questo segmento è partire dall'agente conversazionale verso
i clienti dello studio (è il riflesso condizionato, ed è già in libreria dal caso
Marsili). **Qui il segnale porta altrove:** le sei domande descrivono un **processo
multi-cliente ricorrente, a step noti, che oggi tiene insieme sistemi diversi con
la memoria delle persone**. Quella forma di lavoro ha un archetipo solo.

### Portante — **A2 · Automazione di workflow**
**Segnali:** domande 3, 5 e 6 descrivono letteralmente processi a step ripetuti
identici per N clienti ("lo facciamo a mano ogni volta"); la domanda 1 descrive un
rituale di aggregazione manuale da più fonti.
**Stack:** n8n come spina dorsale · nodi Claude dove serve giudizio (classificare,
redigere, decidere l'eccezione) · trigger a calendario/webhook/email · Google
Workspace.
**Effort baseline:** 32–80 h per workflow di media complessità `[A]`.
**Tag:** **REDEPLOYMENT** sull'impianto (la libreria n8n copre trigger, idempotenza,
retry, notifiche); **NET-NEW** sulle regole di dominio fiscale.

### Supporto — **A7 · Pipeline documentale**
**Segnali:** domanda 2 (data entry, prima nota, fatture passive) e domanda 4
(pacchetto che esce verso il cliente ogni mese). Documento-in → dato-out, e
dato-in → documento-out: entrambe le direzioni.
**Stack:** ingest (PEC/email/cartella) · lettura Claude su PDF · generazione via
template `docx`/`pdf` · n8n per il flusso.
**Effort baseline:** 48–112 h net-new `[A]`.
**Tag:** impianto **REDEPLOYMENT**, template e regole **NET-NEW**.

### Supporto — **A4 · Knowledge di studio**
**Segnali:** domanda 2, ramo "ricerca normativa"; e il fatto che le risposte
ricorrenti dello studio (lettere-tipo, prassi interne, circolari già scritte) siano
disperse. Serve **risposta con citazione della fonte**, mai risposta libera.
**Effort baseline:** 64–144 h net-new `[A]`; nell'MVP se ne prende una versione
**minima** (corpus interno dello studio, non normativa esterna).
**Tag:** impianto **REDEPLOYMENT**, corpus **NET-NEW**.

### Supporto — **A5 · Skill di studio**
**Segnali:** domanda 4 — un output professionale ricorrente, strutturato, che oggi
solo alcune persone sanno confezionare bene.
**Effort baseline:** 48–120 h net-new `[A]`.
**Tag:** **NET-NEW**, ed è il pezzo che **più nutre la libreria**.

### Fase 2, a gate — **A6 · Ponte gestionale (MCP)**
**Segnali:** campo 4. È l'abilitatore che porterebbe tutto in tempo reale.
**Perché è a gate e non nell'MVP:** l'accesso non è verificato e la maturità dei
layer API dei gestionali italiani è ancora in corso di consolidamento `[R]`. Per
la regola del motore (`preventivo-engine.md` §5) **un componente che dipende da un
accesso non verificato non si quota a fisso.**
**Tag:** **NET-NEW** · *lascia in libreria il connettore verso il gestionale — asset
ad altissimo ritorno, perché due fornitori coprono oltre il 70% del mercato* `[R]`.

### Espansione, Fase 3 — **A1 · Agente conversazionale verso i clienti dello studio**
**Tag:** **REDEPLOYMENT** pieno (template agente-studio-professionale già in
libreria dal caso Marsili). Non è il primo progetto: si vende dopo, a CAC ≈ 0.

> **Perché questa combinazione e non un'altra.** Il dolore primario non è "rispondere
> ai clienti": è **tenere in piedi un ciclo ricorrente senza che nulla cada**. Un
> agente conversazionale sopra un ciclo non presidiato aumenta il rumore. Si mette
> prima il sistema nervoso (A2), poi le mani (A7), poi la memoria (A4/A5), e solo
> alla fine la bocca (A1).

### Il catalogo dei workflow agentici (la risposta operativa alle sei domande)

| ID | Workflow | Trigger | Passi agentici | Dove interviene l'umano | Output | Archetipo · Fase |
|---|---|---|---|---|---|---|
| **W1** | **Cruscotto del mattino** | schedulato, 7:30 | legge PEC/email della notte, classifica per urgenza e cliente; incrocia scadenze a 7/15/30 gg; rileva pratiche ferme oltre soglia; segnala risposte AdE e notifiche | il socio legge e decide: il brief propone, non agisce | un messaggio unico (mail/Slack/WhatsApp) con "oggi conta questo" + link diretti | A2 · **MVP-Pro** |
| **W2** | **Sollecito documenti** | schedulato, per cliente e per adempimento | verifica cosa manca rispetto alla checklist del periodo, redige il sollecito nel tono dello studio, invia, traccia, **escala dopo N giorni**, aggiorna lo stato | approvazione batch alla prima esecuzione, poi solo le eccezioni | email/WhatsApp al cliente + stato aggiornato + lista dei renitenti | A2+A5 · **MVP-Essential** |
| **W3** | **Prima nota & fatture passive** | arrivo documento (PEC/cartella) | estrae dati dal PDF, propone la classificazione contabile, segnala anomalie e duplicati, prepara il tracciato per il gestionale | **revisione obbligatoria** prima di qualsiasi scrittura: la macchina propone, non registra | tracciato di importazione + report delle eccezioni | A7 · **Premium** |
| **W4** | **Ricerca normativa con fonte** | su richiesta | cerca nel corpus dello studio (circolari, prassi, risposte già date), risponde **solo con citazione del documento**, dichiara quando non sa | sempre: è uno strumento per il professionista, non un parere | risposta con fonte citata + link al documento | A4 · **Pro** |
| **W5** | **Chiusura mensile guidata** | calendario del periodo | genera la checklist per cliente in base al regime, verifica lo stato di ogni voce, blocca l'avanzamento sulle incompletezze, produce lo stato di avanzamento dello studio | il collaboratore spunta e conferma; il sistema non chiude nulla da solo | cruscotto di chiusura per cliente e per collaboratore | A2 · **Pro** |
| **W6** | **Pacchetto cliente mensile** | a chiusura completata | assembla F24, prospetto IVA, situazione periodica; genera la lettera di accompagnamento nel tono dello studio; prepara l'invio | **firma/approvazione umana obbligatoria** prima dell'invio (art. 13 L. 132/2025) | PDF brandizzati + email pronta, in bozza | A7+A5 · **Pro** |
| **W7** | **Motore scadenze & promemoria** | continuo | mantiene lo scadenzario per cliente e adempimento, avvisa lo studio e — su regola — il cliente, gestisce il preavviso sui pagamenti F24 | il socio decide le regole una volta; poi solo eccezioni | scadenzario vivo + promemoria multicanale | A2 · **MVP-Essential** |
| **W8** | **Ciclo attivo dello studio** | mensile + eventi | genera le parcelle dal maturato, invia, monitora gli incassi, sollecita gli insoluti per fasce, calcola il DSO | approvazione della proposta di parcellazione | parcelle + solleciti + cruscotto incassi | A2 · **Premium** |
| **W0** | **Knowledge di studio** | continuo | indicizza prassi, lettere-tipo, circolari, risposte storiche; alimenta W2, W4, W6 | il referente interno cura il corpus | base di conoscenza citabile | A4 · **Pro** |

> **Regola di disegno trasversale, non negoziabile:** **nessun workflow invia nulla
> a un cliente o allo Stato senza approvazione umana.** Non è prudenza tecnica: è il
> requisito dell'art. 13 L. 132/2025 (l'apporto intellettuale del professionista deve
> restare prevalente e determinante) `[R]`. Va scritto nel blueprint e va mostrato al
> cliente — è un argomento di vendita, non un limite.

---

## 3 · Studio: dominio + stato dell'arte

**Dominio.** Lo studio commercialista italiano vive una compressione classica: la
parte a basso valore (adempimenti, data entry, presidio delle scadenze) assorbe la
capacità, mentre la parte che margina (consulenza fiscale, supporto alle decisioni,
pianificazione) è quella che resta indietro — ed è esattamente la direzione in cui
il mercato 2026 sta spingendo gli studi, verso modelli basati su digitalizzazione
dei processi, automazione e consulenza strategica `[R]`. Il vincolo strutturale è
che **il lavoro si ripete identico per N clienti**: qualunque minuto tolto a un
ciclo va moltiplicato per il portafoglio, ed è lì che sta il valore ancorabile.
Vincoli di settore: segreto professionale, titolarità del trattamento in capo al
professionista, obbligo di registro dei trattamenti, misure tecniche e organizzative
adeguate e notifica del data breach entro 72 ore — **il segreto professionale non
sostituisce né deroga a nessuno di questi obblighi** `[R]`.
Rischio di dominio da non sottovalutare `[A]`: la **stagionalità**. Un progetto che
va in go-live a giugno o a novembre fallisce l'adozione anche se il software è
perfetto.

**Stato dell'arte tecnologico.** Il pattern portante (A2, automazione di workflow con
nodi AI su n8n) è maturo e production-ready: è il mattone più riusabile dello stack.
La pipeline documentale su PDF fiscali è matura in lettura, **fragile
sull'accuratezza dei dati critici** — motivo per cui W3 resta *proposta da rivedere*,
mai scrittura automatica. Il punto critico vero è l'integrazione: i due poli del
mercato (TeamSystem e Zucchetti, insieme oltre il 70% degli studi `[R]`) stanno
costruendo layer di integrazione sempre più aperti verso API esterne `[R]`, e hanno
introdotto funzionalità AI native nei gestionali dalla primavera 2025 `[R]`, ma
**l'operatività diretta più ampia è attesa su Genya e Ago entro fine 2026** `[R]`:
cioè oggi l'accesso API pieno **non si può dare per scontato** e va verificato
studio per studio. Conseguenza architetturale già presa: **l'MVP gira su fonti che
lo studio controlla comunque** (PEC/email, Drive, export schedulati), e l'API va in
Fase 2 con un gate.
Costi infra: le piattaforme low-code stanno tipicamente su €50–200/mese e le API AI
su €50–300/mese secondo il volume `[R]` → per uno studio di media dimensione stimo
**€150–350/mese** `[A]`, pass-through.
Bande di mercato italiane 2026 utili al sanity check: progetto base su 1–3 processi
**€2.000–5.000**, ecosistema completo **€5.000–15.000** `[R]` per la fascia
low-cost/low-code; retainer per PMI dopo il primo agente **€5–8k/mese** nella fascia
alta `[R]`. **Attenzione: la forbice di mercato su questo segmento è enorme** ed è
il fattore che condiziona di più la trattativa → §6 e §7.

---

## 4 · Scope

### 4.1 · Monte-ore di catalogo per workstream

| Workstream | **Essential** | **Pro** *(target a 12 mesi)* | **Premium** |
|---|---:|---:|---:|
| Discovery & blueprint | 0 | 0 | 0 |
| Architettura & setup | 8 | 12 | 14 |
| Build | 24 | 48 | 88 |
| Integrazione | 12 | 20 | 24 |
| Test & iterazione | 10 | 20 | 32 |
| Deploy & go-live | 5 | 8 | 10 |
| **Compliance & AI Act** | 8 | 12 | 12 |
| Documentazione & handoff | 6 | 10 | 14 |
| **Totale ore di catalogo** | **73** | **130** | **194** |

*Discovery a 0 in tutti i tier: è già pagata dallo sprint diagnostico.*
*Il workstream **Compliance & AI Act** è **lavoro reale, non buffer**: registro dei
sistemi, classificazione del rischio, informativa art. 13, istruzioni d'uso,
logging e supervisione (dettaglio in Allegato A). Tenerlo come voce a sé lo rende
vendibile e riusabile — e impedisce di nasconderlo dentro il rischio.*

### 4.2 · Composizione dei tier

| | Workflow inclusi | Nota |
|---|---|---|
| **Essential** | W7 scadenze + W2 sollecito documenti | il dolore più sentito, l'archetipo più riusabile, il go-live più veloce |
| **Pro** | Essential + W1 cruscotto + W5 chiusura + W6 pacchetto cliente + W0 knowledge + W4 ricerca | il ciclo mensile completo presidiato |
| **Premium** | Pro + W3 prima nota + W8 ciclo attivo dello studio | tocca la contabilità e la cassa dello studio |
| **Fase 2 a gate** | A6 ponte gestionale | **non quotabile a fisso** finché l'accesso non è verificato |
| **Fase 3** | A1 agente verso i clienti | redeployment, land-and-expand |

### 4.3 · Perimetro

**DENTRO (MVP Essential):**
1. Scadenzario per cliente e adempimento, alimentato da export/foglio esistente.
2. Promemoria interni allo studio e — su regola esplicita — al cliente.
3. Sollecito documenti multicanale con escalation e tracciamento.
4. Approvazione umana su tutto ciò che esce dallo studio.
5. Registro dei sistemi AI, informativa art. 13 e policy d'uso interno.

**FUORI (è pipeline di espansione, non perdita):**
1. Qualsiasi **scrittura automatica** nel gestionale o verso lo SdI.
2. Invio di F24 o adempimenti allo Stato senza mano umana. *Mai, in nessun tier.*
3. Pareri fiscali nel merito: il sistema cita, non consiglia.
4. Valutazione del **merito creditizio** dei clienti persone fisiche e qualunque uso
   su **selezione del personale** — sono aree dell'Allegato III AI Act (§Allegato A):
   fuori perimetro per scelta, non per dimenticanza.
5. Area paghe, se presente, oltre al promemoria delle scadenze.
6. Integrazione API con il gestionale (Fase 2, a gate).

**Change-control:** tutto ciò che esce dal blueprint validato è **una nuova riga**
con il suo monte-ore e il suo prezzo. Il fisso regge solo con questa regola scritta.

---

## 5 · Fattibilità + rischio

*Colonna ore = **ore di catalogo del componente** (build + sua quota di integrazione
e di test), misurate **sul perimetro Premium**. Riconciliazione con §4.1: la somma
dei componenti W7→W8 è **144 h** = Premium 194 h − 50 h di workstream trasversali
(setup 14 + deploy 10 + compliance 12 + handoff 14). **A6 è fuori dai 194** perché
non si quota. Nei tier più bassi i singoli componenti pesano di più, perché si
caricano da soli l'integrazione e il test che nel Premium sono condivisi.*

| Componente | Sistemi coinvolti | Integrazione | Ore `[A]` | Rischio | Verdetto | Riusabile già in libreria | Cosa lascia in libreria |
|---|---|---|---:|---|---|---|---|
| **W7** scadenze | foglio/export, calendario, canale | bassa complessità | 14 | basso — pattern maturo | 🟢 | scheletro n8n scadenze/promemoria | **motore-scadenzario-professionale** (vale su avvocati e consulenti del lavoro) |
| **W2** solleciti | email/WhatsApp, storage | media | 16 | basso-medio — tono e casi-limite | 🟢 | workflow riattivazione/sollecito | **sollecito-documenti multicanale con escalation** |
| **W1** cruscotto | PEC/email, W7 | media — la PEC è il punto delicato | 16 | medio — classificazione della posta | 🟡 | triage email | template **daily-brief professionale** |
| **W5** chiusura | checklist, stato per cliente | media | 18 | medio — le regole per regime sono tante | 🟡 | — | **checklist engine per regime fiscale** |
| **W6** pacchetto | template docx/pdf, email | media | 20 | medio — qualità e tono dell'output | 🟡 | renderer documentale | **skill pacchetto-cliente-mensile** (A5) |
| **W0/W4** knowledge | corpus dello studio | dipende dall'igiene del corpus | 16 | medio — se il corpus è sporco, esplode | 🟡 | impianto RAG | — |
| **W3** prima nota | PDF fatture, tracciato gestionale | alta | 26 | **alto — accuratezza su dati critici** | 🟡 | pipeline ingest→parse | parser fatture passive italiane |
| **W8** ciclo attivo | maturato, incassi, banca | alta | 18 | medio-alto — dipende dai dati del maturato | 🟡 | — | **workflow parcellazione & solleciti incassi** |
| | | **somma componenti** | **144** | | | | |
| **A6** gestionale | TeamSystem/Zucchetti/Genya… | **non verificata** | 36 *(fuori totale)* | **alto — accesso non verificato** `[R]` | 🔴→🟡 | — | **connettore gestionale fiscale italiano** *(l'asset più prezioso del build)* |
| **Kit AI Act** | — | — | 12 *(= workstream Compliance)* | basso | 🟢 | — | **kit conformità AI Act per studi professionali** *(rivendibile)* |

**Le due regole applicate qui:**
- **A6 non si prezza** finché la verifica non è fatta dentro lo sprint. Se va male,
  non si sconta: **resta fuori dal perimetro** e il sistema continua a funzionare in
  modalità export — è per questo che l'MVP è stato disegnato per non dipenderne.
- **W3 non scrive mai.** Propone un tracciato che un umano importa. L'accuratezza su
  dati contabili critici è il punto dove queste pipeline falliscono `[A]`, e un
  errore di registrazione su un cliente distrugge la fiducia sull'intero sistema.

---

## 6 · Il preventivo + lettura interna

### Strato 0 — Sprint diagnostico *(sempre, prima di tutto)*
```
Ore di catalogo                     = 12 h
  · analisi della call e delle sei domande            3 h
  · VERIFICA ACCESSI (gestionale, PEC, export, Drive) 3 h
  · INVENTARIO SISTEMI AI + classificazione rischio   3 h   ← adempimento art. 4, utile da solo
  · blueprint + monte-ore + preventivo                3 h
Prezzo = 12 × €350                  = €4.200          ← si scala INTEGRALMENTE dall'attivazione
```
> Lo sprint qui ha un argomento di vendita che altrove non c'è: **produce un
> deliverable che lo studio è già obbligato ad avere** (l'inventario dei sistemi AI
> e la classificazione del rischio). Anche se il cliente non procede, ha comprato un
> adempimento. È il miglior sprint del nostro catalogo per tasso di chiusura `[A]`.

### Strato 2 — Attivazione (chiavi in mano)
```
ESSENTIAL   ore catalogo 73  × (1 + 0,25) = 92 h  → 92 × €350  = € 32.200
PRO         ore catalogo 130 × (1 + 0,30) = 169 h → 169 × €350 = € 59.150
PREMIUM     ore catalogo 194 × (1 + 0,30) = 253 h → 253 × €350 = € 88.550
+ infra setup ≈ €400 a costo `[A]`
```

**Buffer e razionale:**
- **Essential 25%** — pattern in larga parte a redeployment, nessuna integrazione
  critica (gira su export e email), scope stretto.
- **Pro / Premium 30%** — mix net-new/redeployment, corpus di knowledge di igiene
  ignota (§5), regole per regime fiscale numerose, tono degli output da calibrare.
- **Buffer di settore 0%** — lo studio professionale non è dominio sanitario. **Il
  lavoro di compliance non sta nel buffer: sta nelle 8–12 h del workstream dedicato**
  (§4.1). Coerente con il precedente Studio Marsili.
- **A6 gestionale: nessun prezzo fisso.** Dopo verifica positiva nello sprint:
  36 h × (1 + 0,40) = 51 h → **≈ €17.850**, *indicativo e non impegnativo*.

### Strato 3 — Canone *(c'è un sistema in produzione → si propone sempre)*
```
Essential  presidio base    2 h/mese × €350 = €   700/mese
Pro        presidio attivo  4 h/mese × €350 = € 1.400/mese
Premium    presidio evolut. 8 h/mese × €350 = € 2.800/mese
Infra pass-through          €150–350/mese `[A]`, a costo, SEPARATA dalla fee di cura
```
Il canone qui è particolarmente difendibile: **la normativa fiscale cambia in
continuazione** e le regole dentro i workflow (scadenze, checklist per regime,
template) vanno mantenute vive. Un sistema di scadenze non aggiornato è peggio che
nessun sistema — argomento onesto e forte contro l'obiezione sull'abbonamento.

### Lettura interna *(non fa il prezzo — decide se conviene)*
```
Tier Pro
Ore reali attese                  ≈  90 h  [A]   (impianto A2/A7 in libreria: −35% sul build)
Costo interno = 90 × €100/h       = € 9.000
Margine attivazione               = €59.150 − €9.000 − €400 = € 49.750
CAPACITÀ (il vincolo vero)        = 169 h di catalogo, ~90 h reali ≈ 2,5 settimane
                                    a tempo pieno in due
Margine canone/mese               = €1.400 − (4 h × €100) = € 1.000
LTV canone (30 mesi, +20% espans.)= 1.000 × 30 × 1,20 = € 36.000
CAC netto = acquisizione €500–1.500 − margine attivazione  → ampiamente ≤ 0   ✅
```
> **Il numero non è il problema: il problema è il peso sul cliente.** Con margine
> ampio e CAC negativo, l'economia dice GO senza esitazioni. Ciò che va gestito è
> tutto dall'altra parte del tavolo → sanity check.

### Sanity check di mercato e peso sul cliente
Il Pro a €59.150 sta **sopra** la banda che il mercato italiano racconta per i
progetti su ecosistemi di automazione (€5–15k per un ecosistema completo `[R]`) e
si colloca in fascia "programma". La distanza è reale e va gestita, non negata: si
difende **solo** con il monte-ore esposto, il presidio continuativo e la conformità
inclusa — mai con "perché è AI".
**Peso sul fatturato dello studio: `n/d`** — è il dato che manca ed è il più
importante. Se il riferimento è **0,5–2% annuo del fatturato** `[R]`, il Pro è
sostenibile solo per uno studio da **€3M+**; sotto, va **sequenziato** (Essential
adesso, Pro a 6–9 mesi) — che è esattamente la raccomandazione della §8.
**Ancoraggio da usare in trattativa `[A]`:** non il costo del software, ma il costo
di **una risorsa junior a tempo pieno** che oggi fa questo lavoro (da farsi dichiarare
in call, non da stimare noi). Il confronto va fatto lì.

### Cosa lascia in libreria
**motore-scadenzario-professionale** · **sollecito-documenti multicanale** ·
**checklist engine per regime fiscale** · **skill pacchetto-cliente-mensile** ·
**parser fatture passive italiane** · **workflow parcellazione & solleciti** ·
**connettore gestionale fiscale italiano** (se A6 si fa) · **kit conformità AI Act
per studi professionali**.
> Sul secondo studio le **ore reali del Build scendono stimate del 40–50%** `[A]`;
> **le ore di catalogo e il prezzo restano identici.** Questo segmento è il candidato
> più forte del nostro portafoglio a diventare **prodotto orizzontale**: due
> fornitori coprono oltre il 70% degli studi `[R]`, quindi un connettore serve un
> mercato enorme, e il ciclo mensile è quasi identico da studio a studio.

### Framing client-facing
Lo studio **non compra software e non noleggia codice**: si abbona a un **sistema
operato** che tiene in piedi il ciclo mensile, non fa cadere una scadenza, rincorre
i clienti al posto dei collaboratori — **e lo fa in una forma che regge l'AI Act e
l'art. 13 della legge italiana**, con la firma del professionista sempre in mezzo.

---

## 7 · Mappa decisionale + obiezioni

| Persona | Tipo | Leva | Ostacolo |
|---|---|---|---|
| **Socio anziano / titolare** | decisore economico | non perdere una scadenza; responsabilità professionale | diffidenza verso l'AI sui dati dei clienti; "l'ho sempre fatto così" |
| **Socio giovane / responsabile contabilità** | champion | liberare i collaboratori, smettere di rincorrere i clienti | non firma |
| **Collaboratore senior** | utente / **potenziale blocco** | meno lavoro odioso | teme di essere sostituito → va coinvolto subito, non informato dopo |
| **Referente interno (`n/d`)** | abilitante | protagonismo | **se non esiste, il canone va alzato e la delivery peggiora** |
| **Consulente privacy / DPO, se c'è** | **blocco tecnico** | conformità documentata | può fermare tutto se lo scopre a progetto fatto → coinvolgerlo nello sprint |

**Strategia di ingaggio in tre mosse:**
1. **Entrare dalla domanda 2**, non dalla tecnologia: "cosa proprio non vorresti
   fare?" — è lì che il titolare si sbilancia e regala la citazione che regge tutto.
2. **Vendere lo sprint come adempimento**, non come consulenza: l'inventario dei
   sistemi AI e la classificazione del rischio sono già dovuti (art. 4 applicabile
   dal 2 febbraio 2025 `[R]`). Il socio anziano compra la messa in regola più
   facilmente di quanto compri l'innovazione.
3. **Partire da Essential**, sempre. Scadenze e solleciti sono il dolore più nudo,
   il go-live più rapido e il caso più facile da mostrare agli altri soci. Il Pro si
   vende dopo, con i dati del sistema stesso in mano.

**Obiezioni attese e contromosse:**
- *"È un abbonamento per un software che compriamo."* → Non è codice: è un sistema
  presidiato in un dominio dove **le regole cambiano ogni anno**. Uno scadenzario
  fermo al 2026 nel 2027 è un rischio professionale, non un risparmio.
- *"E il segreto professionale? I dati dei nostri clienti?"* → Lo studio **resta
  titolare del trattamento e risponde** dell'inserimento dei dati in sistemi non
  conformi `[R]`: proprio per questo il progetto **include** il perimetro dei dati,
  la nomina a responsabile ex art. 28, il no-training e la policy interna. La
  domanda giusta non è "posso usare l'AI", è **"chi sta già usando ChatGPT sui dati
  dei miei clienti senza dirmelo?"** — e quella risposta la dà lo sprint.
- *"Su internet trovo chi me lo fa a 5.000 euro."* `[R]` → Vero, ed è un'offerta
  diversa: quella vende dei workflow, noi vendiamo **un ciclo presidiato con la
  responsabilità professionale dentro**. Se il budget è quello, l'onestà è **togliere
  perimetro** (Essential, un workflow solo), **mai abbassare la tariffa**.
- *"L'AI sbaglia, e sui numeri non me lo posso permettere."* → Concordo, e infatti
  **nessun workflow scrive in contabilità e nessuno invia nulla senza la vostra
  approvazione**. È un requisito di legge prima che una scelta tecnica (art. 13
  L. 132/2025 `[R]`).
- *"Non abbiamo tempo per seguirvi."* → È la domanda giusta: **quante ore a settimana
  potete metterci davvero?** Se sono poche, si va chiavi in mano; se il tempo non c'è
  nemmeno per validare, si rimanda — un progetto senza referente interno non regge.

---

## 8 · Raccomandazione

🟢 **GO sul disegno · 🟡 GO CONDIZIONATO sul dimensionamento.**

**Probabilità di chiusura:** `n/d` sul caso specifico. Di categoria, **media-alta
sull'Essential** e **bassa sul Pro come primo acquisto** `[A]`: il salto di prezzo
rispetto a ciò che il mercato racconta `[R]` è troppo ampio per un primo ingaggio.
**Probabilità di delivery riuscita:** **alta** sull'Essential (nessuna dipendenza da
accessi non verificati, per costruzione) · **media** sul Premium, dove W3 e A6
concentrano tutto il rischio.

**Condizioni-gate — nulla si quota a fisso prima che siano soddisfatte:**
1. **Fare la call.** La §1 è oggi quasi tutta `n/d`: numero di clienti,
   collaboratori, gestionale e fatturato **determinano il monte-ore**. Senza, questo
   è un template, non un preventivo.
2. **Verificare gli accessi** nello sprint (gestionale, PEC, export, Drive). A6 non
   si prezza prima; l'MVP è già disegnato per non dipenderne.
3. **Qualificare il referente interno.** Se non c'è, si alza il presidio del canone
   di un livello e si dichiara il rischio di adozione.
4. **Fissare il go-live fuori dai picchi di scadenza** `[A]`.
5. **Chiudere il perimetro compliance prima del build**, non dopo (Allegato A).

**Prossima azione:** proporre lo **sprint diagnostico a €4.200, scalabile**,
presentandolo come *messa in regola AI Act + blueprint* — non come consulenza
tecnologica. Da lì: **Essential €32.200 + €700/mese** come ingresso, con il Pro
esplicitamente sequenziato a 6–9 mesi (land-and-expand a CAC ≈ 0), e A6 e A1 come
Fase 2 e 3.

**La nota strategica che conta più del singolo deal.** Questo build non vale per il
margine su un cliente: vale perché **il ciclo mensile di uno studio è quasi identico
a quello di ogni altro studio**, due fornitori coprono oltre il 70% del mercato `[R]`
e il **kit di conformità AI Act è vendibile a sé, a ogni professionista italiano,
subito**. Il primo studio va prezzato come net-new; dal secondo in poi questo
diventa il nostro **prodotto orizzontale a più alto potenziale** — e la libreria,
non il singolo preventivo, è il vero deliverable di questo progetto.

---
---

# Allegato A · AI Act — come muoversi per essere in regola

> Questo allegato è **duplice**: è il perimetro di conformità del *nostro* build (le
> 8–12 h del workstream Compliance, §4.1) **ed è il kit che lo studio può rivendere
> ai propri clienti**. Normativa verificata all'11 agosto 2026. Ogni claim `[R]` ha
> la fonte in fondo. **Non è un parere legale**: è la mappa operativa con cui si
> imposta il lavoro e si decide dove serve il legale.

## A.1 · Il calendario reale (aggiornato al Digital Omnibus)

| Data | Cosa si applica | Stato |
|---|---|---|
| 1 ago 2024 | Entrata in vigore dell'AI Act | fatto |
| **2 feb 2025** | **Art. 5 pratiche vietate** + **art. 4 alfabetizzazione IA** | **già applicabile — molti studi sono in ritardo** `[R]` |
| 2 ago 2025 | Obblighi sui modelli GPAI + governance | fatto `[R]` |
| **2 ago 2026** | **Art. 50 trasparenza** · **regime sanzionatorio nazionale (art. 99)** · vigilanza operativa delle autorità | **appena scattato** `[R]` |
| **2 dic 2027** | Alto rischio **Allegato III** (sistemi stand-alone) — **rinviato** dal Digital Omnibus | `[R]` |
| 2 ago 2028 | Alto rischio **Allegato I** (AI nei prodotti regolati) — rinviato | `[R]` |

Il rinvio non è una voce di corridoio: il **Digital Omnibus on AI, Regolamento (UE)
2026/1744**, è stato pubblicato in Gazzetta Ufficiale il **24 luglio 2026** ed è in
vigore dal **27 luglio 2026** `[R]`. **Ha spostato l'alto rischio, non il resto:
l'art. 50 (trasparenza) e l'art. 4 (alfabetizzazione) sono rimasti esattamente dove
erano** `[R]`.

**Italia.** La **legge 132/2025** è in vigore dal **10 ottobre 2025** `[R]`.
**AgID** è autorità di notifica e **ACN** autorità di vigilanza del mercato; Banca
d'Italia, Consob e IVASS vigilano sui sistemi ad alto rischio in ambito finanziario
`[R]`.

**Sanzioni, applicabili dal 2 agosto 2026:** fino a **€35M o 7%** del fatturato
mondiale per le pratiche vietate; fino a **€15M o 3%** per la violazione degli altri
obblighi, trasparenza inclusa; soglie ridotte per le PMI `[R]`.

## A.2 · Il primo chiarimento: che ruolo ha lo studio

Lo studio commercialista è **deployer** (utilizzatore professionale), praticamente
mai fornitore `[R]`. Con **una eccezione da sorvegliare**: se lo studio mette il
proprio marchio su un sistema AI e lo espone ai propri clienti — per esempio un
assistente sul sito o su WhatsApp — **può assumere il ruolo di fornitore** e con
esso obblighi molto più pesanti. È uno dei motivi per cui, in questo progetto,
l'agente verso i clienti (A1) è deliberatamente in **Fase 3** e non nell'MVP.

## A.3 · I workflow di questo progetto sono ad alto rischio? No — ma va scritto

**Nessuno dei workflow W0–W8 rientra nell'Allegato III.** Scadenzari, solleciti,
lettura di fatture, generazione di documenti, promemoria: non sono categorie ad alto
rischio. **Ma la valutazione va fatta e messa per iscritto**, perché è la prova che
si è guardato.

**Le due zone gialle da presidiare in uno studio**, entrambe **fuori perimetro per
scelta esplicita** (§4.3):
- **Selezione del personale** (Allegato III): se lo studio ha un'area paghe/HR o
  supporta i clienti nel recruiting, qualsiasi AI applicata a screening di CV o
  valutazione di candidati **entra nell'alto rischio** — con obblighi che dal
  2 dicembre 2027 diventano pesanti.
- **Merito creditizio delle persone fisiche** (Allegato III): un sistema di scoring
  o di valutazione dell'affidabilità creditizia dei clienti persona fisica ricade
  nella stessa categoria. Analisi di bilancio e indici a supporto del professionista,
  no; uno *scoring che decide*, sì.

> **Il rinvio al 2 dicembre 2027 non è un condono, è tempo.** Chi costruisce oggi un
> sistema in una di queste due aree deve progettarlo già conforme, o riscriverlo dopo.

## A.4 · Cosa scatta davvero: art. 50, dal 2 agosto 2026

La trasparenza si divide fra **chi fornisce** e **chi utilizza** `[R]`:

| Obbligo | Su chi grava | Cosa significa per lo studio |
|---|---|---|
| **Chatbot riconoscibile** — chi interagisce deve sapere che sta parlando con un'AI, salvo che sia evidente | **fornitore** (progettazione) | riguarda lo studio **solo se espone un assistente ai clienti** (Fase 3). L'informazione va data **al più tardi alla prima interazione** `[R]` |
| **Marcatura machine-readable** dei contenuti sintetici (testo, immagini, audio, video) | **fornitore** | lo studio lo eredita dagli strumenti che usa: va **verificato in fase di scelta del fornitore**, non dopo |
| **Deepfake** — dichiarare che immagini/audio/video sono generati o manipolati | **deployer** | rilevante se lo studio produce contenuti di comunicazione con AI generativa |
| **Testi pubblicati per informare il pubblico su temi di interesse pubblico** | **deployer** | **riguarda le circolari e i contenuti divulgativi dello studio.** ⚠️ **Esenzione decisiva: non si applica se il contenuto è passato da revisione umana o controllo editoriale e una persona ne assume la responsabilità editoriale** `[R]` — cioè il flusso di W6, con approvazione del professionista, **è già dentro l'esenzione** |

**Traduzione operativa:** con l'MVP disegnato come in §2 (nessun invio senza
approvazione umana, nessun agente pubblico in Fase 1), **lo studio ha un'esposizione
all'art. 50 molto contenuta**. Diventa rilevante nel momento esatto in cui si accende
l'agente verso i clienti — ed è un altro motivo per cui quella fase va venduta con il
kit di conformità dentro, non separata.

## A.5 · L'obbligo che quasi nessuno ha assolto: art. 4, alfabetizzazione

È **applicabile dal 2 febbraio 2025** `[R]`, quindi **già scaduto**, e riguarda
chiunque usi l'AI professionalmente — **anche chi si limita a usare assistenti
generativi di uso comune** `[R]`. Non è subordinato a soglie di rischio.

Cosa serve concretamente:
1. **Sapere quali strumenti AI entrano nello studio, chi li usa e con quali garanzie
   di supervisione umana** `[R]` — inclusa la **shadow AI**: gli account personali dei
   collaboratori. È il punto da cui partire e quasi sempre il più imbarazzante.
2. Un **percorso di alfabetizzazione documentato e calibrato sui ruoli** `[R]`: socio,
   senior, junior, segreteria non hanno bisogno dello stesso livello. **Non serve un
   livello uniforme** e la norma non impone un livello specifico `[R]`.
3. **Prova documentale**: programma, destinatari, date, materiali, attestati. Senza
   traccia, per un'autorità l'obbligo non è stato assolto.

## A.6 · GDPR e segreto professionale: il livello che morde di più

Nella pratica quotidiana di uno studio, **è qui che si fanno i danni veri**, prima
ancora che nell'AI Act.

- Il commercialista **resta titolare del trattamento** e **risponde dell'inserimento
  dei dati dei clienti in sistemi AI non conformi** `[R]`.
- Il **segreto professionale non sostituisce né deroga** agli obblighi GDPR: registro
  dei trattamenti, misure tecniche e organizzative adeguate, notifica del data breach
  entro **72 ore** `[R]`.
- Emergono **criticità significative con i sistemi AI generalisti** `[R]`: sono il
  punto di rottura più comune — un collaboratore che incolla un bilancio in un
  assistente consumer.
- Ogni fornitore AI va **nominato responsabile del trattamento ex art. 28**, con
  verifica di **no-training sui dati**, ubicazione dei dati e trasferimenti extra-UE.
- Dove il trattamento presenta rischi elevati, serve **integrare la DPIA** `[R]`.

## A.7 · L'obbligo italiano specifico: art. 13 L. 132/2025

Applicabile alle professioni intellettuali, commercialisti inclusi `[R]`, in vigore
dal 10 ottobre 2025:

1. **L'AI è solo strumento di supporto e assistenza**: non può sostituire l'apporto
   personale e critico del professionista. **Il lavoro intellettuale umano deve
   mantenere ruolo prevalente e determinante** nella prestazione `[R]`.
2. **Obbligo di informare preventivamente il cliente** sull'uso di strumenti AI, in
   modo **chiaro, semplice ed esaustivo**, a tutela della trasparenza e del rapporto
   fiduciario `[R]`.

**Come si adempie, concretamente:** una **clausola informativa nella lettera
d'incarico** (per i nuovi incarichi) più una **comunicazione una tantum** ai clienti
in essere, che dica *quali* strumenti si usano, *per cosa*, e che **la responsabilità
professionale e la validazione restano del professionista**. È un testo breve, si
scrive una volta, e nel nostro build è **dentro il workstream Compliance**.

## A.8 · Il piano in 10 mosse

| # | Mossa | Chi | Quando | Prova che resta |
|---|---|---|---|---|
| 1 | **Inventario dei sistemi AI** in uso, shadow AI inclusa | referente interno + noi | sprint | registro dei sistemi AI |
| 2 | **Classificazione del rischio** per sistema (vietato / alto / trasparenza / minimo) con motivazione | noi | sprint | scheda di valutazione firmata |
| 3 | **Determinare il ruolo**: deployer o fornitore (attenzione al rebranding di un agente) | noi | sprint | nota di ruolo |
| 4 | **Piano di alfabetizzazione art. 4** calibrato per ruolo | studio + noi | entro 60 gg | programma, registro presenze, attestati |
| 5 | **Policy d'uso interno**: strumenti approvati, divieto di sistemi consumer sui dati dei clienti | studio + noi | prima del go-live | policy firmata dai collaboratori |
| 6 | **Informativa art. 13** in lettera d'incarico + comunicazione ai clienti in essere | studio (testo nostro) | prima del go-live | modello + evidenza di invio |
| 7 | **Adeguamento GDPR**: registro trattamenti, nomine art. 28, no-training, extra-UE, DPIA dove serve | studio/DPO + noi | prima del go-live | registro aggiornato, contratti |
| 8 | **Supervisione umana e logging** dentro ogni workflow: nulla esce senza approvazione, ogni esecuzione è tracciata | noi | build | log + schema di approvazione |
| 9 | **Trasparenza art. 50** dove pertinente: dichiarazione AI sul canale conversazionale, disclosure sui contenuti generati | noi | alla Fase 3 | evidenze sul canale |
| 10 | **Riesame semestrale** + aggiornamento in vista del **2 dicembre 2027** | studio + noi (canone) | ricorrente | verbale di riesame |

> Le mosse **1, 2, 3, 8** e **9** sono **dentro il nostro workstream Compliance**
> (8–12 h). Le mosse **4, 5, 6, 7** sono dello studio, con i nostri modelli. La **10**
> è una delle ragioni per cui il canone esiste.

## A.9 · La lettura commerciale: la compliance è un ricavo, non un costo

Ogni cliente di quello studio — **ogni impresa italiana che usa l'AI** — ha gli
stessi obblighi: inventario, classificazione del rischio, alfabetizzazione art. 4,
policy, informative. Uno studio che si è messo in regola sul serio possiede **il
metodo, i modelli e la prova che funziona**, e può offrirlo come **nuovo servizio ai
propri clienti**.

Per noi questo cambia due cose:
1. **Nella vendita:** l'adeguamento smette di essere un costo da giustificare e
   diventa un **investimento con un ritorno diretto e dimostrabile**. È l'argomento
   più forte che abbiamo contro l'obiezione sul prezzo, e non richiede di scontare
   nulla.
2. **Nella libreria:** il **kit conformità AI Act per studi professionali** è un
   asset a sé, **vendibile separatamente e a costo marginale quasi nullo dal secondo
   cliente in poi**. Va costruito una volta, bene, in questo progetto.

---

## Fonti `[R]`

- [AI Act: che cosa cambia davvero dal 2 agosto 2026 per imprese e professionisti — Altalex](https://www.altalex.com/documents/2026/07/31/act-cambia-davvero-2-agosto-2026-imprese-professionisti)
- [AI Act, dal 2 agosto debuttano la vigilanza e i doveri di trasparenza — Il Sole 24 Ore](https://www.ilsole24ore.com/art/ai-act-2-agosto-debuttano-vigilanza-e-doveri-trasparenza-AJtYEMV)
- [Art. 50 AI Act, la trasparenza diventa operativa: cosa cambia dal 2 agosto — Agenda Digitale](https://www.agendadigitale.eu/sicurezza/art-50-ai-act-la-trasparenza-diventa-operativa-cosa-cambia-dal-2-agosto/)
- [Articolo 50 AI Act: obblighi di trasparenza e ripartizione delle responsabilità tra provider e deployer — Iusletter](https://iusletter.com/dalla-redazione/intelligenza-artificiale/articolo-50-ai-act-obblighi-di-trasparenza-e-ripartizione-delle-responsabilita-tra-provider-e-deployer/)
- [Deepfake e testo generato dall'AI: nuove regole dal 2 agosto 2026 — Diritto al Digitale](https://dirittoaldigitale.com/2026/08/07/deep-fake-ai-ai-act-deployer/)
- [The Digital Omnibus and the postponement of high-risk obligations to December 2027](https://www.aiactblog.nl/en/posts/digital-omnibus-high-risk-postponement-december-2027)
- [EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines and Other Key Changes — Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [Digital Omnibus on AI: il Consiglio adotta il Regolamento di semplificazione dell'AI Act — ADVANT Nctm](https://www.advant-nctm.com/en/news/digital-omnibus-on-ai-il-consiglio-adotta-il-regolamento-di-semplificazione-dellai-act)
- [AI Act, il 2 agosto 2026 e l'obbligo di alfabetizzazione IA: la guida per i professionisti — LavoriPubblici](https://www.lavoripubblici.it/news/ai-act-2-agosto-2026-alfabetizzazione-ia-professionisti-38446)
- [Alfabetizzazione IA (art. 4 AI Act): l'obbligo che studi e aziende hanno già dal 2025](https://www.giacomopiva.com/alfabetizzazione-ia-art-4-ai-act/)
- [Il Consiglio dei Ministri approva i decreti di adeguamento all'AI Act — Federprivacy](https://www.federprivacy.org/informazione/flash-news/il-consiglio-dei-ministri-ha-approvato-i-decreti-di-adeguamento-della-normativa-nazionale-all-artificial-intelligence-act)
- [AI Act a regime dal 2 agosto 2026 con sanzioni e obblighi di trasparenza — Studio Teruzzi](https://www.studioteruzzi.it/ai-act-a-regime-dal-2-agosto-2026-con-sanzioni-e-obblighi-di-trasparenza/)
- [Legge n. 132/2025. Intelligenza artificiale nelle professioni solo di supporto — art. 13 — Finanza & Fisco](https://www.finanzaefisco.com/legge-132-2025-ia-professioni-dal-10-ottobre/)
- [Professionisti e uso dell'AI: dubbi alla luce dell'art. 13 della Legge 132/2025 — Altalex](https://www.altalex.com/documents/2025/10/29/professionisti-uso-ai-tanti-dubbi-poche-certezze-luce-art-13-legge-132-2025)
- [AI e privacy negli studi professionali: profili critici nell'uso dei sistemi generalisti — EC News](https://www.ecnews.it/fiscale/mondo-professione/digitalizzazione/ai-e-privacy-negli-studi-professionali-profili-critici-e-rischi-privacy-nelluso-dei-sistemi-generalisti/)
- [La gestione della privacy negli studi professionali — CNDCEC, informativa n. 52/2026 (PDF)](https://commercialisti.it/wp-content/uploads/2026/03/All.-info-n.-52-2026.pdf)
- [Software Commercialisti 2026: AI, Gestionali e Tool a Confronto — Scadero](https://scadero.it/blog/software-commercialisti-2026-ai-gestionali-confronto/)
- [AI gestionali italiani: TeamSystem vs Zucchetti 2026 — Luca Sammarco](https://lucasammarco.com/blog/ai-gestionali-italiani-teamsystem-zucchetti-2026)
- [Digitalizzazione dei commercialisti: evoluzioni e trend 2026 — DATALOG](https://www.datalog.it/commercialisti-2026-trend/)
- [7 Automazioni AI per PMI: casi reali, costi e ROI (2026) — Castaldo Solutions](https://www.castaldosolutions.it/articles/blog/automazione-ai-pmi-italia)
- [Costi della consulenza AI: range, modelli, cosa influenza il prezzo — Soraia](https://www.soraia.io/guide/costi-consulenza-ai/)

---
*Handoff: questo dossier, una volta validato e corretto — e **soprattutto una volta
riempita la §1 con una call vera** — alimenta `ai-solution-proposal`, che filtra
buffer, margini, ore reali, LTV/CAC, rischi interni e nomi di workflow, e mostra al
cliente solo tier, prezzi in chiaro, valore e percorso nella brochure full-bleed.* 🌶️
