import arcade
import arcade.gui
from arcade.gui import UIOnClickEvent


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: UIOnClickEvent):
        print('i quit')
        arcade.exit()

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
        
        start_button = arcade.gui.UIFlatButton(text='старт',width=200)
        self.box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text='настройки',width=200)
        self.box.add(settings_button.with_space_around(bottom=20))

        quit_button = QuitButton(text='выход',width=200)
        self.box.add(quit_button)

        settings_button.on_click = self.on_click_settings

        @start_button.event('on_click')
        def on_click_start(event):
            print('start')

    def on_click_settings(self,event):
        print('настройки')

    def on_draw(self):
        self.clear()
        self.manager.draw()

window = MyWindow()
arcade.run()