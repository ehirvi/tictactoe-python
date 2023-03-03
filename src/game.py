from src import players

def new_game():
    GAME_BOARD = [None for i in range(9)]
    GAME_PLAYERS = ("X", "O")
    game_turns = 0
    game_loop()

def restart_game():
    restart = input("Would you like to play again? (y/n): ")
    if restart == "y":
        return True
    return False

def game_loop():
    while True:
        render_board()
        current_player = GAME_PLAYERS[game_turns % 2]
        coordinates = players.player_move(GAME_BOARD, current_player)
        make_move(coordinates, current_player)

        if check_for_winner(current_player):
            render_board()
            print(f"Player {current_player} has won the game!")
            if restart_game():
                new_game()
            else:
                break

        if check_for_draw():
            render_board()
            print("It's a draw!")
            if restart_game():
                new_game()
            else:
                break

        game_turns += 1
            

def check_for_winner(current_player):
    winning_rows = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for i in winning_rows:
        if GAME_BOARD[i[0]] == current_player and GAME_BOARD[i[1]] == current_player and GAME_BOARD[i[2]] == current_player:
            return True
    return False


def check_for_draw():
    if None not in GAME_BOARD:
        return True
    return False

def render_board():
    print()
    for i in range(9):
        if i == 3 or i == 6:
            print()
        if GAME_BOARD[i] == None:
            print("_", end=" ")
        else:
            print(GAME_BOARD[i], end=" ")
        print("\n" * 2)


def make_move(coordinates: int, player: str):
    GAME_BOARD[coordinates] = player