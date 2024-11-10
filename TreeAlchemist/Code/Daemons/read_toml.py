import toml
import os

# Get stuff from daemon_varaibles.toml
toml_file_path = os.path.join(os.path.dirname(__file__), 'daemon_variables.toml')
config = toml.load(toml_file_path)

toml_port = config['settings']['port']

# Get credentials
toml_file_path = os.path.join(os.path.dirname(__file__), 'api_credentials.toml')
config = toml.load(toml_file_path)

toml_username = config['username']
toml_pwd = config['password']


# Get api settings
toml_file_path = os.path.join(os.path.dirname(__file__), 'api_settings.toml')
config = toml.load(toml_file_path)

toml_JWT_refresh_time = int(config['JWT_refresh_time'])

def get_port():
    return toml_port

def get_api_username():
    return toml_username

def get_api_pwd():
    return toml_pwd

def get_JWT_refresh_time() -> int:
    return toml_JWT_refresh_time