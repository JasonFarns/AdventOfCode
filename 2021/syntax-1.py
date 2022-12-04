#!/usr/bin/python3
import sys
import os
import re
from collections import deque

def is_line_corrupt (line):
    print (line)
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
    for idx,line in enumerate(input_data):
        corrupt_if_char_returned = is_line_corrupt(line)
        if (corrupt_if_char_returned is not None):
            print ("Corruptin detected with:",corrupt_if_char_returned)
            corrupt_chars.append(corrupt_if_char_returned)

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

    print ("Final corruption score:",corruption_score)
##end main  
main()
