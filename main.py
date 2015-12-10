import yaml

def init():
    global config
    yaml_file = open('config/db.yml')
    config = yaml.safe_load(yaml_file)
    yaml_file.close()

init()

from login import login

login(config['username'], config['password'])
