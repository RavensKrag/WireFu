import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d

screen_height = None
scale = 50*3# Number of pixels per meter

def to_px(meters):
	return int(meters*scale)

def to_meters(px):
	return float(px)/scale

def to_pygame(vec):
	# Convert from pymunk coordinates to pygame coordinates
	return to_px(vec.x), screen_height-to_px(vec.y)

def to_pymunk(point):
	# Only implement if necessary
	return Vec2d(to_meters(point[0]), to_meters(point[1]))
