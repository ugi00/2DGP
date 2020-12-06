import random
from pico2d import *
import gfw
import gobj

class Skill1: # 젤리 랜덤 생성
    def __init__(self, speed):
        self.num = 1
        self.image = gfw.image.load(gobj.res('skill_jelly.png'))
        self.effect_image = gfw.image.load(gobj.res('skill1_effect_1.png'))
        self.x = random.randrange(800, 1000)
        self.y = random.randrange(100, 300)
        self.rect = 0,0,66,66
        self.speed = speed

    def update(self):
        if self.num < 5:
            self.num += 0.5
            self.effect_image = gfw.image.load(gobj.res('skill1_effect_%d.png' % self.num))
        self.x -= self.speed * gfw.delta_time
        if self.x + 66 < 0:
            gfw.world.remove(self)
    def draw(self):
        if self.num < 5:
            self.effect_image.clip_draw(*self.rect, self.x, self.y)
        else:
            self.image.clip_draw(*self.rect, self.x, self.y)
    def get_bb(self):
        return (
            self.x - 33, self.y - 33,
            self.x + 33, self.y + 33,
        )

class Skill2: # 파도
    def __init__(self):
        self.num = 1
        self.effect_image = gfw.image.load(gobj.res('skill2_effect_1.png'))
        self.x = 200
        self.y = 200
        self.rect = 0, 0, 413, 298
        self.nn = 0

    def update(self):
        if self.nn == 0:
            self.num += 0.5
            self.effect_image = gfw.image.load(gobj.res('skill2_effect_%d.png' % self.num))
            if self.num == 7:
                self.nn = 1
        else:
            self.nn += 1
            if self.nn == 10:
                gfw.world.remove(self)
                self.nn = 0

    def draw(self):
        self.effect_image.clip_draw(*self.rect, self.x, self.y)

    def get_bb(self):
        return (
            self.x - 205, self.y - 205,
            self.x + 150, self.y + 150,
        )

class Skill3: # 꽃
    def __init__(self):
        self.num = 1
        self.effect_image2 = gfw.image.load(gobj.res('skill3_effect2_1.png'))
        self.effect_image1 = gfw.image.load(gobj.res('skill3_effect_1.png'))
        self.x1 = random.randrange(300, 800)
        self.y1 = random.randrange(100, 400)
        self.x2 = random.randrange(300, 800)
        self.y2 = random.randrange(100, 400)
        self.rect1 = 0, 0, 210, 210
        self.rect2 = 0, 0, 217, 217

    def update(self):
        if self.num < 6:
            self.num += 0.5
            self.effect_image1 = gfw.image.load(gobj.res('skill3_effect_%d.png' % self.num))
            self.effect_image2 = gfw.image.load(gobj.res('skill3_effect2_%d.png' % self.num))
        else:
            gfw.world.remove(self)

    def draw(self):
        self.effect_image1.clip_draw(*self.rect1, self.x1, self.y1)
        self.effect_image2.clip_draw(*self.rect2, self.x2, self.y2)

class Skill4:
    pass