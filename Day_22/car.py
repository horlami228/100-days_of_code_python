from turtle import *
import random

CAR_COLOR = ["red", "black", "purple", "brown", "yellow", "blue", "green", "orange", "pink"]


class Car:
    def __init__(self):
        """Initializing a new Car Object"""
        self.cars_garage = []
        self.move = -10

    def create_car(self):
        car_chance_creation = random.randint(1, 6)
        if car_chance_creation == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(CAR_COLOR))
            new_car.penup()
            new_car.shapesize(2, 1)
            random_y_coordinate = random.randint(-230, 230)
            new_car.goto(400, random_y_coordinate)
            new_car.setheading(270)
            self.cars_garage.append(new_car)

    def move_car(self):
        """This method moves the car"""
        for cars in self.cars_garage:
            x_cor = cars.xcor() + self.move
            cars.goto(x_cor, cars.ycor())

    def next_level(self):
        self.move += -5
