import constants
import pygame
import os.path

from os import path
from button import Button
from screen import Screen
from state import State
from text import Text

class MainScreen(Screen):
    def __init__(self, display, profile1, profile2):
        Screen.__init__(self, display)
        
        self.profile1 = profile1
        self.profile2 = profile2

        self.initComponents()
        self.attachComponents()
    
    # Create the components of the main screen
    def initComponents(self):
        # Labels
        self.titleText = Text("Rock Clicker", 310, 150, constants.WHITE, "Arial-Bold", 50)

        # Buttons
        self.startButton = Button("Start", 360, 225, 100, 50)
        self.detectButton = Button("Detect", 360, 300, 100, 50)
        self.quitButton = Button("Quit", 360, 375, 100, 50)
    
    # Attach the created components to the screen
    def attachComponents(self):
        # Labels
        self.components.append(self.titleText)

        # Buttons
        self.components.append(self.startButton)
        self.components.append(self.detectButton)
        self.components.append(self.quitButton)
    
    def checkForComponentClicks(self):
        if self.startButton.isBeingClicked() == True:
            self.profile1.state = State.GAME_SCREEN
            self.profile2.state = State.GAME_SCREEN

        if self.detectButton.isBeingClicked() == True:
            if path.exists(constants.SECONDARY_FILE_NAME) and constants.MULTIPLAYER == False:
                # Increase screen size
                display = pygame.display.set_mode((constants.SCREEN_WIDTH * 2, constants.SCREEN_HEIGHT))

                # Reposition components
                for component in self.components:
                    component.setX(component.getX() * 2 - component.width/2)

                constants.MULTIPLAYER = True
        
        if self.quitButton.isBeingClicked() == True:
            print("Game should close now!")
            raise SystemExit