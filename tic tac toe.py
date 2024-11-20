board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

player1 = 'X'
winner = 0
gamerunning = True

def my_func (board):

    print(board[0] + ' | '+ board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | '+ board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | '+ board[7] + ' | ' + board[8])
my_func(board)


def new_func (board):
    inp = int(input('choose a number btn 1-9 ' ))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = player1

    else:
        print('That spot is filled')
        
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    
    elif  board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif  board[6] == board[7] == board[8] and board[5] != '-':
        winner = board[6]
        return True
    

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    
    elif  board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif  board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True
    
def check_diag(board): 
    global winner

    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    
    elif  board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True
        
def check_tie(board):
    global gamerunning
    if '-' not in board:
        my_func(board)
        print('it is a tie')
        gamerunning = False 

def check_win():
    if check_diag(board) or check_horizontal(board) or check_row(board):
        print(f'the winner is {winner}' )


def switch_player():
    global player1
    if player1 == 'X':
        player1 = 'O'
    else:
        player1 = 'X'



while gamerunning:
    my_func(board)
    new_func(board)
    check_win()
    check_tie(board)
    switch_player()










