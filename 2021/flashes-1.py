#!/usr/bin/python3
import sys
import os
import re
from collections import deque

def watch_octopus_one_step (octopus_grid):
    x_len = len(octopus_grid[0])
    y_len = len(octopus_grid)

    x = 0
    y = 0
    octopus_flashed = []
    for y in range(y_len):
        for x in range(x_len):
            octopus_grid[y][x] += 1
            if (octopus_grid[y][x] > 9):
                if [x,y] not in octopus_flashed:
                    octopus_flashed.append([x,y])
                    flash_result = do_flash(octopus_grid,[x,y],octopus_flashed)
                    octopus_grid = flash_result[0]
                    for new_flash in flash_result[1]:
                        if (new_flash not in octopus_flashed):
                            octopus_flashed.append(new_flash)
            x += 1
        y += 1
    #end adding 1 to all octopus

    x = 0
    y = 0
    for y in range(y_len):
        for x in range(x_len):
            if (octopus_grid[y][x] > 9):
                octopus_grid[y][x] = 0
            x += 1
        y += 1

    one_step_result = [octopus_grid,octopus_flashed]
    return one_step_result
##end watch_ocotopus_one_step

def do_flash (octopus_grid, flasher, octopus_flashed):

    x = flasher[0]
    y = flasher[1]
    flashed_coords = [[x-1,y+1],[x,y+1],[x+1,y+1],[x-1,y],[x+1,y],[x-1,y-1],[x,y-1],[x+1,y-1]]

    x = 0
    y = 0
    x_len = len(octopus_grid[0])
    y_len = len(octopus_grid)
    for y in range(y_len):
        for x in range(x_len):
            if ([x,y] in flashed_coords):
                octopus_grid[y][x] += 1
                if (octopus_grid[y][x] > 9):
                    if ([x,y] not in octopus_flashed):
                        octopus_flashed.append([x,y])
                        flash_result = do_flash(octopus_grid,[x,y],octopus_flashed)
                        octopus_grid = flash_result[0]
                        #octopus_flashed = octopus_flashed + flash_result[1]
                        for new_flash in flash_result[1]:
                            if (new_flash not in octopus_flashed):
                                octopus_flashed.append(new_flash)

            x += 1
        y += 1

    flash_result = [octopus_grid,octopus_flashed]
    return flash_result
##end do_flash

def main():

    #filename = "input11-test.txt"
    filename = "input11.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2021", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    octopus_grid = []
    for line in input_data:
        octopus_line = list([int(x) for x in line])
        octopus_grid.append(octopus_line)

    print (octopus_grid)

    total_octopus_flashes = 0
    i=0
    while i < 100:
        step_result = watch_octopus_one_step(octopus_grid)
        octopus_grid = step_result[0]
        total_octopus_flashes += len(step_result[1])
        i += 1

    print ("Total octopus flashes:",total_octopus_flashes)
##end main  
main()
