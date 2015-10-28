##import pygame
##from pygame.locals import KEYDOWN, K_UP, K_RIGHT, K_DOWN, K_LEFT, QUIT, K_r, K_q
##
##event = pygame.event.poll()
##

##
##    if dead:
##        continue

        
import sys, pygame
from MainMenu import *
from PlayMap import *
from Snake import *
from Food import *
from pygame.locals import KEYDOWN, K_UP, K_RIGHT, K_DOWN, K_LEFT, QUIT, K_r, K_q
from itertools import count

size=x,y=550,500

pygame.init()
print"wassup"
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
print "brooo"
font = pygame.font.Font(None,25)

mainMenu = MainMenu()
print"menucrreated"
foreground, background = (255, 255, 255), (0, 0, 0)

screen.fill(background)
obj=mainMenu.updateState()
if mainMenu.state=='menu':
        print"MenuMADE"
        for rect in obj:
            pygame.draw.rect(screen,foreground,rect)
            surface = font.render('Play Game', True, background)
            screen.blit(surface, (150, 250))
        pygame.display.flip()

        
for counter in count():
    #if mainMenu.state=='game' : clock.tick(min(5 + (mainMenu.gameMap.score / 4), 30))
    clock.tick(min(5, 30))

    event = pygame.event.poll()

    if event.type == QUIT:
                pygame.quit()
                sys.exit()

            ## CHANGE TO variable for coordinates
    elif event.type == pygame.MOUSEBUTTONUP :
        pos = pygame.mouse.get_pos()
        if mainMenu.state=='menu' and mainMenu.startGameButton.collidepoint(pos) :
                mainMenu.changeState('game')
        if mainMenu.state=='menu' and mainMenu.exitGameButton.collidepoint(pos) :
                pygame.event.post(pygame.event.Event(QUIT))
                    
    elif event.type == KEYDOWN and mainMenu.state=='game':

        if event.key == K_UP:
            mainMenu.gameMap.snake.changeDir(1)
        elif event.key == K_RIGHT:
            mainMenu.gameMap.snake.changeDir(2)
        elif event.key == K_DOWN:
            mainMenu.gameMap.snake.changeDir(-1)
        elif event.key == K_LEFT:
            mainMenu.gameMap.snake.changeDir(-2)
                    
                #elif event.key == K_r:
                #    snake_dir, food, dead = down, None, False
                #    snake = [pygame.Rect(10, 10 + value * 10, 10, 10)
                #         for value in range(20)]
                #    foreground, background = (255, 255, 255), (0, 0, 0)
                    
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

            
    screen.fill(background)
    obj=mainMenu.updateState()
    if mainMenu.state=='game':
        if obj==-1 :
                print "gameOver state begins"
                mainMenu.changeState('gameOver')
        print "THIS IS BEFORE THE LOOP",obj[0]
        print "THIS IS THE VALUE OF SNAKE.POINTS",mainMenu.gameMap.snake.points
        print "len:",len(obj[0])
        for i in range(2) :
            if i==0:
                for j in range(len(obj[0])-1):
                    print "INSIDE LOOP:",j," ::: ",obj[0][j]
                    pygame.draw.rect(screen,foreground,obj[0][j])
            else : pygame.draw.rect(screen,foreground,obj[1])
            #surface = font.render(str(len(snake)), True, foreground)
            #screen.blit(surface, (460, 0))
        pygame.display.flip()
                
            
