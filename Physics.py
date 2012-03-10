class Physics(object):
	screen_height = None
	
	def to_px(meters):
		return int(meters)
	
	def to_meters(px):
		return int(p.x)
		
	def to_pygame(vec):
		# Convert from pymunk coordinates to pygame coordinates
		return to_px(vec.x), self.screen_height-to_px(vec.y)
	
	def to_pymunk(x, y):
		# Only implement if necessary
		pass
