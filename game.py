import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('img/background.jpg')

# Player
player_img = pygame.transform.scale(pygame.image.load("img/turtle.png"), (40, 40))
player_x = 360
player_y = 550
player_speed = 0.4


def player(x, y):
    screen.blit(player_img, (x, y))


# mini_turtles
miniturtle_img = pygame.transform.scale(pygame.image.load("img/mini_turtle.png"), (10, 10))
mini_turtle_x = player_x
mini_turtle_y = 500
mini_turtle_speed = 2
mini_turtle_state = "waiting"


def mini_turtle(x, y):
    global mini_turtle_state
    mini_turtle_state = "shot"
    screen.blit(miniturtle_img, (x + 20, y + 20))


# Enemy
enemy_img = pygame.transform.scale(pygame.image.load("img/monster.png"), (40, 40))
enemy_img_big = pygame.transform.scale(pygame.image.load("img/monster.png"), (200, 200))
enemy_x = 360
enemy_y = 50
enemy_x_delta = 0.2


def enemy(x, y):
    screen.blit(enemy_img, (x, y))

def boss(x, y):
    screen.blit(enemy_img_big, (x, y))


def collision(enemy_y, enemy_x, mini_turtle_x, mini_turtle_y):
    return math.sqrt(math.pow(enemy_x - mini_turtle_x, 2) + (math.pow(enemy_y - mini_turtle_y, 2))) < 23


score_points = 0
font = pygame.font.Font('freesansbold.ttf', 32)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 40)

def show_score(x, y):
    score = font.render("Score : " + str(score_points), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    over_text2 = game_over_font2.render(f"your score is {score_points}", True, (255, 255, 255))
    screen.blit(over_text, (200, 350))
    screen.blit(over_text2, (265, 450))


game_over = False
# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player_x_delta = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player_x_delta -= player_speed
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player_x_delta += player_speed
            if event.key == pygame.K_SPACE:
                if mini_turtle_state == "waiting":
                    mini_turtle(player_x, mini_turtle_y)
                    mini_turtle_state = "shot"

    if enemy_x > 750 or enemy_x < 0:
        enemy_x_delta *= -1
        enemy_y += 50

    enemy_x += enemy_x_delta
    enemy(enemy_x, enemy_y)

    if player_x < 0:
        player_x = 0
    elif player_x > 760:
        player_x = 760

    player(player_x, player_y)
    player_x += player_x_delta

    if mini_turtle_state == "shot":
        mini_turtle_y -= mini_turtle_speed
        mini_turtle(player_x, mini_turtle_y)
        print(mini_turtle_y)

    if mini_turtle_y <= 0:
        mini_turtle_state = "waiting"
        mini_turtle_y = 550

    colliding = collision(enemy_y, enemy_x, player_x, mini_turtle_y)
    if colliding:
        mini_turtle_state = "waiting"
        mini_turtle_y = 550
        print("MigrExE se la come")
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(50, 150)
        score_points += 1
        enemy_x_delta *= 1.1
        print(enemy_x_delta)

    if enemy_y > 400:
        enemy_y = 2000
        boss(300, 100)
        game_over_text()

    show_score(10, 10)

    pygame.display.update()
