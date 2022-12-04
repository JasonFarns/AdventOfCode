#!/usr/bin/python3
import sys
import os
import curses
import time
import re

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
class transparency:
    def __init__(self, raw_sheet):
        self.parse_instructions(raw_sheet)

    def parse_instructions(self, raw_sheet):
        self.point_instructions = []
        self.fold_instructions = []

        for line in raw_sheet:
            point_re_search = '^\d+,\d+'
            if (re.search(point_re_search, line)):
                    line = line.split(',')
                    line = [int(x) for x in line]
                    self.point_instructions.append(line)
            elif (line != ''):
                line = line.split()
                fold = line[2].split('=')
                self.fold_instructions.append(fold)
    
    def get_point_instructions(self):
        return self.point_instructions

    def has_more_instructions(self):
        if (len(self.fold_instructions) > 0):
            return True
        return False
        

    def do_fold(self, points):
        fold_instruction = self.fold_instructions.pop(0)
        direction = fold_instruction[0]
        fold_line = int(fold_instruction[1])

        print ("Folding along",direction,'=',fold_line)

        new_points = set()
        for orig_point in points:
            if (direction == 'x'):
                #move first point in pair
                if (orig_point[0] > fold_line):
                    distance = (orig_point[0] - fold_line) * 2
                    new_x = orig_point[0] - distance
                    new_points.add((new_x,orig_point[1]))
                else:
                    new_points.add((orig_point[0],orig_point[1]))

            if (direction == 'y'):
                #move second point in pair
                if (orig_point[1] > fold_line):
                    distance = (orig_point[1] - fold_line) * 2
                    new_y = orig_point[1] - distance
                    new_points.add((orig_point[0], new_y))
#                    print ("Moving",orig_point,distance,' --> ',orig_point[0],',',new_y)
                else:
                    new_points.add((orig_point[0],orig_point[1]))

        new_points = list(new_points)
        return new_points

##end class transparency


def main():

    #input_file = "input13-test.txt"
    input_file = "input13.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    new_transparency = transparency(input_data)
    new_points = new_transparency.get_point_instructions()

    while (new_transparency.has_more_instructions()):
        new_points = new_transparency.do_fold(new_points)
#        for point in new_points:
#            print (point)

        num_points = len(new_points)
        print ("Total points:",num_points)

    grid = []
    max_x = 0
    max_y = 0
    for point in new_points:
        x,y = point
        if (x > max_x):
            max_x = x
        if (y > max_y):
            max_y = y

    for i in range(max_y+1):
        dummy_x_list = []
        for j in range(max_x+1):
            dummy_x_list.append('.')
        grid.append(dummy_x_list)

    for point in new_points:
        x,y = point
        grid[y][x] = '#'

    for line in grid:
        line_to_print = ''
        for ele in line:
            if (ele == '#'):
                #line_to_print += ele
                line_to_print += '█'
            else:
                line_to_print += ' '

        print (line_to_print)


    blank_char = u'\u2588'
    print ("\n\n",blank_char)
    ##end main  
main()
