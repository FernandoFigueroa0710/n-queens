import copy

def take_input():
    """Accept the size of the chessboard"""
    while True:
        try:
            size = int(input('What is the size of the chessboard? n= \n'))
            if size == 1:
                print('Trivial solution, choose a board of at least 4')
            if size <= 3:
                print('Enter a value that is >= 4')
                continue
            return size
        except ValueError:
            print('Invalid value entered. Enter again')

def get_board(size):
    """Returns a n by n board"""
    board = [0]*size
    for ix in range = [0]*size
            board[ix] = [0]*size
        return board

def print_solutions(solutions, size):
    """Prints solutions"""
    for sol in solutions:
        for row in sol:
            print(row)
        print()

def is_safe(board, row, col, size):
    """Check if it's safe to place a queen at board[x][y]"""

    #check row on left side
    for iy in range(col):
        if board[row][iy] == 1:
            return False

    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1
            return False
        jx+=1
        jy-=1
    return True

def solve(board, col, size):
    """Use backtracking to fins all the solutions"""
    #base case
    if col >= size:
        return

    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = 1
            if col == size-1:
                add_solution(board)
                board[i][col] = 0
                return
            solve(board, col+1, size)
            #backtrack
            board[i][col] = 0

        
