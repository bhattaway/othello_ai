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


def flat_score(board, color):
    tally = 0
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            print("IJ:",i,j, end=' ')
            if board[i][j] == color:
                tally += 1
    print("IN FLAT SCORE FOR",color,tally)
    return tally

def score(board, color):
    tally = 0
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == color:
                if (i == 0 and j == 0) or \
                        (i == board_size - 1 and j == 0) or \
                        (i == 0 and j == board_size - 1) or \
                        (i == board_size - 1 and j == board_size - 1):
                    tally += 99
                    print("CORNER!!",i,j)

                elif i == 0 or j == 0 or i == board_size - 1 or j == board_size - 1:
                    tally += 2

                tally += 1
    return tally

def utility(board, color, opponent_color):
    myscore = flat_score(board, color)
    oppscore = flat_score(board, opponent_color)

    #only care about win loss
    if myscore < oppscore:
        return -998
    elif myscore > oppscore:
        return 998
    else:
        return 0

def evaluate(board, color, opponent_color):
    '''
    #care about amount of moves
    return len(get_valid_moves(board, color, opponent_color)) - len(get_valid_moves(board, opponent_color, color))
    '''

    get_out = False
    for row in board:
        for char in row:
            if char == SPACE:
                get_out = True
                break
        if get_out:
            break
    else:
        # no spaces were found: care only about final outcome
        # (technically need to care about len of each player's moves being zero, but w/e)
        return utility(board, color, opponent_color)

    #some spaces were found...
    #care about score difference
    return score(board, color) - score(board, opponent_color)

def minimax(board, color, opponent_color, depth, isMaximizing):
    if depth == 0:
        #print("DEPTH 0, eval is:",evaluate(board, color, opponent_color))
        return evaluate(board, color, opponent_color), [99,99]

    if isMaximizing:
        bestvalue = -999
        bestmove = None
        movelist = get_valid_moves(board, color, opponent_color)
        if len(movelist) < 1:
            bestvalue = evaluate(board, color, opponent_color)
        for move in movelist:
            dummy_board = copy.deepcopy(board)
            put(dummy_board, color, opponent_color, move[0], move[1])
            childvalue, childmove = minimax(dummy_board, color, opponent_color, depth - 1, False)
            print("IN MAX, INVESTIGATING MOVE", move, "AT DEPTH",depth,"VALUE",childvalue)
            if bestvalue <= childvalue:
                bestvalue = childvalue
                bestmove = move
        print("MAX: DEPTH",depth,"; BESTVALUE",bestvalue,"; BESTMOVE",bestmove)
        return bestvalue, bestmove
    else:
        bestvalue = 999
        bestmove = None
        movelist = get_valid_moves(board, opponent_color, color)
        if len(movelist) < 1:
            bestvalue = evaluate(board, color, opponent_color)
        for move in movelist:
            dummy_board = copy.deepcopy(board)
            put(dummy_board, opponent_color, color, move[0], move[1])
            childvalue, childmove = minimax(dummy_board, color, opponent_color, depth - 1, True)
            print("IN MIN, INVESTIGATING MOVE", move, "AT DEPTH",depth,"VALUE",childvalue)
            if bestvalue >= childvalue:
                bestvalue = childvalue
                bestmove = move
        print("MIN: DEPTH",depth,"; BESTVALUE",bestvalue,"; BESTMOVE",bestmove)
        return bestvalue, bestmove


def get_move(board_size, board_state, turn, time_left, opponent_time_left):
    arr_board_size = board_size - 1
    oppcolor = opposite_color(turn)
    movelist = get_valid_moves(board_state, turn, oppcolor)
    if len(movelist) > 0:
        if time_left < 5000:
            bestval, bestmove = minimax(board_state, turn, oppcolor, 3, True)
        elif time_left < 500:
            bestval = "RANDOM"
            bestmove = random.choice(movelist)
        else:
            bestval, bestmove = minimax(board_state, turn, oppcolor, 5, True)
        print("MAIN: BESTVALUE:",bestval,"BESTMOVE",bestmove)

        return bestmove

    else:
        return None
