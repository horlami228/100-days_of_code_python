"""" We are making a turtle race game """

from turtle import *
import random

game_on = False
color = ["red", "green", "blue", "yellow", "brown", "black"]
"""creating 5 different turtle objects"""
red = Turtle("turtle")
green = Turtle("turtle")
blue = Turtle("turtle")
yellow = Turtle("turtle")
brown = Turtle("turtle")
black = Turtle("turtle")

""" Adding color to the turtle """
red.color(color[0])
green.color(color[1])
blue.color(color[2])
yellow.color(color[3])
brown.color(color[4])
black.color(color[5])





screen = Screen()
screen.setup(500, 400)

user_choice = screen.textinput("Make a bet", "Which turtle would be the winner? Enter a color: ")
red.penup()
green.penup()
blue.penup()
brown.penup()
yellow.penup()
black.penup()

red.goto(x=-235, y=100)
green.goto(x=-235, y=70)
blue.goto(x=-235, y=40)
yellow.goto(x=-235, y=10)
brown.goto(x=-235, y=-20)
black.goto(x=-235, y=-50)

if user_choice:
    game_on = True

while game_on:
    red.forward(random.randint(0, 10))
    if red.xcor() > 235:
        turtle_color = red.pencolor()
        if turtle_color == user_choice:
            print("You won! The {} turtle won the race".format(turtle_color))
            exit(98)
        else:
            print("You lost! The {} turtle won the race".format(turtle_color))
            exit(98)
    green.forward(random.randint(0, 10))
    if green.xcor() > 235:
        turtle_color = green.pencolor()
        if turtle_color == user_choice:
            print("You won! The {} turtle won the race".format(turtle_color))
            exit(98)
        else:
            print("You lost! The {} turtle won the race".format(turtle_color))
            exit(98)
    blue.forward(random.randint(0, 10))
    if blue.xcor() > 235:
        turtle_color = blue.pencolor()
        if turtle_color == user_choice:
            print("You won! The {} turtle won the race".format(turtle_color))
            exit(98)
        else:
            print("You lost! The {} turtle won the race".format(turtle_color))
            exit(98)
    brown.forward(random.randint(0, 10))
    if brown.xcor() > 235:
        turtle_color = brown.pencolor()
        if turtle_color == user_choice:
            print("You won! The {} turtle won the race".format(turtle_color))
            exit(98)
        else:
            print("You lost! The {} turtle won the race".format(turtle_color))
            exit(98)
    black.forward(random.randint(0, 10))
    if black.xcor() > 235:
        turtle_color = black.pencolor()
        if turtle_color == user_choice:
            print("You won! The {} turtle won the race".format(turtle_color))
            exit(98)
        else:
            print("You lost! The {} turtle won the race".format(turtle_color))
            exit(98)
    yellow.forward(random.randint(0, 10))
    if yellow.xcor() > 230:
        turtle_color = yellow.pencolor()
        if turtle_color == user_choice:
            print("You won! The {} turtle won the race".format(turtle_color))
            exit(98)
        else:
            print("You lost! The {} turtle won the race".format(turtle_color))
            exit(98)












screen.exitonclick()