import pygame

class Snake:

    # x,y coordinate of the head of the snake
    def __init__(self,x,y):
        self.life = True 
        #DIRECTIONS: -1=down,1=up,-2=left,2=right
        self.direction = -1
        # READ AS: points[i] shows [x,y] for ith object
        self.points = []

        #make a vertical snake 20 points long
        for i in range(20):
            self.points.insert(i,pygame.Rect(x,y-i*10,10,10))
            print "in Snake.py: ",self.points[i]

    # updates direction if it is valid
    def changeDir(self,direction):
        print "Snake.changeDir ran"
        if (self.direction!=direction and self.direction!=-direction): self.direction = direction

    # increase size of the snake
    def grow(self):
        print "Snake.grow ran"
        #appends a duplicate of the last point of snake to the points list
        self.points.insert(len(self.points)+1,self.points[-1])

    # Moves snake in current direction
    def move(self) :
        print "Snake.move ran"
        #remove tail of the snake
        self.points.pop(-1)

        #based on the direction, add a new point to the head
        if self.direction==1:
            self.points.insert(0,pygame.Rect(self.points[0].left,self.points[0].top-10,10,10))
        if self.direction==-1:
            self.points.insert(0,pygame.Rect(self.points[0].left,self.points[0].top+10,10,10))
        if self.direction==2:
            self.points.insert(0,pygame.Rect(self.points[0].left+10,self.points[0].top,10,10))
        if self.direction==-2:
            self.points.insert(0,pygame.Rect(self.points[0].left-10,self.points[0].top,10,10))
    
    # remove all points after passed index
    def remove(self,index) :
        i = len(self.points)
        while len(self.points) != index+1 : self.points.pop()
            
                        
