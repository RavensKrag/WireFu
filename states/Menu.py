import pygame, os

WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Menu(object):
	def __init__(self, screen):
		self.screen = screen
		
		self.background, self.backRect = load_image('bg2.png')
		self.screen.blit(background, (0,0))
	
	def load_image(name, colorkey=None):
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
	
	def display_Menu(screen):
		background, backRect = load_image('bg2.png')
		screen.blit(background, (0,0))
		
		menu_list = ["New Game", "Options", "Credits", "Exit"]
		menu_list_pos = []
		font = pygame.font.Font(None, 32)
		
		pos_x = screen.get_width()/2
		pos_y = screen.get_height()/2
		
		selected = 0 % 4
		
		for m in menu_list:
			text = font.render(m, 1, RED)
			textpos = text.get_rect(centerx = pos_x, centery = pos_y)
			screen.blit(text, textpos)
			menu_list_pos.append(textpos)
			pos_y = pos_y + 32
		
		#as a default, the first item is selected
		text = font.render(menu_list[selected], 1, WHITE)
		screen.blit(text, menu_list_pos[selected])
		
		pygame.display.flip()
		
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						#make the previous selection in red
						text = font.render(menu_list[selected], 1, RED)
						screen.blit(text, menu_list_pos[selected])
		
						#current selection is in white
						selected = (selected + 1) % 4
						text = font.render(menu_list[selected], 1, WHITE)
						screen.blit(text, menu_list_pos[selected])
						pygame.display.flip()
		
					elif event.key == pygame.K_UP:
						#make the previous selection in red
						text = font.render(menu_list[selected], 1, RED)
						screen.blit(text, menu_list_pos[selected])
		
						#current selection is in white
						selected = (selected - 1) % 4
						text = font.render(menu_list[selected], 1, WHITE)
						screen.blit(text, menu_list_pos[selected])
						pygame.display.flip()
		
					elif event.key == pygame.K_RETURN:
						return menu_list[selected]
	
	
	def display_Credits(screen):
		pos_x = screen.get_width()/2
		pos_y = screen.get_width()/2
		
		background, backRect = load_image('bg1.jpg')
		screen.blit(background, backRect)
		pygame.display.flip()
		
		s = pygame.Surface((1020, 2000), pygame.SRCALPHA, 32)
		s = s.convert_alpha()
		s_rect = s.get_rect()
		
		font = pygame.font.Font(None, 32)
		
		text = font.render("PRESS SPACE BAR TO GO BACK....", 1, WHITE)
		textpos = text.get_rect(centerx = pos_x, centery = pos_y)
		s.blit(text, textpos)
		pos_y = pos_y + 32
		
		openFile = open('data/credits.txt', "r")
		contents = openFile.readlines()
		for line in contents:
			text = font.render(line.strip(), 1, RED)
			textpos = text.get_rect(centerx = pos_x, centery = pos_y)
			s.blit(text, textpos)
			pos_y = pos_y + 32
			
		screen.blit(s, s_rect)
		pygame.display.flip()
		
		clock = pygame.time.Clock()
		
		running = True
		while running:
			clock.tick(50)
			s.scroll(0, -1)
			screen.blit(background, backRect)
			screen.blit(s, s_rect)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						#go back to the menu screen when space is pressed
						running = False
	
