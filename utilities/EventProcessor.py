# Module for processing pygame events
import sys, pygame
from pygame.locals import *

from states import Menu, Killscreen, CreditsScreen, OptionsScreen
from states import Level, PauseScreen

class EventProcessor(object):
	def __init__(self, window, jukebox):
		self.window = window
		
		self.inputs = {} # Initialize new dictionary
		
		self.right_key = pygame.K_RIGHT
		self.left_key = pygame.K_LEFT
		self.jump_key = pygame.K_SPACE

		self.jukebox = jukebox
		
		self.restart_key = pygame.K_r
		
		self.volume_up_key = pygame.K_1
		self.volume_down_key = pygame.K_2
		
		self.pause_key = pygame.K_p
		
		self.active = True;
	
	def update(self):
		if self.active:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					# Get general button press events
					if event.key == pygame.K_ESCAPE:
						self.window.running = False
					else:	# Get button hold keydowns
						self.inputs[event.key] = True
					
					if isinstance(self.window.states[-1], Menu):
						if event.key == pygame.K_UP:
							self.window.states[-1].cursor_up()
						elif event.key == pygame.K_DOWN:
							self.window.states[-1].cursor_down()
						elif event.key == pygame.K_RETURN:
							self.window.states[-1].select()
					#~ elif self.window.state == 'options':
						#~ pass
					elif isinstance(self.window.states[-1], Killscreen):
						# When killscreen is reached, unbind the player
						self.unbind_player()
						if event.key == pygame.K_SPACE:
							self.window.states[-1].next_level()
					elif isinstance(self.window.states[-1], CreditsScreen):
						if event.key == pygame.K_SPACE:
							#go back to the menu screen when space is pressed
							self.window.pop_state()
					elif isinstance(self.window.states[-1], OptionsScreen):
						if event.key == pygame.K_SPACE:
							#go back to the menu screen when space is pressed
							self.window.pop_state()						
					elif isinstance(self.window.states[-1], Level):
						if event.key == self.right_key or event.key == self.left_key or event.key == self.jump_key:
							self.window.gameclock.start()
						
						if event.key == self.pause_key:
							self.window.gameclock.stop()
							self.window.push_state(PauseScreen(self.window))
						elif event.key == self.jump_key:
							if(self.player.handhold != None):
								self.player.let_go(self.window.space)
							else:
								self.player.jump()
						elif event.key == self.restart_key:
							# Restart level
							self.window.states[-1].reload()
					elif isinstance(self.window.states[-1], PauseScreen):
						if event.key == self.pause_key:
							self.window.pop_state()
							#~ self.window.gameclock.start()


				elif event.type == pygame.KEYUP:
					self.inputs[event.key] = False
				elif event.type == pygame.QUIT:
					self.window.running = False
					
				# ===== Process mouse events
				elif event.type == MOUSEBUTTONDOWN:
					if isinstance(self.window.states[-1], OptionsScreen):
						if pygame.mouse.get_pressed()[0] == 1:
							if self.window.states[-1].music_rect.collidepoint(pygame.mouse.get_pos()):
								self.jukebox.toggle_Music()
							elif self.window.states[-1].sound_rect.collidepoint(pygame.mouse.get_pos()):
								self.jukebox.toggle_Sound()
				
			# ===== Process held buttons
			# State specific hold events
			if isinstance(self.window.states[-1], Menu):
				pass
			#~ elif self.window.state == 'options':
				#~ pass
			elif isinstance(self.window.states[-1], Killscreen):
				pass
			elif isinstance(self.window.states[-1], CreditsScreen):
				pass
			elif isinstance(self.window.states[-1], Level):
				if self.inputs.get(self.right_key, False):
					self.player.move_right()
				if self.inputs.get(self.left_key, False):
					self.player.move_left()
			#~ elif self.window.state == 'pause':
				#~ pass
			
			# Universal button hold events
			if self.inputs.get(self.volume_up_key, False):
				self.jukebox.higher_volume()
			if self.inputs.get(self.volume_down_key, False):
				self.jukebox.lower_volume()
		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				self.window.running = False
			elif event.type == pygame.QUIT:
				self.window.running = False
	
	def bind_player(self, player):
		self.player = player
	
	def unbind_player(self):
		self.player = None
