#!/usr/bin/python3
import sys
import os
import re

def tally_position_digits (items, position):
    zeroes = 0
    ones = 0
    
    for item in items:
        if (int(item[position]) == 0):
            zeroes += 1
        else:
            ones += 1

    tally_results = [zeroes,ones]
    return tally_results

def main():

    input_file = "input3.txt"
    diagnostics = []
    
    with open(input_file) as filereader:
        print ('Reading diagnostics from ',input_file)
        for line in filereader:
            line = line.strip()
            diagnostics.append(line)
    
    filereader.close()
    
    diagnostic_len = len(diagnostics)
    print ("Number of diagnostic codes: ",diagnostic_len)

    #oxygen code search
    subset = diagnostics
    matches = 0
    index = 0
    regex = "^"

    while (matches != 1):
        tally = tally_position_digits(subset, index)
        zeroes = tally[0]
        ones = tally[1]

        if (zeroes > ones):
            #more 0's than 1's
            regex += str(0)
        else:
            #more 1's than 0's
            regex += str(1)
   
        subset = [x for x in subset if re.search(regex, x)]
        matches = len(subset)
        print ("Remaining items:",matches)
        index += 1

    oxygen_code = subset[0]
    oxygen_decimal = int(oxygen_code,2)

    print ("Oxygen code:",oxygen_code)
    print ("Oxygen value:",oxygen_decimal)

    #co2 code search
    subset = diagnostics
    matches = 0
    index = 0
    regex = "^"

    while (matches != 1):
        tally = tally_position_digits(subset, index)
        zeroes = tally[0]
        ones = tally[1]

        if (zeroes > ones):
            #more 0's than 1's
            regex += str(1)
        else:
            #more 1's than 0's
            regex += str(0)

        subset = [x for x in subset if re.search(regex, x)]
        matches = len(subset)
        print ("Remaining items:",matches)
        index += 1

    co2_code = subset[0]
    co2_decimal = int(co2_code,2)

    print ("CO2 code:",co2_code)
    print ("CO2 value:",co2_decimal)

    life_support_value = oxygen_decimal * co2_decimal
    print ("Life Support:",life_support_value)

main()
