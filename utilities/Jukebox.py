import pygame
import os
pygame.mixer.init()
 
 
class Jukebox:
	def __init__(self):
		self.name = "Jukebox"
		
		self.music_on = True
		self.sound_on = True
		
		#default bgm
		#self.bgm = self.load_sound('elec_Spin.wav')
		self.bgm = self.load_sound('elec_Run_The_Blockade.wav')
		#default powerup_sound
		self.powerup_sound = self.load_sound('beep-01.wav')
		#default
		self.victory = self.load_sound('victory.wav')
	
	def ToggleMusic(self):
		if self.music_on == False:
			self.music_on = True
			self.bgm.play()
		else:
			self.music_on = False
			self.bgm.stop()
	
	def ToggleSound(self):
		if self.sound_on == False:
			self.sound_on = True
			self.powerup_sound.play()
		else:
			self.sound_on = False
			self.powerup_sound.stop()

        #set audio manually
	def set_bgm(self, name):
		self.bgm = self.load_sound(name)

	def set_powerup(self, name):
		self.powerup_sound = self.load_sound(name)

	def set_victory(self, name):
                self.victory = self.load_sound(name)
	
	def load_sound(self, name):
		class NoneSound:
			def play(self): pass
		
		if not pygame.mixer or not pygame.mixer.get_init():
			return NoneSound()
		
		fullname = os.path.join('data', name)
		try:
			sound = pygame.mixer.Sound(fullname)
		except pygame.error, message:
			print 'Cannot load sound:', name
			raise SystemExit, message
		return sound

	#play or stop audio manually
	def play_bgm(self):
                if self.music_on:
                        self.bgm.play(-1)
		
	def stop_bgm(self):
		self.bgm.stop()
	
	def play_powerup(self):
                if self.sound_on:
                        self.powerup_sound.play()

	def stop_powerup(self):
		self.powerup_sound.stop()

	def play_victory(self):
                if self.sound_on:
                        self.victory.play()

	def stop_victory(self):
		self.victory.stop()

	def set_volume(self, vol):
		#vol is between 0.1 - 1.0
		self.bgm.set_volume(vol)

	def get_volume(self):
		return self.bgm.get_volume()

	def lower_volume(self):
		vol = self.bgm.get_volume() - 0.01
		self.bgm.set_volume(vol)

	def higher_volume(self):
		vol = self.bgm.get_volume() + 0.01
		self.bgm.set_volume(vol)
                
	
