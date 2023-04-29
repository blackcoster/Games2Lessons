import pygame
from pygame.locals import *

RED = (255,0,0)
GRAY = (150,150,150)
GREEN = (0,255,0)

pygame.init()
w,h = 640,440
screen = pygame.display.set_mode((w,h))
running = True

img0 = pygame.image.load('bird.png')
img0.convert()

img = pygame.image.load('bird.png')
img.convert()




rect0 = img0.get_rect()
center = w//2,h//2

img = img0
rect = img.get_rect()

rect.center = center
moving = False

angle = 0
scale = 1

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type ==KEYDOWN:
            if event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    angle -=10
                else:
                    angle +=10
                img = pygame.transform.rotozoom(img0,angle,scale)

            if event.key == K_z:
                if event.mod & KMOD_SHIFT:
                    scale /=1.1
                else:
                    scale *=1.1
                img = pygame.transform.rotozoom(img0,angle,scale)

            if event.key == K_o:
                img = img0
                angle = 0
                scale = 1

            if event.key == K_h:
                img = pygame.transform.flip(img,True,False)
            if event.key == K_v:
                img = pygame.transform.flip(img,False,True)

            if event.key == K_l:
                img = pygame.transform.laplacian(img)

            if event.key == K_2:
                img = pygame.transform.scale2x(img)


    screen.fill(GRAY)
    rect = img.get_rect()
    rect.center = center
    screen.blit(img,rect)
    pygame.draw.rect(screen,RED,rect,1)

    pygame.display.update()

pygame.quit()