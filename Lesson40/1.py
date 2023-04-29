import pygame
from pygame.locals import *

RED = (255,0,0)
GRAY = (150,150,150)

pygame.init()
w,h = 640,440
screen = pygame.display.set_mode((w,h))
running = True

img = pygame.image.load('bird.png')
img.convert()

moving = False

rect = img.get_rect()
rect.center = w//2, h//2

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
    screen.blit(img,rect)
    pygame.draw.rect(screen,RED,rect,1)

    pygame.display.update()

pygame.quit()