Documentazione puramente illustrativa e non formale di TreeAlchemist.
Consideriamolo un foglio di appunti.

TODO:
Devo caricare qui ADT-syntax-new.md reso più carino.
Devo creare la documentazione fatta meglio


# Scrittura dell'ADT

1) Scrivere un ADT senza i nodi di difesa dentro un file seguendo la sintassi ADT-syntax-new.md. Il file è un file .xml
Quello che viene dato in input non è un ADT, ma 

2) Definire <command> e <active_response> di Wazuh all'interno di 
defense_definition.xml

Sintassi:

<defense name="#any defense name"> <!-- name of the defense script -->
    <wazuh_command_config> <!-- Start of the Wazuh "command" configuration for the defense -->
        <extra_args>#arg1 arg2 arg3#</extra_args> <!-- This is Wazuh's <extra_args> tag in command. The arguments for the defensive script. -->
        <timeout_allowed>yes | no</timeout_allowed>  <!-- Activate the <timeout> tag inside of the next <wazuh_activeres_config> -->
    </wazuh_command_config>
    <wazuh_activeres_config> <!-- Start of the Wazuh "active-response" configuration for the defense -->
        <location>{local} | server | defined-agent | all</location> <!-- Specify where to execute the script once the node is reached -->
        <agent_id>#any number#</agent_id> <!-- Only with "defined-agent" declared in <location> -->
        <timeout>#any number#</timeout> <!-- Seconds after which the response is reverted. You must have <timeout_allowed> on the command section -->
    </wazuh_activeres_config> 
</defense_config>


---

defense name="#any#"
Nome della difesa.
In wazuh, diventeranno i blocchi

<command>
    <name>execute_#any#</name>
    <executable>#any#</executable>
</command>

<active-response>
    <command>execute_#any#</command>
</active-response>

NOTE:
Lo script difensivo che andrà sugli Agent dovrà NECESSARIAMENTE chiamarsi nel modo in cui ho definito la difesa,
per definizione di Wazuh.

---

Dentro <defense_config>


    Dentro <defense_config> / <wazuh_command_config>


        Omettere l'intero tag <wazuh_command_config> è lecito.
        Le opzioni seguenti sono TUTTE opzionali.


        <extra_args>

        Allows the user to customize the parameters sent to the active response script living on the agent side.

        <timeout_allowed>

        Allows a timeout after a period of time. Setting this value to yes reverts the action after a period of time. Check stateful active response below for more details.


    Dentro <defense_config> / <wazuh_activeres_config>
    Omettere l'intero tag <wazuh_activeres_config> è lecito.
    Le opzioni seguenti sono TUTTE opzionali.

        <location>

        local | server | defined-agent | all

        By default, it is "local", so it executes on the agent that raised the alert.

        <agent_id>001</agent_id> <!-- Only with "defined-agent" declared in <location> -->

        <timeout>
        any seconds
        <!-- Seconds after which the response is reverted -->


3) Mappare le difese a un nodo dentro il file defense_to_nodes.json.
Sintassi di defense_to_nodes.json:

{
    "defense_name" : ["node_id_1", "node_id_2"],
    ...
}

Example:

{
    "very_powerful_defense" : ["1", "2"],
    "very_powerful_defense2" : ["3", "4"],
}


Attenzione a scrivere defense_name esistenti e corretti, e mapparli a nodi esistenti e corretti.
IMPORTANTISSIMO:
Non si possono mappare due difese diverse allo stesso nodo, lancia un errore.