#!/usr/bin/python3
import sys
import os
import re

def bingo_winner (winning_number, card_index, card_data):
    print ("WINNER! Card",card_index,"With lucky number",winning_number)
    card_value_total = 0
    for line in card_data:
        print (line)
        for data in line:
            if data.isnumeric():
                card_value_total += int(data)

    score = card_value_total * int(winning_number)
    return score

#end bingo winner function

def main():

    #input_file = "input4-test.txt"
    input_file = "input4.txt"
    bingo_data = []
    
    with open(input_file) as filereader:
        print ('Reading data from ',input_file)
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
    
    bingo = False
    winning_cards = []
    winners = []
    full_winner_details = []
    #evaluate bingo card for winning potential??
    for num in called_numbers:
        for i in range(len(bingo_cards)):
            #each bingo card
            for j in range(len(bingo_cards[i])):
                #each line in the bingo card
                for k in range(len(bingo_cards[i][j])):
                #each number in the bingo card line
                    if str(bingo_cards[i][j][k]) == str(num):
                        bingo_cards[i][j][k] = "x"

                #check for horizontal bingo!
                if str(bingo_cards[i][j]) == "['x', 'x', 'x', 'x', 'x']":
                    #BINGO!!!
                    if i not in winners:
                        score = bingo_winner(num,i,bingo_cards[i])
                        print ("Horizontal Score:",score)
                        winners.append(i)
                        card_info = [i,score]
                        winning_cards.append(card_info)
                        full_winner_details.append(bingo_cards[i])
                        #break

                #check for vertical bingo!
                pos = 0
                row = j - 4
                while pos < 5:
                    if (bingo_cards[i][row][pos] != 'x'):
                        if (row == 0):
                            pos += 1
                        else:
                            break
                    else:
                        if row < 4:
                            row += 1
                        else:
                            #BINGO!!!
                            if i not in winners:
                                score = bingo_winner(num,i,bingo_cards[i])
                                print ("Vertical Score:",score)
                                winners.append(i)
                                card_info = [i,score]
                                winning_cards.append(card_info)
                                full_winner_details.append(bingo_cards[i])
                            break
        
    #end winning number search

    #print (winning_cards)
    final_winner = winning_cards.pop()
    print ("Last one to win:",final_winner)

    #num_winning_boards = len(winners)
    num_winning_boards = len(full_winner_details)
    print ("Total winning cards:",num_winning_boards)

#    for card in full_winner_details:
#        print ("Card")
#        for line in card:
#            print (line)



#    for card in bingo_cards:
#        print ("Bingo card:")
#        for line in card:
#            print (line)
#end main  
   
main()
