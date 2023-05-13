import pygame
from pygame.locals import *
# pygame.mixer - короткие звуки
# pygame.mixer.music -  фоновая музыка

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400,300))
pygame.mixer.music.load('1.ogg')
# pygame.mixer.music.queue('2.ogg') # ставлю звук в очередь
pygame.mixer.music.play(-1) # зациклю

sound1 = pygame.mixer.Sound('2.ogg') # только wav,ogg
sound2 = pygame.mixer.Sound('3.ogg')
running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYUP:
            if event.key == K_1:
                pygame.mixer.music.pause()

            elif event.key == K_2:
                pygame.mixer.music.unpause()
            elif event.key == K_DOWN:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(0.5)
            elif event.key == K_UP:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(1)

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                sound1.play()
            elif event.button == 3:
                sound2.play()

    pygame.display.update()
pygame.quit()