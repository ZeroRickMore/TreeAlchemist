<defenses-definition>
    <!-- List every defense node replicating this syntax -->
    <defense name="#any def name#">
        <command> <!-- OPTIONAL Start of the Wazuh "command" configuration for the defense -->
            <extra_args>#arg1 arg2 arg3#</extra_args> <!-- OPTIONAL This is Wazuh's <extra_args> tag in command. The arguments for the defensive script. -->
            <timeout_allowed>#yes#</timeout_allowed>  <!-- OPTIONAL Activate the <timeout> tag inside of the next <wazuh_activeres_config> -->
        </command>
        <active-response> <!-- OPTIONAL Start of the Wazuh "active-response" configuration for the defense -->
            <location>{local} | server | defined-agent | all</location> <!-- OPTIONAL Specify where to execute the script once the node is reached -->
            <agent_id>001</agent_id> <!-- OPTIONAL Only with "defined-agent" declared in <location> -->
            <timeout>180</timeout> <!-- OPTIONAL Seconds after which the response is reverted. You must have <timeout_allowed> on the command section -->
        </active-response> 
    </defense>
</defenses-definition>



## <defense>

The main tag that contains the defense entry.

ATTRIBUTE:

- name

It is MANDATORY.
It is the name of the defensive script, meaning that for a correct functionality you MUST
call your defensive script with this format:
{name}.extension
Also, it is the name that will be used for the mapping in defense_to_nodes.json

Important note:
NOT giving an extension in this attribute means every file on the agent that's called like that, extension excluded, will be looked for.
Meaning that you MUST NOT have multiple defensive scripts with the same name!
It is recommended to put the extension too.

EXAMPLE:
<defense name="strong-defense">

the file on the monitored hosts will be called:
strong-defense.[any]

IMPLEMENTATION NOTE:
<command>
    <name>Launch {name}</name>
    <executable>{name}</executable>
<command>

<active-response>
    <command>Launch {name}</command>
</active-response>


## Dentro <command>
Omettere l'intero tag <command> è lecito.
Le opzioni seguenti sono TUTTE opzionali.

### <extra_args>

Allows the user to customize the parameters sent to the active response script living on the agent side.

### <timeout_allowed>

Allows a timeout after a period of time. Setting this value to yes reverts the action after a period of time. Check stateful active response below for more details.

##### Dentro <active-response>
Omettere l'intero tag <wazuh_activeres_config> è lecito.
Le opzioni seguenti sono TUTTE opzionali.

######  <location>

{local} | server | defined-agent | all

By default, it is "local", so it executes on the agent that raised the alert.

<agent_id>001</agent_id> <!-- Only with "defined-agent" declared in <location> -->

###### <timeout>
any seconds
 <!-- Seconds after which the response is reverted -->