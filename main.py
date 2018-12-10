import random
import cornersandedges


BLACK = 'B'
WHITE = 'W'
SPACE = ' '

def init_board(size=8):
    board = []
    for i in range(size):
        board.append([SPACE for j in range(size)])

    board[size//2][size//2] = BLACK
    board[size//2 - 1][size//2 - 1] = BLACK
    board[size//2][size//2 - 1] = WHITE
    board[size//2 - 1][size//2] = WHITE

    return board

def print_board(board):
    print('  ', end='')
    for idx in range(len(board)):
        print(idx, end=' ')

    print('\n -', end='')

    for idx in range(len(board)):
        print('--', end='')

    print()

    for idx, row in enumerate(board):
        print(idx, end='|')
        for col in row:
            print(col + '|', end='')
        print(idx)

    print(' -', end='')

    for idx in range(len(board)):
        print('--', end='')

    print('\n  ', end='')
    for idx in range(len(board)):
        print(idx, end=' ')

    print()

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
                    list_of_moves.append((i,j))

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

def do_turn(board, color, opp_color):
    #get input
    print("%s's turn..." % (color))
    moves = get_valid_moves(board, color, opp_color)
    print(get_valid_moves(board, color, opp_color))
    if color == 0:
        #do human move
        row = input("input row: ")
        col = input("input col: ")
        if row == '':
            row = 0
        if col == '':
            col = 0

        row = int(row)
        col = int(col)
    else:
        #do AI move
        move = random.choice(moves)
        row = move[0]
        col = move[1]


    boardlen = len(board)
    while row < 0 or col < 0 or \
            row >= boardlen or col >= boardlen or \
            not put(board, color, opp_color, row, col):
        print("BAD MOVE!")
        row = int(input("input row: "))
        col = int(input("input col: "))

def score(board, color):
    tally = 0
    for row in board:
        for col in row:
            if col == color:
                tally += 1
    return tally

def play(board, turn=WHITE, opp_color=BLACK):
    while has_valid_move(board, turn, opp_color) or has_valid_move(board, opp_color, turn):
        if has_valid_move(board, turn, opp_color):
            do_turn(board, turn, opp_color)
        else:
            print("%s has no valid moves! Sorry!" % (turn))
        
        print_board(board)

        opp_color, turn = turn, opp_color

    print("GAME OVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print_board(board)

    white_score = score(board, WHITE)
    black_score = score(board, BLACK)
    print("White:", white_score)
    print("Black:", black_score)
    if white_score > black_score:
        print("WHITE WINS!!!!!!")
    elif white_score < black_score:
        print("BLACK WINS!!!!!!")
    else:
        print("ITS A TIE!!!!!!!")




def main():
    print("Welcome to Othello!")

#    board = init_board(8)


    board = [
    ["W", " ", " ", " ", " ", " ", " ", " "],
    [" ", "W", " ", " ", " ", " ", "W", "B"],
    [" ", " ", "W", "W", " ", "W", "W", "B"],
    [" ", " ", "W", "W", "W", "W", "W", "B"],
    [" ", "B", "B", "B", "B", "B", "B", "B"],
    ["B", " ", "B", " ", "B", " ", "B", " "],
    [" ", "B", "B", "B", "B", "B", " ", "B"],
    ["W", " ", "B", " ", "B", " ", "B", " "]
    ]
    print_board(board)
    print( get_valid_moves(board, BLACK, WHITE))


    print(cornersandedges.get_move(len(board), board, BLACK, 30000, 30000))


#    play(board)

main()
