import arcade
import arcade.gui
from arcade.gui import UIOnClickEvent


class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, 'title', resizable=True)
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


        self.button = arcade.gui.UIFlatButton(text='open', width=200)
        self.box.add(self.button.with_space_around(bottom=20))

        self.button.on_click = self.on_click_b

    def on_click_b(self,event):
        message_box = arcade.gui.UIMessageBox(
            width=300,
            height=200,
            message_text='нажмите ок или выход',
            buttons=['Ok','Выход'],
            callback=self.on_message_box_press
        )
        self.manager.add(message_box)
        # self.box.remove(self.button)

    def on_message_box_press(self,button_text):
        if button_text=='Ok':
            print(button_text)
        elif button_text=='Выход':
            arcade.close_window()

    def on_draw(self):
        self.clear()
        self.manager.draw()


window = MyWindow()
arcade.run()