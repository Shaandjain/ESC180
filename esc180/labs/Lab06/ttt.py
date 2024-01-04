'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
    
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    
    print_board_and_legend(board)

#PART A
def square_num_to_coord(square_num):
    row = (square_num - 1) // 3
    col = (square_num - 1) % 3
    return [row, col]

#PART B
def put_in_board(board, mark, square_num):
    coord = square_num_to_coord(square_num)
    board[coord[0]][coord[1]] = mark

#PART C
def play(board):
    for i in range(9):
        if i % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        square_num = int(input("Enter a square number: "))
        put_in_board(board, mark, square_num)
        print_board_and_legend(board)
        print("\n\n")

#PROBLEM 5
#PART A
def get_free_squares(board):
    free_squares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                free_squares.append([i, j])
    return free_squares

#PART B
import random
def make_random_move(board, mark):
    free_squares = get_free_squares(board)
    random_square = free_squares[int(len(free_squares) * random.random())]
    board[random_square[0]][random_square[1]] = mark

#PART C
'''Now use make_random_move() in order to have the computer play against the user.'''
def play_random(board):
    for i in range(9):
        if i % 2 == 0:
            mark = "X"
            square_num = int(input("Enter a square number: "))
            put_in_board(board, mark, square_num)
        else:
            mark = "O"
            make_random_move(board, mark)
        print_board_and_legend(board)
        print("\n\n")


#PROBLEM 6
#PART A
def is_row_all_marks(board, row_i, mark):
    for i in range(len(board[row_i])):
        if board[row_i][i] != mark: #iterate through 
            return False
    return True

#PART B
def is_col_all_marks(board, col_i, mark):
    for i in range(len(board)):
        if board[i][col_i] != mark:
            return False
    return True

#CHECK FOR ALL DIAGONALS (WIN CONDITION)
def diagonal_all_marks(board, mark):
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark: #all coordinates of first diagonal
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark: #all coordinates of second diagonal
        return True
    return False


#PART C
def is_win(board, mark):
    for i in range(len(board)):
        if is_row_all_marks(board, i, mark) or is_col_all_marks(board, i, mark) or diagonal_all_marks(board, mark):
            return True
    return False
#if the row, column, or diagonal is full of a mark, win is true

#PART D
def play_with_win(board):
    for i in range(9):
        if i % 2 == 0:
            mark = "X"
            square_num = int(input("Enter a square number: "))
            put_in_board(board, mark, square_num)
        else:
            mark = "O"
            make_smart_move(board, mark)
        print_board_and_legend(board)
        print("\n\n")
        if is_win(board, mark):
            print(mark + " wins!")
            break
    if not is_win(board, mark):
        print("It's a tie!")
    

def make_smart_move(board, mark):
    free_squares = get_free_squares(board)
    opponent_mark = "X"
    mark = "O"

    for square in free_squares:
        board[square[0]][square[1]] = mark
        if is_win(board, mark): #check for is_win
            return 
        board[square[0]][square[1]] = " " 

    for square in free_squares:
        board[square[0]][square[1]] = opponent_mark
        if is_win(board, opponent_mark): #check if user has is_win
            board[square[0]][square[1]] = mark 
            return  
        board[square[0]][square[1]] = " "  

    # If there are no winning or blocking moves, make a random move
    make_random_move(board, mark)



if __name__ == "__main__":
    board = make_empty_board()
    play_with_win(board)
    