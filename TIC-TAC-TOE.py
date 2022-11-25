import time     #the time module is to give the game a realistic aspect, as if the computer is thinking of its next move
from random import randrange

def display(board):
    for i in range(13):
        if i==0 or i%4==0:
            print("+","+","+","+",sep=("-------"))
        elif i==2:
            print("|",board[0][0],"|",board[0][1],"|",board[0][2],"|",sep=("   "))
        elif i==6:
            print("|",board[1][0],"|",board[1][1],"|",board[1][2],"|",sep=("   "))
        elif i==10:
            print("|",board[2][0],"|",board[2][1],"|",board[2][2],"|",sep=("   "))
        else:
            print("|","|","|","|",sep=("       "))
    # this function accepts one parameter containing the board's current status
    # and prints it out to the console.
    

def move(board):
    empty=False
    move=int(input("enter your move: "))
    while True:
        if move not in range(1,10):
            move=int(input("invalid move! Try again: "))
        else: break
    while not empty:
        if move in range(1,4):
            i=0
        elif move in range(4,7):
            i=1
        else:
            i=2
        if move%3==0:
            j=2
        elif move==1 or move==4 or move==7:
            j=0
        else:
            j=1
        if (i,j) in free_fields(board):
            board[i][j]="O"
            empty=True
        else:
            move=int(input("field occupied! choose another move: "))
    time.sleep(2)
    display(board)
    # the function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    


def free_fields(board):
    liste=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["O","X"]:
                liste+=(i,j),
    return liste
    # this function browses the board and builds a list of all the free cells; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    

def winner(board, sign):
    s1=[]
    s2=[]
    s3=[]
    for i in range (1,4):
        if board[i-1]==sign:
            return True
        s2.append(board[-i][-i])
        s3.append(board[i-1][3-i])
    for i in range(3):
        s1.clear()
        for j in range(3):
            s1.append(board[j][i-1])
        if s1==sign:
            return True
    if s2==sign or s3==sign:
        return True
    return board
    # this function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def cpu_move(board):
    valid=False
    move=randrange(1,10)
    print(move)
    while not valid:
        if move in range(1,4):
            i=0
        elif move in range(4,7):
            i=1
        else:
            i=2
        if move%3==0:
            j=2
        elif move==1 or move==4 or move==7:
            j=0
        else:
            j=1
        if (i,j) in free_fields(board):
            board[i][j]="X"
            valid=True
        else:
            print("field occupied! Try another move: ")
            move=randrange(1,10)
            print(move)
    time.sleep(2)
    display(board)
    # The function draws the computer's move and updates the board.
    

if __name__ == "__main__":
    board=[[i for i in range(1,4)],[i for i in range(4,7)],[i for i in range (7,10)]]       #initialize the board
    board[1][1]="X"     #the central cell is the first computer move
    display(board)      #show the board
    while True:
        move(board)
        sign=["O","O","O"]
        if winner(board, sign)==True:       #check if the "O"s make a line
            print("You win!".center(len("you win!")+17))        #output the message in the center
            break
        if free_fields(board)==[]:      #check if there are no more empty cells
            print("Draw!".center(len("draw")+17))
            break
        cpu_move(board)
        sign=["X","X","X"]
        if winner(board,sign)==True:        #check if the "X"s make a line
            print("you lose!".center(len("you lose!")+17))
            break
        if free_fields(board)==[]:
            print("Draw!".center(len("draw")+17))
            break
