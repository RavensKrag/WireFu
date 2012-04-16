import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

import Physics
from PhysicsInterface import *

class GameObject(pygame.sprite.Sprite, PhysicsInterface):
	# Gameobjects use the same drawing method as pygame sprites.
	# This means that the image specified in self.sprite will be drawn at the location
	# specified by self.rect.  When animating, simply update the image reference
	# in time for the next draw.
	def __init__(self, body, verts):
		shape = pm.Poly(body, verts)
		PhysicsInterface.__init__(self, shape)
		
		self.shape.gameobject = self
		
		pygame.sprite.Sprite.__init__(self)
	
	def update(self):
		pass
		
	def draw(self, surface):
		surface.blit(self.image, Physics.to_pygame(self.body.position))
		#~ surface.blit(self.image, self.body.position)
		#~ surface.blit(self.image, self.rect)
	
	def delete(self):
		# Remove the gameobject from all groups which contain it, as well as the Pymunk space
		# TODO: Test this method.  Remove this comment when tested
		super(GameObject, self).remove_from_space()
		
		groups = super(GameObject, self).groups()
		super(GameObject, self).remove(groups)
