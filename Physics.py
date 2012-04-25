import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d

from Camera import Camera

screen_height = 600  # This will need to be set by the Level being used

def to_pygame(vec):
	# Convert from pymunk coordinates to pygame coordinates
	# TODO: Change this so that the screen scrolls.
	#		If additional values are needed, store them as variables in the package
	#		rather than requesting them as function parameters.
	#print('TESTING -- Inside to_pygame')
	#print('TESTING -- vec', vec)
	#~ print "{}, {}".format(Camera.offset_x, Camera.offset_y)
	
	return vec.x-Camera.offset_x, screen_height-vec.y+Camera.offset_y

def x_to_pygame(x):
	return x-Camera.offset_x
	
def y_to_pygame(y):
	return screen_height-y+Camera.offset_y
