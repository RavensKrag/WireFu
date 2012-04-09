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
		shape = pm.Poly(body, verts)
		Physics.__init__(self, shape)
		
		self.shape.gameobject = self
		
		pygame.sprite.Sprite.__init__(self)
	
	def update(self):
		pass
		
	def draw(self, surface):
		surface.blit(self.image, Physics.to_pygame(self.body.position))
		#~ surface.blit(self.image, self.rect)

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
		
		for i in range(0, len(verts)):
			#~ print verts[i]
			verts[i] = Physics.to_pymunk(verts[i])
			#~ print "...{}".format(verts[i])
		
		super(NonstaticObject, self).__init__(body, verts)
	
	def update(self):
		self.image, self.rect = self._animation.update()
		
		#~ pos = Physics.to_pygame(self.body.position)
		#~ self.rect.left = pos[0]
		#~ self.rect.bottom = pos[1]
	
	def get_height(self):
		return self._animation.get_height()
		

class StaticObject(GameObject):
	def __init__(self, verts):
		super(StaticObject, self).__init__(pm.Body(), verts)
		
		# Compute the dimensions of a rectangle which will encompass the shape, so that
		# a Surface of the appropriate size can be generated. 
		left = right = top = bottom = None
		for v in verts:
			if left == None or v[0] < left:
				left = v[0]
			if right == None or v[0] > right:
				right = v[0]
			if top == None or v[1] > top:
				top = v[1]
			if bottom == None or v[1] < bottom:
				bottom = v[1]
		
		self.image = pygame.Surface([Physics.to_px(self.width), Physics.to_px(self.height)])
		
		# Draw polygon on image
		#~ color = pygame.Color("red")
		#~ self.image.fill(color)
		#~ pygame.draw.polygon(self.image, color, verts)
		
		self.rect = self.image.get_rect()
		#~ self.rect.left = self.body.position[0]
		#~ self.rect.bottom = self.body.position[1]
		
	def update(self):
		pass
	
	def add_to(self, space):
		space.add_static(self.shape)

	
