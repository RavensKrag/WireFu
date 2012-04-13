import pygame
#~ from gameobjects import Player
#~ from gameobjects import StaticObject
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

import collisions
from utilities import ExitTimer

class GroundCollision(object):
	@staticmethod
	def begin(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		player_shape.gameobject.normal = arbiter.contacts[0].normal
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter):
		#~ a, b = arbiter.shapes
		player_shape, env_shape = arbiter.shapes
		
		print "==== Ground Collision ===="
		print player_shape.gameobject
		#~ for contact in arbiter.contacts:
			#~ print contact.normal
		print arbiter.contacts[0].normal
		print "=========="
		
		#~ if(player_shape.body.velocity.y < 0 and player_shape.body.position.y > env_shape.body.position.y):
			# If moving downwards from above
			#~ player_shape.gameobject.ground_collision()
		#~ if(player_shape.collision_type == collisions.PLAYER):
			#~ print "player a"
			
		#~ elif(b.collision_type == PLAYER):
			#~ print "player b"
			#~ b.gameobject.ground_collision()
		
		return True
	
	@staticmethod
	def post_solve(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		player_shape.gameobject.ground_collision()
		
		return True
	
	@staticmethod
	def separate(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		return False
