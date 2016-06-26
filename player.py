from abc import ABCMeta, abstractmethod
import numpy as np
import random as rand
import cmath as math
import copy
from operator import itemgetter

class Player:
	__metaclass__ = ABCMeta

	@abstractmethod
	def make_move(self, board): pass

class HumanPlayer(Player):
	def __init__(self, tick):
		self.marker = tick #marker to identify this player

	def make_move(self, board):
		"""Prompts user for 1 indexed move"""
		print("Enter Row Num (1-3)")
		row = int(raw_input()) - 1
		print("Enter Col Num (1-3)")
		col = int(raw_input()) - 1
		return row, col

class RandomAIPlayer(Player):
	def __init__(self, tick):
		self.marker = tick #marker to identfy this player

	def make_move(self, board):
		"""looks at all 9 possible moves and randomly
		choose an open slot"""
		openslots = np.full(9, 0, dtype=int) #-1 is invalid slots
		counter = 0 #index to keep track of open slots

		#traversing the board to look for free slots
		for i in range(0, board.DIMENSION):
			for j in range(0, board.DIMENSION):
				if (board.checkMove(i, j)):
					openslots[counter] = counter
				counter = counter + 1

		#randomly choose an index that's free
		#only consider free slots (nonzero)
		openslots = openslots[np.nonzero(openslots)]
		#grabs a random index of these open slots
		if len(openslots) == 0:
			return 0,0
		index = rand.randrange(0, len(openslots))
		#grab the grid coordinate of this open slot
		slot = openslots[index]

		return int(slot/3), slot%3

class AI(Player):
	__metaclass__ = ABCMeta

	@abstractmethod
	def eval(self, board): pass

class MediumAIPlayer(AI):
	def __init__(self, tick):
		self.marker = tick

	def eval(self, board, depth):
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

	def minimax(self, board, curr_tick, depth):
		# get a list of valid moves
		valid_moves = []
		for i in range(board.DIMENSION):
			for j in range(board.DIMENSION):
				if board.checkMove(i, j):
					valid_moves.append((i,j))

		ratings = []
		# make each move
		for move in valid_moves:
			x, y = move
			newBoard = copy.deepcopy(board)
			newBoard.setMove(x ,y, curr_tick)
			# add ratings to moves
			tmp = self.eval(newBoard, depth)
			if tmp != None:
				ratings.append(((x,y), tmp))
			# don't know who wins recurse to find
			else:
				result = self.minimax(newBoard, (1 - curr_tick), depth - 1)
				# if there were valid rated moves
				if result:
					# append the move that caused the result rating
					ratings.append((move, result[1]))

		if ratings:
			if curr_tick == self.marker:
				return max(ratings, key=itemgetter(1))
			else:
				return min(ratings, key=itemgetter(1))

	def make_move(self, board):
		move, rating = self.minimax(board, self.marker, 10)
		return move
