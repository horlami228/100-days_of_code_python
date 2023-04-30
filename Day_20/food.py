"""This is the food object for our snake game"""

from turtle import *
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh_food()

    def refresh_food(self):
        position_x = random.randint(-260, 260)
        position_y = random.randint(-260, 260)
        self.goto(x=position_x, y=position_y)
