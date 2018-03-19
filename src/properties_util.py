from configparser import ConfigParser


class PropertyUtil:
    parser: ConfigParser = ConfigParser

    def __init__(self):
        PropertyUtil.parser = ConfigParser()
        PropertyUtil.parser.read("api.properties")

    def get(self, section, property_name):
        return PropertyUtil.parser.get(section, property_name)

    def get_boolean(self, section, property_name):
        return PropertyUtil.parser.getboolean(section, property_name)
    
    def get_int(self, section, property_name):
        return PropertyUtil.parser.getint(section, property_name)
