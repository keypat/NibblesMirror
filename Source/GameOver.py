import pygame

class GameOver:

    def __init__(self,score) :
        self.score = score
        self.retryButton = pygame.Rect(100,200,150,100)
        self.exitButton = pygame.Rect(300,200,150,100)
        
    def updateState(self,score) :
        self.score=score
        
    def getCurrentState(self) :
        return [self.score,self.retryButton,self.exitButton]
