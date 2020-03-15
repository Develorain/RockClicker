import constants

from button import Button
from text import Text

class ShopScreen():
    def __init__(self, display):
        self.display = display

        # All the components of the screen
        self.upgradeButton1 = Button("Upgrade 1", 350, 125, 100, 50)
        self.upgradeButton2 = Button("Upgrade 2", 350, 200, 100, 50)
        self.upgradeButton3 = Button("Upgrade 3", 350, 275, 100, 50)
        self.upgradeButton4 = Button("Upgrade 4", 350, 350, 100, 50)
        self.backButton = Button("Back", 700, 550, 100, 50)

        # Add components to a list
        self.components = []
        self.components.append(self.upgradeButton1)
        self.components.append(self.upgradeButton2)
        self.components.append(self.upgradeButton3)
        self.components.append(self.upgradeButton4)
        self.components.append(self.backButton)

    def draw(self):
        for component in self.components:
            component.draw(self.display)
    
    def checkForClicks(self, state):
        self.upgradeButton1.isBeingClicked(state)
        self.upgradeButton2.isBeingClicked(state)
        self.upgradeButton3.isBeingClicked(state)
        self.upgradeButton4.isBeingClicked(state)
        state = self.backButton.isBeingClicked(state)

        return state