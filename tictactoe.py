#!/usr/bin/python

import player
import board

def main():

	brd = board.Board()

	p1 = player.EasyAIPlayer(0)
	p2 = player.EasyAIPlayer(1)

	curr_p = p1

	while not brd.isOver():
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

if __name__ == '__main__':
    main()
