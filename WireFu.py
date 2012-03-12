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
		
		# Initialize physics
		self.space = pm.Space()
		self.space.damping = 0.12
		self.space.gravity = (0, -9.8)
		
		# Initialize other systems
		Physics.screen_height = self.height
		
		# Initialize game objects
		self.gameobjects = pygame.sprite.Group()
		self.player = Player()
		self.platforms = pygame.sprite.Group(Platform([0,1], [1, 0.1]),
											Platform([3,2], [1, 0.1]),
											Platform([4,1], [1, 0.1]),
											Ramp([5,1], [5.2,2], width=5, skew=100))
		
		# Add objects to space
		self.player.add_to(self.space)
		for p in self.platforms:
			self.space.add_static(p.shape)
		
		# Assign collision handlers
		self._init_collision_handlers()
		
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
		
		for p in self.platforms:
			p.draw(self.screen)
			
		self.player.draw(self.screen)
	
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
		
		self._add_collision_handler(Collisions.PLAYER, Collisions.PLATFORM, 
									Collisions.PlayerEnvCollision)
		
	def _add_collision_handler(self, a, b, collision_class):
		self.space.add_collision_handler(a, b, 
			collision_class.begin, collision_class.pre_solve, 
			collision_class.post_solve, collision_class.separate)
	
Window(1020, 600).main()
