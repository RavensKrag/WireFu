import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from EventProcessor import EventProcessor
from GameObject import GameObject

pygame.init()

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

events = EventProcessor()

def update():
	events.update()
	
def draw():
	pass

while 1:
	update()
	draw()
	pygame.display.flip()
	clock.tick(50)
