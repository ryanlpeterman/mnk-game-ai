from abc import ABCMeta, abstractmethod
import numpy as np
import random as rand
import cmath as math
import copy

class Player:
	__metaclass__ = ABCMeta

	@abstractmethod
	def make_move(self, board): pass

class HumanPlayer(Player):
	def __init__(self, tick):
		self.marker = tick #marker to identify this player

	def make_move(self, board):
		"""Prompts user for 1 indexed move"""
		print("Enter X Coord (1-3)")
		x = int(raw_input()) - 1
		print("Enter Y Coord (1-3)")
		y = int(raw_input()) - 1

		while not board.checkMove(x,y):
			print("Enter X Coord (1-3)")
			x = int(raw_input()) - 1
			print("Enter Y Coord (1-3)")
			y = int(raw_input()) - 1

		return x, y

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

	def eval(self, board, curr_tick):
		# TODO: we need some notion of good over and bad over
		if board.isOver() == curr_tick:
			return 1
		# elif board.isOver() == not self.marker:
			# return -1
		else:
			return 0

	def minimax(self, board, curr_tick):
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
			if self.eval(newBoard, curr_tick) == 1:
				return x, y
			else:
				return self.minimax(newBoard, not curr_tick)

		# no valid moves found

	def make_move(self, board):
		return self.minimax(board, self.marker)
