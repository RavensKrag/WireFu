# Module for processing pygame events
import sys, pygame

class EventProcessor(object):
	def __init__(self, window, player, jukebox):
		self.window = window
		self.player = player
		
		self.inputs = {} # Initialize new dictionary
		
		self.right_key = pygame.K_RIGHT
		self.left_key = pygame.K_LEFT
		self.jump_key = pygame.K_SPACE

		self.jukebox = jukebox
		
		self.restart_key = pygame.K_r
		
		self.active = True;
	
	def update(self):
		if self.active:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					self.window.gameclock.start()
					
					# Get button press events
					if event.key == pygame.K_ESCAPE:
						self.window.running = False
					elif event.key == self.jump_key:
						if(self.player.handhold != None):
							self.player.let_go(self.window.space)
						else:
							self.player.jump()
					elif event.key == self.restart_key:
						# Restart level
						self.window.loadLevel(self.window.currentLevel)
					elif event.key == pygame.K_1:
						self.jukebox.lower_volume()
					elif event.key == pygame.K_2:
						self.jukebox.higher_volume()
					else:	# Get button hold keydowns
						self.inputs[event.key] = True
				elif event.type == pygame.KEYUP:
					self.inputs[event.key] = False
				elif event.type == pygame.QUIT:
					self.window.running = False
				#~ elif event.type == pygame.MOUSEBUTTONDOWN:
					#~ if event.button == 1: # Left Click
						#~ pos = (event.pos[0]-self.window.offset_x, event.pos[1])
	
			
			# Process held buttons
			if self.inputs.get(self.right_key, False):
				#~ pass
				self.player.move_right()
			if self.inputs.get(self.left_key, False):
				#~ pass
				self.player.move_left()
		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.window.running = False
			elif event.type == pygame.QUIT:
				self.window.running = False
	
	def deactivate_input(self):
		self.active = False
