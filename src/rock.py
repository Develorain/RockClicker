import pygame
import constants

class Rock:
    MAX_SIZE = 150
    MIN_SIZE = 50
    GROWTH_AMOUNT = 5
    SHRINK_AMOUNT = 5
    TIMER = 1000  #1000 milliseconds before the rock shrinks

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.timeSinceLastClicked = 0
    
    def update(self, deltaTime):
        self.timeSinceLastClicked = self.timeSinceLastClicked + deltaTime

        if self.timeSinceLastClicked > self.TIMER:
            self.shrink()
            self.timeSinceLastClicked = 0

    def grow(self):
        # Reset timer when growing
        self.timeSinceLastClicked = 0

        # Grow if there is still room to grow when pressed
        if self.width <= self.MAX_SIZE:
            self.width = self.width + self.GROWTH_AMOUNT
            self.height = self.height + self.GROWTH_AMOUNT
    
    def shrink(self):
        if self.width >= self.MIN_SIZE:
            self.width = self.width - self.SHRINK_AMOUNT
            self.height = self.height - self.SHRINK_AMOUNT

    def draw(self, screen):
        pygame.draw.rect(screen, constants.WHITE, (constants.CENTER_SCREEN_X - (self.width / 2), constants.CENTER_SCREEN_Y - (self.height / 2), self.width, self.height))

    def isBeingClicked(self):
        mouse = pygame.mouse.get_pos()

        if self.isClickInTheRock(mouse[0], mouse[1]):
            self.grow()

            return True
        
        return False

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