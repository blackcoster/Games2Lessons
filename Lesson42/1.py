import pygame
from pygame.locals import *

size = width,height = 600,400
background_color = pygame.Color('white')
is_walking = False
MOVE_SPEED = 7
left = right = False


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images =[]

        for i in range(1,11):
            k = pygame.image.load(f'images/walk{i}.png')
            self.images.append(k)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5,5,150,198)

    def update(self):

        if is_walking == True:
            self.rect.x += self.xvel
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        if left == True:
            self.xvel = -MOVE_SPEED
            self.image = pygame.transform.flip(self.image,True, False)
        if right == True:
            self.xvel = MOVE_SPEED
        if not(left or right):
            self.xvel = 0



        # self.index += 1
        # if self.index >= len(self.images):
        #     self.index = 0
        # self.image = self.images[self.index]

def main():
    global left,right,is_walking
    pygame.init()
    screen = pygame.display.set_mode(size)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group()
    my_group.add(my_sprite)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_LEFT:
                left = True
                is_walking = True
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
                is_walking = True
            elif event.type == KEYUP and event.key == K_LEFT:
                left = False
                is_walking = False
            elif event.type == KEYUP and event.key == K_RIGHT:
                right = False
                is_walking = False
        my_group.update()
        screen.fill(background_color)
        my_group.draw(screen)
        pygame.display.update()

main()

