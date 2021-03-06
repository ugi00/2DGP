from pico2d import *
import gfw
import gobj
from button import Button
import game_state
import cookie_state

canvas_width = 1000
canvas_height = 700
PLAYER_SIZE = 270
Select = cookie_state.Select

class Player:
    ANIMS = [[0x40, 0x41, 0x42, 0x43]]
    def __init__(self):
        self.pos = 480, 350
        self.delta = 0, 0
        self.image = gfw.image.load(gobj.res('cookie_%d.png' % Select))
        self.time = 0
        self.FPS = 10
        self.anim = Player.ANIMS[0]

    def draw(self):
        anim = self.anim
        fidx = round(self.time * self.FPS) % len(anim)
        sprite_num = anim[fidx]
        x, y = sprite_num % 0x10, sprite_num // 0x10
        x = x * (PLAYER_SIZE + 2) + 2
        y = y * (PLAYER_SIZE + 2) + 2
        size = PLAYER_SIZE, PLAYER_SIZE
        self.image.clip_draw(x, y, 270, 270, *self.pos, *size)

    def update(self):
        global Select
        self.time += gfw.delta_time
        Select = cookie_state.Select
        self.image = gfw.image.load(gobj.res('cookie_%d.png' % Select))

def build_world():
    gfw.world.init(['bg', 'ui', 'player'])

    center = (canvas_width // 2, canvas_height // 2)
    bg = gobj.ImageObject('lobby.png', center)
    gfw.world.add(gfw.layer.bg, bg)

    font = gfw.font.load(gobj.res('CookieRun.TTF'), 30)

    l, b, w, h = 700, 150, 200, 80
    btn = Button(l, b, w, h, font, "게임 시작", lambda: gfw.change(game_state))
    gfw.world.add(gfw.layer.ui, btn)

    b -= 100
    btn = Button(l, b, w, h, font, "쿠키 선택", lambda: gfw.change(cookie_state))
    gfw.world.add(gfw.layer.ui, btn)

    global player
    player = Player()
    gfw.world.add(gfw.layer.player,player)

def enter():
    build_world()

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()

    if handle_mouse(e):
        return

capture = None

def handle_mouse(e):
    global capture
    if capture is not None:
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    for obj in gfw.world.objects_at(gfw.layer.ui):
        if obj.handle_event(e):
            capture = obj
            return True

    return False

def exit():
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()