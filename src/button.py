import pygame
import constants

from state import State
from text import Text

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = Text(text, x,  y, constants.BLACK, "Arial", 20, True, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, display):
        pygame.draw.rect(display, constants.WHITE, (self.x, self.y, self.width, self.height))
        self.text.draw(display)
    
    def isBeingClicked(self):
        mouse = pygame.mouse.get_pos()
        
        if self.isClickInTheButton(mouse[0], mouse[1]):
            return True
        
        return False
    
    def isClickInTheButton(self, mouseX, mouseY):
        if self.x < mouseX < self.x + self.width:
            if self.y < mouseY < self.y + self.height:
                return True
        
        return False
    
    def getX(self):
        return self.x
    
    def setX(self, x):
        # Set button x
        self.x = x

        # Set text x
        self.text.setX(self.x)