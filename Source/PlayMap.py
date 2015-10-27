from Snake import *
import pygame
from Food import *

class PlayMap:

        def __init__(self):
                self.height = 500
                self.width = 550
                self.snake = Snake(250, 10) # starting coord of snake
                self.food = Food()

                self.score = len(self.snake.points)  

        def getCurrentState(self):
                if isSnakeDead:
                        return -1
                else:
                        return [snake.points, food.position]

        def updateState(self):
                snake.move()
                # deal with food
                
                head = snake.points[0]
                if head == food:
                        snake.grow()
                        self.food = Food()


        def isSnakeDead(self):
                status = didSnakeHitBoarder() or didSnakeHitSelf()
                return status

        def didSnakeHitBoarder(self):
                head = self.snake.points[0]
                if head.left < 0: return True
                if head.left >= width: return True
                if head.top < 0: return True
                if head.top >= height: return True
                return False


        def didSnakeHitSelf(self):
                for i in range(1, len(snake.points)):
                    if snake.points[i]==snake.points[0]: return True
                return False
