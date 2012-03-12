#!/usr/bin/python

# Import core libraries
import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

# Import files
from EventProcessor import EventProcessor
from gameobjects import *
from Physics import Physics
from Animation import *
import Collisions


class Window(object):
	def __init__(self, width, height):
		# Main gamestate initialization
		pygame.init()
		
		self.width = width
		self.height = height
		self.dimentions = self.width, self.height
		
		self.screen = pygame.display.set_mode(self.dimentions)
		self.clock = pygame.time.Clock()
		self.framerate = 50
		
		self.space = pm.Space()
		#~ self.space._set_damping(0.12)
		self.space.damping = 0.12
		#~ print self.space._get_damping()
		#~ self.space.damping = 0.8
		#~ self.space._set_gravity = (0, -9.8)
		self.space.gravity = (0, -9.8)
		#~ self.space._set_gravity((0.0, -15.0))
		#~ print self.space._get_gravity()
		
		# Initialize game objects
		self.gameobjects = pygame.sprite.Group()
		self.player = Player()
		#~ self.platforms = [Platform([0,0], [100, 10]),
					#~ Platform([0,0], [100, 10]),
					#~ Platform([0,0], [100, 10])]
		
		# Add objects to space
		self.player.add_to(self.space)
		#~ self.space.add_static(self.platforms.shape)
		#~ for p in self.platforms:
			#~ self.space.add_static(p.shape)
			#~ p.add_to(self.space)
		
		# Initialize systems
		Physics.screen_height = self.height
		self.input_processor = EventProcessor(self, self.player)
		
		# Set running to True so main game loop will execute
		self.running = True
	
	def update(self):
		self.input_processor.update()
		self.space.step(1.0/self.framerate)
		self.player.update(self.width)
		
		pygame.display.set_caption("fps: " + str(self.clock.get_fps()))
	
	def draw(self):
		self.screen.fill([0,0,0])
		
		self.player.draw(self.screen)
		
		#~ for p in self.platforms:
			#~ p.draw(self.screen)
	
	def main(self):
		while self.running:
			self.update()
			self.draw()
			pygame.display.flip()
			self.clock.tick(self.framerate)
	
	def _init_collision_handlers(self):
		self.player.collision_type = Collisions.PLAYER
		for p in self.platforms:
			p.collision_type = Collisions.PLATFORM
		
		#~ self._add_collision_handler(Collisions.PLAYER, Collisions.PLATFORM, 
									#~ Collisions.PlayerEnvCollision)
		false_func = lambda space, arbiter : False
		self.space.add_collision_handler(Collisions.PLAYER, Collisions.PLATFORM, 
										false_func, false_func, false_func, false_func)
		
		
	def _add_collision_handler(self, a, b, collision_class):
		self.space.add_collision_handler(a, b, 
			collision_class.begin, collision_class.pre_solve, 
			collision_class.post_solve, collision_class.separate)
	
Window(1020, 600).main()
