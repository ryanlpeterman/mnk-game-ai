from abc import ABCMeta, abstractmethod

class Player:
	__metaclass__ = ABCMeta

	@abstractmethod
	def make_move(self, board): pass

class HumanPlayer(Player):
	def __init__(self, tick):
		self.marker = tick #marker to identify this player	

	def make_move(self, board):
		x = -1
		y = -1
		while (not board.checkMove(x,y))
			print("Enter X Coord (1-3)")
			x = raw_input()
			print("Enter Y Coord (1-3)")
			y = raw_input()
		
		return x, y
