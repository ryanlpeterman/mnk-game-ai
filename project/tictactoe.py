#!/usr/bin/python
""" Main game logic for tictactoe """

import player
import board

def game():
    """
    Game loop for tictactoe
    """
    dumbcnt = 0
    smartcnt = 0
    for _ in range(0, 5):
        brd = board.Board()
        player2 = player.PerfectAIPlayer(0)
        player1 = player.HumanPlayer(1)

        curr_player = player1

        while brd.isOver() == -1:
            print "Player " + str(curr_player.marker) + "'s move...",
            brd.display()
            row, col = curr_player.make_move(brd)

            while not brd.checkMove(row, col):
                row, col = curr_player.make_move(brd)

            brd.setMove(row, col, curr_player.marker)

            # switch players
            if curr_player == player1:
                curr_player = player2
            else:
                curr_player = player1

        brd.display()
        print "Game Over!"
        if brd.isOver() == 2:
            print "Cat's Game"
        elif brd.isOver() == 1:
            print "Player O Wins!!"
            dumbcnt += 1
        elif brd.isOver() == 0:
            print "Player X Wins!!"
            smartcnt += 1

    print "Smart AI Won " + str(smartcnt) + " Times!"
    print "Random AI Won " + str(dumbcnt) + " Times!"

if __name__ == '__main__':
    game()
