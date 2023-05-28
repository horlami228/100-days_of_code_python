from turtle import *
import time
from player import Player
from car import Car
from scoreboard import ScoreBoard
"""setup the screen size and color"""

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("white")
screen.tracer(0)  # switch off animation

player = Player()  # creating a new object Player
car = Car()
score = ScoreBoard()

screen.listen()  # checks for keyboard clicks
screen.onkey(fun=player.move_player, key="Up")
screen.onkey(fun=player.move_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()  # update the screen
    time.sleep(0.1)
    car.create_car()
    car.move_car()

    "Detect collision between car and player"
    for cars in car.cars_garage:
        if cars.distance(player) < 20:
            score.game_over()
            game_is_on = False

    "Detect if player reach finish line"
    if player.ycor() > 280:
        player.starting_position()
        car.next_level()
        score.increase_score()
screen.exitonclick()
