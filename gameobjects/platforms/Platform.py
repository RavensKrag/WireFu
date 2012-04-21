import pygame
import Physics
import collisions
from gameobjects import StaticObject

class Platform(StaticObject):
	def __init__(self, pos, dimensions, color=pygame.Color("red")):
		# Position: 	Bottom left of platform
		# Dimensions:	width, height
		
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
		
		super(Platform, self).__init__(verts)
		
		self.body.position.x = pos[0]
		self.body.position.y = pos[1]
		
		self.image.fill(color)
		
		self.shape.collision_type = collisions.PLATFORM
		self.shape.friction = 0.8
		
	def update(self):
		pass
	
	def draw(self, screen):
		#print('TESTING -- Entering Platform.draw()')
		pos = Physics.to_pygame(self.body.position)
		#~ screen.blit(self.image, (pos[0], pos[1]-Physics.to_px(self.height)))
		#~ pos = self.body.position
		screen.blit(self.image, (pos[0], pos[1]-self.height))
		
		# Debug outline
		#~ x_px = Physics.to_px(self.body.position.x)
		#~ y_px = Physics.to_px(self.body.position.y)
		#~ width_px = Physics.to_px(self.width)
		#~ height_px = Physics.to_px(self.height)
		
		#~ color = pygame.Color("green")
		#~ 
		#~ verts =	[(x_px, Physics.screen_height-y_px) ,
				#~ (x_px+width_px, Physics.screen_height-y_px),
				#~ (x_px+width_px, Physics.screen_height-y_px-height_px),
				#~ (x_px, Physics.screen_height-y_px-height_px)]
		#~ 
		#~ pygame.draw.polygon(screen, color, verts, 2)
			
