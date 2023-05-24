import random

import pygame

running = True
pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

PARTICLE_EVENT = pygame.USEREVENT
pygame.time.set_timer(PARTICLE_EVENT,80)

class ParticleStyle:
    def __init__(self):
        self.particles = []
    def process(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][0]+=particle[2][0]
                particle[0][1]+=particle[2][1]
                particle[1]-=0.2
                pygame.draw.circle(screen,pygame.Color('White'),particle[0],int(particle[1]))

    def add_particles(self):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]
        radius = 10
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3,3)
        particle_element = [[pos_x,pos_y],radius,[direction_x,direction_y]]
        self.particles.append(particle_element)
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1]>0]
        self.particles = particle_copy

particle_style = ParticleStyle()

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == PARTICLE_EVENT:
            particle_style.add_particles()

    screen.fill((30,30,30))
    particle_style.process()
    pygame.display.update()
    clock.tick(60)