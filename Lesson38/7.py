import  pygame
from pygame.locals import  *

GRAY = (127, 127, 127)
RED = (255,0,0)
BLUE = (0,0,255)
background = GRAY
size = 640,320
width,height = size
screen = pygame.display.set_mode(size)
running = True
start = (0,0)
size = (0,0)
drawing = False
rect_list = []

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            start = event.pos #(x1,y1)
            size = 0,0
            drawing = True

        if event.type == MOUSEBUTTONUP:
            end = event.pos #(x2,y2)
            size = end[0] - start[0],end[1] - start[1]
            rect = Rect(start,size)
            rect_list.append(rect)
            drawing = False

        if event.type == MOUSEMOTION and drawing ==True:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]

    screen.fill(background)
    for rect in rect_list:
        pygame.draw.rect(screen, RED, rect, 3)
    pygame.draw.rect(screen,BLUE,(start,size),1)


    # домашка
    # for rect in rect_list:
    #     pygame.draw.ellipse(screen, RED, rect, 3)
    # pygame.draw.ellipse(screen,BLUE,(start,size),1)

    pygame.display.update()
pygame.quit()