from random import randint

import pygame
from pygame import *

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('свет')
clock = pygame.time.Clock()
running = True


particles = []
#
def circle_surf(radius,color):
    surf = pygame.Surface((radius*2,radius*2))
    pygame.draw.circle(surf,color,(radius,radius),radius)
    surf.set_colorkey((0,0,0))
    return surf

while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    mx,my = pygame.mouse.get_pos()
    particles.append([[mx,my],
                      [randint(-3,3),randint(-3,3)],
                      randint(6,11)])

    for particle in particles:
        particle[0][0]+=particle[1][0]
        particle[0][1]+=particle[1][1]
        particle[2] -=  0.5
        particle[0][1] += 2
        radius = particle[2]*2
        a= circle_surf(radius,(20,20,60))
        screen.blit(circle_surf(radius, (20, 20, 80)),
                    ((int(particle[0][0] - radius)),int(particle[0][1] - radius)),
                    special_flags=BLEND_RGB_ADD)

        pygame.draw.circle(screen, "white",
                           (int(particle[0][0]), int(particle[0][1])), int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

    pygame.display.update()
pygame.quit()