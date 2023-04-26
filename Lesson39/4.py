import pygame
from pygame.locals import *

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRAY = (127,127,127)

pygame.init()
screen = pygame.display.set_mode((600,400))

dir = {K_LEFT: (-5,0),
     K_RIGHT: (5, 0),
     K_UP: (0, -5),
     K_DOWN: (0,5)}

rect0 = Rect(50,60,200,80)
rect = rect0.copy()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in dir:
                vector = dir[event.key]
                rect.inflate_ip(vector)

    screen.fill(GRAY)
    pygame.draw.rect(screen,BLUE,rect0,1)
    pygame.draw.rect(screen,RED,rect,4)

    pygame.display.update()

pygame.quit()