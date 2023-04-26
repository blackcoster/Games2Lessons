import pygame
from pygame.locals import *

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRAY = (127,127,127)

pygame.init()
screen = pygame.display.set_mode((600,400))

running = True
drawing = False
points = []

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
            drawing = True

        if event.type == MOUSEBUTTONUP:
            drawing = False

        if event.type == MOUSEMOTION and drawing:
            points[-1] = event.pos

        if event.type == KEYDOWN and event.key == K_SPACE:
            if len(points)>0:
                points.pop()

    screen.fill(GRAY)
    if len(points)>1:
        line1 = pygame.draw.lines(screen,RED,False,points,3)
        pygame.draw.rect(screen,GREEN,line1,1)
    pygame.display.update()

pygame.quit()