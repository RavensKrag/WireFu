import os, pygame
import pygame
import pymunk as pm
from pymunk import Vec2d

class Killscreen(object):
	def __init__(self, window, color=pygame.Color("red")):
		self.music = 'jazz_Goin_Up.wav'
		
		self.window = window
		
		self.font = pygame.font.SysFont("Dejavu Sans", 20)
		self.color = color
		self.time_score = None
		
		self.time_score = self._time_score()
	
	def update(self):
		pass
		# The killscreen should probably control the loading of the next level
		# Get an input to signal that the user is done looking at the score screen
		# Take the name of the next level to load from the "next" field of the previous level
		# Pop the stack twice (killscreen and old level)
		# Push the new level
	
	def draw(self, screen):
		time_score_image = self.font.render("time score: {}/5".format(self.time_score), True, self.color)
		screen.blit(time_score_image, (self.window.width/2, 0))
	
	def delete(self):
		pass
	
	def _time_score(self):
		# All scores should be out of five
		# Values present are hardcoded for the demo level.
		
		# Most significant time position first
		# To get the score, the time at the end of the level must be less that the time specified
		time_benchmarks = [
			(0,6,1000),		# 5 star maximum time
			(0,10,0),		# 4 star maximum time
			(0,15,500),		# 3 star maximum time
			(0,25,5000)	# 2 star maximum time
			# 1 star is any time greater than the 2 star time
		]
		
		time_score = 5
		time = self.window.gameclock.get_time()
		#~ print time
		for benchmark in time_benchmarks:
			#~ print time_score
			if time[0] <= benchmark[0] and time[1] <= benchmark[1] and time[2] <= benchmark[2]:
				break
			else:
				time_score -= 1
		
		return time_score
