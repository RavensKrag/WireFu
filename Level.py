import os, pygame, re, sys
import pymunk as pm
from pymunk import Vec2d

# Import files
import Physics
import collisions

from gameobjects.platforms import Ground, Exit, Platform, Ramp
from gameobjects.zipline import ZiplineHandle, ZiplineWire
from gameobjects.powerups import Powerup_Jump_Number

class Level:
	def __init__(self, screen, filename, game_clock, input_handler):
		pygame.init()
		
		# Open level file
		level_file = self.openFile(filename)
		
		# Read load the background image
		line = level_file.readline()
		##image_fname = openFile(line)
		##fullname = os.path.join('levels', line)
		self.background = pygame.image.load('levels/level01.jpg').convert()
		
		# Set level size from file
		line = level_file.readline()
		matches = self.findPatterns(r'\d+', line)
		self.level_width = int(matches[0])
		self.level_height = int(matches[1])
		screen = pygame.display.set_mode((self.level_width,self.level_height))
		print('screen', screen)
		
		# Load platforms, ramps, and ziplines
		self.platforms = pygame.sprite.Group()
		line = level_file.readline()
		section = 0
		while line != '':
			print('section', section)
			if(line[0] == '#' or line[0] == '\n'):
				if line[0] == '#': section += 1
				line = level_file.readline()
			elif(section == 1):		# Load platforms
				matches = self.findPatterns(r'\d+.\d+', line)
				pos = [float(matches[0]),float(matches[1])]
				dimensions = [float(matches[2]),float(matches[3])]
				platform = Platform(pos,dimensions)
				self.platforms.add(platform)
				line = level_file.readline()
			elif(section == 2): 	# Load ramps
				matches = self.findPatterns(r'\d+.\d+', line)
				endPoint1 = [float(matches[0]),float(matches[1])]
				endPoint2 = [float(matches[2]),float(matches[3])]
				rampWidth = int(float(matches[4]))
				platform = Ramp(endPoint1,endPoint2,rampWidth)
				self.platforms.add(platform)
				line = level_file.readline()
			elif(section == 3):		# Load ziplines
				matches = self.findPatterns(r'\d+.\d+', line)
				endPoint1 = [float(matches[0]),float(matches[1])]
				endPoint2 = [float(matches[2]),float(matches[3])]
				print('endPoint1', endPoint1)
				print('endPoint2', endPoint2)
				platform = ZiplineWire(endPoint1,endPoint2)
				self.platforms.add(platform)			
				line = level_file.readline()
			elif(section == 4): 	# Load Exit platform
				matches = self.findPatterns(r'\d+.\d+', line)
				pos = [float(matches[0]),float(matches[1])]
				dimensions = [float(matches[2]),float(matches[3])]
				platform = Exit(pos,dimensions,game_clock,input_handler)
				self.platforms.add(platform)				
				line = level_file.readline()
			elif(section == 5):		# Load Jump powerups
				matches = self.findPatterns(r'\d+.\d+', line)
				pos = [float(matches[0]),float(matches[1])]
				dimensions = [float(matches[2]),float(matches[3])]
				platform = Powerup_Jump_Number(pos,dimensions)
				self.platforms.add(platform)
				line = level_file.readline()
			else:
				print('Format error in ' + filename + '. Program terminated.')
				sys.exit()
			
			

		self.screen = pygame.display.set_mode((self.level_width,self.level_height))
		self.screen.blit(self.background, (0,0))
	
	# Regular expression is used to find pattern within text
	def findPatterns(self, pat, text):
		match = re.findall(pat, text)
		if match:
			match
			return match
		else:
			print(pat + ' not found')
			
	def update(self):
		for p in self.platforms:
			p.update()
		
	def draw(self, screen):
		# Background
		self.screen.fill([0,0,0])
		
		print('TESTING -- self.platforms', self.platforms)
		
		# Environment
		for p in self.platforms:
			p.draw(self.screen)
			
		#self.screen.blit(self.background, (0,0))

	def openFile(self, filename):
		fullname = os.path.join('levels', filename)
		try:
			file = open(fullname, 'rU')
		except pygame.error, message:
			print 'Cannot load file:', fullname
			raise SystemExit, message
		return file
			
		
		
def main():
	pygame.init()
	screen = pygame.display.set_mode()
	pygame.display.set_caption('Level Tester')
	pygame.mouse.set_visible(0)
	
	clock = pygame.time.Clock()
	gameclock = GameClock(clock)
	
	player = Player()
	input_processor = EventProcessor(player)

	level01 = Level(screen, 'level01.txt', gameclock, input_processor)
	level01.draw(screen)

	pygame.quit()
	
#this calls the 'main' function when this script is executed
#if __name__ == '__main__': main()
	