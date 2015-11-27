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

        #width of block
        int block_width = 10

        #length of block
        int block_length = 10

        #scale factor to multiply by the randomly generated number to appear on screen.
        int scale_factor = 10

        #offset to skip the header (which contains score)
        int offset = 20

        #randomly generate the a y position on the screen to display the food
        int x_val = random.randrange(55)

        #randomly generate the an x position on the screen to display the food
        int y_val = random.randrange(48)

        #position has x and y values.
        self.position = pygame.Rect(x_val * scale_factor, y_val * scale_factor + offset, block_width, block_length)


