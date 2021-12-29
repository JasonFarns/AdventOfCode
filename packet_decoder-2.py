#!/usr/bin/python3
import sys
import os
import re

class BITS:
    def __init__ (self, input):
        self.transmission = input[0]


    def get_bin_string(self):
        self.bin_msg_string = ''
        hex_msg = list(self.transmission)
        for hex_char in hex_msg:
            bin_value = str(bin(int(hex_char, base=16)))[2:].zfill(4)
            self.bin_msg_string += bin_value

        self.bin_msg_list = list(self.bin_msg_string)
        return self.bin_msg_string

    def get_all_packets_versions_total(self):
        versions_total = 0

        versions_total += self.get_packet_version()
        versions_total += self.scan_over_remaining_packet()

        return versions_total

    def are_packets_remaining(self):
        if (len(self.bin_msg_list) < 6): # if there is not a complete header's worth of bits
            return False
        else: # need to try and read the next complete packet to confirm a valid packet exists?
            return True

    def scan_over_remaining_packet(self):
        packet_type = int(self.get_packet_type())

        if (packet_type == 4):
            literal_value = self.pop_literal_packet_payload()[0]
            versions_total_returned = 0
        else: # any other type
            #ID 0: sum
            #ID 1: product
            #ID 2: min
            #ID 3: max
            #ID 5: 1 if 1st sub is greater than  2nd
            #ID 6: 1 if 1st sub is less than 2nd
            #id 7: 1 if subs are equal

            operator_rules = {0:'add',1:'mult',2:'ret_min',3:'ret_max',5:'greater',6:'less',7:'equal'}
            operation = operator_rules[packet_type]

            returned_results = list(self.get_operator_payload(operation))
            versions_total_returned = returned_results.pop(0)
            returned_results.pop(0)
            returned_values = returned_results.pop(0)
            print ("Result of logic:",returned_values)
            

        return versions_total_returned


    def get_packet_version(self):
        packet_version = ''
#        print (self.bin_msg_list)
#        num_bits_remaining = len(self.bin_msg_list)
#        print ("Num bits remaining:",num_bits_remaining)
        bit1 = self.bin_msg_list.pop(0)
        bit2 = self.bin_msg_list.pop(0)
        bit3 = self.bin_msg_list.pop(0)
        
        packet_version_bits = bit1 + bit2 + bit3
        packet_version = int(packet_version_bits, 2)

#        print ("Version:",packet_version)
        return packet_version
   
    def get_packet_type(self):
        packet_type = ''
        bit1 = self.bin_msg_list.pop(0)
        bit2 = self.bin_msg_list.pop(0)
        bit3 = self.bin_msg_list.pop(0)

        packet_type_bits = bit1 + bit2 + bit3
        packet_type = int(packet_type_bits, 2)

        return packet_type

    def pop_literal_packet_payload(self):
        literal_payload = ''
        literal_payload_filtered = ''
        num_bits_popped = 0

        more_bits = True
        while (more_bits == True):
            try:
                has_more_groups_bit = self.bin_msg_list.pop(0)
                for i in range(4):
                    literal_payload_filtered += self.bin_msg_list.pop(0)

                num_bits_popped += 5
                if (int(has_more_groups_bit) == 0):
                    more_bits = False
            except:
                more_bits = False
        
        literal_payload = int(literal_payload_filtered,2)
        #print ('value:',literal_payload)
        return num_bits_popped,literal_payload

    def get_operator_payload(self, operation):
        version_totals_to_return = 0
        bits_popped = 0
        returned_literals = []

        length_type = self.bin_msg_list.pop(0)
        bits_popped += 1

        get_next_bits = 11
        if (int(length_type) == 0):
            get_next_bits = 15

        operator_payload = ''
        i = 0
        while (i < get_next_bits):
            operator_payload += self.bin_msg_list.pop(0)
            i += 1
        bits_popped += get_next_bits

        if (int(length_type) == 0):
            #sub-packets bit length referenced by/following this operator
            sub_packet_bit_length = int(operator_payload, 2)
#            print ("Operator --> variable bit length:",sub_packet_bit_length)

            while (sub_packet_bit_length > 0):
                if (len(self.bin_msg_list) < 11):
                    sub_packet_bit_length = 0
                    bits_popped += 11
                    continue

 #               print ("calling version check from variable length")

                version_totals_to_return += self.get_packet_version()
                sub_packet_type = self.get_packet_type()
                sub_packet_bit_length -= 6
                bits_popped += 6

                operator_rules = {0:'add',1:'mult',2:'ret_min',3:'ret_max',5:'greater',6:'less',7:'equal'}
                if (sub_packet_type != 4):
                    next_operation = operator_rules[sub_packet_type]

                if (sub_packet_type == 4):
#                    print ("Variable containing literal packet")
                    literal_payload_returned = self.pop_literal_packet_payload()
                    bits_popped += literal_payload_returned[0]
                    sub_packet_bit_length -= literal_payload_returned[0]
                    returned_literals.append(literal_payload_returned[1])
#                    print (returned_literals,operation)


                else:
#                    print ("Variable operator containing operator packet")
                    recurse_return_vals = self.get_operator_payload(next_operation)
                    version_totals_to_return += recurse_return_vals[0]
                    bits_popped += recurse_return_vals[1]
                    returned_literals.append(recurse_return_vals[2])
                    #print (returned_literals,operation,next_operation)

        else:
            #sub-packets number
            num_sub_packets = int(operator_payload, 2)
#            print ("Operator --> with sub-packets:",num_sub_packets)

            while (num_sub_packets > 0):
                if (len(self.bin_msg_list) < 11):
                    num_sub_packets = 0
                    bits_popped += 11
                    continue

#                print ("calling version check from definite packets")

                version_totals_to_return += self.get_packet_version()
                sub_packet_type = self.get_packet_type()

                operator_rules = {0:'add',1:'mult',2:'ret_min',3:'ret_max',5:'greater',6:'less',7:'equal'}
                if (sub_packet_type != 4):
                    next_operation = operator_rules[sub_packet_type]

                bits_popped += 6

                if (sub_packet_type == 4):
#                    print ("Definite containing literal packet")
                    literal_payload_returned = self.pop_literal_packet_payload()
                    bits_popped += literal_payload_returned[0]
                    returned_literals.append(literal_payload_returned[1])
#                    print (returned_literals,operation)
                else:
#                    print ("Definite operator containing operator packet")
                    recurse_return_vals = self.get_operator_payload(next_operation)
                    version_totals_to_return += recurse_return_vals[0]
                    bits_popped += recurse_return_vals[1]
                    returned_literals.append(recurse_return_vals[2])
                    #print (returned_literals,operation,next_operation)

                num_sub_packets -= 1
#                print ("sub packets remaining:",num_sub_packets)
       

        operation_result = ''
        if (operation == 'add'):
            operation_result = 0
            for value in returned_literals:
                operation_result += int(value)
        elif (operation == 'mult'):
            operation_result = 1
            for value in returned_literals:
                operation_result *= int(value)
        elif (operation == 'ret_min'):
            operation_result = 999999999999999999999999
            for value in returned_literals:
                if (int(value) < operation_result):
                    operation_result = int(value)
        elif (operation == 'ret_max'):
            operation_result = 0
            for value in returned_literals:
                if (int(value) > operation_result):
                    operation_result = int(value)
        elif (operation == 'greater'):
            operation_result = 0
            if (int(returned_literals[0]) > int(returned_literals[1])):
                operation_result = 1 
        elif (operation == 'less'):
            operation_result = 0
            if (int(returned_literals[0]) < int(returned_literals[1])):
                operation_result = 1 
        elif (operation == 'equal'):
            operation_result = 0
            if (int(returned_literals[0]) == int(returned_literals[1])):
                operation_result = 1 
        else:
            print ("Well, this is, uh... awkward...")

        return version_totals_to_return,bits_popped,operation_result
    
def main():

    #input_file = "input16-test.txt"
    input_file = "input16.txt"
    input_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
        for line in filereader:
            line = line.strip()
            input_data.append(line)
    filereader.close()

    ## part2 tests ##
    #input_data = ['C200B40A82']
    #input_data = ['04005AC33890']
    #input_data = ['880086C3E88112']
    #input_data = ['CE00C43D881120']
    #input_data = ['D8005AC2A8F0']
    #input_data = ['F600BC2D8F']
    #input_data = ['F600BC2D8F']
    #input_data = ['9C0141080250320F1802104A08']

    ## part1 tests ##
    #input_data = ['38006F45291200']
    #input_data = ['EE00D40C823060']

    elf_msg = BITS(input_data)
    binary_msg = elf_msg.get_bin_string()
#    print (input_data,'-->',binary_msg)    

    packet_version_numbers_total = elf_msg.get_all_packets_versions_total()
    print ("Sum of all packet version numbers:",packet_version_numbers_total)


#    packet_version = elf_msg.get_packet_version()
#    packet_type = elf_msg.get_packet_type()
#    print ('vers.',packet_version,'type:',packet_type)
#
#    if (packet_type == 4): #Type 4 holds literal values
#        elf_msg.get_msg_payload()

    
#end main  

main()
