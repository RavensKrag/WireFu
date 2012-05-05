import pygame
#~ from gameobjects import Player
#~ from gameobjects import StaticObject
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from collisions.PlayerZiplineCollision import PlayerZiplineCollision

class PowerZiplineCollision(PlayerZiplineCollision):
	@staticmethod
	def begin(space, arbiter, jukebox):
		super(PowerZiplineCollision).begin(space, arbiter, jukebox)
		
		player_shape, zipline_shape = arbiter.shapes
		
		player = player_shape.gameobject
		
		zipline = zipline_shape.gameobject
		force = zipline.wire_force
		
		
		player.body.wire_force.apply_force(force * 200)
		
		return True
	
	#~ @staticmethod
	#~ def pre_solve(space, arbiter, jukebox):
		#~ 
		#~ 
		#~ return True
	#~ 
	#~ @staticmethod
	#~ def post_solve(space, arbiter, jukebox):
		#~ 
		#~ 
		#~ return True
	#~ 
	#~ @staticmethod
	#~ def separate(space, arbiter, jukebox):
		#~ 
		#~ 
		#~ return False
	#~ 
	#~ @staticmethod
	#~ def post_collision_callback(space, player):
		#~ # Assumption: Player must let go of current zipline before grabbing a new one
		#~ if(player.handhold == None and PlayerZiplineCollision.new_handhold):
			#~ space.add(PlayerZiplineCollision.new_handhold)
			#~ player.handhold = PlayerZiplineCollision.new_handhold
			#~ 
			#~ PlayerZiplineCollision.new_handhold = None
