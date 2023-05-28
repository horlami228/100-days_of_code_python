import csv
import pandas

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
print(temperatures)

data = pandas.read_csv("weather_data.csv")
data_temp_list = data["temp"].to_list()

sum = 0
length = len(data_temp_list)
for num in data_temp_list:
    sum += num
print(f"The average is {round(sum / length, 2)}")

maximum = data["temp"].max()
print(maximum)

print(data[data.temp == data["temp"].max()])


def convert_cel_to_far(number):
    F = (number * 9 / 5) + 32
    print(F)

monday = data[data.day == "Monday"]

print((monday.temp * 9/5) + 32)

log_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = log_data[log_data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = log_data[log_data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = log_data[log_data["Primary Fur Color"] == "Black"]

squirrel = {"fur color": ["grey", "cinnamon", "black"],
            "count": [len(grey_squirrels), len(cinnamon_squirrels), len(black_squirrels)]
            }
data = pandas.DataFrame(squirrel)
data.to_csv("new_squirrel_data.csv")