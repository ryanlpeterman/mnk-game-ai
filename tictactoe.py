#!/usr/bin/python

import player
import board

def main():

	brd = board.Board()

	p1 = player.HumanPlayer(0)
	p2 = player.HumanPlayer(1)

	curr_p = p1

	while not brd.isOver():

		brd.display()
		print "TESTICLE"
		x, y = curr_p.make_move(brd)
		brd.setMove(x, y, curr_p.marker)

		# switch players
		if curr_p == p1:
			curr_p = p2
		else:
			curr_p = p1

	brd.display()
	print "Game Over!"

if __name__ == '__main__':
    main()
