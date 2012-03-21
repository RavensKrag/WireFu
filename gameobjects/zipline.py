import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobject import *
from Ramp import Ramp
import Collisions

class ZiplineWire(Ramp):
	# Inherit from the Ramp class to enable the
	# creation of angled ziplines.
	def __init__(self, p1, p2):
		super(ZiplineWire, self).__init__(p1, p2, 50)
		self.handle = ZiplineHandle()
		#~ self.handle.body.position = Vec2d(p1)
		
		#~ self.joint = pm.GrooveJoint(self.body, self.handle.body,
									#~ (p1[0]+self.width/2, p1[1]), (p2[0]+self.width/2, p2[1]),
									#~ (0,0))
		
		self.shape.collision_type = Collisions.ZIPLINE
		self.shape.friction = 0.1
	
	def update(self):
		#~ pass
		self.handle.update()
	
	def draw(self, screen):
		#~ print "zipline draw"
		super(ZiplineWire, self).draw(screen)
		self.handle.draw(screen)
	
	def add_to(self, space):
		super(ZiplineWire, self).add_to(space)
		self.handle.add_to(space)
		
		#~ space.add(self.joint)
		
		self.space = space

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
