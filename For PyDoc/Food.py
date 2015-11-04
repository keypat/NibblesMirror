import pygame
import random

class Food:
    
    def __init__(self):
        
        self.position = pygame.Rect(random.randrange(55) * 10, random.randrange(48) * 10 + 20, 10, 10)


