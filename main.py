import yaml

def init():
    global config
    yaml_file = open('conf.yml')
    config = yaml.safe_load(yaml_file)
    yaml_file.close()

init()

from login import login

login(config['username'], config['password'], 20)
