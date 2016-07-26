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

## M-N-K Generalization (In progress)
1. Generalize Board:
  * Restrictions:
   * K must be at least 3 (must match at least 3 in a row to win, else it's too easy)
   * min(M, N) >= K (the smaller dimension of (M,N) must be greater than K to allow for a playable game
   * M, N must be less than 10 (just for your convenience...)

2. Refine Computation of Game States:
  * Create a general board checker for a NxN square board
  * For cases in which M != N, continuously pass in subsets of square boards to check game state

3. Set up front-end hosting separate from personal website
4. Clean up backend response
