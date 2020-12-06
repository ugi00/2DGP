import gfw
from pico2d import *
import gobj
import random
import game_state

JELLY_BORDER = 2
JELLY_SIZE = 66
BB_RADIUS = 30

def get_jelly_rect(index):
    ix, iy = index % 30, index // 30
    x = ix * (JELLY_BORDER + JELLY_SIZE) + JELLY_BORDER
    y = iy * (JELLY_BORDER + JELLY_SIZE) + JELLY_BORDER
    return x, y, JELLY_SIZE, JELLY_SIZE

class Jelly:
    def __init__(self, speed, x, y):
        self.image = gfw.image.load(gobj.res('jelly.png'))
        idx = random.randint(3, 60)
        self.rect = get_jelly_rect(idx)
        self.x = x
        self.y = y
        self.speed = speed
    def update(self):
        self.x -= self.speed * gfw.delta_time
        sp = game_state.n_speed
        self.speed = sp
        if self.x + JELLY_SIZE < 0:
            gfw.world.remove(self)
    def draw(self):
        self.image.clip_draw(*self.rect, self.x, self.y)
    def get_bb(self):
        return (
            self.x - BB_RADIUS, self.y - BB_RADIUS,
            self.x + BB_RADIUS, self.y + BB_RADIUS
        )

