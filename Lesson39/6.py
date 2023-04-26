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

running = True
moving = False

rect = Rect(50,60,200,80)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        if event.type == MOUSEBUTTONUP:
            moving = False

        if event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    screen.fill(GRAY)
    pygame.draw.rect(screen,RED,rect)
    if moving:
        pygame.draw.rect(screen,BLUE,rect,4)

    pygame.display.update()

pygame.quit()