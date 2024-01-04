#returns true iff the square is a valid sqare in the Gomoku game board
def is_sq_in_board(board, y, x):
    return y >= 0 and y < len(board) and x >= 0 and x < len(board[0])



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def is_sequence_complete(board, col, y_start, x_start, length, d_y, d_x):
    y = y_start 
    x = x_start
    for i in range(length):
        if not is_sq_in_board(board, y, x):
            return False
        if board[y][x] != col:
            return False
        y += d_y
        x += d_x
    if board[y_start-d_y][x_start-d_x] == col:
        return False
    if board[y][x] == col:
        return False
    return True