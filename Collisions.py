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
		
		if(player_shape.body.velocity.y < 0 and env_shape.point_query(player_shape.body.position)):
			# If moving downwards from above
			player_shape.gameobject.ground_collision()
			
		
		return True
	
	@staticmethod
	def post_solve(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		return True
	
	@staticmethod
	def separate(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		return False
		
