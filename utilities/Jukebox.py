import pygame
import os
pygame.mixer.init()
 
 
class Jukebox:
	def __init__(self):
		self.name = "Jukebox"
		
		self.music_on = True
		self.sound_on = True
		
		self.volume = 0.5
		
		#default bgm
		#self.bgm = self.load_sound('elec_Spin.wav')
		self.bgm = self.load_sound('elec_Run_The_Blockade.wav')
		#default powerup_sound
		self.powerup_sound = self.load_sound('beep-01.wav')
		#default
		self.victory = self.load_sound('victory.wav')
	
	def toggle_Music(self):
		if self.music_on == False:
			self.music_on = True
			self.bgm.play()
		else:
			self.music_on = False
			self.bgm.stop()
	
	def toggle_Sound(self):
		if self.sound_on == False:
			self.sound_on = True
			self.powerup_sound.play()
		else:
			self.sound_on = False
			self.powerup_sound.stop()

        #set audio manually
	def set_bgm(self, name):
		self.bgm = self.load_sound(name)
		self.bgm.set_volume(self.volume)

	def set_powerup(self, name):
		self.powerup_sound = self.load_sound(name)
		self.powerup_sound.set_volume(self.volume)

	def set_victory(self, name):
		self.victory = self.load_sound(name)
		self.victory.set_volume(self.volume)
	
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

	def get_volume(self):
		return self.volume

	def lower_volume(self):
		self.set_volume(self.volume - 0.002)
		
	def higher_volume(self):
		self.set_volume(self.volume + 0.002)
	
	def set_volume(self, vol):
		self.volume = vol
		
		self.bgm.set_volume(vol)
		self.powerup_sound.set_volume(vol)
		self.victory.set_volume(vol)
                
	
