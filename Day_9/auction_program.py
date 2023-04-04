#!/usr/bin/python3
import os
# This is an auction program
# It selects the heights bidder

# create an empty dictionary and empty list
auction_list = []
auction_dic = {}
print("Welcome to the secret auction program")

while(True): # Bidding ends when there are no other bidders
    # Ask user for input
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    auction_dic[name] = bid # create a dictionary key and value from user input

    end_loop = input("Are there any other bidders? Type 'yes' or 'no'\n")
    os.system("clear")
    if end_loop in ["no", "No"]:
        break

for keys in auction_dic:
    auction_list.append(auction_dic[keys])
sum = max(auction_list) # get the maximum number in the list

# loop through to find key to value same as the maximum number
for key in auction_dic:
    if auction_dic[key] == sum:
        bidder_name = key #save the key in a variable


# print out the highest bidders name with thier bid
print("The winner is {} with a bid of ${}".format(bidder_name, sum))