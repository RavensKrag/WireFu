import pygame

import Physics
from gameobjects import StaticObject
from gameobjects.powerups import Powerup
import collisions

class Powerup_Jump_Number(Powerup):
	def __init__(self, pos, dimensions, color=pygame.Color("green")):
		super(Powerup_Jump_Number, self).__init__(pos, dimensions, color)
		
		#~ self.untouched = True
		
	def update(self):
		pass
	
	def apply_effect(self, player):
		#~ if(self.untouched == True):
		player.jump_limit = player.jump_limit + 1
		print 'jump limit: ' , player.jump_limit
		
		color = pygame.Color("red")
		self.image.fill(color)
		#elif(self.type == 1):
		#		player.shape.friction = player.shape.friction - 0.02
		#2 = longer jumps
		#elif(self.type == 2):
		#		player.jump_velocity = player.jump_velocity + 10
