import random
import gfw
from pico2d import *
import gobj
from player import Player
from back_g import Background
from ground import Ground
from jelly import Jelly

canvas_width = 1200
canvas_height = 700
n_speed = 400
jelly_trigger = 0

def enter():
    gfw.world.init(['bg', 'ground', 'jelly', 'player'])

    for n, speed in [(1,10), (2,100)]:
        bg = Background('cookie_run_bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    for l, sp in [(0, n_speed), (480, n_speed),(960, n_speed),(1440, n_speed)]:
        ground = Ground(l, sp)
        gfw.world.add(gfw.layer.ground, ground)

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

paused = False
def update():
    if paused:
        return
    gfw.world.update()
    global jelly_trigger
    jelly_trigger += 1
    if jelly_trigger == 60:
        make_jelly()
        jelly_trigger = 0
    check_jelly()

def check_jelly():
    for jelly in gfw.world.objects_at(gfw.layer.jelly):
        if gobj.collides_box(player, jelly):
            gfw.world.remove(jelly)
            break

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return
        elif e.key == SDLK_p:
            global paused
            paused = not paused

    if player.handle_event(e):
        return

def make_jelly():
    sh = random.randrange(1, 4)
    if sh == 1:
        for i in range(10):
            x = canvas_width + i*60
            y = 200
            jelly = Jelly(n_speed, x, y)
            gfw.world.add(gfw.layer.jelly, jelly)
    elif sh == 2:
        for i in range(4):
            x = canvas_width + i*60
            y = 250 + i*60
            jelly = Jelly(n_speed, x, y)
            gfw.world.add(gfw.layer.jelly, jelly)
        for i in range(4):
            x = canvas_width + (i+4)*60
            y = 430 - i*60
            jelly = Jelly(n_speed, x, y)
            gfw.world.add(gfw.layer.jelly, jelly)
    elif sh == 3:
        for i in range(2):
            x = canvas_width + i*60
            y = 200 + i*60
            jelly = Jelly(n_speed, x, y)
            gfw.world.add(gfw.layer.jelly, jelly)
        for i in range(4):
            x = canvas_width + (i+2)*60
            y = 260
            jelly = Jelly(n_speed, x, y)
            gfw.world.add(gfw.layer.jelly, jelly)
        for i in range(2):
            x = canvas_width + (i+6)*60
            y = 260 - i*60
            jelly = Jelly(n_speed, x, y)
            gfw.world.add(gfw.layer.jelly, jelly)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
