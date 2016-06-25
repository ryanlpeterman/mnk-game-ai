import numpy as np

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
		print self.board

	def checkMove(self, x, y):
		"""verify if it's a correct move,
		return true if it's a valid move"""
		if self.board[x][y] != -1:
			print "invalid move"
			return False
		return True

	def setMove(self, x, y, tick):
		"""sets a valid move on the grid"""
		self.board[x][y] = tick

	def isOver(self):
		"""returns true if game is over else false"""
		check_func = lambda arr: arr[0] != -1 and all(elem == arr[0] for elem in arr)

		# all same marker in a row
		for row in self.board:
			if check_func(row):
				return True

		# all same marker in a col
		for col in [self.board[:,idx] for idx in range(self.DIMENSION)]:
			if check_func(col):
				return True

		# check pos_diag
		if check_func(self.board.diagonal()):
			return True
		# check neg_diag
		elif check_func([self.board[idx][(self.DIMENSION - 1) - idx] for idx in range(self.DIMENSION)]):
			return True

		# cats game
		return np.count_nonzero(self.board == -1) == 0