# This program should add two digits in a two digits number

# Get input from user
two_digit = input("Type a two digit number only\n")

# convert input to a string if not already a string
two_digit = str(two_digit)

# convert each elements in the string to an int to be able to perform an arithmetic operation
Add = int(str(two_digit[0])) + int(str(two_digit[1]))
# Print result
print(Add)