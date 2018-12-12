import random
import copy

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

def utility(board, color, opponent_color):
    myscore = score(board, color)
    oppscore = score(board, opponent_color)

    #only care about win loss
    if myscore < oppscore:
        return -1
    elif myscore > oppscore:
        return 1
    else:
        return 0

def evaluate(board, color, opponent_color):
    '''
    #care about amount of moves
    return len(get_valid_moves(board, color, opponent_color)) - len(get_valid_moves(board, opponent_color, color))
    '''

    #care about score difference
    return score(board, color) - score(board, opponent_color)

def minimax(board, color, opponent_color, depth, isMaximizing):
    if depth == 0:
        return evaluate(board, color, opponent_color), None

    if isMaximizing:
        bestvalue = -999
        bestmove = None
        movelist = get_valid_moves(board, color, opponent_color)
        for move in movelist:
            dummy_board = copy.deepcopy(board)
            put(dummy_board, color, opponent_color, move[0], move[1])
            childvalue, childmove = minimax(dummy_board, color, opponent_color, depth - 1, False)
            if bestvalue < childvalue:
                bestvalue = childvalue
                bestmove = move
        return bestvalue, bestmove
    else:
        bestvalue = 999
        bestmove = None
        movelist = get_valid_moves(board, opponent_color, color)
        for move in movelist:
            dummy_board = copy.deepcopy(board)
            put(dummy_board, opponent_color, color, move[0], move[1])
            childvalue, childmove = minimax(dummy_board, color, opponent_color, depth - 1, True)
            if bestvalue > childvalue:
                bestvalue = childvalue
                bestmove = move
        return bestvalue, bestmove
        '''
        value = 999
        movelist = getmoves(board)
        for move in movelist:
            value = min(value, minimax(child, depth - 1, True))

        return value
        '''


def get_move(board_size, board_state, turn, time_left, opponent_time_left):
    arr_board_size = board_size - 1
    oppcolor = opposite_color(turn)
    movelist = get_valid_moves(board_state, turn, oppcolor)
    if len(movelist) > 0:
        bestval, bestmove = minimax(board_state, turn, oppcolor, 3, True)
        print("BESTVALUE:",bestval,"BESTMOVE",bestmove)

        return bestmove
        '''
        maxscore = -99
        scorelist = []
        bestmove = []
        for move in moves:
            dummy_board = copy.deepcopy(board_state)
            put(dummy_board, turn, oppcolor, move[0], move[1])
            movescore = (move, evaluate(dummy_board, turn, oppcolor))
            scorelist.append(movescore)
            if movescore[1] > maxscore:
                maxscore = movescore[1]
                bestmove = move

        
        print(maxscore, scorelist)
        return bestmove
        '''

    else:
        return None
