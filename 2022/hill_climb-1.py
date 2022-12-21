#!/usr/bin/python3
import sys
import os
import re        

def find_path(heightmap,start,end):
    print ("trying to get from",start,"to",end)

    valid_paths = {}

    for idx1,line in enumerate(heightmap):
        for idx2,height in enumerate(line):
            up = idx1 - 1
            down = idx1 + 1
            right = idx2 + 1
            left = idx2 - 1

            valid_moves = []

            if (up >= 0):
                if ((heightmap[up][idx2] - height) <= 1):
                    valid_moves.append((up,idx2))

            try:
                next_height = heightmap[down][idx2]
                if ((next_height - height) <= 1):
                    valid_moves.append((down,idx2))
            except:
                1 == 1

            if (left >= 0):
                if ((heightmap[idx1][left] - height) <= 1):
                    valid_moves.append((idx1,left))

            try:
                next_height = heightmap[idx1][right]
                if ((next_height - height) <= 1):
                    valid_moves.append((idx1,right))
            except:
                1 == 1
        
            valid_paths[(idx1,idx2)] = valid_moves


    for loc,paths in valid_paths.items():
        print (loc,"-->",paths)

    

    visited_locs = []
    queue = []
    #find_a_path(start,end,valid_paths,visited_locs)
    bfs(visited_locs,queue,valid_paths,start,end)
    print ("path:",visited_locs)
    print (len(visited_locs))

def bfs(visited_locs,queue,valid_paths,start,end):
    visited_locs.append(start)
    queue.append(start)
    
    #if (start != end):
    while queue:
        s = queue.pop(0)
        #print (s, end = " ")
    
        for neighbour in valid_paths[s]:
            if neighbour not in visited_locs:
                if (neighbour == end):
                    return visited_locs
                else:
                    visited_locs.append(neighbour)
                    queue.append(neighbour)


def find_a_path(current_loc,end,valid_paths,visited_locs):
    #print ("called with:",current_loc,end)
    if (current_loc != end):
        visited_locs.append(current_loc)
        paths_from_here = valid_paths[current_loc]
        paths_already_tried = []
        if (len(paths_from_here) > 0):
            #print ("paths from here",current_loc,paths_from_here)
            for new_loc in paths_from_here:
                if (new_loc not in visited_locs):
                    returned_locs = find_a_path(new_loc,end,valid_paths,visited_locs)
                    if (len(returned_locs) < len(visited_locs)):
                        visited_locs = returned_locs
                else:
                    paths_already_tried.append(new_loc)
                    for i in range(1000):
                        visited_locs.append((999,999))
                    return visited_locs
        
            if (len(paths_already_tried) == len(paths_from_here)):
                print ("exhausted paths!")

    else:
        print ("found the end!",visited_locs)
        #return visited_locs
        


def main():

    filename = "aoc_2022_input_12-test.txt"
    #filename = "aoc_2022_input_12.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()
    
    heightmap = []
    startloc = ""
    endloc = ""
    
    for idx1,ele in enumerate(input_data):
        line = []
        for idx2,char in enumerate(ele):
            height = char
            if(char == "S"):
                startloc = (idx1,idx2)
                height = 1
            elif (char == "E"):
                endloc = (idx1,idx2)
                height = 26
            else:
                new_char = ord(char)
                height = new_char - 96

            line.append(height)
        heightmap.append(line)

    find_path(heightmap,startloc,endloc)
    
##end main  
main()

