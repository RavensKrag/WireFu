import os, pygame
import pymunk as pm
from pymunk import Vec2d

class Killscreen(object):
	def __init__(self):
		pass
	
	def update(self):
		pass
	
	def draw(self):
		if((not self.game_clock.is_active()) and (self.game_clock.get_time() != (0,0,0))):
			self.killscreen.update()
			self.killscreen.draw(screen)
	
	def delete(self):
		pass
