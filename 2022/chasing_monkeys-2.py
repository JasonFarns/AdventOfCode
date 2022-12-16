#!/usr/bin/python3
import sys
import os
import re
from math import floor
sys.set_int_max_str_digits(1920000)
        

def main():

    #filename = "aoc_2022_input_11-test.txt"
    filename = "aoc_2022_input_11.txt"
    input_file = os.path.join("C:\\", "Users", "Jason", "Google Drive", "Geek Stuff", "Python code", "AdventOfCode", "2022", filename)
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()
    
    global important_clock_values
    important_clock_values = set()

    monkey_inventories = []
    monkey_ops = []
    monkey_tests = []
    monkey_business = []

    for idx in range(len(input_data)):
        line = str(input_data[idx]).split(" ")
        if (line[0] == "Monkey"):
            monkey_num = int(line[1][:-1])
            monkey_business.insert(monkey_num, 0)

            idx += 1
            
            line = str(input_data[idx]).split(" ")
            line.reverse()
            line.pop()
            line.pop()

            line.reverse()
            for inv in range(len(line)):
                entry = str(line[inv]).split(",")
                line[inv] = int(entry[0])
                
            monkey_inventories.insert(monkey_num, line)

            idx += 1
            line = str(input_data[idx]).split(" ")
            line.reverse()
            line.pop()
            line.pop()
            line.pop()
            line.reverse()
            monkey_ops.insert(monkey_num, line)

            idx += 1
            line = str(input_data[idx]).split(" ")
            test = int(line[-1])

            idx += 1
            line = str(input_data[idx]).split(" ")
            true_target = line[-1]

            idx += 1
            line = str(input_data[idx]).split(" ")
            false_target = line[-1]

            new_test = [test, true_target, false_target]
            monkey_tests.insert(monkey_num, new_test)


    #print (monkey_inventories)
    #print (monkey_ops)
    #print (monkey_tests)
    #print (monkey_business)
    
    monkey_test_vals = []
    for idx in range(len(monkey_tests)):
        monkey_test_vals.append(monkey_tests[idx][0])
        monkey_test_vals.append("*")
    
    monkey_test_vals.pop()
    monkey_test_vals_expression = ""
    
    for ele in monkey_test_vals:
        monkey_test_vals_expression += str(ele)

    worry_reducer_modulo = eval(monkey_test_vals_expression)
    print (worry_reducer_modulo)

    

    num_rounds = 10000
    #num_rounds = 20
    for round in range(num_rounds):
        curr_monkey = 0
        for curr_monkey in range(len(monkey_business)):
            inventory = monkey_inventories[curr_monkey]
            item = 0
            for item in range(len(inventory)):
                item_worry_level = inventory[item]
                formula = "("
                for i in range(0,3):
                    if (monkey_ops[curr_monkey][i] == "old"):
                        formula += str(item_worry_level)
                    else:
                        formula += monkey_ops[curr_monkey][i]
                
                #formula += ")/3"
                formula += ") % worry_reducer_modulo"

                result = eval(formula)
                new_worry_level = floor(result)
                
                divisor = monkey_tests[curr_monkey][0]
                if ((new_worry_level % divisor) == 0):
                    #true
                    toss_to_monkey = int(monkey_tests[curr_monkey][1])
                else:
                    #false
                    toss_to_monkey = int(monkey_tests[curr_monkey][2])

                #toss item to appropriate monkey
                monkey_inventories[toss_to_monkey].append(new_worry_level)
                
                #update monkey business counter
                monkey_business[curr_monkey] += 1
    
            #don't forget to wipe out current monkey inventory
            empty_inventory = []
            monkey_inventories[curr_monkey] = empty_inventory
    

    #print (monkey_inventories)    
    monkey_business.sort(reverse = True)
    print ("Monkey business:", monkey_business)

    product_of_most_biz = monkey_business[0] * monkey_business[1]
    print ("Highest Monkey biz product:", product_of_most_biz)

    


##end main  
main()

