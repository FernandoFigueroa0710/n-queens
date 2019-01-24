import copy

def take_input():

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

     
