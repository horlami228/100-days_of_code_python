# This program checks if a year is a leap year

# Get input from user
print("Welcome to the Leap year calculator")
year = int(input("What year do you want to check: "))

# check the alogrithms is correct
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is a Leap year".format(year))
        else:
            print("{} is not a Leap year".format(year))
    else:
        print("{} is a Leap year".format(year))
else:
    print("{} is not a Leap year".format(year))