#!/usr/bin/python

# Import core libraries
import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

# Import files
import Physics
import collisions

from utilities import EventProcessor
from user_interface import GameClock
from user_interface import KillScreen

from gameobjects.platforms import Ground
from gameobjects.platforms import Exit
from gameobjects.platforms import Platform
from gameobjects.platforms import Ramp

from gameobjects.zipline import ZiplineHandle
from gameobjects.zipline import ZiplineWire

from gameobjects.powerups import Powerup_Jump_Number

from gameobjects import Player

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
		#~ self.space.damping = 0.12
		self.space.gravity = (0, -9.8)
		
		# Initialize other systems
		Physics.screen_height = self.height
		self.gameclock = GameClock(self.clock)
		
		self.player = Player()
		self.input_processor = EventProcessor(self, self.player)
		
		# Initialize game objects
		self.gameobjects = pygame.sprite.Group()
		
		self.platforms = pygame.sprite.Group(
				Ground(), 
				Exit([0.3,2.4], [1, 0.1], self.gameclock, self.input_processor),
				Platform([3.8,2.7], [1, 0.1]),
				Platform([3,1], [2, 0.1]),
				Platform([1.3,0.5], [1, 0.1]),
				Ramp([5,1], [5.5,2.5], width=5),
				ZiplineWire([1.5,3.6], [3.8,3.9]),
				Powerup_Jump_Number([6, 0], [0.3, 0.3])
		)
		
		# Add objects to space
		self.player.add_to(self.space)
		for p in self.platforms:
			p.add_to(self.space)
		
		# Assign collision handlers
		self._init_collision_handlers()
		
		# Set running to True so main game loop will execute
		self.running = True
		
		#~ # Create killscreen
		self.killscreen = KillScreen(self)
	
	def update(self):
		self.input_processor.update()
		self.space.step(1.0/self.framerate)
		self.gameclock.update()

		for p in self.platforms:
			p.update()

		self.player.update(self.width)
		
		pygame.display.set_caption("fps: " + str(self.clock.get_fps()))
		
		for joint in collisions.PlayerZiplineCollision.joint_queue:
			if(self.player.handhold == None):
				self.space.add(joint)
				self.player.handhold = joint
		
		joints = collisions.PlayerZiplineCollision.joint_queue
		while(len(joints) > 0): joints.pop()
	
	def draw(self):
		# Background
		self.screen.fill([0,0,0])
		
		# Environment
		for p in self.platforms:
			p.draw(self.screen)
		
		# Player
		self.player.draw(self.screen)
		
		# Draw UI
		self.gameclock.draw(self.screen)
		
		# Draw killscreen if level over
		if not self.gameclock.is_active():
			self.killscreen.update()
			self.killscreen.draw(self.screen)
	
	def main(self):
		while self.running:
			self.update()
			self.draw()
			pygame.display.flip()
			self.clock.tick(self.framerate)
	
	def _init_collision_handlers(self):
		self._add_collision_handler(collisions.PLAYER, collisions.PLATFORM, 
									collisions.PlayerEnvCollision)
		
		self._add_collision_handler(collisions.PLAYER, collisions.ZIPLINE, 
									collisions.PlayerZiplineCollision)
		
		self._add_collision_handler(collisions.PLAYER, collisions.GROUND,
									collisions.GroundCollision)
		
		self._add_collision_handler(collisions.PLAYER, collisions.EXIT_ZONE,
									collisions.PlayerExitCollision)

		self._add_collision_handler(collisions.PLAYER, collisions.POWERUP,
									collisions.PowerupCollision)
		
	def _add_collision_handler(self, a, b, collision_class):
		self.space.add_collision_handler(a, b, 
			collision_class.begin, collision_class.pre_solve, 
			collision_class.post_solve, collision_class.separate)
	
Window(1020, 600).main()
