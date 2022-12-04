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

    fish_population = [int(x) for x in list(input_data[0].split(','))]
    baby_fish = 0
    gen7_fish = 0
    gen6_fish = 0
    gen5_fish = 0
    gen4_fish = 0
    gen3_fish = 0
    gen2_fish = 0
    gen1_fish = 0
    gen0_fish = 0
    for idx,fish in enumerate(fish_population):
        if fish == 8:
            baby_fish += 1
        if fish == 7:
            gen7_fish += 1
        if fish == 6:
            gen6_fish += 1
        if fish == 5:
            gen5_fish += 1
        if fish == 4:
            gen4_fish += 1
        if fish == 3:
            gen3_fish += 1
        if fish == 2:
            gen2_fish += 1
        if fish == 1:
            gen1_fish += 1
        if fish == 0:
            gen0_fish += 1
    # end fish generation buckets
    print (".:: Population sizes ::.\n\tbabies:",baby_fish,"\n\tteenagers:",gen7_fish,"\n\t6 days:",gen6_fish,"\n\t5 days:",gen5_fish,"\n\t4 days:",gen4_fish,"\n\t3 days:",gen3_fish,"\n\t2 days:",gen2_fish,"\n\t1 day:",gen1_fish,"\n\tpregnant fish:",gen0_fish)

    day = 0
    end_day = 80 
    while day < end_day:
        no_longer_pregnant_fish = gen0_fish
        gen0_fish = gen1_fish
        gen1_fish = gen2_fish
        gen2_fish = gen3_fish
        gen3_fish = gen4_fish
        gen4_fish = gen5_fish
        gen5_fish = gen6_fish
        gen6_fish = no_longer_pregnant_fish + gen7_fish
        gen7_fish = baby_fish
        baby_fish = no_longer_pregnant_fish

        day += 1
    # end day progression


    print (".:: Population sizes ::.\n\tbabies:",baby_fish,"\n\tteenagers:",gen7_fish,"\n\t6 days:",gen6_fish,"\n\t5 days:",gen5_fish,"\n\t4 days:",gen4_fish,"\n\t3 days:",gen3_fish,"\n\t2 days:",gen2_fish,"\n\t1 day:",gen1_fish,"\n\tpregnant fish:",gen0_fish)
    total_population = gen0_fish + gen1_fish + gen2_fish + gen3_fish + gen4_fish + gen5_fish + gen6_fish + gen7_fish + baby_fish
    print ("Fish population after",end_day,"days:",total_population)
        


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
