import pygame
from pygame.locals import KEYDOWN, K_UP, K_RIGHT, K_DOWN, K_LEFT, QUIT, K_r, K_q

event = pygame.event.poll()

def controller(event):
        if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_UP and snake_dir != down:
            snake_dir = up
        elif event.key == K_RIGHT and snake_dir != left:
            snake_dir = right
        elif event.key == K_DOWN and snake_dir != up:
            snake_dir = down
        elif event.key == K_LEFT and snake_dir != right:
            snake_dir = left
        elif event.key == K_r:
            snake_dir, food, dead = down, None, False
            snake = [pygame.Rect(10, 10 + value * 10, 10, 10)
                     for value in range(20)]
            foreground, background = (255, 255, 255), (0, 0, 0)
        elif event.key == K_q:
            pygame.event.post(pygame.event.Event(QUIT))

    if dead:
        continue

        
