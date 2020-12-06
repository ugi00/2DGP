import random
import gfw
from pico2d import *
import gobj
from player import Player
from back_g import Background
from ground import Ground
from jelly import Jelly
from spine import *
from skill import *
from missile import Missile
import cookie_state
import ranking_state
from item import *

canvas_width = 1000
canvas_height = 700
n_speed = 500
jelly_trigger = 0
colide_trigger = 0
uspine_trigger = 40
missile_trigger = 0
speed_trigger = 0
score = 0
Select = cookie_state.Select
tt = 0
ctrl_m = 100
ctrl_c = 30
skill2_trigger = 20
skill4_trigger = 40
hp_item_trigger = 60
speed_item_trigger = 100
at_speed = 0
ats_trigger = 200

def enter():
    gfw.world.init(['bg', 'ground', 'spine', 'jelly', 'h_item', 's_item', 'missile','skill_w', 'skill_f', 'skill_g', 'player'])
    global score
    score = 0

    for n, speed in [(1,10), (2,100)]:
        bg = Background('cookie_run_bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    global ground
    for l, sp in [(0, n_speed), (500, n_speed),(1000, n_speed),(1500, n_speed)]:
        ground = Ground(l, sp)
        gfw.world.add(gfw.layer.ground, ground)

    global font
    font = gfw.font.load('res/CookieRun.ttf', 30)

    global Select
    Select = cookie_state.Select
    global player
    player = Player(Select)
    gfw.world.add(gfw.layer.player, player)

paused = False
def update():
    global tt
    if paused == True:
        return
    if player.hp <= 0:
        if Select == 2:
            if tt >= 4:
                gfw.change(ranking_state)
        else:
            if tt >= 5:
                gfw.change(ranking_state)
        tt += 1
        player.update()

    else:
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

        global ctrl_c, ctrl_m
        if player.colide == 1:
            colide_trigger += 1
            if colide_trigger == ctrl_c:
                player.colide = 0
                colide_trigger = 0

        global n_speed, speed_trigger
        speed_trigger += 1
        if speed_trigger == 100:
            n_speed += 10
            speed_trigger = 0
            if score > 10000:
                ctrl_m -= 5
                ctrl_c -= 0.5

        if score > 10000:
            missile_trigger += 1
            if missile_trigger == ctrl_m:
                make_missile()
                missile_trigger = 0

        global hp_item_trigger, speed_item_trigger
        if score > 5000:
            hp_item_trigger -= 1
            if hp_item_trigger == 0:
                make_hp()
                hp_item_trigger = 1000

        if score > 3000:
            speed_item_trigger -= 1
            if speed_item_trigger == 0:
                make_speed()
                speed_item_trigger = 500

        global at_speed, ats_trigger
        check_h_item()
        check_s_item()
        if at_speed != 0:
            ats_trigger -= 1
            if ats_trigger == 0:
                n_speed = at_speed
                at_speed = 0
                ats_trigger = 2000

        global skill2_trigger, skill4_trigger, skill_w, skill_f, skill_g

        if player.gauge == 0:
            if Select == 3:
                n = random.randrange(2,5)
                for i in range(n):
                    skill_j = Skill1(n_speed)
                    gfw.world.add(gfw.layer.jelly, skill_j)

            elif Select == 4:
                skill_w = Skill2()
                gfw.world.add(gfw.layer.skill_w, skill_w)
                check_S2_to_spine()

            elif Select == 5:
                S3_effect()
                skill_f = Skill3()
                gfw.world.add(gfw.layer.skill_f, skill_f)

            elif Select == 6:
                skill_g = Skill4()
                gfw.world.add(gfw.layer.skill_g, skill_g)
                S4_effect()

        elif player.gauge < 0:
            if Select == 3:
                player.gauge = 100
            elif Select == 4:
                check_S2_to_spine()
                skill2_trigger -= 1
                if skill2_trigger == 0:
                    player.gauge = 100
                    skill2_trigger = 20
            elif Select == 5:
                player.gauge = 100
            elif Select == 6:
                S4_effect()
                skill4_trigger -= 1
                if skill4_trigger == 0:
                    player.gauge = 100
                    skill4_trigger = 40

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

def check_h_item():
    for h_item in gfw.world.objects_at(gfw.layer.h_item):
        if gobj.collides_box(player, h_item):
            player.hp += 10
            gfw.world.remove(h_item)
            break

def check_s_item():
    global at_speed, n_speed
    for s_item in gfw.world.objects_at(gfw.layer.s_item):
        if gobj.collides_box(player, s_item):
            at_speed = n_speed
            n_speed += 200
            gfw.world.remove(s_item)
            break

def check_missile():
    for missile in gfw.world.objects_at(gfw.layer.missile):
        if gobj.collides_box(player, missile):
            player.hp -= 5
            gfw.world.remove(missile)
            break

def check_S2_to_spine():
    for missile in gfw.world.objects_at(gfw.layer.missile):
        if gobj.collides_box(skill_w, missile):
            gfw.world.remove(missile)
            break

    for spine in gfw.world.objects_at(gfw.layer.spine):
        if gobj.collides_box(skill_w, spine):
            gfw.world.remove(spine)
            break

def S3_effect():
    for missile in gfw.world.objects_at(gfw.layer.missile):
            gfw.world.remove(missile)

    for spine in gfw.world.objects_at(gfw.layer.spine):
            gfw.world.remove(spine)

def S4_effect():
    for jelly in gfw.world.objects_at(gfw.layer.jelly):
        if gobj.collides_box(skill_g, jelly):
            gfw.world.remove(jelly)
            global score
            score += 100
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

def make_hp():
    hp_item =Hp_Item(canvas_width,300,n_speed)
    gfw.world.add(gfw.layer.h_item,hp_item)

def make_speed():
    speed_item = Speed_Item(canvas_width,300,n_speed)
    gfw.world.add(gfw.layer.s_item,speed_item)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
