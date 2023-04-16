from turtle import Turtle
MOVE_DISTANCE = 20
INITIAL_SNAKE = [ (0,0), (0, -20), (0, -40)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakeParts = []
        self.create_snake()
        self.head = self.snakeParts[0]

    def create_snake(self):
        for position in INITIAL_SNAKE:
            self.add_part(position)

    def reset_snake(self):
        for part in self.snakeParts:
            part.hideturtle()
        self.snakeParts.clear()
        self.create_snake()
        self.head = self.snakeParts[0]

    def add_part(self, position):
        part = Turtle('square')
        part.color('white')
        part.penup()
        part.goto(position)
        self.snakeParts.append(part)

    def snake_grow(self):
        self.add_part(self.snakeParts[-1].position())


    def snake_movement(self):
        for part in range(len(self.snakeParts) - 1, 0, -1):
            posInFront = self.snakeParts[part - 1].pos()
            self.snakeParts[part].goto(posInFront)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



