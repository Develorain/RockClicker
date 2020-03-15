import constants

from rock import Rock
from button import Button
from text import Text

class GameScreen():
    def __init__(self, display):
        self.display = display

        # All the components of the screen
        self.rock = Rock(constants.CENTER_SCREEN_X, constants.CENTER_SCREEN_Y, 100, 100)
        self.shopButton = Button("Shop", 700, 550, 100, 50)
        self.gemText = Text("Gems: " + self.rock.getGemCountAsString(), 10, 550, constants.WHITE, "Arial", 30)

        self.components = []
        self.components.append(self.rock)
        self.components.append(self.shopButton)
        self.components.append(self.gemText)

    def draw(self):
        for component in self.components:
            component.draw(self.display)
    
    def checkForClicks(self, state):
        self.rock.isBeingClicked()
        state = self.shopButton.isBeingClicked(state)

        return state