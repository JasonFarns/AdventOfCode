#!/usr/bin/python3
import sys
import os
import re

def advance_day (population):
    new_fish = []
    for idx,fish in enumerate(population):
        if fish == 0:
            population[idx] = 6
            new_fish.append(8)
        else:
            fish -= 1
            population[idx] = fish
    # end for
    if len(new_fish) > 0:
        population = population + new_fish
    return population
## end advance_day

def main():

    #input_file = "input6-test.txt"
    input_file = "input6.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

#    fish_population = input_data
    fish_population = [int(x) for x in list(input_data[0].split(','))]

    day = 0
    end_day = 80
    while day < end_day:
        fish_population = advance_day(fish_population)
        #print (fish_population)
        day += 1
    # end day progression

    population_size = len(fish_population)
    print ("Fish population after",end_day,"days:",population_size)
##end main  
main()
