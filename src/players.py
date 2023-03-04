def player_move(player: str, board: list) -> int:
    while True:
        move = int(input(f"Player {player} move: "))
        if move > len(board)-1 or board[move] is not None:
            print("Invalid square, try again")
            continue
        return move