#!/usr/bin/python3
import sys
import os
import curses
import time

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

class cave:
    def __init__(self, cave_info):
        parsed_cave_info = self.parse_cave_info(cave_info)
        self.build_graph(parsed_cave_info)

    def parse_cave_info(self, cave_info):
        parsed = []
        for line in cave_info:
            parsed.append(line.split('-'))
        return parsed
    
    def build_graph(self, caves):
        self.graph = {}
        for connector in caves:
            self.create_connection(connector)
        print (self.graph)
    ##end find_all_paths

    def create_connection (self, connector):
        A = connector[0]
        B = connector[1]

        self.graph.setdefault(A, set())
        self.graph.setdefault(B, set())
        self.graph[A].add(B)
        self.graph[B].add(A)
    ##end explore

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node.islower():
                if node not in path:
                    newpaths = self.find_all_paths(node, end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            if node.isupper():
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)

        return paths
    ##end find_all_paths

def main():

    #input_file = "input12-test.txt"
    input_file = "input12.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    newcave = cave(input_data)
    paths = newcave.find_all_paths('start', 'end')
    num_paths = len(paths)
    print (paths)
    print ("Found:",num_paths,"paths")
    

##end main  
main()
