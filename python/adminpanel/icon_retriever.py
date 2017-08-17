import base64

import os


class IconContainer(object):
    def __init__(self, icon_set_name):
        self.container = {}
        self.icon_set_root_folder = icon_set_name[2:].strip()
        self.parsing_scheme = "DEFAULT"
        self.absolute_path = None

    def set_parsing_scheme(self, parsing_scheme="DEFAULT"):
        if parsing_scheme is not "DEFAULT":
            self.parsing_scheme = parsing_scheme[2:].strip()

    def add_name(self, name):
        self.container[name] = ""

    def add_absolute_path(self, absolute_path):
        self.absolute_path = absolute_path

    def add_image_data(self, name, image_path):
        with open(image_path, "rb") as image_file:
            data = image_file.read()
            self.container[name] = base64.b64encode(data)

    def size(self):
        return len(self.container)

    def dump_icon_set(self):
        for k, v in self.container.iteritems():
            print (k, v)


# TODO: ADD MERGE FOR MULTIPLE ICONSETS
class IconRetriever(object):
    ICON_FILE_COMMENT_PREFIX = "//"
    ICON_FILE_FOLDER_PREFIX = "/_"

    def __init__(self, root_directory, resolution="2x_web"):  # Default value is highest resolution
        self.root_directory = root_directory
        self.resolution = resolution
        self.icons_sets = []
        self.parse_options = {
            "DEFAULT": self.parse_default,
            "material_parsing_scheme": self.parse_material_icon_file_name
        }

    def parse_icon_file(self, filename):
        first_line = True
        second_line = True
        retval = None
        with open(filename, "r") as _file:
            for line in _file.readlines():
                if first_line:
                    if line.startswith(self.ICON_FILE_FOLDER_PREFIX):
                        retval = IconContainer(line)
                    else:
                        print "ERROR: Could not parse icon file: " + filename
                        return retval
                    first_line = False
                    continue
                if second_line:
                    should_continue = False
                    if line.startswith(self.ICON_FILE_FOLDER_PREFIX):
                        retval.set_parsing_scheme(line)
                        should_continue = True
                    second_line = False
                    if should_continue:
                        continue
                if retval is not None:
                    if line.startswith(self.ICON_FILE_COMMENT_PREFIX):
                        continue
                    retval.add_name(line.split(" ")[0])
        return retval

    @staticmethod
    def get_immediate_subdirectories(a_dir):
        return [name for name in os.listdir(a_dir)
                if os.path.isdir(os.path.join(a_dir, name))]

    @staticmethod
    def get_immediate_files(a_dir):
        return [name for name in os.listdir(a_dir)
                if os.path.isfile(os.path.join(a_dir, name))]

    def parse_default(self, current_container, filename):
        pass

    @staticmethod
    def parse_material_icon_file_name(current_container, filename, resolution="48dp", theme="black"):
        # Remove ic_ from filename
        new_name = filename[3:]
        new_name, resolution_and_extension = new_name.rsplit("_", 1)
        # Material icons have themes black/white.
        current_resolution = resolution_and_extension.split(".")[0]
        base_name, file_theme = new_name.rsplit("_", 1)
        if file_theme == theme and current_resolution == resolution:
            # File ok add to dictionary
            current_container.add_image_data(base_name, os.path.join(current_container.absolute_path, filename))

    def parse_icon_file_name(self, current_icon_container, image_filename, resolution=None, theme=None):
        if resolution is not None:
            return self.parse_options[current_icon_container.parsing_scheme](current_icon_container, image_filename)
        return self.parse_options[current_icon_container.parsing_scheme](current_icon_container, image_filename)

    def walk_and_parse_icon_root_folder(self):
        icon_descriptor_files = self.get_immediate_files(self.root_directory)
        for _file in icon_descriptor_files:
            (self.icons_sets.append(
                self.parse_icon_file(os.path.join(self.root_directory, _file))) if self.parse_icon_file(
                os.path.join(self.root_directory, _file)) is not None else None)

        icon_set_directories = self.get_immediate_subdirectories(self.root_directory)
        for icon_set in self.icons_sets:
            if icon_set.icon_set_root_folder in icon_set_directories:
                sub_directory_path = os.path.join(self.root_directory, icon_set.icon_set_root_folder)
                resolutions = self.get_immediate_subdirectories(sub_directory_path)
                if self.resolution in resolutions:
                    icon_set_directory = os.path.join(sub_directory_path, self.resolution)
                    icon_set.add_absolute_path(icon_set_directory)
                    for icon_image in self.get_immediate_files(icon_set_directory):
                        self.parse_icon_file_name(icon_set, icon_image)
            else:
                print "Invalid iconset, missing iconset for: " + icon_set.icon_set_root_folder

    def get_icons(self):
        retval = {}
        print self.icons_sets
        for icon_set in self.icons_sets:
            retval.update(icon_set.container)
        return retval


if __name__ == "__main__":
    icon_retriever = IconRetriever("./../../private/icons")
    icon_retriever.walk_and_parse_icon_root_folder()
    for container in icon_retriever.icons_sets:
        # container.dump_icon_set()
        print container.size()
