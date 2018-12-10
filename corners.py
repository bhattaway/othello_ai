import random

BLACK = 'B'
WHITE = 'W'
SPACE = ' '



def opposite_color(color):
    if color == BLACK:
        return WHITE
    else:
        return BLACK

def put_no_check(board, color, row, col):
    board[row][col] = color



def check_right(board, color, opp_color, row, col):
    found_opp_color = False
    for i in range(col + 1, len(board)):
        spot = board[row][i]
        if spot == opp_color:
            found_opp_color = True
        elif spot == color and found_opp_color:
            return True
        else:
            return False

    return False

def check_left(board, color, opp_color, row, col):
    found_opp_color = False
    for i in range(col - 1, -1, -1):
        spot = board[row][i]
        if spot == opp_color:
            found_opp_color = True
        elif spot == color and found_opp_color:
            return True
        else:
            return False

    return False

def check_up(board, color, opp_color, row, col):
    found_opp_color = False
    for i in range(row - 1, -1, -1):
        spot = board[i][col]
        if spot == opp_color:
            found_opp_color = True
        elif spot == color and found_opp_color:
            return True
        else:
            return False

    return False

def check_down(board, color, opp_color, row, col):
    found_opp_color = False
    for i in range(row + 1, len(board)):
        spot = board[i][col]
        if spot == opp_color:
            found_opp_color = True
        elif spot == color and found_opp_color:
            return True
        else:
            return False

    return False

def check_upleft(board, color, opp_color, row, col):
    found_opp_color = False

    for i in range(1, len(board)):
        if row - i < 0 or col - i < 0:
            break

        spot = board[row-i][col-i]
        if spot == opp_color:
            found_opp_color = True
        elif spot == color and found_opp_color:
            return True
        else:
            return False

    return False

def check_upright(board, color, opp_color, row, col):
    found_opp_color = False

    boardlen = len(board)
    for i in range(1, boardlen):
        if row - i < 0 or col + i >= boardlen:
            break

        spot = board[row-i][col+i]
        if spot == opp_color:
            found_opp_color = True
        elif spot == color and found_opp_color:
            return True
        else:
            return False

def check_downleft(board, color, opp_color, row, col):
    found_opp_color = False

    boardlen = len(board)
    for i in range(1, boardlen):
        if col - i < 0 or row + i >= boardlen:
            break

        spot = board[row+i][col-i]
        if spot == opp_color:
            found_opp_color = True
        elif spot == color and found_opp_color:
            return True
        else:
            return False

def check_downright(board, color, opp_color, row, col):
    found_opp_color = False

    boardlen = len(board)
    for i in range(1, boardlen):
        if row + i >= boardlen or col + i >= boardlen:
            break

        spot = board[row+i][col+i]
        if spot == opp_color:
            found_opp_color = True
        elif spot == color and found_opp_color:
            return True
        else:
            return False

    return False

def check_valid_move(board, color, opp_color, row, col):
    return board[row][col] == SPACE and \
            (check_right(board, color, opp_color, row, col) or \
            check_left(board, color, opp_color, row, col) or \
            check_up(board, color, opp_color, row, col) or \
            check_down(board, color, opp_color, row, col) or \
            check_upleft(board, color, opp_color, row, col) or \
            check_upright(board, color, opp_color, row, col) or \
            check_downleft(board, color, opp_color, row, col) or \
            check_downright(board, color, opp_color, row, col))

def get_valid_moves(board, color, opp_color):
    list_of_moves = []
    boardlen = len(board)
    for i in range(boardlen):
        for j in range(boardlen):
            if board[i][j] == SPACE:
                if check_valid_move(board, color, opp_color, i, j):
                    list_of_moves.append([i,j])

    return list_of_moves

def has_valid_move(board, color, opp_color):
    return len(get_valid_moves(board, color, opp_color)) > 0

def flip_right(board, color, row, col):
    col += 1
    while board[row][col] != color:
        put_no_check(board, color, row, col)
        col += 1

def flip_left(board, color, row, col):
    col -= 1
    while board[row][col] != color:
        put_no_check(board, color, row, col)
        col -= 1

def flip_up(board, color, row, col):
    row -= 1
    while board[row][col] != color:
        put_no_check(board, color, row, col)
        row -= 1

def flip_down(board, color, row, col):
    row += 1
    while board[row][col] != color:
        put_no_check(board, color, row, col)
        row += 1

def flip_upleft(board, color, row, col):
    row -= 1
    col -= 1
    while board[row][col] != color:
        put_no_check(board, color, row, col)
        row -= 1
        col -= 1

def flip_upright(board, color, row, col):
    row -= 1
    col += 1
    while board[row][col] != color:
        put_no_check(board, color, row, col)
        row -= 1
        col += 1

def flip_downleft(board, color, row, col):
    row += 1
    col -= 1
    while board[row][col] != color:
        put_no_check(board, color, row, col)
        row += 1
        col -= 1

def flip_downright(board, color, row, col):
    row += 1
    col += 1
    while board[row][col] != color:
        put_no_check(board, color, row, col)
        row += 1
        col += 1

def put(board, color, opp_color, row, col):
    if check_valid_move(board, color, opp_color, row, col):
        if check_right(board, color, opp_color, row, col):
            flip_right(board, color, row, col)
        if check_left(board, color, opp_color, row, col):
            flip_left(board, color, row, col)
        if check_up(board, color, opp_color, row, col):
            flip_up(board, color, row, col)
        if check_down(board, color, opp_color, row, col):
            flip_down(board, color, row, col)
        if check_upleft(board, color, opp_color, row, col):
            flip_upleft(board, color, row, col)
        if check_upright(board, color, opp_color, row, col):
            flip_upright(board, color, row, col)
        if check_downleft(board, color, opp_color, row, col):
            flip_downleft(board, color, row, col)
        if check_downright(board, color, opp_color, row, col):
            flip_downright(board, color, row, col)

        put_no_check(board, color, row, col)
        return True
    else:
        return False


def score(board, color):
    tally = 0
    for row in board:
        for col in row:
            if col == color:
                tally += 1
    return tally

def get_move(board_size, board_state, turn, time_left, opponent_time_left):
    arr_board_size = board_size - 1
    moves = get_valid_moves(board_state, turn, opposite_color(turn))
    if len(moves) > 0:
        for move in moves:
            if move == [0,0] or \
            move == [arr_board_size, 0] or \
            move == [0, arr_board_size] or \
            move == [arr_board_size, arr_board_size]:
                return move
        return random.choice(moves)
    else:
        return None
