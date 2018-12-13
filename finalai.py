import random
import copy

BLACK = 'B'
WHITE = 'W'
SPACE = ' '


def get_num_turns(board):
    num_turns = 0
    for row in board:
        for char in row:
            if char != SPACE:
                num_turns += 1

    return num_turns

def num_frontier_discs(board, color):
    num_discs = 0
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            #print("checking ij...", end='')
            if board[i][j] == color:
                #print("COLOR FOUND!",i,j, end='')
                #the middle
                if i > 0 and j > 0 and i < board_size - 1 and j < board_size - 1:
                    #print("MIDDLE FOUND",i,j)
                    #n w s e se ne sw nw
                    if board[i-1][j] == SPACE or \
                        board[i][j-1] == SPACE or \
                        board[i+1][j] == SPACE or \
                        board[i][j+1] == SPACE or \
                        board[i+1][j+1] == SPACE or \
                        board[i-1][j+1] == SPACE or \
                        board[i+1][j-1] == SPACE or \
                        board[i-1][j-1] == SPACE:
                        num_discs += 1

                #top/bot rows
                elif i == 0 or i == board_size - 1:
                    if j != 0 and j != board_size - 1:
                        #print("TOPBOT FOUND",i,j)
                        # w e
                        if board[i][j-1] == SPACE or \
                            board[i][j+1] == SPACE:
                            num_discs += 1
                    else:
                        #print("CORNER FOUND",i,j)
                        num_discs -= 20

                #left/right cols
                elif j == 0 or j == board_size - 1:
                    #print("LR FOUND",i,j)
                    if i != 0 and i != board_size - 1:
                        # n s
                        if board[i-1][j] == SPACE or \
                            board[i+1][j] == SPACE: \
                            num_discs += 1
    return num_discs

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
            #print("IJ:",i,j, end=' ')
            if board[i][j] == color:
                tally += 1
    #print("IN FLAT SCORE FOR",color,tally)
    return tally

def score(board, color):
    tally = 0
    board_size = len(board) - 1
    scores = [[5, 3, 3, 3, 3, 3, 3, 5],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [5, 3, 3, 3, 3, 3, 3, 5]]
    '''
    scores = [[40, 3, 3, 3, 3, 3, 3, 40],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [40, 3, 3, 3, 3, 3, 3, 40]]
    '''
    '''
    scores = [[80, -5, 3, 3, 3, 3, -5, 80],
                   [-5, -7, 1, 1, 1, 1, -7, -5],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [3, 1, 1, 1, 1, 1, 1, 3],
                   [-5, -7, 1, 1, 1, 1, -7, -5],
                   [80, -5, 3, 3, 3, 3, -5, 80]]
    if board[0][0] != SPACE:
        scores[1][1] = 1
        scores[0][1] = 3
        scores[1][0] = 3
    if board[-1][0] != SPACE:
        scores[-2][1] = 1
        scores[-1][1] = 3
        scores[-2][0] = 3
    if board[0][-1] != SPACE:
        scores[1][-2] = 1
        scores[1][-1] = 3
        scores[0][-2] = 3
    if board[-1][-1] != SPACE:
        scores[-2][-2] = 1
        scores[-1][-2] = 3
        scores[-2][-1] = 3
    '''
    for i in range(board_size + 1):
        for j in range(board_size + 1):
            if board[i][j] == color:
                #print("SCORING:",i,j,scores[i][j])
                tally += scores[i][j]
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

def corner_test(board, color):
    total = 0

    if board[0][0] == color:
        total += 1
    if board[-1][0] == color:
        total += 1
    if board[0][-1] == color:
        total += 1
    if board[-1][-1] == color:
        total += 1

    if board[0][0] == SPACE:
        if board[1][1] == color:
            total -= 2
        if board[1][0] == color:
            total -= 2
        if board[0][1] == color:
            total -= 2
    if board[-1][0] == SPACE:
        if board[-2][1] == color:
            total -= 2
        if board[-1][1] == color:
            total -= 2
        if board[-2][0] == color:
            total -= 2
    if board[0][-1] == SPACE:
        if board[1][-2] == color:
            total -= 2
        if board[1][-1] == color:
            total -= 2
        if board[0][-2] == color:
            total -= 2
    if board[-1][-1] == SPACE:
        if board[-2][-1] == color:
            total -= 2
        if board[-1][-2] == color:
            total -= 2
        if board[-2][-2] == color:
            total -= 2

    return total



def evaluate(board, color, opponent_color):
    '''
    #care about amount of moves
    return len(get_valid_moves(board, color, opponent_color)) - len(get_valid_moves(board, opponent_color, color))
    '''
    board_size = len(board)

    #no more turns left, do a true eval
    if get_num_turns(board) - board_size * board_size == 0:
        # no spaces were found: care only about final outcome
        # (technically need to care about len of each player's moves being zero, but w/e)
        score_weight = 100
        score_value = score_weight * (flat_score(board, color) - flat_score(board, opponent_color)) / \
                        (flat_score(board, color) + flat_score(board, opponent_color))

        #print("SCORE ONLY:",score_value)
        return score_value
    else:
        #if get_num_turns(board) < board_size * board_size - 10:
        #mobility
        score_weight = 25
        score_value = score_weight * (flat_score(board, color) - flat_score(board, opponent_color)) / \
                        (flat_score(board, color) + flat_score(board, opponent_color))

        corner_denom = corner_test(board, color) + corner_test(board, opponent_color)
        if corner_denom != 0:
            corner_weight = 300
            corner_value = corner_weight * (corner_test(board, color) - corner_test(board, opponent_color)) / \
                            corner_denom
        else:
            corner_value = 0


        frontier_denom = num_frontier_discs(board, color) + num_frontier_discs(board, opponent_color)
        if frontier_denom != 0:
            frontier_weight = 35
            frontier_value = frontier_weight * (num_frontier_discs(board, color) - num_frontier_discs(board, opponent_color)) / \
                                frontier_denom
        else:
            frontier_value = 0


        #print("SCORE:",score_value,"CORNER:",corner_value,"FRONTIER:",frontier_value,"TOTAL:",score_value + corner_value + frontier_value)
        return score_value + corner_value + frontier_value
        #return num_frontier_discs(board, opponent_color) - num_frontier_discs(board, color)
        #care about score difference
        #print("DOING SCORE")
        #score_value = score_weight * score(board, color) - score(board, opponent_color)

def alphabeta(board, color, opponent_color, depth, alpha, beta, isMaximizing):
    if depth == 0:
        #print("DEPTH 0, eval is:",evaluate(board, color, opponent_color))
        #if isMaximizing:
        return evaluate(board, color, opponent_color), [99,99]
        '''
        else:
            return evaluate(board, opponent_color, color), [99,99]
        '''

    if isMaximizing:
        bestvalue = -999
        bestmove = None
        movelist = get_valid_moves(board, color, opponent_color)
        if len(movelist) < 1:
            bestvalue = evaluate(board, color, opponent_color)
        for move in movelist:
            '''
            board_size = len(board) - 1
            if move in ([0,0],[0,board_size],[board_size,0],[board_size,board_size]):
                print("CORNER MOVE MAX FOUND GIMME GIMME",move)
                return 500, move
            '''
            dummy_board = copy.deepcopy(board)
            put(dummy_board, color, opponent_color, move[0], move[1])
            childvalue, childmove = alphabeta(dummy_board, color, opponent_color, depth - 1, alpha, beta, False)
            #print("IN MAX, INVESTIGATING MOVE", move, "AT DEPTH",depth,"VALUE",childvalue)
            if bestvalue <= childvalue:
                bestvalue = childvalue
                bestmove = move
            alpha = max(alpha, bestvalue)
            if alpha >= beta:
                #print("BETA CUTOFF REACHED a:",alpha,"b:",beta)
                break

        #print("MAX: DEPTH",depth,"; BESTVALUE",bestvalue,"; BESTMOVE",bestmove)
        return bestvalue, bestmove
    else:
        bestvalue = 999
        bestmove = None
        movelist = get_valid_moves(board, opponent_color, color)
        #print(movelist)
        if len(movelist) < 1:
            bestvalue = evaluate(board, color, opponent_color)
        for move in movelist:
            '''
            board_size = len(board) - 1
            print("MOVE IS:",move)
            if move in ([0,0],[0,board_size],[board_size,0],[7,7]):
                print("CORNER MOVE MIN FOUND GIMME GIMME",move)
                return -500, move
            '''
            dummy_board = copy.deepcopy(board)
            put(dummy_board, opponent_color, color, move[0], move[1])
            childvalue, childmove = alphabeta(dummy_board, color, opponent_color, depth - 1, alpha, beta, True)
            #print("IN MIN, INVESTIGATING MOVE", move, "AT DEPTH",depth,"VALUE",childvalue)
            if bestvalue >= childvalue:
                bestvalue = childvalue
                bestmove = move
            beta = min(beta, bestvalue)
            if alpha >= beta:
                #print("ALPHA CUTOFF REACHED a:",alpha,"b:",beta)
                break
        #print("MIN: DEPTH",depth,"; BESTVALUE",bestvalue,"; BESTMOVE",bestmove)
        return bestvalue, bestmove


def get_move(board_size, board_state, turn, time_left, opponent_time_left):
    arr_board_size = board_size - 1
    oppcolor = opposite_color(turn)
    movelist = get_valid_moves(board_state, turn, oppcolor)
    #input()
    #print("TURN", get_num_turns(board_state))
    if len(movelist) > 0:
        if time_left < 5000:
            bestval, bestmove = alphabeta(board_state, turn, oppcolor, 4, -9999, 9999, True)
            pass
        elif time_left < 500:
            bestval = "RANDOM"
            bestmove = random.choice(movelist)
            pass
        else:
            bestval, bestmove = alphabeta(board_state, turn, oppcolor, 4, -9999, 9999, True)
        #print("MAIN: BESTVALUE:",bestval,"BESTMOVE",bestmove)

        return bestmove

    else:
        return None
