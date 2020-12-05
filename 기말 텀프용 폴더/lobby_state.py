from pico2d import *
import gfw
import gobj
from button import Button
import game_state

canvas_width = 1000
canvas_height = 700

def build_world():
    gfw.world.init(['bg', 'ui'])

    center = (canvas_width // 2, canvas_height // 2)
    bg = gobj.ImageObject('lobby.png', center)
    gfw.world.add(gfw.layer.bg, bg)

    font = gfw.font.load(gobj.res('CookieRun.TTF'), 30)

    l, b, w, h = 700, 150, 200, 80
    btn = Button(l, b, w, h, font, "게임 시작", lambda: gfw.change(game_state))
    gfw.world.add(gfw.layer.ui, btn)

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