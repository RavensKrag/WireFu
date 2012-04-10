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
	
	@staticmethod
	def to_px(meters):
		return int(meters*Physics.scale)
	
	@staticmethod
	def to_meters(px):
		return float(px)/Physics.scale
	
	@staticmethod	
	def to_pygame(vec):
		# Convert from pymunk coordinates to pygame coordinates
		return Physics.to_px(vec.x), Physics.screen_height-Physics.to_px(vec.y)
	
	@staticmethod
	def to_pymunk(point):
		# Only implement if necessary
		return Vec2d(Physics.to_meters(point[0]), Physics.to_meters(point[1]))
	
	def add_to(self, space):
		self.space = space	# Store reference to space, so that the object can remove itself
		space.add(self.body, self.shape)
	
	def remove_from_space(self):
		self.space.remove(self.body, self.shape)
	
	def _get_x(self):
		return self.body.position.x
	def _set_x(self, val):
		self.body.position.x = val
	x = property(_get_x, _set_x)
	
	def _get_y(self):
		return self.body.position.y
	def _set_y(self, val):
		self.body.position.y = val
	y = property(_get_y, _set_y)
	
	def _get_collision_type(self):
		self.shape.collision_type
	def _set_collision_type(self, col_type):
		self.shape.collision_type = col_type
	collision_type = property(_get_collision_type, _set_collision_type)
