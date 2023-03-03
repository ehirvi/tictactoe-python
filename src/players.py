def player_move(GAME_BOARD: list, player: str) -> int:
    while True:
        move = int(input(f"Player {player} move: "))
        if move > len(GAME_BOARD)-1 or GAME_BOARD[move] is not None:
            print("Invalid square, try again")
            continue
        return move