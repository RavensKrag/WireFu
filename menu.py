import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)

def display_Menu(screen):
	menu_list = ["New Game", "Load Game", "Credits", "Exit"]
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
