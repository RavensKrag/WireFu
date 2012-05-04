# Define the exit portal for the level
# Essentially just a special platform that the player must stand on for
# a brief period.  Thus, unlike games like N or Sonic the Hedgehog, the
# player can not charge through the goal.  This is to create an element
# of skill to stopping appropriately at the end of a level, while still
# minimizing the time it takes to complete a course.
import pygame
import Physics
import collisions
from gameobjects.platforms import Platform

class Exit(Platform):
	def __init__(self, position, dimensions, gameclock):
		# Store a reference to the game clock, so that the exit can pause it
		self.gameclock = gameclock
		
		color = pygame.Color("yellow")
		super(Exit, self).__init__(position, dimensions, color)
		
		self.shape.collision_type = collisions.EXIT_ZONE
	
	#~ def update(self):
		#~ pass
	
	#~ def draw(self, screen):
		#~ pass
