from turtle import Turtle
from turtle.bullet import Bullet

STARTING_POSITION = (0, -370)
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Space_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)
        self.shapesize(1.8)

    def left(self):
        x = self.xcor() - MOVE_DISTANCE
        y = self.ycor()
        self.goto(x, y)

    def right(self):
        x = self.xcor() + MOVE_DISTANCE
        y = self.ycor()
        self.goto(x, y)

    def shoot(self):
        pos = self.xcor(), self.ycor() + 25
        bullet = Bullet(pos)
        bullet.new_bullet(bullet)

    def where_are_you(self):
        return self.position

