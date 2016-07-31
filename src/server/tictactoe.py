#!/usr/bin/python
""" Main game logic for tictactoe """

import player
import board
import argparse

def game(player1_type, player2_type, num_games=1):
    """
    Game loop for tictactoe
    """
    player1_type += 'Player'
    player2_type += 'Player'

    # get constructor of player based on command line argument
    player1 = getattr(player, player1_type)(1)
    player2 = getattr(player, player2_type)(0)

    p1_win_cnt = 0
    p2_win_cnt = 0

    for _ in range(0, num_games):

        brd = board.Board(3, 4, 3)

        # ref to current player
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

        print "Game Over State:",
        brd.display()

        if brd.isOver() == 2:
            print "Cat's Game"
        elif brd.isOver() == 1:
            print player1_type + " (player1) Wins!!"
            p1_win_cnt += 1
        elif brd.isOver() == 0:
            print player2_type + " (player2) Wins!!"
            p2_win_cnt += 1

    print "\nSummary of Games Played:"
    print player1_type + " (player1) won " + str(p1_win_cnt) + " Times!"
    print player2_type + " (player2) won " + str(p2_win_cnt) + " Times!"
    print "There were " + str(num_games - (p1_win_cnt + p2_win_cnt)) + " Cat's Games"

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # optional arguments with associated default values
    parser.add_argument("-p1", "--player1", nargs='?', const="Human", default="Human",
                help="specify \"Human\", \"PerfectAI\", or \"RandomAI\" for p1")
    parser.add_argument("-p2", "--player2", nargs='?', const="PerfectAI", default="PerfectAI",
                help="specify \"Human\", \"PerfectAI\", or \"RandomAI\" for p2")
    parser.add_argument("-n", "--num", nargs='?', const=1, type=int, default=1,
                help="num games to be played, defaults to 1")

    args = parser.parse_args()
    valid_inputs = ["Human", "PerfectAI", "RandomAI"]

    # check if player inputs are correct
    if not args.player1 in valid_inputs or not args.player2 in valid_inputs:
        print "Player parameters must either be \"Human\", \"PerfectAI\", or \"RandomAI\""
        exit()

    game(args.player1, args.player2, args.num)
