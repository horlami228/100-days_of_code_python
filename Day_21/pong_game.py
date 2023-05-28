"""We are creating a PongGame"""
from turtle import *
from ball import Ball
from paddles import Paddle
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("white")
screen.title("Ping Pong")

screen.tracer(0)
paddle = Paddle()
ball = Ball()
score_left = ScoreBoard(-100, 170)
score_right = ScoreBoard(110, 170)
screen.listen()


screen.onkey(fun=paddle.right_move_up, key="Up")
screen.onkey(fun=paddle.right_move_down, key="Down")
screen.onkey(fun=paddle.left_move_up, key="w")
screen.onkey(fun=paddle.left_move_down, key="s")

game_continue = True
while game_continue:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    """Detect collision with the Y_axis of the screen"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    """Detect ball collision with the right paddle"""
    if ball.distance(paddle.right_head) < 60 and ball.xcor() > 340:
        ball.bounce_ball_x()

    """Detect ball collision with the left paddle"""
    if ball.distance(paddle.left_head) < 60 and ball.xcor() < -345:
        ball.bounce_ball_x()

    """ Detect if ball goes pass paddle"""
    if ball.xcor() > 410:
        score_left.refresh_score()
        ball.refresh_game()
    if ball.xcor() < -410:
        score_right.refresh_score()
        ball.refresh_game()

screen.exitonclick()
