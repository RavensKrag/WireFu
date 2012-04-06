# Message displayed at the end of a level
import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

class KillScreen(object):
	def __init__(self, window, color=pygame.Color("white")):
		self.window = window
		
		self.font = pygame.font.SysFont("Dejavu Sans", 20)
		self.color = color
	
	def update(self):
		pass
	
	def draw(self, screen):
		# All scores should be out of five
		# Values present are hardcoded for the demo level.
		
		time_score = None
		time = self.window.gameclock.get_time()
		if time[0] < 1000 and time[1] < 6 and time[2] == 0:
			time_score = 5
		elif time[0] < 1000 and time[1] < 9 and time[2] == 0:
			time_score = 4
		elif time[0] < 500 and time[1] < 12 and time[2] == 0:
			time_score = 3
		elif time[0] < 500 and time[1] < 20 and time[2] == 0:
			time_score = 2
		else:
			time_score = 1
		
		
		time_score_image = self.font.render("time score: {}/5".format(time_score), True, self.color)
		screen.blit(time_score_image, (self.window.width/2, 0))
	
