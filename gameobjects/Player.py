import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobjects import NonstaticObject
import Physics

class Player(NonstaticObject):
	def __init__(self):
		mass = 60
		moment = pm.inf
		
		super(Player, self).__init__(mass, moment, 28, 89)
		
		self.rect = self.image.get_rect()
		self.rect.topleft = [0,0]
		
		self.body.velocity_limit = 1100
		self.jump_velocity = 600
		
		self.body.position.x = 0
		self.body.position.y = 100

		self.handhold = None # Pointer to a joint used to hold the player somewhere
		
		self.jump_count = 0
		self.jump_limit = 1
		self.in_air = False
		
		self.movement_force = Vec2d(200*150, 0.0)
		self.air_movement_force = Vec2d(50*150, 0.0)
		
		self.shape.friction = 0.12
		
		# Normal vector of the surface the player is currently on
		self.normal = Vec2d(0.0, 1.0)
		
		self.alive = True
		
		self._animation.transition_to('walk_loop')
	
	def update(self, window_width):
		#~ super(Player, self).update()
		#~ print "=== Player ==="
		#~ print self.body.position
		#~ print "====="
		
		
		
		self.image, self.rect = (None, None)
		
		self.image, self.rect = self._animation.update(self.body.velocity)
		
		# Constrain movement of player to screen
		width = self._animation.get_width()
		height = self._animation.get_height()
		#~ print height
		#~ print self.body.force
		
		if(self.y + height < 0):
			self.alive = False
		
		#~ print self.alive
		self.body.reset_forces()
	
	def draw(self, screen):
		pos = Physics.to_pygame(self.body.position)
		#~ pos = self.body.position
		screen.blit(self.image, (pos[0]-self._animation.get_width()/2, 
								pos[1]-self._animation.get_height()))
	
	def add_to(self, space):
		super(Player, self).add_to(space)
	
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
			self._animation.transition_to('jump')
			
			self.in_air = True
			self.body.velocity.y = self.jump_velocity
			self.jump_count += 1
	
	def let_go(self, space):
		#~ print "let go"
		space.remove(self.handhold)
		self.handhold = None
	
	def ground_collision(self):
		#~ print "ground"
		
		
		if self.in_air:
			self.in_air = False
			self._animation.transition_to('stand')
		
		self.jump_count = 0
		
		
		self.body.velocity -= self.body.velocity.projection(self.normal)
		self.body.force -= self.body.force.projection(self.normal)
		#~ self.body.velocity.y = 0
		#~ self.body.reset_forces
	
	def is_in_air(self):
		return self.in_air
	
	#~ def rotate(self, angle):
		#~ image = self._animation.update()[0]
		#~ self.image = pygame.transform.rotate(image, angle)
	
	def get_width(self):
		return self._animation.get_width()
	
	def get_height(self):
		return self._animation.get_height()
		
