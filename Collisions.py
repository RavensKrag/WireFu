# Define collision handlers in this package
#~ LAYER_PLAYER = 0
#~ LAYER_PLATFORM = 1
PLAYER = 0
PLATFORM = 1

class PlayerEnvCollision(object):
	def __init__(self):
		pass
	
	@staticmethod
	def begin(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		print "test"
		
		return False
	
	@staticmethod
	def pre_solve(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		return False
	
	@staticmethod
	def post_solve(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		return False
	
	@staticmethod
	def separate(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		return False
		
