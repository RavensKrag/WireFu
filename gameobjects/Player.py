import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from gameobjects import NonstaticObject
from Camera import Camera
import Physics

class Player(NonstaticObject):
	def __init__(self):
		mass = 60
		moment = pm.inf
		
		super(Player, self).__init__(mass, moment, verts=[])
		
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
		
		self.camera = Camera(self)
		
		self.alive = True
	
	def update(self, window_width):
		super(Player, self).update()
		#~ print "=== Player ==="
		#~ print self.body.position
		#~ print "====="
		self.camera.update()
		
		image, rect = self._animation.update()
			
		# Constrain movement of player to screen
		
		# Define bounding box for camera movement
		width = self._animation.get_width()
		height = self._animation.get_height()
		#~ print height
		#~ print self.body.force
		if(self.x < width/2):
			self.x = width/2
			self.body.force.x = 0
			self.body.velocity.x = 0
			Camera.offset_x = 0
		#~ elif(self.x + width/2 > window_width):
			#~ self.x = window_width - width/2
			#~ self.body.force.x = 0
			#~ self.body.velocity.x = 0
		
		if(self.y - height < 0):
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
			self.in_air = True
			self.body.velocity.y = self.jump_velocity
			self.jump_count += 1
	
	def let_go(self, space):
		#~ print "let go"
		space.remove(self.handhold)
		self.handhold = None
	
	def ground_collision(self):
		#~ print "ground"
		self.in_air = False
		
		self.jump_count = 0
		
		
		self.body.velocity -= self.body.velocity.projection(self.normal)
		self.body.force -= self.body.force.projection(self.normal)
		#~ self.body.velocity.y = 0
		#~ self.body.reset_forces
	
	def is_in_air(self):
		return self.in_air
	
	def rotate(self, angle):
		image = self._animation.update()[0]
		self.image = pygame.transform.rotate(image, angle)
