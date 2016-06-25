from abc import ABCMeta, abstractmethod
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

class HardAIPlayer(Player):
	def __init__(self, tick):
		self.marker = tick

	def eval(self, board):
		# TODO: we need some notion of good over and bad over
		if board.isOver():
			return 1
		else:
			return 0

	def minimax(self, board, curr_tick):
		# get a list of valid moves
		valid_moves = []

		for i in range(board.DIMENSION):
			for j in range(board.DIMENSION):
				if board.checkMove(i, j):
					valid_moves.append((i,j))

		# make each move
		for move in valid_moves:
			x, y = move
			newBoard = copy.deepcopy(board)
			newBoard.setMove(x ,y, curr_tick)
			if self.eval(newBoard) == 1:
				return x, y
			else:
				return self.minimax(newBoard, not curr_tick)

	def make_move(self, board):
		return self.minimax(board, self.marker)