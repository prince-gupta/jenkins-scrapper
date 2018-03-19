import yaml

class PropertyUtil:

    cfg_file = None

    def __init__(self):
        with open("api.yml", 'r') as y_file:
            PropertyUtil.cfg_file = yaml.load(y_file)

    def get(self, section, property_name):
        return PropertyUtil.cfg_file[section][property_name]