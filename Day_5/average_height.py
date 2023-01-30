# This program calculates the average heights from a list

# Ask for student heights

student_heights = input("Input a list of students heights ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(student_heights)
# make a count of the number of elements in the list
count = 0
for i in student_heights:
    count += 1
# add all elements together in the list
sum = 0
for i in student_heights:
    sum += i
# find the average height
average_height = round(sum / count)
print("The average height is: {}".format(average_height))

# now to get the highest value
score = 0
for i in student_heights:
    if i > score:
        score = i
print("The highest score in the class is: {}".format(score))