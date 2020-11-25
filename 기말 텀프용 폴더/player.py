import random
from pico2d import *
import gfw
import gobj

PLAYER_SIZE = 270

class Player:
    RUNNING, FALLING, JUMPING, DOUBLE_JUMP, SLIDING = range(5)
    ANIMS = [
        [ 0x40, 0x41, 0x42, 0x43 ], # RUNNING
        [ 0x50 ],                   # FALLING
        [ 0x57, 0x58 ],             # JUMPING
        [ 0x51, 0x52, 0x53, 0x54 ], # DOUBLE_JUMP
        [ 0x59, 0x5A ],             # SLIDING
    ]
    MAGNIFIED_RUN_ANIM = [ 0x44, 0x45, 0x46, 0x47 ]
    BB_DIFFS = [
        (-60,-135,60,0),   # RUNNING
        (-60,-135,60,10),  # FALLING
        (-60,-135,60,-20), # JUMPING
        (-60,-135,60,-20), # DOUBLE_JUMP
        (-80,-135,80,-68), # SLIDING
    ]

    GRAVITY = 3000
    JUMP = 1000

    def __init__(self):
        self.pos = 150, get_canvas_height() // 2 -200
        self.delta = 0, 0
        self.image = gfw.image.load(gobj.res('cookie_1.png'))
        self.hp_image = gfw.image.load(gobj.res('hp.png'))
        self.time = 0
        self.FPS = 10
        self.state = Player.RUNNING
        self.hp = 100
        self.colide = 0

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state
        self.anim = Player.ANIMS[state]
    def draw(self):
        anim = self.anim
        fidx = round(self.time * self.FPS) % len(anim)
        sprite_num = anim[fidx]
        x, y = sprite_num % 0x10, sprite_num // 0x10
        x = x * (PLAYER_SIZE + 2) + 2
        y = y * (PLAYER_SIZE + 2) + 2
        size = PLAYER_SIZE, PLAYER_SIZE
        self.image.clip_draw(x, y, 270, 270, *self.pos, *size)
        h_x, h_y = self.hp*5, 30
        self.hp_image.draw_to_origin(100,600,h_x,h_y)

    def jump(self):
        if self.state in [Player.FALLING, Player.DOUBLE_JUMP, Player.SLIDING]: 
            return
        if self.state == Player.RUNNING:
            self.state = Player.JUMPING
        elif self.state == Player.JUMPING:
            self.state = Player.DOUBLE_JUMP
        self.jump_speed = Player.JUMP
    def slide(self):
        if self.state != Player.RUNNING: return
        self.state = Player.SLIDING
        self.time = 0.0
    def update(self):
        self.time += gfw.delta_time
        self.hp -= 0.05
        if self.hp <= 0:
            gfw.quit()
        if self.state in [Player.JUMPING, Player.DOUBLE_JUMP, Player.FALLING]:
            self.move((0, self.jump_speed * gfw.delta_time))
            self.jump_speed -= Player.GRAVITY * gfw.delta_time
            x,y = self.pos
            if y <= 150:
                y = 150
                self.pos = x,y
                self.state = Player.RUNNING

    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_DOWN:
                self.slide()
            elif e.key == SDLK_SPACE or e.key == SDLK_UP:
                self.jump()
            elif e.key == SDLK_1:
                n = random.randrange(1,7)
                self.image = gfw.image.load(gobj.res('cookie_%d.png' % n))
        if e.type == SDL_KEYUP:
            if e.key == SDLK_DOWN:
                self.state = Player.RUNNING

    def get_bb(self):
        l, b, r, t = Player.BB_DIFFS[self.state]
        x, y = self.pos
        return x + l, y + b, x + r, y + t
