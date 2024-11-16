def ConstBoard(board):
    print("Current board state:\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("\n")
        if board[i] == 1:
            print("O ", end=" ")
        elif board[i] == -1:
            print("X ", end=" ")
        else:
            print("- ", end=" ")
    print("\n")

def User1Turn(board):
    pos = int(input("Enter X's position from [1,2...9]: "))
    if board[pos - 1] != 0:
        print("Wrong Move")
        return False  # Indicate an invalid move
    board[pos - 1] = -1
    return True

def User2Turn(board):
    pos = int(input("Enter O's position from [1,2...9]: "))
    if board[pos - 1] != 0:
        print("Wrong Move")
        return False  # Indicate an invalid move
    board[pos - 1] = 1
    return True

def analyzeboard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(8):
        if board[cb[i][0]] + board[cb[i][1]] + board[cb[i][2]] == 3:
            return 1
        if board[cb[i][0]] + board[cb[i][1]] + board[cb[i][2]] == -3:
            return -1
    return 0

def main():
    choice = int(input("Enter 1 for single player, 2 for multiplayer: "))
    board = [0] * 9
    if choice == 1:
        print("Computer: O vs You: X")
        player = int(input("Do you wanna play 1(st) or 2(nd): "))
        for i in range(9):
            ConstBoard(board)
            if analyzeboard(board) != 0:
                break
            if (i + player) % 2 == 0:
                computerturn(board)
            else:
                if not User1Turn(board):  # Retry on invalid move
                    continue
    else:
        for i in range(9):
            ConstBoard(board)
            if analyzeboard(board) != 0:
                break
            if i % 2 != 0:
                if not User2Turn(board):
                    continue
            else:
                if not User1Turn(board):
                    continue
    x = analyzeboard(board)
    ConstBoard(board)
    if x == 0:
        print("DRAW!!")
    elif x == 1:
        print("O has Won and X lost")
    elif x == -1:
        print("X has Won and O lost")

def computerturn(board):
    pos = -1
    val = -2
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = -minmax(board, -1)
            board[i] = 0
            if score > val:
                val = score
                pos = i
    if pos != -1:
        board[pos] = 1

def minmax(board, player):
    x = analyzeboard(board)
    if x != 0:
        return x * player
    pos = -1
    val = -2
    for i in range(9):
        if board[i] == 0:
            board[i] = player
            score = -minmax(board, -player)
            board[i] = 0
            if score > val:
                val = score
                pos = i
    if pos == -1:
        return 0
    return val

# Run the game
main()
  