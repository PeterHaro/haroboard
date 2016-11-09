import os
import re
import json
from pprint import pprint


class Expander(object):
    REGULAR_EXPRESSION_FOR_LOCATING_EXPANSION_ENTRY = re.compile("\{\{__\(\'(.*?)\'\)\}\}")

    def __init__(self, configuration_file, custom_configuration_file=None, root_directory="../public/templates",
                 output_directory="../public/", language_code="en"):

        self.language_code = language_code
        self.root_directory = root_directory
        self.output_directory = output_directory
        with open(configuration_file) as default_config:
            self.configuration_file = json.load(default_config)
        self.custom_configuration_file = None
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
                if filename.endswith(".html"):
                    self.expand_file(os.path.join(root, filename), filename)

    def expand_file(self, path, filename):
        output_lines = []
        with open(path, "r") as templateFile:
            for line in templateFile:
                output_lines.append(self.process_line(line))

        with open(self.output_directory + filename, "w+") as outputFile:
            outputFile.writelines(output_lines)

    def process_line(self, line):
        match = self.REGULAR_EXPRESSION_FOR_LOCATING_EXPANSION_ENTRY.search(line)
        if match:
            expansion = self.fetch_expansion(match.group(1))
            return line.replace(match.group(0), expansion[self.language_code])
        else:
            return line

    def fetch_expansion(self, index):
        if self.custom_configuration_file is not None:
            if self.custom_configuration_file[index] is not None:
                return self.custom_configuration_file[index]
        return "" if self.configuration_file[index] is None else self.configuration_file[index]

if __name__ == "__main__":
    Expander = Expander("../public/templates/configuration.json")
    Expander.walk_and_parse()
