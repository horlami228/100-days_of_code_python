from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_cor = 10
        self.x_cor = 10
        self.ball_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.x_cor
        y_cor = self.ycor() + self.y_cor

        self.goto(x_cor, y_cor)

    def bounce_ball_y(self):
        self.y_cor *= -1

    def bounce_ball_x(self):
        self.x_cor *= -1
        self.ball_speed *= 0.9

    def refresh_game(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_ball_x()
