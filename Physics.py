import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d

screen_height = 600  # This will need to be set by the Level being used
scale = 50*3	# Number of pixels per meter

def to_pygame(vec):
	# Convert from pymunk coordinates to pygame coordinates
	# TODO: Change this so that the screen scrolls.
	#		If additional values are needed, store them as variables in the package
	#		rather than requesting them as function parameters.
	print('TESTING -- Inside to_pygame')
	print('TESTING -- vec', vec)
	return vec.x, screen_height-vec.y

def to_pymunk(point):
	# Only implement if necessary
	return Vec2d(to_meters(point[0]), to_meters(point[1]))
