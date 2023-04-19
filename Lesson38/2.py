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

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

    screen.fill(YELLOW)
    pygame.display.update()

pygame.quit()