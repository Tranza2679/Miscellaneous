#Tic tac toe

import random 
numbers_avaliable = [1,2,3,4,5,6,7,8,9]
turns = 0
user_input = input("Will you play X or O?").strip().title()
board = ["-","-","-","-","-","-","-","-","-"]
game_end = False 

def game_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

def change_board(num, turn):
    num = num - 1
    if num == 0:
        board[0] = turn    
    elif num == 1:
        board[1] = turn
    elif num == 2:
        board[2] = turn
    elif num == 3:
        board[3] = turn
    elif num == 4:
        board[4] = turn
    elif num == 5:
        board[5] = turn
    if num == 6:
        board[6] = turn
    if num == 7:
        board[7] = turn
    elif num == 8:
        board[8] = turn
    
    
    while game_end == False: 
        if turns % 2 == 1 and user_input == "X":
            print(game_board())
            player_choice = input("Choose a number from 1 to 9:")
            if player_choice >=1 or player_choice <= 9:
                change_board(player_choice, user_input)
            

    

