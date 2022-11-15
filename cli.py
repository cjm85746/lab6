# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import TicTacToe
from random import randint

"""
Args: 
    board: tic-tac-toe board
    winner: check if there is winner, if there is a winner break the loop (true/false)
    player: contain the players
    count: check if the board is full (count >8 - board full)

Return:
until there is a winner or draw, the code keep shows and updates the tic-tac-toe so that two different players can play the game

"""

if __name__ == '__main__':
    ttt= TicTacToe()

    #let user choose the play type
    print ('Choose a player number (1,2), Single Player(1), Multi Player(2)')
    n_player = int(input())

    if n_player ==1:
        print ('You are O')
        ttt.player_type = ttt.single_player()
    else:
        print ('O play first, and X play next')

    #Play game
    while ttt.winner == None:

        print("TODO: take a turn!")
        for i in ttt.board:
            print (i)

        if ttt.player_type[ttt.player] == True:

            print("input a row number (1-3)")
            a = int(input ())
            print("input a column number (1-3)")
            b=int (input())

            if b<0 or b>=4 or a<0 or a>=4:
                while b>0 and b<4 and a>0 and a<4:
                    print ("Choose a number between 1-3")
                    print("input a row number (1-3)")
                    a= int (input ())
                    print("input a column number (1-3)")
                    b = int (input ())


            if ttt.board[a-1][b-1] != None:
                while ttt.board[a-1][b-1]!= None:
                    print ("Choose an empty slot")
                    print ("input a row number (1-3)")
                    a= int (input())              
                    print ("input a column number (1-3)")
                    b=int (input ())

                    if b<0 or b>=4 or a<0 or a>=4:
                        while b>0 and b<4 and a>0 and a<4:
                            print ("Choose a number between 1-3")
                            print("input a row number (1-3)")
                            a= int (input ())
                            print("input a column number (1-3)")
                            b = int (input ())


        if ttt.player_type[ttt.player]==False:
            a= int(randint (1,3))
            b = int(randint (1,3))
            if ttt.board[a-1][b-1] != None:
                while ttt.board[a-1][b-1]!= None:
                    a= int(input())
                    b=int(input())
            ttt.player_type=ttt.single_player()
        # if an user choose the slot that the other user already occupied, the game require the user to pick another slot.

        ttt.board [a-1][b-1] = ttt.player
        ttt.count +=1

        #Check if there is an winner
        if ttt.get_winner(ttt.board) != None:
            print ("The winner is", ttt.player)
            break
        # if the board is full and no winner the game is draw.
        if ttt.count ==9:
            print ("Draw")
            break

        ttt.player = ttt.other_player(ttt.player)
        print ("Now it is", ttt.player, "'s turn")


