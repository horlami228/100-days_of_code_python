"""import the turtle class"""
from turtle import *

"""snake position on the screen"""
SNAKE_STARTING_POS = [(0, 0), (-21, 0), (-41, 0)]
MOVEMENT = 21
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """create a new snake instance"""

    def __init__(self):
        self.snake_segment = []
        self.create_new_snake()
        self.snake_head = self.snake_segment[0]

    def create_new_snake(self):
        """This function initializes the new snake"""
        for position in SNAKE_STARTING_POS:
            self.add_snake(position)

    def add_snake(self, position):
        """This function adds a new snake"""
        new_snake = Turtle("square")
        new_snake.color("red")
        new_snake.penup()
        new_snake.goto(position)
        self.snake_segment.append(new_snake)

    def extend_snake(self):
        """This function extends the snake to the given position"""
        self.add_snake(self.snake_segment[-1].position())

    def move(self):
        """replace each coordinates to follow the head snake"""
        for movement in range(len(self.snake_segment) - 1, 0, -1):
            x_coordinate = self.snake_segment[movement - 1].xcor()
            y_coordinate = self.snake_segment[movement - 1].ycor()

            self.snake_segment[movement].goto(x_coordinate, y_coordinate)
        self.snake_head.forward(MOVEMENT)

    def up(self):
        """ move snake up"""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """ move snake down """
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def back(self):
        """ move snake back """
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def front(self):
        """ move snake front """
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
