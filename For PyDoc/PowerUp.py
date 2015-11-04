import pygame
import random

class PowerUp:
    
    def __init__(self):
        
        self.position = pygame.Rect(random.randrange(55) * 10, random.randrange(45) * 10, 10, 10)



