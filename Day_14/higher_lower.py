from data import data
from game_art import logo, vs
import random
import os
game_count = 0
random.shuffle(data)

optionA = random.randint(0, len(data) - 1)
dictionary = data[optionA]
game_continue = False
print(logo)
while not game_continue:
    optionB = random.randint(0, len(data) - 1)
    dictionary_2 = data[optionB]
    
    if dictionary == dictionary_2:
        optionB = random.randint(0, len(data) - 1)
        dictionary_2 = data[optionB]
    
    def data_collect_for_A():
        global dictionary
        print("Compare A: {}, {}, from {}".format(dictionary["name"], dictionary["description"], dictionary["country"]))
    def data_collect_for_B():
        global dictionary_2
        print("Against B: {}, {}, from {}".format(dictionary_2["name"], dictionary_2["description"], dictionary_2["country"]))
    def check_answer(answer):
        if answer in ['A', 'a'] and compare_count() == True:
            return "correct"
        elif answer in ['A', 'a'] and compare_count() == False:
            return "not correct"
        elif answer in ['B', 'b'] and compare_count() == False:
            return "correct"
        elif answer in ['B', 'b'] and compare_count() == True:
            return "not correct"
    def compare_count():
        global dictionary
        global dictionary_2

        if dictionary["follower_count"] > dictionary_2["follower_count"]:
            return True
        else:
            return False


    data_collect_for_A()
    print(vs)
    data_collect_for_B()
    compare_count()

    answer = input("Who has more instagram followers? Type 'A' or 'B': ")
    if check_answer(answer) == "correct":
        os.system("clear")
        game_count += 1
        print(logo)
        print("You are right! Current score: {}".format(game_count))
        dictionary = data[optionB]
    else:
        os.system("clear")
        print("sorry that is wrong. Final score: {}".format(game_count))
        game_continue = True