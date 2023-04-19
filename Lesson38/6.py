import pygame
from pygame.locals import *

GRAY = (127, 127, 127)
RED = (255, 0,0)
GREEN= (0, 255, 0)
BLUE = (0,0,255)

background = GRAY
size = 640,320
width,height = size

screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(background)
    pygame.draw.ellipse(screen,RED,(50,20,160,100))
    pygame.draw.ellipse(screen, GREEN, (100, 60, 160, 100))
    pygame.draw.ellipse(screen, BLUE, (150, 100, 160, 100))

    pygame.draw.ellipse(screen,RED,(350,20,160,100),4)
    # pygame.draw.rect(screen, RED, rect, 3)
    pygame.draw.ellipse(screen, GREEN, (400, 60, 160, 100), 4)
    pygame.draw.ellipse(screen, BLUE, (450, 100, 160, 100), 4)

    pygame.draw.circle(screen,BLUE,(100,250),70,6)
    pygame.draw.polygon(screen,RED,([320,280],[360,280],[360,310],[270,310]),3)
    pygame.display.update()
pygame.quit()

