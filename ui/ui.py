'''
Created on Dec 21, 2018

@author: Robert
'''
from game.GameException import GameException
from Board.Board import Board
from game.game import Game
from random import choice
class ui:
    def __init__(self):
        self._game = Game()
    def readMove(self):
        while True:
            try:
                move = input("Enter The Coordonates: ")
                if move[0] == 'A':
                    c = 1
                elif move[0] =='B':
                    c = 2
                elif move[0] =='C':
                    c = 3
                elif move[0] =='D':
                    c = 4
                elif move[0] =='E':
                    c = 5
                elif move[0] =='F':
                    c = 6
                elif move[0] =='G':
                    c = 7
                elif move[0] =='H':
                    c = 8
                else:
                    raise GameException("Wrong Input")
                
                if int(move[1]) < 1 or int(move[1]) - 1 > 8:
                    raise GameException("Wrong Input")
                return (c, int(move[1]))
            except GameException as ve:
                print(ve)
                
    def readSide(self):
        while True:
            try:
                side = input("Enter the side: ")
                if side != "right" and side !="up" and side !="down" and side !="left":
                    raise GameException("Wrong side input!")
                return side
            except GameException as ve:
                print(ve)
        
    def battleshipPlacement(self,b):
        while True:
            try:
                
                c,l = self.readMove()
                side = self.readSide()
                b.placeShip(c,l,side,3)
                return
            except GameException as ve:
                print(ve)
                
    def cruiserPlacement(self,b):
        while True:
            try:
                c,l = self.readMove()
                side = self.readSide()
                b.placeShip(c,l,side,2)
                return
            except GameException as ve:
                print(ve)
                
    def destroyerPlacement(self,b):
        while True:
            try:
                c,l = self.readMove()
                side = self.readSide()
                b.placeShip(c,l,side,1)
                return
            except GameException as ve:
                print(ve)
                
    def battleshipPlacement2(self,b):
        while True:
            try:
                coord,side = self.randomizeInput(b)
                b.placeShip(coord[0],coord[1],side,3)
                return
            except GameException as ve:
                pass
                
    def cruiserPlacement2(self,b):
        while True:
            try:
                coord,side = self.randomizeInput(b)
                b.placeShip(coord[0],coord[1],side,2)
                return
            except GameException as ve:
                pass
                
    def destroyerPlacement2(self,b):
        while True:
            try:
                coord,side = self.randomizeInput(b)
                b.placeShip(coord[0],coord[1],side,1)
                return
            except GameException as ve:
                pass
                 
                
    def randomizeInput(self,b2):
        coord = b2.getEmptySquares()
        rand = choice(coord)
        lst = ["right","left","up","down"]
        side = choice(lst)
        
        return rand,side
                
    def printBoards(self,b1,b3):
        print("Your Board: ")
        print(b1)
        print('\n')
        print("Computer's Board: ")
        print(b3)
                
    def start(self):
        b1 = self._game.boardHuman
        b2 = self._game.boardComputer
        b3 = self._game.boardEmpty
        self._game.bordered()
        playerTurn = True
        self.printBoards(b1,b3)
        self.battleshipPlacement2(b1)
        self.printBoards(b1,b3)
        self.cruiserPlacement2(b1)
        self.printBoards(b1,b3)
        self.destroyerPlacement2(b1)
        self.battleshipPlacement2(b2)
        self.cruiserPlacement2(b2)
        self.destroyerPlacement2(b2)
        dr = []
        st = []
        sus = []    
        jos = []
        lastHit = ["random",False]
        try:
            while b1.isWon() == False and b2.isWon() == False:
                self.printBoards(b1,b3)
                if playerTurn:
                    
                    c,l = self.readMove()
                    if self._game.moveHuman(c, l) == True:
                        b2.markMove(c, l, True)
                        b3.markMove(c, l, True)
                    else:
                        b2.markMove(c,l,False)
                        b3.markMove(c,l,False)
                        playerTurn = False
                else:
                    
                    
                    
                    if lastHit[1] == False and lastHit[0] != "random":
                        if lastHit[0] == "dr":
                            dr.clear()
                        elif lastHit[0] == "st":
                            st.clear()
                        elif lastHit[0] == "sus":
                            sus.clear()
                        elif lastHit[0] == "jos":
                            jos.clear()
                            
                    elif lastHit[1] == True and lastHit[0] != "random":
                        if lastHit[0] == "dr":
                            sus.clear()
                            jos.clear()
                        elif lastHit[0] == "st":
                            sus.clear()
                            jos.clear()
                        elif lastHit[0] == "sus":
                            dr.clear()
                            st.clear()
                        elif lastHit[0] == "jos":
                            dr.clear()
                            st.clear()
                            
                    
                            
                    if len(dr)!=0:
                        if b1.verif(dr[0][0],dr[0][1]) == True:
                            c = dr[0][0]
                            l = dr[0][1]
                            lastHit[0] = "dr"
                            del dr[0]
                        else:
                            dr.clear()
                    
                    elif len(st)!=0:
                        if b1.verif(st[0][0],st[0][1]) == True:
                            c = st[0][0]
                            l = st[0][1]
                            
                            lastHit[0] = "st"
                            del st[0]
                            
                        else:
                            st.clear()
                    
                    elif len(sus)!=0:
                        if b1.verif(sus[0][0],sus[0][1]) == True:
                            c = sus[0][0]
                            l = sus[0][1]
                            
                            lastHit[0] = "sus"
                            del sus[0]
                            
                        else:
                            sus.clear()
                    
                    elif len(jos)!=0:
                        if b1.verif(jos[0][0],jos[0][1]) == True:
                            c = jos[0][0]
                            l = jos[0][1]
                            lastHit[0] = "jos"
                            
                            del jos [0]
                            
                        else:
                            jos.clear()
                        
                                
                        
                        
                    
                    
                    else:
                        nush = False    
                        while nush == False:  
                            
                            options = b1.getEmptySquares()
                            print(options)
                            coord = choice(options)
                            c = coord[0]
                            l = coord[1]
                            if b1.verif(c, l) == True:
                                nush = True
                                
                            lastHit[0] = "random"
                                
                            
                                
                                
                                
                                
                                
                    if self._game.moveComputer(c,l) == True:
                        b1.markMove(c, l, True)
                        lastHit[1] = True
                        for i in range(8):
                            dr.append([c+i+1,l])
                            
                        for i in range(8):
                            st.append([c-i-1,l])
                            
                        for i in range(8):
                            sus.append([c,l-i-1])
                            
                        for i in range(8):
                            jos.append([c,l+i+1])
                        
                        
                    
                    elif self._game.moveComputer(c,l) == False:
                        b1.markMove(c,l,False)
                        playerTurn = True
                        lastHit[1] = False
                
                
        except GameException as ve:
            print(ve)
        
            
        if playerTurn == True:
            print("You win!")
            
        else:
            print("You lose!")
            
        

ui = ui()
ui.start()
print("Game is over!")
        
        