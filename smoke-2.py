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
        print (row_low_positions[i])
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

def get_low_spot_width(floor_map,xy):
    x = xy[0]
    y = xy[1]
    row_data = floor_map[x]
    #look left until end or 9
    left_points = []
    while y > 0:
        y -= 1
        if row_data[y] < 9:
            left_points.append([x,y])
        else:
            break

    #look right until end or 9
    y = xy[1]
    right_points = []
    while y < (len(row_data)-1):
        y += 1
        if row_data[y] < 9:
                right_points.append([x,y])
        else:
            break

    low_spot_row_coords = [xy]
    if (len(left_points) > 0):
        for idx,point in enumerate(left_points):
            low_spot_row_coords.append(point)
    if (len(right_points) > 0):
        for idx,point in enumerate(right_points):
            low_spot_row_coords.append(point)
    return low_spot_row_coords
##end get_low_spot_width

def get_low_spot_height(floor_map,basin_y_coords):
    low_spot_x_coords = []
    for idx,coord in enumerate(basin_y_coords):
        x = coord[0]
        y = coord[1]
        while x > 0:
            x -= 1
            if (floor_map[x][y] < 9):
                low_spot_x_coords.append([x,y])
            else:
                break
        x = coord[0]
        while x < (len(floor_map)-1):
            x += 1
            if (floor_map[x][y] < 9):
                low_spot_x_coords.append([x,y])
            else:
                break
        
    return low_spot_x_coords
##end get_low_spot_height

def main():

    #input_file = "input9-test.txt"
    #input_file = "input9-test2.txt"
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

    lowest_positions = find_low_on_columns(floor_map,row_low_positions)
    basin_size = []
    for idx,xy in enumerate(lowest_positions):
        row = xy[0]
        col = xy[1]
        basin_y_coords = get_low_spot_width(floor_map,xy)
        basin_x_coords = get_low_spot_height(floor_map,basin_y_coords)

        num_x_coords = len(basin_x_coords)
        basin_x_coords = list(set(tuple(xy) for xy in basin_x_coords))
        basin_x_coords = [list(x) for x in basin_x_coords]

        basin_growing = True
        count = 0
        while basin_growing == True:
            x_size = len(basin_x_coords)
            y_size = len(basin_y_coords)
            for indx,xy2 in enumerate(basin_x_coords):
                row2 = xy2[0]
                col2 = xy2[1]
                basin_y_coords2 = get_low_spot_width(floor_map,xy2)
                for ndx,coord in enumerate(basin_y_coords2):
                    basin_y_coords.append(coord)
            basin_y_coords = list(set(tuple(xy3) for xy3 in basin_y_coords))
            basin_y_coords = [list(y) for y in basin_y_coords]

            basin_x_coords2 = get_low_spot_height(floor_map,basin_y_coords)
            for ndx,coord in enumerate(basin_x_coords2):
                basin_x_coords.append(coord)

            basin_x_coords = list(set(tuple(xy) for xy in basin_x_coords))
            basin_x_coords = [list(x) for x in basin_x_coords]
        
            count += 1
            if (len(basin_x_coords) == x_size) and (len(basin_y_coords) == y_size):
                basin_growing = False
        
        all_basin_coords = basin_x_coords
        for indx,coord in enumerate(basin_y_coords):
            all_basin_coords.append(coord)

        basin_len = len(all_basin_coords)
        all_basin_coords = list(set(tuple(xy) for xy in all_basin_coords))
        all_basin_coords = [list(x) for x in all_basin_coords]
        print ("All coords were:",basin_len,"Now:",len(all_basin_coords))
        basin_size.append(len(all_basin_coords))

    basin_size.sort(reverse=True)
    top3_basin_product = basin_size[0] * basin_size[1] *basin_size[2]
    print ("Largest 3 basins multiplied:",top3_basin_product)


##end main  
main()
