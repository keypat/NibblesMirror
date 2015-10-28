from PlayMap import *
import pygame
from GameOver import *


class MainMenu :
    #MENU = ['menu','game','gameOver']

    def __init__(self) :
        print "MainMenu constructor ran"
        #self.MENU = ['menu','game','gameOver']
        self.gameMap = PlayMap()
        self.gameOver = 'defaultVALUE'
        #What stage of the interface the game is on
        self.state = 'menu'
        #Size of the window
        self.size = [550,500]
        self.startGameButton = pygame.Rect(150,200,100,150)
        self.exitGameButton = pygame.Rect(300,200,100,150)
        
        self.updateState()

    #Add ValueError exception
    #change value of self.state
    def changeState(self,newState) :
        print "MainMenu.changeState ran"
        self.state = newState
        if self.state=='game':
            self.gameMap = PlayMap()
            print"PLAYMAP MADE"
        if self.state=='gameOver':
            self.gameOver = GameOver(gameMap.score)
        
    #call necessary functions based on current state
    def updateState(self) :
        print "MainMenu.updateState ran"
        if self.state=='menu' :
            return [self.startGameButton,self.exitGameButton]
        if self.state=='game' :
            self.gameMap.updateState()
            #for i in self.gameMap.getCurrentState()[0]:
            #    print i
            return self.gameMap.getCurrentState()
            
        if self.state=='gameOver' :
            self.gameOver.updateState(gameMap.score)
            return self.gameOver.getCurrentState()
    
    


            
        
