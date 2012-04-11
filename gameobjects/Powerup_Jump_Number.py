import pygame
from Physics import Physics
from gameobject import StaticObject
import Collisions

class Powerup_Jump_Number(StaticObject):
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
		
		super(Powerup_Jump_Number, self).__init__(verts)
		
		self.body.position.x = pos[0]
		self.body.position.y = pos[1]
		
		self.image.fill(color)
		
		self.shape.collision_type = Collisions.POWERUP_JUMP_NUMBER
		self.shape.friction = 0.2
		
		self.untouched = True
		
	def update(self):
                pass
	
	def draw(self, screen):
                pos = Physics.to_pygame(self.body.position)
                screen.blit(self.image, (pos[0], pos[1]-Physics.to_px(self.height)))

	def apply_effect(self, player):
		if(self.untouched == True):
				player.jump_limit = player.jump_limit + 1
		#elif(self.type == 1):
		#		player.shape.friction = player.shape.friction - 0.02
		#2 = longer jumps
		#elif(self.type == 2):
		#		player.jump_velocity = player.jump_velocity + 10

		
