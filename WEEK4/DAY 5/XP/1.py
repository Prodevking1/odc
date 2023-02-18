def print_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |")

def check_win(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != ' ':
            return True

    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6] and board[i] != ' ':
            return True

    if board[0] == board[4] == board[8] and board[0] != ' ':
        return True

    if board[2] == board[4] == board[6] and board[2] != ' ':
        return True

    return False

def main():
    board = [' ']*9
    player1 = 'X'
    player2 = 'O'
    current_player = player1

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        move = int(input("Enter move (1-9): "))
        move -= 1

        if board[move] != ' ':
            print("That square is already occupied. Try again.")
            continue

        board[move] = current_player

        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if all(square != ' ' for square in board):
            print_board(board)
            print("The game ends in a tie.")
            break

        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
