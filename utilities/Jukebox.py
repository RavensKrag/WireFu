import pygame
import os
pygame.mixer.init()
 
 
class Jukebox:
	def __init__(self):
		self.name = "Jukebox"
		
		self.music_on = True
		self.sound_on = True
		
		#default bgm
		self.bgm = self.load_sound('elec_Spin.wav')
		#default powerup_sound
		self.powerup_sound = self.load_sound('beep-01.wav')
	
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
		self.bgm.play(-1)
	
	def play_powerup(self):
		self.powerup_sound.play()

	def stop_bgm(self):
                self.bgm.stop()

        def stop_powerup(self):
                self.powerup_sound.stop()
	
