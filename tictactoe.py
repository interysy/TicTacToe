# A simple tictactoe game for practice 

 
import random

    
# creating the board
def createBoard(): 
    board = ['0','1','2','3','4','5','6','7','8']  
    return board      
 
  


# placing symbols
def changeBoard(board,where,symbol1,symbol2):   
    try: 
        where = int(where) 
    except ValueError: 
        print('Invalid input') 
        return board,False

    if 0<=where<9 and (board[where] != symbol1 and board[where] != symbol2): 
        board[where] = symbol1 
        return board,True 
    else:  
        print('The space is taken or non-exitant \n')
        return board,False 

         




# checking if a winning combination has been found or board is full   
def checkWin(board,symbol1,symbol2): 
    winCombinations  = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]  
         
    for element in winCombinations: 
        if board[element[0]] == board[element[1]] and board[element[1]] == board[element[2]]:  
            return True 
             
    if not any(False if (elt == symbol1 or elt== symbol2) else True for elt in board):  
        print('Board is full')  
        print('It is a DRAW between the 2 players')
        return True 
 
    return False
    # check for board fullness  
    # check for symbol wins (only calling player)
    
      

       

    

# displaying the board in the command line
def displayBoard(board): 
    print() 
    print(board[0] + " | " + board[1] + " | " + board[2])  
    print('-'.ljust(3) + '-'.center(3) + '-'.rjust(3))
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print('-'.ljust(3) + '-'.center(3) + '-'.rjust(3))
    print(board[6] + " | " + board[7] + " | " + board[8]) 
    print() 
      

       
        
def comTurn(board,symbol1,symbol2): 
    print('Computer Turn') 
    posCor = [int(elt) for elt in board if elt!= symbol1 and elt != symbol2]

    # check for winning moves, either to block or win 
    # place edge 
    # place corner 

       
    # symbol1 = 'O' 
    # symbol2 = 'X' 

    # check for winning moves
    for idx in posCor: 
        for symbol in [symbol1,symbol2]:  
            boardCp = board[:]  
            boardCp[idx] = symbol
            boolean = checkWin(boardCp,symbol2,symbol1)  
            if boolean: 
                board[idx] = symbol1
                return board  
                 

    # if possible take the middle spot, makes it harder for player to win            
    if board[4] == '4': 
        board[4] = symbol1 
        return board
                     
    # place edge 
    edges = [elt for elt in posCor if elt%2 == 1]

    if len(edges) > 0:  
        edge = random.choice(edges) 
        board[edge] = symbol1 
        return board  
         

          
    # place corner or middle 
    corners = [elt for elt in posCor if elt%2 ==0 ] 
    if len(corners) > 0: 
        corner = random.choice(corners) 
        board[corner] = symbol1 
        return board
     
      

 
# the turn
def turn(player,symbol1,symbol2,board):   
    if player == 3: 
        comTurn(board,symbol1,symbol2) 
    else:
        boolean = False 
        while not boolean: 
            print("Player " + str(player) + " Turn")  
            where = input('Please enter the number where you would like to place your symbol \n') 
            board,boolean = changeBoard(board,where,symbol1,symbol2) 
         
    return board



# the main function- ie mainloop 
def main(): 
 
  
    # variables
    board = createBoard()
    quit = False 
    symbol1 = "X"  
    symbol2 = "O" 
    nOfPlayers = 0 
     

    # welcome messages + questions
    print("Welcome, type in quit at any time to terminate the game \n") 
      
    correctSet = False 
     
  
    while not(0<int(nOfPlayers)<3):  
        nOfPlayers = input("Please enter the amount of players \n") 
        try: 
            nOfPlayers = int(nOfPlayers.strip()) 
        except ValueError: 
            nOfPlayers = 0   
        

    

        

     
    # setting up second player or computer
    if nOfPlayers == 1: 
        p2 = 3 
    else: 
        p2 = 2
    displayBoard(board) 
      
       
    # game mainloop
    while not quit:  
         

        # player one turn   
        board = turn(1,symbol1,symbol2,board)
        displayBoard(board)
        # check if player one won  
        quit = checkWin(board,symbol1,symbol2)   
         
        
        if quit == False:      # need quit otherwise the second player or PC will get indefinite turns after player1 wins
            board = turn(p2,symbol2,symbol1,board) 
            displayBoard(board) 
            quit = checkWin(board,symbol2,symbol1)  
            if quit: 
                print('Player 2 ({symbol}) is the winner'.format(symbol  = symbol2)) 
                
        else: 
            print("The Player ({symbol}) is the winner".format(symbol = symbol1))
 
        # work on the termination bug
        # player two turn  
    
    notAnswered = True
    while notAnswered:
        playAgain = input('Would you like to play again Y/N? \n') 
        if playAgain.strip().upper() == 'Y':   
            print()
            notAnswered = False 
            main()  
        elif playAgain.strip().upper() == 'N': 
            notAnswered = False 

 
# starter
if __name__ == "__main__":  
    main() 

     




# def window(): 
#     root = tk.Tk() 
#     root.title("Tic-Tac-Toe") 
    