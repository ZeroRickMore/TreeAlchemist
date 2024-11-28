Hello, and welcome to the TreeAlchemist guide!
This is an extremely short text to guide you through the upload of these files inside of Wazuh.



Rules File=======================

	- Go into /var/ossec/etc/rules/
	- Move the rules file 
		[ /home/wazuhserver/Desktop/TreeAlchemist/TreeAlchemist/Code/TreeAlchemizer/Output-Files/Root/100010-TreeAlchemized-Root.xml ]
	 inside of it, and job done!

Else, just copy these commands:

	sudo su
	cp /home/wazuhserver/Desktop/TreeAlchemist/TreeAlchemist/Code/TreeAlchemizer/Output-Files/Root/100010-TreeAlchemized-Root.xml /var/ossec/etc/rules



Command Active-Response File=======================

	- Modify content of /var/ossec/etc/ossec.conf
	- Copypaste all of the content of 
		[ /home/wazuhserver/Desktop/TreeAlchemist/TreeAlchemist/Code/TreeAlchemizer/Output-Files/Root/Command-Activeres-Root_manually_put_into_ossec_conf.xml ]
	 inside of it, at the very end, and job done!



Daemon readable txt=======================

	- Go into the directory where the daemon reads file from.
	It is the "Trees" directory located where Athanor.py is located.
	If you did not touch the github code, it is inside /TreeAlchemist/Code/Daemons/ .
	- Move 
		[ /home/wazuhserver/Desktop/TreeAlchemist/TreeAlchemist/Code/TreeAlchemizer/Output-Files/Root/Root_daemon_readable.txt ]
	 inside of it.

Commands for untouched github folders:

	cp /home/wazuhserver/Desktop/TreeAlchemist/TreeAlchemist/Code/TreeAlchemizer/Output-Files/Root/Root_daemon_readable.txt /home/wazuhserver/Desktop/TreeAlchemist/TreeAlchemist/Code/Daemons/Trees


===[ DO NOT FORGET ]===

Place the defensive scripts inside of the watched hosts (NOT THE WAZUH SERVER) in /var/ossec/active-response/bin !!!

The name of the script MUST be what you find inside of each <executable> in the file
	[ /home/wazuhserver/Desktop/TreeAlchemist/TreeAlchemist/Code/TreeAlchemizer/Output-Files/Root/Command-Activeres-Root_manually_put_into_ossec_conf.xml ]
plus a file extension if you did not declare it in the tag!!
REMEMBER to change permissions of the scripts with these commands:

	sudo chmod 750 /var/ossec/active-response/bin/your_script_name.extension
	sudo chown root:wazuh /var/ossec/active-response/bin/your_script_name.extension

In the end, doing [ls -l] should show same permissions for each script.
ALSO DO NOT FORGET TO sudo systemctl restart wazuh-manager !!!
Else the changes will have no impact.


I hope everything worked for you!
Have fun with your tree, and do not forget to launch the daemon in order to make the tree handling functional!