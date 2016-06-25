import numpy as np

class Board:
	DIMENSION = 3

	def __init__(self):
		#represented as integer matrix
		#'-1' is blank
		#'0' is player 1's tick
		#'1' is player 2's tick
		self.board = np.fill((3,3),-1);#empty board
	
	def display(self):
		"""display the entire grid"""
		print "TODO"

	def checkMove(self, x, y):
		"""verify if it's a correct move"""
		print "TODO"

	def setMove(self, x, y, tick):
		"""sets a valid move on the grid"""
		print "TODO"
