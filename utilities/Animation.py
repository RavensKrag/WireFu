import pygame
import pymunk as pm
from pymunk import Vec2d
import math, sys, random, os

class Animation(object):
	def __init__(self):
		#~ self._image = pygame.Surface([30,50])
		name = 'player.png'
		fullname = os.path.join('sprites', name)
		self._image = pygame.image.load(fullname)
		self._rect = self._image.get_rect()
		
		
		# Animation sequence
		# 	Stand
		# 	Walk start
		# 	Walk loop
		# 	Walk to run
		# 	Run
		# 	Slide
		# 	Slide to stand
		# 	--> back to top
		self.animations = {
			'stand' : self._load('player_stand.png', (80, 110)), # SET
			
			'walk_start' : self._load('player_walkStart.png', (80, 110)), # SET
			'walk_loop' : self._load('player_walkLoop.png', (80, 110)), # SET
			'walk_to_run' : self._load('player_walkToRun.png', (80, 110)), # SET
			
			'run' : self._load('player_run.png', (100, 110)), # SET
			
			'slide' : self._load('player_slide.png', (100, 110)), # SET
			'slide_to_stand' : self._load('player_slideToStand.png', (100, 110)), # SET
			
			'jump' : self._load('player_jump.png', (80, 110)), # 1-24 jump, 25-27 hit ground
			
			'wire_kick' : self._load('player_wireKick.png', (100, 110)) # SET
		}
		
		self.state = None
		self.next_state = 'stand'
		self._frame_count = 0
		
		self.direction = 'right'
		
		self.tick = 0
		
	
	def update(self, velocity=None):
		# Set the image to the next frame, and update the rect as well
		if self.next_state != self.state:
			self._transition_to_new_state()
		else:
			#~ print "update"
			#~ self._frame_count += 1
			
			vx = 0
			
			if velocity:
				vx = velocity.x
			
			if vx < 0:
				vx *= -1
				self.direction = 'left'
			else:
				self.direction = 'right'
				
			self.tick += 1
			
			if self.state == 'walk_loop':
				if vx > 100:
					#~ print "high speed walking!!"
					if self.tick >= 2:
						self.tick = 0
						self._frame_count += 1
				elif vx > 0:
					#~ print "Low speed"
					if self.tick >= 4:
						self.tick = 0
						self._frame_count += 1
				else:
					self.tick = 0
					self._frame_count = 0
			elif self.state == 'jump':
				if self.tick >= 2:
					self.tick = 0
					self._frame_count += 1
			
			
			
			if self.state == 'jump':
				if self._frame_count >= self.animations[self.state][2]:
					self._frame_count = self.animations[self.state][2]-1
			elif self._frame_count >= self.animations[self.state][2]:
				self._frame_count = 0
			
			# Prep current frame
			current_frame_rect = self.frame_rects[self._frame_count]
			self.current_frame.fill((0,0,0,0)) # ARGB
			self.current_frame.blit(self.spritesheet, (0,0), current_frame_rect)
			
			if self.direction == 'left':
				self.current_frame = pygame.transform.flip(self.current_frame, True, False)
			else:
				pass
		
		return self.current_frame, self.current_frame.get_rect()
	
	def draw(self, surface):
		pass
	
	def transition_to(self, state):
		self.next_state = state
	
	def get_width(self):
		return self.current_frame.get_rect().width
	
	def get_height(self):
		return self.current_frame.get_rect().height
	
	def _load(self, name, frame_size):
		fullname = os.path.join('sprites', name)
		image = pygame.image.load(fullname)
		
		image.convert_alpha()
		
		frame_rects = []
		
		frame_count = 0
		x = 0
		y = 0
		#~ print "width: {}   height: {}".format(image.get_width(), image.get_height())
		#~ print "frame size: {}x{}".format(frame_size[0], frame_size[1])
		while y < image.get_height():
			x = 0
			while x < image.get_width():
				frame_count += 1
				#~ print "new frame {}".format(name)
				# Cut out sprite
				frame_rects.append(pygame.Rect((x, y), frame_size))
				
				x += frame_size[0]
			y += frame_size[1]
		
		return image, frame_rects, frame_count
	
	def _transition_to_new_state(self):
		self.state = self.next_state
		print "new state: {}".format(self.state)
		self._frame_count = 0
		
		# Transition to spritesheet for new state
		self.spritesheet = self.animations[self.state][0]
		self.frame_rects = self.animations[self.state][1]
		
		# Create new frame surface
		current_frame_rect = self.frame_rects[self._frame_count]
		
		self.current_frame = pygame.Surface((current_frame_rect[2], current_frame_rect[3]),
											pygame.SRCALPHA)
		
		self.current_frame.blit(self.spritesheet, (0,0), current_frame_rect)
	
	
