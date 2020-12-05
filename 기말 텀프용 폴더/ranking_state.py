from pico2d import *
import gfw
import gobj
from button import Button
import game_state
import lobby_state
import highscore

canvas_width = 1000
canvas_height = 700

def build_world():
    gfw.world.init(['ui', 'ui2'])
    global image
    image = load_image('res/ranking.png')

    font = gfw.font.load(gobj.res('CookieRun.TTF'), 30)

    l, b, w, h = 750, 50, 200, 80
    btn = Button(l, b, w, h, font, "로비", lambda: gfw.change(lobby_state))
    gfw.world.add(gfw.layer.ui, btn)

    highscore.load()
    highscore.add(game_state.score)
    gfw.world.add(gfw.layer.ui2, highscore)


def enter():
    build_world()

def update():
    gfw.world.update()

def draw():
    image.draw_to_origin(0, 0, 1000, 700)
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