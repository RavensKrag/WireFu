import pygame
#~ from gameobjects import Player
#~ from gameobjects import StaticObject
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from utilities import ExitTimer

class PowerupCollision(object):
	old_powerups_queue = []	# Contains consumed powerups waiting to be removed
	
	@staticmethod
	def begin(space, arbiter):
		player_shape, env_shape = arbiter.shapes
		
		player = player_shape.gameobject
		powerup = env_shape.gameobject
		
		powerup.apply_effect(player)
		
		PowerupCollision.old_powerups_queue.append(powerup)
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter):
		#~ a, b = arbiter.shapes
		player_shape, env_shape = arbiter.shapes
		
		return False
	
	@staticmethod
	def post_solve(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		return False
	
	@staticmethod
	def separate(space, arbiter):
		#~ player_shape, env_shape = arbiter.shapes
		
		arbiter.shapes[0].body.angle = 0
		
		return False
