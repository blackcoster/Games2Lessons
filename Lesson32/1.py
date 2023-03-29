import arcade

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 360
SCREEN_TITLE = 'ЗВУК'

class SoundWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.background = arcade.load_texture('resources/sound.jpg')
        self.sound = None
        self.sound_player = None

    def setup(self):
        self.sound = arcade.load_sound('resources/music.mp3')


    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 150<y<211 and 45<x<108:
            print('play')
            self.sound_player = arcade.play_sound(self.sound,volume=0.4,looping=True)

        if 150<y<211 and 147<x<211:
            print('stop')
            arcade.stop_sound(self.sound_player)


game = SoundWindow()
game.setup()
arcade.run()


