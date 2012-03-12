import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d

class Physics(object):
	screen_height = None
	scale = 50*3# Number of pixels per meter
	
	def __init__(self, shape):
		self.shape = shape
		self.body = shape.body
	
	def to_px(self, meters):
		return int(meters*self.scale)
	
	def to_meters(self, px):
		return float(px)/self.scale
		
	def to_pygame(self, vec):
		# Convert from pymunk coordinates to pygame coordinates
		return self.to_px(vec.x), self.screen_height-self.to_px(vec.y)
	
	def to_pymunk(self, point):
		# Only implement if necessary
		return Vec2d(self.to_meters(point[0]), self.to_meters(point[1]))
	
	def add_to(self, space):
		space.add(self.body, self.shape)
	
	def get_x(self):
		return self.body.position.x
	
	def get_y(self):
		return self.body.position.y
	
