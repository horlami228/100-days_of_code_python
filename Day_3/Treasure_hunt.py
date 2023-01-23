#!/usr/bin/python3
print("Welcome to the Treasure Island")
print('''

  _                                       _                 _   
 | |_ _ __ ___  __ _ ___ _   _ _ __ ___  | |__  _   _ _ __ | |_ 
 | __| '__/ _ \/ _` / __| | | | '__/ _ \ | '_ \| | | | '_ \| __|
 | |_| | |  __| (_| \__ | |_| | | |  __/ | | | | |_| | | | | |_ 
  \__|_|  \___|\__,_|___/\__,_|_|  \___| |_| |_|\__,_|_| |_|\__|
                                                                

''')

print("Your mission is to find the hidden treasure")
start = input('Do you want to start this game? Yes or No\n')
# convert the input to lower case to avoid any errors
start.lower()
if start[0] == "y":
    print("Lets begin")
    left_right = input("You are getting chased by bandits. And now at a crossroad. Where would you like to go. "
                                            "Type \"left\" or type \"right\"\n")
    left_right.lower()
    if left_right == "right":
        wait = input("You made it past the bandits. Now you are at the beach. There is an island in the middle of the beach. "
        "Type \"wait\" to wait for a boat or Type \"swim\" to swim accross\n")
        wait.lower()
        if wait == "wait":
            red = input("You arrived at the island unarmed. There is a red and a green apple on the floor "
            "Type \"red\" to eat the red apple. Type \"green\" to eat the green apple\n")
            red.lower()
            if red == "red":
                front = input("You have a full stomach now. Type \"front\" to move forward or Type \"back\" to have a scan of the house\n")
                front.lower()
                if front == "front":
                    white = input("There are 3 doors. One red, One blue. One white. Which color do you choose\n")
                    white.lower()
                    if white == "white":
                        print('''
                        *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
                        ''')
                        print("Winner. You found the hidden Treasure.")
                    else:
                        print("Game over. That door leads to a dark room with traps everywhere.")
                else:
                    print("Game over. While making a scan you got caught") 
            else:
                print("Game over. The green apple was poisonous")
        else:
            print("Game over. You got surrounded by killer crocodiles")

    else:
        print("Game over. You got caught by the bandits")

else:
    print("Game over")