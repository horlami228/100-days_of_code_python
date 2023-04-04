import math
# This a program that checks for prime number

def prime_check(num):
    # prime numbers are numbers with multiples of 1 and itself
    i = 2
    if(num == 2):
        print("{} is a prime number".format(num))
        exit()
    if(num == 1):
        print("{} is not a prime number".format(num))
        exit()

    while(i <= math.sqrt(num)):
        if(num % i == 0):
            print("{} is not prime number".format(num))
            exit()
        i = i + 1
    print("{} is a prime number".format(num))

n = int(input("Check this number: "))
prime_check(n)