import os

from flask import Flask
from flask import render_template

# from Utility.FileSystemUtilities import get_immediate_subdirectories

app = Flask(__name__, static_folder="./../../public", template_folder="./templates")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_new_site")
def new_site():
    return render_template("create_new_site.html")


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


@app.route("/registeredprojects")
def get_registered_projects():
    return get_immediate_subdirectories("./../templates/")


if __name__ == "__main__":
    app.run(debug=True)
