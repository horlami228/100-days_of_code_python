import random
# create a list for letters, symbol and numbers

# list to get all letters with a loop
letters = []
for i in range(ord('a'), ord('z') + 1):
    letters.append(chr(i))

for i in range(ord('A'), ord('Z') + 1):
    letters.append(chr(i))

# list for numers in strings
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8' '9']
symbols = ['%', '!', '#', '*', ':', '&', '^', '?', '.', '(', ')']

letter_choice = int(input("How many letters do you want in your password: "))
number_choice = int(input("How many numbers do you want: "))
symbol_choice = int(input("How many symbols do you want: "))

password = ""

for i in range(0, letter_choice):
    password += random.choice(letters)
for i in range(0, number_choice):
    password += random.choice(numbers)
for i in range(0, symbol_choice):
    password += random.choice(symbols)

# shuffle the passowrd to make it random selected
password = list(password) # make password a list
random.shuffle(password) # use the shuffle method on the list
password = "".join(password) # The join method is called on an empty string '' and takes a list of strings as its argument.
print("Your password is: {}".format(password))
