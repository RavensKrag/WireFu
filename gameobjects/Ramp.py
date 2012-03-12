import pygame
from Physics import Physics
from gameobject import StaticObject

import pymunk as pm
from pymunk import Vec2d

class Ramp(StaticObject):
	def __init__(self, p1, p2, width=2, skew=50):
		self.line_width = Physics.to_meters(width)
		self.skew = Physics.to_meters(skew)
		
		# Sort by y
		if(p1[1] > p2[1]):
			swap = p2
			p2 = p1
			p1 = swap
		
		self.height = p2[1] - p1[1]
		
		# Sort by x
		if(p1[0] > p2[0]):
			swap = p2
			p2 = p1
			p1 = swap
		
		self.width = p2[0] - p1[0]
		
		# Counterclockwise winding
		# Start from bottom left
		# Pos x: right		Pos y: up
		half_width = self.width/2.0
		half_height = self.height/2.0
		
		
		verts = [(0,0),
				(self.line_width, 0),
				(self.skew+self.line_width, self.height),
				(self.skew, self.height)]
			
		
		self.width += self.line_width + self.skew
		super(Ramp, self).__init__(verts)
		
		self.body.position.x = p1[0]
		self.body.position.y = p1[1]
		
		line_width = Physics.to_px(self.line_width)
		skew = Physics.to_px(self.skew)
		points = [(0, self.image.get_height()),
				(0 + line_width, self.image.get_height()),
				(0 + skew + line_width, 0),
				(0 + skew, 0)]
		
		#~ color = pygame.Color("white")
		#~ self.image.fill(color)
		color = pygame.Color("red")
		pygame.draw.polygon(self.image, color, points)
		
		# TODO: Trim image size
		
		self.p1 = p1
		self.p2 = p2
		
	def update(self):
		pass
	
	def draw(self, screen):
		pos = Physics.to_pygame(self.body.position)
		screen.blit(self.image, (pos[0], pos[1]-Physics.to_px(self.height)))
		
		# Debug outline
		#~ x_px = Physics.to_px(self.body.position.x)
		#~ y_px = Physics.screen_height - Physics.to_px(self.body.position.y)
		#~ width_px = Physics.to_px(self.width)
		#~ height_px = Physics.to_px(self.height)
		#~ 
		#~ line_width = Physics.to_px(self.line_width)
		#~ skew = Physics.to_px(self.skew)
		#~ 
		#~ color = pygame.Color("green")
		#~ 
		#~ height = self.p2[1]-self.p1[1]
		#~ 
		#~ verts = [(x_px, y_px),
				#~ (x_px + line_width, y_px),
				#~ (x_px + skew + line_width, y_px - height_px),
				#~ (x_px + skew, y_px - height_px)]
		#~ 
		#~ pygame.draw.circle(screen, color, (x_px, y_px), 3)
		
		#~ print "==="
		#~ for v in verts:
			#~ print v
		#~ 
		#~ pygame.draw.polygon(screen, color, verts, 2)
			

