from gameobject import StaticObject

class Platform(StaticObject):
	def __init__(self, pos, dimensions):
		self.width = dimensions[0]
		self.height = dimensions[1]
		
		# Counterclockwise winding
		# Start from bottom left
		# Pos x: right		Pos y: up
		half_width = self.width/2.0
		half_height = self.height/2.0
		
		verts = [(-half_width, -half_height),
				(half_width, -half_height),
				(half_width, half_height),
				(-half_width, half_height)]
		
		super(Platform, self).__init__(verts)
		
		self.body.position.x = pos[0]
		self.body.position.y = pos[1]
		
	def update(self):
		pass
	
	def draw(self, screen):
		pos = self.to_pygame(self.body.position)
		screen.blit(self.image, (pos[0], pos[1]-self.height))
