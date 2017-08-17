import json
import os

from flask import Flask
from flask import render_template

# from Utility.FileSystemUtilities import get_immediate_subdirectories
from python.adminpanel.icon_retriever import IconRetriever

app = Flask(__name__, static_folder="./../../public", template_folder="./templates")


def parse_material_icons_list():
    retval = []
    with open("./../../public/styles/material-icons") as iconFile:
        for line in iconFile:
            if line.startswith("//"):  # Comment
                continue
            retval.append(line.split(" ")[0])

    # Match image name to image


    return retval


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_new_site")
def new_site():
    return render_template("create_new_site.html")


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


@app.route("/get_icons")
def get_all_icons_for_list():
    icon_retriever = IconRetriever("./../../private/icons")
    icon_retriever.walk_and_parse_icon_root_folder()
    return json.dumps(icon_retriever.get_icons())


@app.route("/get_material_icons")
def get_material_icons():
    return json.dumps(parse_material_icons_list())


@app.route("/registeredprojects")
def get_registered_projects():
    print get_immediate_subdirectories("./../../public/templates/")
    return json.dumps(get_immediate_subdirectories("./../../public/templates/"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, threaded=True, debug=True)
