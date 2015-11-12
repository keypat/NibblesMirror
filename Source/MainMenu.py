from PlayMap import *
import pygame
from GameOver import *
from GamePause import *

"""
Main Menu Class encapsulates the 'window' of the game
as the logic(backend) and decides what to send to Controller.py to display
"""

class MainMenu :
    """
    MainMenu has state variables:
    gameMap: PlayMap object
    gameOver: GameOver object
    state: string
    startGameButton: pygame.Rect object
    exitGameButton: pygame.Rect object

    Assumptions: __init__() is called before any other access program
    
    """
    #MENU = ['menu','game','gameOver']

    def __init__(self) :
        """
        Constructor for MainMenu class
        Transition: initialized to main menu state
        exception: none
        """
        print "MainMenu constructor ran"
        #self.MENU = ['menu','game','gameOver']
        self.gameMap = PlayMap()
        self.gameOver = 'defaultVALUE'
        self.gamePause = 'defaultVALUE'
        self.pauseStatus = False
        #What stage of the interface the game is on
        self.state = 'menu'
        
        #Size of the window
        #self.size = [550,500]
        self.startGameButton = pygame.Rect(50,200,200,100)
        self.exitGameButton = pygame.Rect(300,200,200,100)
        
        self.updateState()

    #Add ValueError exception
    #change value of self.state
    def changeState(self,newState) :
        """
        function to change the current state of the main menu
        Transition: self.state is updated to new state
        exception: none
        input: newState - string value of new state
        output: none
        """

        self.state = newState
        if self.state=='game':
            if not(self.pauseStatus) :
                self.gameMap = PlayMap()
        if self.state=='gameOver':
            self.gameOver = GameOver(self.gameMap.score)
        if self.state=='gamePause':
            self.pauseStatus = True
            self.gamePause = GamePause(self.gameMap.score)
        
    #call necessary functions based on current state
    def updateState(self) :
        """
        function to return which objects to display on GUI (current state of game)
        Transition: an array of objects to display on the screen is returned
        exception: none
        input: none
        output: an array of objects (pygame)
        """
        #print "MainMenu.updateState ran"
        if self.state=='menu' :
            return [self.startGameButton,self.exitGameButton]
        if self.state=='game' :
            self.gameMap.updateState()
            return self.gameMap.getCurrentState()     
        if self.state=='gameOver' :
            self.gameOver.updateState(self.gameMap.score)
            return self.gameOver.getCurrentState()
        if self.state=='gamePause' :
            self.gamePause.updateState(self.gameMap.score)
            return self.gamePause.getCurrentState()
    
    


            
        
