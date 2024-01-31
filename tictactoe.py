import sys

board = [' ' for _ in range(9)]

winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]


def printBoard():
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")


def evaluateBoard():
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == 'X':
            return 1
        elif board[combo[0]] == board[combo[1]] == board[combo[2]] == 'O':
            return -1
    return 0


def emptyCells():
    return [i for i, cell in enumerate(board) if cell == ' ']


def isBoardFull():
    return ' ' not in board


def isGameOver():
    return evaluateBoard() or isBoardFull()


def minimax(depth, maximizingPlayer):
    if maximizingPlayer:
        maxEval = -sys.maxsize
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(depth + 1, False)
                board[i] = ' '
                maxEval = max(maxEval, eval)
        return maxEval if depth > 0 else maxEval
    else:
        minEval = sys.maxsize
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(depth + 1, True)
                board[i] = ' '
                minEval = min(minEval, eval)
        return minEval if depth > 0 else minEval


def aiMove():
    bestScore = -sys.maxsize
    bestMove = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(0, False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i

    board[bestMove] = 'X'
    print("AI:")
    printBoard()


def humanMove():
    while True:
        move = input("You: (Enter from 0-8): ")
        if move.isdigit() and int(move) in range(9) and board[int(move)] == ' ':
            board[int(move)] = 'O'
            break
        else:
            print("Invalid move, try again!")
    printBoard()


def playTicTacToe():
    print("Welcome to Tic-Tac-Toe by Pranit Zambre! Note: the following numbering: 0->1->2 /n 3->4->5 /n 6->7->8")
    printBoard()

    while not isGameOver():
        aiMove()
        if isGameOver():
            break
        humanMove()

    result = evaluateBoard()
    if result == 1:
        print("AI WON, LOL!")
    elif result == -1:
        print("YOU WON! DON'T GET TOO COCKY.")
    else:
        print("TIE!")


if __name__ == "__main__":
    playTicTacToe()
