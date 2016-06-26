# Tic Tac Toe AI

AI for Tic Tac Toe written in Python by Ryan Peterman and Scott Shi. Uses [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax) to explore possible game states. Applies [Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) to only explore necessary states. Deployed on Heroku using Flask. Front-end written in ReactJS.

## Usage
* From command line:
```
$ python project/tic-tac-toe.py
```
* From web: [https://tic-tac-toe-ai.herokuapp.com](tic-tac-toe-ai.herokuapp.com)

## Project file structure

```
tic-tac-toe-ai/
├── Procfile (For Heroku)
├── project
│   ├── app.py (Flask Server)
│   ├── board.py
│   ├── player.py
│   └── tictactoe.py (Main)
├── README.md
└── requirements.txt
```

## TODO
1. Add command line flags to access different players and number of games
2. Build out front end in ReactJS