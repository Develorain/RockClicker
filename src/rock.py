import pygame
import constants

class Rock:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gemCount = 0

    def draw(self, screen):
        pygame.draw.rect(screen, constants.WHITE, (constants.CENTER_SCREEN_X - (self.width / 2), constants.CENTER_SCREEN_Y - (self.height / 2), self.width, self.height))

    def isBeingClicked(self):
        mouse = pygame.mouse.get_pos()

        if self.isClickInTheRock(mouse[0], mouse[1]):
            self.gemCount = self.gemCount + 1
            print("Pressed rock!")

    def isClickInTheRock(self, mouseX, mouseY):
        # Determines if the click is actually within the bounds of the rock
        if self.x - self.width / 2 < mouseX < self.x + self.width / 2:
            if self.y - self.height / 2 < mouseY < self.y + self.height / 2:
                return True
        
        return False

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        
    def getGemCount(self):
        return self.gemCount

    def getGemCountAsString(self):
        return str(self.gemCount)