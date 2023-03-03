import pygame
from src import ui_elements

def load_buttons(display_size: tuple, display: pygame.surface):
    buttons = {}
    buttons["New_Game"] = ui_elements.Button("New Game", 38, display_size[0] / 2, display_size[1] / 2 + display_size[1] / 3, display)

def load_game_squares(display_size: tuple, display: pygame.surface):
    squares = {"square_0": ui_elements.Square(), 
               "square_1": ui_elements.Square(), 
               "square_3": ui_elements.Square(), 
               "square_4": ui_elements.Square(), 
               "square_5": ui_elements.Square(), 
               "square_6": ui_elements.Square(), 
               "square_7": ui_elements.Square(), 
               "square_8": ui_elements.Square()}
    
def load_background_square(display_size: tuple, display: pygame.surface):
    grid_square = pygame.Rect(1, 2, 3, 4)
    

def check_events(buttons):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

def draw_graphics(buttons: dict, font: pygame.font, display_size: tuple, display: pygame.surface):
    pass