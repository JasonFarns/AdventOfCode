#!/usr/bin/python3
import sys
import os
import re
import numpy as np

def find_low_on_row(height_row):
    low_positions = set()
    i = 0
    positions = len(height_row)
    for i in range(positions):
        curr_height = height_row[i]
        if i > 0:
            prev_height = height_row[i-1]
        else:
            prev_height = 9
        try:
            next_height = height_row[i+1]
        except:
            next_height = 9

        if (prev_height > curr_height):
            if (next_height > curr_height):
                low_positions.add(i)

    low_positions = list(low_positions)
    low_positions.sort()
    
    return low_positions
##end find_low_on_row

def find_low_on_columns(floor_map,row_low_positions):
    deepest_spots = []
    column_low_positions = set()
    i = 0
    columns = len(floor_map)
    for i in range(columns):
        for idx,low_pos in enumerate(row_low_positions[i]):
            curr_low_value = floor_map[i][low_pos]
            if (i > 0):
                prev_height = floor_map[i-1][low_pos]
            else:
                prev_height = 9
            try:
                next_height = floor_map[i+1][low_pos]
            except:
                next_height = 9

            if (prev_height > curr_low_value):
                if (next_height > curr_low_value):
                    deepest_spots.append([i,low_pos])

    return deepest_spots
##end find_low_on_columns

def main():

    #input_file = "input9-test.txt"
    input_file = "input9.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    floor_map = []
    row_low_positions = []
    for idx,entry in enumerate(input_data):
        height_row = [int(x) for x in entry]
        floor_map.append(height_row)
        low_positions = find_low_on_row(height_row)
        row_low_positions.append(low_positions)

    column_low_positions = find_low_on_columns(floor_map,row_low_positions)
    risk = 0
    for idx,vals in enumerate(column_low_positions):
        row = vals[0]
        col = vals[1]
        value = int(floor_map[row][col])
        risk += value + 1

    print ("Total risk at low points:",risk)

##end main  
main()
