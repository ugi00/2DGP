import random
import gfw
from pico2d import *
import gobj
from player import Player
from back_g import Background
from ground import Ground
from jelly import Jelly
from spine import *
from missile import Missile

canvas_width = 1000
canvas_height = 700
n_speed = 500
jelly_trigger = 0
colide_trigger = 0
uspine_trigger = 40
missile_trigger = 0
score = 0

def enter():
    gfw.world.init(['bg', 'ground', 'spine', 'jelly', 'missile', 'player'])

    for n, speed in [(1,10), (2,100)]:
        bg = Background('cookie_run_bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    for l, sp in [(0, n_speed), (500, n_speed),(1000, n_speed),(1500, n_speed)]:
        ground = Ground(l, sp)
        gfw.world.add(gfw.layer.ground, ground)

    global font
    font = gfw.font.load('res/CookieRun.ttf', 30)

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

paused = False
def update():
    if paused:
        return
    global score
    score += gfw.delta_time * 10

    gfw.world.update()
    global jelly_trigger, colide_trigger, uspine_trigger, missile_trigger
    jelly_trigger += 1
    if jelly_trigger == 80:
        make_jelly()
        jelly_trigger = 0
    check_jelly()
    uspine_trigger += 1
    if uspine_trigger == 80:
        make_uspine()
        uspine_trigger = 0

    if player.colide == 0:
        check_spine()
        check_missile()

    if player.colide == 1:
        colide_trigger += 1
        if colide_trigger == 30:
            player.colide = 0
            colide_trigger = 0

    if score > 5000:
        missile_trigger += 1
        if missile_trigger == 100:
            make_missile()
            missile_trigger = 0

def check_jelly():
    for jelly in gfw.world.objects_at(gfw.layer.jelly):
        if gobj.collides_box(player, jelly):
            gfw.world.remove(jelly)
            global score
            score += 100
            break
def check_spine():
    for spine in gfw.world.objects_at(gfw.layer.spine):
        if gobj.collides_box(player, spine):
            player.hp -= 10
            player.colide = 1
            break

def check_missile():
    for missile in gfw.world.objects_at(gfw.layer.missile):
        if gobj.collides_box(player, missile):
            player.hp -= 5
            gfw.world.remove(missile)
            break

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()
    score_pos = 800, get_canvas_height() - 30
    font.draw(*score_pos, 'Score: %.0f' % score, (255, 255, 255))

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
        spine = Spine2(n_speed, canvas_width + 10)
        gfw.world.add(gfw.layer.spine, spine)
        spine = Spine2(n_speed, canvas_width + 400)
        gfw.world.add(gfw.layer.spine, spine)
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
        spine = Spine1(n_speed,canvas_width + 150 )
        gfw.world.add(gfw.layer.spine, spine)
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
        spine = Spine2(n_speed, canvas_width + 100)
        gfw.world.add(gfw.layer.spine, spine)
        spine = Spine2(n_speed, canvas_width + 200)
        gfw.world.add(gfw.layer.spine, spine)

def make_uspine():
    spine = Spine3(n_speed,canvas_width + 120)
    gfw.world.add(gfw.layer.spine,spine)

def make_missile():
    missile = Missile(n_speed * 1.5,canvas_width + 100)
    gfw.world.add(gfw.layer.missile,missile)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
