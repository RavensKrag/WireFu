import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobjects import NonstaticObject
from gameobjects.platforms import Ramp
import collisions

class ZiplineHandle(NonstaticObject):
	# TODO: Create separate animation for the zipline handle
	
	def __init__(self):
		mass = 10
		
		# From bottom left, ccw winding
		verts = [(-0.2, -0.2), (0.2, -0.2), (0.2, 0.2), (-0.2, 0.2)]
		
		super(ZiplineHandle, self).__init__(mass, pm.inf, verts)
		
		# Override the image from NonstaticObject for now
		self.image = pygame.Surface([0.2*2, 0.2*2])
		self.image.fill(pygame.Color("yellow"))
		
		self.shape.collision_type = -1
	
	def update(self):
		pass
		#~ print self.body.position
		#~ NonstaticObject.update(self)
			#~ self.image, self.rect = self._animation.update()
	
	def draw(self, screen):
		pos = Physics.to_pygame(self.body.position)
		
		# Draw centered
		screen.blit(self.image, (pos[0]-self.image.get_width()/2, 
								pos[1]-self.image.get_height()/2))
