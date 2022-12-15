#!/usr/bin/python3
import sys
import os
import re

def process_instruct(line, clock, x):
    line = line.split(" ")

    if (line[0] != "noop"):
        clock += 1
        if (clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220):
            print ("clock value:",clock, x, line)
            important_clock_values.add((clock,x))
        x += int(line[1])
        
        clock += 1

        if (clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220):
            print ("clock value:",clock, x, line)
            important_clock_values.add((clock,x))
    else:
        clock += 1
        if (clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220):
            print ("clock value:",clock, x, line)
            important_clock_values.add((clock,x))

    return clock, x
        

def main():

    #filename = "aoc_2022_input_10-test.txt"
    filename = "aoc_2022_input_10.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()
    
    clock = 1
    #global instruct
    #instruct = 0
    x = 1
    global important_clock_values
    important_clock_values = set()

    global test
    test = 1

    for idx,vals in enumerate(input_data):
        clock, x = process_instruct(vals, clock, x)
    

    while (clock < 221):
        clock += 1
        if (clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220):
            print ("clock value:",clock, x)
            important_clock_values.add((clock,x))

    print ("Clock cycles:",clock)
    print ("Value of X at end:", x)

    interesting_signal_total = 0
    print (important_clock_values)
    while (important_clock_values):
        entry = important_clock_values.pop()
        interesting_signal_total += entry[0] * entry[1]

    print ("Interesting signal calculation:",interesting_signal_total)
##end main  
main()

