""" creating a new ScoreBoard class"""

from turtle import *

"Lets open the data file"
with open("data.txt", mode="r") as data:
    content = int(data.read())

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
        self.high_score = content
        self.current_score()

    def current_score(self):
        self.clear()
        self.write("Score: {} High Score: {}".format(self.score, self.high_score), align=ALIGNMENT, font=FONT_CHOICE)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write("Score: {} High Score: {}".format(self.score, self.high_score), align=ALIGNMENT, font=FONT_CHOICE)

    def refresh_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("data.txt", mode="w") as data1:
            data1.write(f"{self.high_score}")
        self.current_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game over", align=ALIGNMENT, font=FONT_CHOICE)
