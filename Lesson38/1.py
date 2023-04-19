import pygame


screen = pygame.display.set_mode((640,240))
running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
