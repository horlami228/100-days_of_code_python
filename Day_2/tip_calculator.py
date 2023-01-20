# This program calculates the tip to pay and shared between friends

# Ask user for the total amount to be paid
Total_amount = input("What is the total amount to be paid? $")
Total_amount = float(Total_amount)

# Ask for the percentage tip to give

tip_percent = input("What percentage tip to give? 10, 12, or 15\n")
tip_percent = int(tip_percent)

# Add the percentage tip to the total amount
tip_percent = tip_percent / 100
New_amount1 = Total_amount * tip_percent
Total_amount = Total_amount + New_amount1

#Ask how many people to split the bill
split = input("How many people do you want to split the bill with?\n")
split = int(split)

New_amount = Total_amount / split
# Round to two decimal place
New_amount = round(New_amount, 2)

# print result
print("Each person should pay ${}".format(New_amount))