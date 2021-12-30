#!/usr/bin/python3
import sys
import os
import re

def get_next_pos_and_vel(pos,vel):
    new_x_pos = pos[0] + vel[0]
    new_y_pos = pos[1] + vel[1]
    new_pos = [new_x_pos,new_y_pos]

    if (vel[0] > 0):
        new_x_vel = vel[0] - 1
    elif (vel[0] < 0):
        new_x_vel = vel[0] + 1
    else:
        new_x_vel = vel[0]

    new_y_vel = vel[1] - 1
    
    new_vel = [new_x_vel,new_y_vel]

    return new_pos,new_vel

def probe_on_target(pos,x_range,y_range):

    x_pos_check = pos[0] in range(x_range[0],x_range[1])
    y_pos_check = pos[1] in range(y_range[0],y_range[1])

    if x_pos_check and y_pos_check:
        return True

    return False

def probe_beyond_target(pos,x_range,y_range):
    beyond_x = False
    beyond_y = False

    if (pos[0] > x_range[1]):
        beyond_x = True
    if (y_range[1] > pos[1]):
        beyond_y = True

    if beyond_x and beyond_y:
        return True
    if beyond_y:
        return True

    return False

def main():
    target_area = 'target area: x=57..116, y=-198..-148' ## problem data
#    target_area = 'target area: x=20..30, y=-10..-5'     ## test data

    target_area = target_area.split(':')
    target_area_x = target_area[1].split(',')[0].strip()
    target_area_y = target_area[1].split(',')[1].strip()
    target_area_x = target_area_x.split('=')[1]

    target_x_min = int(target_area_x.split('..')[0])
    target_x_max = int(target_area_x.split('..')[1])
    target_x = [target_x_min,target_x_max]

    target_area_y = target_area_y.split('=')[1]
    target_y_min = int(target_area_y.split('..')[0])
    target_y_max = int(target_area_y.split('..')[1])

#    if (abs(target_y_min) > abs(target_y_max)):
#        temp_y = target_y_min
#        target_y_min = target_y_max
#        target_y_max = temp_y

    target_y = [target_y_min,target_y_max]

    successful_shots = []

    for x in range(500):
        for y in range(500):

            curr_pos = [0,0]
            curr_vel = shot_vel = [x,y]
            #print ("New shot:",starting_vel)
            highest_y_pos = 0

            on_target = False
            beyond_target = False
            continue_stepping = True
            steps = 0
            while continue_stepping:
                curr_pos,curr_vel = get_next_pos_and_vel(curr_pos,curr_vel)
#                print ('Position:',curr_pos,'Velocity:',curr_vel)
                if (curr_pos[1] > highest_y_pos):
                    highest_y_pos = curr_pos[1]
                
                on_target = probe_on_target(curr_pos,target_x,target_y)
                if (on_target):
#                    print ("Target hit!")
                    shot_info = [shot_vel,highest_y_pos]
                    successful_shots.append(shot_info)
                    continue_stepping = False
                else:
                    beyond_target = probe_beyond_target(curr_pos,target_x,target_y)
                    if (beyond_target):
#                        print ("We went too far!")
                        continue_stepping = False

                steps += 1
                if (steps > 999):
                    print ("Timeout reached. (",x,',',y,') -->',curr_pos)
                    continue_stepping = False

    highest_alt = 0
    best_vel = ''

    for shot in successful_shots:
        vel = shot[0]
        alt = shot[1]
        if (alt > highest_alt):
            highest_alt = alt
            best_vel = vel
   
    print ("Highest shot is:",best_vel,'\tReaching:',highest_alt)
    print ("Successful shots:",len(successful_shots))
    

##end main  
main()
