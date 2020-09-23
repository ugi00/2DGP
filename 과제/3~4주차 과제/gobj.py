import random
from pico2d import *

class Grass:
	def __init__(self):
		self.image = load_image('./grass.png')
	def draw(self):
		self.image.draw(400, 30)
	def update(self):
		pass

class Boy:
	#constructor
	# def __init__(self, pos, delta):
	# 	self.x, self.y = pos
	# 	self.dx, self.dy = delta
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

		
