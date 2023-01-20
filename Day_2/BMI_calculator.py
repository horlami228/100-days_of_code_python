# Calculate the Body Mass index of the user

# Ask user for their Weight and height
weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")

# convert weight to float and height to float
weight = int(weight)
height = float(height)
# claculate the result with this formula weight(kg) / height ** 2
BMI = weight / height ** 2

# print the result and round to the nearest whole number

print("Your body mass index is {:.0f}".format(BMI))