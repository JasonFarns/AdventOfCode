#!/usr/bin/python3
import sys
import os
import re
from collections import deque

def is_line_corrupt (line):
#    print (line)
    corrupt = False
    char_stack = deque()
    chars = [x for x in line]
    for idx,char in enumerate(chars):
        if (char == '(') or (char == '[') or (char == '{') or (char == '<'):
            #push onto stack
            char_stack.append(char)
        if (char == ')') or (char == ']') or (char == '}') or (char == '>'):
            #pop previous off stack, make sure current and popped are matching, else corruption!
            prev_char = char_stack.pop()
#            print ("Close:",prev_char,'--',char)
            if (prev_char == '(') and (char != ')'):
#                print ("Corrupted syntax detected. Expected: )")
                corrupt = True
            if (prev_char == '[') and (char != ']'):
#                print ("Corrupted syntax detected. Expected: ]")
                corrupt = True
            if (prev_char == '{') and (char != '}'):
#                print ("Corrupted syntax detected. Expected: }")
                corrupt = True
            if (prev_char == '<') and (char != '>'):
#                print ("Corrupted syntax detected. Expected: >")
                corrupt = True

        if (corrupt == True):
            break

    if (corrupt == False):
        char = None
#    return_info = [corrupt,char]
#    return return_info
    return char
## end is_line_corrupt

def complete_valid_line(line):
    closing_chars = []
    char_stack = deque()
    chars = list(line)
    for char in chars:
        if (char == '(') or (char == '[') or (char == '{') or (char == '<'):
            #push onto stack
            char_stack.append(char)
        if (char == ')') or (char == ']') or (char == '}') or (char == '>'):
            #pop previous off stack, make sure current and popped are matching, else corruption!
            prev_char = char_stack.pop()
    
    all_closed = False
    while all_closed == False:
        try:
            prev_char = char_stack.pop()
            if (prev_char == '('):
                closing_chars.append(')')
            if (prev_char == '['):
                closing_chars.append(']')
            if (prev_char == '{'):
                closing_chars.append('}')
            if (prev_char == '<'):
                closing_chars.append('>')

        except:
            all_closed = True

    return closing_chars
##end complete_valid_line

def score_autocomplete_chars(char_list):
    score = 0
    for char in char_list:
        if (char == ')'):
            score = (score * 5) + 1
        if (char == ']'):
            score = (score * 5) + 2
        if (char == '}'):
            score = (score * 5) + 3
        if (char == '>'):
            score = (score * 5) + 4

    return score
##end score_autocomplete_chars

def main():

    #input_file = "input10-test.txt"
    input_file = "input10.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    corrupt_chars = []
    autocomplete_scores = []
    for idx,line in enumerate(input_data):
        corrupt_if_char_returned = is_line_corrupt(line)
        if (corrupt_if_char_returned is not None):
#            print ("Corruptin detected with:",corrupt_if_char_returned)
            corrupt_chars.append(corrupt_if_char_returned)
        else:
            #non-corrupt line
            needed_chars_to_close_line = complete_valid_line(line)
            score = score_autocomplete_chars(needed_chars_to_close_line)
            autocomplete_scores.append(score)

    corruption_score = 0
    for char in corrupt_chars:
        if (char == ')'):
            corruption_score += 3
        if (char == ']'):
            corruption_score += 57
        if (char == '}'):
            corruption_score += 1197
        if (char == '>'):
            corruption_score += 25137

    num_scores = len(autocomplete_scores)
    print ("Number of scores:",num_scores)

    autocomplete_scores.sort()
    middle_pos = num_scores // 2
    print ("Middle score:",autocomplete_scores[middle_pos])

    print ("Final corruption score:",corruption_score)
##end main  
main()
