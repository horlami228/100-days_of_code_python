# This program prints out how many days, weeks, and months we have left if we lived up till 90 years
"""We have 365 days in a year
   We have 52 weeks in a year and
   12 months in a year
"""
# Ask user for current age
age = input("What is your current Age? ")
#convert to int
age = int(age)

years = 90 - age
days = years * 365
weeks = years * 52
months = years * 12

# print out the result
print("You have {} days, {} weeks and {} months to live".format(days, weeks, months))