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
		
	def to_pygame(self, vec):
		# Convert from pymunk coordinates to pygame coordinates
		return Physics.to_px(vec.x), self.screen_height-Physics.to_px(vec.y)
	
	def to_pymunk(self, point):
		# Only implement if necessary
		return Vec2d(Physics.to_meters(point[0]), Physics.to_meters(point[1]))
	
	def add_to(self, space):
		space.add(self.body, self.shape)
	
	def get_x(self):
		return self.body.position.x
	
	def get_y(self):
		return self.body.position.y
	
