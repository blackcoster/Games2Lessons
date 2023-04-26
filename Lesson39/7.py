from random import randint
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
rect  = Rect(100,50,50,50)

def random_point():
    x = randint(0,SIZE[0])
    y = randint(0,SIZE[1])
    return (x,y)

def random_points(n):
    points = []
    for i in range(n):
        p = random_point()
        points.append(p)
    return points

points = random_points(100)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_r:
            points = random_points(100)
    screen.fill(GRAY)
    pygame.draw.rect(screen,GREEN,rect,1)
    for p in points:
        if rect.collidepoint(p):
            pygame.draw.circle(screen,RED,p,4,0)
        else:
            pygame.draw.circle(screen, BLUE, p, 4, 0)
    pygame.display.update()
pygame.quit()