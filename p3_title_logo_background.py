import pygame

# pygame setup
pygame.init()

# create a screen to display graphics
screen = pygame.display.set_mode((800, 600))
running = True

# create background
background = pygame.image.load('background.png')


# set caption
pygame.display.set_caption("Space Invader")

# set caption, icon - https://www.flaticon.com/
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


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

    # flip() the display to put your work on screen
    pygame.display.flip()
