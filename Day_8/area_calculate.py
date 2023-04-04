import math
def paint_cal(height, weight, coverage):
    
    number_of_cans = (height * weight) / coverage # perform the calculations 
    # print out result and round it up to the nearest integer
    print("The number of cans you will need is {}".format(math.ceil(number_of_cans)))

# get input for user
wall_height = int(input("Height of wall: "))
wall_weight = int(input("Width of wall: "))

coverage = 5
paint_cal(wall_height, wall_weight, coverage)