import pygame
import constants

from state import State

class Rock:
    MAX_SIZE = 150
    MIN_SIZE = 50
    GROWTH_AMOUNT = 5
    SHRINK_AMOUNT = 5
    TIMER = 3000  # milliseconds before the rock shrinks

    def __init__(self, x, y, width, height, profile):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.profile = profile
        self.color = constants.WHITE
        self.timeSinceLastClicked = 0
    
    def update(self, deltaTime):
        self.timeSinceLastClicked = self.timeSinceLastClicked + deltaTime

        print(self.timeSinceLastClicked)

        if self.timeSinceLastClicked > self.TIMER:
            self.shrink()
            self.timeSinceLastClicked = 0
        
        self.profile.health = (self.width - self.MIN_SIZE) / 10

        self.checkColor()
        self.checkIfDead()
        print(self.width)

    def checkColor(self):
        # Determine color of rock based on health
        if self.profile.health > 7.5:
            self.color = constants.WHITE
        elif self.profile.health > 5.5:
            self.color = constants.LIGHT_ORANGE
        elif self.profile.health > 3.5:
            self.color = constants.ORANGE
        elif self.profile.health > 1.5:
            self.color = constants.DARK_ORANGE
        elif self.profile.health > 0.0:
            self.color = constants.RED

    def checkIfDead(self):
        if self.profile.health < 0:
            self.profile.state = State.GAME_OVER_SCREEN

    def grow(self):
        # Reset timer when growing
        self.timeSinceLastClicked = 0

        # Grow if there is still room to grow when pressed
        if self.width < self.MAX_SIZE:
            self.width = self.width + self.GROWTH_AMOUNT
            self.height = self.height + self.GROWTH_AMOUNT
    
    def shrink(self):
        if self.width >= self.MIN_SIZE:
            self.width = self.width - self.SHRINK_AMOUNT
            self.height = self.height - self.SHRINK_AMOUNT

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x - (self.width / 2), self.y - (self.height / 2), self.width, self.height))

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
    
    def setX(self, x):
        self.x = x
    
    def getY(self):
        return self.y

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    