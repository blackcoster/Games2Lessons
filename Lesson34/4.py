import arcade
import arcade.gui
lives = 5
monetkas = 0

LOREM_IPSUM = (
   "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eget pellentesque velit. "
   "Nam eu rhoncus nulla. Fusce ornare libero eget ex vulputate, vitae mattis orci eleifend. "
   "Donec quis volutpat arcu. Proin lacinia velit id imperdiet ultrices. Fusce porta magna leo, "
   "non maximus justo facilisis vel. Duis pretium sem ut eros scelerisque, a dignissim ante "
   "pellentesque. Cras rutrum aliquam fermentum. Donec id mollis mi.\n"
   "\n"
   "Nullam vitae nunc aliquet, lobortis purus eget, porttitor purus. Curabitur feugiat purus sit "
   "amet finibus accumsan. Proin varius, enim in pretium pulvinar, augue erat pellentesque ipsum, "
   "sit amet varius leo risus quis tellus. Donec posuere ligula risus, et scelerisque nibh cursus "
   "ac. Mauris feugiat tortor turpis, vitae imperdiet mi euismod aliquam. Fusce vel ligula volutpat, "
   "finibus sapien in, lacinia lorem. Proin tincidunt gravida nisl in pellentesque. Aenean sed "
   "arcu ipsum. Vivamus quam arcu, elementum nec auctor non, convallis non elit. Maecenas id "
   "scelerisque lectus. Vivamus eget sem tristique, dictum lorem eget, maximus leo. Mauris lorem "
   "tellus, molestie eu orci ut, porta aliquam est. Nullam lobortis tempor magna, egestas lacinia lectus.\n")

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(800,600,'okno',resizable=True)
        arcade.set_background_color(arcade.color.COOL_GREY)
        bg_tex = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.box = arcade.gui.UIBoxLayout()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x='center_x',
                anchor_y = 'center_y',
                child=self.box
            )
        )

        self.manager.add(
            arcade.gui.UITexturePane(
                child=arcade.gui.UIInputText(x=340,y=200,width=200,height=50,text=str(lives)),
                tex= bg_tex,
                padding=(10,10,10,10)

            )
        )

        self.manager.add(
            arcade.gui.UIInputText(x= 340,y = 110,width=200,height=50,text=str(monetkas))
        )


        text_area = arcade.gui.UITextArea(x=100,y=200,width=200,height=300,text = LOREM_IPSUM,text_color=(0,0,0,255))
        self.manager.add(
            arcade.gui.UITexturePane(
                child = text_area.with_space_around(right=20),
                tex = bg_tex,
                padding = (10,10,10,10)


            )

        )


    def on_draw(self):
        self.clear()
        self.manager.draw()




window = MyWindow()
arcade.run()