#!/usr/bin/python3
import sys
import os
import re

def parse_cmd(input):
    input = input.split(" ")
    if (input[1]== "cd"):
        target_dir = input[2]
        #print ("changing directory to",target_dir)
        change_dir(target_dir)
        #print (curr_dir)
    elif (input[1] == "ls"):
        #print ("listing dir",input)
        list_contents()

def change_dir(target_dir):
    if (len(curr_dir) == 0):
        curr_dir.append(target_dir)
    else:
        if (target_dir == ".."):
            #move upwards
            curr_dir.pop()
        else:
            curr_dir.append(target_dir)

def list_contents():
    path = ""
    for idx,ele in enumerate(curr_dir):
        if (ele != "/"):
            path += ele + "/"
        else:
            path += ele
    
    new_dir_entry = [path,0]
    filesystem_stats.append(new_dir_entry)

def add_to_filesystem(entry):
    entry = entry.split(" ")
    #curr_path = filesystem_stats[-1:][0]
    curr_path = filesystem_stats.pop()
    if (entry[0] == "dir"):
        #need to add to filesystem_layout
        if (curr_path[0] not in filesystem_layout):
            fs_layout_entry = curr_path[0] + entry[1]
            filesystem_layout.append(fs_layout_entry)
    else:
        #need to add to filesystem_stats
        filesize = int(entry[0])
        curr_path[1] += filesize
        #print ("adding size to:",curr_path)
        #bubble the size info up the filestem layout
        if (curr_path[0] != "/"):
            prev_path = curr_path[0].split("/")
            prev_path[0] = "/"
            prev_path.pop()
            #prev_path.pop()
            
            while (len(prev_path) > 0):
                update_path = "/"
                for idx,val in enumerate(prev_path):
                    if (val != "/"):
                        update_path += val + "/"
            
                #print("next to update:",update_path)
                for idx,val in enumerate(filesystem_stats):
                    if (val[0] == update_path):
                        #print ("updating stats on:",val,"because of",entry)
                        filesystem_stats[idx][1] += filesize
            
                prev_path.pop()

    filesystem_stats.append(curr_path)

def main():

    #filename = "aoc_2022_input_7-test.txt"
    filename = "aoc_2022_input_7.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    global filesystem_stats
    filesystem_stats = []
    global filesystem_layout
    filesystem_layout = []
    global curr_dir
    curr_dir = []
    global ls_path
    ls_path = ""

    for idx,vals in enumerate(input_data):
        if (vals[0] == "$"):
            parse_cmd(vals)
        else:
            #not a command, so add file info to filesystem list
            add_to_filesystem(vals)
            
    print ("Directories:",filesystem_layout)
    print ("FS stats:",filesystem_stats)

    size_calc = 0
    for idx,vals in enumerate(filesystem_stats):
        if (vals[1] <= 100000):
            size_calc += vals[1]

    print ("resulting sum of directories under 100000:",size_calc)

        
        


    
##end main  
main()

