import pygame
import os
pygame.mixer.init()
 
MUSIC_ON = True
SOUND_ON = True
 
 
class Jukebox:
    def __init__(self):
        self.name = "Jukebox"
 
        self.music_on = MUSIC_ON
        self.sound_on = SOUND_ON

        self.bgm = self.load_sound('HawaiiFive.wav')
        
        self.powerup_sound = self.load_sound('shiny-ding.wav')

    def ToggleMusic(self,on=True):
        self.music_on = on
        if self.music_on == False:
                self.powerup_sound.stop()
        else:
                self.powerup_sound.play()
 
    def ToggleSound(self,on=True):
        self.sound_on = on
        if self.sound_on == False:
                self.bgm.stop()
        else:
                self.bgm.play()

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
        self.bgm.play(-1)

    def play_powerup(self):
        self.powerup_sound.play()
