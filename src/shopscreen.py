import constants

from button import Button
from text import Text
from screen import Screen
from state import State

class ShopScreen(Screen):
    def __init__(self, display, gemsAndUpgrades):
        Screen.__init__(self, display)
        
        # Give screen access to gems and upgrades
        self.gemsAndUpgrades = gemsAndUpgrades

        self.init()
    
    def init(self):
        # Create the components of the main screen
        self.upgradeButton1 = Button("Upgrade 1", 350, 150, 100, 50)
        self.upgradeButton2 = Button("Upgrade 2", 350, 225, 100, 50)
        self.upgradeButton3 = Button("Upgrade 3", 350, 300, 100, 50)
        self.upgradeButton4 = Button("Upgrade 4", 350, 375, 100, 50)
        self.backButton = Button("Back", 700, 550, 100, 50)
        self.gemLabel = Text("Gem:", 10, 550, constants.WHITE, "Arial", 30)
        self.gemText = Text(str(self.gemsAndUpgrades.getGemCount()), 90, 550, constants.WHITE, "Arial", 30)

        # Add components to components list
        self.components.append(self.upgradeButton1)
        self.components.append(self.upgradeButton2)
        self.components.append(self.upgradeButton3)
        self.components.append(self.upgradeButton4)
        self.components.append(self.backButton)
        self.components.append(self.gemLabel)
        self.components.append(self.gemText)

    def update(self, deltaTime):
        self.gemsAndUpgrades.handlePassive(deltaTime)

        self.gemText.update(str(self.gemsAndUpgrades.getGemCount()))
    
    def checkForComponentClicks(self, state):
        if self.upgradeButton1.isBeingClicked(state) == True:
            self.gemsAndUpgrades.upgradeIncrementAmount()
        elif self.upgradeButton2.isBeingClicked(state) == True:
            self.gemsAndUpgrades.upgradePassiveIncrementAmount()
        elif self.upgradeButton3.isBeingClicked(state) == True:
            print("Button 3 Pressed")
        elif self.upgradeButton4.isBeingClicked(state) == True:
            print("Button 4 Pressed")
        elif self.backButton.isBeingClicked(state) == True:
            state = State.GAME_SCREEN

        return state