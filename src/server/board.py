"""
Board module for tic tac toe. Displays and maintains the
state of the board
"""
import sys
import numpy as np

class Board:
    """
    maintains board state as a numpy int array where:
        -1 -> blank
        0  -> player 1 mark
        1  -> player 2 mark
    """
    DIMENSION = 3

    def __init__(self):
        self.board = np.zeros(shape=(3, 3))
        self.board.fill(-1)

    def __init__(self, board_arr):
        """
        initalizes board based on given flattened array
        """
        self.board = np.array(board_arr).reshape((self.DIMENSION, self.DIMENSION))

    def display(self):
        """
        display the entire grid
        """
        sys.stdout.write('\n-------\n')

        for row in self.board:
            sys.stdout.write('|')

            for elem in row:
                char = ' '
                if elem == 0:
                    char = 'X'
                elif elem == 1:
                    char = 'O'

                sys.stdout.write(char + '|')
            sys.stdout.write('\n-------\n')

    def checkMove(self, row, col):
        """
        verify if row, col would be a valid move,
        return true if it's a valid move else false
        """
        if row >= self.DIMENSION or row < 0 or col >= self.DIMENSION or col < 0:
            print "Input out of Bounds"
            return False

        if self.board[row][col] != -1:
            #print "Slot already taken"
            return False

        return True

    def setMove(self, row, col, tick):
        """
        sets a valid move on the grid
        """
        self.board[row][col] = tick

    def isOver(self):
        """
        returns element causing game over or 2 if cats game
        """
        CATS_GAME = 2
        GAME_ONGOING = -1

        check_func = lambda arr: arr[0] != -1 and all(elem == arr[0] for elem in arr)

        # all same marker in a row
        for row in self.board:
            if check_func(row):
                return row[0]

        # all same marker in a col
        for col in [self.board[:, idx] for idx in range(self.DIMENSION)]:
            if check_func(col):
                return col[0]

        # check pos_diag
        pos_diag = self.board.diagonal()
        neg_diag = [self.board[idx][(self.DIMENSION - 1) - idx] for idx in range(self.DIMENSION)]
        if check_func(pos_diag):
            return pos_diag[0]
        # check neg_diag
        elif check_func(neg_diag):
            return neg_diag[0]

        # cats game
        if np.count_nonzero(self.board == -1) == 0:
            return CATS_GAME

        # game not over
        return GAME_ONGOING
