import pygame
from pygame.locals import *

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('пинг-понг')

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound('sound.wav')
win = pygame.mixer.Sound('win.wav')

xb = 500
yb = 300
ball_speed = 5
right = False
top = False

x1 = 0
y1 = 250

x2 = 490
y2 = 250

score1 = 0
score2 = 0
def collision():
    global x1,x2,y1,y2,xb,yb,x,y,right,top,score2,score1

    if right == True:
        if xb > 480:
            if yb >= y and yb <= y+50:
                sound.play()
                right = False
            else:
                score1 += 1
                win.play()
                pygame.display.set_caption(f'пинг-понг  СЧЁТ {score1}:{score2}')
                pygame.time.delay(500)
                xb,yb = 10,20
    else:
        if xb <11:
            if yb >= y1 and yb <= y1+50:
                sound.play()
                right = True
            else:

                score2 +=1
                win.play()
                pygame.display.set_caption(f'пинг-понг  СЧЁТ {score1}:{score2}')
                pygame.time.delay(500)
                xb, yb = 480, 20


def sprite1(y):
    pygame.draw.rect(screen,BLUE,(x1,y,10,50))

def sprite2(y):
    pygame.draw.rect(screen,RED,(x2,y,10,50))

def move1():
    global y1
    if keys[K_z] == True and y1 <=440:
        y1 += 10
    if keys[K_a]== True and y1 >0:
        y1 -= 10

def ball():
    global xb,yb
    pygame.draw.circle(screen,GREEN,(xb,yb),5)

def move_ball(x,y):
    global xb,yb,right,top,ball_speed
    if right == False:
        xb -= ball_speed
    if top == False:
        yb += ball_speed
        if yb > 490:
            top = True
    if top == True:
        yb -= ball_speed
        if yb < 5:
            top = False
    if right == True:
        xb += ball_speed
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()


    screen.fill(BLACK)
    ball()
    sprite1(y1)
    x,y = pygame.mouse.get_pos()
    sprite2(y)
    move1()
    move_ball(xb,yb)
    collision()
    pygame.display.update()
pygame.quit()