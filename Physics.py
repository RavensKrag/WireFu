#~ import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
#~ import pymunk as pm
#~ from pymunk import Vec2d

class Physics(object):
	screen_height = None
	
	#~ def to_px(self, meters):
		#~ return int(meters)
	#~ 
	#~ def to_meters(self, px):
		#~ return int(p.x)
		
	def to_pygame(self, vec):
		# Convert from pymunk coordinates to pygame coordinates
		return to_px(vec.x), self.screen_height-to_px(vec.y)
	
	#~ def to_pymunk(self, point):
		#~ # Only implement if necessary
		#~ return Vec2d(float(point[0]), float(point[1]))
	
	def add_to(self, space):
		space.add(self.body, self.shape)
	
