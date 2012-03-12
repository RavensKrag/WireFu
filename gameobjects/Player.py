import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobject import NonstaticObject
from Physics import Physics

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
		self.body.position.y = 1
		
		
		self.jump_count = 0
		self.jump_limit = 2
		self.in_air = False
		
		self.movement_force = Vec2d(250, 0.0)
		self.air_movement_force = Vec2d(120, 0.0)
	
	def draw(self, screen):
		pos = Physics.to_pygame(self.body.position)
		screen.blit(self.image, (pos[0]-self._animation.get_width()/2, 
								pos[1]-self._animation.get_height()))
	
	def update(self, window_width):
		super(Player, self).update()
		if(self.body.position.y < 0):
			self.ground_collision()
			self.body.position.y = 0
			
		#~ print self.body.position
		#~ print Physics.to_pygame(self.body.position)
		#~ print self.rect
		
		# Constrain movement of player to screen
		window_width = Physics.to_meters(window_width)
		width = Physics.to_meters(self._animation.get_width())
		#~ print self.body.force
		if(self.x < width/2):
			self.x = width/2
			self.body.force.x = 0
			self.body.velocity.x = 0
		elif(self.x + width/2 > window_width):
			self.x = window_width - width/2
			self.body.force.x = 0
			self.body.velocity.x = 0
		
		self.body.reset_forces()
	
	def move_left(self):
		if(self.in_air):
			self.body.apply_force(-self.air_movement_force)
		else:
			self.body.apply_force(-self.movement_force)
	
	def move_right(self):
		if(self.in_air):
			self.body.apply_force(self.air_movement_force)
		else:
			self.body.apply_force(self.movement_force)
	
	def jump(self):
		if self.jump_count < self.jump_limit:
			self.in_air = True
			self.body.velocity.y += 5	# Add instead of setting to take momentum into account
			self.jump_count += 1
	
	def ground_collision(self):
		#~ print "ground"
		self.in_air = False
		
		self.jump_count = 0
		
		self.body.velocity.y = 0
		self.body.reset_forces
	
	def is_in_air(self):
		return self.in_air
	
