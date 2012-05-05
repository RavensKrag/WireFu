import pygame
#~ from gameobjects import Player
#~ from gameobjects import StaticObject
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from collisions.PlayerZiplineCollision import PlayerZiplineCollision

class PowerZiplineCollision(object): # Inheritance not working as expected
	new_handhold = None # new constraint to bind player to zipline
	
	@staticmethod
	def begin(space, arbiter, jukebox):
		#~ player_shape, env_shape = arbiter.shapes
		
		print "yeaaaaaaaah"
		
		arbiter.contacts[0].position
		
		player_shape, zipline_shape = arbiter.shapes
		
		a = zipline_shape.body.world_to_local(zipline_shape.a)
		b = zipline_shape.body.world_to_local(zipline_shape.b)
		
		PlayerZiplineCollision.new_handhold = pm.GrooveJoint(zipline_shape.body, player_shape.body,
									a, b, (0, 100))
		
		player_shape.gameobject.zipline_collision()
		
		print("collide!!!")
		player_shape, zipline_shape = arbiter.shapes
		
		player = player_shape.gameobject
		
		zipline = zipline_shape.gameobject
		velocity = zipline.wire_velocity
		
		
		player.body.velocity = velocity * 20000
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter, jukebox):
		#~ a, b = arbiter.shapes
		
		return True
	
	@staticmethod
	def post_solve(space, arbiter, jukebox):
		#~ player_shape, env_shape = arbiter.shapes
		
		return True
	
	@staticmethod
	def separate(space, arbiter, jukebox):
		#~ player_shape, env_shape = arbiter.shapes
		
		#~ arbiter.shapes[0].body.angle = 0
		
		return False
	
	@staticmethod
	def post_collision_callback(space, player):
		# Assumption: Player must let go of current zipline before grabbing a new one
		if(player.handhold == None and PlayerZiplineCollision.new_handhold):
			space.add(PlayerZiplineCollision.new_handhold)
			player.handhold = PlayerZiplineCollision.new_handhold
			
			PlayerZiplineCollision.new_handhold = None
