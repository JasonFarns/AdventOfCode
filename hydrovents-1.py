#!/usr/bin/python3
import sys
import os
import re

def create_ocean_grid(max_x, max_y):
    y = 0
    new_ocean_grid = []
    while y <= max_y:
        x = 0
        horiz_axis = []
        while x <= max_x:
            horiz_axis.append(0)
            x += 1
        new_ocean_grid.append(horiz_axis)
        y += 1

    return new_ocean_grid
# end create_ocean_grid

def mark_vertical_line (grid,line):
    x = line[0][0]
    y1 = line[0][1]
    y2 = line[1][1]
    if (y1 > y2):
        y_temp = y2
        y2 = y1
        y1 = y_temp

    all_y_points = []
    y_curr = y1
    while y_curr <= y2:
        all_y_points.append(y_curr)
        y_curr += 1

    for y in all_y_points:
        point_val = grid[y][x]
        point_val += 1
        grid[y][x] = point_val

    return grid
# end mark_vertical_line

def mark_horizontal_line (grid,line):
    y = line[0][1]
    x1 = line[0][0]
    x2 = line[1][0]
    if (x1 > x2):
        x_temp = x2
        x2 = x1
        x1 = x_temp

    all_x_points = []
    x_curr = x1
    while x_curr <= x2:
        all_x_points.append(x_curr)
        x_curr += 1

    for x in all_x_points:
        point_val = grid[y][x]
        point_val += 1
        grid[y][x] = point_val

    return grid
#end mark_horizontal_line

def main():

    #input_file = "input5-test.txt"
    input_file = "input5.txt"
    vents_input = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            vents_input.append(line)
    filereader.close()
    
    max_x = 0
    max_y = 0

    ##
    for idx,line in enumerate(vents_input):
        coords = line.split('->')
        for coord in coords:
            xy = [int(x) for x in coord.split(',')]
            ## find max
            if xy[0] > max_x:
                max_x = xy[0]
            if xy[1] > max_y:
                max_y = xy[1]
            ## max found
    ##
    print ("Max x:",max_x,"Max y:",max_y)
    ocean_grid = create_ocean_grid(max_x,max_y)
    
    xy = []
    for idx,line in enumerate(vents_input):
        coords = line.split('->')
        line_coords = []
        line_coords.append([int(x) for x in coords[0].split(',')])
        line_coords.append([int(x) for x in coords[1].split(',')])
        xy.append(line_coords)

    for idx,line in enumerate(xy):
        # horizontal lines
        if (line[0][1] == line[1][1]):
            ocean_grid = mark_horizontal_line(ocean_grid,line)

        # vertical lines
        if (line[0][0] == line[1][0]):
            ocean_grid = mark_vertical_line(ocean_grid,line)
            
    overlapping_points = 0
    for grid_row in ocean_grid:
        print (grid_row)
        for point in grid_row:
            if point > 1:
                overlapping_points += 1

    print ("Number of points with at least 2 overlapping lines:",overlapping_points)
    
#end main  

main()
