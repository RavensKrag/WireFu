# Clock displayed as part of the game HUD which counts up as the
# game progresses.  Allows the player to keep track of how fast
# they are running through the level.

import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

class GameClock(object):
	def __init__(self, clock, color=pygame.Color("green")):
		self.clock = clock	# Reference to a pygame.time.Clock object
		
		# Time elapsed since the start of the level
		self.milliseconds = 0
		self.seconds = 0
		self.minutes = 0
		
		# Things to draw the clock with
		self.font = pygame.font.SysFont("Dejavu Sans", 20)
		self.color = color
		
		self.active = False
	
	def update(self):
		if self.active:
			self.milliseconds += self.clock.get_time()
			if self.milliseconds > 1000:
				self.milliseconds %= 1000
				self.seconds += 1
			if self.seconds > 60:
				self.seconds %= 60
				self.minutes += 1
	
	def draw(self, screen):
		timestamp = "time: {}:{}:{}".format(self.minutes, self.seconds, self.milliseconds)
		time_display = self.font.render(timestamp, False, self.color)
		time_display.get_rect().topleft = (0, 0)
		
		screen.blit(time_display, time_display.get_rect())
	
	def stop(self):
		self.active = False
		self.color = pygame.Color("red")
	
	def start(self, color=pygame.Color("green")):
		if self.active == False:
			self.active = True
			self.color = color
	
	def reset(self, color=pygame.Color("green")):
		self.milliseconds = 0
		self.seconds = 0
		self.minutes = 0
		
		self.active = True
		
		self.color = color
	
	def get_time(self):
		# Return time as a tuple, big-endian style
		return (self.minutes, self.seconds, self.milliseconds)
	
	def is_active(self):
		return self.active
	
