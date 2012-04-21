#!/usr/bin/python
# Import core libraries
import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d
import math, sys, random, os

# Change to the directory where this file resides
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


# Import files
import Physics
import collisions
from Level import Level

from utilities import EventProcessor
from user_interface import GameClock, KillScreen

from gameobjects.platforms import Exit, Platform, Ramp
from gameobjects.zipline import ZiplineHandle, ZiplineWire
from gameobjects.powerups import Powerup_Jump_Number

from gameobjects import Player

from utilities import Jukebox

class Window(object):
	def __init__(self, width, height):
		# Main gamestate initialization
		pygame.init()

		#background music plays endlessly
		self.jukebox = Jukebox()
		self.jukebox.play_bgm()
		
		self.width = width
		self.height = height
		self.dimentions = self.width, self.height
		
		self.screen = pygame.display.set_mode(self.dimentions)
		self.clock = pygame.time.Clock()
		self.framerate = 60
		
		# Initialize physics
		self.space = pm.Space(100)
		#~ self.space.damping = 0.12
		self.space.gravity = (0, -10*150)
		
		# Initialize other systems
		Physics.screen_height = self.height
		self.gameclock = GameClock(self.clock)
		
		self.player = Player()
		self.input_processor = EventProcessor(self, self.player)
		
		# Initialize game objects
		self.gameobjects = pygame.sprite.Group()
		
		self.loadLevel('level01.txt')
		# Initialize level background
		#self.background
		
#		self.platforms = pygame.sprite.Group(
#				Ground(), 
#				Exit([0.3*150,2.4*150], [1*150, 0.3*150], self.gameclock, self.input_processor),
#				Platform([1.0*150,1.0*150], [1*150, 0.3*150]),
#				Platform([1.0*150,2.0*150], [1*150, 0.3*150]),
#				Platform([1.0*150,3.0*150], [1*150, 0.3*150]),
#				Platform([3.8*150,2.7*150], [1*150, 0.3*150]),
#				Platform([3*150,1*150], [2*150, 0.3*150]),
#				Platform([1.3*150,0.5*150], [1*150, 0.3*150]),
#				Ramp([5*150,1*150], [5.5*150,2.5*150], width=10),
#				ZiplineWire([1.5*150,3.6*150], [3.8*150,3.9*150]),
#				Powerup_Jump_Number([6*150, 0*150], [0.3*150, 0.3*150])
#		)
		
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
		
	def loadLevel(self, levelFName):
		level = Level(self.screen, levelFName, self.gameclock, self.input_processor)
		self.platforms = level.platforms
		self.background = level.background
	
	def update(self):
		self.input_processor.update()
		self.space.step(1.0/self.framerate)
		self.gameclock.update()

		for p in self.platforms:
			p.update()

		self.player.update(self.width)
		
		collisions.PlayerZiplineCollision.post_collision_callback(self.space, self.player)
		
		pygame.display.set_caption("fps: " + str(self.clock.get_fps()))
	
	def draw(self):
		# Display Background
		self.screen.fill([0,0,0])
		self.screen.blit(self.background, (0, 0))	
		
		# Environment
		for p in self.platforms:
			p.draw(self.screen)
		
		# Player
		self.player.draw(self.screen)
		
		# Draw UI
		self.gameclock.draw(self.screen)
		
		# Draw killscreen if level over
		if((not self.gameclock.is_active()) and (self.gameclock.get_time() != (0,0,0))):
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
									collisions.PlayerEnvCollision, self.jukebox)
		
		self._add_collision_handler(collisions.PLAYER, collisions.ZIPLINE, 
									collisions.PlayerZiplineCollision, self.jukebox)
		
		self._add_collision_handler(collisions.PLAYER, collisions.GROUND,
									collisions.GroundCollision, self.jukebox)
		
		self._add_collision_handler(collisions.PLAYER, collisions.EXIT_ZONE,
									collisions.PlayerExitCollision, self.jukebox)

		self._add_collision_handler(collisions.PLAYER, collisions.POWERUP,
									collisions.PowerupCollision, self.jukebox)
		
	def _add_collision_handler(self, a, b, collision_class, jukebox):
		self.space.add_collision_handler(a, b, 
			collision_class.begin, collision_class.pre_solve, 
			collision_class.post_solve, collision_class.separate, jukebox)
	
Window(1020, 600).main()
