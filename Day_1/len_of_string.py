# Determine the lenght of a string given by the user
# We can do that with the in-built len()

Name = input("what is your name? ")
print("Your name is " + Name)
print("The lenght is", len(Name))

#We can always use the string format for better readablity of our code

print("Your name is {} and the lenght is {}".format(Name, len(Name)))