import pygame
import sys

class EventProcessor(object):
	def __init__(self):
		pass
		
	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				# KeyDown events
				if event.key == pygame.K_ESCAPE:
					sys.exit()
