import pymunk as pm
from pymunk import Vec2d

import pygame
import Physics
import collisions
from gameobjects import StaticObject

class Ramp(StaticObject):
	def __init__(self, p1, p2, width=2):
		# CCW winding
		self.width = 5
		self.height = 5
		verts = [(p1[0] + width/2, p1[1]),
				(p1[0] - width/2, p1[1]),
				(p2[0] - width/2, p2[1]),
				(p2[0] + width/2, p2[1])]
		super(Ramp, self).__init__(verts)
		
		# Sort points by x
		if p2[0] < p1[0]:
			swap = p1
			p2 = p2
			p2 = swap
		
		# Calculate dimensions of bounding box around the slant image
		self.width = p2[0] - p1[0]
		y_offset = 0
		if p1[1] > p2[1]:
			self.height = p1[1] - p2[1]
			y_offset = p2[1]
		else:
			self.height = p2[1] - p1[1]
			y_offset = p1[1]
		x_offset = p1[0]
		
		self.width += width
		self.p1 = p1
		self.p2 = p2
		
		
		
		self.shape = pm.Segment(pm.Body(), Vec2d(p1[0], p1[1]), Vec2d(p2[0], p2[1]), width)
		self.shape.gameobject = self
		
		self.color = pygame.Color("red")
		
		#~ p1[0] -= x_offset
		#~ p1[1] -= y_offset
		#~ 
		#~ p2[0] -= x_offset
		#~ p2[1] -= y_offset
		
		#~ pygame.draw.line(self.image, color, p1, p2, width) # SOMETHING LIKE THAT
		
		
		self.shape.collision_type = collisions.PLATFORM
		
	def update(self):
		pass
	
	def draw(self, screen):
		#~ pos = Physics.to_pygame(self.body.position)
		#~ screen.blit(self.image, (pos[0], pos[1]-self.height)) # Draw at bottom left
		
		self.v1 = Physics.to_pygame(Vec2d(self.p1[0], self.p1[1]))
		self.v2 = Physics.to_pygame(Vec2d(self.p2[0], self.p2[1]))
		pygame.draw.line(screen, self.color, self.v1, self.v2, 20)
