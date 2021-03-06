#!/usr/bin/python
# Import core libraries
import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d
import math, sys, random, os

# Change to the directory where this file resides
#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)


# Import files
import Physics
import collisions

from utilities import EventProcessor
from user_interface import GameClock
from Camera import Camera

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
	
	def main(self):
		self.push_state(Menu(self, self.jukebox))
		
		while self.running:
			self.update()
			self.draw()
			pygame.display.flip()
			self.clock.tick(self.framerate)
	
	def update(self):
		self.input_processor.update()
		self.gameclock.update()
		
		self.states[-1].update()
		
		pygame.display.set_caption("fps: " + str(self.clock.get_fps()))
	
	def draw(self):
		for state in self.states:
			state.draw(self.screen)
	
	def push_state(self, state):
		self.jukebox.stop_bgm()
		
		self.states.append(state)
		
		self.jukebox.set_bgm(state.music)
		self.jukebox.play_bgm()
		
	def pop_state(self):
		Camera.offset_x = 0
		Camera.offset_y = 0
		self.jukebox.stop_bgm()
		old_state = self.states.pop()
		old_state.delete()
		
		top_state = self.states[-1]
		if top_state:
			self.jukebox.set_bgm(top_state.music)
		self.jukebox.play_bgm()
		
		return old_state
		
	def _init_collision_handlers(self):
		self._add_collision_handler(collisions.PLAYER, collisions.PLATFORM, 
									collisions.PlayerEnvCollision, self.jukebox)
		
		self._add_collision_handler(collisions.PLAYER, collisions.ZIPLINE, 
									collisions.PlayerZiplineCollision, self.jukebox)
		
		self._add_collision_handler(collisions.PLAYER, collisions.POWER_ZIPLINE, 
									collisions.PowerZiplineCollision, self.jukebox)
		
		self._add_collision_handler(collisions.PLAYER, collisions.GROUND,
									collisions.GroundCollision, self.jukebox)
		
		self._add_collision_handler(collisions.PLAYER, collisions.EXIT_ZONE,
									collisions.PlayerExitCollision, self.jukebox)
		
		collision_class = collisions.PlayerExitCollision
		self.space.add_collision_handler(collisions.PLAYER, collisions.EXIT_ZONE, 
			collision_class.begin, collision_class.pre_solve, 
			collision_class.post_solve, collision_class.separate, self, self.jukebox)
		
		self._add_collision_handler(collisions.PLAYER, collisions.POWERUP,
									collisions.PowerupCollision, self.jukebox)
		
	def _add_collision_handler(self, a, b, collision_class, jukebox):
		self.space.add_collision_handler(a, b, 
			collision_class.begin, collision_class.pre_solve, 
			collision_class.post_solve, collision_class.separate, jukebox)
	
Window(1020,600).main()
