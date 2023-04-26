import pygame
from pygame.locals import *

RED = (255,0,0)
GRAY  = (127,127,127)

SIZE = 500,200

pygame.init()
screen = pygame.display.set_mode(SIZE)

# rect1 = Rect(50,60,200,80)
rect1 = Rect(50,SIZE[1]/2,200,80)

print(f'x={rect1.x}, y = {rect1.y}, w = {rect1.w}, h = {rect1.h}')
print(f'left={rect1.left}, right = {rect1.right}, top = {rect1.top}, bottom = {rect1.bottom}')
print(f'center = {rect1.center}')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_l:
                rect1.left = 0
            if event.key == K_r:
                rect1.right = SIZE[0]

            if event.key == K_t:
                rect1.top = 0
            if event.key == K_b:
                rect1.bottom = SIZE[1]
                
            if event.key == K_h:
                rect1.centerx = SIZE[0]//2
            if event.key == K_v:
                rect1.centery = SIZE[1]//2

    screen.fill(GRAY)
    pygame.draw.rect(screen,RED,rect1)
    pygame.display.flip()

pygame.quit()

