import pygame
#~ from gameobjects import Player
#~ from gameobjects import StaticObject
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from utilities import ExitTimer

class PlayerZiplineCollision(object):
	joint_queue = []
	
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
