import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobject import NonstaticObject

class Player(NonstaticObject):
	def __init__(self):
		mass = 60
		moment = 1
		
		super(Player, self).__init__(mass, moment, verts=[])
		
		#~ self.image = pygame.Surface([30,50])
		color = pygame.Color("blue")
		self.image.fill(color)
		
		self.rect = self.image.get_rect()
		self.rect.topleft = [0,0]
		
		self.body.velocity_limit = 8
		
		self.body.position.x = 0
		self.body.position.y = 0
	
	def draw(self, screen):
		pos = self.to_pygame(self.body.position)
		screen.blit(self.image, (pos[0], pos[1]-self._animation.get_height()))
	
	def update(self):
		super(Player, self).update()
		if(self.body.position.y < 0):
			self._ground_collision()
			
		print self.body.position
		#~ print self.to_pygame(self.body.position)
		#~ print self.rect
		
	
	def move_up(self):
		pass
	
	def move_down(self):
		pass
	
	def move_left(self):
		self.body.apply_force((-100, 0.0))
	
	def move_right(self):
		self.body.apply_force((100, 0.0))
	
	def jump(self):
		self.body.velocity.y += 5
	
	def _ground_collision(self):
		#~ print "ground"
		self.body.position.y = 0
		self.body.velocity.y = 0
		self.body.reset_forces
		
		
