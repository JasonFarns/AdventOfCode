#!/usr/bin/python3
import sys
import os
import re

def strategy_tally(strat):
    round_num = 1
    total_score = 0
    for idx,vals in enumerate(strat):
        opp_play = translate_play_to_num(vals[0])
        my_play = translate_play_to_num(vals[2])
        
        round_score = 0
        
        if (opp_play == my_play):
            print ("DRAW:", opp_play, "-->", my_play)
            round_score = 3 + my_play
        elif (opp_play == 1 and my_play == 3):
            print ("LOOSE:", opp_play, "-->", my_play)
            round_score = my_play
        elif (opp_play == 2 and my_play == 1):
            print ("LOOSE:", opp_play, "-->", my_play)
            round_score = my_play
        elif (opp_play == 3 and my_play == 2):
            print ("LOOSE:", opp_play, "-->", my_play)
            round_score = my_play
        else:
            print ("WIN:", opp_play, "-->", my_play)
            round_score = 6 + my_play
        print ("round score:", round_score)

        total_score += round_score
        round_num += 1
    print ("Total score:", total_score)

def translate_play_to_num(play):
    num = 3
    if (play == "A" or play == "X"):
        num = 1
    elif (play == "B" or play == "Y"):
        num = 2
    return num


def main():

    #filename = "aoc_2022_input_2-test.txt"
    filename = "aoc_2022_input_2.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "advent_of_code_2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    strategy_tally(input_data)

##end main  
main()

