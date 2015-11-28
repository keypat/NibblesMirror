class Snake:
    def __init__(self):
        #DIRECTIONS: -1=down,1=up,-2=left,2=right
        self.dir = 1
        # READ AS: points[i] shows [x,y] for ith object
        self.points = [[]]
        for i in range(20):
            self.points.insert(i,([250,10+i*10]))

    def changeDir(self,dir):
        if (self.dir!=dir and self.dir!=-dir): self.dir = dir

   # def grow():
    #    self.points.insert(i+1,([

        
    #def move(self,direction) :
