import toml
import os

toml_file_path = os.path.join(os.path.dirname(__file__), 'daemon_variables.toml')
config = toml.load(toml_file_path)

toml_port = config['settings']['port']

def get_port():
    return toml_port