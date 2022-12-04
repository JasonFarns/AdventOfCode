#!/usr/bin/python3
import sys
import os


input_file = "input1.txt"

#depth_measurements = system_cmd_stream.readlines()
depth_readings = []
curr_depth_larger_than_previous = 0

with open(input_file) as filereader:
    print ('Reading depths from ',input_file)
    for line in filereader:
        line = line.strip()
        depth_readings.append(line)

filereader.close()

depths_count = len(depth_readings)
print ("Number of measurements: ",depths_count)
for i in range(depths_count):
    if (i == 0):
        continue
    else:
        curr_depth = int(depth_readings[i])
        p = i-1
        prev_depth = int(depth_readings[p])

        if (curr_depth > prev_depth):
            curr_depth_larger_than_previous+=1
#        else:
#            print (prev_depth," -->> ",curr_depth)

# done scanning depths
print ("We went deeper: ",curr_depth_larger_than_previous," times")

