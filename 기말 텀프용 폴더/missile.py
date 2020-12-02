import gfw
from pico2d import *
import gobj
import random

class Missile:
    def __init__(self, speed, x):
        self.image = gfw.image.load(gobj.res('missile.png'))
        self.x = x
        r = random.randrange(100,300)
        self.y = r
        self.rect = 0,0,202,117
        self.speed = speed
    def update(self):
        self.x -= self.speed * gfw.delta_time
        if self.x + 202 < 0:
            gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw_to_origin(*self.rect, self.x,self.y,202,117)
    def get_bb(self):
        return (
            self.x + 40, self.y + 20,
            self.x + 150, self.y + 80
        )