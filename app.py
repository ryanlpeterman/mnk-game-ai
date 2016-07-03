"""
Flask server code to host the react front end that displays the
Tic Tac Toe output
"""
from flask import Flask, request
from flask_cors import CORS, cross_origin

import sys
sys.path.append('./src/server')
import board as brd

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    """
    outputs hello world to screen for now
    """
    return "Hello world!"

@app.route('/api/board', methods=['POST'])
def getMove():
    """
    returns a move based on board passed in
    """
    # data = request.form.getlist('board', type=int)
    # print data
    # cnv_to_int = [int(x) for x in data['board']]
    # curr_brd = brd.Board(cnv_to_int)

    # return curr_brd.board
    return "Hi you wanted a move huh?"

if __name__ == "__main__":
    app.run(debug=True)
