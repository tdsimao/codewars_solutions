"""
    https://www.codewars.com/kata/529bf0e9bdf7657179000008
"""


def validSolution(board):
    return valid_rows(board) and valid_columns(board) and valid_sub_regions(board)


def valid_rows(board):
    for row in board:
        if has_repeated_values(row):
            return False
    return True


def valid_columns(board):
    for i in range(9):
        if has_repeated_values(row[i] for row in board):
            return False
    return True


def valid_sub_regions(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if has_repeated_values(sub_region(board, i, j)):
                return False
    return True


def sub_region(board, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            yield board[i][j]


def has_repeated_values(values, values_len=9):
    return len(set(values)) != values_len

