import json
SPAZIO="https://brave-vet-business.circle.so/c/spazio-di-confronto"
MAT="https://brave-vet-business.circle.so/c/materiale-d-aula-38f6ea"
def embed(vid,title):
    return (f'<p><strong>▶ GUARDA IL VIDEO: <a href="https://www.youtube.com/watch?v={vid}">{title}</a></strong></p>'
            f'<p>Il video si apre su YouTube in una nuova scheda (link riservato ai partecipanti, non condividerlo all\'esterno). Guardalo per intero, poi torna qui per le note e l\'esercizio.</p>')
def video_lesson(n,vid,title,dur,focus,why,action,next_):
    h=f'<h2>{title}</h2><p><strong>Durata:</strong> {dur} · <strong>Lezione {n} di 7</strong></p>'
    h+=embed(vid,title)
    h+='<h3>Su cosa concentrarti</h3><ul>'+''.join(f'<li>{x}</li>' for x in focus)+'</ul>'
    h+=f'<h3>Perché ti serve nel sistema agentico</h3><p>{why}</p>'
    h+=f'<h3>Prima di proseguire (5 minuti)</h3><p>{action}</p>'
    h+=f'<p><em>Prossima lezione:</em> {next_}</p>'
    h+=f'<p>Domande o passaggi poco chiari? Scrivili nei commenti qui sotto oppure nello <a href="{SPAZIO}">Spazio di confronto</a>.</p>'
    return h
L=[]
# Section: Prima di iniziare
L.append(dict(section="intro",name="Guida al percorso: come usare questo video corso",body=
'<h2>N8N per la Clinica Veterinaria</h2>'
'<p>Questo video corso è il tassello che serve per capire <strong>a cosa serve n8n</strong>, <strong>come funziona</strong> e <strong>come lo integreremo nel sistema agentico</strong> che stiamo costruendo insieme nel Super Master AI. Sono 7 video per circa 75 minuti complessivi, pensati per essere guardati in ordine.</p>'
'<h3>Il percorso</h3>'
'<p><strong>Modulo 1 · Capire n8n</strong></p><ol><li>N8N: basi e utilizzo in clinica (19:07)</li><li>Introduzione a n8n e panoramica iniziale (5:05)</li><li>L\'interfaccia di n8n: panoramica (7:24)</li></ol>'
'<p><strong>Modulo 2 · Costruire il primo workflow</strong></p><ol start="4"><li>Creare il primo workflow su n8n (9:35)</li><li>Configurare un workflow in n8n (8:52)</li></ol>'
'<p><strong>Modulo 3 · n8n e Claude nel sistema agentico</strong></p><ol start="6"><li>Connettere Claude e n8n (6:02)</li><li>Creare un servizio veterinario con l\'IA (18:49)</li></ol>'
'<p><strong>Materiali a supporto</strong>: glossario essenziale, quattro automazioni dalla clinica, checklist per il primo workflow, domande e prossimi passi.</p>'
'<h3>Come guardarlo</h3><ul><li><strong>Un modulo per volta.</strong> Il Modulo 1 spiega il "perché" e il "cosa": guardalo anche se non hai intenzione di costruire nulla da solo. I Moduli 2 e 3 sono operativi: tienili per quando hai il computer davanti.</li><li><strong>Taccuino aperto.</strong> Ad ogni video annota una sola cosa: un\'attività ripetitiva della tua clinica che quel passaggio potrebbe automatizzare.</li><li><strong>Nessun prerequisito tecnico.</strong> Non serve scrivere codice. Se sai descrivere una procedura a una persona nuova, sai già progettare un workflow.</li></ul>'
'<h3>Cosa ti serve per la parte pratica</h3><ul><li>Un account n8n Cloud (la prova gratuita è sufficiente per seguire i video).</li><li>Un account Claude, per il Modulo 3.</li><li>Un processo reale della tua clinica da usare come banco di prova: un promemoria, una richiesta in entrata, un report.</li></ul>'
'<h3>La domanda da portarsi a casa</h3><p><em>Quali attività della tua clinica stai ancora pagando a tariffa medica, pur sapendo che si ripetono identiche ogni settimana?</em></p>'
f'<p>Le domande vanno nei commenti di ogni lezione oppure nello <a href="{SPAZIO}">Spazio di confronto</a>: rispondiamo a tutti e portiamo i casi reali in aula.</p>'))
# Modulo 1
L.append(dict(section="m1",name="01 · N8N: basi e utilizzo in clinica",body=video_lesson(1,"-eQG7texouE","N8N: basi e utilizzo in clinica","19:07",
 ["Il problema che n8n risolve: il lavoro ripetitivo che nessuno fattura (promemoria, richieste da quattro canali, ricopiature, report a mano).",
  "Le tre parole da portarsi a casa: <strong>trigger</strong> (il momento), <strong>nodo</strong> (l'azione), <strong>workflow</strong> (la procedura).",
  "Cosa n8n non è: non è un gestionale e non decide al posto tuo. Esegue procedure che hai deciso tu.",
  "Dove gira: n8n Cloud per partire, self-hosted quando serve tenere i dati in casa."],
 "È la lezione di fondazione. Tutto il sistema agentico della clinica (Claude che ragiona, il gestionale che fornisce i dati, Brevo e WhatsApp che comunicano, Circle che forma) ha bisogno di un motore che colleghi i pezzi e li faccia partire al momento giusto. Quel motore è n8n.",
 "Scrivi su un foglio tre attività che in clinica si ripetono identiche ogni settimana. Accanto a ciascuna segna: quando parte (il trigger) e dove finisce il dato (il risultato). Le userai nel Modulo 2.",
 "02 · Introduzione a n8n e panoramica iniziale")))
L.append(dict(section="m1",name="02 · Introduzione a n8n e panoramica iniziale",body=video_lesson(2,"0Kf4UxL-vaM","Introduzione a n8n e panoramica iniziale","5:05",
 ["Come si presenta n8n al primo accesso e come sono organizzati workflow, esecuzioni e credenziali.",
  "La logica a riquadri collegati da linee: si legge come un diagramma di flusso, non come un programma.",
  "La differenza fra costruire un workflow e attivarlo (metterlo in produzione)."],
 "Prima di costruire qualsiasi automazione devi saper leggere un workflow altrui: nel Super Master AI riceverai workflow già pronti da importare e adattare alla tua clinica, e questa panoramica ti dà il vocabolario per capirli.",
 "Se non l'hai ancora fatto, crea il tuo account n8n Cloud e apri l'area di lavoro vuota. Non costruire nulla: guarda solo dove sono i tre menu che il video ti mostra.",
 "03 · L'interfaccia di n8n: panoramica")))
L.append(dict(section="m1",name="03 · L'interfaccia di n8n: panoramica",body=video_lesson(3,"vRhCuxS-SCg","Panoramica e introduzione all'interfaccia di n8n","7:24",
 ["La tela (canvas) dove si trascinano i nodi e come si collegano fra loro.",
  "Il pannello di un nodo: parametri, input a sinistra, output a destra.",
  "Dove vedere i dati che passano da un nodo all'altro e come rileggere un'esecuzione.",
  "Dove si salvano le credenziali dei servizi collegati (posta, fogli, WhatsApp, Claude)."],
 "Nel sistema agentico ogni nodo è un gesto della clinica: leggi un foglio, manda un messaggio, chiedi a Claude, aggiorna il gestionale. Capire dove entrano ed escono i dati è ciò che ti permette di capire perché un'automazione funziona o si ferma.",
 "Apri un workflow di esempio dalla libreria di n8n (una qualsiasi automazione con Gmail o Google Sheets) e, senza eseguirlo, individua: il trigger, il primo nodo, l'ultimo nodo e dove finisce il dato.",
 "04 · Creare il primo workflow su n8n")))
# Modulo 2
L.append(dict(section="m2",name="04 · Creare il primo workflow su n8n",body=video_lesson(4,"kyx1sIf21DQ","Creare il primo workflow su N8n","9:35",
 ["Partire da un trigger e aggiungere i nodi uno alla volta.",
  "Eseguire il workflow in prova e leggere il risultato di ogni passaggio.",
  "Il principio guida delle prime settimane: il primo workflow serve a imparare, non a risolvere il problema più grande della clinica."],
 "Il 70% delle automazioni utili in clinica ha la stessa forma: arriva qualcosa, si scrive una riga, si manda una conferma, si avvisa una persona. Quattro riquadri. Costruirne uno con le tue mani ti toglie la paura e ti fa capire cosa chiedere quando lo faremo insieme.",
 "Riprendi le tre attività annotate nella lezione 01 e scegli la più noiosa: bassa importanza clinica, alta frequenza. Scrivila in dieci righe come procedura: quando parte, cosa fa, dove finisce il dato.",
 "05 · Configurare un workflow in n8n")))
L.append(dict(section="m2",name="05 · Configurare un workflow in n8n",body=video_lesson(5,"LALAend8B-Y","Configurazione di un workflow in n8n","8:52",
 ["Impostare i parametri di un nodo e collegare le credenziali del servizio.",
  "Passare i dati da un nodo al successivo (le espressioni che leggono i campi in ingresso).",
  "Gestire l'errore più comune: un dato mancante o scritto male a monte che fa fallire il passaggio a valle.",
  "Attivare il workflow e verificare le esecuzioni."],
 "Le automazioni sbagliate sbagliano più in fretta. Se l'anagrafica è incompleta, i messaggi automatici arrivano sbagliati a tutti insieme: per questo nel percorso lavoriamo prima sull'ordine dei dati e poi sull'automazione. Questa lezione ti mostra dove, in pratica, un workflow si rompe.",
 "Nel workflow di prova della lezione 04 cambia un parametro (un indirizzo email, il nome di un foglio) e osserva come cambia l'output. Poi rimettilo a posto. Serve a perdere la paura di toccare le impostazioni.",
 "06 · Connettere Claude e n8n")))
# Modulo 3
L.append(dict(section="m3",name="06 · Connettere Claude e n8n",body=video_lesson(6,"N4i3BgmdBSo","Come connettere Claude e n8n con successo","6:02",
 ["Come si collega Claude a n8n tramite credenziale API.",
  "Cosa fa un nodo di intelligenza artificiale dentro un workflow: riceve un testo, ragiona secondo le istruzioni che gli dai, restituisce un risultato strutturato.",
  "Le istruzioni (prompt) come parte della procedura: vanno scritte con la stessa cura della procedura stessa."],
 "È il punto d'incontro fra i due mondi del Super Master AI: Claude ragiona, n8n esegue. Con questa connessione una mail in entrata può essere classificata (urgenza, appuntamento, fornitore, spam), smistata e risposta in bozza. Regola da tenere: l'automazione prepara, la persona firma.",
 "Recupera la chiave API del tuo account Claude e salvala come credenziale in n8n, seguendo il video. Non costruire ancora il workflow: assicurati solo che la connessione risulti valida.",
 "07 · Creare un servizio veterinario con l'IA")))
L.append(dict(section="m3",name="07 · Creare un servizio veterinario con l'IA",body=video_lesson(7,"uZkpLQGWow8","Creare un servizio veterinario con l'IA","18:49",
 ["Come si passa da un'idea di servizio a un workflow completo: trigger, raccolta dati, ragionamento di Claude, risposta al cliente, registrazione.",
  "Dove mettere il controllo umano: su tutto ciò che è clinico o economico l'ultimo passaggio resta a una persona.",
  "Come misurare il risultato: non il messaggio automatico in sé, ma il numero di richieste gestite, il tempo di prima risposta, le scadenze che non escono più dal radar."],
 "Questa lezione è il modello di ciò che costruiremo in aula per la tua clinica: un servizio che parte da un evento reale (una richiesta, una scadenza, una visita completata), coinvolge Claude dove serve giudizio e usa n8n per far accadere le cose nei sistemi che già usi.",
 "Descrivi in mezza pagina il servizio che vorresti offrire ai tuoi clienti con questa architettura. Rispondi a tre domande: quale evento lo fa partire, cosa deve decidere Claude, chi firma prima che il cliente riceva qualcosa. Portalo in aula o pubblicalo nello Spazio di confronto.",
 f"hai completato il percorso. Passa ai <a href=\"{MAT}\">materiali a supporto</a> e alla checklist per il primo workflow.")))
# Materiali a supporto
L.append(dict(section="sup",name="Glossario essenziale di n8n",body=
'<h2>Glossario essenziale di n8n</h2><p>Le parole che sentirai nei video e che useremo in aula, spiegate con esempi presi dalla clinica.</p>'
'<ul>'
'<li><strong>Workflow</strong>: la procedura della clinica scritta in modo eseguibile. Una catena di nodi che parte da un trigger e arriva a un risultato.</li>'
'<li><strong>Trigger</strong>: l\'evento che fa partire tutto. Un modulo compilato sul sito, una mail ricevuta, le 8 del mattino di lunedì, una riga nuova in un foglio.</li>'
'<li><strong>Nodo</strong>: un singolo gesto. Leggi un foglio, invia un messaggio WhatsApp, chiedi a Claude, aggiorna il gestionale.</li>'
'<li><strong>Esecuzione</strong>: una singola corsa del workflow, dal trigger alla fine. Ogni esecuzione resta registrata e si può rileggere passo per passo.</li>'
'<li><strong>Credenziale</strong>: l\'accesso salvato a un servizio esterno (Gmail, Google Sheets, Brevo, Claude). Si configura una volta e si riusa in tutti i workflow.</li>'
'<li><strong>Webhook</strong>: un indirizzo che n8n espone per ricevere dati da altri sistemi. È il modo con cui il sito, il gestionale o un modulo "bussano" al workflow.</li>'
'<li><strong>Espressione</strong>: la piccola formula con cui un nodo legge un dato prodotto dal nodo precedente (per esempio il nome del proprietario o la data della scadenza).</li>'
'<li><strong>Nodo AI</strong>: un nodo che passa un testo a un modello come Claude con delle istruzioni e ne riceve il risultato. Serve dove c\'è da capire, classificare o scrivere una bozza.</li>'
'<li><strong>Attivo / Inattivo</strong>: un workflow attivo risponde ai trigger da solo, anche a studio chiuso. Uno inattivo parte solo quando lo esegui a mano.</li>'
'<li><strong>n8n Cloud / Self-hosted</strong>: nel primo caso lavori dal browser senza server; nel secondo n8n è installato su un tuo server. Il modo di costruire i workflow è identico.</li>'
'</ul>'))
L.append(dict(section="sup",name="Quattro automazioni dalla clinica",body=
'<h2>Quattro automazioni dalla clinica</h2><p>Gli esempi su cui ragioniamo in aula. Per ciascuno: cosa fa il workflow e cosa cambia in clinica.</p>'
'<h3>1. Il richiamo vaccinale che si ricorda da solo</h3><p><strong>Ogni notte</strong> controlla le scadenze dei prossimi trenta giorni → <strong>prepara</strong> un messaggio con nome dell\'animale e data → <strong>invia</strong> WhatsApp o email al proprietario → <strong>registra</strong> chi ha risposto e chi va richiamato.</p><p><em>Prima:</em> la reception se ne ricorda quando può. <em>Dopo:</em> nessuna scadenza esce dal radar.</p>'
'<h3>2. Le richieste che arrivano da quattro canali diversi</h3><p>Raccoglie modulo del sito, messaggi social, WhatsApp e mail in un unico elenco con data, canale e stato. Manda una risposta immediata al proprietario e assegna la richiesta a chi è di turno.</p><p><em>Cosa cambia:</em> tempo di prima risposta sotto il minuto anche a studio chiuso, un solo posto da guardare la mattina, e finalmente il numero delle richieste che prima nessuno contava.</p>'
'<h3>3. Quando dentro il workflow entra l\'intelligenza artificiale</h3><p>Arriva una mail nella casella della clinica → un <strong>nodo AI</strong> capisce se è urgenza, appuntamento, fornitore o spam → <strong>smista</strong>: urgenze in chat al medico, il resto in coda → <strong>propone</strong> una bozza di risposta che una persona approva.</p><p><em>Regola da tenere:</em> l\'automazione prepara, la persona firma. Su tutto ciò che è clinico o economico l\'ultimo passaggio resta umano.</p>'
'<h3>4. Il report del lunedì che nessuno deve preparare</h3><p><strong>Legge</strong> incassi, visite, nuovi clienti e richieste della settimana dai sistemi che già usi → <strong>confronta</strong> con la settimana precedente e con lo stesso periodo dell\'anno scorso → <strong>invia</strong> una pagina sola, in chat o per mail, lunedì alle otto.</p><p>Una struttura che riceve i propri numeri ogni settimana prende decisioni diverse da una che li guarda a fine anno.</p>'
'<h3>Cosa n8n può collegare</h3><ul><li>Posta e agenda: Gmail, Outlook, Google Calendar</li><li>Fogli e archivi: Sheets, Excel, Drive, database</li><li>Messaggistica: WhatsApp Business, Telegram, SMS</li><li>Email marketing: Brevo, moduli web</li><li>Intelligenza artificiale: Claude, trascrizione audio</li><li>Gestionali con API o webhook, pagamenti e fatturazione, documenti e referti</li></ul>'))
L.append(dict(section="sup",name="Checklist: il tuo primo workflow in clinica",body=
'<h2>Checklist: il tuo primo workflow in clinica</h2><p>Tre passi che puoi fare questa settimana, senza comprare nulla, e i tre errori da evitare.</p>'
'<h3>Passo uno · Conta le ripetizioni</h3><p>Per cinque giorni annota ogni operazione che fai più di tre volte a settimana. Chi la fa, quanto dura, da dove arriva il dato, dove finisce.</p>'
'<h3>Passo due · Scegline una noiosa</h3><p>Bassa importanza clinica, alta frequenza: è il candidato perfetto per il primo workflow. Non partire dal processo più complicato.</p>'
'<h3>Passo tre · Scrivila come procedura</h3><p>Quando parte, cosa deve fare, dove finisce il dato. Se sta in dieci righe, n8n la può eseguire.</p>'
'<h3>Gli errori delle prime settimane</h3><ol><li><strong>Partire dal processo più complicato.</strong> Il primo workflow serve a imparare, non a risolvere il problema più grande della clinica.</li><li><strong>Automatizzare il disordine.</strong> Se l\'anagrafica è incompleta, i messaggi automatici arrivano sbagliati a tutti insieme.</li><li><strong>Non dirlo alla squadra.</strong> Un\'automazione che nessuno sa di avere viene scavalcata a mano entro una settimana.</li></ol>'
'<h3>Prima di attivare</h3><ul><li>Ho provato il workflow su un caso finto e su un caso reale mio.</li><li>Ho deciso chi controlla il risultato la prima settimana.</li><li>Il team sa che esiste, cosa fa e chi chiamare se qualcosa non torna.</li><li>Su ciò che è clinico o economico, l\'ultimo passaggio lo firma una persona.</li></ul>'
'<p>Automatizzare non significa togliere persone: significa spostarle dove servono, cioè davanti al cliente e all\'animale.</p>'))
L.append(dict(section="sup",name="Domande, supporto e prossimi passi",body=
'<h2>Domande, supporto e prossimi passi</h2>'
f'<h3>Dove fare domande</h3><p>Nei commenti di ogni lezione, per i dubbi legati a quel video, oppure nello <a href="{SPAZIO}">Spazio di confronto</a> per tutto il resto. Rispondiamo a tutti e i casi più interessanti diventano esercitazioni in aula.</p>'
'<h3>Come chiedere aiuto in modo utile</h3><ul><li>Di\' quale lezione stavi seguendo e a che minuto.</li><li>Descrivi cosa ti aspettavi e cosa è successo invece.</li><li>Se il workflow si ferma, allega uno screenshot del nodo in errore.</li></ul>'
'<h3>Cosa portare al prossimo incontro</h3><ol><li>Le tre attività ripetitive annotate nella lezione 01.</li><li>La procedura in dieci righe scritta nella lezione 04.</li><li>La mezza pagina sul servizio con l\'IA scritta nella lezione 07.</li></ol>'
f'<p>Con questi tre fogli in mano costruiremo insieme il primo workflow della tua clinica. Tutti i materiali restano disponibili qui, nello spazio <a href="{MAT}">Materiale d\'aula</a>.</p>'))
json.dump(L,open('/tmp/claude-0/-home-user-ai-activation/1f29f099-a0b3-5813-9027-99f4fb3c6ae5/scratchpad/lessons.json','w'),ensure_ascii=False,indent=1)
for l in L: print(l['section'], '|', l['name'], '|', len(l['body']))
