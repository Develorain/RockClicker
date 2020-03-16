import pygame
import constants

from state import State
from text import Text

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = Text(text, x,  y, constants.BLACK, "Arial", 20)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, display):
        pygame.draw.rect(display, constants.WHITE, (self.x, self.y, self.width, self.height))
        self.text.draw(display)
    
    def isBeingClicked(self, state):
        mouse = pygame.mouse.get_pos()
        
        if self.isClickInTheButton(mouse[0], mouse[1]):
            print(self.text.getText() + " Pressed")
            return True
        
        return state
    
    def isClickInTheButton(self, mouseX, mouseY):
        if self.x < mouseX < self.x + self.width:
            if self.y < mouseY < self.y + self.height:
                return True
        
        return False