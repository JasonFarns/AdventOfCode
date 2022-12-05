#!/usr/bin/python3
import sys
import os
import re

def generate_letter_values():
    print (ord("A"))
    print (ord("Z"))
    print (ord("a"))
    print (ord("z"))
       
def main():

    #filename = "aoc_2022_input_3-test.txt"
    filename = "aoc_2022_input_3.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "advent_of_code_2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    #generate_letter_values()

    total_char_value = 0
    i = 0
    while i < len(input_data):
        sack1 = set(input_data[i])
        i += 1
        sack2 = set(input_data[i])
        i += 1
        sack3 = set(input_data[i])
        i += 1

        common = sack1 & sack2 & sack3
        common_char = list(common)[0]
        
        if (common_char.isupper()):
            char_val = ord(common_char) - 38
        else:
            char_val = ord(common_char) - 96
        
        total_char_value += char_val
        print (common_char,"--",char_val)

    print ("Total value:", total_char_value)

##end main  
main()

