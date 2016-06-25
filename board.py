import numpy as np
import sys

class Board:
	DIMENSION = 3

	def __init__(self):
		#represented as integer matrix
		#'-1' is blank
		#'0' is player 1's tick
		#'1' is player 2's tick
		self.board = np.zeros(shape=(3,3))
		self.board.fill(-1)

	def display(self):
		"""display the entire grid"""
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

	def checkMove(self, x, y):
		"""verify if it's a correct move,
		return true if it's a valid move"""
		if x >= self.DIMENSION or x < 0 or y >= self.DIMENSION or y < 0:
			print "Input out of Bounds"
			return False

		if self.board[x][y] != -1:
			#print "Slot already taken"
			return False

		return True

	def setMove(self, x, y, tick):
		"""sets a valid move on the grid"""
		self.board[x][y] = tick

	def isOver(self):
		"""returns element causing game over or 2 if cats game"""
		CATS_GAME = 2
		GAME_ONGOING = -1

		check_func = lambda arr: arr[0] != -1 and all(elem == arr[0] for elem in arr)

		# all same marker in a row
		for row in self.board:
			if check_func(row):
				return row[0]

		# all same marker in a col
		for col in [self.board[:,idx] for idx in range(self.DIMENSION)]:
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
