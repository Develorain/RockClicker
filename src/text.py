import pygame
import constants

class Text:
    def __init__(self, text, x, y, colour, font, fontSize):
        self.text = text
        self.x = x
        self.y = y
        self.colour = colour
        self.font = font
        self.fontSize = fontSize

    # Draws text that might change while on display
    def drawDynamic(self, display, text):
        font = pygame.font.SysFont(self.font, self.fontSize)
        abc = font.render(text, True, self.colour, None)
        display.blit(abc, (self.x, self.y))
    
    # Draws text that never changes once it is displayed on display
    def draw(self, display):
        font = pygame.font.SysFont(self.font, self.fontSize)
        text = font.render(self.text, True, self.colour, None)
        display.blit(text, (self.x, self.y))
    
    def getText(self):
        return self.text