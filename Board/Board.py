'''
Created on Dec 21, 2018

@author: Robert
'''
from texttable import Texttable
from random import choice
from game.GameException import GameException
class Board:
    def __init__(self):
        self._data = ['  '] * 81
        
    def placeShip(self,c,l,side,k):
        
        if side == "right":
            if c+k >= 9:
                raise GameException("It does not fit")
            
            if self._data[9*l+c] == 1:
                raise GameException("It has a ship already")
            for i in range(k):
                if self._data[9*l+c+i+1] == 1:
                    raise GameException("It does not fit")
            
            self._data[9*l+c] = 1
            for i in range(k):
                self._data[9*l+c+i+1] = 1
            return
        elif side == "left":
            if c-k < 1:
                raise GameException("It does not fit")
            
            if self._data[9*l+c] == 1:
                raise GameException("It has a ship already")
            
            for i in range(k):
                if self._data[9*l+c-i-1] == 1:
                    raise GameException("It does not fit")
                
            self._data[9*l+c] = 1
            for i in range(k):
                self._data[9*l+c-i-1] = 1
            return
        elif side == "up":
            if l-k < 1:
                raise GameException("It does not fit")
            
            if self._data[9*l+c] == 1:
                raise GameException("It has a ship already")
            
            for i in range(k):
                if self._data[9*(l-i-1)+c] == 1:
                    raise GameException("It does not fit")
            
            self._data[9*l+c] = 1
            for i in range(k):
                self._data[9*(l-i-1)+c] = 1
            return
        elif side == "down":
            if l+k >= 9:
                raise GameException("It does not fit")
            
            if self._data[9*l+c] == 1:
                raise GameException("It has a ship already")
            for i in range(k):
                if self._data[9*(l+i+1)+c] ==  1:
                    raise GameException("It does not fit")
            self._data[9*l+c] = 1
            for i in range(k):
                self._data[9*(l+i+1)+c] = 1
            return
        
        
    def getEmptySquares(self):
        res = []
        
        for i in range(81):
            if self._data[i] == '  ' or self._data[i] == 1:   
                res.append( (i % 9, i // 9) )
        return res
                
    def verif(self,c,l):
        if c>=1 and c<9:
            if l>=1 and l<9:
                if self._data[9*l+c] == 1 or self._data[9*l+c] == '  ':
                    return True
        return False
        
    def markMove(self,c,l,aux):
        if aux == True:
            self._data[9*l+c] ="Hit"
        else:
            self._data[9*l+c] ="MISS"

            
        
    def Shot(self,c,l):
        if self._data[9*l + c] == 1 :
            return True
        elif self._data[9*l + c] == '  ':
            return False
        return None
    
    def border(self):
        
        self._data[1] = 'A'
        self._data[2] = 'B'
        self._data[3] = 'C'
        self._data[4] = 'D'
        self._data[5] = 'E'
        self._data[6] = 'F'
        self._data[7] = 'G'
        self._data[8] = 'H'
        for i in range(9):
            self._data[9*i] = i
            
        self._data[0] = ':D'
        self._data[9] = '1'
            
        
    def isWon(self):
        for i in self._data:
            if i == 1:
                return False
        return True
        
        
    def __str__(self):
        t = Texttable()
        
        for i in range(9):
            lst = self._data [9*i: 9*i + 9]
            t.add_row(lst)
        return t.draw()
    
    
