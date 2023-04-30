""" creating a new ScoreBoard class"""

from turtle import *

ALIGNMENT = "center"
FONT_CHOICE = ("Futura", 15, "normal")


class ScoreBoard(Turtle):
    """inherit the turtle class"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.score = 0
        self.write("Score: {}".format(self.score), align=ALIGNMENT, font=FONT_CHOICE)

    def update_current_score(self):
        self.score += 1
        self.clear()
        self.write("Score: {}".format(self.score), align=ALIGNMENT, font=FONT_CHOICE)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game over", align=ALIGNMENT, font=FONT_CHOICE)
