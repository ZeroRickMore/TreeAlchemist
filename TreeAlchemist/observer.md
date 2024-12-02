Athanor.py is a theorical daemon that constantly listens to alerts,
and handles the defenses launch through a calculation and then a PUT to launch the command
for the chosen defense.

It is a direct consequence of TreeAlchemist generation, and it is meant to be used with its syntax and classes.

The idea is:

Having TreeAlchemist produce the rules for the singular node trigger, the <command> and <active-response> tags.
Once that is done, the script generates:
a file contains the <rule>s to put into the xml wazuh file, grouped into a <group>
another file contains <command> and <active-response> to manually insert into ossec.conf (automating it might be risky)
and a very last file containing the informations to allow this daemon to generate the Tree. Ideally, the daemon itself is located
inside of a folder, containing the .py execution files and a folder containing txt files to re-create the ADTs on restart.


