# place the X where the user choose

print("This is the rows and column")

row_1 = ["⬜", "⬜", "⬜"]
row_2 = ["⬜", "⬜", "⬜"]
row_3 = ["⬜", "⬜", "⬜"]

# add list to another list

map = [row_1, row_2, row_3] # nested list
print("{}\n{}\n{}".format(row_1, row_2, row_3))
# ask user where they want to put the "X"
position = input("Where do you want to the Treasure? ")
# get each string and convert to int
horizontal = int(position[0])
vertical = int(position[1])
# map is a two dimensional array
map[vertical -1][horizontal -1] = "X"
# print new rows
print("{}\n{}\n{}".format(row_1, row_2, row_3))