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
        self.star_img = pygame.image.load('star.png').convert_alpha()
        self.width = self.star_img.get_rect().width
        self.height = self.star_img.get_rect().height
    def process(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0].x+=particle[1]
                particle[0].y+=particle[2]
                particle[3]-=0.2
                screen.blit(self.star_img,particle[0])

    def add_particles(self):
        pos_x = pygame.mouse.get_pos()[0]-self.width/2
        pos_y = pygame.mouse.get_pos()[1]-self.height/2
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3,3)
        lifetime = random.randint(4,10)
        particle_rect = pygame.Rect(pos_x,pos_y,self.width,self.height)
        self.particles.append([particle_rect,direction_x,direction_y,lifetime])

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[3]>0]
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