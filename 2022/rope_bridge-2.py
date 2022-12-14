#!/usr/bin/python3
import sys
import os
import re
import math

def process_instruction(line):
    line = str(line).split(" ")
    direction = line[0]
    move_dist = int(line[1])
    
    H_loc = H_curr_loc.pop()
    T0_loc = T_curr_loc[0]

    if (direction == "R"):
        while (move_dist > 0):
            #move head 1
            H_loc[1] += 1
            #check if tail needs to move
            if (get_dist_between_locs(H_loc, T0_loc) > 1.5):
                H_loc,T0_loc = move_tail(H_loc,T0_loc)
                for tail_num in range (0,8):
                    if (get_dist_between_locs(T_curr_loc[tail_num],T_curr_loc[tail_num+1]) > 1.5):
                        T_curr_loc[tail_num],T_curr_loc[tail_num+1] = move_tail(T_curr_loc[tail_num],T_curr_loc[tail_num+1])
                end_of_tail = T_curr_loc[8]
                T_locs.add((end_of_tail[0],end_of_tail[1]))
            move_dist -= 1

    if (direction == "L"):
        while (move_dist > 0):
            H_loc[1] -= 1
            #check if tail needs to move
            if (get_dist_between_locs(H_loc, T0_loc) > 1.5):
                H_loc,T0_loc = move_tail(H_loc,T0_loc)
                for tail_num in range (0,8):
                    if (get_dist_between_locs(T_curr_loc[tail_num],T_curr_loc[tail_num+1]) > 1.5):
                        T_curr_loc[tail_num],T_curr_loc[tail_num+1] = move_tail(T_curr_loc[tail_num],T_curr_loc[tail_num+1])
                end_of_tail = T_curr_loc[8]
                T_locs.add((end_of_tail[0],end_of_tail[1]))
            move_dist -= 1

    if (direction == "U"):
        while (move_dist > 0):
            H_loc[0] -= 1
            if (get_dist_between_locs(H_loc, T0_loc) > 1.5):
                H_loc,T0_loc = move_tail(H_loc,T0_loc)
                for tail_num in range (0,8):
                    if (get_dist_between_locs(T_curr_loc[tail_num],T_curr_loc[tail_num+1]) > 1.5):
                        T_curr_loc[tail_num],T_curr_loc[tail_num+1] = move_tail(T_curr_loc[tail_num],T_curr_loc[tail_num+1])
                end_of_tail = T_curr_loc[8]
                T_locs.add((end_of_tail[0],end_of_tail[1]))
            move_dist -= 1

    if (direction == "D"):
        while (move_dist > 0):
            H_loc[0] += 1
            if (get_dist_between_locs(H_loc, T0_loc) > 1.5):
                H_loc,T0_loc = move_tail(H_loc,T0_loc)
                for tail_num in range (0,8):
                    if (get_dist_between_locs(T_curr_loc[tail_num],T_curr_loc[tail_num+1]) > 1.5):
                        T_curr_loc[tail_num],T_curr_loc[tail_num+1] = move_tail(T_curr_loc[tail_num],T_curr_loc[tail_num+1])
                end_of_tail = T_curr_loc[8]
                T_locs.add((end_of_tail[0],end_of_tail[1]))
            move_dist -= 1

    H_curr_loc.append(H_loc)

def get_dist_between_locs(head,tail):
    
    x_dist = abs(head[1] - tail[1])
    y_dist = abs(head[0] - tail[0])

    #print (x_dist,",",y_dist)

    dist = math.dist(head,tail)
    #print ("checking distance:",head,tail,"-->",dist)
    return dist

def move_tail(head,tail):
    if (head[0] == tail[0]):
        #on the same horizontal line
        if (head[1] > tail[1]):
            tail[1] += 1
        else:
            tail[1] -= 1
    elif (head[1] == tail[1]):
        #on the same vertical line
        if (head[0] > tail[0]):
            tail[0] += 1
        else:
            tail[0] -= 1
    else:
        #print ("must be diagonal:",head,tail)
        #diagonally seperated
        if (head[0] < tail[0]):
            #head above
            if (head[1] > tail[1]):
                #head to the right
                tail[0] -= 1
                tail[1] += 1
            else:
                tail[0] -= 1
                tail[1] -= 1
                #head to the left
        else:
            #head below
            if (head[1] > tail[1]):
                #head to the right
                tail[0] += 1
                tail[1] += 1
            else:
                tail[0] += 1
                tail[1] -= 1
                #head to the left
        #print ("moved diagonally:",head,tail)
            
    return head,tail


def main():

    #filename = "aoc_2022_input_9-test2.txt"
    filename = "aoc_2022_input_9.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    global H_curr_loc
    H_curr_loc = []
    global T_locs
    T_locs = set()
    global T_curr_loc
    T_curr_loc = []

    H_curr_loc.append([0,0])

    for i in range(9):
        T_curr_loc.append([0,0])

    
    T_locs.add((0,0))

    for idx,vals in enumerate(input_data):
        process_instruction(vals)
        #print (H_curr_loc,T_curr_loc)
     
    print ("Number of unique tail locations:",len(T_locs))
##end main  
main()

