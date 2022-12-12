#!/usr/bin/python3
import sys
import os
import re

def add_line_to_grid(line):
    new_grid_row = []
    for idx,vals in enumerate(line):
        new_grid_row.append(vals)
    
    grid.append(new_grid_row)

def main():

    filename = "aoc_2022_input_8-test.txt"
    #filename = "aoc_2022_input_8.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    global grid
    grid = []
    global visible_trees
    scenic_score = set()

    for idx,vals in enumerate(input_data):
        add_line_to_grid(vals)

    for i,v in enumerate(grid):
        for q,u in enumerate(v):
            look_left,look_right = i,i
            look_up,look_down = q,q
            tree_height = grid[i][q]

            left_score = 0
            while (look_left > 0):
                left_score += 1
                look_left -= 1
                next_tree_height = grid[look_left][q]
                if (next_tree_height >= tree_height):
                    #print ("left obscured tree:",(i,q))
                    break

            right_score = 0
            while (look_right < (len(v)-1)):
                right_score += 1
                look_right += 1
                next_tree_height = grid[look_right][q]
                if (next_tree_height >= tree_height):
                    #print ("right obscured tree:",(i,q))
                    break

            up_score = 0
            while (look_up > 0):
                up_score += 1
                look_up -= 1
                next_tree_height = grid[i][look_up]
                if (next_tree_height >= tree_height):
                    #print ("up obscured tree:",(i,q))
                    break
            
            down_score = 0
            while (look_down < (len(grid)-1)):
                down_score += 1
                look_down += 1
                next_tree_height = grid[i][look_down]
                if (next_tree_height >= tree_height):
                    #print ("down obscured tree:",(i,q))
                    break
            
            print (left_score,right_score,up_score,down_score)
            total_view_score = left_score * right_score * up_score * down_score
            scenic_score.add(total_view_score)

    scenic_score.add(0)
    print ("Highest scenic score found:",max(scenic_score))

    
##end main  
main()

