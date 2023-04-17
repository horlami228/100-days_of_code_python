import random
from blackjack_art import logo
import os
def deal_card():
    """This function randoms select the cards
    Args:
        cards(list): list to append to
        Return: returns a card from the list
    """

    game_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    random.shuffle(game_cards)
    card = random.choice(game_cards)
    return card

def calculation(cards):
    """returns the total value of card in deck 
    Args:
        cards(list): cards selected
    """
    if sum(cards) == 21 and len(cards) == 2:
        return (21)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return (sum(cards))

def compare_scores(user_score, comp_score):
    """compare both userscore and computer score
    Args:
        user(int): user score
        computer(int) computer score
    """
    if user_score == comp_score:
        return "Draw 🙂"
    elif user_score > 21 and comp_score > 21:
        return "Draw 🙂"
    elif user_score > 21:
        return "You went over you loose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score == 0:
        return "You have Black jack"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You loose"
    
print(logo)
def black_jack():
    print(logo)

    user = []
    computer = []
    game_over = False
    for i in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    while not game_over:
        user_score = calculation(user)
        comp_score = calculation(computer)
        print("     Your cards: {}, current score: {}".format(user, user_score))
        print("     Computer first card: {}".format(computer[0]))

        if user_score == 21 or comp_score == 21 or user_score > 21:
            game_over = True
        else:
            should_hit = input("Hit 'y' to get another card. Hit 'n' to pass: ")
            if should_hit == 'y':
                user.append(deal_card())
            else:
                game_over = True

    while(comp_score < 17 and comp_score != 0):
        computer.append(deal_card())
        comp_score = calculation(computer)

    print("     Your final hand: {}, final score: {}".format(user, user_score))
    print("     Computer's final hand: {}. current score: {}".format(computer, comp_score))
    print(compare_scores(user_score, comp_score))
while input("\nDo you want to play a game of Blackjack? Type 'y' to start. Type 'n' to quit: ") == 'y':
    os.system("clear")
    black_jack()