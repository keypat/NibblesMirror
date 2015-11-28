
"""
The Controller Module
-The controller.py Module contains the GUI of the game and manages user input
 and output

"""

        
import sys, pygame
from MainMenu import *
from PlayMap import *
from Snake import *
from Food import *
from pygame.locals import KEYDOWN, K_ESCAPE, K_SPACE, K_UP, K_RIGHT, K_DOWN, K_LEFT, QUIT, K_1, K_2, K_3, K_m, K_a, K_w, K_s, K_d, K_r, K_q
from itertools import count


"""
initialize state variables : size, clock, screen, fonts, mainMenu
"""

size=x,y=550,500

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
fontButton = pygame.font.Font(None,25)
fontScore = pygame.font.Font(None,23)

mainMenu = MainMenu()
gameSpeeds = [5,10,15]
currentSpeed = 5
white, black , red, green, yellow, gray= (255, 255, 255), (0, 0, 0), (255,0,0), (0,130,0) , (255,255,0), (200,200,200)

##############################################################################
##########################-----GUI-----#######################################
##############################################################################

def updateGUIDisplay() :
    """
    Function Description: This function is called by the main code to update the GUI on the display.
    input:none
    output:none
    exceptions:none
    """

    screen.fill(black)
    obj=mainMenu.updateState()

    if mainMenu.state=='menu' :
        pygame.draw.rect(screen,white,obj[0])
        pygame.draw.rect(screen,white,obj[1])
        pygame.draw.rect(screen,green,obj[2])
        pygame.draw.rect(screen,yellow,obj[3])
        pygame.draw.rect(screen,red,obj[4])
        
        surface = fontButton.render('Play Game [SPACE]', True, red)
        surface2 = fontButton.render('Quit Game [q]', True, red)
        surface3 = fontButton.render('Difficulty: ',True,white)
        surface4 = fontButton.render('1',True,black)
        surface5 = fontButton.render('2',True,black)
        surface6 = fontButton.render('3',True,black)
        
        screen.blit(surface, (50, 250))
        screen.blit(surface2, (300, 250))
        screen.blit(surface3, (50,300))
        screen.blit(surface4, (100,400))
        screen.blit(surface5, (200,400))
        screen.blit(surface6, (300,400))
        
        pygame.display.flip()

            
    if mainMenu.state=='game':
        if obj==-1 :
                print "score,",mainMenu.gameMap.score
                mainMenu.changeState('gameOver')


    if mainMenu.state=='game' :
        for i in range(3) :
            if i==0:
                for j in range(len(obj[0])-1):
                    if mainMenu.gameMap.powerUpStatus and j==0 : pygame.draw.rect(screen,red,obj[0][j])
                    else : pygame.draw.rect(screen,white,obj[0][j])
            if i==1 : pygame.draw.rect(screen,white,obj[1])
            if i==2 : pygame.draw.rect(screen,gray,obj[2])
        surface = fontScore.render('SCORE:  '+str(mainMenu.gameMap.score), True, green)
        screen.blit(surface, (225, 0))   

        pygame.display.flip()

    if mainMenu.state=='gameOver' :
        obj = mainMenu.updateState()
        surface = fontButton.render('Game Over!       SCORE: '+str(obj[0]),True,red)
        screen.blit(surface,(150,100))

        pygame.draw.rect(screen,white,obj[1])
        surface2 = fontButton.render('Retry [SPACE]', True, black)
        screen.blit(surface2,(100,250))

        pygame.draw.rect(screen,white,obj[3])
        surface3 = fontButton.render('Quit [q]', True, black)
        screen.blit(surface3,(200,400))

        pygame.draw.rect(screen,white,obj[2])
        surface4 = fontButton.render('Menu [m]', True, black)
        screen.blit(surface4,(300,250)) 
            
        pygame.display.flip()


    if mainMenu.state=='gamePause' :
        obj = mainMenu.updateState()
        surface = fontButton.render('Game Paused!       SCORE: '+str(obj[0]),True,red)
        screen.blit(surface,(150,100))

        pygame.draw.rect(screen,white,obj[2])
        surface2 = fontButton.render('Menu [m]', True, black)
        screen.blit(surface2,(300,250))
        
        pygame.draw.rect(screen,white,obj[1])
        surface3 = fontButton.render('Resume [SPACE]', True, black)
        screen.blit(surface3,(100,250))

        pygame.draw.rect(screen,white,obj[3])
        surface4 = fontButton.render('Quit [q]', True, black)
        screen.blit(surface4,(200,400)) 
            
        pygame.display.flip()            


##############################################################################
########################-----CONTROLLER-----##################################
##############################################################################
        
def eventChecker() :
    """
    This method is the controller for our software model. This method
    manages the behaviour changes of the system based on input from hardware.
    """
    
    changedDir = False
    global currentSpeed
    # Loops through the list of events that occured
    for event in pygame.event.get() :
            if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

            # Controlling for when the mouse is unclicked
            elif event.type == pygame.MOUSEBUTTONUP :
                pos = pygame.mouse.get_pos()
                 
                if mainMenu.state=='menu' and mainMenu.startGameButton.collidepoint(pos) :
                        mainMenu.changeState('game')
                if mainMenu.state=='menu' and mainMenu.exitGameButton.collidepoint(pos) :
                        pygame.event.post(pygame.event.Event(QUIT))
                if mainMenu.state=='menu' and mainMenu.diff0Button.collidepoint(pos) :
                        mainMenu.gameMap.setDiff(0)
                        currentSpeed = gameSpeeds[0]
                if mainMenu.state=='menu' and mainMenu.diff1Button.collidepoint(pos) :
                        mainMenu.gameMap.setDiff(1)
                        currentSpeed = gameSpeeds[1]
                if mainMenu.state=='menu' and mainMenu.diff2Button.collidepoint(pos) :
                        mainMenu.gameMap.setDiff(2)
                        currentSpeed = gameSpeeds[2]
                        
                if (mainMenu.state=='gameOver' or mainMenu.state=='gamePause') and mainMenu.gameOver.retryButton.collidepoint(pos) :
                        mainMenu.changeState('game')
                if mainMenu.state=='gameOver' or mainMenu.state=='gamePause' and mainMenu.gameOver.exitButton.collidepoint(pos) :
                        pygame.event.post(pygame.event.Event(QUIT))          
                if mainMenu.state=='gameOver' or mainMenu.state=='gamePause' and mainMenu.gamePause.menuButton.collidepoint(pos) :
                        mainMenu.changeState('menu')

            # Controlling for when a keyboard key is pressed                
            elif event.type == KEYDOWN :
                
                if mainMenu.state=='menu' :
                    if event.key == K_1 : currentSpeed = gameSpeeds[0]
                    if event.key == K_2 : currentSpeed = gameSpeeds[1]
                    if event.key == K_3 : currentSpeed = gameSpeeds[2]
                    
                if mainMenu.state=='game' and not(changedDir):
                        if event.key == K_UP or event.key == K_w:
                            mainMenu.gameMap.snake.changeDir(1)
                        elif event.key == K_RIGHT or event.key == K_d:
                            mainMenu.gameMap.snake.changeDir(2)
                        elif event.key == K_DOWN or event.key == K_s:
                            mainMenu.gameMap.snake.changeDir(-1)
                        elif event.key == K_LEFT or event.key == K_a:
                            mainMenu.gameMap.snake.changeDir(-2)
                        changedDir = True
                        
                if event.key==K_ESCAPE and mainMenu.state=='game' : mainMenu.changeState('gamePause')    
                if event.key == K_SPACE and mainMenu.state!='game' : mainMenu.changeState('game')
                if event.key == K_m and mainMenu.state!='game' : mainMenu.changeState('menu')
                if event.key == K_q : pygame.event.post(pygame.event.Event(QUIT))
    return 1

##############################################################################
##############################################################################

# Main loop to run the game
def main() :
        while 1:
                if mainMenu.state!='game' : clock.tick(30)
                else: clock.tick(min(currentSpeed + (mainMenu.gameMap.score / 4), 30))
                    
                if eventChecker() == 0 :
                        return
                updateGUIDisplay()

main()
