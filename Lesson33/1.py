import datetime
import time

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'работа с окнами'

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.25
COIN_COUNT = 10

class PauseView(arcade.View):
    def __init__(self,game_view):
        super().__init__()
        self.game_view = game_view
        arcade.set_background_color(arcade.color.ORANGE_PEEL)
    def on_draw(self):
        self.clear()
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()
        arcade.draw_text('Нажми пробел для продолжения',
                         self.window.width / 2,
                         self.window.height / 2,
                         arcade.color.BLACK,
                         font_size=30,
                         anchor_x='center')
        arcade.draw_text('Нажми Esc чтобы играть заново',
                         self.window.width / 2,
                         self.window.height / 2 - 75,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x='center')
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top = player_sprite.top,
                                          bottom = player_sprite.bottom,
                                          color=arcade.color.ORANGE+(200,))

    def on_key_press(self, key: int, modifiers: int):
        if key==arcade.key.SPACE:
            self.window.show_view(self.game_view)
        elif key==arcade.key.ESCAPE:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('game_over.png')

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

class StartView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        # arcade.set
    def on_draw(self):
        self.clear()
        arcade.draw_text('Стартовый экран',
                         self.window.width/2,
                         self.window.height/2,
                         arcade.color.WHITE,
                         font_size=50,
                         anchor_x='center')
        arcade.draw_text('Щелкни для продолжения',
                         self.window.width / 2,
                         self.window.height / 2 - 75,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x='center')

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 233 < x< 564 and 221 <y< 248:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

    # def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
    #     print(f'x-{x}')
    #     print(f'y-{y}')


class GameView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)
        self.window.set_mouse_visible(False)
        self.player_sprite = None
        self.player_list = None

        self.coin_list = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(':resources:images/animated_characters/female_person/femalePerson_idle.png',
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.coin_list = arcade.SpriteList()
        a = random.randint(10,100)
        for i in range(a):
            coin = arcade.Sprite(':resources:images/items/coinGold.png',
                                 SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.coin_list.draw()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time: float):
        self.coin_list.update()
        coins_hit_list =arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()

        coin = arcade.Sprite(':resources:images/items/coinGold.png',
                             SPRITE_SCALING_COIN)
        coin.center_x = random.randrange(SCREEN_WIDTH)
        coin.center_y = random.randrange(SCREEN_HEIGHT)
        if len(self.coin_list) ==0:
            gameoverview = GameOverView()
            self.window.show_view(gameoverview)

    def on_key_press(self, key: int, modifiers: int):
        if key==arcade.key.SPACE:
            pause = PauseView(self)
            self.window.show_view(pause)

window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
start_view = StartView()
window.show_view(start_view)
arcade.run()
