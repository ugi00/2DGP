import gfw
from pico2d import *
import gobj
import random

class Spine1:
    def __init__(self, speed, x):
        self.image = gfw.image.load(gobj.res('Hspine_1.png'))
        self.x = x
        self.y = 0
        self.idx = 1
        self.rect = 0,0,87,222
        self.speed = speed
    def update(self):
        self.x -= self.speed * gfw.delta_time
        if self.x < 800 and self.idx == 1:
            self.image = gfw.image.load(gobj.res('Hspine_2.png'))
            self.idx = 2
            if self.idx == 2:
                self.image = gfw.image.load(gobj.res('Hspine_3.png'))

        if self.x + 131 < 0:
            gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw_to_origin(*self.rect, self.x,self.y,120,310)
    def get_bb(self):
        return (
            self.x + 15, self.y,
            self.x + 90, self.y + 230
        )

class Spine2:
    def __init__(self, speed, x):
        self.image = gfw.image.load(gobj.res('Lspine_1.png'))
        self.x = x
        self.y = 0
        self.idx = 1
        self.rect = 0,0,81,131
        self.speed = speed
    def update(self):
        self.x -= self.speed * gfw.delta_time
        if self.x < 800 and self.idx == 1:
            self.image = gfw.image.load(gobj.res('Lspine_2.png'))
            self.idx = 2
            if self.idx == 2:
                self.image = gfw.image.load(gobj.res('Lspine_3.png'))

        if self.x + 131 < 0:
            gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw_to_origin(*self.rect, self.x,self.y,90,180)
    def get_bb(self):
        return (
            self.x + 15, self.y,
            self.x + 80, self.y + 130
        )