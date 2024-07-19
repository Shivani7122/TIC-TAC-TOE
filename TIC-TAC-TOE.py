def print_board(board):
    print("  0   1   2")
    for i, row in enumerate(board):
        print(" ", " | ".join(row))
        if i < 2:
            print(" ---+---+---")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    
    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
            continue

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = players[current_player]
                if check_winner(board, players[current_player]):
                    print_board(board)
                    print(f"Player {players[current_player]} wins!")
                    break
                if check_full(board):
                    print_board(board)
                    print("The game is a draw!")
                    break
                current_player = 1 - current_player
            else:
                print("That position is already taken. Try again.")
        else:
            print("Invalid position. Enter row and column between 0 and 2.")

if __name__ == "__main__":
    main()
