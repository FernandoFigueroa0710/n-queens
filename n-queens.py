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
