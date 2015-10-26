import Snake
import Food

class PlayMap:

	def __init__(self):
		self.height = 500
		self.width = 550


		self.snake = Snake(x, y) # starting coord of snake
		self.food = Food()

		self.score = len(snake.points)
		

	def getCurrentState(self):
		if isSnakeDead: 
			return -1
		else: 
			return objArr = [snake, food]

	def updateState():
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
		head = snake.points[0]
    	if head.left < 0: return True
    	elif head.left >= width: return True
    	elif head.top < 0: return True
    	elif head.top >= height: return True
    	else: return False


    def didSnakeHitSelf(self):
        for i in range(1, len(snake.points)):
            if snake.points[i]==snake.points[0]: return True
        return False