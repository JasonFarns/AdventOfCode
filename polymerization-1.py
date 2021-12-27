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
class polymer:
    def __init__ (self, input_data):
        self.parse_input_data(input_data)
#        for key, entry in self.rules.items():
#            print (key, ':', entry)

    def parse_input_data(self, input_data):
        self.template = ''
        self.rules = dict()

        pair_re_search = '->'
        for line in input_data:
            if (re.search(pair_re_search, line)):
                line = line.split('->')
                self.rules[line[0].strip()] = line[1].strip()
            elif (line != ''):
                self.template = line
            
    def get_state(self):
        return self.template
    ##end parse input_data

    def step_forward(self, polymer):
        polymer = list(polymer)
        pairs = []
        for idx,ele in enumerate(polymer):
            try:
                next_ele = polymer[idx+1]
                new_pair = ele + next_ele
                pairs.append(new_pair)
            except:
                continue

        new_polymer = ''
        last_ele = ''

        for pair in pairs:
            insertion = self.rules[pair]
            pair = list(pair)
            new_polymer += pair[0] + insertion
            last_ele = pair[1]

        new_polymer += last_ele

        return new_polymer

    def get_most_least_common(self, polymer):
        polymer = list(polymer)
        counts = dict()

        for ele in polymer:
            try:
                ele_count = counts[ele]
                counts[ele] = ele_count + 1
            except:
                counts[ele] = 1
        
        print (counts)
        max_value = max(zip(counts.values(), counts.keys()))[0]
        min_value = min(zip(counts.values(), counts.keys()))[0]
        
        max_min = str(max_value) + ',' + str(min_value)

        return max_min
    ##end get_most_common

def main():

    #input_file = "input14-test.txt"
    input_file = "input14.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    poly_template = polymer(input_data)

    current_state = poly_template.get_state()
    i = 1
    for i in range(1):
        current_state = poly_template.step_forward(current_state)
        i += 1

    print (current_state)

    most_least_common = poly_template.get_most_least_common(current_state)
    max_min = most_least_common.split(',')
    print (max_min)
    difference = int(max_min[0]) - int(max_min[1])

    print ("Difference between most & least common value in polymer:",difference)


##end main  
main()
