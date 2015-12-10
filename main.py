import yaml

from login import login
from search import search

# init
def init():
    global config
    yaml_file = open('conf.yml')
    config = yaml.safe_load(yaml_file)
    yaml_file.close()

init()

# user login
login(config['username'], config['password'], 20)

# search
search("python")
