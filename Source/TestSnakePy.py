import pygame
import unittest
import copy
from Snake import *

class TestSnakePy(unittest.TestCase) :

    def setUp(self) :
        global sConstructor
        global grownSnakes
        global changeDirVars
        global removeIndexes
        sConstructor = Snake()
        changeDirVars = [-1,1,-2,2]
##        
        UP = Snake()
        UP.changeDir(2)
        UP.move()
        UP.changeDir(1)
        DOWN = Snake()
        RIGHT = Snake()
        RIGHT.changeDir(2)
        LEFT = Snake()
        LEFT.changeDir(-2)
        
        directionSnakes = [DOWN,UP,LEFT,RIGHT]
##
        grownSnakes = []
        for i in range(4) : grownSnakes.insert(i,directionSnakes[i].grow())
            
        removeIndexes = [5,10,15]
        pass
        

    def test_constructorTests(self) :
        global sConstructor
        self.assertEquals(str(Snake()),str(sConstructor))

    def test_changeDirTests(self) :
        # i : directionSnakes, j : changeDirVars
        UP = Snake()
        UP.changeDir(2)
        UP.move()
        UP.changeDir(1)
        DOWN = Snake()
        RIGHT = Snake()
        RIGHT.changeDir(2)
        LEFT = Snake()
        LEFT.changeDir(-2)
                
        directionSnakes = [DOWN,UP,LEFT,RIGHT]
        for i in range(4) :
            
            for j in range(4) :
                UP2 = Snake()
                UP2.changeDir(2)
                UP2.move()
                UP2.changeDir(1)
                DOWN2 = Snake()
                RIGHT2 = Snake()
                RIGHT2.changeDir(2)
                LEFT2 = Snake()
                LEFT2.changeDir(-2)
                
                directionSnakes2 = [DOWN2,UP2,LEFT2,RIGHT2]

                directionSnakes2[i].changeDir(changeDirVars[j])
                obj = directionSnakes2[i].direction
                if i<2 :
                    if j<2 : self.assertEquals(directionSnakes[i].direction,obj)
                    else : self.assertEquals(changeDirVars[j],obj)
                else :
                    if j<2 : self.assertEquals(changeDirVars[j],obj)
                    else : self.assertEquals(directionSnakes[i].direction,obj)

        
    
    def test_remove(self) :
        
        for i in removeIndexes :
            x = Snake()
            x.remove(i)
            self.assertEquals(i+1,len(x.points))
        
            
            


if __name__ == '__main__' :
    unittest.main(verbosity=2)
