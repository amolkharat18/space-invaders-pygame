import pygame

# pygame setup
pygame.init()

# create a screen to display graphics
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

    # flip() the display to put your work on screen
    pygame.display.flip()
