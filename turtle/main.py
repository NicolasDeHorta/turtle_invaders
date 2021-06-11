from turtle import Screen
from turtle.bullet import Bullet
from space_turtle import Space_turtle
import time

#SCREEN
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.tracer(0)

player = Space_turtle()
bullet = Bullet(player.position())
bullet.goto(500, 500)

# MOVEMENT
screen.listen()
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")
screen.onkey(player.shoot, "space")

bullets = ""
score = 0
game_running = True
fps = 0.1

while game_running:
    time.sleep(fps)
    screen.update()

    bullet.move_bullets()

    if player.xcor() > 380:
        player.goto(380, -370)
    elif player.xcor() < -380:
        player.goto(-380, -370)
