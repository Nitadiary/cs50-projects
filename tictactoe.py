import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)
    if X_count <= O_count:
        return X
    else:
        return O


def actions(board):
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    i, j = action
    if i < 0 or i > 2 or j < 0 or j > 2:
        raise Exception("Invalid Move")
    if board[i][j] != EMPTY:
        raise Exception("Invalid Move")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)

    return new_board


def winner(board):

    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):

    if winner(board) != None:
        return True
    if all(cell != EMPTY for row in board for cell in row):
        return True
    return False


def utility(board):

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):

    if terminal(board):
        return None
    turn = player(board)

    def max_value(b):
        if terminal(b):
            return utility(b)
        v = -float("inf")
        for action in actions(b):
            v = max(v, min_value(result(b, action)))
        return v

    def min_value(b):
        if terminal(b):
            return utility(b)
        v = float("inf")
        for action in actions(b):
            v = min(v, max_value(result(b, action)))
        return v
    best_action = None

    if turn == X:
        value = -float("inf")
        for action in actions(board):
            move_val = min_value(result(board, action))
            if move_val > value:
                value = move_val
                best_action = action

    else:
        value = float("inf")
        for action in actions(board):
            move_val = max_value(result(board, action))
            if move_val < value:
                value = move_val
                best_action = action
    return best_action
