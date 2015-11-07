import pygame
import random


class Food:
    """
    Food class to encapsulate position of food particle
    state variables:
        position: pygame.Rect object
    """
    def __init__(self):
        """
            constructor for Food.py
            
            Transition: initializes a food object with random position
            input:none
            output:none
        """
        self.position = pygame.Rect(random.randrange(55) * 10, random.randrange(48) * 10 + 20, 10, 10)


