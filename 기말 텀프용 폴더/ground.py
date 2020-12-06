import gfw
from pico2d import *
import gobj
import game_state

class Ground:
    def __init__(self, left, speed):
        self.image = gfw.image.load(gobj.res('platform.png'))
        self.left = left
        self.bottom = 0
        self.width = 500
        self.height = 50
        self.speed = speed
    def update(self):
        self.left -= self.speed * gfw.delta_time
        sp = game_state.n_speed
        self.speed = sp
        if self.left + self.width <= 0:
            self.left = 1500 + self.left

    def draw(self):
        self.image.draw_to_origin(self.left, self.bottom, self.width, self.height)
