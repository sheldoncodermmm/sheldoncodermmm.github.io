from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/work_experience")
def work_experience():
    return render_template("experience.html")

@app.route("/coursework")
def coursework():
    return render_template("coursework.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")
