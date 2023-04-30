import turtle
from turtle import *
import random
shelly = Turtle()
color = ["green", "turquoise", "saddle brown", "slate blue", "red", "olive"]
direction = [0, 90, 180, 270]
shelly.speed("fastest")
turtle.colormode(255)
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colors = (r, g, b)
    return colors

for i in range(100):
    shelly.color(color())
    shelly.circle(100)
    shelly.left(10)
    #shelly.setheading(shelly.heading() + 10)




screen = Screen()
screen.exitonclick()





