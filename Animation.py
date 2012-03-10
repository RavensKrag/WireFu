import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

class Animation(object):
	def __init__(self):
		self.image = pygame.Surface([1,1])
		self.rect = self.image.get_rect()
	
	def update(self):
		pass
	
	def draw(self, surface):
		pass
	
	def get_frame():
		# Return the next frame of the animation.
		return self.image
