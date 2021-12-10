#!/usr/bin/python3
import sys
import os


input_file = "input3.txt"
diagnostics = []

with open(input_file) as filereader:
    print ('Reading diagnostics from ',input_file)
    for line in filereader:
        line = line.strip()
        diagnostics.append(line)

filereader.close()

diagnostic_len = len(diagnostics)
print ("Number of diagnostic codes: ",diagnostic_len)

zero_bits_totals = []
one_bits_totals = []

length_of_codes = len(diagnostics[0])
for i in range(length_of_codes):
    zero_bits_totals.append(0)
    one_bits_totals.append(0)

for i in range(diagnostic_len):
    code = diagnostics[i]
    code_len = len(code)
    for j in range(code_len):
        digit = int(code[j])
        if (digit == 0):
            zero_bits_totals[j] += 1
        else:
            one_bits_totals[j] += 1
 
# done scanning codes

gamma_rate = []
epsilon_rate = []

for i in range(length_of_codes):
    if (zero_bits_totals[i] > one_bits_totals[i]):
        gamma = 0
        epsilon = 1
    else:
        gamma = 1
        epsilon = 0

    gamma_rate.append(gamma)
    epsilon_rate.append(epsilon)

print ("Zeros count is:",zero_bits_totals)
print ("Ones count is:",one_bits_totals)

print ("Gamma result:",gamma_rate)
print ("Epsilon result:",epsilon_rate)

gamma_string = ''.join(str(element) for element in gamma_rate)
gamma_int = int(gamma_string,2)
print ("Gamma value in integer is:",gamma_int)

epsilon_string = ''.join(str(element) for element in epsilon_rate)
epsilon_int = int(epsilon_string,2)
print ("Epsilon value in integer is:",epsilon_int)

gamma_epsilon_product = gamma_int * epsilon_int
print ("Gamma x Epsilon product:",gamma_epsilon_product)

#position_product = horiz_pos * depth_pos
#print ("Final location: ",horiz_pos,"H, ",depth_pos,"D")
#print ("Product: ",position_product)

