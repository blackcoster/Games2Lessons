import pygame
import math

text_map = [
   'WWWWWWWWWWWW',
   'W..........W',
   'W..........W',
   'W....WW....W',
   'W..........W',
   'W....WW....W',
   'W..........W',
   'WWWWWWWWWWWW',
]
TILE = 100
world_map = set()
for j, row in enumerate(text_map):
   for i, char in enumerate(row):
       if char == 'W':
           world_map.add((i * TILE, j * TILE))

class Player:
   def __init__(self):
       self.x, self.y = player_pos
       self.angle = player_angle

   @property
   def pos(self):
       return (self.x, self.y)

   def movement(self):
       sin_a = math.sin(self.angle)
       cos_a = math.cos(self.angle)
       keys = pygame.key.get_pressed()
       if keys[pygame.K_w]:
           self.x += player_speed * cos_a
           self.y += player_speed * sin_a
       if keys[pygame.K_s]:
           self.x += -player_speed * cos_a
           self.y += -player_speed * sin_a
       if keys[pygame.K_a]:
           self.x += player_speed * sin_a
           self.y += -player_speed * cos_a
       if keys[pygame.K_d]:
           self.x += -player_speed * sin_a
           self.y += player_speed * cos_a
       if keys[pygame.K_LEFT]:
           self.angle -= 0.02
       if keys[pygame.K_RIGHT]:
           self.angle += 0.02

WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH / 2
HALF_HEIGHT = HEIGHT / 2
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 50
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH  // NUM_RAYS

player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2

def ray_casting(sc, player_pos, player_angle):
   cur_angle = player_angle - HALF_FOV
   xo, yo = player_pos
   for ray in range(NUM_RAYS):
       sin_a = math.sin(cur_angle)
       cos_a = math.cos(cur_angle)
       for depth in range(MAX_DEPTH):
           x = xo + depth * cos_a
           y = yo + depth * sin_a
           # pygame.draw.line(sc, DARKGRAY, player_pos, (x, y), 2)
           if (x // TILE * TILE, y // TILE * TILE) in world_map:
               depth *= math.cos(player_angle - cur_angle)
               proj_height = PROJ_COEFF / depth
               c = 255 / (1 + depth * depth * 0.0001)
               color = (c, c, c)
               pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
               break
       cur_angle += DELTA_ANGLE
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player()
while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           quit()

   player.movement()
   sc.fill(BLACK)
   ray_casting(sc, player.pos, player.angle)
   # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
   # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
   #                                          player.y + WIDTH * math.sin(player.angle)))
   #
   # for x, y in world_map:
   #     pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)
   pygame.display.update()
   clock.tick(FPS)



