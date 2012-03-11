import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from Physics import *
from Animation import *

class GameObject(pygame.sprite.Sprite, Physics):
	# Gameobjects use the same drawing method as pygame sprites.
	# This means that the image specified in self.sprite will be drawn at the location
	# specified by self.rect.  When animating, simply update the image reference
	# in time for the next draw.
	def __init__(self, body, verts):
		self.body = body
		self.shape = pm.Poly(body, verts)
	
	def update(self):
		pass
		
	def draw(self, surface):
		surface.blit(self.image, self.rect)

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
		
		super(NonstaticObject, self).__init__(body, verts)
		
		
		
	
	def update(self):
		self.image, self.rect = self._animation.update()

class StaticObject(GameObject):
	static_body = pm.Body()
	
	def __init__(self, verts):
		super(StaticObject, self).__init__(self.static_body, verts)
		
		self.image = pygame.Surface([1,1])
		self.rect = self.image.get_rect()
		
	def update(self):
		pass
