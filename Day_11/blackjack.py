import random
import os
from blackjack_art import logo
print(logo)
"""This a black jack game"""
"""Create a function with a list of possible cards in black jack"""
def deal_card():
    while(True):
       # print()
        start_game = input("Do you want to play a game of Blackjack? Type 'y' to start. Type 'n' to end: ")
        if start_game == 'y':
            os.system("clear")
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            decks = cards * 4
            random.shuffle(decks)

            sum_user = 0
            sum_comp = 0
            # create a list for user and computer
            user = []
            comp = []

            # start with two cards for user and comp each
            for i in range(1, 3):
                user.append(decks.pop())
                comp.append(decks.pop())
            #calculate the values of the cards for both user and comp
            for i in user:
                sum_user += i
            for k in comp:
                sum_comp += k

            # print it two out for only the user, one for computer
            print("       Your cards: {}, current score: {}".format(user, sum_user))
            print("       Dealer's first card: {}".format(comp[0]))

            # make conditions to win if card value is 21 for blackjack
            if sum_user == 21 and sum_comp != 21:
                print("     Your final hand: {}, final score: {}".format(user, sum_user))
                print("     Dealer's final card is: {}, final score: {}".format(comp, sum_comp))
                print("Blackjack, You win 😁")
                deal_card()
            if sum_user != 21 and sum_comp == 21:
                print("     Your final hand: {}, final score: {}".format(user, sum_user))
                print("     Dealer's final hand: {}, final score: {}".format(comp, sum_comp))
                print("Dealer Blackjack, You loose 😭")
                deal_card()
            if sum_user == 21 and sum_comp == 21:
                print("     Your final hand: {}, final score: {}".format(user, sum_user))
                print("     Dealer's final hand: {}, final score: {}".format(comp, sum_comp))
                print("It's a draw 🙂")
                deal_card()
            while(True):
                pick_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if pick_card == 'y':
                    sum_user = 0
                    sum_comp = 0
                    user.append(decks.pop())
                    comp.append(decks.pop())
                    for i in user:
                        sum_user += i
                    for k in comp:
                        sum_comp += k

                    if sum_user > 21: # check if ace is present in list
                        if 11 in user:
                            sum_user = sum_user - 10
                            user.remove(11)
                            user.append(1)
                    if sum_comp > 21: #check if ace is present in list
                        if 11 in comp:
                            sum_comp = sum_comp - 10
                            comp.remove(11)
                            comp.append(1)
                    if sum_user > 21 and sum_comp <= 21:
                        print("     Your final hand: {}, final score: {}".format(user, sum_user))
                        print("     Dealer's final hand is: {}, final score: {}".format(comp, sum_comp))
                        print("You went over. You loose 😭")
                        deal_card()
                    if sum_user <= 21 and sum_comp > 21:
                        print("     Your final hand: {}, final score: {}".format(user, sum_user))
                        print("     Dealer's final hand: {}, final score: {}".format(comp, sum_comp))
                        print("Opponent went over. You win 😁")
                        deal_card()
                    if sum_user > 21 and sum_comp > 21:
                        print("     Your final hand: {}, final score: {}".format(user, sum_user))
                        print("     Dealer's final hand: {}, final score: {}".format(comp, sum_comp))
                        print("It's a bust. You draw 🙂")
                        deal_card()
                    else:
                        # print it two out for only the user one for comp
                        print("      Your cards: {}, current score: {}".format(user, sum_user))
                        print("      Dealer first card: {}".format(comp[0]))

                if pick_card == 'n':
                    # check who have the greater values 
                    if sum_user > sum_comp:
                        print("     Your final hand: {}, final score: {}".format(user, sum_user))
                        print("     Dealer's final hand: {}, final score: {}".format(comp, sum_comp))
                        print("You win 😁")
                    if sum_user < sum_comp:
                        print("     Your final hand: {}, final score: {}".format(user, sum_user))
                        print("     Dealer's final hand: {}, final score: {}".format(comp, sum_comp))
                        print("Dealer win 😭")
                    if sum_user == sum_comp:
                        print("     Your final card is: {}, final score: {}".format(user, sum_user))
                        print("     Dealer's final hand: {}, final score: {}".format(comp, sum_comp))
                        print("It's a draw 🙂")
                    deal_card()
        elif start_game == 'n':
            exit(98)
        else:
            print("Invalid input")
deal_card()