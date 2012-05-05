import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

class Camera(object):
	offset_x = 0
	offset_y = 0
	
	dx = 5
	dy = 3
	
	def __init__(self, window, level_width, level_height, player):
		self.window = window
		self.level_width = level_width
		self.level_height = level_height
		self.player = player
		
		self.bb_width = 200
		self.bb_height = 100
		
		#~ self.offset_x = 0
		#~ self.offset_y = 0
	
	def update(self):
		left_screen_edge = self.offset_x
		right_screen_edge = self.offset_x + self.window.width
		
		left_bb_edge = self.offset_x + self.window.width/2 - self.bb_width/2
		right_bb_edge = self.offset_x + self.window.width/2 + self.bb_width/2
		
		# Margin is the area between the bounding box and the screen edge
		margin_left = left_bb_edge - left_screen_edge
		margin_right = right_screen_edge - right_bb_edge
		
		left_level_edge = 0 + margin_left
		right_level_edge = self.level_width - margin_right
		
		if self.player.x < left_level_edge:
			# Left Edge
			#print "left"
			pass
			Camera.offset_x = 0
		elif self.player.x > right_level_edge:
			# Right Edge
			#print "right"
			pass
			Camera.offset_x = self.level_width - self.window.width
		elif self.player.x < left_bb_edge:
			# Scroll Left
			Camera.offset_x -= Camera.dx
		elif self.player.x > right_bb_edge:
			# Scroll Right
			Camera.offset_x += Camera.dx
		
		x_min = 0
		x_max = self.level_width - self.window.width
		if Camera.offset_x < x_min:
			Camera.offset_x = x_min
		elif Camera.offset_x > x_max:
			Camera.offset_x = x_max
		
		
		
		bottom_screen_edge = self.offset_y
		top_screen_edge = self.offset_y + self.window.height
		
		bottom_bb_edge = self.offset_y + self.window.height/2 - self.bb_height/2
		top_bb_edge = self.offset_y + self.window.height/2 + self.bb_height/2
		
		# Margin is the area between the bounding box and the screen edge
		margin_bottom = bottom_bb_edge - bottom_screen_edge
		margin_top = top_screen_edge - top_bb_edge
		
		bottom_level_edge = 0 + margin_bottom
		top_level_edge = self.level_height - margin_top
		
		if self.player.y < bottom_level_edge:
			# Left Edge
			#print "Bottom"
			#~ pass
			Camera.offset_y = 0
		elif self.player.y > top_level_edge:
			# Right Edge
			#print "Top"
			#~ pass
			Camera.offset_y = self.level_height - self.window.height
		elif self.player.y < bottom_bb_edge:
			# Scroll Left
			Camera.offset_y -= Camera.dy
		elif self.player.y > top_bb_edge:
			# Scroll Right
			Camera.offset_y += Camera.dy
		
		
		#~ Camera.offset_y = self.player.y
		
		#~ x_min = 0
		#~ x_max = self.level_width - self.window.width
		#~ if Camera.offset_x < x_min:
			#~ Camera.offset_x = x_min
		#~ elif Camera.offset_x > x_max:
			#~ Camera.offset_x = x_max
		
		
		
	def draw(self):
		pass
