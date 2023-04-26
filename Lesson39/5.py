import pygame
from pygame.locals import *

SIZE = 500,200
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRAY = (127,127,127)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode(SIZE)

dir = {K_LEFT: (-5,0),
     K_RIGHT: (5, 0),
     K_UP: (0, -5),
     K_DOWN: (0,5)}

running = True

r0 = Rect(50,60,200,80)
r1 = Rect(100,20,100,140)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in dir:
                r1.move_ip(dir[event.key])

    clip = r0.clip(r1)
    union = r0.union(r1)

    screen.fill(GRAY)

    pygame.draw.rect(screen,YELLOW,union,0)
    pygame.draw.rect(screen,GREEN,clip,0)
    pygame.draw.rect(screen, BLUE, r0, 4)
    pygame.draw.rect(screen, RED, r1, 4)
    pygame.display.update()

pygame.quit()