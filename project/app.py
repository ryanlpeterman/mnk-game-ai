"""
Flask server code to host the react front end that displays the
Tic Tac Toe output
"""
import os
from flask import Flask
# import tictactoe as tic

app = Flask(__name__)

@app.route("/")
def hello():
    """
    outputs hello world to screen for now
    """
    return "Hello world!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)
