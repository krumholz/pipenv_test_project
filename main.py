import sys
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return("Flask running on Google App Engine developed locally with pipenv for package management and tracked on Github.")

@app.route("/about")
def about():
    return("About Page")

@app.route("/systeminfo")
def systeminfo():
    return(sys.version)
