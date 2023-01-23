# This program calculates your love score

print("Welcome to the love calculator")
true = 0
love = 0
# collect all user input
name1 = input("Enter your name: \n")
name2 = input("Enter your patner name: \n")
# join both strings together to start count
new_name = name1 + name2
# convert to all character to lower case
new_name.lower()
# count characters to calculate
true += new_name.count("t")
true += new_name.count("r")
true += new_name.count("u")
true += new_name.count("e")

love += new_name.count("l")
love += new_name.count("o")
love += new_name.count("v")
love += new_name.count("e")

# convert both true and love value to strings
true = str(true)
love = str(love)
# concatenate the two strings together
score = true + love
# convert the string back to int to get a number
score = int(score)

if score < 10 or score > 90:
    print("Your score is {}, you go together like coke and mentos.".format(score))
elif score >= 40 and score <= 50:
    print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}".format(score))
