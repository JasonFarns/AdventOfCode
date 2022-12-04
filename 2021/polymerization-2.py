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
    ##end parse input_data

    def get_state(self):
        return self.template
    ##end get_state

    def get_rules(self):
        return self.rules
    ##end get_rules

    def step_forward(self, pair_count, letter_totals):
        new_pair_count = dict()
        for rule in self.rules.keys():
            new_pair_count[rule] = 0

        for rule in self.rules.keys():
            if (pair_count[rule] > 0):
                new_letter = self.rules[rule]
                new_pair_count[rule[0] + new_letter] += pair_count[rule]
                new_pair_count[new_letter + rule[1]] += pair_count[rule]

                if (new_letter in letter_totals):
                    letter_totals[new_letter] += pair_count[rule]
                else:
                    letter_totals[new_letter] = 1

        return new_pair_count, letter_totals
    ##end step_forward


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

    current_state = list(poly_template.get_state())

    pair_rules = poly_template.get_rules()
    pairs_count = dict()
    letter_totals = dict()

    for rule in pair_rules.keys():
        pairs_count[rule] = 0

    last_added = ''
    for idx,ele in enumerate(current_state):
        try:
            next_ele = current_state[idx+1]
            pair = ele + next_ele
            pairs_count[pair] += 1

            if (ele not in letter_totals):
                letter_totals[ele] = 1
            else:
                letter_totals[ele] += 1
        except:
            continue

    if (next_ele not in letter_totals):
        letter_totals[next_ele] = 1
    else:
        letter_totals[next_ele] += 1

    i = 1
    for i in range(40):
        pairs_count,letter_totals = poly_template.step_forward(pairs_count,letter_totals)
        i += 1

    total_letters = 0
    for count in pairs_count.values():
        total_letters += (count)

    max_letter_count = 0
    min_letter_count = 9999999999999999999999999999999999999999999999999999
    for total in letter_totals.values():
        if (total > max_letter_count):
            max_letter_count = total
        if (total < min_letter_count):
            min_letter_count = total

    max_min_difference = max_letter_count - min_letter_count

    print ("Polymer length is now:",total_letters)
    print ("High letter count:",max_letter_count)
    print ("Low letter count:",min_letter_count)
    print ("\tDifference:",max_min_difference)

##end main  
main()
