# M,N,K Game AI

AI for a generic m,n,k game written in Python by Ryan Peterman and Scott Shi. Uses [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax) to explore possible game states. Applies [Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) to only explore necessary states. Deployed on Heroku using Flask. Front-end written in ReactJS.

## Usage
* From command line:
```
$ python tic-tac-toe.py
```
* From web: [Current Link Here](http://www.rpeterman.me)

## Project file structure

```
├── app.py
├── package.json
├── Procfile
├── README.md
├── requirements.txt
├── src
│   ├── client
│   │   ├── app
│   │   │   ├── components
│   │   │   │   └── Board.js
│   │   │   ├── index.jsx
│   │   │   └── static
│   │   ├── index.html
│   │   └── public
│   │       ├── bundle.js
│   │       └── bundle.js.map
│   └── server
│       ├── board.py
│       ├── player.py
│       └── tictactoe.py
└── webpack.config.js
```

## TODO
1. Generalize AI
2. Set up front-end hosting separate from personal website
3. Clean up backend response