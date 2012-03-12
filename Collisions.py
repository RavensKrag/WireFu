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
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		if(player.body.velocity.y < 0):
			# If moving downwards
			player.ground_collision()
		
		return True
	
	@staticmethod
	def post_solve(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		return False
	
	@staticmethod
	def separate(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		return False
		
