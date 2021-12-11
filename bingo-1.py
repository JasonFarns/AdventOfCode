#!/usr/bin/python3
import sys
import os
import re

def main():

    input_file = "input4.txt"
    bingo_data = []
    
    with open(input_file) as filereader:
        print ('Reading diagnostics from ',input_file)
        for line in filereader:
            line = line.strip()
            bingo_data.append(line)
    
    filereader.close()

    called_numbers = bingo_data.pop(0).split(',')
    bingo_data.pop(0)

    bingo_cards = []
    while bingo_data:
        #grab 5 bingo card lines
        card_line1 = bingo_data.pop(0).split(' ')
        card_line1 = [i for i in card_line1 if i]
        card_line2 = bingo_data.pop(0).split(' ')
        card_line2 = [i for i in card_line2 if i]
        card_line3 = bingo_data.pop(0).split(' ')
        card_line3 = [i for i in card_line3 if i]
        card_line4 = bingo_data.pop(0).split(' ')
        card_line4 = [i for i in card_line4 if i]
        card_line5 = bingo_data.pop(0).split(' ')
        card_line5 = [i for i in card_line5 if i]
        #skip blank line
        try:
            bingo_data.pop(0)
        except:
            print ("Bingo cards created!")
        #add to a bingo card object
        bingo_card = [card_line1,card_line2,card_line3,card_line4,card_line5]
        bingo_cards.append(bingo_card)
    #end bingo card creation
    
    winning_numbers = []
    bingo = False
    #evaluate bingo card for winning potential??
    for num in called_numbers:
        print (num)
        for i in range(len(bingo_cards)):
            #each bingo card
            for j in range(len(bingo_cards[i])):
                #each line in the bingo card
                bingo_number = None
                bingo_number = num in bingo_cards[i][j]
                if bingo_number:
                    if num not in winning_numbers:
                        winning_numbers.append(num)
                    for k in range(len(bingo_cards[i][j])):
                        #each number in the bingo card line
                        if str(bingo_cards[i][j][k]) == str(num):
                            bingo_cards[i][j][k] = "x"
                            j = len(bingo_cards[i]) - 1
                        #check for horizontal bingo!
                        if bingo_cards[i][j] == ['x','x','x','x','x']:
                            bingo = True
                            print ("BINGO! With",num,"at card index",i)
                            print (bingo_cards[i])
                            break
                    if bingo == True: #before checking next item in line
                        break
                if bingo == True: #before moving to next line
                    break
            if bingo == True: #before moving to next card
                break

            #check for vertical bingo!
#            print ("Currently on card",i,", row",j)
            pos = 0
            row = j - 4
            while pos < 5:
                #print (bingo_cards[i])
                if (bingo_cards[i][row][pos] != 'x'):
                    if (row == 0):
                        pos += 1
                    else:
                        break
                else:
                    if row < 4:
                        row += 1
                    else:
                        print ("BINGO! With",num,"at card index",i)
                        print (bingo_cards[i])
                        bingo = True
                        break
        
            if bingo == True:
                print ("Card:",i)
                row = 0
                pos = 0
                remaining_numbers_total = 0
                while row < 5:
                    while pos < 5:
                        entry = bingo_cards[i][row][pos]
                        if (entry.isnumeric()):
                            remaining_numbers_total += int(entry)
                        pos += 1
                    pos = 0
                    row += 1
                print ("Board score:",remaining_numbers_total)

        if bingo == True: #before calling next number
            winning_score = int(num) * int(remaining_numbers_total)
            print ("Winning score:",winning_score)
            break
    #end winning number search

    all_nums = len(called_numbers)
    winning_nums = len(winning_numbers)
    print ("Found",winning_nums,"winning numbers out of",all_nums)

    #print(bingo_cards)

#end main  
   
main()
