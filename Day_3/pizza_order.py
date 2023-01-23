# make a pizza order program
print("Welcome to Olamilekan pizza deliveries")
# ask user the size of pizza
name = input("what is your name? ")
size = input("What size of pizza do you want to order? S, M or L\n ")

# create a global total variable
total = 0

if size == "S":
    total = 15
    print("The small pizza price is $15")
    pepperoni = input("Do you want pepperoni on it? Y or N\n ")
    if pepperoni == "Y":
        total += 2
        print("pepperoni is $2")
    extra_cheese = input("Do you want extra cheese? Y or N\n ")
    if extra_cheese == "Y":
        total += 1
        print("extra cheese is $1")

elif size == "M":
    total = 20
    print("The medium pizza price is $20")
    pepperoni = input("Do you want pepperoni on it? Y or N\n ")
    if pepperoni == "Y":
        total += 3
        print("pepperoni is $3")
    extra_cheese = input("Do you want extra cheese? Y or N\n ")
    if extra_cheese == "Y":
        total += 1
        print("extra cheese is $1")

elif size == "L":
    total = 25
    print("The large pizza price is $25")
    pepperoni = input("Do you want pepperoni on it? Y or N\n ")
    if pepperoni == "Y":
        print("pepperoni is $3")
        total += 3
    extra_cheese = input("Do you want extra cheese? Y or N\n ")
    if extra_cheese == "Y":
        total += 1
        print("extra cheese is $1")
print()
print("{} Your tota bill is ${}".format(name, total))
