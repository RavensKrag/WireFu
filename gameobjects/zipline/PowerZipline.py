import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobjects import NonstaticObject
from gameobjects.platforms import Ramp
from gameobjects.zipline import ZiplineWire
import collisions

class PowerZipline(ZiplineWire):
	# A zipline which emparts a force on the player as he grabs it, pushing
	# him into a given direction.
	# The force will move from p1 towards p2
	def __init__(self, p1, p2):
		print('p1, p2', p1, p2)
		super(PowerZipline, self).__init__(p1, p2)
		self.shape.collision_type = collisions.POWER_ZIPLINE
		
		self.wire_velocity = pm.Vec2d(p2[0]-p1[0], p2[1]-p1[1])
		self.wire_velocity = self.wire_velocity.normalized()
		
		self.color = pygame.Color("green")
	
	#~ def update(self):
		#~ pass
	#~ 
	#~ def draw(self, screen):
		#~ super(PowerZipline, self).draw(screen)
	#~ 
	#~ def add_to(self, space):
		#~ super(PowerZipline, self).add_to(space)
