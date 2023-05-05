import pygame
from pygame.locals import *

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BG = (50,50,50)
BLACK = (0,0,0)

class SpriteSheet():
    def __init__(self,image):
        self.sheet = image

    def get_image(self, width, height, scale, frame):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(BLACK)
        return image



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('анимация')

sprite_sheet_image = pygame.image.load('dino.png')
sprite_sheet = SpriteSheet(sprite_sheet_image)

animation_list = []
animation_steps = [4,6,3,4,7]

step_counter = 0
for animation in animation_steps:
    temp_img_list = []
    for i in range(animation):
        k = sprite_sheet.get_image(24,24,3,step_counter)
        temp_img_list.append(k)
        step_counter +=1
    animation_list.append(temp_img_list)

last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0
action = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN and action > 0:
                action -=1
                frame = 0

            if event.key == K_UP and action < len(animation_list)-1:
                action += 1
                frame = 0

            if event.key == K_1:
                action = 0
                frame = 0
            if event.key == K_2:
                action = 1
                frame = 0
            if event.key == K_3:
                action = 2
                frame = 0
            if event.key == K_4:
                action = 3
                frame = 0
            if event.key == K_5:
                action = 4
                frame = 0



    screen.fill(BG)

    screen.blit(animation_list[action][frame],(0,0))

    current_time = pygame.time.get_ticks()
    if current_time-last_update >= animation_cooldown:
        frame += 1
        if frame >= len(animation_list[action]):
            frame = 0

        last_update = current_time



    pygame.display.update()

pygame.quit()
