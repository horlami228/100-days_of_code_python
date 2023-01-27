import random
# create a toin coss program

# ask for a seed value
seed_value = int(input("What is the seed value: "))
random.seed(seed_value)

# generate random number from 0 to 1
coin = random.randint(0, 1)
if coin == 1:
    print("Heads")
else:
    print("Tails")