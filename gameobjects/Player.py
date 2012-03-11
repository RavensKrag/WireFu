import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobject import NonstaticObject

class Player(NonstaticObject):
	def __init__(self):
		mass = 1
		moment = 1
		
		super(Player, self).__init__(mass, moment, verts=[])
		
		#~ self.image = pygame.Surface([30,50])
		color = pygame.Color("red")
		self.image.fill(color)
		
		self.rect = self.image.get_rect()
		self.rect.topleft = [0,0]
	
	def update(self):
		super(Player, self).update()
