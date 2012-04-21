import pygame
#~ from gameobjects import Player
#~ from gameobjects import StaticObject
import pymunk as pm
from pymunk import Vec2d
import math, sys, random

from utilities import ExitTimer

class PlayerExitCollision(object):
	timer = ExitTimer(500)
	
	@staticmethod
	def begin(space, arbiter, jukebox):
		player_shape, env_shape = arbiter.shapes
		
		# When the collision occurs, start the level exit timer.
		# When this timer finishes, then complete the level.
		
		if(player_shape.body.velocity.y < 0 and player_shape.body.position.y > env_shape.body.position.y):
			player_shape.gameobject.ground_collision()
			
			print "exiting zone..."
		
		return True
	
	@staticmethod
	def pre_solve(space, arbiter, jukebox):
		player_shape, env_shape = arbiter.shapes
		
		PlayerExitCollision.timer.update(20) # 50 FPS
		#~ timer.update(16) # 60 FPS
		
		if PlayerExitCollision.timer.can_exit():
			PlayerExitCollision.timer.kill()
			
			env_shape.gameobject.gameclock.stop()
			env_shape.gameobject.input_handler.deactivate_input()
			print "level complete"

			jukebox.stop_bgm()
			jukebox.play_victory()
			
		return True
	
	@staticmethod
	def post_solve(space, arbiter, jukebox):
		#~ player_shape, env_shape = arbiter.shapes
		
		return True
	
	@staticmethod
	def separate(space, arbiter, jukebox):
		#~ player_shape, env_shape = arbiter.shapes
		print "Exit interrupted"
		
		PlayerExitCollision.timer.reset()
		
		return False
