import pygame, os

WHITE = (255, 255, 255)
RED = (255, 0, 0)

class CreditsScreen(object):
	def __init__(self):
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
	
	def update(self):
		pass
	
	def draw(self):
		
