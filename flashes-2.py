#!/usr/bin/python3
import sys
import os
import curses
import time

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

def print_grid(grid,steps):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    grid_print = ''
    for line in grid:
        println = ''
        for ele in line:
            println += str(ele) + ' '
        println += '\n'
        grid_print += println

    if (steps % 2 == 1):
        stdscr.addstr(2, 0, grid_print, curses.A_BOLD)
    else:
        stdscr.addstr(2, 0, grid_print)
    
    info_print = 'Steps: ' + str(steps) + '\n'
    stdscr.addstr(13, 0, info_print)

    stdscr.refresh()

    time.sleep(0.05)

    curses.echo()
    curses.nocbreak()
    curses.endwin()
##end print_grid

def main():

    #input_file = "input11-test.txt"
    input_file = "input11.txt"
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

    print_grid(octopus_grid,0)

    all_flashed = False
    i = 0

    while all_flashed == False:
        step_result = watch_octopus_one_step(octopus_grid)
        octopus_grid = step_result[0]
        octopus_flashed = len(step_result[1])
        if (octopus_flashed == 100):
            all_flashed = True
        i += 1

        print_grid(octopus_grid,i)

    print ("All octopus flashed on step:",i)
##end main  
main()
