import pygame
import constants

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen):
        pygame.draw.rect(screen, constants.WHITE, (self.x, self.y, self.width, self.height))
        
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(self.text, True, constants.BLACK, None)
        screen.blit(text, (self.x, self.y))
    
    def isBeingClicked(self):
        mouse = pygame.mouse.get_pos()
        
        if self.isClickInTheButton(mouse[0], mouse[1]):
            print(self.text + " Pressed")
    
    def isClickInTheButton(self, mouseX, mouseY):
        if self.x < mouseX < self.x + self.width:
            if self.y < mouseY < self.y + self.height:
                return True
        
        return False