#!/usr/bin/python

# Import core libraries
import pygame
#~ from pygame.locals import *
#~ from pygame.color import *
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

# Import files
from EventProcessor import EventProcessor
from gameobjects import *
import Physics
from Animation import *

# Main gamestate initialization
pygame.init()

width, height = dimentions = (600,600)

screen = pygame.display.set_mode(dimentions)
clock = pygame.time.Clock()

# Initialize systems
Physics.screen_height = height
input_processor = EventProcessor()

# Initialize game objects
gameobjects = pygame.sprite.Group()
player = Player()
platforms = [Platform(),
			Platform(),
			Platform()]

def update():
	input_processor.update()
	
def draw():
	player.draw(screen)

while 1:
	update()
	draw()
	pygame.display.flip()
	clock.tick(50)
