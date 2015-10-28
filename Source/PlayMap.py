from Snake import *
import pygame
from Food import *

class PlayMap:

        def __init__(self):
                print "PlayMap constructor ran"
                self.height = 500
                self.width = 550
                self.snake = Snake(250, 290) # starting coord of snake
                self.food = Food()

                self.score = len(self.snake.points)  



        def updateState(self):
                print "PlayMap.updateState ran"
                self.snake.move()
                # deal with food
                
                head = self.snake.points[0]
                if head == self.food:
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
                else:
                        return [self.snake.points, self.food.position]

        def didSnakeHitBorder(self):
                print "PlayMap.didSnakeHitBorder ran"
                head = self.snake.points[0]
                if head.left < 0: return True
                if head.left >= self.width: return True
                if head.top < 0: return True
                if head.top >= self.height: return True
                return False


        def didSnakeHitSelf(self):
                print "PlayMap.didSnakeHitSelf ran"
                for i in range(1, len(self.snake.points)):
                    if self.snake.points[i]==self.snake.points[0]: return True
                return False
