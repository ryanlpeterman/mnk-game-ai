from abc import ABCMeta, abstractmethod

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
