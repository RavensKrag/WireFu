import pygame, os

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)

class PauseScreen(object):
	def __init__(self, window, font_size=32):
		self.window = window
		self.font_size = font_size

		self.music = "jazz_I_Like_to_Hit_Thing.wav"
		
		self.font = pygame.font.Font(None, font_size)
		self.prompt = self.font.render("Press P to resume", 1, BLACK)
		self.promptpos = self.prompt.get_rect(centerx = self.window.width/2, centery = self.window.height/3)
                self.window.gameclock.stop()
		
	def update(self):
		pass
	
	def draw(self, screen):
                pygame.draw.rect(screen, BLUE, (self.window.width/2-300, self.window.height/3-50, 650, 100))
		screen.blit(self.prompt, self.promptpos)
	
	def delete(self):
		pass
