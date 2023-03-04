import pygame
from src import menu, grid

def main():
    load_menu()

def load_menu():
    menu_buttons = menu.load_buttons(DISPLAY_SIZE, GAME_DISPLAY)
    menu_font = pygame.font.SysFont("Courier", 52)
    while True:
        menu.check_events(menu_buttons)
        menu.draw_graphics(menu_buttons, menu_font, DISPLAY_SIZE, GAME_DISPLAY)
        pygame.display.flip()
        game_clock.tick(60)
        if menu.game_started:
            load_game()

def load_game():
    game_buttons = grid.load_buttons(DISPLAY_SIZE, GAME_DISPLAY)
    game_squares = grid.load_game_squares(DISPLAY_SIZE, GAME_DISPLAY)
    background_square = grid.load_background_square(DISPLAY_SIZE, GAME_DISPLAY)
    game_font = pygame.font.SysFont("Courier", 32)
    while True:
        grid.check_events(game_buttons)
        grid.draw_graphics(game_buttons, game_font, DISPLAY_SIZE, GAME_DISPLAY)
        pygame.display.flip()
        game_clock.tick(60)


pygame.init()
game_clock = pygame.time.Clock()
DISPLAY_SIZE = (1280, 960)
GAME_DISPLAY = pygame.display.set_mode((DISPLAY_SIZE))
pygame.display.set_caption("Tic Tac Toe")
main()