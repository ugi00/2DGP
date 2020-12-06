import gfw
from pico2d import *
import gobj
import game_state

class Hp_Item:
    def __init__(self, x, y, speed):
        self.image = gfw.image.load(gobj.res('hp_item.png'))
        self.rect = 2,2,113,113
        self.x = x
        self.y = y
        self.speed = speed
    def update(self):
        self.x -= self.speed * gfw.delta_time
        sp = game_state.n_speed
        self.speed = sp
        if self.x + 55 < 0:
            gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(*self.rect, self.x, self.y)
    def get_bb(self):
        return (
            self.x - 55, self.y - 55,
            self.x + 55, self.y + 55
        )

class Speed_Item:
    def __init__(self, x, y, speed):
        self.image = gfw.image.load(gobj.res('speed_item.png'))
        self.rect = 2,2,90,90
        self.x = x
        self.y = y
        self.speed = speed
    def update(self):
        self.x -= self.speed * gfw.delta_time
        sp = game_state.n_speed
        self.speed = sp
        if self.x + 45 < 0:
            gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(*self.rect, self.x, self.y)
    def get_bb(self):
        return (
            self.x - 45, self.y - 45,
            self.x + 45, self.y + 45
        )