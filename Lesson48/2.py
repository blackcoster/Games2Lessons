import random

import pygame

running = True
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

PARTICLE_EVENT = pygame.USEREVENT
pygame.time.set_timer(PARTICLE_EVENT,20)
nyan_img = pygame.image.load('nyan_cat.png').convert_alpha()
w,h, = nyan_img.get_rect().w,nyan_img.get_rect().h
nyan_img = pygame.transform.scale(nyan_img,(w*0.66,h*0.66))

pygame.mixer.music.load('nyan.mp3')
pygame.mixer.music.play(-1)
pygame.mixer_music.set_volume(0.5)

class ParticleStyle:
    def __init__(self):
        self.particles = []
        self.size = 8
    def process(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                    particle[0].x -=1
                    pygame.draw.rect(screen,particle[1],particle[0])
        self.draw_nyan()

    def add_particles(self,offset,color):
        pos_x = pygame.mouse.get_pos()[0]
        pos_y = pygame.mouse.get_pos()[1]+offset
        particle_rect = pygame.Rect(pos_x-self.size/2,pos_y-self.size/2,self.size,self.size)

        self.particles.append((particle_rect,color))
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[0].x>0]
        self.particles = particle_copy
    def draw_nyan(self):

        nyan_rect = nyan_img.get_rect()
        nyan_rect.center = pygame.mouse.get_pos()
        screen.blit(nyan_img,nyan_rect)

particle_style = ParticleStyle()

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == PARTICLE_EVENT:
            particle_style.add_particles(-20,pygame.Color('Red'))
            particle_style.add_particles(-12, pygame.Color('Orange'))
            particle_style.add_particles(-4, pygame.Color('Yellow'))
            particle_style.add_particles(4, pygame.Color('Green'))
            particle_style.add_particles(12, pygame.Color('Blue'))
            particle_style.add_particles(20, pygame.Color('Purple'))

    screen.fill((30,30,30))
    particle_style.process()
    pygame.display.update()
    clock.tick(60)