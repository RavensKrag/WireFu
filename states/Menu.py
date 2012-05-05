import pygame, os

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)

from states import Level, CreditsScreen, OptionsScreen

class Menu(object):
	def __init__(self, window, jukebox, font_size=32):
		self.window = window
		self.font_size = font_size
		
		self.music = 'elec_Run_The_Blockade.wav'
		
		self.background, self.backRect = self._load_image('bg2.png')
		
		self.menu_list = ["New Game", "Options", "Credits", "Exit"]
		self.selected = 0
		
		self.font = pygame.font.Font(None, font_size)

		self.jukebox = jukebox
		
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

                pos_y = pos_y + self.font_size
		prompt = self.font.render("Press enter to select", 1, BLACK)
		promptpos = prompt.get_rect(centerx=pos_x, centery = pos_y)
		screen.blit(prompt, promptpos)
	
	def delete(self):
		pass
	
	def cursor_up(self):
		self.selected = (self.selected - 1) % 4
	
	def cursor_down(self):
		self.selected = (self.selected + 1) % 4
	
	def select(self):
		#~ self.menu_list[self.selected]
		
		state = None
		if self.menu_list[self.selected] == "New Game":

			state = Level.Level(self.window, self.window.space, 'level03.txt', 
							self.window.input_processor, self.window.gameclock)
		elif self.menu_list[self.selected] == "Options":
			state = OptionsScreen.OptionsScreen(self.window.screen, self.jukebox)
		elif self.menu_list[self.selected] == "Credits":
			state = CreditsScreen.CreditsScreen(self.window.screen)
		elif self.menu_list[self.selected] == "Exit":
			pass
		
		if state:
			self.window.push_state(state)
		else:
			self.window.running = False
	
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
