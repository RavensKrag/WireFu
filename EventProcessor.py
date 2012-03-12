# Module for processing pygame events
import sys, pygame

class EventProcessor(object):
	def __init__(self, window, player):
		self.window = window
		self.player = player
		
		self.inputs = {} # Initialize new dictionary
		
		self.right_key = pygame.K_RIGHT
		self.left_key = pygame.K_LEFT
		self.jump_key = pygame.K_SPACE
	
	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				# Get button press events
				if event.key == pygame.K_ESCAPE:
					self.window.running = False
				elif event.key == self.jump_key:
					self.player.jump()
					
				
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
