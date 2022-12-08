#!/usr/bin/python3
import sys
import os
import re

def move_multi_crates(stacks, instructions):
    
    for idx,curr_move in enumerate(instructions):
        num_crates_to_move = int(curr_move[0])
        source = int(curr_move[1])
        dest = int(curr_move[2])

        source_indexed = source - 1
        dest_indexed = dest - 1
        
        temp_stack = []

        while (num_crates_to_move > 0):        
            crate = stacks[source_indexed].pop()
            temp_stack.append(crate)
            #print ("moving",crate,"from",source,"to",dest)
            num_crates_to_move -= 1

        for i in range(len(temp_stack)):
            crate = temp_stack.pop()
            stacks[dest_indexed].append(crate)

    return stacks
        
def main():

    #filename = "aoc_2022_input_6-test.txt"
    filename = "aoc_2022_input_6.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    datastream = list(input_data[0])
    buffer = []
    for idx,char in enumerate(datastream):
        if (len(buffer) < 14):
            buffer.append(char)
            if (len(set(buffer)) != len(buffer)):
                for i in range(len(buffer)-1):
                    t = i+1
                    buffer[i] = buffer[t]
                buffer.pop()
                #print("cleaned out",buffer,char)
        else:
            print (buffer,idx)
            break

    
##end main  
main()

