#!/usr/bin/python3
import sys
import os
import re

def infer_segments_from_patterns (patterns):
    interpretation = [None,None,None,None,None,None,None,None,None,None]
    zero = one = two = three = four = five = six = seven = eight = nine = False
    #while (not zero) or (not one) or (not two) or (not three) or (not four) or (not five) or (not six) or (not seven) or (not eight) or (not nine):
    while (not one) or (not four) or (not seven) or (not eight):
        #record unique configurations
        for idx,reading in enumerate(patterns):
            num_lit = len(reading)
            reading = ''.join(sorted(reading))
            if (num_lit == 2):
                interpretation[1] = reading
                one = True
            if (num_lit == 3):
                interpretation[7] = reading
                seven = True
            if (num_lit == 4):
                interpretation[4] = reading
                four = True
            if (num_lit == 7):
                interpretation[8] = reading
                eight = True
    
    one_set = {x for x in interpretation[1]}
    four_set = {x for x in interpretation[4]}
    seven_set = {x for x in interpretation[7]}
    eight_set = {x for x in interpretation[8]}
    upper_L_set = four_set.difference(one_set)

    while (not zero) or (not two) or (not three) or (not five) or (not six) or (not nine):
        #logic your way to these ones
        for idx,reading in enumerate(patterns):
            num_lit = len(reading)
            reading = ''.join(sorted(reading))
            curr_set = {x for x in reading}
            if (num_lit == 5): #possible options are 2,3,5
                if one_set.issubset(curr_set): #all 'one' segments are lit on a 'three'
                    interpretation[3] = reading
                    three = True
                elif upper_L_set.issubset(curr_set): #all of the 'Upper L' segments are lit on a 'five'
                    interpretation[5] = reading
                    five = True
                else: #only remaining 5-segment number is 'two'
                    interpretation[2] = reading
                    two = True
            if (num_lit == 6): #possible options are 0,6,9
                if four_set.issubset(curr_set): #all of 'four' segments are lit on a 'nine'
                    interpretation[9] = reading
                    nine = True
                elif not seven_set.issubset(curr_set): #not ALL of the 'seven' segments are lit on a 'six'
                #elif upper_L_set.issubset(curr_set):
                    interpretation[6] = reading
                    six = True
                else: #only remaining 6-segment number is 'zero'
                    interpretation[0] = reading
                    zero = True

    return interpretation
##end infter_segments_from_patterns

def main():

    #input_file = "input8-test.txt"
    input_file = "input8.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    total_count = 0

    for idx,ele in enumerate(input_data):
        notes = ele.split('|')
        patterns = notes[0].split()
        output_values = notes[1].split()

        segment_meaning = infer_segments_from_patterns(patterns)
#        print (segment_meaning)
#        print (output_values)
        reading_value = ''
        for value in output_values:
            value = ''.join(sorted(value))
            decoded_segment = segment_meaning.index(value)
            reading_value += str(decoded_segment)
        print ("Fixed display:",reading_value)
        total_count += int(reading_value)
    print ("Total:",total_count)

##end main  
main()
