from gameobject import StaticObject

class Platform(StaticObject):
	def __init__(self, pos, dimensions):
		# Counterclockwise winding
		# Start from bottom left
		# Pos x: right		Pos y: up
		half_width = dimensions[0]/2.0
		half_height = dimensions[1]/2.0
		
		verts = [(-half_width, -half_height),
				(half_width, -half_height),
				(half_width, half_height),
				(-half_width, half_height)]
		
		super(Platform, self).__init__(verts)
		
		self.body.position.x = pos[0]
		self.body.position.y = pos[1]
		
	def update(self):
		pass
