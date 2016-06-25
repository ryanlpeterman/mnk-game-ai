from abc import ABCMeta, abstractmethod

class Player:
	__metaclass__ = ABCMeta

	@abstractmethod
	def make_move(self, board): pass

class HumanPlayer(Player):
	def make_move(self, board):
		print("Enter X Coord (1-3)")
		x = input()
		print("Enter Y Coord (1-3)")
		y = input()

		# board.checkMove(x, y)

		return x, y