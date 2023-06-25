#!/usr/bin/python3
"""This script Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
"""
from flask import Flask

app = Flask(__name__)


# bind "/" to say_hello
@app.route("/", strict_slashes=False)
def say_hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
