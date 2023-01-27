# a program to random select who to pay the bill

import random

# ask for a seed number
seed_number = int(input("Create a seed number: "))
random.seed(seed_number)

# ask for the names of everyone to pay a bill

Everyname = input("Enter the name of everyone paying, seperated by a comma\n")
# split the names after the comma
name = Everyname.split(", ")

# lets generate a random number with it
num = random.randint(0, len(name) - 1)
# use the random number as index to print out a random name
print("{} is going to pay for the meal today!".format(name[num]))