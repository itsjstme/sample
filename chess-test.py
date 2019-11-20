
#!/usr/bin/python

import unittest
from chess import queen_moves , rook_moves , knight_moves

class TestSum(unittest.TestCase):

    def test_queen_moves(self):
        position = "a1"
        starting_position =  [( position[0] , position[1] )]
        moves = queen_moves(starting_position)
        moves = sorted(moves.keys()) 
        self.assertEqual( moves , ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'c1', 'c3', 'd1', 'd4', 'e1', 'e5', 'f1', 'f6', 'g1', 'g7', 'h1', 'h8']  , "Should be equal")

    def test_rook_moves(self):
        position = "a1"
        starting_position =  [( position[0] , position[1] )]
        moves = rook_moves(starting_position)
        moves = sorted(moves.keys())
        self.assertEqual( moves , ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'] , "Should be equal")

    def test_knight_moves(self):
        position = "a1"
        starting_position =  [( position[0] , position[1] )]
        moves = knight_moves(starting_position)
        moves = sorted(moves.keys())
        self.assertEqual( moves , ['b3', 'c2'] , "Should be equal")  


if __name__ == '__main__':
    unittest.main()