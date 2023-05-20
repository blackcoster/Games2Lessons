import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))

font = pygame.font.SysFont(None,40)

user_text = ''

input_rect = pygame.Rect(200,200,140,32)
color_active = pygame.Color('lightskyblue')
color_passive = pygame.Color('gray15')

color = color_passive

active = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and active:
            if event.key == K_BACKSPACE:
                if len(user_text) > 0:
                    user_text = user_text[:-1]
            else:
                user_text += event.unicode
        if event.type == MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True

    screen.fill((0,0,0))

    color = color_active if active else color_passive

    pygame.draw.rect(screen,color,input_rect)

    text_surf = font.render(user_text,True,(255,255,255))

    screen.blit(text_surf,(input_rect.x+5,input_rect.y+5))

    input_rect.w = max(100,text_surf.get_width())

    pygame.display.update()
pygame.quit()
