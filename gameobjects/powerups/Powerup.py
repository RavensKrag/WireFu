import pygame

import Physics
from gameobjects import StaticObject
import collisions

class Powerup(StaticObject):
	def __init__(self, pos, dimensions, color=pygame.Color("green")):
		self.width = dimensions[0]
		self.height = dimensions[1]
		
		# Counterclockwise winding
		# Start from bottom left
		# Pos x: right		Pos y: up
		half_width = self.width/2.0
		half_height = self.height/2.0
		
		#~ verts = [(-half_width, -half_height),
				#~ (half_width, -half_height),
				#~ (half_width, half_height),
				#~ (-half_width, half_height)]
		
		verts = [(0,0),
				(self.width, 0),
				(self.width, self.height),
				(0, self.height)]
		
		super(Powerup, self).__init__(verts)
		
		self.body.position.x = pos[0]
		self.body.position.y = pos[1]
		
		self.image.fill(color)
		
		self.shape.collision_type = collisions.POWERUP
		self.shape.friction = 0.8

		self.visible = True
		
	def update(self):
                pass
	
	def draw(self, screen):
		if(self.visible == True):
			#~ super(Powerup, self).draw(screen)
			pos = Physics.to_pygame(self.body.position)
			screen.blit(self.image, (pos[0], pos[1]-self.height))
	
	def getPowerup_Type(self):
		print self.type
	def setPowerup_Type(self, p_type):
		self.type = p_type
	
	def apply_effect(self, player):
		#0 = num of jumps + 1
		if(self.type == 0):
				player.jump_limit = player.jump_limit + 1
		elif(self.type == 1):
				player.shape.friction = player.shape.friction - 0.02
		#2 = longer jumps
		elif(self.type == 2):
				player.jump_velocity = player.jump_velocity + 10

		
