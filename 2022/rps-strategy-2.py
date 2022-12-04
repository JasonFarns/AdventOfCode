#!/usr/bin/python3
import sys
import os
import re

def strategy_tally(strat):
    round_num = 1
    total_score = 0
    for idx,vals in enumerate(strat):
        opp_play = translate_play_to_num(vals[0])
        guided_play = vals[2]

        my_play = what_should_i_play(opp_play, guided_play)
        
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
    if (play == "A"):
        num = 1
    elif (play == "B"):
        num = 2
    return num

def what_should_i_play(opp, guide):
    
    if (guide == "X"): #loose
        if (opp == 1):
            return 3
        if (opp == 2):
            return 1
        return 2
    if (guide == "Y"): #draw
        return opp
    if (guide == "Z"): #win
        if (opp == 3):
            return 1
        else:
            return opp+1
    

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

