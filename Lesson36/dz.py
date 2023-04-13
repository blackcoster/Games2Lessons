
from array import array
from dataclasses import dataclass
import arcade
import arcade.gl
import random
import time
import math

SCREEN_TITLE = 'ДЗ31'

SPRITE_IMAGE_SIZE = 128

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_TILES = 0.5

SPRITE_SIZE = int(SPRITE_IMAGE_SIZE * SPRITE_SCALING_PLAYER)

SCREEN_GRID_WIDTH = 25
SCREEN_GRID_HEIGHT = 15

SCREEN_WIDTH = SPRITE_SIZE * SCREEN_GRID_WIDTH
SCREEN_HEIGHT = SPRITE_SIZE * SCREEN_GRID_HEIGHT

GRAVITY = 1500

DEFAULT_DAMPING = 1.0
PLAYER_DAMPING = 0.4

PLAYER_FRICTION = 1.0
WALL_FRICTION = 0.7
DYNAMIC_ITEM_FRICTION = 0.6

PLAYER_MASS = 2.0

PLAYER_MAX_HORIZONTAL_SPEED = 450
PLAYER_MAX_VERTICAL_SPEED = 1600
PLAYER_MOVE_FORCE_ON_GROUND = 8000
PLAYER_JUMP_IMPULSE = 1800

# начало добавленного кода дз 36
PARTICLE_COUNT = 300
MIN_FADE_TIME = 0.25
MAX_FADE_TIME = 1.5

@dataclass
class Burst:
   buffer: arcade.gl.Buffer
   vao: arcade.gl.Geometry
   start_time: float
# конец добавленного кода дз 36


class Game(arcade.Window):
    def __init__(self):
        super().__init__()
        self.player_sprite = None
        self.player_list = None
        self.wall_list = None
        self.bullet_list = None
        self.item_list = None

        self.left_pressed = False
        self.right_pressed = False

        arcade.set_background_color(arcade.color.AMAZON)

        self.physics_engine = None
        self.enemy = None
        self.enemy_list = None
        self.game = True

# начало добавленного кода дз 36
        self.burst_list = []

        self.program = self.ctx.load_program(
           vertex_shader="vertex_shader.glsl",
           fragment_shader="fragment_shader.glsl",
        )

        self.ctx.enable_only(self.ctx.BLEND)
# конец добавленного кода дз 36

    def setup(self):

        map_name = ":resources:/tiled_maps/pymunk_test_map.json"

        tile_map = arcade.load_tilemap(map_name, SPRITE_SCALING_TILES)

        self.wall_list = tile_map.sprite_lists["Platforms"]
        self.item_list = tile_map.sprite_lists["Dynamic Items"]

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING_PLAYER)
        grid_x = 1
        grid_y = 1
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.enemy = arcade.Sprite(':resources:images/tiles/bomb.png', 0.3)
        self.enemy.center_x = 200
        self.enemy.center_y = 100
        self.enemy_list.append(self.enemy)

        self.player_sprite.center_x = SPRITE_SIZE * grid_x + SPRITE_SIZE / 2
        self.player_sprite.center_y = SPRITE_SIZE * grid_y + SPRITE_SIZE / 2
        self.player_list.append(self.player_sprite)

        damping = DEFAULT_DAMPING
        gravity = (0, -GRAVITY)
        self.physics_engine = arcade.PymunkPhysicsEngine(damping=damping,
                                                         gravity=gravity)

        self.physics_engine.add_sprite(self.player_sprite,
                                       friction=PLAYER_FRICTION,
                                       mass=PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                       collision_type="player",
                                       max_horizontal_velocity=PLAYER_MAX_HORIZONTAL_SPEED,
                                       max_vertical_velocity=PLAYER_MAX_VERTICAL_SPEED)

        self.physics_engine.add_sprite_list(self.wall_list,
                                            friction=WALL_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

        self.physics_engine.add_sprite_list(self.enemy_list,
                                            friction=DYNAMIC_ITEM_FRICTION,
                                            collision_type="enemy")

        self.physics_engine.add_sprite_list(self.item_list,
                                            friction=DYNAMIC_ITEM_FRICTION,
                                            collision_type="item")



        def item_hit_handler(player, item_sprite, _arbiter, _space, _data):
            item_sprite.remove_from_sprite_lists()
# начало добавленного кода
            def _gen_initial_data(initial_x, initial_y):
                for i in range(PARTICLE_COUNT):
                    angle = random.uniform(0, 2 * math.pi)
                    speed = abs(random.gauss(0, 1)) * .5
                    dx = math.sin(angle) * speed
                    dy = math.cos(angle) * speed
                    red = random.uniform(0.5, 1.0)
                    green = random.uniform(0, red)
                    blue = 0
                    fade_rate = random.uniform(1 / MAX_FADE_TIME, 1 / MIN_FADE_TIME)

                    yield initial_x
                    yield initial_y
                    yield dx
                    yield dy
                    yield red
                    yield green
                    yield blue
                    yield fade_rate

            x2 = self.player_sprite.center_x / self.width * 2. - 1.
            y2 = self.player_sprite.center_y / self.height * 2. - 1.

            initial_data = _gen_initial_data(x2, y2)

            buffer = self.ctx.buffer(data=array('f', initial_data))
            buffer_description = arcade.gl.BufferDescription(buffer,
                                                             '2f 2f 3f f',
                                                             ['in_pos',
                                                              'in_vel',
                                                              'in_color',
                                                              'in_fade_rate'])
            vao = self.ctx.geometry([buffer_description])
            burst = Burst(buffer=buffer, vao=vao, start_time=time.time())
            self.burst_list.append(burst)
# конец добавленного кода


        self.physics_engine.add_collision_handler("player", "item", post_handler=item_hit_handler)

        def enemy_hit_handler(player, enemy, _arbiter, _space, _data):
            self.game = False

        self.physics_engine.add_collision_handler("player", "enemy", post_handler=enemy_hit_handler)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.UP:
            if self.physics_engine.is_on_ground(self.player_sprite):
                impulse = (0, PLAYER_JUMP_IMPULSE)
                self.physics_engine.apply_impulse(self.player_sprite, impulse)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        if self.game:
            if self.left_pressed and not self.right_pressed:
                force = (-PLAYER_MOVE_FORCE_ON_GROUND, 0)
                self.physics_engine.apply_force(self.player_sprite, force)
                self.physics_engine.set_friction(self.player_sprite, 0)
            elif self.right_pressed and not self.left_pressed:
                force = (PLAYER_MOVE_FORCE_ON_GROUND, 0)
                self.physics_engine.apply_force(self.player_sprite, force)
                self.physics_engine.set_friction(self.player_sprite, 0)
            else:
                self.physics_engine.set_friction(self.player_sprite, 1.0)
            self.physics_engine.step()
# начало добавленного кода
            temp_list = self.burst_list.copy()
            for burst in temp_list:
                if time.time() - burst.start_time > MAX_FADE_TIME:
                    self.burst_list.remove(burst)
# конец добавленного кода

    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.item_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()

# начало добавленного кода
        self.ctx.point_size = 2 * self.get_pixel_ratio()

        for burst in self.burst_list:
            self.program['time'] = time.time() - burst.start_time
            burst.vao.render(self.program, mode=self.ctx.POINTS)
# конец добавленного кода

if __name__ == "__main__":
    window = Game()
    window.setup()
    arcade.run()