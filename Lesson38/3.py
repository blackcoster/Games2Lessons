import pygame

BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

screen = pygame.display.set_mode((600,400))
running = True
background = GRAY
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            if event.key == pygame.K_g:
                background = GREEN
            if event.key == pygame.K_b:
                background = BLUE

    screen.fill(background)
    caption = f'Цвет фона - {background}'
    pygame.display.set_caption(caption)
    pygame.display.update()


pygame.quit()