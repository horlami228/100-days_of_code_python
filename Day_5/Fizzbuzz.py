"""
make a range from 1 to 100
if the number is divisible by 3 print fizz
if the number is divisible y 5 print Buzz
if the number is divisible y both 3 and 5 print FizzBuzz
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=", ")
    elif i % 3 == 0:
        print("Fizz", end=", ")
    elif i % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")