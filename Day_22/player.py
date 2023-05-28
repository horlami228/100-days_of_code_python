"""Creating the player for the game """
# a constant value
MOVE_UP = 10
MOVE_DOWN = 10
from turtle import *


class Player(Turtle):
    """Initializing a new Player Object"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.starting_position()

    def move_player(self):
        """This method moves the player by 10 pixels"""
        self.forward(MOVE_UP)

    def move_down(self):
        """This method lets the player move down by 10 pixels"""
        self.backward(MOVE_DOWN)

    def starting_position(self):
        self.goto(x=0, y=-280)
