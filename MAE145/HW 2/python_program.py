#A16479821 #PID

# import all modules here if you need any

import numpy as np
import random

# your file should always start from definition of functions 

def create_board():
    """ Add illustrations here, if needed 

   (0,0)| (0,1)| (0,2)
    ____|______|____
   (1,0)| (1,1)| (1,2)                 Here is the coordinate system due to array indexing
    ____|______|____
   (2,0)| (2,1)| (2,2)
        |      |
"""
    # define variables you need
    
    board = np.array([[0,0,0],[0,0,0],[0,0,0]])#numpy array to represent a 3 x 3 table, each element
            #should be set as an integer equal to zero
    
    return board


def place(board , player, position):
    """ Add illustrations here, if needed """
    if player != 1 and player != 2:
        print('player must be 1 or 2')
        return
    elif type(board) != type(np.array([])):
        print('Board object must be an array.')
        return
    elif type(position) != tuple and len(position) != 2:
        print('Position must be in coordinate form: (x,y)')
        return
    else:
        if board[position] == 0:
            board[position] = player
    
    # Operations
    
    return board #(same data type as input board)

def possibilities(board):

    ind = []

#operations

    a = np.where(board == 0)
    for n in range(0,len(a[1])):
        ind.append((a[0][n],a[1][n]))


    
    
    return ind #each element in this list should be tuple or it is
               #empty (return [])

def random_place(board, player):  # Important: you need to use a random seed of 1 to show results
    random.seed(1)                # for truly random results comment this line out
    
    # operations
    
    empty = possibilities(board)

    choice = random.choice(empty)

    place(board,player,choice)

    return board

def repeat(n):                     # Important: you should enter 1 to initialize the random seed
                                   #  for truly random results comment this line out     
    board = create_board()
    random.seed(1)
    # Operations
    player = 1

    for i in range(0,n):
        board = random_place(board,player)
        if player == 1:
            player =2
        elif player == 2:
            player = 1
        board = random_place(board,player)


    return board
    
if __name__ == '__main__':
    """ 
    This is the place where you can test your function. 
    You can define variables, feed them into your function and check the output   
    """
    
    board = create_board()
    
    board = place(board, 1, (0,0))  
    
    empty_positions = possibilities(board)
    
    board = random_place(board, 1)
    
    n =  3  # an integer n < 5 since there are only 9 cells in the board and two players in turn place the mark
                  # repeat n times
    board = repeat(n)
    