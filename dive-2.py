#!/usr/bin/python3
import sys
import os


input_file = "input2.txt"

depth_readings = []
course = []
#trending_deeper = 0

with open(input_file) as filereader:
    print ('Reading course from ',input_file)
    for line in filereader:
        line = line.strip()
        course.append(line)

filereader.close()

course_len = len(course)
print ("Number of manuvers: ",course_len)

horiz_pos = 0;
depth_pos = 0;
aim = 0;



for i in range(course_len):
   cmd = course[i].split()
   direction = str(cmd[0])
   distance = int(cmd[1])
   
   if (direction == "forward"):
       #add horizontal pos
       horiz_pos += distance
       depth_pos += aim * distance
       continue
   if (direction == "down"):
       #add depth
       aim += distance
       continue
   if (direction == "up"):
       #subtract depth
       aim -= distance
       continue

# done scanning course
position_product = horiz_pos * depth_pos
print ("Final location: ",horiz_pos,"H, ",depth_pos,"D")
print ("Product: ",position_product)

