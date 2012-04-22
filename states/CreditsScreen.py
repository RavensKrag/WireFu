import pygame, os

WHITE = (255, 255, 255)
RED = (255, 0, 0)

class CreditsScreen(object):
	def __init__(self, screen):
		self.background, self.backRect = self._load_image('bg1.jpg')
		
		self.text_surface, self.text_surface_rect = self.render_credits_text(screen)
		
	def update(self):
		self.text_surface.scroll(0, -1)
	
	def draw(self, screen):
		screen.blit(self.background, self.backRect)
		screen.blit(self.text_surface, self.text_surface_rect)
	
	def render_credits_text(self, screen, font_size=32):
		pos_x = screen.get_width()/2
		pos_y = screen.get_width()/2
		
		text_surface = pygame.Surface((1020, 2000), pygame.SRCALPHA, 32)
		text_surface = text_surface.convert_alpha()
		text_surface_rect = text_surface.get_rect()
		
		font = pygame.font.Font(None, font_size)
		
		text = font.render("PRESS SPACE BAR TO GO BACK....", 1, WHITE)
		textpos = text.get_rect(centerx = pos_x, centery = pos_y)
		text_surface.blit(text, textpos)
		pos_y = pos_y + font_size
		
		openFile = open('data/credits.txt', "r")
		contents = openFile.readlines()
		for line in contents:
			text = font.render(line.strip(), 1, RED)
			textpos = text.get_rect(centerx = pos_x, centery = pos_y)
			text_surface.blit(text, textpos)
			pos_y = pos_y + font_size
		
		return text_surface, text_surface_rect
	
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
