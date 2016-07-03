"""
Flask server code to host the react front end that displays the
Tic Tac Toe output
"""
from flask import Flask
# import tictactoe as tic

app = Flask(__name__)

@app.route("/")
def hello():
    """
    outputs hello world to screen for now
    """
    return "Hello world!"

@app.route('/<name>')
def hello_name(name):
    """
    outputs name
    """
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run()
