from turtle import Turtle

STARTING_POSITION = [
    [(-375, 0)], [(370, 0)]
]
MOVEMENT = 15


class Paddle:
    def __init__(self):
        self.left_puddle = []
        self.right_puddle = []
        self.create_puddle()
        self.left_head = self.left_puddle[0]
        self.right_head = self.right_puddle[0]

    def create_puddle(self):
        for position in STARTING_POSITION[0]:
            new_puddle = Turtle()
            new_puddle.penup()
            new_puddle.shape("square")
            new_puddle.color("brown")
            new_puddle.shapesize(5, 1)
            new_puddle.goto(position)
            self.left_puddle.append(new_puddle)
        for position in STARTING_POSITION[1]:
            new_puddle = Turtle()
            new_puddle.penup()
            new_puddle.shape("square")
            new_puddle.color("brown")
            new_puddle.shapesize(5, 1)
            new_puddle.goto(position)
            self.right_puddle.append(new_puddle)

    def right_move_up(self):
        y_coordinate = self.right_head.ycor() + MOVEMENT
        self.right_head.goto(x=self.right_head.xcor(), y=y_coordinate)

    def right_move_down(self):
        y_coordinate = self.right_head.ycor() - MOVEMENT
        self.right_head.goto(x=self.right_head.xcor(), y=y_coordinate)

    def left_move_up(self):
        y_coordinate = self.left_head.ycor() + MOVEMENT
        self.left_head.goto(x=self.left_head.xcor(), y=y_coordinate)

    def left_move_down(self):
        y_coordinate = self.left_head.ycor() - MOVEMENT
        self.left_head.goto(x=self.left_head.xcor(), y=y_coordinate)
