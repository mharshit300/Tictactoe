board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
winner = None

current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2]+"   1 | 2 | 3 ")
    print(board[3] + " | " + board[4] + " | " + board[5]+"   4 | 5 | 6 ")
    print(board[6] + " | " + board[7] + " | " + board[8]+"   7 | 8 | 9 ")


def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()
        
    if winner=="X" or winner=="0":
        print(winner + " Won. ")
    elif winner==None:
        print("Match tie.")


def handle_turn(player):
    print(player +"'s turn.")
    position = input("choose a position from 1-9:")
    valid = False
    while not valid:
        while position not in["1","2","3","4","5","6","7","8","9"]:
             position=input("choose a position from 1-9:")
        
    
        position = int(position) - 1
        if board[position]=="-":
            valid=True
        else:
            print("you can't go there, Go again")
    board[ position ] = player
    display_board()


def check_if_game_over():
    check_if_winner()
    check_if_tie()


def check_if_winner():
    global winner
    row_winner=check_row()
     
    column_winner=check_columns() 
    
    diagonal_winner=check_diagonals()
    
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return


def check_row():
    global game_still_going
    row_1=board[0]==board[1]==board[2]!="-"
    row_2=board[3]==board[4]==board[5]!="-"
    row_3=board[6]==board[7]==board[8]!="-"
    
    if row_1 or  row_2 or row_3:
          game_still_going=False
    if row_1:
          return board[0]
    elif row_2:
          return board[3]
    elif  row_3:
          return board[6]
    else:
          return None


def check_columns():
    global game_still_going
    column_1=board[0]==board[3]==board[6]!="-"
    column_2=board[1]==board[4]==board[7]!="-"
    column_3=board[2]==board[5]==board[8]!="-"
    
    if column_1 or  column_2 or column_3:
          game_still_going=False
    if column_1:
          
          return board[0]
    elif column_2:
          return board[1]
    elif column_3:
          return board[2]
    else:
          return None

def check_diagonals():
    global game_still_going
    diagonals_1=board[0]==board[4]==board[8] != "-"
    diagonals_2=board[2]==board[4]==board[6] != "-"

    
    
    if diagonals_1 or  diagonals_2:
          game_still_going=False
    if diagonals_1:
          return board[0]
    elif diagonals_2:
          return board[2]
    else:
          return None 

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
        return True
    else:
        return False

def flip_player():
    global current_player
    if current_player=="X":
        current_player="0"
    elif current_player=="0":
        current_player="X"
play_game()
   
