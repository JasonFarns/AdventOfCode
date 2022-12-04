#!/usr/bin/python3
import sys
import os


input_file = "input1.txt"

#depth_measurements = system_cmd_stream.readlines()
depth_readings = []
trending_deeper = 0

with open(input_file) as filereader:
    print ('Reading depths from ',input_file)
    for line in filereader:
        line = line.strip()
        depth_readings.append(line)

filereader.close()

depths_count = len(depth_readings)
print ("Number of measurements: ",depths_count)

for i in range(depths_count):
    if (i < 3):
        continue
    else:
        if ((depths_count - i) < 1):
            print ("Exiting calculation at position: ",i)
            break
        else:         
            r1_1 = i - 3
            r1_2 = i - 2
            r1_3 = i - 1
            range1_sum = int(depth_readings[r1_1]) + int(depth_readings[r1_2]) + int(depth_readings[r1_3])
            
            r2_1 = i - 2
            r2_2 = i - 1
            r2_3 = i
            range2_sum = int(depth_readings[r2_1]) + int(depth_readings[r2_2]) + int(depth_readings[r2_3])
    
            if (range2_sum > range1_sum):
                trending_deeper+=1

# done scanning depths
print ("We went deeper: ",trending_deeper," times")

