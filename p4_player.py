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


def player():
    screen.blit(playerImg, (player_x, player_y))


while running:
    # background color
    screen.fill('Black')

    # background image
    screen.blit(background, (0, 0))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

    # add player
    player()

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
