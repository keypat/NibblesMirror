
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
from pygame.locals import KEYDOWN, K_ESCAPE, K_SPACE, K_UP, K_RIGHT, K_DOWN, K_LEFT, QUIT, K_m, K_a, K_w, K_s, K_d, K_r, K_q
from itertools import count


"""
initialize state variables : size, clock, screen, fonts, mainMenu
"""

size=x,y=550,500

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None,25)
font2 = pygame.font.Font(None,20)

mainMenu = MainMenu()
foreground, background , menuCol= (255, 255, 255), (0, 0, 0), (255,0,0)

def updateGUIDisplay() :
    """
    Function Description: This function is called by the main code to update the GUI on the display.
    input:none
    output:none
    exceptions:none
    """

    screen.fill(background)
    obj=mainMenu.updateState()

    if mainMenu.state=='menu' :
        for rect in obj:
            pygame.draw.rect(screen,foreground,rect)
        surface = font.render('Play Game [SPACE]', True, menuCol)
        surface2 = font.render('Quit Game [q]', True, menuCol)
        screen.blit(surface, (50, 250))
        screen.blit(surface2, (300, 250))
        pygame.display.flip()

            
    if mainMenu.state=='game':
        if obj==-1 :
                print "score,",mainMenu.gameMap.score
                mainMenu.changeState('gameOver')


    if mainMenu.state=='game' :
        for i in range(3) :
            if i==0:
                for j in range(len(obj[0])-1):
                    if mainMenu.gameMap.powerUpStatus and j==0 : pygame.draw.rect(screen,menuCol,obj[0][j])
                    else : pygame.draw.rect(screen,foreground,obj[0][j])
            if i==1 : pygame.draw.rect(screen,foreground,obj[1])
            if i==2 : pygame.draw.rect(screen,foreground,obj[2])
            #if i==3 and obj[i]!=-1 : pygame.draw.rect(screen,menuCol,obj[3])
            #if i==4 and obj[i]!=-1 : pygame.draw.rect(screen,menuCol,obj[4])
        surface = font2.render('SCORE:  '+str(mainMenu.gameMap.score), True, menuCol)
        screen.blit(surface, (200, 0))   

        pygame.display.flip()

    if mainMenu.state=='gameOver' :
        obj = mainMenu.updateState()
        surface = font.render('Game Over!       SCORE: '+str(obj[0]),True,menuCol)
        screen.blit(surface,(150,400))

        pygame.draw.rect(screen,foreground,obj[1])
        surface2 = font.render('Retry [SPACE]', True, background)
        screen.blit(surface2,(100,250))

        pygame.draw.rect(screen,foreground,obj[2])
        surface3 = font.render('Quit [q]', True, background)
        screen.blit(surface3,(300,250)) 
            
        pygame.display.flip()


    if mainMenu.state=='gamePause' :
        obj = mainMenu.updateState()
        surface = font.render('Game Paused!       SCORE: '+str(obj[0]),True,menuCol)
        screen.blit(surface,(150,100))

        pygame.draw.rect(screen,foreground,obj[2])
        surface2 = font.render('Menu [m]', True, background)
        screen.blit(surface2,(300,250))
        
        pygame.draw.rect(screen,foreground,obj[1])
        surface3 = font.render('Resume [SPACE]', True, background)
        screen.blit(surface3,(100,250))

        pygame.draw.rect(screen,foreground,obj[3])
        surface4 = font.render('Quit [q]', True, background)
        screen.blit(surface4,(200,400)) 
            
        pygame.display.flip()            



        
def eventChecker() :
    changedDir = False
    for event in pygame.event.get() :
            if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP :
                pos = pygame.mouse.get_pos()
                if mainMenu.state=='menu' and mainMenu.startGameButton.collidepoint(pos) :
                        mainMenu.changeState('game')
                if mainMenu.state=='menu' and mainMenu.exitGameButton.collidepoint(pos) :
                        pygame.event.post(pygame.event.Event(QUIT))
                if mainMenu.state=='gameOver' and mainMenu.gameOver.retryButton.collidepoint(pos) :
                        mainMenu.changeState('game')
                if mainMenu.state=='gameOver' and mainMenu.gameOver.exitButton.collidepoint(pos) :
                        pygame.event.post(pygame.event.Event(QUIT))
                if mainMenu.state=='gamePause' and mainMenu.gamePause.menuButton.collidepoint(pos) :
                        mainMenu.changeState('menu')
                if mainMenu.state=='gamePause' and mainMenu.gamePause.exitButton.collidepoint(pos) :
                        pygame.event.post(pygame.event.Event(QUIT))
                if mainMenu.state=='gamePause' and mainMenu.gamePause.resumeButton.collidepoint(pos) :
                        mainMenu.changeState('game')
                            
            elif event.type == KEYDOWN :

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
                if event.key==K_ESCAPE and mainMenu.state=='game' :
                        mainMenu.changeState('gamePause')
                        print 'gamePaused'
                if event.key == K_SPACE and mainMenu.state!='game' : mainMenu.changeState('game')
                if event.key == K_m and mainMenu.state=='gamePause' : mainMenu.changeState('menu')
                #if event.key == K_ESCAPE and mainMenu.state=='gamePause' : mainMenu.changeState('game')
                if event.key == K_q:
                    pygame.event.post(pygame.event.Event(QUIT))
    return 1


def main() :
        while 1:
                if mainMenu.state!='game' : clock.tick(30)
                else: clock.tick(min(5 + (mainMenu.gameMap.score / 4), 30))

                if eventChecker() == 0 :
                        return
                updateGUIDisplay()

main()
