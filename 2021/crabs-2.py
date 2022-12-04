#!/usr/bin/python3
import sys
import os
import re

def sum_fuel_burn (crab_positions, pos):
    total_fuel = 0
    for idx,crab in enumerate(crab_positions):
        dist = abs(crab - pos)
        
        fuel_burn = 0
        if (dist > 0):
            for i in range(1,dist+1):
                fuel_burn += i
        total_fuel += fuel_burn

#    print ("Checking position:",pos,"Distance:",total_dist)
    return total_fuel
##end sum_fuel_burn

def main():

    #input_file = "input7-test.txt"
    input_file = "input7.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    crab_locations = [int(x) for x in list(input_data[0].split(','))]
    print (crab_locations)
    
    min_pos = min(crab_locations)
    max_pos = max(crab_locations)

    dist_sum = 0
    min_dist_pos = 0
    min_dist_sum = 1000000000000000
    pos = min_pos
    while pos <= max_pos:
        dist_sum = sum_fuel_burn(crab_locations, pos)
        if dist_sum < min_dist_sum:
            min_dist_pos = pos
            min_dist_sum = dist_sum
        pos += 1

    print ("Ideal position for all crabs is:",min_dist_pos,"-- requiring",min_dist_sum,"fuel")
##end main  
main()
