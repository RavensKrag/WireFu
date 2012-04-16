import pygame
#~ from gameobjects import Player
#~ from gameobjects import StaticObject
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from utilities import ExitTimer

class PlayerEnvCollision(object):
	@staticmethod
	def begin(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		player_shape.gameobject.normal = arbiter.contacts[0].normal
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter):
		#~ a, b = arbiter.shapes
		player_shape, env_shape = arbiter.shapes
		
		#~ print "==== Collision ===="
		#~ print player_shape.gameobject
		#~ print arbiter.contacts[0].normal
		#~ print "=========="
		
		
		#~ print "collide"
		#~ if(isinstance(a, Player) and isinstance(b, StaticObject)):
			#~ print "proper"
		#~ player_shape = a
		#~ env_shape = b
		
		#~ if(player_shape.body.velocity.y < 0 and env_shape.point_query(player_shape.body.position)):
		
			
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
		player_shape, env_shape = arbiter.shapes
		
		#~ if(player_shape.body.velocity.y < 0 and player_shape.body.position.y > env_shape.body.position.y):
		if arbiter.contacts[0].normal.y > 0:
			# If moving downwards from above
			player_shape.gameobject.ground_collision()
		
		return True
	
	@staticmethod
	def separate(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		#~ arbiter.shapes[0].body.angle = 0
		
		return True
