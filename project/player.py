"""
Player module that contains HumanPlayer, RandomAIPlayer, and PerfectAIPlayer
implementations
"""
import copy

from abc import ABCMeta, abstractmethod
from operator import itemgetter

import random as rand
import numpy as np

class Player:
    """
    abstract class that represents a player
    """
    __metaclass__ = ABCMeta

    def __init__(self, marker):
        """
        A Player only needs to know its marker
        """
        self.marker = marker

    @abstractmethod
    def make_move(self, board):
        """
        A Player needs to know how to make a move on the board
        """
        pass

class HumanPlayer(Player):
    """
    Human players make moves by printing for input from stdin
    """
    def make_move(self, board):
        """Prompts user for 1 indexed move"""
        print "Enter Row Num (1-3)"
        row = int(raw_input()) - 1
        print "Enter Col Num (1-3)"
        col = int(raw_input()) - 1
        return row, col

class RandomAIPlayer(Player):
    """
    AI that randomly generates a valid move
    """
    def make_move(self, board):
        """
        looks at all 9 possible moves and randomly
        choose an open slot
        """
        # -1 is invalid slots
        openslots = np.full(9, 0, dtype=int)
        num_open = 0

        # traversing the board to look for free slots
        for i in range(0, board.DIMENSION):
            for j in range(0, board.DIMENSION):
                if board.checkMove(i, j):
                    openslots[num_open] = num_open
                num_open = num_open + 1

        # randomly choose an index that's free
        # only consider free slots (nonzero)
        openslots = openslots[np.nonzero(openslots)]

        # grabs a random index of these open slots
        if len(openslots) == 0:
            return 0, 0
        index = rand.randrange(0, len(openslots))

        # grab the grid coordinate of this open slot
        slot = openslots[index]

        return int(slot/3), slot%3

class PerfectAIPlayer(Player):
    """
    AI that uses minimax algorithm to always choose
    the optimal move. Never loses
    """
    def eval(self, board, depth):
        """ Evaluate the current board state from AI's point of view

        Args:
            board: the board to evaluate
            depth: the current depth in the minimax recursion
        Returns:
            > 0 if win for AI
            < 0 if loss for AI
            0 if cats game
            None if game still ongoing

        """
        # over due to AI player winning
        if board.isOver() == self.marker:
            return depth
        # over due to other player winning
        elif board.isOver() == (1 - self.marker):
            return -depth
        # don't know who wins or tie
        elif board.isOver() == 2:
            return 0
        # not over
        else:
            return None

    def minimax(self, board, curr_marker, depth, p_alpha, p_beta):
        """ Returns the best move from the perspective of the current player

        Args:
            board - current board state
            curr_marker - current player's marker
            depth - depth in minimax recursion
        Returns:
            (move, rating) where move is a tuple specifying the best move
            for the AI and rating is how highly rated the move was

        """
        # get a list of valid moves
        valid_moves = []
        for row in range(board.DIMENSION):
            for col in range(board.DIMENSION):
                if board.checkMove(row, col):
                    valid_moves.append((row, col))

        ratings = []

        # initialization for alpha / beta pruning
        # will alter each of these as I call each child
        alpha = p_alpha
        beta = p_beta
        # want to keep track of which node we are on
        is_max_node = (self.marker == curr_marker)

        # make each move
        for move in valid_moves:
                # pruning the tree, no possible better solution here
            if alpha >= beta:
                if is_max_node:
                    return (max(ratings, key=itemgetter(1))[0], alpha)
                else:
                    return (min(ratings, key=itemgetter(1))[0], beta)

            row, col = move
            new_board = copy.deepcopy(board)
            new_board.setMove(row, col, curr_marker)
            # add ratings to moves
            tmp = self.eval(new_board, depth)
            # if it's possible to evaluate the board...
            if tmp != None:
                ratings.append(((row, col), tmp))
                if is_max_node:
                    # we are at a max mode, want to return max lower bound of solutions
                    if tmp > alpha:
                        alpha = tmp #update alpha as the max lower bound
                else:
                    # we are at a min node, want to return min upper bound of solutions
                    if tmp < beta:
                        beta = tmp #update beta as the min upper bound

            # don't know who wins recurse to find
            else:
                result = self.minimax(new_board, (1 - curr_marker), depth - 1, alpha, beta)
                # we want to re-evaluate alpha / beta based on children...same logic as above
                tmp = result[1]
                if is_max_node:
                    if tmp > alpha:
                        alpha = tmp
                else:
                    if tmp < beta:
                        beta = tmp

                # if there were valid rated moves
                if result:
                    # append the move that caused the result rating
                    ratings.append((move, result[1]))

            if ratings:
                if is_max_node:
                    return (max(ratings, key=itemgetter(1))[0], alpha)
                else:
                    return (min(ratings, key=itemgetter(1))[0], beta)

    def make_move(self, board):
        """
        Wrapper interface for minimax function
        """
        move, _ = self.minimax(board, self.marker, 10, -10000, 10000)
        return move
