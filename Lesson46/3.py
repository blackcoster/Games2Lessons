import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))

font = pygame.font.SysFont(None,30)

class Button:
    def __init__(self,text,width,height,pos,elevation):
        self.pressed = False
        self.elevation = elevation
        self.original_y_pos = pos[1]
        self.dynamic_elevation = elevation
        self.rect = pygame.Rect(pos,(width,height))
        self.color = '#475F77'
        self.text_surf = font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

        self.bottom_rect = pygame.Rect(pos,(width,elevation))
        self.bottom_color = '#354B5E'

    def draw(self):
        self.rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.rect.center
        self.bottom_rect.midtop = self.rect.center
        self.bottom_rect.height = self.rect.height + self.dynamic_elevation


        pygame.draw.rect(screen,self.bottom_color,self.bottom_rect,border_radius=12)
        pygame.draw.rect(screen, self.color, self.rect, border_radius=12)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):

        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.color='#D73B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                if self.pressed:
                    self.dynamic_elevation = self.elevation
                    global running
                    running = False
                    self.pressed = False
        else:

            self.dynamic_elevation = self.elevation
            self.color = '#475F77'
button1 = Button('Нажми на меня',200,40,(150,250),6)


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


    screen.fill('#DCDDD8')
    button1.draw()
    pygame.display.update()
pygame.quit()