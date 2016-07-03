"""
Flask server code to host the react front end that displays the
Tic Tac Toe output
"""
from flask import Flask, request
from flask_cors import CORS, cross_origin

import sys
import json
sys.path.append('./src/server')
import board as brd
import player

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
    # board passed in from post req
    curr_brd = brd.Board(json.loads(request.form['board']))

    response = {"row": -1, "col": -1}
    result = curr_brd.isOver()
    # game is over
    if result != -1:
        if result== 2:
            response["winner"] = "cat's game"
        elif result== 0:
            response["winner"] = "human"

        return json.dumps(response)
    else:
        computer_player = player.PerfectAIPlayer(1)
        row, col = computer_player.make_move(curr_brd)
        curr_brd.setMove(row, col, 1)

    # if move caused win for computer
    if curr_brd.isOver() == 1:
        response["winner"] = "computer"

    response["row"] = row
    response["col"] = col
    return json.dumps(response)

if __name__ == "__main__":
    app.run(debug=True)
