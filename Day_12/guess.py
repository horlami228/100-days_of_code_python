import random
import os
"""This program selects a random number and user tries to guess the number"""
def easy():
    """ Takes no arguement performs the easy part of the game """
    attempt = 10
    while(attempt != 0):
        try:
            print("You have {} attempt remaining".format(attempt))
            guess = int(input("Make a guess: "))
            if guess != number:
                attempt -= 1
            if guess < number:
                print("Too low")
            if guess > number:
                print("Too high")
            if attempt == 0:
                print("You have run out of guesses")
            if guess == number:
                print("You got the correct number")
                break
        except(ValueError, TypeError):
            print("Only numbers")
def hard():
    attempt = 4
    while(attempt != 0):
        try:
            print("You have {} attempt remaining".format(attempt))
            guess = int(input("Make a guess: "))
            if guess != number:
                attempt -= 1
            if guess < number:
                print("Too low")
            if guess > number:
                print("Too high")
            if attempt == 0:
                print("You have run out of guesses")
            if guess == number:
                print("You got the correct number")
                break
        except(ValueError, TypeError):
            print("Only numbers")

game_start = True
while game_start:
    number = random.randrange(1, 101) # a random number from 1 to 100
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
    if difficulty == "easy":
        easy()
    elif difficulty == "hard":
        hard()
    else:
        print("Incorrect input")
    will_play = input("Do you want to play again. Type 'y' to play, Type 'n' to end: ")
    if will_play == "n":
        game_start = False
    elif will_play == "y":
        os.system("clear")
    else:
        print("Wrong input")
        
