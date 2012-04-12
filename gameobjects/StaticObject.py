import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

import Physics
from gameobjects import GameObject

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
