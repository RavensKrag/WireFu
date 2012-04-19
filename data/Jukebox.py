import pygame
import os
pygame.mixer.init()
 
 
class Jukebox:
	def __init__(self):
		self.name = "Jukebox"
		
		self.music_on = True
		self.sound_on = True
		
		self.currentlvl = 0
		
		self.bgm = []
		self.bgm.append(self.load_sound('elec_Spin.wav')) #for level 1
		self.bgm.append(self.load_sound('elec_Run_The_Blockade.wav')) #for level 2
		#self.bgm = self.load_sound('elec_Follow_Me.wav')
		
		self.powerup_sound = self.load_sound('beep-01.wav')
	
	def ToggleMusic(self,on=True):
		self.music_on = on
		if self.music_on == False:
			self.powerup_sound.stop()
		else:
			self.powerup_sound.play()
	
	def ToggleSound(self,on=True):
		self.sound_on = on
		if self.sound_on == False:
			self.bgm[0].stop()
		else:
			self.bgm[0].play()
	
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
	
	def play_bgm(self):
		self.bgm[0].play(-1)
	
	def play_powerup(self):
		self.powerup_sound.play()
	
