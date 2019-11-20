#!/usr/bin/python

from __future__ import division
import  sys

the_board = {}
chess_board_max = []

pieces = ['knight','queen','rook']
board = {}


def convert(array):

    value =''

    if ( 1 <= array[0]  <= 8 ):
        value = str(chr(array[0] + 96))
    else:
        value = int(ord(array[0]) - 96)        

    return [ value , int(array[1]) ]

def merge_values(val1, val2):
    if val1 is None:
        return [val2]
    elif val2 is None:
        return [val1]
    else:
        return [val1, val2]
   


def queen_moves(pos):

    bishop = bishop_moves(pos)
    rook   = rook_moves(pos)

    position = {
        key: merge_values(bishop.get(key), rook.get(key))
        for key in set(bishop).union(rook)
    }


    return position


def bishop_moves(pos):

    moves = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
    board = []
    position = {}
    board = convert(pos[0])

    for x in range( 0 , 8 ):
        for move in moves:
            x_axis = int(board[0]) + int(move[0]) * x
            y_axis = int(board[1]) + int(move[1]) * x
            if ( 1 <=  x_axis   <= 8 )  and ( 1 <=  y_axis  <= 8 ) :
                results = convert(( x_axis , y_axis ))
                position[results[0]+str(results[1])] = 1

    return position

def rook_moves(pos):

    board = []
    position = {}
    board = convert(pos[0])

    for x in range( 1 , 9 ):       
        results = convert(( int(x)   ,  board[1] ))
        position[str(results[0])+str(results[1])] = 1 
        results = convert(( board[0]   ,  int(x) ))
        position[results[0]+str(results[1])] = 1
        
 
    return position

def knight_moves(pos):

    board = []
    position = {}
    moves = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    board = convert(pos[0])
    
    for move in moves:
        x_axis = int(board[0]) + int(move[0]) 
        y_axis = int(board[1]) + int(move[1])
        if ( 1 <=  x_axis   <= 7 )  and ( 1 <=  y_axis     <= 7 ) :
            results = convert(( x_axis   ,  y_axis ))
            position[str(results[0])+str(results[1])] = 1

    return  position   
    

def main():

    for x in range( 1 , 8 ):
        for y in range( 1 , 8 ):
            results = convert(( x , y ))
            board[results[0]+str(results[1])] = 1

    arguments = len(sys.argv) - 1

    if arguments == 2 and sys.argv[1].lower() in pieces  and sys.argv[2].lower() in board.keys() :
        
        chess_piece         = sys.argv[1]
        starting_position   =  [( sys.argv[2][0] , sys.argv[2][1] )]

        if chess_piece == "queen": 
            rs = queen_moves(starting_position)
            print(sorted(rs.keys()))
        elif chess_piece == "rook": 
            rs = rook_moves(starting_position)
            print(sorted(rs.keys()))
        elif chess_piece == "knight":          
            rs = knight_moves(starting_position)
            print(sorted(rs.keys()))
    else:
        print ("Script require two parameters with the first parameter either queen, rook or knight and an appriopriate board position")    


 

    
    

if __name__ == '__main__':
    main()
   