import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobjects import GameObject
from utilities import Animation
import Physics

class NonstaticObject(GameObject):
	# All moving objects should have some sort of animation.
	
	def __init__(self, mass=1, moment=1, verts=[]):
		self._animation = Animation()
		self.image, self.rect = self._animation.update()
		
		body = pm.Body(mass, moment)
		# Counterclockwise winding
		# Start from bottom left
		# Pos x: right		Pos y: up
		verts = [(-self._animation.get_width()/2, 0),
				(self._animation.get_width()/2, 0), 
				(self._animation.get_width()/2, self._animation.get_height()),
				(-self._animation.get_width()/2, self._animation.get_height())]
		
		#~ for i in range(0, len(verts)):
			#~ print verts[i]
			#~ verts[i] = Physics.to_pymunk(verts[i])
			#~ print "...{}".format(verts[i])
		
		super(NonstaticObject, self).__init__(body, verts)
	
	def update(self):
		self.image, self.rect = self._animation.update()
		
		#~ pos = Physics.to_pygame(self.body.position)
		#~ self.rect.left = pos[0]
		#~ self.rect.bottom = pos[1]
	
	def get_height(self):
		return self._animation.get_height()
