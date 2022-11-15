# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

class TicTacToe:

    def __init__(self):
        """
        Set up a game by initializing board, player type, Player, Winner, Count
        """
        self.board = [
            [None,None,None],
            [None,None,None],
            [None,None,None]
        ]
        self.player_type = {'O':True, 'X': True}
        self.player = 'O'
        self.winner=None
        self.count = 0

    def single_player(self):
        self.player_type['X'] = False
        return self.player_type

    def get_winner(self,board):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        #Row winner reader
        for row in range (0,2):
            if board[row][0] == board[row][1] == board[row][2] and board[row][0]!=None:
                return board[row][0]
        #Column winner reader
        for col in range (0,2):    
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != None:
                return board[0][col]
        #Diagonal winner reader
        if board[0][0] == board[1][1]==board[2][2] and board[0][0] != None:
            return board[0][0]
        elif board[0][2] == board [1][1]==board[2][0] and board[0][2] != None:
            return board[0][2]
        #If there is no winner, return None
        else:
            return None

    def other_player(self,player):
        """Given the character for a player, returns the other player."""
        if player=='O':
            return 'X'
        else:
            return 'O'
