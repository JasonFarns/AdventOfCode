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

        more_packets_exist = True
        while more_packets_exist:
            try:
                versions_total += self.get_packet_version()
                versions_total += self.skip_over_remaining_packet()
            except:
#                print ("\n!! Exception. Trying to read more packets !!\n")
                more_packets_exist = False

            more_packets_exist = self.are_packets_remaining()
            #more_packets_exist = False ##### testing #####

        return versions_total

    def are_packets_remaining(self):
        if (len(list(self.bin_msg_list)) < 6): # if there is not a complete header's worth of bits
            return False
        else: # need to try and read the next complete packet to confirm a valid packet exists?
            return True

    def skip_over_remaining_packet(self):
        packet_type = self.get_packet_type()

        if (int(packet_type) == 4):
            self.pop_literal_packet_payload()
            versions_total_returned = 0
        else: # any other type
            payload_return = self.get_operator_payload()
            versions_total_returned = payload_return[0]
#            versions_total_returned = self.get_operator_payload()[0]

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
        return num_bits_popped

    def get_operator_payload(self):
        version_totals_to_return = 0
        bits_popped = 0

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

                if (sub_packet_type == 4):
#                    print ("Variable containing literal packet")
                    literal_packet_bits_popped = self.pop_literal_packet_payload()
                    sub_packet_bit_length -= literal_packet_bits_popped
                    bits_popped += literal_packet_bits_popped
                else:
#                    print ("Variable operator containing operator packet")
                    recurse_return_vals = self.get_operator_payload()
                    version_totals_to_return += recurse_return_vals[0]
                    bits_popped += recurse_return_vals[1]


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
               
                bits_popped += 6

                if (sub_packet_type == 4):
#                    print ("Definite containing literal packet")
                    bits_popped += self.pop_literal_packet_payload()
                else:
#                    print ("Definite operator containing operator packet")
                    recurse_return_vals = self.get_operator_payload()
                    version_totals_to_return += recurse_return_vals[0]
                    bits_popped += recurse_return_vals[1]

                num_sub_packets -= 1
#                print ("sub packets remaining:",num_sub_packets)

        return version_totals_to_return,bits_popped
    
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

    #input_data = ['38006F45291200']
    #input_data = ['EE00D40C823060']
    #input_data = ['8A004A801A8002F478']
    #input_data = ['620080001611562C8802118E34']
    #input_data = ['C0015000016115A2E0802F182340']
    #input_data = ['A0016C880162017C3686B18A3D4780']

    elf_msg = BITS(input_data)
    binary_msg = elf_msg.get_bin_string()
    print (input_data,'-->',binary_msg)    

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
