#Tic Tac Toe Game Python
 
board = [' ' for x in range(10)]

def printBoard():
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(' '+board[1],board[2],board[3],sep=" | ",end="\n---+---+---\n")
    print(' '+board[4],board[5],board[6],sep=" | ",end="\n---+---+---\n")
    print(' '+board[7],board[8],board[9],sep=" | ")
    
  
 
def insertBoard(letter, pos):
    global board
    board[pos] = letter
 
def spaceIsFree(pos):
    return board[pos] == ' '
 
def isWinner(bo, letter):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and 
    return ((bo[7] == letter and bo[8] == letter and bo[9] == letter) or # across the top
    (bo[4] == letter and bo[5] == letter and bo[6] == letter) or # across the middle
    (bo[1] == letter and bo[2] == letter and bo[3] == letter) or # across the bottom
    (bo[7] == letter and bo[4] == letter and bo[1] == letter) or # down the left side
    (bo[8] == letter and bo[5] == letter and bo[2] == letter) or # down the middle
    (bo[9] == letter and bo[6] == letter and bo[3] == letter) or # down the right side
    (bo[7] == letter and bo[5] == letter and bo[3] == letter) or # diagonal
    (bo[9] == letter and bo[5] == letter and bo[1] == letter)) # diagonal
 
 
def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move  = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard('X', move)
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
       
 
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
   
 
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
   
    #Check for possible winning move to take or to block opponents winning move
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
 
 
    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
   
    #Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move
 
    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
 
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
 
    return move
 
 
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
 

 
def mainGame():
    #Main game loop
    print("""Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical).
    The board has positions 1-9 starting at the top left.""")
    printBoard()
 
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print("'O' wins this time...")
            break
 
       
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Game is a Tie! No more spaces left to move.')
            else:
                insertBoard('O', move)
                print("Computer placed an 'O' in position", move, ':')
                printBoard()
        else:
            print("'X' wins, good job!")
            break
 
 
    if isBoardFull(board):
        print('Game is a tie! No more spaces left to move.')
 
mainGame()
 
while True:
    answer = input('Do you want to play again? (Y/N) :')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
"""OUTPUT:
Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical).
    The board has positions 1-9 starting at the top left.
   |   |
---+---+---
   |   |
---+---+---
   |   |
Please select a position to place an 'X' (1-9): 1
 X |   |  
---+---+---
   |   |
---+---+---
   |   |  
Computer placed an 'O' in position 7 :
 X |   |
---+---+---
   |   |  
---+---+---
 O |   |
Please select a position to place an 'X' (1-9): 5
 X |   |  
---+---+---
   | X |
---+---+---
 O |   |  
Computer placed an 'O' in position 9 :
 X |   |
---+---+---
   | X |
---+---+---
 O |   | O
Please select a position to place an 'X' (1-9): 8
 X |   |  
---+---+---
   | X |
---+---+---
 O | X | O
Computer placed an 'O' in position 2 :
 X | O |
---+---+---
   | X |
---+---+---
 O | X | O
Please select a position to place an 'X' (1-9): 6
 X | O |  
---+---+---
   | X | X
---+---+---
 O | X | O
Computer placed an 'O' in position 4 :
 X | O |
---+---+---
 O | X | X
---+---+---
 O | X | O
Please select a position to place an 'X' (1-9): 3
 X | O | X
---+---+---
 O | X | X
---+---+---
 O | X | O
Game is a Tie! No more spaces left to move.
Game is a tie! No more spaces left to move.
Do you want to play again? (Y/N) :N
"""