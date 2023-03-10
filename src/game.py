from src import players


def start_game():
    board = [None for i in range(9)]
    PLAYERS = ("X", "O")
    turns = 0

    while True:
        render_board(board)
        player = PLAYERS[turns % 2]
        coordinates = players.player_move(player, board)    # asks the player for a move
        make_move(coordinates, player, board)

        if check_for_winner(player, board):
            render_board(board)
            print(f"Player {player} has won the game!")
            return

        if check_for_draw(board):
            render_board(board)
            print("It's a draw!")
            return

        turns += 1


def check_for_winner(player: str, board: list):
    winning_rows = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for i in winning_rows:
        if board[i[0]] == player and board[i[1]] == player and board[i[2]] == player:
            return True
    return False


def check_for_draw(board: list):
    if None not in board:
        return True
    return False


def render_board(board: list):
    print()
    for i in range(9):
        if i == 3 or i == 6:
            print()
        if board[i] == None:
            print("_", end = " ")
        else:
            print(board[i], end = " ")
    print("\n" * 2)


def make_move(coordinates: int, player: str, board: list):
    board[coordinates] = player


#start_game()