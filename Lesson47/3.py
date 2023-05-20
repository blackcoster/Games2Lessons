import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('свет')
clock = pygame.time.Clock()
running = True

player_img = pygame.image.load('player.png')
player_rect = player_img.get_rect()
player_rect.centerx = 100
player_rect.bottom = 100

light = pygame.image.load('light.png')
light = pygame.transform.scale(light,(100,50))
light_on = False

while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key ==pygame.K_SPACE:
            light_on = True
        if e.type == pygame.KEYUP and e.key ==pygame.K_SPACE:
            light_on = False
    screen.fill('gray')
    shadow = pygame.surface.Surface((500, 500))
    shadow.fill('grey')
    if light_on:
        shadow.blit(light,(player_rect.x + 20,player_rect.y + 20))
    screen.blit(shadow,(0,0),special_flags=pygame.BLEND_RGBA_SUB)
    screen.blit(player_img, player_rect)


    pygame.display.update()
pygame.quit()