import pygame
import constants

class Text:
    def __init__(self, text, x, y, colour, font, fontSize, isForAButton=False, width=0, height=0):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isForAButton = isForAButton
        self.colour = colour
        self.font = font
        self.fontSize = fontSize
    
    def update(self, text):
        self.text = text
    
    # Draws text that never changes once it is displayed on display
    def draw(self, display):
        font = pygame.font.SysFont(self.font, self.fontSize)
        textSurface = font.render(self.text, True, self.colour, None)

        if self.isForAButton:
            textRect = textSurface.get_rect()
            textRect.center = (self.x + self.width / 2, self.y + self.height / 2)
            display.blit(textSurface, textRect)
        else:
            display.blit(textSurface, (self.x, self.y))
    
    def getText(self):
        return self.text
    
    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x