import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

class Camera(object):
	offset_x = 0
	offset_y = 0
	
	dx = 5
	dy = 1
	
	def __init__(self, player):
		self.player = player
		
		self.bb_width = 200
		self.bb_height = 100
		
		self.screen_width = 1020
		self.screen_height = 600
		
		#~ self.offset_x = 0
		#~ self.offset_y = 0
	
	def update(self):
		if self.player.x > self.offset_x + (self.screen_width + self.bb_width)/2:
			#~ if self.player.x > self.bb_width:
				#~ pass
				#~ Camera.offset_x = 0 # Should be level width- self.offset_x
			#~ else:
				Camera.offset_x += Camera.dx
		elif self.player.x < self.offset_x + (self.screen_width - self.bb_width)/2:
			print "left side"
			if self.player.x < (self.screen_width - self.bb_width)/2:
				print "left border"
				Camera.offset_x = 0
			else:
				print "left standard"
				Camera.offset_x -= Camera.dx
		
		
		if self.player.y > self.offset_y + (self.screen_height + self.bb_height)/2:
			#~ if self.player.y > self.bb_height:
				#~ pass
				#~ Camera.offset_y = 0 # Should be level height- self.offset_y
			#~ else:
				Camera.offset_y += Camera.dy
		elif self.player.y < self.offset_y + (self.screen_height - self.bb_height)/2:
			print "bottom side"
			if self.player.y < (self.screen_height - self.bb_height)/2:
				print "bottom border"
				Camera.offset_y = 0
			else:
				print "bottom standard"
				Camera.offset_y -= Camera.dx
		
	def draw(self):
		pass
