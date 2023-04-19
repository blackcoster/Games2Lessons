import pygame
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (127, 127, 127)
SIZE = (600,400)
width,height = SIZE

screen = pygame.display.set_mode(SIZE)
background = GRAY
window_title = 'ШАРИК'
running = True
speed = [1,1]

ball = pygame.image.load('ball.gif')
rect = ball.get_rect()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = - speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = - speed[1]


    screen.fill(background)
    pygame.draw.rect(screen, RED, rect, 3)
    screen.blit(ball,rect)

    pygame.display.set_caption(window_title)

    pygame.display.update()

pygame.quit()

pygame.quit()
