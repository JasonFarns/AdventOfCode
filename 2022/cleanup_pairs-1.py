#!/usr/bin/python3
import sys
import os
import re

def check_overlap(pairs):
    overlap = False

    pairs = str(pairs)
    elf_assignments = pairs.split(",")
    elf1 = str(elf_assignments[0]).split("-")
    elf2 = str(elf_assignments[1]).split("-")
    
    e1_start = int(elf1[0])
    e1_end = int(elf1[1])
    e2_start = int(elf2[0])
    e2_end = int(elf2[1])

    if (e2_end <= e1_end):
        #print (elf1,"might overlap",elf2)
        if (e2_start >= e1_start):
            #print (elf1,"overlaps",elf2)
            overlap = True
    
    if (e2_end >= e1_end):
        #print (elf1,"might overlap",elf2)
        if (e2_start <= e1_start):
            #print (elf1,"overlaps",elf2)
            overlap = True

    return overlap

        


    
    

    
def main():

    #filename = "aoc_2022_input_4-test.txt"
    filename = "aoc_2022_input_4.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    overlap_count = 0
    for idx,vals in enumerate(input_data):
        overlap = False
        overlap = check_overlap(vals)
        if (overlap):
            overlap_count += 1

    print ("Total overlapping assignments:",overlap_count)
##end main  
main()

