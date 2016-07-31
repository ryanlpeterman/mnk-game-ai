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
    M = -1
    N = -1
    K = -1

    def __init__(self, *args):
        """
        initalizes board based on what arguments are given
        if given 0: create a default board
        if given 3: interpret as M, N, K dimensions -- create board based on that
        if given 4: interpret as created board, with M, N, K dimensions --
                    create board based off existing board
        """
        if len(args) == 0: #I will create a default board
            self.M, self.N, self.K = 3, 3, 3
            self.board = np.zeros(shape=(self.M, self.N))
            self.board.fill(-1)

        elif len(args) == 4: #i'm expecting a completed board 
            self.M, self.N, self.K = args[1], args[2], args[3]
            self.board = np.array(args[0]).reshape((self.M, self.N))

        elif len(args) == 3: #they supplied dimensions (M, N, K)
            self.M, self.N, self.K = args[0], args[1], args[2]
            if self.K < 3:
                print "must match at least 3"
                self.board = None
            elif min(self.M, self.N) < self.K:
                print "min dimension of board must be greater than K"
                self.board = None
            elif self.M > 10 or self.N > 10:
                print "dimensions exceeds limit"
                self.board = None
            else:
                self.board = np.zeros(shape=(self.M,self.N))
                self.board.fill(-1)

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
        if row >= self.M or row < 0 or col >= self.N or col < 0:
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
        checks all iterations of the board to see if it's finished
        """
        catscnt = 0 #keeping track of if all the subboards that are cat's game'd
        subboardcnt = 0
        tempboard = np.zeros(shape=(self.K,self.K)) #temp square board to check game
        for i in xrange(self.K, self.M + 1):
            for j in xrange(self.K, self.N + 1):
                tempboard = self.board[i-self.K:i,j-self.K:j]
                ret = self.checkSquare(tempboard)
                subboardcnt = subboardcnt + 1
                if ret == 2:
                    catscnt = catscnt + 1 #if any subboard returns a non-cat's game, it's not over
                if ret != 2 and ret != -1:
                    return ret #one of the players won the sub array
        if catscnt == subboardcnt:
            return 2
        return -1 #nobody won and it's not a cat's game
                

    def checkSquare(self, board):
        """
        returns element causing game over or 2 if cats game
        """
		
        CATS_GAME = 2
        GAME_ONGOING = -1
        
        # checks if everything in a row is the same
        check_func = lambda arr: arr[0] != -1 and all(elem == arr[0] for elem in arr)

        # all same marker in a row
        for row in board:
            if check_func(row):
                return row[0]

        # all same marker in a col
        for col in [board[:, idx] for idx in range(self.K)]:
            if check_func(col):
                return col[0]

        # check pos_diag
        pos_diag = board.diagonal()
        neg_diag = [board[idx][(self.K - 1) - idx] for idx in range(self.K)]
        if check_func(pos_diag):
            return pos_diag[0]
        # check neg_diag
        elif check_func(neg_diag):
            return neg_diag[0]

        # cats game
        if np.count_nonzero(board == -1) == 0:
            return CATS_GAME

        # game not over
        return GAME_ONGOING
