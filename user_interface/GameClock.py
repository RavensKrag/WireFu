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
		
		self.font = pygame.font.SysFont("Dejavu Sans", 12)
		self.color = color
	
	def update(self):
		self.milliseconds += self.clock.get_time()
		if self.milliseconds > 1000:
			self.milliseconds %= 1000
			self.seconds += 1
		if self.seconds > 60:
			self.seconds %= 60
			self.minutes += 1
	
	def draw(self, screen):
		#~ time_display = None
		
		#~ if self.minutes > 0:
			#~ time_display = self.font.render("time: {}".format(self.time), False, self.color)
		#~ elif self.seconds > 0:
			#~ time_display = self.font.render("time: {}".format(self.time), False, self.color)
		#~ else # Only milliseconds
			#~ time_display = self.font.render("time: {}".format(self.time), False, self.color)
		
		timestamp = "time: {}:{}:{}".format(self.minutes, self.seconds, self.milliseconds)
		time_display = self.font.render(timestamp, False, self.color)
		
		time_display.get_rect().topleft = (0, 0)
		
		screen.blit(time_display, time_display.get_rect())
	
