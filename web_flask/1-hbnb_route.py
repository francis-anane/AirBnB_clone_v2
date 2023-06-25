#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
"""
from flask import Flask

app = Flask(__name__)


# bind "/" to say_hello
@app.route("/", strict_slashes=False)
def say_hello():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


# bind "/hbnb" to hbnb
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
