import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('свет')
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill('red')
    for x in  range(0,500,20):
        pygame.draw.line(screen,'green',(x,0),(x,500),3)
    mouse = pygame.mouse.get_pos()
    shadow = pygame.surface.Surface((500, 500))
    shadow.fill('grey')
    shadow.blit(pygame.image.load('light.png'), mouse)
    screen.blit(shadow, (0, 0), special_flags=pygame.BLEND_RGB_SUB)


    pygame.display.update()
pygame.quit()