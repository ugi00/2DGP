from pico2d import *
import helper
import random

class Grass:
	def __init__(self):
		self.image = load_image('./grass.png')
	def draw(self):
		self.image.draw(400, 30)
	def update(self):
		pass

class Boy:
        def __init__(self):
                self.x = random.randint(100, 300)
                self.y = random.randint(100, 300)
                self.dx, self.dy = 0, 0
                self.list = []
                self.target = (self.x, self.y)
                self.speed = 0
                self.done = True
                self.pos = (self.x, self.y)
                self.fidx = 0
                self.image = load_image('./run_animation.png')
        def draw(self):
                self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
        def update(self):
                self.fidx = (self.fidx + 1) % 8
                self.x, self.y = self.pos
                if self.done == True:
                        del self.list[0]
                        self.target = self.list[0]
                        self.speed = 1
                

def enter():
    global grass, boy
    grass = Grass()
    boy = Boy()

def update():
    boy.update()

def draw():
    grass.draw()
    boy.draw()

def handle_events():
    global running
    global dx, dy, x, y
    evts = get_events()
    boy.done = False
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False
        elif e.type == SDL_MOUSEBUTTONDOWN:
            boy.speed += 1
            boy.list.append((e.x, 600-e.y-1))
            boy.target = boy.list[0]
            boy.pos,boy.done = helper.move_toward(boy.pos, helper.delta(boy.pos, boy.target, boy.speed), boy.target)

open_canvas(800, 600)

enter()

running = True

while running:
    handle_events()
    boy.pos,boy.done = helper.move_toward(boy.pos, helper.delta(boy.pos, boy.target, boy.speed), boy.target)

    update()

    clear_canvas()
    draw()
    update_canvas()

    delay(0.01)

close_canvas()
