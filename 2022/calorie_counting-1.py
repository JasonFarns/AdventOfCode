#!/usr/bin/python3
import sys
import os
import re

def get_calorie_totals(calories_array):
    totals = []
    
    curr_total = 0
    for idx,vals in enumerate(calories_array):
        if vals == '':
            totals.append(curr_total)
            curr_total = 0
        else:
            curr_total += int(vals)

    return totals

def main():

    #filename = "aoc_2022_input_1-test.txt"
    filename = "aoc_2022_input_1.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "advent_of_code_2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    elf_calorie_totals = get_calorie_totals(input_data) 
    for idx,vals in enumerate(elf_calorie_totals):
        print (vals)
    
    max_elf_value = max(elf_calorie_totals)   
    print ("Max value:", max_elf_value)

##end main  
main()

