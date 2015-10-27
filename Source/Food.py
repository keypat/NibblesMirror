import pygame
import random

class Food:
    
    def __init__(self):
        
        self.position = pygame.Rect(random.randrange(50) * 10, random.randrange(50) * 10, 10, 10)


