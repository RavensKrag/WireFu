import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobjects import NonstaticObject
from gameobjects.platforms import Ramp
import collisions

class ZiplineWire(Ramp):
	# Inherit from the Ramp class to enable the
	# creation of angled ziplines.
	def __init__(self, p1, p2):
		super(ZiplineWire, self).__init__(p1, p2, 50)
		#~ self.handle = ZiplineHandle()
		#~ self.handle.body.position = Vec2d(p1)
		
		#~ self.joint = pm.GrooveJoint(self.body, self.handle.body,
									#~ (p1[0]+self.width/2, p1[1]), (p2[0]+self.width/2, p2[1]),
									#~ (0,0))
		
		self.shape.collision_type = collisions.ZIPLINE
		self.shape.friction = 0.1
	
	def update(self):
		pass
		#~ self.handle.update()
	
	def draw(self, screen):
		print('TESTING -- Entering ZiplineWire.draw()')
		#~ print "zipline draw"
		super(ZiplineWire, self).draw(screen)
		#~ self.handle.draw(screen)
	
	def add_to(self, space):
		super(ZiplineWire, self).add_to(space)
		#~ self.handle.add_to(space)
		
		#~ space.add(self.joint)
		
		self.space = space
