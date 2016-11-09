import os
import json
from pprint import pprint


class Expander(object):
    def __init__(self, configuration_file, custom_configuration_file=None, root_directory="../public/templates",
                 output_directory="../public/"):

        self.root_directory = root_directory
        self.output_directory = output_directory
        with open(configuration_file) as default_config:
            self.configuration_file = json.load(default_config)
        if custom_configuration_file is not None:
            with open(custom_configuration_file) as specialized_config:
                self.custom_configuration_file = json.load(specialized_config)

    def dump_configurations(self):
        pprint(self.configuration_file)
        if self.custom_configuration_file is not None:
            pprint(self.custom_configuration_file)

    def walk_and_parse(self):
        for root, dirs, files in os.walk(self.root_directory):
            for filename in files:
                self.expand_file(os.path.join(root, filename))

    def expand_file(self, path):
        with open(path, "r") as templateFile:
            

if __name__ == "__main__":
    Expander = Expander("../public/templates/configuration.json")
    Expander.walk_and_parse()
