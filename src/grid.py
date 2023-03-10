import pygame
from src import ui_elements
from src import game

def load_buttons(display_size: tuple, display: pygame.Surface):
    buttons = {}
    buttons["New_Game"] = ui_elements.Button("New Game", 32, display_size[0] / 2, display_size[1] / 2 + display_size[1] / 3, display)
    return buttons


def load_game_squares(background_square_size: tuple, display_size: tuple, display: pygame.Surface):
    squares = {"square_0": ui_elements.Square(display_size[0] / 4, display_size[1] / 8, background_square_size[0] / 3, background_square_size[1] / 3, display), 
               "square_1": ui_elements.Square(display_size[0] / 4 + background_square_size[0] / 3, display_size[1] / 8, background_square_size[0] / 3, background_square_size[1] / 3, display), 
               "square_2": ui_elements.Square(display_size[0] / 4 + (background_square_size[0] / 3 * 2), display_size[1] / 8, background_square_size[0] / 3 + 1, background_square_size[1] / 3, display,), 
               "square_3": ui_elements.Square(display_size[0] / 4, display_size[1] / 8 + background_square_size[1] / 3, background_square_size[0] / 3, background_square_size[1] / 3, display), 
               "square_4": ui_elements.Square(display_size[0] / 4 + background_square_size[0] / 3, display_size[1] / 8 + background_square_size[1] / 3, background_square_size[0] / 3, background_square_size[1] / 3, display), 
               "square_5": ui_elements.Square(display_size[0] / 4 + (background_square_size[0] / 3 * 2), display_size[1] / 8 + background_square_size[1] / 3, background_square_size[0] / 3 + 1, background_square_size[1] / 3, display), 
               "square_6": ui_elements.Square(display_size[0] / 4, display_size[1] / 8 + (background_square_size[0] / 3 * 2), background_square_size[0] / 3, background_square_size[1] / 3 + 1, display), 
               "square_7": ui_elements.Square(display_size[0] / 4 + background_square_size[0] / 3, display_size[1] / 8 + (background_square_size[0] / 3 * 2), background_square_size[0] / 3, background_square_size[1] / 3 + 1, display), 
               "square_8": ui_elements.Square(display_size[0] / 4 + (background_square_size[0] / 3 * 2), display_size[1] / 8 + (background_square_size[0] / 3 * 2), background_square_size[0] / 3 + 1, background_square_size[1] / 3 + 1, display)}
    return squares
    

def load_background_square(display_size: tuple):
    square = pygame.Rect(display_size[0] / 4, display_size[1] / 8, display_size[0] / 2, display_size[0] / 2)
    return square


def check_events(buttons: dict, game_squares: dict):
    events = pygame.event.get()

    are_squares_pressed_on(game_squares)
    buttons["New_Game"].is_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()


def are_squares_pressed_on(squares: dict):
    for i in squares.values():
        i.is_pressed()


def draw_graphics(buttons: dict, squares: dict, background_square: pygame.Rect, font: pygame.font.Font, display_size: tuple, display: pygame.Surface):
    display.fill((70, 130, 180))
    draw_background_square(background_square, display)
    draw_game_squares(squares)
    buttons["New_Game"].draw_button()
    pygame.display.flip()


def draw_game_squares(squares: dict):
    for i in squares.values():
        i.draw_square()


def draw_background_square(square: pygame.Rect, display: pygame.Surface):
    pygame.draw.rect(display, (255, 255, 255), square, 10, 5)