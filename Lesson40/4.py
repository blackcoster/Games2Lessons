import time

import pygame
from pygame.locals import *

width,height = size = 800,600

GREEN = (150,255,150)
RED =(255,0,0)



pygame.init()
pygame.font.init()



timer = pygame.time.Clock()
screen = pygame.display.set_mode(size)
running = True
background = pygame.image.load('desert.png')
screen.blit(background,(0,0))
pygame.display.set_caption('Dino game')

player_sprite = pygame.image.load('dino1.png')
player_sprite = pygame.transform.rotozoom(player_sprite,0,0.5)

cactus = pygame.image.load('cactus.png')
cactus = pygame.transform.rotozoom(cactus,0,0.5)

player_rect = player_sprite.get_rect()
player_rect.center = 0 + player_rect.size[0]//2, size[1]//2

cactus_rect = cactus.get_rect()
cactus_rect.left = size[0]
cactus_rect.bottom = height-100

cactus_speed = [-10,0]

gravity = [0,9]
jumping = False
score = 0

score_font = pygame.font.SysFont('arial',36)
score_text = score_font.render(f'Score - {score}',True,(180,0,0))

lose_text = score_font.render('',True,(180,0,0))

while running:
    timer.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            jumping = True

    keys = pygame.key.get_pressed()
    if keys[K_SPACE] and jumping == False:
        player_rect.y -=20



    screen.blit(background,(0,0))
    screen.blit(player_sprite,player_rect)
    screen.blit(cactus,cactus_rect)
    screen.blit(score_text,(10,20))


    cactus_rect = cactus_rect.move(cactus_speed)

    if cactus_rect.left <0:
        cactus_rect.right = width
        score+=1
        score_text = score_font.render(f'Score - {score}',True,(180,0,0))

    player_rect = player_rect.move(gravity)

    if player_rect.bottom > height-100:
        player_rect.bottom = height-100
        jumping = False

    if player_rect.colliderect(cactus_rect):
        lose_text = score_font.render('YOU LOST', True, (180, 0, 0))
        screen.blit(lose_text, (width / 2, height / 2))
        pygame.display.update()
        time.sleep(3)
        running = False

    pygame.display.update()
pygame.quit()