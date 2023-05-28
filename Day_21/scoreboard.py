"""creating our scoreboard for the Pong game"""
from turtle import *


class ScoreBoard(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.goto(x_cor, y_cor)
        self.scores()

    def scores(self):
        self.write(f"{self.score}", align="center", font=("Futura", 70, "normal"))

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.scores()
