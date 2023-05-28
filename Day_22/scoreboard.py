from turtle import *

"""creating our score board which is going to inherit from the turtle class"""


class ScoreBoard(Turtle):
    """Initializing a new ScoreBoard Object"""

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x=-350, y=270)
        self.score = 1
        self.score_level()

    def score_level(self):
        self.write(f"Level: {self.score}", align="center", font=("Futura", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_level()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game over", align="center", font=("Futura", 15, "normal"))
