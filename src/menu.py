import pygame
from src import ui_elements

def load_buttons(display_size: tuple, display: pygame.Surface):
    buttons =  {}
    buttons["New_Game"] = ui_elements.Button("New Game", 38, display_size[0] / 2, display_size[1] / 2 + display_size[1] / 8, display)
    return buttons

def check_events(buttons):
    events = pygame.event.get()
    global game_started
    game_started = buttons["New_Game"].is_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

def draw_graphics(buttons: dict, font: pygame.font, display_size: tuple, display: pygame.Surface):
    display.fill((70, 130, 180))
    menu_title = font.render("Tic Tac Toe", True, (255, 255, 255))
    display.blit(menu_title, (display_size[0] / 2 - menu_title.get_width() / 2, display_size[1] / 2 - menu_title.get_height() / 2))
    buttons["New_Game"].draw_button()
    pygame.display.flip()

game_started = False
