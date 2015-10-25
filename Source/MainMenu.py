import PlayMap
import pygame
import GameOver


class MainMenu :
    MENU = ['menu','game','gameOver']

    def __init__(self) :
        #What stage of the interface the game is on
        self.state = MENU[0]
        #Size of the window
        self.size = [550,500]
        updateState()

    #Add ValueError exception
    #change value of self.state
    def changeState(self,newState) :
        self.state = newState
        if self.state==MENU[0]:
            
        if self.state==MENU[1]:
            gameMap = PlayMap()
        if self.state==MENU[2]:
            gameOver = GameOver(gameMap.score
        
    #call necessary functions based on current state
    def updateState(self) :
        if self.state==MENU[0] :

        if self.state==MENU[1] :
            gameMap.updateState()
            return gameMap.getCurrentState()
        if self.state==MENU[2] :
            gameOver.updateState(gameMap.score)
            return gameOver.getCurrentState()
            
        
