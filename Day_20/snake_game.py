"""import turtle module"""

from turtle import Screen
import time
from snake import *
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Zenzia")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.back, key="Left")
screen.onkey(fun=snake.front, key="Right")

game_continue = True
while game_continue:
    screen.update()
    time.sleep(0.1)

    snake.move()

    """check if snake head collide with food """
    if snake.snake_head.distance(food) < 20:
        food.refresh_food()
        snake.extend_snake()
        score.update_score()

    """check if snake head hit the wall"""
    if snake.snake_head.xcor() > 298 or snake.snake_head.xcor() < -298 or snake.snake_head.ycor() > 298 \
            or snake.snake_head.ycor() < -298:
        score.refresh_score()
        snake.refresh_snake()

    """check if snake head hits the body"""
    for body in snake.snake_segment[1:]:
        """check if snake head is equal to its self"""
        if snake.snake_head.distance(body) < 10:
            score.refresh_score()
            snake.refresh_snake()
        
screen.exitonclick()
