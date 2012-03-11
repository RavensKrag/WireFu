from gameobject import StaticObject

class Platform(StaticObject):
	def __init__(self):
		# Counterclockwise winding
		# Start from bottom left
		# Pos x: right		Pos y: up
		verts = [(-1,-1), (1,-1), (1,1), (-1,1)]
		
		super(Platform, self).__init__(verts)
	
	def update(self):
		pass
