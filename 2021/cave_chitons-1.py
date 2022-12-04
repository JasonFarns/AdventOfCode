#!/usr/bin/python3
import sys
import os
import curses
import time
import re
from collections import defaultdict
import heapq as heap

from queue import PriorityQueue
import numpy as np

def neighbours(coord):
    i, j = coord[0], coord[-1]
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

def find_min_path(grid, start, end):
    arr_height, arr_width = len(grid), len(grid[0])
    P = PriorityQueue()
    P.put((0, start))
    visited = {start, }
    while P:
        r, coord = P.get() # ordering needs to be (risk, coord) as priority is done on 1st element size. 
        if coord == end:
            # break clause
            return r
        for n in neighbours(coord):
            if 0 <= n[0] < arr_height and 0 <= n[-1] < arr_width:
                if n not in visited:
                    visited.add(n)
                    dr = grid[(n[0], n[-1])]
                    P.put((r + dr, n))

def create_matrix(grid, N):
    arr = []
    for r in range(N):
        for c in range(N):
            arr.append((grid + (r + c)) % 9)
    rows = []
    for i in range(0, N**2, N):
        # join every set of 5 grids horizontally 
        rows.append(np.concatenate([arr[i] for i in range(i, i+N)], axis=1))
    # stack the grids vertically
    M = np.vstack([row for row in rows])
    # flip 0s to 9s
    flip = np.where(M==0)
    for c in list(zip(flip[0], flip[-1])):
        M[c] = 9

    return M


def main():

    #input_file = "input15-test.txt"
    input_file = "input15.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    grid = []
    for line in input_data:
        row = [int(x) for x in line]
        grid.append(row)

    # part 1:
    grid = np.array(grid)
    print(f'part1: {find_min_path(grid, (0, 0), (grid.shape[0]-1, grid.shape[-1]-1))}')

    # part 2:
    M = create_matrix(grid, 5)
    print(f'part2: {find_min_path(M, (0, 0), (M.shape[0]-1, M.shape[-1]-1))}')

    ##end main  
main()
