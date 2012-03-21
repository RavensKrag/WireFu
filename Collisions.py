import pygame
#~ from gameobjects import Player
#~ from gameobjects import StaticObject
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

# Define collision handlers in this package
#~ LAYER_PLAYER = 0
#~ LAYER_PLATFORM = 1
PLAYER = 0
PLATFORM = 1
ZIPLINE = 2
GROUND = 3


class PlayerEnvCollision(object):
	def __init__(self):
		pass
	
	@staticmethod
	def begin(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter):
		#~ a, b = arbiter.shapes
		player_shape, env_shape = arbiter.shapes
		
		#~ print "collide"
		#~ if(isinstance(a, Player) and isinstance(b, StaticObject)):
			#~ print "proper"
		#~ player_shape = a
		#~ env_shape = b
		
		#~ if(player_shape.body.velocity.y < 0 and env_shape.point_query(player_shape.body.position)):
		if(player_shape.body.velocity.y < 0 and player_shape.body.position.y > env_shape.body.position.y):
			# If moving downwards from above
			player_shape.gameobject.ground_collision()
			
			#~ print "===contacts"
			#~ for p in arbiter.contacts:
				#~ print p
			
			
			#~ print arbiter.contacts[0].normal
			
			# Orient the player in the direction of the normal
			#~ normal = arbiter.contacts[0].normal
			#~ if(normal.y < 0):	# Insure y component is positive
				#~ normal.x *= -1
				#~ normal.y *= -1
			#~ angle = normal.get_angle()
			#~ if(angle < 0):
				#~ angle + math.pi
			#~ print "=="
			#~ print angle
			#~ player_shape.body.angle = angle
			#~ print player_shape.body.angle
			#~ player_shape.gameobject.rotate(player_shape.body.angle)
			
		
		return True
	
	@staticmethod
	def post_solve(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		return True
	
	@staticmethod
	def separate(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		arbiter.shapes[0].body.angle = 0
		
		return False

class PlayerZiplineCollision(object):
	joint_queue = []
	
	def __init__(self):
		pass
	
	@staticmethod
	def begin(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		print "yeaaaaaaaah"
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter):
		#~ a, b = arbiter.shapes
		player_shape, zipline_shape = arbiter.shapes
		
		arbiter.contacts[0].position
		
		joint = pm.GrooveJoint(zipline_shape.body, player_shape.body,
									(-zipline_shape.gameobject.width, -zipline_shape.gameobject.height), 
									(zipline_shape.gameobject.width, zipline_shape.gameobject.height),
									(0, 0.4))
		
		PlayerZiplineCollision.joint_queue.append(joint)
		
		return True
	
	@staticmethod
	def post_solve(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		return True
	
	@staticmethod
	def separate(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		#~ arbiter.shapes[0].body.angle = 0
		
		return False

class GroundCollision(object):
	def __init__(self):
		pass
	
	@staticmethod
	def begin(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter):
		a, b = arbiter.shapes
		#~ player_shape, env_shape = arbiter.shapes
		
		
		#~ if(player_shape.body.velocity.y < 0 and player_shape.body.position.y > env_shape.body.position.y):
			# If moving downwards from above
			#~ player_shape.gameobject.ground_collision()
		if(a.collision_type == PLAYER):
			#~ print "player a"
			a.gameobject.ground_collision()
		#~ elif(b.collision_type == PLAYER):
			#~ print "player b"
			#~ b.gameobject.ground_collision()
		
		return True
	
	@staticmethod
	def post_solve(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		return True
	
	@staticmethod
	def separate(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		return False
		
