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
import Physics
from Animation import *


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
		
		# Initialize game objects
		self.gameobjects = pygame.sprite.Group()
		self.player = Player()
		self.platforms = [Platform([0,0], [100, 10]),
					Platform([0,0], [100, 10]),
					Platform([0,0], [100, 10])]
		
		# Add objects to space
		self.player.add_to(self.space)
		#~ for p in platforms:
			#~ p.add_to(space)
		
		# Initialize systems
		Physics.screen_height = height
		self.input_processor = EventProcessor(self, self.player)
	
	def update(self):
		self.space.step(self.framerate)
		self.input_processor.update()
		
	def draw(self):
		self.player.draw(self.screen)
		for p in self.platforms:
			p.draw(self.screen)
	
	def main(self):
		while 1:
			self.update()
			self.draw()
			pygame.display.flip()
			self.clock.tick(self.framerate)
	
Window(600,600).main()
