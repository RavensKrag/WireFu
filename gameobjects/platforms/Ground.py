# Define the 

import pygame
import Physics
import collisions
from gameobjects import StaticObject

class Ground(StaticObject):
	def __init__(self):
		self.width = 10
		self.height = 5
		
		verts = [(0,0), (self.width,0), (self.width,-self.height), (0,-self.height)]
		
		super(Ground, self).__init__(verts)
		
		self.shape.collision_type = collisions.GROUND
		self.shape.friction = 0.8
		
	def update(self):
		pass
	
	def draw(self, screen):
		pass
