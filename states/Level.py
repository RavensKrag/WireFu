import os, pygame, re, sys
import pymunk as pm
from pymunk import Vec2d

# Import files
import Physics
import collisions

from Camera import Camera

from gameobjects import Player
from gameobjects.platforms import Exit, Platform, Ramp
from gameobjects.zipline import ZiplineHandle, ZiplineWire
from gameobjects.powerups import Powerup_Jump_Number

class Level(object):
	def __init__(self, window, space, filename, input_handler, game_clock):
		self.music = 'elec_Spin.wav'
		
		# Open level file
		self.window = window
		self.space = space
		self.name = filename
		self.input_handler = input_handler
		self.game_clock = game_clock
		
		self.game_clock.reset()
		
		# Load level background and the objects in the level
		# level_width, level_width, background, powerups, platforms
		self._load(self.name)
		
		self.player = Player()
		self.player.body.position.x = 0
		self.player.body.position.y = 100
		
		self.gameobjects = pygame.sprite.Group()
		
		# Add objects to space
		self.player.add_to(self.space)
		for p in self.platforms:
			p.add_to(self.space)
		for p in self.powerups:
			p.add_to(self.space)
		
		# Bind input
		input_handler.bind_player(self.player) # Remember to unbind on level end
		
		# Create camera
		self.camera = Camera(self.window, self.level_width, self.level_height, self.player)
	
	def update(self):
		self.camera.update()
		
		if not self.player.alive:
			self.reload()
		
		self.player.update(self.level_width)
		
		# Keep the player within the level
		self._constrain_to_level(self.player)
		
		for p in self.platforms:
			p.update()
		for p in self.powerups:
			p.update
		
		collisions.PlayerZiplineCollision.post_collision_callback(self.space, self.player)
		collisions.PowerupCollision.post_collision_callback()
		
	def draw(self, screen):
		# Display Background
		screen.fill([0,0,0])
		screen.blit(self.background, (0, 0))	
		
		# Environment
		for p in self.platforms:
			p.draw(screen)
		
		# Powerups
		for p in self.powerups:
			p.draw(screen)
		
		# Player
		self.player.draw(screen)
		
		# Draw UI
		self.game_clock.draw(screen)
	
	def delete(self):
		# Remove all objects contained in this level from the pymunk space, and mark for gc
		for p in self.platforms:
			p.delete()
		
		# Powerups
		for p in self.powerups:
			p.delete()
		
		self.player.delete()
	
	def reload(self):
		# Pop current state off the stack and replace with an identical one
		old_state = self.window.pop_state()
		
		state = Level(self.window, old_state.space, old_state.name, old_state.input_handler, old_state.game_clock)
		
		self.window.push_state(state)
	
	def _constrain_to_level(self, gameobject):
		# Keep the gameobject within the confines of the level
		if(gameobject.x - gameobject.get_width()/2) < 0:
			# Player went off the left side
			gameobject.x = gameobject.get_width()/2
			gameobject.body.force.x = 0
			gameobject.body.velocity.x = 0

		elif(gameobject.x + gameobject.get_width()/2 > self.level_width):
			# Player went off the right side
			gameobject.x = self.level_width - gameobject.get_width()/2
			gameobject.body.force.x = 0
			gameobject.body.velocity.x = 0
	
	def _load(self, filename):
		level_file = self._openFile(filename)
		
		# Read load the background image
		line = level_file.readline().rstrip('\n')
		fullname = os.path.join('levels', line)
		self.background = pygame.image.load(fullname).convert()
		
		# Set level size from file
		line = level_file.readline()
		matches = self._findPatterns(r'\d+', line)
		self.level_width = int(matches[0])
		self.level_height = int(matches[1])
		#~ self.screen = pygame.display.set_mode((self.level_width,self.level_height))
		
		
		# Load platforms, ramps, ziplines, and powerups
		self.platforms = pygame.sprite.Group()
		self.powerups = pygame.sprite.Group()
		
		line = level_file.readline()
		section = 0
		while line != '':
			if(line[0] == '#' or line[0] == '\n'):
				if line[0] == '#': section += 1
				line = level_file.readline()
			elif(section == 1):		# Load platforms
				matches = self._findPatterns(r'\d+.\d+', line)
				pos = [float(matches[0]),float(matches[1])]
				dimensions = [float(matches[2]),float(matches[3])]
				platform = Platform(pos,dimensions)
				self.platforms.add(platform)
				line = level_file.readline()
			elif(section == 2): 	# Load ramps
				matches = self._findPatterns(r'\d+.\d+', line)
				endPoint1 = [float(matches[0]),float(matches[1])]
				endPoint2 = [float(matches[2]),float(matches[3])]
				rampWidth = int(float(matches[4]))
				platform = Ramp(endPoint1,endPoint2,rampWidth)
				self.platforms.add(platform)
				line = level_file.readline()
			elif(section == 3):		# Load ziplines
				matches = self._findPatterns(r'\d+.\d+', line)
				endPoint1 = [float(matches[0]),float(matches[1])]
				endPoint2 = [float(matches[2]),float(matches[3])]
				platform = ZiplineWire(endPoint1,endPoint2)
				self.platforms.add(platform)			
				line = level_file.readline()
			elif(section == 4): 	# Load Exit platform
				matches = self._findPatterns(r'\d+.\d+', line)
				pos = [float(matches[0]),float(matches[1])]
				dimensions = [float(matches[2]),float(matches[3])]
				platform = Exit(pos,dimensions,self.game_clock,self.input_handler)
				self.platforms.add(platform)				
				line = level_file.readline()
			elif(section == 5):		# Load Jump powerups
				matches = self._findPatterns(r'\d+.\d+', line)
				pos = [float(matches[0]),float(matches[1])]
				dimensions = [float(matches[2]),float(matches[3])]
				platform = Powerup_Jump_Number(pos,dimensions)
				self.powerups.add(platform)
				line = level_file.readline()
			else:
				print('Format error in ' + filename + '. Program terminated.')
				sys.exit()
	
	# Regular expression is used to find pattern within text
	def _findPatterns(self, pat, text):
		match = re.findall(pat, text)
		if match:
			match
			return match
		else:
			print(pat + ' not found')
	
	def _openFile(self, filename):
		fullname = os.path.join('levels', filename)
		try:
			file = open(fullname, 'rU')
		except pygame.error, message:
			print 'Cannot load file:', fullname
			raise SystemExit, message
		return file	
