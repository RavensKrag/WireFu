import pygame, os

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
            
class OptionsScreen(object):
	def __init__(self, screen, jukebox):
		self.music = 'elec_Follow_Me.wav'

		self.font = pygame.font.Font(None, 32)

		pos_x = screen.get_width()/2
		pos_y = screen.get_width()/5

		self.background, self.backRect = self._load_image('bg1.jpg')
		self.music_on = self.font.render("Music Enabled", 1, WHITE)
		self.music_rect = self.music_on.get_rect(centerx = pos_x, centery = pos_y)
		self.music_level_pos_x = pos_x + 100
		self.music_level_pos_y = pos_y
		pos_y = pos_y + 40
		
		self.sound = self.sound = self.font.render("Sound Enabled", 1, WHITE)
		self.sound_rect = self.sound.get_rect(centerx=pos_x, centery=pos_y)

		self.jukebox = jukebox
		
	def update(self):
		pass
	
	def draw(self, screen):

                if self.jukebox.music_on:
                        self.music_on = self.font.render("Music Enabled", 1, WHITE)
                else:
                        self.music_on = self.font.render("Music Disabled", 1, RED)

                if self.jukebox.sound_on:
                        self.sound = self.font.render("Sound Enabled", 1, WHITE)
                else:
                        self.sound = self.font.render("Sound Disabled", 1, RED)

                text = self.font.render("PRESS SPACE BAR TO GO BACK....", 1, RED)
                textpos = text.get_rect(centerx = 500, centery = 500) 
		screen.blit(self.background, self.backRect)
		screen.blit(self.music_on, self.music_rect)
		screen.blit(self.sound, self.sound_rect)
		screen.blit(text, textpos)
		#volume level
		pygame.draw.line(screen, WHITE, (self.music_level_pos_x, self.music_level_pos_y),(self.music_level_pos_x+100, self.music_level_pos_y))
                pygame.draw.rect(screen, RED, (self.music_level_pos_x+(self.jukebox.get_volume()*100), self.music_level_pos_y, 10, 10))
		pygame.display.flip()
	
	def delete(self):
		pass
	
	def _load_image(self, name, colorkey=None):
		fullname = os.path.join('data', name)
		try:
			image = pygame.image.load(fullname)
		except pygame.error, message:
			print 'Cannot load image:', fullname
			raise SystemExit, message
		image = image.convert()
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, RLEACCEL) # accelerate 
		return image, image.get_rect()
