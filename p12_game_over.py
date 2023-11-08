import pygame
import random
import math
from pygame import mixer

# pygame setup
pygame.init()

# create a screen to display graphics
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# create background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# set caption
pygame.display.set_caption("Space Invader")

# set caption, icon - https://www.flaticon.com/
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# create player
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0


# create enemy
enemy_img = pygame.image.load('enemy.png')
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 5
enemy_y_change = 40

# create bullet
# ready - You can't see the bullet on the screen
# Ffire - The bullet is currently moving
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collision(ex, ey, bx, by):
    distance = math.sqrt(math.pow(ex - bx, 2) + (math.pow(ey - by, 2)))
    return distance < 27


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, 'White')
    screen.blit(score, (x, y))


def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, 'Red')
    screen.blit(over_text, (200, 250))


while running:
    # background color
    screen.fill('Black')

    # background image
    screen.blit(background, (0, 0))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left and move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the current x coordinate of the spaceship
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        # if key released then stop movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    enemy_x += enemy_x_change

    # add player
    player(player_x, player_y)

    # add enemy
    enemy(enemy_x, enemy_y)

    # add score
    show_score(10, 10)

    # keep player within the screen
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # keep player within the screen
    if enemy_x <= 0:
        enemy_x_change = 5
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -5
        enemy_y += enemy_y_change

    # Bullet Movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Game Over
    if enemy_y > 440:
        enemy_y = 2000
        game_over_text()

    # Collision
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = "ready"
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(50, 150)
        score_value += 1

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
