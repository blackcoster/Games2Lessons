import arcade
from array import array
from dataclasses import dataclass
import arcade.gl
import random
import time
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_TITLE = 'ЧАСТИЦЫ'

PARTICLE_COUNT = 300
MIN_FADE_TIME = 0.25
MAX_FADE_TIME = 1.5


@dataclass
class Burst:
    buffer: arcade.gl.Buffer
    vao: arcade.gl.Geometry
    start_time: float


class MyWindow(arcade.Window):
    # def on_show(self):
    #     self.set_viewport(0,self.window.width,0,self.window.height)
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.burst_list = []

        self.program = self.ctx.load_program(
            vertex_shader='vertex_shader.glsl',
            fragment_shader='fragment_shader.glsl'
        )

        self.ctx.enable_only(self.ctx.BLEND)

    def on_draw(self):
        self.clear()
        self.ctx.point_size = 2 * self.get_pixel_ratio()

        for burst in self.burst_list:
            self.program['time'] = time.time() - burst.start_time
            burst.vao.render(self.program,mode = self.ctx.POINTS)

    def on_update(self, delta_time: float):
        temp_list = self.burst_list.copy()
        for burst in temp_list:
            if time.time() - burst.start_time > 4.0:
                self.burst_list.remove(burst)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        def _gen_initial_data(initial_x, initial_y):
            for i in range(PARTICLE_COUNT):
                angle = random.uniform(0,2*math.pi)
                speed = random.uniform(0.0,0.3)
                dx = math.cos(angle)*speed
                dy = math.sin(angle)*speed
                red = random.uniform(0.5,1.0)
                green = random.uniform(0,red)
                blue = 0.0
                fade_rate = random.uniform(1/MAX_FADE_TIME,1/MIN_FADE_TIME)

                yield initial_x
                yield initial_y
                yield dx
                yield dy
                yield red
                yield green
                yield blue
                yield fade_rate

        x2 = x / self.width * 2. - 1.
        y2 = y / self.height * 2. - 1.

        initial_data = _gen_initial_data(x2, y2)

        buffer = self.ctx.buffer(data=array('f', initial_data))
        buffer_description = arcade.gl.BufferDescription(buffer,
                                                         '2f 2f 3f f',
                                                         ['in_pos','in_vel','in_color','in_fade_rate'])

        vao = self.ctx.geometry([buffer_description])

        burst = Burst(buffer=buffer, vao=vao, start_time=time.time())
        self.burst_list.append(burst)


window = MyWindow()
arcade.run()
