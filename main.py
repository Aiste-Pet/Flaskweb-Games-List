from flask import Flask, render_template
from data import games
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", games=games, datetime=datetime)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
