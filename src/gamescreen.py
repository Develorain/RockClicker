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
        self.gemText = Text("Gems: " + self.rock.getGemCountAsString(), 10, 550, constants.WHITE, "Arial", 30)

        # Add components to components list
        self.components.append(self.rock)
        self.components.append(self.shopButton)
        self.components.append(self.gemText)
    
    def checkForComponentClicks(self, state):
        self.rock.isBeingClicked()
        state = self.shopButton.isBeingClicked(state)

        return state