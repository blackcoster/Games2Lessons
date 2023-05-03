# rect.collidepoint()
# rect.colliderect(Rect)
# rect.colidelist(list)
# rect.colidelistall(list)

import pygame
from pygame import *


class Platform(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH,PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x,y,PLATFORM_WIDTH,PLATFORM_HEIGHT)

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)

        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right,up,platforms):
        if up:
            if self.onGround:
                self.yvel-=JUMP_POWER
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED

        if not (right or left):
            self.xvel = 0

        if self.onGround == False:
            self.yvel+=GRAVITY
        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0,self.yvel,platforms)
        self.rect.x += self.xvel
        self.collide(self.xvel,0,platforms)



    def collide(self,xvel,yvel,platforms):
        for p in platforms:
            if sprite.collide_rect(self,p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel <0:
                    self.rect.left = p.rect.right

                if yvel>0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel <0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0


SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 640
BACKGROUND_COLOR = '#004400'

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = '#FF6262'

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = '#888888'

GRAVITY = 0.35
JUMP_POWER = 10


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Платформер')
    bg = Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))

    running = True
    hero = Player(55, 55)
    left = right = False
    up = False

    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)

    timer = pygame.time.Clock()

    level = [
        "-------------------------",
        "-                       -",
        "-                       -",
        "-                       -",
        "-            --         -",
        "-                       -",
        "--                      -",
        "-                       -",
        "-                   --- -",
        "-                       -",
        "-                       -",
        "-      ---              -",
        "-                       -",
        "-   -----------         -",
        "-                       -",
        "-                -      -",
        "-                   --  -",
        "-                       -",
        "-                       -",
        "-------------------------"]

    x = y = 0
    for row in level:
        for col in row:
            if col == '-':
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0

    while running:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYDOWN and event.key == K_UP:
                up = True

            if event.type == KEYUP and event.key == K_LEFT:
                left = False
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False
            if event.type == KEYUP and event.key == K_UP:
                up = False

        screen.blit(bg, (0, 0))


        hero.update(left, right,up,platforms)
        entities.draw(screen)
        pygame.display.update()


main()
