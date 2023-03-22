import random

import arcade

SCREEN_TITLE = 'аНИМАЦИЯ'
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

GRAVITY = 1

PLAYER_MOVEMENT_SPEED = 2

RIGHT_FACING = 0
LEFT_FACING = 1

def load_texture_pair(filename):
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename,flipped_horizontally=True)
    ]
class NPC(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.current_texture = 0
        self.scale = 1
        main_path = 'resources/person'
        self.ded_texture = []
        for i in range(1,9):
            texture = load_texture_pair(f'{main_path}/oldman-idle/oldman-idle-{i}.png')
            self.ded_texture.append(texture)
        self.texture = self.ded_texture[0][1]

    def update_animation(self, delta_time: float = 1 / 60):
        self.current_texture+=0.25
        if self.current_texture%2==0:
            self.current_texture =0

        self.texture = self.ded_texture[int(self.current_texture)][1]

class Person(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.person_face_direction = RIGHT_FACING
        self.current_texture = 0
        self.scale = 1
        main_path = 'resources/person'
        self.does_he_stand = True

        self.stand_textures = []
        for i in range(1,6):
            texture = load_texture_pair(f'{main_path}/bearded-idle/bearded-idle-{i}.png')
            self.stand_textures.append(texture)

        self.run_textures = []
        for i in range(1,7):
            texture = load_texture_pair(f'{main_path}/bearded-walk/bearded-walk-{i}.png')
            self.run_textures.append(texture)

        self.texture = self.stand_textures[0][0]

    def update_animation(self, delta_time: float = 1 / 60):
        if self.change_x<0 and self.person_face_direction ==RIGHT_FACING:
            self.person_face_direction = LEFT_FACING

        elif self.change_x>0 and self.person_face_direction ==LEFT_FACING:
            self.person_face_direction = RIGHT_FACING

        if self.change_x == 0:
            self.current_texture += 0.5
            if self.current_texture % 2 == 0:
                self.texture = self.stand_textures[0][self.person_face_direction]
                if self.current_texture >= 5:
                    self.current_texture = 0
                self.texture = self.stand_textures[int(self.current_texture)][
                    self.person_face_direction
                ]
        if not self.does_he_stand:
            self.current_texture = int(self.current_texture)
            self.current_texture += 1
            if self.current_texture >= 6:
                self.current_texture = 0
            self.texture = self.run_textures[self.current_texture][
                self.person_face_direction
            ]


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE,update_rate=1/30)
        self.bg_layer1 = arcade.load_texture('resources/bg/background.png')
        self.bg_layer2 = arcade.load_texture('resources/bg/middleground.png')
        self.ground_list = None
        self.house_list = None
        self.physics_engine = None

    def setup(self):
        self.ground_list = arcade.SpriteList()
        for i in range(0,SCREEN_WIDTH+1,16):
            r_sprite = random.randint(1,2)
            ground = arcade.Sprite(f'resources/enviroments/wall-{r_sprite}.png')
            ground.center_x = i
            ground.center_y = 5
            self.ground_list.append(ground)

        self.house_list = arcade.SpriteList()
        for i in range(3):
            house = arcade.Sprite(f'resources/enviroments/house-{i}.png')
            house.center_x = 80 + i*220
            if i!=1:
                house.center_y = 105
            else:
                house.center_y = 135
            self.house_list.append(house)

        self.player = Person()
        self.player.center_x = 50
        self.player.bottom = self.ground_list[0].top

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,gravity_constant=GRAVITY,walls = self.ground_list)

        self.npc = NPC()
        self.npc.center_x = 150
        self.npc.bottom = self.ground_list[0].top

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg_layer1)
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg_layer2)
        self.ground_list.draw()
        self.house_list.draw()
        self.player.draw()
        self.npc.draw()

    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.player.update_animation()
        self.npc.update_animation()

    def on_key_press(self, key: int, modifiers: int):
        if key==arcade.key.LEFT:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
            self.player.does_he_stand = False

        elif key==arcade.key.RIGHT:
            self.player.change_x = PLAYER_MOVEMENT_SPEED
            self.player.does_he_stand = False

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.player.change_x = 0
            self.player.does_he_stand = True

        elif key == arcade.key.RIGHT:
            self.player.change_x = 0
            self.player.does_he_stand = True


game = Game()
game.setup()
arcade.run()


