import random
# a rock paper scissors game
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
while True:
    user = int(input("Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors.\n"))
# print the ascii art according to user input
# make ascii art into a list
    game_img = [rock, paper, scissors]
    if user == 0 or user == 1 or user == 2:
        print(game_img[user])
    else:
        print("Invalid number, Only pick(0, 1, 2).")
        continue
# lets make the computer pick at random

    computer = random.randint(0, 2)

# print the ascii art according to computer input
    print()
    print("Computer chose:")
    print()
    print(game_img[computer])

    """
    rock wins against scissors.
    scissors wins against paper.
    paper wins against rock.
    """
    if user == 0 and computer == 2:
        print("You win")
        break
    elif user == 2 and computer == 1:
        print("you win")
        break
    elif user == 1 and computer == 0:
        print("You win")
        break
    elif user == computer:
        print("It's a draw")
        break
    else:
        print("You lose")
        break