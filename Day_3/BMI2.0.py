# Calculate the Body Mass index of the user

# Ask user for their Weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

# claculate the result with this formula weight(kg) / height ** 2
BMI = weight / height ** 2
BMI = int(BMI)
# print the result and round to the nearest whole number
print("Your body mass index is {}".format(BMI))

# Tell the intepretation of the BMI based on the value
if BMI < 18.5:
    print("{}: You are Underweight".format(BMI))
elif BMI < 25:
    print("{}: You have a normal weight".format(BMI))
elif BMI < 30:
    print("{}: You are Overwieght".format(BMI))
elif BMI < 35:
    print("{}: You are Obese".format(BMI))
else:
    print("{}: You are clinically Obese".format(BMI))
