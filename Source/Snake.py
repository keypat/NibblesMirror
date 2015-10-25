class Snake:
    def __init__(self):
        #DIRECTIONS: -1=down,1=up,-2=left,2=right
        self.dir = 1
        # READ AS: points[i] shows [x,y] for ith object
        self.points = [[]]

        #make a vertical snake 20 points long
        for i in range(20):
            self.points.insert(i,([250,10+i*10]))

    # updates direction if it is valid
    def changeDir(self,dir):
        
        if (self.dir!=dir and self.dir!=-dir): self.dir = dir

    # increase size of the snake
    def grow():
        #appends a duplicate of the last point of snake to the points list
        self.points.insert(len(self.points)+1,self.points[-1])

    # Moves snake in current direction
    def move(self) :
        #remove tail of the snake
        self.points.pop[-1]

        #based on the direction, add a new point to the head
        if self.dir==1:
            self.points.insert(0,[self.points[0][0],self.points[0][1]+10])
        if self.dir==-1:
            self.points.insert(0,[self.points[0][0],self.points[0][1]-10])
        if self.dir==2:
            self.points.insert(0,[self.points[0][0]+10,self.points[0][1]])
        if self.dir==-2:
            self.points.insert(0,[self.points[0][0]-10,self.points[0][1]])
    
    #checks if snake has eaten itself
    def didSnakeEatSelf(self) :
        for i in range(len(self.points)) :
            if self.points[i]==self.points[0]: return true
        return false
