import pymunk as pm
from pymunk import Vec2d
import math, sys, random

class GameObject(object):
	def __init__(self, body, verts):
		self.body = body
		self.shape = 1
	
	def add_to(space):
		space.add(self.body, self.shape)
	
	def update(self):
		pass
	
	def draw(self):
		pass

class NonstaticObject(GameObject):
	def __init__(self, mass=1, moment=1, verts=[]):
		body = pm.Body(mass, moment)
		verts = 1
		
		super(NonstaticObject, self).__init__(body, verts)
	
	def update(self):
		pass
	
	def draw(self):
		pass

class StaticObject(GameObject):
	static_body = pm.Body
	
	def __init__(self, verts):
		verts = 1
		
		super(StaticObject, self).__init__(self.static_body, verts)
		
	def update(self):
		pass
	
	def draw(self):
		pass
	
