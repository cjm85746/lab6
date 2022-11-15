

import unittest
import logic


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
    

if __name__ == '__main__':
    unittest.main()
