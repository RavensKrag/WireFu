import pygame, os
from pygame.locals import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)

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

def display_Menu(screen, jukebox):
    background, back_rect = load_image('bg2.png')
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

    inputs = {}

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    inputs[event.key] = True

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
                
            elif event.type == pygame.KEYUP:
                    inputs[event.key] = False

        if inputs.get(pygame.K_1, False):
	    jukebox.higher_volume()
	if inputs.get(pygame.K_2, False):
	    jukebox.lower_volume()


def display_Credits(screen):
    pos_x = screen.get_width()/2
    pos_y = screen.get_width()/2

    background, back_rect = load_image('bg1.jpg')
    screen.blit(background, back_rect)
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
        screen.blit(background, back_rect)
        screen.blit(s, s_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #go back to the menu screen when space is pressed
                    running = False

def display_Options(screen, jukebox):
    font = pygame.font.Font(None, 32)

    #pos_x = screen.get_width()/2
    #pos_y = screen.get_width()/2
    pos_x = 100
    pos_y = 100

    if jukebox.music_on:
        music = font.render("Music Enabled", 1, WHITE)
    else:
        music = font.render("Music Disabled", 1, RED)
    music_rect = music.get_rect(centerx = pos_x, centery = pos_y)
    pos_y = pos_y + 40


    if jukebox.sound_on:
        sound = font.render("Sound Enabled", 1, WHITE)
    else:
        sound = font.render("Sound Disabled", 1, RED)
    sound_rect = sound.get_rect(centerx=pos_x, centery=pos_y)

    text = font.render("PRESS SPACE BAR TO GO BACK....", 1, WHITE)
    textpos = text.get_rect(centerx = 500, centery = 500) 
    
    background, back_rect = load_image('bg1.jpg')
    screen.blit(background, back_rect)
    screen.blit(music, music_rect)
    screen.blit(sound, sound_rect)
    screen.blit(text, textpos)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
            
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == 1:
                    if music_rect.collidepoint(pygame.mouse.get_pos()):
                        jukebox.ToggleMusic()
                        if jukebox.music_on:
                            music = font.render("Music Enabled", 1, WHITE)
                        else:
                            music = font.render("Music Disabled", 1, RED)

                    if sound_rect.collidepoint(pygame.mouse.get_pos()):
                        jukebox.ToggleSound()
                        if jukebox.sound_on:
                            sound = font.render("Sound Enabled", 1, WHITE)
                        else:
                            sound = font.render("Sound Disabled", 1, RED)

            screen.blit(background, back_rect)
            screen.blit(music, music_rect)
            screen.blit(sound, sound_rect)
            screen.blit(text, textpos)
            pygame.display.flip()

