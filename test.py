

import unittest
import logic
from random import randint

class TestLogic(unittest.TestCase):

    def setUp(self):
        self.ttt = logic.TicTacToe()

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(self.ttt.get_winner(board), 'X')

    def test_single_player(self):
        player = 'X'
        self.assertEqual(self.ttt.single_player(),{'O':True, 'X': False})

    def test_other_player(self):
        player = 'O'
        self.assertEqual(self.ttt.other_player(player), 'X')

    def test_constraint(self):
        a=1
        b=1
        self.assertEqual(self.ttt.constraint(a,b), (a,b))
    

if __name__ == '__main__':
    unittest.main()
