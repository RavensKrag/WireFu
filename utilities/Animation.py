import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random, os

class Animation(object):
	def __init__(self):
		#~ self._image = pygame.Surface([30,50])
		name = 'player.png'
		fullname = os.path.join('sprites', name)
		self._image = pygame.image.load(fullname)
		self._rect = self._image.get_rect()
	
	def update(self):
		# Set the image to the next frame, and update the rect as well
		return self._image, self._rect
	
	def draw(self, surface):
		pass
	
	def get_width(self):
		return self._rect.width
	
	def get_height(self):
		return self._rect.height
	
