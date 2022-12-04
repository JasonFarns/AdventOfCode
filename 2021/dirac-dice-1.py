#!/usr/bin/python3
import sys
import os


def main():

    starting_positions = ['Player 1 starting position: 10','Player 2 starting position: 8']
    #starting_positions = ['Player 1 starting position: 4','Player 2 starting position: 8'] ##test input

    pos = int(starting_positions[0][-1:].strip())
    players = {1:[pos,0]}

    pos = int(starting_positions[1][-1:].strip())
    players.update({2:[pos,0]})

    #100-sided deterministic die - roles 1 incrementally higher each time
    die = 1
    max_die = 100
    score_goal = 1000
    die_rolls = 0
    player_turn = 1
    winning_score_attained = False

    while not winning_score_attained:
#    while (players[1][1] < score_goal) or (players[2][1] < score_goal): ## will or do it or do I need xor??
        turn_movement = 0
        for i in range(3):
            turn_movement += die
            die += 1
            if (die > 100):
                die = 1

        die_rolls += 3

        player_pos = players[player_turn][0]
        positions_moved = 0

        while (positions_moved < turn_movement):
            player_pos += 1
            if player_pos > 10:
                player_pos = 1

            positions_moved += 1

        players[player_turn][1] += player_pos
        players[player_turn][0] = player_pos

        if (players[player_turn][1] >= score_goal):
            winning_score_attained = True

        if (player_turn == 1):
            player_turn = 2
        else:
            player_turn = 1
        

    print ("Players:",players)
    print ("Die rolls:",die_rolls)

    part1_output = players[player_turn][1] * die_rolls
    print ("Part 1 result:",part1_output)


##end main  
main()
