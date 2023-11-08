import pygame

# pygame setup
pygame.init()

# create a screen to display graphics
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# create background
background = pygame.image.load('background.png')


# set caption
pygame.display.set_caption("Space Invader")

# set caption, icon - https://www.flaticon.com/
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# create player
playerImg = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


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
                player_x_change = -3
            if event.key == pygame.K_RIGHT:
                player_x_change = 3

        # if key released then stop movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change

    # add player
    player(player_x, player_y)
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
