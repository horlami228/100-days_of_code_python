#Step 1
import random

#Hangman ascii art in a list of 6
from hangman_ascii import stages

# This is the list of words to choose from
from hangman_ascii import word_list

# randomly chose a word from the word list
#Step 2
chosen_word = random.choice(word_list)

#Step 3
display = [] # a list to show the guessed word
# print display with empty list representing the word
for i in chosen_word:
    display += "_"
print(display)

# make a while loop to let the user guess again
#Step 4
stage_len = 0 # for the ascii art
lives = 7
end_of_game = False
while not end_of_game:
     #ask user to guess a letter and assign it to guess
    guess = input("Guess a letter: ").lower() # make input lower case
    if (guess in display):
        print("You have already guessed this letter\n")

    # check if letter guessed is one of the letters in the chosen_word
    list_len = len(chosen_word)
    for position in range(list_len):
        letter = chosen_word[position]
        #print("Current position: {} Current letter: {} Guessed letter: {}".format(position, letter, guess))
        if letter == guess:
            display[position] = letter

    if "_" not in display: # check if display is filled
            end_of_game = True
            print(f"{' '.join(display)}")
            print("You win\n")
            exit(1)
    if guess not in chosen_word: # check if word is wrong
        lives -= 1
        print("You guessed {}, that's not in the word. you lose a life.\n".format(guess))
        print("{}".format(stages[stage_len]))
        stage_len += 1
        if (lives == 0):
            end_of_game = True
            print("You lose\n")
            exit(1)


    print("{}".format(' '.join(display))) #add dispaly as string