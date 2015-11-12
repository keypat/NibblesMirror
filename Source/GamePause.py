import pygame

class GamePause:
    """
        GameOver class to emulate the game state 'game paused'
        state variables:
            score:integer
            menuButton: pygame.Rect object
            retryButton: pygame.Rect object
            exitButton: pygame.Rect object
    """
    def __init__(self,score) :
        """
            constructor for GamePause.py
            
            Transition: initializes a pause screen
            input:none
            output:none
        """
        self.score = score
        self.exitButton = pygame.Rect(200,350,150,100)
        self.resumeButton = pygame.Rect(100,200,150,100)
        self.menuButton = pygame.Rect(300,200,150,100)
        
    def updateState(self,score) :
        """
            function to update the score at the time of game pause
            
            Transition: changes the current score at game pause time
            input:integer value for score
            output:none
        """
        self.score=score
        
    def getCurrentState(self) :
        """
            function to return the current game state
            
            Transition: returns the objects to display on the main screen
            input:none
            output:an array of objects
        """
        return [self.score,self.resumeButton,self.menuButton,self.exitButton]
