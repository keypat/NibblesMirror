
class GameOver:

    def __init__(self,score) :
        self.score = score
        
    def updateState(self,score) :
        self.score=score
        
    def getCurrentState(self) :
        return [pygame.Rect(100,200,300,200),self.score]
