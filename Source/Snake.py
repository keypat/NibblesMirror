import pygame

class Snake:

    # x,y coordinate of the head of the snake
    def __init__(self,x,y):
        self.life = true 
        #DIRECTIONS: -1=down,1=up,-2=left,2=right
        self.dir = 1
        # READ AS: points[i] shows [x,y] for ith object
        self.points = []

        #make a vertical snake 20 points long
        for i in range(20):
            self.points.insert(i,pygame.Rect(x,y+i*10,10,10))

    # updates direction if it is valid
    def changeDir(self,dir):
        
        if (self.dir!=dir and self.dir!=-dir): self.dir = dir

    # increase size of the snake
    def grow(self):
        #appends a duplicate of the last point of snake to the points list
        self.points.insert(len(self.points)+1,self.points[-1])

    # Moves snake in current direction
    def move(self) :
        #remove tail of the snake
        self.points.pop[-1]

        #based on the direction, add a new point to the head
        if self.dir==1:
            self.points.insert(0,pygame.Rect(self.points[0].left,self.points[0].top+10,10,10))
        if self.dir==-1:
            self.points.insert(0,pygame.Rect(self.points[0].left,self.points[0].top-10,10,10))
        if self.dir==2:
            self.points.insert(0,pygame.Rect(self.points[0].left+10,self.points[0].top,10,10))
        if self.dir==-2:
            self.points.insert(0,pygame.Rect(self.points[0].left-10,self.points[0].top,10,10))
    
