'''
Created on Dec 21, 2018

@author: Robert
'''
from Board.Board import Board
from random import choice
class Game:
    def __init__(self):
        self._boardHuman = Board()
        self._boardComputer = Board()
        self._boardEmpty = Board()
        
    @property    
    def boardHuman(self):
        return self._boardHuman
    
    @property
    def boardComputer(self):
        return self._boardComputer
    
    @property
    def boardEmpty(self):
        return self._boardEmpty
    
    def moveHuman(self,c,l):
        return self._boardComputer.Shot(c, l)
        
    def moveComputer(self,c,l):
        
        return self._boardHuman.Shot(c, l)
    
    def bordered(self):
        self._boardComputer.border()
        self._boardHuman.border()
        self._boardEmpty.border()
        