import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobject import NonstaticObject
from Physics import Physics

class Player(NonstaticObject):
	def __init__(self):
		mass = 60
		moment = pm.inf
		
		super(Player, self).__init__(mass, moment, verts=[])
		
		#~ self.image = pygame.Surface([30,50])
		color = pygame.Color("blue")
		self.image.fill(color)
		
		self.rect = self.image.get_rect()
		self.rect.topleft = [0,0]
		
		self.body.velocity_limit = 8
		
		self.body.position.x = 0
		self.body.position.y = 1
		
		self.handhold = None # Pointer to a joint used to hold the player somewhere
		
		self.jump_count = 0
		self.jump_limit = 1
		self.in_air = False
		
		self.movement_force = Vec2d(200, 0.0)
		self.air_movement_force = Vec2d(50, 0.0)
		
		self.shape.friction = 0.12
	
	def draw(self, screen):
		pos = Physics.to_pygame(self.body.position)
		screen.blit(self.image, (pos[0]-self._animation.get_width()/2, 
								pos[1]-self._animation.get_height()))
	
	def update(self, window_width):
		#~ super(Player, self).update()
		image, rect = self._animation.update()
		self.image = pygame.transform.rotate(image, self.body.angle/math.pi*180)
		#~ print "{:03.5f}".format(self.body.angle/math.pi*180)
		
		#~ if(self.body.position.y < 0):
			#~ self.ground_collision()
			#~ self.body.position.y = 0
			
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
	
	def add_to(self, space):
		super(Player, self).add_to(space)
		#~ space.add(self.feet, self.feet.body, self.pin_joint)
		
	
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
			self.body.velocity.y = 4
			self.jump_count += 1
	
	def let_go(self, space):
		#~ print "let go"
		space.remove(self.handhold)
		self.handhold = None
	
	def ground_collision(self):
		#~ print "ground"
		self.in_air = False
		
		self.jump_count = 0
		
		#~ self.body.velocity.y = 0
		#~ self.body.reset_forces
	
	def is_in_air(self):
		return self.in_air
	
	def rotate(self, angle):
		image = self._animation.update()[0]
		self.image = pygame.transform.rotate(image, angle)
		
	
