#Tic tac toe

import random 
user_input = input("Will you play X or O?")
one = "_"
two = "_"
three = "_"
four = "_"
five = "_"
six ="_"
seven = "_"
eight = "_"
nine = "_"
def board():
    print(f"  |  |  ")
    print(f"_")
    print(f"__|__|__")
    print(f"  |  | ")
first_turn = int(input("Where are you going to place X/O?"))