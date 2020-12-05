from pico2d import *
import gfw
import gobj
from button import Button
import lobby_state

canvas_width = 1000
canvas_height = 700
PLAYER_SIZE = 270
Select = 1

class Player:
    ANIMS = [[0x40, 0x41, 0x42, 0x43]]
    def __init__(self):
        self.pos = 250, 550
        self.delta = 0, 0
        self.image = gfw.image.load(gobj.res('cookie_1.png'))
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
        self.time += gfw.delta_time
        self.image = gfw.image.load(gobj.res('cookie_%d.png' % Select))

def build_world():
    gfw.world.init(['bg', 'ui', 'player'])

    center = (canvas_width // 2, canvas_height // 2)
    bg = gobj.ImageObject('character.png', center)
    gfw.world.add(gfw.layer.bg, bg)

    global font
    font = gfw.font.load(gobj.res('CookieRun.TTF'), 30)

    l, b, w, h = 650, 50, 200, 80
    btn = Button(l, b, w, h, font, "로비", lambda: gfw.change(lobby_state))
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

    pos = 620, get_canvas_height() - 150
    if Select == 1:
        font.draw(*pos, '용감한 쿠키', (255, 255, 255))
        pos = 560, get_canvas_height() - 250
        font.draw(*pos,'hp 높음', (255,255,255))
    elif Select == 2:
        font.draw(*pos, '명량한 쿠키', (255, 255, 255))
        pos = 560, get_canvas_height() - 250
        font.draw(*pos, 'hp 회복', (255, 255, 255))
    elif Select == 3:
        font.draw(*pos, '버터크림 쿠키', (255, 255, 255))
        pos = 560, get_canvas_height() - 250
        font.draw(*pos, '젤리 생성', (255, 255, 255))
    elif Select == 4:
        font.draw(*pos, '구름맛 쿠키', (255, 255, 255))
        pos = 560, get_canvas_height() - 250
        font.draw(*pos, '특수 공격', (255, 255, 255))
    elif Select == 5:
        font.draw(*pos, '딸기맛 쿠키', (255, 255, 255))
        pos = 560, get_canvas_height() - 250
        font.draw(*pos, '특수 공격', (255, 255, 255))
    elif Select == 6:
        font.draw(*pos, '쿠엔크 쿠키', (255, 255, 255))
        pos = 560, get_canvas_height() - 250
        font.draw(*pos, '특수 공격', (255, 255, 255))

def handle_event(e):
    global Select
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()
        if e.key == SDLK_RIGHT:
            Select += 1
            if Select == 7:
                Select = 1
        if e.key == SDLK_LEFT:
            Select -= 1
            if Select == 0:
                Select = 6

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