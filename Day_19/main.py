from turtle import *

shell = Turtle()
screen = Screen()


def move_forward():
    shell.forward(10)


def move_backward():
    shell.back(10)


def move_left():
    shell.left(10)


def move_right():
    shell.right(10)


def clear_all():
    shell.clear()
    shell.penup()
    shell.home()
    shell.pendown()


screen.listen()
screen.onkey(move_forward, "d")
screen.onkey(move_backward, "a")
screen.onkey(move_left, "w")
screen.onkey(move_right, "s")
screen.onkey(clear_all, "c")

screen.exitonclick()
