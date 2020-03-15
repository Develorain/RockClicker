import pygame

class Screen:
    def __init__(self, display):
        self.display = display

         # List holds all the components of the screen (buttons, text, etc)
        self.components = []
    
    def draw(self):
        for component in self.components:
            component.draw(self.display)