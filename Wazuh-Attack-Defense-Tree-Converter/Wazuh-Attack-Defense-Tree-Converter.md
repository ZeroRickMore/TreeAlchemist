Idea: Creare un software che converta Attack-Defense Trees in regole e active responses comprese da Wazuh

NOTE DI SVILUPPO:

ADTCVT == Attack Defense Tree ConVerTed

user_{} == Attributi che DEVONO essere in INPUT dall'UTENTE

system_{} == Attributi che DEVONO essere CALCOLATI da SISTEMA

Attributi senza quel prefisso sono sia calcolabili che da input

# 1 - Leggere e validare il file .xml dell'ADT in input

Il file è scritto secondo la sintassi di [./ADT-syntax.md].
Quello che devo fare è mappare le variabili che stanno descritte allo step 3, in modo da poter generare le regole.

L'idea potrebbe essere:

ADT_xml_parser.py -> 

    Script che fa il parsing del file xml e salva i dati nelle giuste variabili. 
    Per ogni tag, interroga wazuh_tags_validator e vede se funziona.
    Realisticamente, salverò i contenuti in un dizionario {str : list} al quale poi attingerà ADT_rules_generator.py

wazuh_tags_validator.py ->

    Per ogni tag, ho un metodo "validate_[tagname]()" che prende in input il contenuto di quel tag e ne verifica la validità. Ad esempio, se dovrei avere un IPv4, il metodo validate sarà una regex su un IPv4.
    Se ci sono problemi, si ferma il programma lanciando un errore, che riporrà nel file error_logs.txt . In caso di warning (sintassi sbagliata ma accettabile), riporrà il warning dentro warning_logs.txt .
    
ADT_rules_generator.py -> 
    a partire da quel dizionario, filla i campi del TEMPLATE REGOLE che troviamo al punto 3.


# 2 - Creare {numero_prima_regola}-ADTCVT-{nome_root_ADT}.xml

Creazione del file:

numero_prima_regola == il numero, per l'appunto, della primissima regola custom inserita nel file. 
Convenzione inventata da me.

rome_root_ADT == il nome del nodo radice dell'ADT, che rappresenta anche l'intero albero in sé e la minaccia.

# 3 - Dentro quel file, le regole.

Dentro quel file, vanno inserite le regole a partire da quello che l'utente fornisce.
In particolare, la sintassi per l'utente è definita in [./ADT-syntax.md]
NOTA: Una regola rappresenta un nodo dell'ADT.

TEMPLATE REGOLE:
<group name="{nome_root_ADT-senza-underscore}, ADTCVT"> 
    <rule level="{threat_level}" id="{rule_id}" frequency="{user_frequency}" timeframe="{user_timeframe}" ignore="{user_ignore}">
    <match negate="{user_match_negate}" type="{user_match_type}">{user_match}</match>
    <regex negate="{user_regex_negate}" type="{user_regex_type}">
    {user_regex}</regex>
    <srcip negate="{user_srcip_negate}">{user_srcip}</srcip>
    <dstip negate="{user_dstip_negate}">{user_dstip}</dstip>
    <srcport negate="{user_srcport_negate}" type="{user_srcport_type}">{user_srcport}</srcport>
    <dstport negate="{user_dstport_negate}" type="{user_dstport_type}">{user_dstport}</dstport>
    <time>{user_time}</time>
    <weekday>{user_weekday}</weekday>
    <if_sid>{system_if_sid}<if_sid>
    <same_srcip />
    <different_srcip />
    <same_srcport />
    <different_srcport />
    <different_dstport />
    <same_location />
    <same_srcuser />
    <different_srcuser />
    <description>{user_desc}</description>
    <description>Launching [{nome-nodo == nome-script-difensivo}] defense script on [{location_in_active_response_tag}].</description>
    <info type="{user_info_type}">{user_info}</info>
    <options>{user_options}</options>
</group>



======================================================
SPIEGAZIONE DI TUTTI I TAG E I PARAMETRI TRA GRAFFE

------ <group> ------   USER + SYSTEM REQUIRED

- nome_root_ADT-senza-underscore-camel-case == è più carino da leggere cosi
    USER REQUIRED (sta dentro <name> di <node root="yes" />)

- ADTCVT == Vorrei che le regole nate da questo script siano tutte in questo gruppo
    SYSTEM REQUIRED

------ </group> ------



------ <rule> ------

- threat_level == Può deciderlo l'utente, oppure lo automatizzo in base alla profondità dell'albero.
Più sto verso la radice, più è problematico! Potrei ad esempio fare
max(3, 17 - distanza_da_root)
Questo perché:
Max lvl = 16
Se sono accanto a root, faccio 17-1 = 16 MAX ALERT LVL
Man mano che mi allontano, diminuisce il livello di alert
Se l'albero è enorme e ha 15+ nodi, vado sotto il livello di alert 3, ma vorrei che il livello di alert fosse almeno 3 per mia convenzione, quindi uso la funzione max
    USER/SYSTEM REQUIRED

- rule_id == Non decidibile dall'utente, lo scripto per essere crescente a partire dal primissimo disponibile sopra il 100000 (compreso).
Inserire controlli per non duplicare le regole per utenti che non usano il mio script. Magari potrei fare uno script che fa grep e cerca per ogni step il numero della regola?
    USER/SYSTEM REQUIRED

- user_frequency == Decidibile dall'utente, non saprei come si rappresenta sull'ADT però.
No default
    USER OPTIONAL


- user_timeframe == Decidibile dall'utente, legato al nodo, è il te
No default
    USER OPTIONAL

- user_ignore == Decidibile dall'utente, è il tempo per cui, una volta generata un'alert in modo esplicito nella dashboard, la dashboard evita di risollevare l'alert (ma comunque fa il loggin dell'alert)
No default
    USER OPTIONAL

------ </rule> ------



------ <match> ------ USER OPTIONAL

- user_match_negate == Decide se negare lo string literal. Quindi l'alert è sollevata esclusivamente se NON trova lo string literal.
Default value "no"
    

- user_match_type == Imposta il tipo di regex.
Default value "osmatch"

- user_match == Nel file di log, cerca uno string literal e in caso lo trova triggera la regola (più veloce di Regex)
No default

------ </match> ------ USER OPTIONAL



------ <regex> ------ USER OPTIONAL

- user_regex_negate == Decide se negare la regex. Quindi l'alert è sollevata esclusivamente se NON trova la regex.
Default value "no"

- user_regex_type == Imposta il tipo di regex.
Default value "osmatch"

- user_regex == Nel file di log, cerca una regex e in caso lo trova triggera la regola (più veloce di Regex)
No default

------ </regex> ------



------ <srcip> ------ USER OPTIONAL (repeatable)

- user_srcip_negate == Trigger se NON vede quell'IP
Default value "no"

- user_srcip == Trigger se VEDE quell'IP
No default

----- </srcip> ------ 



------ <dstip> ------ USER OPTIONAL (repeatable)

- user_dstip_negate == Trigger se NON vede quell'IP
Default value "no"

- user_dstip == Trigger se VEDE quell'IP
No default

----- </dstip> ------ 



------ <srcport> ------ USER OPTIONAL

- user_srcport_negate == Trigger se NON rientra nella regex
Default value "no"

- user_srcport_type == Imposta il tipo di regex.
Default value "osmatch"

- user_srcport == Trigger se la porta RIENTRA nella regex

----- </srcport> ------ 



------ <dstport> ------ USER OPTIONAL

- user_dstport_negate == Trigger se NON rientra nella regex
Default value "no"

- user_dstport_type == Imposta il tipo di regex.
Default value "osmatch"

- user_dstport == Trigger se la porta RIENTRA nella regex

------ </dstport> ------ 



------ <time> ------ USER OPTIONAL

- user_time == Un qualsiasi range di tempo in cui l'alert si può attivare
<time>6 pm - 8:30 am</time>

hh:mm-hh:mm, hh:mm am-hh:mm pm, hh-hh, hh am-hh pm

------ </time> ------



------ <weekday> ------ USER OPTIONAL

- user_weekday == Un giorno della settimana o più di uno in cui l'alert si può attivare

------ </weekday> ------



------ <if_sid> ------ SYSTEM REQUIRED (la ottengo dalla struttura dell'ADT)
(repeatable)

- system_if_sid == La regola "prerequisito", cioè i nodi da cui proviene. Prendo i nodi subito inferiori.
Da definire il modo in cui si automatizza

------ </if_sid> ------



------ <same_srcip> ------ USER OPTIONAL

Basta dire si o no nel file di input

------ </same_srcip> ------



------ <different_srcip> ------ USER OPTIONAL

Basta dire si o no nel file di input

------ </different_srcip> ------



------ <same_srcport> ------ USER OPTIONAL

Basta dire si o no nel file di input

------ </same_srcport> ------



------ <different_srcport> ------ USER OPTIONAL

Basta dire si o no nel file di input

------ </different_srcport> ------



------ <different_dstport> ------ USER OPTIONAL

Basta dire si o no nel file di input

------ </different_dstport> ------



------ <same_location> ------ USER OPTIONAL

Basta dire si o no nel file di input

------ </same_location> ------



------ <same_srcuser> ------ USER OPTIONAL

Basta dire si o no nel file di input

------ </same_srcuser> ------



------ <different_srcuser> ------ USER OPTIONAL

Basta dire si o no nel file di input

------ </different_srcuser> ------



------ <description> ------ USER OPTIONAL (SYSTEM HAS AUTOFILL WITH DEFAULT DESC THAT I NEED TO DEFINE)

- user_desc == Decidibile dall'utente, è la desc del nodo
    USER REQUIRED
 
v----- QUESTO SOLO SE E' ASSOCIATA UNA DIFESA!! -----v

<description>Launching [{nome-nodo == nome-script-difensivo}] defense script on [{location_in_active_response_tag}].</description>

nome-nodo == nome-script-difensivo == Il nome del nodo è lo corrente è lo stesso della difesa

location_in_active_response_tag == Se c'è una difesa, è una active response, e deve avere una posizione in cui eseguire la difesa.
Default lo metterei a "local", quindi sul device che ha lanciato l'alert.
Altrimenti USER OPTIONAL

^----- QUESTO SOLO SE E' ASSOCIATA UNA DIFESA!! -----^

------ </description> ------



------ <info> ------ USER OPTIONAL

user_info == Informazioni aggiuntive dell'utente, di tipo:

user_info_type == Tipo. Uno tra:
text, cve, link, ovsdb

------ </info> ------



------ <options> ------ USER OPTIONAL

user_options == Opzioni extra definite dall'utente per la regola

alert_by_email
no_email_alert
no_log
no_full_log
no_counter -> Omit field rule.firedtimes in the JSON alert.

------ </options> ------




# 