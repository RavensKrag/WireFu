#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d

class PhysicsInterface(object):
	def __init__(self, shape):
		self.shape = shape
		self.body = shape.body
	
	def add_to(self, space):
		print "adding"
		self.space = space	# Store reference to space, so that the object can remove itself
		space.add(self.body, self.shape)
	
	def remove_from_space(self):
		if self.space:
			#~ if self.body == pm.Body():
			self.space.remove(self.body)
			self.space.remove(self.shape)
			
			#~ if self.body:
				#~ self.space.remove(self.body)
			#~ if self.shape:
				#~ self.space.remove(self.shape)
	
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
