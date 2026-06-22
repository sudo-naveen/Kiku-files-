"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flag = 0

    for row in board:
        for col in row:
            if not col is EMPTY:
                flag += 1

    if flag % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col is EMPTY:
                action.add((i, j))

    return action


def result(board, action):  # only update one cell and then return the whole board,action is (i,j)
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_copy = copy.deepcopy(board)

    if not action in actions(board):
        raise Exception("not a valid action")

    result_copy[action[0]][action[1]] = player(result_copy)
    return (result_copy)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horz
    for row in board:
        if row[0] == row[1] == row[2] and row[2] != EMPTY:
            return row[2]

    # vert
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[2][col] != EMPTY:
            return board[2][col]

    # diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or not any(EMPTY in row for row in board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)

    if win == X:
        return 1
    elif win == None:
        return 0
    else:
        return -1


def minimax(board):  # return (1,j) allowable
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current = player(board)

    if current == X:

        best_score = -math.inf
        best_action = None

        for action in actions(board):
            score = min_value(result(board, action))

            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    else:

        best_score = math.inf
        best_action = None

        for action in actions(board):
            score = max_value(result(board, action))

            if score < best_score:
                best_score = score
                best_action = action

        return best_action


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v