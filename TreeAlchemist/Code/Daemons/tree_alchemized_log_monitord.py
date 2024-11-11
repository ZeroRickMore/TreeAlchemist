'''
Daemon that, using pyinotify, monitors the log file
changes and sends them via POST to the wazuh_adtmanagerd
in order to make it process the request for the ADT

Every process is also logged inside of Logs/tree_alchemized_log_monitord.log
'''

import logging
import pyinotify
import os
import requests
import read_toml

debug = True


class FileChangeHandler(pyinotify.ProcessEvent):
    def __init__(self, file_path : str, webserver_port : int):
        self.webserver_port = webserver_port
        self.file_path = file_path

        with open(self.file_path, 'r') as file:
            file.seek(0, 2)
            self._last_position = file.tell()  # Tracks the last read position in the file


        # Set up logging to file
        log_file_path = os.path.join(os.path.dirname(__file__), 'Logs', 'tree_alchemized_log_monitord.log')
        logging.basicConfig(
            filename=log_file_path,
            filemode='a',  # Append mode
            format='%(asctime)s - %(message)s',
            level=logging.INFO # This captures INFO and higher
        )
        self.logger = logging.getLogger()

        if debug:
            print("Started\n")

        self.logger.info("===== tree_alchemized_log_monitord started =====")

    def process_IN_MODIFY(self, event):
        if debug:
            print(f"NEW EVENT: {event.pathname}")
        if event.pathname == self.file_path:
            print("PROCESSING IT")
            self.process_new_lines()

    def process_new_lines(self):
        with open(self.file_path, 'r') as file:
            # Move to the last read position
            file.seek(self._last_position)
            
            
            # Read and process new lines
            for line in file:
                if debug: print(f"READING FILE ON SEEK = {self._last_position}")
                self.process_line(line.strip())

            # Update the last position
            self._last_position = file.tell()

    def process_line(self, line):
        # Send the new line content to the wazuh_adtmanagerd web server
        # and log the details of the transaction
        try:
            if debug: print(f"SENDING LINE {line}")
            response = requests.post(f"http://localhost:{self.webserver_port}/new-alert", json={"alert": line})
            if debug: print(f"Response: {response.text}")
            response.raise_for_status()
            self.logger.info(f"Sent alert to wazuh_adtmanagerd[{self.webserver_port}]: {line}")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error sending alert to wazuh_adtmanagerd[{self.webserver_port}]: {e}")



def launch_log_monitoring(webserver_port : int = 4700):
    '''
    Launches monitoring of default file /var/log/tree_alchemized_alerts.log

    Sends POST requests to localhost:{webserver_port}/new-alert containing the new lines,
    with the json format {"alert": line}, one line at a time
    defaulting to port 4700

    Logs every transaction with the webserver inside of ./Logs/tree_alchemized_log_monitord.log
    
    '''
    log_path = os.path.join('/', 'var', 'log', 'tree_alchemized_alerts.log')
    monitor_file(log_path, webserver_port)



def monitor_file(file_path : str, webserver_port : int):
    # Set up inotify and the handler
    wm = pyinotify.WatchManager()
    handler = FileChangeHandler(file_path, webserver_port)
    # Watch the file for modifications only
    notifier = pyinotify.Notifier(wm, handler)
    wm.add_watch(file_path, pyinotify.IN_MODIFY)

    print(f"Started monitoring {file_path}")

    # Run the notifier loop to listen for events
    notifier.loop()




if __name__ == '__main__':
    launch_log_monitoring(read_toml.get_port())