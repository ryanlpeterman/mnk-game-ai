#!/usr/bin/python

import player
import board

def main():

	dumbcnt = 0
	smartcnt = 0
	for ite in range(0, 30):
		brd = board.Board()
		p2 = player.MediumAIPlayer(0)
		p1 = player.RandomAIPlayer(1)

		brd.curr_p = p1

		while brd.isOver() == -1:
			print "Player " + str(brd.curr_p.marker) + "'s move...",
			brd.display()

			row,col = brd.curr_p.make_move(brd)

			while not brd.checkMove(row, col):
				row, col = brd.curr_p.make_move(brd)

			brd.setMove(row, col, brd.curr_p.marker)

			# switch players
			if brd.curr_p == p1:
				brd.curr_p = p2
			else:
				brd.curr_p = p1

		brd.display()
		print "Game Over!"
		if brd.isOver() == 2:
			print "Cat's Game"
		elif brd.isOver() == 1:
			print "Player O Wins!!"
			dumbcnt += 1
		elif brd.isOver() == 0:
			print "Player X Wins!!"
			smartcnt+=1

	print "Smart AI Won " + str(smartcnt) + " Times!"
	print "Random AI Won " + str(dumbcnt) + " Times!"

if __name__ == '__main__':
    main()
