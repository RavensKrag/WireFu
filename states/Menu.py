import pygame, os

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

from states import Level, CreditsScreen

class Menu(object):
	def __init__(self, window, font_size=32):
		self.window = window
		self.font_size = font_size
		
		self.background, self.backRect = self._load_image('bg2.png')
		
		self.menu_list = ["New Game", "Options", "Credits", "Exit"]
		self.selected = 0
		
		self.font = pygame.font.Font(None, font_size)
		
	def update(self):
		pass
		#~ self.selected = 0 % 4
	
	def draw(self, screen):
		screen.blit(self.background, (0,0))
		
		pos_x = self.window.width/2
		pos_y = self.window.height/2
		
		for i in range(4):
			color = RED
			if i == self.selected:
				color = BLUE
			
			text = self.font.render(self.menu_list[i], 1, color)
			textpos = text.get_rect(centerx = pos_x, centery = pos_y)
			screen.blit(text, textpos)
			
			pos_y = pos_y + self.font_size
	
	def cursor_up(self):
		self.selected = (self.selected - 1) % 4
	
	def cursor_down(self):
		self.selected = (self.selected + 1) % 4
	
	def select(self):
		#~ self.menu_list[self.selected]
		
		state = None
		if self.menu_list[self.selected] == "New Game":
			state = Level.Level(self.window.screen, self.window.space, 'level01.txt', 
							self.window.input_processor, self.window.gameclock)
		elif self.menu_list[self.selected] == "Options":
			pass
		elif self.menu_list[self.selected] == "Credits":
			state = CreditsScreen.CreditsScreen(self.window.screen)
		elif self.menu_list[self.selected] == "Exit":
			pass
		
		self.window.push_state(state)
	
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
