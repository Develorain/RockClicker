import constants

from rock import Rock
from button import Button
from text import Text
from screen import Screen

class GameScreen(Screen):
    def __init__(self, display):
        Screen.__init__(self, display)

        # Create the componenets of the game screen
        self.rock = Rock(constants.CENTER_SCREEN_X, constants.CENTER_SCREEN_Y, 100, 100)
        self.shopButton = Button("Shop", 700, 550, 100, 50)
        self.gemCount = 0
        self.gemLabel = Text("Gem:", 10, 550, constants.WHITE, "Arial", 30)
        self.gemText = Text(str(self.gemCount), 90, 550, constants.WHITE, "Arial", 30)

        # Add components to components list
        self.components.append(self.rock)
        self.components.append(self.shopButton)
        self.components.append(self.gemLabel)
        self.components.append(self.gemText)
    
    def update(self, deltaTime):
        self.rock.update(deltaTime)
        self.gemText.update(str(self.gemCount))
    
    def checkForComponentClicks(self, state):
        if self.rock.isBeingClicked():
            self.gemCount = self.gemCount + 1
        
        state = self.shopButton.isBeingClicked(state)

        return state