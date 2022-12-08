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

    #filename = "aoc_2022_input_5-test.txt"
    filename = "aoc_2022_input_5.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    stacks = []
    instructions = []
    for idx,vals in enumerate(input_data):
        if (vals[0] != "m"): #stacks starting condition
            stacks.append(list(vals))
        if (vals[0] == "m"): #movement instructions
            instruct = str(vals).split(" ")
            simple_instruct = [instruct[1],instruct[3],instruct[5]]
            instructions.append(simple_instruct)

            
    resulting_stacks = move_multi_crates(stacks, instructions)
    
    top_crates = ""
    for idx,vals in enumerate(resulting_stacks):
        top_crates += vals.pop()
    
    print (top_crates)
        
        
    
##end main  
main()

