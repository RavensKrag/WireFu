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

from utilities import EventProcessor
from user_interface import GameClock, KillScreen

from gameobjects.platforms import Exit, Platform, Ramp
from gameobjects.zipline import ZiplineHandle, ZiplineWire
from gameobjects.powerups import Powerup_Jump_Number

from gameobjects import Player

from utilities import Jukebox

from states import Menu

class Window(object):
	def __init__(self, width, height):
		# Main gamestate initialization
		pygame.init()

		#background music plays endlessly
		self.jukebox = Jukebox()
		
		self.width = width
		self.height = height
		self.dimentions = self.width, self.height
		
		self.screen = pygame.display.set_mode(self.dimentions)
		self.clock = pygame.time.Clock()
		self.framerate = 60
		
		self.gameclock = GameClock(self.clock)
		self.input_processor = EventProcessor(self, self.jukebox)
		
		# Initialize physics
		self.space = pm.Space(100)
		#~ self.space.damping = 0.12
		self.space.gravity = (0, -10*150)
		
		# Set physics variables
		Physics.screen_height = self.height
		self._init_collision_handlers()
		
		# Create gamestate stack
		self.states = []
		
		# Set running to True so main game loop will execute
		self.running = True
		
		# Create killscreen
		self.killscreen = KillScreen(self)
		
	def loadLevel(self, levelFName):
		self.currentLevel = levelFName
		
		self.gameclock.reset()
		
		self.player.body.position.x = 0
		self.player.body.position.y = 100
		
		# TODO: Free old gameobjects from pymunk space
		level = Level(self.screen, levelFName, self.gameclock, self.input_processor)
		self.platforms = level.platforms
		self.background = level.background
		
		return level
	
	def update(self):
		self.input_processor.update()
		self.space.step(1.0/self.framerate)
		self.gameclock.update()
		
		self.states[-1].update()
		
		pygame.display.set_caption("fps: " + str(self.clock.get_fps()))
	
	def draw(self):
		#~ self.level.draw(self.screen)
		#~ for state in self.states:
			#~ state.draw(self.screen)
		self.states[-1].draw(self.screen)
		
	
	def main(self):
		self.push_state(Menu(self))
		
		while self.running:
			self.update()
			self.draw()
			pygame.display.flip()
			self.clock.tick(self.framerate)
	
	def push_state(self, state):
		self.jukebox.stop_bgm()
		
		self.states.append(state)
		
		self.jukebox.set_bgm(state.music)
		self.jukebox.play_bgm()
		
	def pop_state(self):
		self.jukebox.stop_bgm()
		self.states.pop()
		
		top_state = self.states[-1]
		if top_state:
			self.jukebox.set_bgm(top_state.music)
		self.jukebox.play_bgm()
		
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
	
Window(1020,600).main()
