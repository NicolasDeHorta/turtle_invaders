from turtle import Turtle

UP = 90
DOWN = 270
SPEED = 20

bullets = []

class Bullet(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.speed = SPEED
        self.setheading(UP)
        self.goto(pos)

    def new_bullet(self, bullet):
        bullets.append(bullet)
        print(bullets)


    def move(self):
        self.forward(self.speed)

    def move_bullets(self):
        for bullet in bullets:
            bullet.move()


    def get_list(self):
        lista = []
        for bullet in bullets:
            lista.append(bullet)
        return lista
