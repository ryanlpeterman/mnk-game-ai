#!/usr/bin/python

import player
import board

def main():

	brd = board.Board()

	p2 = player.MediumAIPlayer(0)
	p1 = player.HumanPlayer(1)

	curr_p = p1

	while brd.isOver() == -1:
		print "Player " + str(curr_p.marker) + "'s move...",
		brd.display()
		x, y = curr_p.make_move(brd)
		brd.setMove(x, y, curr_p.marker)

		# switch players
		if curr_p == p1:
			curr_p = p2
		else:
			curr_p = p1

	brd.display()
	print "Game Over!"
	if brd.isOver() == 2:
		print "Cat's Game"
	elif brd.isOver() == 1:
		print "Player O Wins!!"
	elif brd.isOver() == 0:
		print "Player X Wins!!"

if __name__ == '__main__':
    main()
