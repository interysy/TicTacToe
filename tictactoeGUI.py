# A tictactoe mini-project with a Tkinter interface


import random
import tkinter as tk
from tkinter.constants import DISABLED
    
class Game(): 
     
    def __init__(self,symbol1,symbol2,nOfPlayers,board):    
        self.cTurn = 1
        self.currentPlayer = 1
        self.symbol1 = symbol1 
        self.symbol2 = symbol2  
        self.c1 = 'green' 
        self.c2 = 'red'
        self.nOfPlayers = nOfPlayers 
        self.board = board      # board is now a dictionary    
      
    def turn(self,btn,lbl):  

        if self.cTurn%2 == 0: 
            symbol = self.symbol2  
            p = 1
            c = self.c2 
        else: 
            symbol = self.symbol1    
            c = self.c1   
            p = 2
             

        if self.checkFree(btn):
            self.board[btn].config(text = symbol,fg = c)    
            
            self.checkWin(self.board,'d',lbl)
             
            if self.nOfPlayers == 3: 
                self.compTurn(lbl)    
                self.cTurn += 2 
            else: 
                self.cTurn += 1     
                lbl['text'] = 'Player {p} : '.format(p=p)
            return

             
    # checking if a winning combination has been found or board is full   
    def checkWin(self,board,type,lbl = None): 
        winCombinations  = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]  

        if type == 'd':  
            for element in winCombinations: 
                if board[element[0]]["text"] == board[element[1]]["text"] and board[element[1]]["text"] ==board[element[2]]["text"]: 
                    lbl['text'] = 'The winner is ' + board[element[0]]['text']  
                    for elt in self.board.values():   
                        elt.config(state = DISABLED)
                    return 
        else: 
            for element in winCombinations: 
                if board[element[0]] == board[element[1]] and board[element[1]] == board[element[2]]:  
                    return True
                 
        if type == 'd':
            if not any(False if (elt["text"] == self.symbol1 or elt["text"]== self.symbol2) else True for elt in board.values()):   
                lbl['text'] ='It is a DRAW' 
                return  
        else: 
            if not any(False if (elt == self.symbol1 or elt == self.symbol2) else True for elt in board): 
                return None
    
        return False
         
    def checkFree(self,btn):  
        if self.board[btn]['text'] != self.symbol1 and self.board[btn]['text'] != self.symbol2:  
            return True  
        return False 
    

    def compTurn(self,lbl):  # needs finishing
        posCor = [int(elt['text']) for elt in self.board.values() if elt['text']!= self.symbol1 and elt['text'] != self.symbol2] 
  
        val  = [elt['text'] for elt in self.board.values()] 
         
        boolean = False
            # check for winning moves
        for idx,v in enumerate(val):  
            for symbol in [self.symbol1,self.symbol2]:    
                if v != self.symbol1 and v!= self.symbol2: 
                    arr = val[:] 
                    arr[idx] = symbol
                    boolean = self.checkWin(arr,'e')
                    if boolean: 
                        self.board[idx].config(text = self.symbol2,fg = self.c2)   
                        self.checkWin(self.board,'d',lbl)
                        return
             
        if self.board[4]['text'] == '4': 
            self.board[4].config(text = self.symbol2,fg = self.c2)
            return
        
         
            # place edge 
        edges = [elt for elt in posCor if elt%2 == 1]

        if len(edges) > 0:  
            edge = random.choice(edges) 
            self.board[edge].config(text = self.symbol2,fg = self.c2) 
            return 
            

            
        # place corner or middle 
        corners = [elt for elt in posCor if elt%2 ==0 ] 
        if len(corners) > 0: 
            corner = random.choice(corners) 
            self.board[corner].config(text = self.symbol2,fg = self.c2)
            return 

    

  
# TKINTER CLASS 
class InitWindow(): 
     
    def __init__(self,root):  
        self.root = root
        self.root.title("TicTacToe") 
        self.mainFrame = tk.Frame(root) 
        self.mainFrame.pack(pady = 100,padx  = 100) 

    

        # radio button for choosing amount of players
        self.playVar = tk.IntVar(None,3) 
        
        self.playRb1 = tk.Radiobutton(self.mainFrame,text = "Single Player",variable = self.playVar,value = 3) 
        self.playRb1.pack(anchor ='w')  
        self.playRb2 = tk.Radiobutton(self.mainFrame,text = '2 Player',variable = self.playVar,value = 2) 
        self.playRb2.pack(anchor = 'w') 
        
    
    
        # setting characters (2 labels and 2 entries)
        self.choiceFrame = tk.Frame(self.mainFrame)
        self.symbolChLbl = tk.Label(self.choiceFrame,text = 'Pick Player 1 symbol:')  
        self.symbolChLbl.grid(row = 0, column=0,sticky='w') 

        self.symbolChEnt = tk.Entry(self.choiceFrame)  
        self.symbolChEnt.grid(row = 0,column = 1 )  

        self.symbolChLbl2 = tk.Label(self.choiceFrame,text = 'Pick the symbol for player 2:') 
        self.symbolChLbl2.grid(row = 1,column  = 0, sticky='w')  
        self.symbolChEnt2 = tk.Entry(self.choiceFrame)  
        self.symbolChEnt2.grid(row = 1,column = 1)
        self.choiceFrame.pack()
    

        # confirming settings
        self.btn = tk.Button(self.mainFrame,text = 'Confirm settings',command = lambda:self.confirmSettings(root),bg = 'green')  
        self.btn.pack()
        self.btn2 = tk.Button(self.mainFrame,text = 'Quit',command = root.destroy,bg = 'red') 
        self.btn2.pack()
        
        self.root.mainloop() 
 

  
    def mainWindow(self):    
        self.lblFrame = tk.Frame(self.root) 
        self.lblFrame.pack() 
        self.slbl = tk.Label(self.lblFrame,text = "Let's Play") 
        self.slbl.pack(padx = 10,pady = 20) 
         

        
        self.secondMainFrame = tk.Frame(self.root) 
        self.secondMainFrame.pack(pady = 30,padx = 50)   
        self.board = {}  
         
        game = Game(self.symbol1,self.symbol2,self.nOfPlayers,self.board)

        
        for i in range(3): 
            for j in range(3):  
                self.board[i*3+j] = tk.Button(self.secondMainFrame,text = str(i*3+j),command = lambda btn = i*3+j :game.turn(btn,self.slbl))
                self.board[i*3+j].grid(row = i,column = j,padx = 5,pady = 5)

                   
        self.resBtn = tk.Button(self.secondMainFrame,text = 'Restart',command= lambda :restart(self.root),bg = 'orange').grid(row = 7,column = 0,columnspan=3) 
        self.quitBtn = tk.Button(self.secondMainFrame,text = 'Quit',command = self.root.destroy,bg = 'red').grid(row = 8,column = 0,columnspan = 3)
          

    def confirmSettings(self,root):  
        ready = False 
        self.symbol1 = self.symbolChEnt.get() 
        self.symbol2 = self.symbolChEnt2.get() 
        self.nOfPlayers = self.playVar.get()
        print(self.nOfPlayers,self.symbol1,self.symbol2) 
         
        if self.symbol1 != self.symbol2 and (0 < len(self.symbol1) < 2 and 0 < len(self.symbol2) < 2) and (self.symbol1 not in '12345678' and self.symbol2 not in '12345678'): 
            ready = True
         
        if ready:
        # delete last window - create new one 
            for elt in root.winfo_children(): 
                elt.destroy()  
            self.mainWindow()
     


def restart(cl): 
    cl.destroy()  
    root = tk.Tk()
    InitWindow(root)

# starter
if __name__ == "__main__": 
    root = tk.Tk()   
    window = InitWindow(root)   

     