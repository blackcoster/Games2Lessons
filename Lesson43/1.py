import math

import pygame
from pygame.locals import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


class Car(pygame.sprite.Sprite):
    def __init__(self,car_image,x,y,rotations = 360):
        pygame.sprite.Sprite.__init__(self)

        self.rot_img = []
        self.min_angle = 360/rotations
        for i in range(rotations):
            rotated_image = pygame.transform.rotozoom(car_image,360-90-(i*self.min_angle),1)
            self.rot_img.append(rotated_image)
        self.min_angle = math.radians(self.min_angle)
        self.image = self.rot_img[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        self.reversing = False
        self.heading = 0
        self.speed = 0
        self.velocity = pygame.math.Vector2(0,0)
        self.position = pygame.math.Vector2(x,y)

    def accelerate(self,amount):
        if not self.reversing:
            self.speed+=amount
        else:
            self.speed-=amount

    def brake(self):
        self.speed/=2
        if abs(self.speed)<0.1:
            self.speed = 0

    def reverse(self):
        self.speed=0
        self.reversing = not self.reversing

    def turn(self,angle_degrees):
        self.heading += math.radians(angle_degrees)
        image_index = int(self.heading/self.min_angle) % len(self.rot_img)
        if self.image != self.rot_img[image_index]:
            x,y = self.rect.center
            self.image = self.rot_img[image_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x,y)

    def update(self):
        self.velocity.from_polar((self.speed,math.degrees(self.heading)))
        self.position+=self.velocity
        self.rect.center = (round(self.position[0]),round(self.position)[1])



pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('машинка')

road_image = pygame.image.load('road_texture (1).png')
road_image = pygame.transform.smoothscale(road_image,(WINDOW_WIDTH,WINDOW_HEIGHT))
car_image = pygame.image.load('car_128 (1).png').convert_alpha()


car = Car(car_image,WINDOW_WIDTH//2,WINDOW_HEIGHT//2)
car_sprites = pygame.sprite.Group()
car_sprites.add(car)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==QUIT:
            running = False
        if event.type == KEYUP:
            if event.key == K_r:
                print('reverse')
                car.reverse()
            elif event.key == K_UP:
                print('gas')
                car.accelerate(0.5)
            elif event.key == K_DOWN:
                print('tormoz')
                car.brake()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        car.turn(-1.8)
    if keys[K_RIGHT]:
        car.turn(1.8)

    screen.blit(road_image,(0,0))
    car_sprites.update()
    car_sprites.draw(screen)
    pygame.display.update()
pygame.quit()