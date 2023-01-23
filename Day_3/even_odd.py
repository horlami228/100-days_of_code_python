# Ask user for a number
Number = int(input("Enter a Number only: "))
# use the modulos operator % to check if it has a remainder of 0 or 1
if Number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
