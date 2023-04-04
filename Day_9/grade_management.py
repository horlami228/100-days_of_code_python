student_scores = {"Harry": 90, "Styles": 72, "James": 64, "Winslow": 91, "Akraf": 41}

for keys in student_scores:
    print("{} : {}".format(keys, student_scores[keys]))
print()  
student_grades = {} #empty grade dictionary

for keys in student_scores: # loop through to get the dictionary keys
    score = student_scores[keys]
    if score > 90:
        student_grades[keys] = "Outstanding"
    elif score > 80:
        student_grades[keys] = "Exceeds Expectations"
    elif score > 70:
        student_grades[keys] = "Acceptable"
    else:
        student_grades[keys] = "Fail"

# print out the grades attributes
for keys in student_grades:
    print("\n{} : {}".format(keys, student_grades[keys]))
