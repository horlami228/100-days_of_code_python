# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# my_color = []
# all_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     my_color.append(new_colors)
import turtle
import random
from turtle import *
rgb_list = [
            (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62), (197, 144, 171),
            (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86),
            (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225),
            (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145),
            (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)
]
shell = Turtle()
screen = Screen()
turtle.colormode(255)
shell.penup()
shell.hideturtle()
shell.setheading(230)
shell.forward(300)
shell.setheading(0)
shell.speed("fast")
for loop1 in range(1, 101):
    shell.dot(15, random.choice(rgb_list))
    shell.forward(50)

    if loop1 % 10 == 0:
        shell.setheading(90)
        shell.forward(50)
        shell.setheading(180)
        shell.forward(500)
        shell.setheading(360)

screen.exitonclick()