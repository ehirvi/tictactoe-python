import pygame
from src import ui_elements

def load_buttons(display_size: tuple, display: pygame.Surface):
    buttons = {}
    buttons["New_Game"] = ui_elements.Button("New Game", 38, display_size[0] / 2, display_size[1] / 2 + display_size[1] / 3, display)

def load_game_squares(display_size: tuple, display: pygame.Surface):
    squares = {"square_0": ui_elements.Square(), 
               "square_1": ui_elements.Square(), 
               "square_3": ui_elements.Square(), 
               "square_4": ui_elements.Square(), 
               "square_5": ui_elements.Square(), 
               "square_6": ui_elements.Square(), 
               "square_7": ui_elements.Square(), 
               "square_8": ui_elements.Square()}
    return squares
    
def load_background_square(display_size: tuple, display: pygame.Surface):
    square = pygame.Rect()
    return square

def check_events(buttons: dict):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

def draw_graphics(buttons: dict, squares: dict, background_square: pygame.Rect, font: pygame.font.Font, display_size: tuple, display: pygame.Surface):
    pass

def draw_game_squares(squares: dict):
    for i in squares:
        i.draw_square()

def draw_background_square(square: pygame.Rect, display: pygame.Surface):
    pygame.draw.rect(display)