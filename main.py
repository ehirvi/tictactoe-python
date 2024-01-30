import pygame
import json
from src import menu, grid, game

def main():
    load_menu()


def load_menu():
    menu_buttons = menu.load_buttons(DISPLAY_SIZE, GAME_DISPLAY)
    #menu_font = pygame.font.SysFont("Courier", 52)
    menu_font = pygame.font.Font("assets/Poppins-Regular.ttf", 52)
    while True:
        menu.check_events(menu_buttons)
        menu.draw_graphics(menu_buttons, menu_font, DISPLAY_SIZE, GAME_DISPLAY)
        if menu.game_started:
            load_game()
        GAME_CLOCK.tick(60)


def load_game():
    game_buttons = grid.load_buttons(DISPLAY_SIZE, GAME_DISPLAY)
    background_square = grid.load_background_square(DISPLAY_SIZE)
    game_squares = grid.load_game_squares((background_square.width, background_square.height), DISPLAY_SIZE, GAME_DISPLAY)
    game_font = pygame.font.SysFont("Courier", 32)
    game.start_game()
    while True:
        player = game.PLAYERS[game.turns % 2]
        grid.check_events(game_buttons, game_squares)
        grid.draw_graphics(game.board, game_buttons, game_squares, background_square, game_font, DISPLAY_SIZE, GAME_DISPLAY)
        GAME_CLOCK.tick(60)


def load_settings():
    with open("settings.json") as file:
        content = file.read()
        settings = json.loads(content)
        resolution = settings["resolution"].split(";")
        return (int(resolution[0]), int(resolution[1]))


pygame.init()
GAME_CLOCK = pygame.time.Clock()
DISPLAY_SIZE = load_settings()
GAME_DISPLAY = pygame.display.set_mode((DISPLAY_SIZE))
pygame.display.set_caption("Tic Tac Toe")
main()