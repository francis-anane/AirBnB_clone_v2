#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
"""
from flask import Flask

app = Flask(__name__)


# bind '/' to say_hello
@app.route("/", strict_slashes=False)
def saya_hello():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


# bind '/hbnb' to hbnb
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB."""
    return "HBNB"


# bind '/c/<text>' to c
@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return f"C {text}"


# bind '/python' to python and '/python/<text>' to python(<param text>)
@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.
    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
