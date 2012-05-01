import pygame
#~ from gameobjects import Player
#~ from gameobjects import StaticObject
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from utilities import ExitTimer

class PlayerEnvCollision(object):
	@staticmethod
	def begin(space, arbiter, jukebox):
		player_shape, env_shape = arbiter.shapes
		player_shape.gameobject.normal = arbiter.contacts[0].normal
		
		#~ if arbiter.contacts[0].normal.y > 0:
			#~ # If moving downwards from above
			#~ player_shape.gameobject.ground_collision()
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter, jukebox):
		#~ a, b = arbiter.shapes
		player_shape, env_shape = arbiter.shapes
		
		return True
	
	@staticmethod
	def post_solve(space, arbiter, jukebox):
		player_shape, env_shape = arbiter.shapes
		
		#~ if(player_shape.body.velocity.y < 0 and player_shape.body.position.y > env_shape.body.position.y):
		if arbiter.contacts[0].normal.y > 0:
			# If moving downwards from above
			player_shape.gameobject.ground_collision()
		
		return True
	
	@staticmethod
	def separate(space, arbiter, jukebox):
		#~ player_shape, env_shape = arbiter.shapes
		
		return True
