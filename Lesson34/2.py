import arcade
import arcade.gui
from arcade.gui import UIOnClickEvent

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800,600,'title',resizable = True)
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.box = arcade.gui.UIBoxLayout()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x='center_x',
                anchor_y='center_y',
                child=self.box
            )
        )

        button = arcade.gui.UIFlatButton(text='flat button',width=200)
        self.box.add(button)

        @button.event('on_click')
        def on_click_button(event):
            print('i pressed flat buttom')


        texture = arcade.load_texture(':resources:onscreen_controls/flat_dark/play.png')
        texture_button = arcade.gui.UITextureButton(texture=texture)
        self.box.add(texture_button.with_space_around(top=30))

        @texture_button.event('on_click')
        def on_click_texture_button(event):
            print('texture button pressed')


        text_label = arcade.gui.UITextArea(text='Пример',
                                           width = 150,
                                           height = 40,
                                           font_size=24,
                                           font_name='Kenney Future')
        self.box.add(text_label)

        text = 'Это текст который будет лежать внутри виджета'
        text_label = arcade.gui.UITextArea(text=text,
                                           width=450,
                                           height=60,
                                           font_size=12,
                                           font_name='Arial')
        self.box.add(text_label)

    def on_draw(self):
        self.clear()
        self.manager.draw()

window = MyWindow()
arcade.run()