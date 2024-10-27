Come descrivo un ADT?

Potrei rappresentarlo come un filesystem, e poi leggere come xml la descrizione di ogni nodo.

STEPS:

# 1 - Struttura dei nodi di attacco (SENZA LE DIFESE)

Proprio come in un filesystem, posso scrivere l'intero cammino per raggiungere un nodo per identificarlo.

POSSIBILE SEMPLIFICAZIONE: 
    PERCORSO ASSOLUTO: /(path here)
    PERCORSO RELATIVO ALLA RIGA PRECEDENTE: ./(path here)
                                            Per usare il path precedente, posso usare "./"

<tree>
    <node conjuncted_children="yes" root="yes">
        <!-- The last string after / is the node name -->
        <path>/root</path>
        <!-- You can use id instead of the node name for the path -->
        <id>0</id>
        <wazuh_rule_config>
            <>
        </wazuh_rule_config>
    </node>


    /root/child1
    /root/child2
    /root/child1/grandchild1
    ./grandgrandchild1
</tree>

Questo albero ha un nodo radice "root", con due nodi figli congiunti "child1" , "child2".
child1 ha un figlio "grandchild1".
grandchild1 ha un figlio "grandgrandchild1"


## Tutorial struttura:

Esempio completo della struttura.

E' ESTREMAMENTE VERBOSO e contiene TUTTE le possibilità.
Un vero nodo è MOLTO più snello.

- I valori tra parentesi graffe sono i valori default.
- La pipe indica "or", e i valori intorno sono i valori ammessi. Metterci altro causa errore.
- Parole entro gli # sono luoghi il cui l'utente può inserire qualsiasi cosa #ciao#
- Molte customizzazioni funzionano solo usando <frequency>, per definizione stessa. Le denoteremo con il prefisso freq_

<tree>
    <!-- ATK Node section -->
    <node conjuncted_children="yes | {no}" root="yes | {no}" type="{atk}">
        <!-- The path to the node, node itself NOT included. MUST end with a / -->
        <path>#/root#/</path>         <!-- Using <name> -->
        <path>#/0#/</path>            <!-- Using <id>   -->
        <id>#0#</id>                  <!-- Recommended to follow ID BEST PRACTICE -->
        <name>#any string#</name>   <!-- Any name that describes the node -->
        <wazuh_rule_config>        <!-- The rule itself. Not everything is necessary -->
            <frequency>#2#</frequency><!-- Amount of times a node must be reached before resulting into a problem -->
            <timeframe>#5#</timeframe><!-- How much time in seconds to reach the frequency described before. Launches a warning if used without <frequency> -->
            <ignore_after>#10#</ignore_after> <!-- Time in seconds after which the alert is ignored as if it never happened -->
            <req_rule_id>#5401#<req_rule_id> <!-- STACKABLE If you need preexisting Wazuh rules for this, insert the IDs here. This is Wazuh's <if_sid> -->
            <match negate="yes | {no}" type="{osmatch} | osregex | pcre2">#any string literal#</match> <!-- STACKABLE String literal log search -->
            <regex negate="yes | {no}" type="{osmatch} | osregex | pcre2">#any regex#</regex> <!-- STACKABLE Regex log search -->
            <freq_srcip negate="yes | {no}">#any IP#</freq_srcip> <!-- STACKABLE src IP to look out for -->
            <freq_dstip negate="yes | {no}">#any IP#</freq_dstip> <!-- STACKABLE dst IP to look out for -->
            <freq_srcport negate="yes | {no}" type="{osmatch} | osregex | pcre2">#any regex for a port#</freq_srcport> <!-- STACKABLE src PORT to look out for -->
            <freq_dstport negate="yes | {no}" type="osmatch | {osregex} | pcre2">#any regex for a port#</freq_dstport> <!-- STACKABLE dst PORT to look out for -->
            <time>#any time interval#</time> <!-- Time interval when the rule is active -->
            <weekday>monday - sunday | weekdays | weekends</weekday> <!-- Week interval when the rule is active -->
            <freq_same_srcip /> <!-- Tells system to increse frequency counter for alerts having same srcip -->
            <freq_different_srcip /> <!-- Tells system to increse frequency counter for alerts having different srcip -->
            <freq_same_srcport /> <!-- Tells system to increse frequency counter for alerts having same src port -->
            <freq_different_srcport /> <!-- Tells system to increse frequency counter for alerts having different src IP -->
            <freq_different_dstport /> <!-- Tells system to increse frequency counter for alerts having different dst IP -->
            <freq_same_location /> <!-- Tells system to increse frequency counter for alerts raised from the same location -->
            <freq_same_srcuser /> <!-- Tells system to increse frequency counter for alerts raised from the same user -->
            <freq_different_srcuser /> <!-- Tells system to increse frequency counter for alerts raised from the different location -->
            <description>#a good rule description#</description> <!-- Node == Rule description that will appear on Wazuh dashboard -->
            <info type="{text} | cve | link | ovsdb">#any information#</info> <!-- Extra information -->
            <options>alert_by_email | no_email_alert | no_log | no_full_log | no_counter</options> <!-- One tag for each you need -->
        </wazuh_rule_config>
        <!-- Configuration of the defense. If the node has none, omit it completely -->
        <defense_config>
            <def_name>#any string#</def_name> <!-- name of the defense script -->
            <wazuh_config> <!-- Start of the Wazuh configuration for the defense -->
                <wazuh_command_config> <!-- Start of the Wazuh "command" configuration for the defense -->
                    <extra_args>#arg1 arg2 arg3#</extra_args> <!-- This is Wazuh's <extra_args> tag in command. The arguments for the defensive script. -->
                    <timeout_allowed>#yes#</timeout_allowed>  <!-- Activate the <timeout> tag inside of the next <wazuh_activeres_config> -->
                </wazuh_command_config>
                <wazuh_activeres_config> <!-- Start of the Wazuh "active-response" configuration for the defense -->
                    <location>{local} | server | defined-agent | all</location> <!-- Specify where to execute the script once the node is reached -->
                    <agent_id>001</agent_id> <!-- Only with "defined-agent" declared in <location> -->
                    <timeout>180</timeout> <!-- Seconds after which the response is reverted. You must have <timeout_allowed> on the command section -->
                </wazuh_activeres_config> 
            </wazuh_config>
        </defense_config>
    </node>
    <!-- Other nodes one after another -->
    <node>
        <!-- Another node like before -->
    </node>
    <!-- Conjunctions section -->
    <conjunction>#4,5#<conjunction>
    <!-- Other conjunctions one after another -->
    <conjunction>#Files access,, very bad , Other node#<conjunction>
</tree>


### 1 - <tree>

Inserisci un tag <tree> che contenga tutti i nodi

### 2 - <node> for ATK nodes

Inserisci i nodi, uno alla volta, con questo tag.
NOTA IMPORTANTE: i nodi vanno definiti dall'alto verso il basso, livello per livello.
                 Il sistema NON riconosce cammini inseriti senza che esistano ancora i parent.

ATTRIBUTI:

- conjuncted_children

ALLOWED VALUES: yes, no
DEFAULT VALUE: no

Definisce se tutti i figli del nodo sono congiunti nell'ADT

- root

ALLOWED VALUES: yes, no
DEFAULT VALUE: no

Definisce se è il nodo radice. Solo un nodo può essere root, altrimenti errore.

- type

ALLOWED VALUES: atk, def
DEFAULT VALUE: atk

Definisce se è un nodo di attacco o di difesa.
Per capirci, i colori sono: rosso = atk, verde = def

Per l'ATK node, è omissibile e vale "atk".

#### Dentro <node>

##### <path>

Determina il cammino verso il nodo, escluso il nodo stesso.
Gli spazi sono ammessi, la separazione si fa sullo / . 
Per scrivere uno / nel nome, uso // .
Il cammino può essere fatto tramite <id> o <name> dei nodi.
Il nome del nodo, quindi l'ultima stringa, NON deve essere un numero. Dopotutto, deve essere esplicativo di cosa è quel nodo!

IMPLEMENTATIVAMENTE: Attenzione a controllare che la path esista!

##### <id>

Stringa numerica che rappresenta l'identificatore del nodo.

ID BEST PRACTICE:
    La best practice sarebbe numerare da sinistra a destra per ogni livello dall'alto al basso, dove root = 0 e i suoi figli sono, ad esempio, 1 e 2.
    Non è vincolante, sono utili esclusivamente per la scrittura delle path

##### <name>

Il nome identificativo del nodo.
Realisticamente, è l'etichetta dentro ai nodi dell'ADT.
Non può essere un numero, si mischierebbe con l'ID.

##### <wazuh_rule_config>

###### <frequency>

Il numero di volte che un attaccante deve raggiungere quel nodo affinché esso sia considerato "raggiunto" a tutti gli effetti.
In altri termini, il numero di volte che vengono sollevate le alert che conducono a quel nodo.

In un ADT può essere espresso graficamente in più modi, in particolare possiamo pensarlo come:

Due figli identici connessi per congiunzione a un padre -> frequency = 2

Un altro modo, forse un numero accanto a un nodo, per definire questo concetto di "questo nodo deve essere raggiunto n volte"


###### <timeframe>

Il tempo concesso all'attaccante per raggiungere il nodo <frequency> volte.

Non può esistere da solo senza frequency. Non avrebbe senso!

Lo si può mettere, la si lancia un WARNING per "inutilità", chiedendo se ci si è dimenticati la <frequency>


###### <ignore_after>

It is the <ignore> tag of Wazuh.
Tells Wazuh to ignore the alert after a certain period of time, and forget it in next rule matchings.

This is STRONGLY recommended for testing purposes!
In fact, I may consider introducing a <test>120</test> tag on top of the whole tree to autofill every node to 120 sec...

###### <req_rule_id> (devo pensarci)

This is what will go inside of <if_matched_sid> on Wazuh's rule.
If you do not want to use pre existing rules but just the ones in your ADT, do not use it.


###### <match> ...

Si rimanda a Wazuh-Attack-Defense-Tree-Converter.md

##### Dentro <defense_config>

Utilizzare solo ed esclusivamente se il nodo ha una difesa annessa.
L'unico tag obbligatorio è <def_name>

###### <def_name>

Il nome della difesa.
è il nome sia del comando che della difesa, in particolare è MOLTO importante
che sia anche il nome dello script che metto sugli Agents.

Finisce dentro <command> e <active-response> delle regole Wazuh nella tag <name> e <executable>

##### Dentro <defense_config> / <wazuh_config> / <wazuh_command_config>
Omettere l'intero tag <wazuh_command_config> è lecito.
Le opzioni seguenti sono TUTTE opzionali.


###### <extra_args>

Allows the user to customize the parameters sent to the active response script living on the agent side.

###### <timeout_allowed>

Allows a timeout after a period of time. Setting this value to yes reverts the action after a period of time. Check stateful active response below for more details.

##### Dentro <defense_config> / <wazuh_config> / <wazuh_activeres_config>
Omettere l'intero tag <wazuh_activeres_config> è lecito.
Le opzioni seguenti sono TUTTE opzionali.

######  <location>

local | server | defined-agent | all

By default, it is "local", so it executes on the agent that raised the alert.

<agent_id>001</agent_id> <!-- Only with "defined-agent" declared in <location> -->

###### <timeout>
any seconds
 <!-- Seconds after which the response is reverted -->


### 3 - <conjunction>

Use this tag to list all the nodes that are conjuncted.

You are free to use one of <id> or <name> tag for a node, but just use one of them in the list.

Split the nodes with a comma ",".

If you node <name> contains a comma "," , use <id> instead, or use a double comma 

Example:

Oh no! My node name is "Files access, very bad", how can I conjunct it with "Other node"?

<conjunction>Files access,, very bad , Other node<conjunction>

or use the <id>s of the nodes, let's say the first one is 4, and the other one is 5:

<conjunction>4,5<conjunction>


## Note importanti

### Why is my defense not working?

NON, e ripeto, NON mappare due nodi consecutivi come semplicemente uno il successore dell'altro con <if_sid>.
Aggiungi qualche condizione per il trigger del nodo successivo, altrimenti si ricade nel seguente problema:

Mappo il nodo "Brute Force" alla difesa "Extremely Strong Defense".
Inserisco il nodo padre di "Brute Force" ponendolo come <if_sid> quello di Brute Force e basta.
Ogni volta che Brute Force viene triggerato, non parte la difesa, ma va al nodo padre, e addio.

L'ho testato inserendo una regola sul famoso extremely-strong-defense con <if_sid>100000</if_sid>
ed effettivamente l'alert che lancerebbe l'active response viene completamente mangiata.

