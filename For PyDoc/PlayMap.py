from Snake import *
import pygame
from Food import *
from PowerUp import *

class PlayMap:

        def __init__(self):
                print "PlayMap constructor ran"
                self.height = 500
                self.width = 550
                self.snake = Snake(250, 290) # starting coord of snake
                self.food = Food()
                self.powerUp = PowerUp()

                self.powerUpStatus = True
                self.gameStatsBar = pygame.Rect(0,0,550,20)
                self.powerUpIndicator = pygame.Rect(10,0,10,10)
                self.score = len(self.snake.points)  



        def updateState(self):
                print "PlayMap.updateState ran"
                self.snake.move()
                # deal with food
                
                head = self.snake.points[0]
                if head == self.food.position:
                        self.snake.grow()
                        self.food = Food()
                        self.score += 1


        def isSnakeDead(self):
                print "PlayMap.isSnakeDead ran"
                status = self.didSnakeHitBorder() or self.didSnakeHitSelf()
                return status

        def getCurrentState(self):
                print "PlayMap.getCurrentState ran"
                if self.isSnakeDead():
                        return -1
                if self.powerUpStatus:
                        return [self.snake.points, self.food.position, self.gameStatsBar, self.powerUpIndicator, self.powerUp.position]
                if self.powerUpStatus==False:
                        return [self.snake.points, self.food.position, self.gameStatsBar, -1, -1]


        def didSnakeHitBorder(self):
                print "PlayMap.didSnakeHitBorder ran"
                head = self.snake.points[0]
                if head.left < 0: return True
                if head.left >= self.width: return True
                if head.top-20 < 0: return True
                if head.top >= self.height: return True
                return False


        def didSnakeHitSelf(self):
                print "PlayMap.didSnakeHitSelf ran"
                print self.snake.points
                temp = len(self.snake.points)
                i = 1
                while i < temp :
                    print i
                    if self.snake.points[0]==self.snake.points[i] :
                        if self.powerUpStatus :
                                self.powerUpStatus=False
                                self.snake.remove(i)
                        else : return True
                    i+=1
                    temp = len(self.snake.points)

                return False
