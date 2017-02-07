import json

from flask import Flask
from flask import jsonify
from flask import render_template


app = Flask(__name__, static_folder="./../../public", template_folder="./templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lochistorydata")
def get_location_history_data():
    with open("./../../public/data/peter_location_history/CleanedLocationHistory.json") as location_history:
        json_object = json.load(location_history)
        return json_object #Cannot do return json.load(location_history) as flask can be a bit wierd with __INTERNAL__ dicts
if __name__ == "__main__":
    app.run(debug=True)
